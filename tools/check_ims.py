#!/usr/bin/env python3
"""Read-only checks for the four IMS v2.6.1 editions. Standard library only.

Inspect formulas, inputs and saved values without changing a workbook or invoking
Excel. Known defects remain failures. --allow-known-defects only permits the
documented prerelease baseline; it does not mark defective behavior as correct.
"""
import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

M='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
X14='{http://schemas.microsoft.com/office/spreadsheetml/2009/9/main}'
FILES=('IMS-Compass-v2.6.1-EN.xlsx','IMS-Compass-v2.6.1-EN-Clean-Start.xlsx',
       'IMS-Kompass-v2.6.1.xlsx','IMS-Kompass-v2.6.1-Leerstart.xlsx')
EN=('Setup','Instructions','StatusGlossary','ISMS-Foundations','AI-Supplements',
    'Governance','Home','JobAid','ReleaseChecks','Overview','Report','Actions',
    'Checks','Implementations','Risks','Safeguards','Decisions','Issues',
    'Obligations','Objectives','StandardView','TargetCoverage','Assessments',
    'Coverage','CoverageRules','Scope','Objects','Controls','Requirements',
    'Mappings','MasterData','Documents','ChangeLog','TaskBase')
DE=('Aufbau','Anleitung','Statusglossar','ISMS-Grundlagen','KI-Ergänzungen',
    'Informationsführung','Start','Arbeitshilfe','Freigabetests','Übersicht',
    'Bericht','Maßnahmen','Prüfungen','Umsetzungen','Risiken','Sicherungen',
    'Entscheidungen','Vorgänge','Betriebspflichten','Ziele','Normsicht',
    'Sollabdeckung','Beurteilungen','Deckung','Deckungsregeln','Geltung',
    'Objekte','Kontrollen','Anforderungen','Normbezug','Stammdaten',
    'Dokumente','Änderungen','Aufgabenbasis')
WORDS={
'EN':dict(yes='Yes',released='Released',all_modes='All modes',control='Reference control',
          internal='Internal requirement',open='Open',still_open='Still open',
          not_used='Not used',effective='Effectively closed',incomplete='Closure incomplete',
          confirmed='Closure confirmed',zero='Target value reached',blank='Measurement open'),
'DE':dict(yes='Ja',released='Freigegeben',all_modes='Alle Modi',control='Referenzkontrolle',
          internal='Interne Anforderung',open='Offen',still_open='Noch offen',
          not_used='Nicht verwendet',effective='Wirksam abgeschlossen',incomplete='Abschluss unvollständig',
          confirmed='Abschluss bestätigt',zero='Zielwert erreicht',blank='Messung offen')}

def read_xlsx(path):
    sheets={};standard=extended=0
    with ZipFile(path) as z:
        if z.testzip() is not None:raise ValueError('ZIP checksum failure')
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            strings=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        for s in ET.fromstring(z.read('xl/workbook.xml')).find(M+'sheets'):
            target=rels[s.get(R+'id')]
            target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            tree=ET.fromstring(z.read(target));cells={}
            standard+=len(tree.findall(M+'dataValidations/'+M+'dataValidation'))
            extended+=sum(1 for _ in tree.iter(X14+'dataValidation'))
            for c in tree.iter(M+'c'):
                v=c.find(M+'v');f=c.find(M+'f');raw=v.text if v is not None else None;typ=c.get('t')
                if typ=='s':value=strings[int(raw)] if raw is not None else ''
                elif typ=='inlineStr':value=''.join(c.find(M+'is').itertext())
                elif typ in ('n',None) and raw is not None:
                    try:value=float(raw)
                    except ValueError:value=raw
                elif typ=='b':value=raw=='1'
                else:value='' if raw is None else raw
                if f is not None or value!='':
                    cells[c.get('r')]={'value':value,'has_formula':f is not None,
                                      'formula':f.text if f is not None else None,'error':typ=='e'}
            sheets[s.get('name')]=cells
        title=ET.fromstring(z.read('docProps/core.xml')).findtext('{http://purl.org/dc/elements/1.1/}title','')
        return dict(sheets=sheets,standard_validations=standard,extended_validations=extended,title=title,
                    vba=any('vbaProject' in p for p in z.namelist()),
                    external_workbooks=any(p.startswith('xl/externalLinks/') for p in z.namelist()))

