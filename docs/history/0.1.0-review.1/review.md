> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

# Review of the supplied IMS Compass files

Reviewed on 22 October 2026. Repository package `0.1.0-review.1` contains these unchanged source artifacts:

- `IMS-Compass-v2.6-EN.xlsx`
- `IMS-Compass-v2.6-Clean-Start.xlsx`

## Conclusion

The workbook has a coherent management-system model and useful distinctions between documentary approval, evidence, current operational assurance and historical closure. However, the supplied English edition contains logic errors that suppress coverage gaps and report totals. It is suitable for a documented development prerelease, with corrections required before a stable operational release.

No source workbook was changed. The package supplies a precise proposed formula patch plan and read-only regression checks. A genuine clean-start edition has not been created.

## Scope and method

Both OOXML packages were parsed to inspect worksheet structure, formula records, saved values, defined names, tables, standard and extended validation, external relationships, macro parts and core metadata. The review traced the main output counts to the underlying scope and catalogue records and read the workbook's operating guidance.

Each source contains:

| Feature | Observed count |
| --- | ---: |
| Worksheets | 34 |
| Hidden worksheets | 1, TaskBase |
| Formula cells | 74,547 |
| Excel tables | 26 |
| Standard data-validation definitions | 101 |
| Additional x14 validation definitions | 71 across 19 worksheets |
| Saved Excel error cells | 0 |
| VBA projects | 0 |
| External-workbook link parts | 0 |

The EN workbook was also opened, recalculated and exported into a disposable copy using **LibreOfficeDev 26.8.0.0.alpha0**. The copy retained all 74,547 formula cells and had zero Excel error cells. All meaningful cell results agreed with the source; 25 timestamp values differed only in floating-point serialization. This supports the saved-state findings but does not certify Microsoft Excel or general LibreOffice compatibility.

An attempted read-only Artifact Tool rendering imported the workbook but exceeded the process memory limit before producing previews. This review therefore makes no visual-verification or screenshot claim. The sources remained byte-for-byte unchanged.

## Findings that change results

### Active coverage population is suppressed

`CoverageRules!J8:J157` compares the active flag with `Ja`, while the data and validation use `Yes`. Every active rule therefore takes the zero-count branch.

Independent reconciliation of the current memberships, object types and operating modes yields **13 expected rule–object combinations**. `Overview!G13` reports **0**. REG-004 covers two IT systems, S-020 and S-021. Only S-020 has a valid coverage record, so there is **one missing assignment**; `Overview!C15` reports **0**.

Correct the exact `Ja` literal in these 150 formulas. For the unchanged sample, the acceptance values include `CoverageRules!J11 = 2`, `CoverageRules!L11 = 1`, `Overview!G13 = 13` and `Overview!C15 = 1`.

### The target view has a second language mismatch

`TargetCoverage!G8:G157` both compares the active flag with `Ja` and returns `Ja` or `Nein`. Downstream columns test for `Yes`. Correcting only the comparison would still leave the dependent results wrong.

The selected REG-004 view should identify S-020 and S-021 and show the missing assignment for S-021. The supplied view exposes no expected targets. Replace the exact `Ja` and `Nein` literals with `Yes` and `No` in the 150 affected formulas.

### The report's control total is incorrect

`Report!C10` counts the German categories `Referenzkontrolle` and `Interne Anforderung`, while Requirements uses `Reference control` and `Internal requirement`. The selected N27 catalogue contains 93 reference controls; the report displays zero.

The corrected formula should give 93 for N27. Selecting N42 should give 40 under the formula's existing definition: 38 reference controls plus the two supplied sample internal requirements.

### Open topics are reported as invalid selections

The 30 ISMS status formulas and 35 AI status formulas test `Offen` before entering their invalid-selection branch. The dropdown uses `Open`. As shipped, 29 ISMS topics and 34 AI topics consequently display `Review selection` even though their selection is valid.

All 65 formulas require the exact `Offen` → `Open` correction. The expected open status is `Still open`. The two completed examples are currently unaffected, but their status formulas have the same latent defect.

### One validation cell cannot respond to inputs

