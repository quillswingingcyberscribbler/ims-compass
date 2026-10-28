#!/usr/bin/env python3
"""Read-only IMS Compass regression checks. Python 3 standard library only.

Reads formulas, supplied values and saved results; never opens, edits or saves
an Excel workbook. These checks are not a substitute for Excel recalculation.
Known defects still fail. --allow-known-defects is for a documented prerelease
baseline and does not turn those failures into passed functionality.
"""
import argparse
import collections
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

M = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

def read_xlsx(path):
    sheets={}
    with ZipFile(path) as z:
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            strings=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels={x.attrib['Id']:x.attrib['Target'] for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        for s in wb.find(M+'sheets'):
            target=rels[s.attrib[R+'id']]
            target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            cells={}
            for c in ET.fromstring(z.read(target)).iter(M+'c'):
                v=c.find(M+'v');f=c.find(M+'f')
                raw=v.text if v is not None else None
                typ=c.attrib.get('t')
                if typ=='s':value=strings[int(raw)] if raw is not None else ''
                elif typ=='inlineStr':value=''.join(c.find(M+'is').itertext())
                elif typ in ('n',None) and raw is not None:
                    try:value=float(raw)
                    except ValueError:value=raw
                else:value='' if raw is None else raw
                if f is not None or value!='':
                    cells[c.attrib['r']]={'value':value,'has_formula':f is not None,'formula':f.text if f is not None else None,'error':typ=='e'}
            sheets[s.attrib['name']]=cells
        macros=any('vbaProject' in p for p in z.namelist())
        external_links=any(p.startswith('xl/externalLinks/') for p in z.namelist())
    return sheets,macros,external_links

def run(path,compare=None):
    book,macros,external_links=read_xlsx(path)
    def val(sheet,address):return book[sheet].get(address,{}).get('value','')
    def rows(sheet,column,start,end):return [(r,val(sheet,column+str(r))) for r in range(start,end+1) if val(sheet,column+str(r))!='']
    def row_for(sheet,id_,start,end):
        found=[r for r,v in rows(sheet,'A',start,end) if v==id_]
        return found[0] if len(found)==1 else None
    results=[]
    def check(id_,description,passed,actual,expected,known=False):
        results.append({'id':id_,'description':description,'passed':bool(passed),'known_defect':bool(known and not passed),'actual':actual,'expected':expected})
    errors=[s+'!'+a+' '+str(c['value']) for s,cs in book.items() for a,c in cs.items() if c['error']]
    check('file_no_cached_errors','Saved formula-error cells',not errors,errors,[])
    check('file_no_macro_or_external_workbook','No VBA or external-workbook dependencies',not macros and not external_links,{'vba':macros,'external_workbooks':external_links},{'vba':False,'external_workbooks':False})
    # Independently derive current object membership from the raw scope records.
    date=val('Setup','C5');members=[]
    for r,_ in rows('Scope','A',25,174):
        ms=val('Scope',f'B{r}');obj=val('Scope',f'C{r}')
        mr=row_for('Scope',ms,8,17);orr=row_for('Objects',obj,8,82)
        if mr is None or orr is None:continue
        dates=[val('Scope',f'F{r}'),val('Scope',f'G{r}'),val('Scope',f'I{mr}'),val('Scope',f'J{mr}')]
        if not all(isinstance(v,(int,float)) for v in dates+[date]):continue
        if val('Scope',f'D{r}')=='In Scope' and val('Scope',f'H{mr}')=='Released' and dates[0]<=date<=dates[1] and dates[2]<=date<=dates[3]:
            members.append((ms,obj,val('Objects',f'C{orr}'),val('Objects',f'Y{orr}')))
    rule_expected={};rule_mismatches=[];expected_missing=[]
    for r,id_ in rows('CoverageRules','A',8,157):
        if val('CoverageRules',f'I{r}')!='OK' or val('CoverageRules',f'F{r}')!='Yes':continue
        ms=val('CoverageRules',f'B{r}');typ=val('CoverageRules',f'D{r}');mode=val('CoverageRules',f'O{r}')
        targets=sorted({obj for m,obj,t,om in members if m==ms and t==typ and (mode=='All modes' or mode==om)})
        rule_expected[id_]=targets
        got=val('CoverageRules',f'J{r}')
        if got!=len(targets):rule_mismatches.append({'cell':f'CoverageRules!J{r}','rule':id_,'actual':got,'expected':len(targets),'targets':targets})
        covered={val('Coverage',f'C{cr}') for cr,_ in rows('Coverage','A',8,1007) if val('Coverage',f'B{cr}')==id_ and val('Coverage',f'L{cr}')=='OK'}
        expected_missing.extend({'rule':id_,'object':obj} for obj in targets if obj not in covered)
    total_targets=sum(map(len,rule_expected.values()))
    check('coverage_target_counts','Active rules enumerate the current applicable targets',not rule_mismatches,rule_mismatches,{'total_targets':total_targets},True)
    check('coverage_missing_assignments','Overview includes applicable objects without a valid coverage record',val('Overview','C15')==len(expected_missing),val('Overview','C15'),{'count':len(expected_missing),'missing':expected_missing},True)
    selected=val('TargetCoverage','B4')
    displayed=sorted({val('TargetCoverage',f'C{r}') for r in range(8,158) if val('TargetCoverage',f'G{r}')=='Yes'})
    expected=rule_expected.get(selected,[])
    check('target_coverage_selected_rule','TargetCoverage exposes all expected targets for its selected rule',displayed==expected,displayed,expected,True)
    standard=val('Report','C4')
    count=sum(val('Requirements',f'C{r}')==standard and val('Requirements',f'B{r}') in ('Reference control','Internal requirement') for r in range(8,308))
    check('report_control_count','Report control total agrees with the standard catalogue',val('Report','C10')==count,val('Report','C10'),count,True)
    bad_open=[]
    for sheet in ('ISMS-Foundations','AI-Supplements'):
        for a,c in book[sheet].items():
            f=c.get('formula') or ''
            match=re.search(r'IF\((C\d+)="(?:Offen|Open)","Still open"',f)
            if match and val(sheet,match.group(1))=='Open' and c['value']!='Still open':
                bad_open.append({'input':sheet+'!'+match.group(1),'output':sheet+'!'+a,'actual':c['value']})
    check('open_foundation_status','An Open foundation is reported as Still open',not bad_open,bad_open,[],True)
    hardcoded=[f'Objects!K{r}' for r,_ in rows('Objects','A',8,82) if not book['Objects'].get(f'K{r}',{}).get('has_formula')]
    check('objects_live_validation','Object validation is formula-driven for populated records',not hardcoded,hardcoded,[],True)
    # Preserve successful control examples as useful regression expectations.
    for id_,expected_status in [('M-005','Effectively closed'),('M-007','Effectively closed'),('M-002','Closure incomplete')]:
        row=row_for('Actions',id_,8,207)
        actual=val('Actions',f'V{row}') if row else 'ID missing or duplicate'
        check('example_'+id_.lower(),f'Example {id_} closure result',actual==expected_status,actual,expected_status)
    row=row_for('Issues','V-007',8,207)
    actual=val('Issues',f'P{row}') if row else 'ID missing or duplicate'
    check('example_matching_finding','Matching finding V-007 is accepted as closed',actual=='Closure confirmed',actual,'Closure confirmed')
    zero_row=row_for('Objectives','Z-002',8,87);blank_row=row_for('Objectives','Z-004',8,87)
    actual={'zero':val('Objectives',f'P{zero_row}'),'blank':val('Objectives',f'P{blank_row}')}
    expected={'zero':'Target value reached','blank':'Measurement open'}
    check('zero_vs_blank_measurement','Measured zero and missing measurement remain distinguishable',actual==expected,actual,expected)
    guidance=val('ReleaseChecks','C14')
    proof=val('ReleaseChecks','E14')
    correct_examples='Z-002' in guidance and 'Z-004' in guidance and 'P10' in proof and 'P11' in proof
    check('release_zero_example_references','Embedded zero-versus-blank test points to the actual sample records',correct_examples,{'procedure':guidance,'proof':proof},{'records':['Z-002','Z-004'],'proof_cells':['Objectives!P10','Objectives!P11']},True)
    text=val('ReleaseChecks','D15');match=re.search(r'(\d+) open tasks',text)
    actual=val('Home','M4');expected=int(match.group(1)) if match else None
    check('release_check_task_count','Embedded filter-reset expectation matches the shipped demo',actual==expected,actual,expected,True)
    if compare:
        other,_,_=read_xlsx(compare)
        same=book==other
        check('distinct_clean_start','Clean-Start differs from the worked example at cell-content level',not same,{'identical_cell_contents':same},{'identical_cell_contents':False},True)
    return {'file':Path(path).name,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'method':'Read-only independent input reconciliation plus saved-result checks; no native Excel engine executed by this script.','passed':sum(r['passed'] for r in results),'failed':sum(not r['passed'] for r in results),'known_failures':sum(r['known_defect'] for r in results),'checks':results}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('workbook',type=Path);ap.add_argument('--compare',type=Path)
    ap.add_argument('--report',type=Path);ap.add_argument('--allow-known-defects',action='store_true')
    args=ap.parse_args();result=run(args.workbook,args.compare)
    output=json.dumps(result,ensure_ascii=False,indent=2)
    if args.report:args.report.write_text(output+'\n')
    print(output)
    bad=[c for c in result['checks'] if not c['passed'] and not (args.allow_known_defects and c['known_defect'])]
    return 1 if bad else 0
if __name__=='__main__':sys.exit(main())