def run(path):
    data=read_xlsx(path);book=data['sheets'];lang='EN' if 'Setup' in book else 'DE'
    names=dict(zip(EN,EN if lang=='EN' else DE));w=WORDS[lang]
    clean='Clean-Start' in path.name or 'Leerstart' in path.name;checks=[]
    def add(id_,description,passed,actual,expected,known=False):
        checks.append(dict(id=id_,description=description,passed=bool(passed),
                           known_defect=bool(known and not passed),actual=actual,expected=expected))
    def cell(s,a):return book[names[s]].get(a,{})
    def val(s,a):return cell(s,a).get('value','')
    def rows(s,c,lo,hi):return [(r,val(s,c+str(r))) for r in range(lo,hi+1) if val(s,c+str(r))!='']
    def find(s,id_,lo,hi):
        found=[r for r,v in rows(s,'A',lo,hi) if v==id_]
        return found[0] if len(found)==1 else None
    errors=[s+'!'+a+' '+str(c['value']) for s,cs in book.items() for a,c in cs.items() if c['error']]
    add('file_no_cached_errors','No saved Excel error cells',not errors,errors,[])
    deps={k:data[k] for k in ('vba','external_workbooks')}
    add('file_no_vba_external_workbooks','No VBA or external-workbook dependency',not any(deps.values()),deps,dict(vba=False,external_workbooks=False))
    add('version_metadata','Core title identifies v2.6.1','2.6.1' in data['title'],data['title'],'v2.6.1')
    dvs=dict(standard=data['standard_validations'],extended=data['extended_validations'])
    add('validation_definitions_retained','Standard and extended validation definitions are retained',dvs==dict(standard=101,extended=71),dvs,dict(standard=101,extended=71))
    for id_,s,col,lo,hi in [('object_validation_live','Objects','K',8,82),
                            ('coverage_rule_validation_live','CoverageRules','I',8,157),
                            ('coverage_validation_live','Coverage','L',8,1007)]:
        missing=[col+str(r) for r in range(lo,hi+1) if not cell(s,col+str(r)).get('has_formula')]
        add(id_,'Prepared input-validation cells contain live formulas: '+names[s],not missing,
            dict(sheet=names[s],count_without_formula=len(missing),first_cells=missing[:15]),
            dict(count_without_formula=0),True)
    # Reconcile the supplied active-rule state from raw IDs, dates, types and modes.
    date=val('Setup','C5');members=[]
    for r,_ in rows('Scope','A',25,174):
        ms=val('Scope',f'B{r}');obj=val('Scope',f'C{r}')
        mr=find('Scope',ms,8,17);orr=find('Objects',obj,8,82)
        if mr is None or orr is None:continue
        dates=[val('Scope',f'F{r}'),val('Scope',f'G{r}'),val('Scope',f'I{mr}'),val('Scope',f'J{mr}')]
        if not all(isinstance(v,(int,float)) for v in dates+[date]):continue
        if val('Scope',f'D{r}')=='In Scope' and val('Scope',f'H{mr}')==w['released'] and dates[0]<=date<=dates[1] and dates[2]<=date<=dates[3]:
            members.append((ms,obj,val('Objects',f'C{orr}'),val('Objects',f'Y{orr}')))
    expected_rules={};mismatches=[];missing_targets=[]
    for r,id_ in rows('CoverageRules','A',8,157):
        if val('CoverageRules',f'I{r}')!='OK' or val('CoverageRules',f'F{r}')!=w['yes']:continue
        ms=val('CoverageRules',f'B{r}');typ=val('CoverageRules',f'D{r}');mode=val('CoverageRules',f'O{r}')
        targets=sorted({obj for m,obj,t,om in members if m==ms and t==typ and (mode==w['all_modes'] or mode==om)})
        expected_rules[id_]=targets
        if val('CoverageRules',f'J{r}')!=len(targets):
            mismatches.append(dict(cell=f'J{r}',rule=id_,actual=val('CoverageRules',f'J{r}'),expected=len(targets)))
        covered={val('Coverage',f'C{cr}') for cr,_ in rows('Coverage','A',8,1007) if val('Coverage',f'B{cr}')==id_ and val('Coverage',f'L{cr}')=='OK'}
        missing_targets.extend(dict(rule=id_,object=obj) for obj in targets if obj not in covered)
    total=sum(map(len,expected_rules.values()))
    add('coverage_target_counts','Saved active-rule counts reconcile with current raw membership',not mismatches and val('Overview','G13')==total,dict(total=val('Overview','G13'),mismatches=mismatches),dict(total=total))
    add('coverage_missing_assignments','Saved missing-coverage total reconciles with supplied records',val('Overview','C15')==len(missing_targets),val('Overview','C15'),dict(count=len(missing_targets),missing=missing_targets))
    displayed=sorted({val('TargetCoverage',f'C{r}') for r in range(8,158) if val('TargetCoverage',f'G{r}')==w['yes']})
    expected=expected_rules.get(val('TargetCoverage','B4'),[])
    add('selected_target_view','Selected rule exposes its expected object set',displayed==expected,displayed,expected)
    std=val('Report','C4')
    count=sum(val('Requirements',f'C{r}')==std and val('Requirements',f'B{r}') in (w['control'],w['internal']) for r in range(8,308))
    add('report_control_count','Report control count matches selected catalogue',val('Report','C10')==count,val('Report','C10'),count)
    topic_count=open_count=0;bad=[]
    for s in ('ISMS-Foundations','AI-Supplements'):
        for a,c in book[names[s]].items():
            match=re.search(r'IF\((C\d+)="'+re.escape(w['open'])+'","'+re.escape(w['still_open'])+'"',c.get('formula') or '')
            if match:
                topic_count+=1
                if val(s,match.group(1))==w['open']:
                    open_count+=1
                    if c['value']!=w['still_open']:bad.append(names[s]+'!'+a)
    actual=dict(formulas=topic_count,open_topics=open_count,bad_cells=bad)
    expected=dict(formulas=65,open_topics=65 if clean else 63,bad_cells=[])
    add('foundation_open_status','All 65 topic formulas recognize the localized Open selection',actual==expected,actual,expected)
    if lang=='EN':
        obsolete={'Ja','Nein','Offen','Referenzkontrolle','Interne Anforderung','Arbeitshilfe','Kennzahlen','Beurteilen','Neue Zeile: MS ','Sehr hoch','Hierarchiezyklus','Register voll'}
        hits=[s+'!'+a for s,cs in book.items() for a,c in cs.items() if obsolete.intersection(re.findall(r'"((?:[^"]|"")*)"',c.get('formula') or ''))]
        add('english_formula_literals','Previously identified untranslated formula literals are absent',not hits,hits,[])
    missing=[]
    for r,fields in ((9,('F16','C19','C20','C22','C23')),(10,('F30','C33','C34','C36','C37'))):
        f=cell('Governance',f'L{r}').get('formula') or ''
        for field in fields:
            if not re.search(r'COUNTIFS\([^\)]*,'+field+r'\)=1',f):missing.append(names['Governance']+f'!L{r}:'+field)
    add('governance_reference_ids','Both governance rows validate five unique referenced IDs',not missing,missing,[])
    procedure=str(val('ReleaseChecks','C14'));proof=str(val('ReleaseChecks','E14'))
    correct=all(x in procedure for x in ('Z-002','Z-004')) and all(x in proof for x in ('P10','P11'))
    add('release_zero_example_references','Embedded zero/blank test identifies actual demo examples',correct,dict(procedure=procedure,proof=proof),dict(records=['Z-002','Z-004'],proof_cells=['P10','P11']),True)
    match=re.search(r'(\d+) (?:open tasks|offene Aufgaben)',str(val('ReleaseChecks','D15')))
    written=int(match.group(1)) if match else None
    add('release_task_count_matches_edition','Embedded task-count expectation applies to this edition',val('Home','M4')==written,dict(actual=val('Home','M4'),written_expectation=written),'Current edition-specific expectation',clean)
    if not clean:
        for id_,want in [('M-005',w['effective']),('M-007',w['effective']),('M-002',w['incomplete'])]:
            r=find('Actions',id_,8,207);got=val('Actions',f'V{r}') if r else 'ID missing or duplicate'
            add('example_'+id_.lower(),id_+' closure result',got==want,got,want)
        r=find('Issues','V-007',8,207);got=val('Issues',f'P{r}') if r else 'ID missing or duplicate'
        add('example_finding_closure','Matching V-007 finding closure',got==w['confirmed'],got,w['confirmed'])
        zr=find('Objectives','Z-002',8,87);br=find('Objectives','Z-004',8,87)
        got=dict(zero=val('Objectives',f'P{zr}'),blank=val('Objectives',f'P{br}'));want=dict(zero=w['zero'],blank=w['blank'])
        add('zero_vs_blank_measurement','Measured zero differs from absent measurement',got==want,got,want)
    else:
        ranges=[('Actions',8,207),('Checks',8,507),('Implementations',8,207),('Risks',8,127),('Safeguards',8,157),('Decisions',8,157),('Issues',8,207),('Obligations',8,127),('Objectives',8,87),('Assessments',8,307),('Coverage',8,1007),('CoverageRules',8,157),('Objects',8,82),('Mappings',8,407),('Scope',8,17),('Scope',25,174),('MasterData',35,74),('MasterData',99,158)]
        retained={names[s]+f'!A{lo}:A{hi}':rows(s,'A',lo,hi) for s,lo,hi in ranges if rows(s,'A',lo,hi)}
        add('clean_operational_ids_cleared','Core operational, scope, person and mandate IDs are cleared',not retained,retained,{})
        count=len(rows('Requirements','A',8,200))
        add('clean_reference_catalogue_retained','193 external catalogue entries remain',count==193,count,193)
        bad=[]
        for r,id_ in rows('Documents','A',8,507):
            for col,target,lo,hi in [('C','Objects',8,82),('F','MasterData',35,74)]:
                ref=val('Documents',f'{col}{r}')
                if find(target,ref,lo,hi) is None:bad.append(dict(cell=names['Documents']+f'!{col}{r}',document=id_,unresolved=ref))
        add('clean_document_references_resolve','Retained document object/person references resolve',not bad,bad,[],True)
        bad=[]
        for r,id_ in rows('MasterData','A',82,91):
            ref=val('MasterData',f'L{r}')
            if find('Documents',ref,8,507) is None:bad.append(dict(cell=names['MasterData']+f'!L{r}',method=id_,unresolved=ref))
        add('clean_method_reference_resolves','Retained example method document reference resolves',not bad,bad,[],True)
        got=[val('Governance','L9'),val('Governance','L10')];want=[w['not_used']]*2
        add('clean_governance_unused','No scope produces no claimed governance definition',got==want,got,want)
        add('clean_home_empty','Clean operational task count is zero',val('Home','M4')==0,val('Home','M4'),0)
    return dict(file=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),language=lang,
                edition='clean-start' if clean else 'demonstration',
                formula_cells=sum(c['has_formula'] for cs in book.values() for c in cs.values()),
                passed=sum(c['passed'] for c in checks),failed=sum(not c['passed'] for c in checks),
                known_failures=sum(c['known_defect'] for c in checks),checks=checks)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('workbook',type=Path,nargs='?',help='One edition; default checks all four.')
    p.add_argument('--workbook-dir',type=Path,default=Path(__file__).resolve().parents[1]/'workbooks')
    p.add_argument('--report',type=Path)
    p.add_argument('--allow-known-defects',action='store_true')
    args=p.parse_args();paths=[args.workbook] if args.workbook else [args.workbook_dir/name for name in FILES]
    files=[run(path) for path in paths]
    report=dict(review_date='2026-10-23',package_version='0.1.0-review.2',
                method='Read-only OOXML inspection, independent input reconciliation and saved-result assertions. No native Excel calculation.',
                passed=sum(f['passed'] for f in files),failed=sum(f['failed'] for f in files),
                known_failures=sum(f['known_failures'] for f in files),files=files)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for f in files:
        print(f"{f['file']}: {f['passed']} passed, {f['failed']} failed ({f['known_failures']} documented)")
        for c in f['checks']:
            if not c['passed']:print('  FAIL '+c['id'])
    print('Saved results and declared expectations do not establish native Excel acceptance.')
    bad=[c for f in files for c in f['checks'] if not c['passed'] and not (args.allow_known_defects and c['known_defect'])]
    return 1 if bad else 0
if __name__=='__main__':sys.exit(main())