`Objects!K8` contains the fixed string `Operating mode missing`. K9:K82 contain formulas. Changing row 8 inputs cannot update K8.

Restore a live validation rule consistently with the other rows. The neighbouring formulas do not currently check operating mode, so simply copying K9 upward also removes the bespoke mode warning. The author needs to decide whether mode is mandatory for every object type and apply that decision consistently.

## The two files are the same populated model

The EN and Clean-Start workbooks have identical values, formulas, cached results and cell style references across all 34 worksheets. Their table and validation parts also match. Only workbook-level XML, the calculation chain and core metadata differ at package level.

Clean-Start therefore retains all demonstration people, objects, assessments, findings, actions, decisions, dates and document references. It should be described as an equivalent populated source copy. The [clean-start plan](clean-start-plan.md) identifies the coordinated reset required for a genuine starting edition.

## Other findings

**Embedded tests.** ReleaseChecks D15 expects 23 open tasks; the supplied Home A6/M4 reports 24. ReleaseChecks C14 names Z-001 and nonexistent Z-00X for a zero-versus-blank example and points to Objectives P8. The actual zero is Z-002 at row 10; the missing measurement is Z-004 at row 11. Their calculated statuses are correct. P8 belongs to Z-003 with an actual value of 12.

**Governance references.** L9:L10 on Governance require method, authority, evidence and person fields to be nonempty, but do not validate all those entered IDs against current source records. Relevant dropdowns do not consistently reject non-list values. Static formula inspection shows that nonempty invalid strings plus valid dates can reach `Defined`. Add referential and status checks before treating this as a reliable approval gate.

**Language.** Additional formula outputs include `Arbeitshilfe`, `Kennzahlen`, `Beurteilen`, `Neue Zeile: MS`, `Sehr hoch`, `Hierarchiezyklus` and `Register voll`. Static labels also remain in German. Translate display text while preserving identifiers and version strings used for matching.

**Metadata.** The core title and description still say v2.4-EN although Overview and the filenames say v2.6-EN. The source remains marked `Draft for release`, with owner `Define before use` and data state `DEMO-2026-10-08`.

**Reporting date.** Setup C5 is fixed at 8 October 2026. The D-003 example expires on 20 October but can correctly appear current in that historical evaluation. The date should be deliberately changed for a new working evaluation, not silently moved in a reproducible demo.

## Behaviours supported by the supplied sample

The saved sample and independent baseline preserve several useful outcomes:

- M-005 and M-007 show `Effectively closed`.
- M-002 remains `Closure incomplete`, despite its reported closed processing state.
- The matching finding V-007 shows `Closure confirmed`.
- Z-002's measured zero is distinct from Z-004's missing measurement.
- Open risk governance produces an explicit `Governance open` state rather than an apparently complete numeric risk total.

These observations support particular sample cases. They are not changed-input tests of every branch or a general certification of the full model.

## Reproducible checks and proposed changes

[check_ims.py](../../../validation/history/0.1.0-review.1/check_ims.py) uses only the Python standard library and never edits the workbook. It independently reconciles current applicable coverage and catalogue counts, checks the sample workflow outcomes, detects fixed object validation and compares the two source copies.

The [recorded results](../../../validation/history/0.1.0-review.1/regression-results.json) contain **16 focused assertions: 7 pass and 9 fail for known defects**. The default command returns a nonzero status while these defects remain. The known-defect option is limited to tracking the unchanged prerelease baseline and does not turn failed assertions into passes.

The [formula patch plan](../../../validation/history/0.1.0-review.1/formula-patch-plan.json) specifies exact old and proposed formulas for **366 functional corrections** and **849 optional English display-language corrections**. It does not apply them. The fixed Objects K8 cell, reset of Clean-Start, governance validation and metadata need separate decisions or edits.

The [extended-validation inventory](../../../validation/history/0.1.0-review.1/extended-validations.json) preserves the original 71 x14 definitions for comparison during an authorised edit. A valid round trip needs to preserve those definitions as well as the 101 standard ones, formulas, protection, tables, navigation and styles.

Native Excel scenario checks, save/reopen verification, substantive evidence review and standard conformity remain pending. The package's next steps are set out in [issues to open](issues-to-open.md).
