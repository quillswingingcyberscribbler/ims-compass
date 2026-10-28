> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

# Quickstart

## Before opening the workbook

This package is a reviewed prerelease. The source files contain known calculation defects described in [known issues](known-issues.md). Use the supplied records to inspect and develop the model. Resolve the blockers before relying on its coverage and report totals in an operational management system.

Download `the EN workbook` and make a local working copy. Desktop Microsoft Excel is the intended application. No macro execution or connection to an external system is required by the supplied workbook.

The supplied `Clean-Start copy` contains the same demonstration records. Follow the [clean-start plan](clean-start-plan.md) when preparing a future starting edition.

## A useful first visit

1. **Setup.** Check the reporting date in C5. The demo is evaluated as of 8 October 2026. Follow the owner link to Overview and read the draft status and data-state identifier.
2. **ISMS-Foundations.** Inspect the recorded first topic and an open topic. The current English-literal defect makes valid open topics display `Review selection`; the expected status is `Still open`.
3. **AI-Supplements.** Inspect how the existing ISMS definition is adopted, amended or replaced. A checked source version is an explicit saved selection. Changing the source version should require another review.
4. **Governance.** Inspect the choice between internal and external risk management. Both sample selections start open. Direct local risk figures remain explicitly unavailable until the relevant governance is defined.
5. **JobAid.** Follow the evidence and action procedures. Read the required input fields and the resulting status separately.
6. **Home.** Try the person, management-system, task and case filters. Reset the case filter with `All cases`, and return to page 1 after narrowing the selection.

## Trace one complete example

The evidence chain `DOC-RIGHTS → P-007 → U-004` connects the source document, verification record and implementation. P-007 also supports acceptance of action M-007. The supplied action shows `Effectively closed`, and the matching finding V-007 shows `Closure confirmed`.

Compare M-002, which is reported closed in processing but still shows `Closure incomplete`. This demonstrates why a processing label and validated acceptance remain separate.

For measurements, compare **Z-002 at Objectives row 10**, whose actual value is zero, with **Z-004 at row 11**, whose measurement is absent. Their statuses are `Target value reached` and `Measurement open`. The corresponding instructions in ReleaseChecks currently name the wrong sample IDs; use these actual records.

## Read the outputs

**Overview** summarises the recorded state. **StandardView** selects a management system in B4 and shows reference-level judgements. **TargetCoverage** selects a rule in B4 and should expose its expected objects and missing assignments. **Report** presents the working statement of applicability.

Coverage totals and the control count in Report are affected by the known translation defects. After correction, the unchanged demo should show 13 expected rule–object combinations, one missing assignment for REG-004 / S-021, and 93 N27 reference controls. These are regression expectations for the example, not targets for a real organisation.

## Run reproducible checks

From the repository root:

```bash
python3 tools/validate_repository.py --json validation/repository-check-current.json
python3 tools/check_ims.py workbooks/IMS-Compass-v2.6-EN.xlsx --compare workbooks/IMS-Compass-v2.6-Clean-Start.xlsx --report validation/ims-check-current.json
```

The second command returns exit status 1 for the shipped sources because the known defects remain. For a deliberately preserved prerelease baseline, `--allow-known-defects` permits the documented failed assertions while leaving them visibly failed in the report. Use that option only with the unchanged source files and the manifest check. It is not a stable-release approval gate.

Both scripts are read-only with respect to the workbooks. Optional JSON reports are newly written files. The IMS checker assumes the supplied example IDs and is not a general audit of arbitrary organisational data.

## Before an operational release

Apply and review the agreed corrections, preserve all standard and extended Excel validation rules, and run the changed scenarios in Microsoft Excel. Recalculate, save, close and reopen the candidate. Confirm the resulting values and the input workflow, then preserve the exact released file with its reporting date, rule version and data-state identifier.

Keep real evidence, findings and personal assignments in the organisation's controlled working copy rather than committing them to a public repository.
