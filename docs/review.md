# Review of IMS v2.6.1

Reviewed on **23 October 2026** for repository package **0.1.0-review.2**. This review covers the English and German demonstrations and their two cleared starting editions. All four source files are retained unchanged; their exact identities are in the [manifest](../validation/manifest.json).

## Conclusion

The update repairs the major English-language calculation defects reported for v2.6. The starting editions now remove the operational demonstration records and retain the calculation/validation infrastructure. Those are substantive improvements.

The first-use and editing workflow still has material gaps. Two entire input-validation columns are stored values, and the first object row has no live validator. A valid new rule can disappear from expected coverage; an invalid changed assignment can remain counted as valid. Governance checks now validate unique referenced IDs, but still treat several unusable linked records as a completed definition.

The files remain a **reviewed prerelease**. This package updates the review and repository materials; it does not repair the uploaded workbooks or claim native Microsoft Excel acceptance.

## What was resolved

| Prior finding | v2.6.1 evidence | Assessment |
| --- | --- | --- |
| IMS-001: English rule-count literal | CoverageRules J8:J157 now tests Yes. The demo reconciles to 13 expected rule–object pairs; REG-004 J11=2 and L11=1. | Literal defect resolved. Live rule validation remains a separate blocker. |
| IMS-002: TargetCoverage Yes/No mismatch | REG-004 exposes S-020 and S-021; changing mode or active flag updates the tested target branches. | Resolved in the tested paths. |
| IMS-003: Report counts German categories in EN | Report C10=93 for N27. Selecting MS-AIMS produces N42 and 40: 38 reference controls plus two internal samples. | Resolved. |
| IMS-004: Open topic selection rejected | All 65 topic-status formulas recognize the local selection. Demo has 63 open topics; clean-start has 65. | Resolved. |
| IMS-009: listed German formula outputs | Previously listed German literals are absent from English formula strings; language-paired formula analysis finds a consistent status vocabulary. | Calculation literals resolved; minor static labels remain. |
| IMS-010: stale core version | All four core titles and descriptions identify v2.6.1 and their edition. | Version metadata repaired. |
| IMS-007: 23-task demo claim | ReleaseChecks / Freigabetests D15 now says 24, matching Home / Start M4 in the demos. | Demo count repaired; zero/blank instructions and clean-edition expectations remain wrong. |
| IMS-008: arbitrary governance IDs accepted | Missing reference IDs and a duplicate responsible ID are rejected; confirmation expiry is detected. | Partial repair; linked-record validity is not propagated. |
| IMS-006: Clean-Start duplicated demo | 1,677 nonempty constants are removed per language, and operational ID registers are cleared. | Reset is materially improved; first-use validation and retained dependencies still need work. |
| IMS-005: fixed Objects K8 | EN clears the value; DE still has the fixed warning. Neither has a formula. | Unresolved. |

The old [v2.6 review](history/0.1.0-review.1/review.md) and its [recorded results](../validation/history/0.1.0-review.1/regression-results.json) remain historical. The old formula proposal is archived and must not be applied indiscriminately to v2.6.1.

## Newly identified inherited validation defects

An independent scan covered **25 validation-output columns and 5,405 prepared cells per file**. There are 4,254 formulas and 1,151 cells without formulas. The other 22 reviewed columns contain formulas throughout. All 26 Excel tables were inspected; none provides a calculated-column-formula fallback.

| English / German range | Missing live formulas | Consequence demonstrated by changed-input tests |
| --- | ---: | --- |
| CoverageRules I8:I157 / Deckungsregeln I8:I157 | 150 | A valid first rule remains blank in validation and reports 0 expected targets and 0 missing assignments instead of 1 each. Duplicate existing rule IDs keep OK. |
| Coverage L8:L1007 / Deckung L8:L1007 | 1,000 | A valid row moved to unused row 21 is omitted. Duplicate records count twice. An absent implementation reference still leaves the assignment counted as valid. |
| Objects K8 / Objekte K8 | 1 | The first complete object cannot establish a current membership; the same input at row 9 works. |

The frozen coverage labels are present in both old v2.6 files as well. These findings expand the earlier audit; they are not introduced by the new upload. See [the column inventory](../validation/validation-column-inventory.json) and the [scenario results](../validation/scenario-results.json).

The clean coverage register retains twelve OK labels and one mode-mismatch label despite having no records. This illustrates why a formula/cache error scan alone is insufficient: a stored label has no calculation to recalculate.

## Governance tests

The optional harness runs eleven governance scenarios per language. Eight pass: a complete reference set, five missing-ID cases, one duplicate-person case and one expired-confirmation case.

Three cases per language fail the desired definition behavior. With complete, unique IDs and valid confirmation dates, the definition remains Defined / Festgelegt when:

- The referenced method has invalid limits and its own M82 status rejects them.
- The referenced mandate names a missing person and its own J99 status rejects it.
- The referenced evidence document is Draft / Entwurf and its own M8 status says not released.

The exact fixture inputs and localized outputs are recorded in the scenario JSON. These are definition-validation failures. The review does not infer that every downstream risk or decision formula has the same bypass.

## Clean-start and language comparison

The cleared editions have no operational IDs in the reviewed action, check, implementation, risk, safeguard, decision, issue, obligation, objective, assessment, coverage, rule, scope, membership, object, mapping, person or mandate ranges. The two sample internal requirements are also removed.

They retain 193 external catalogue entries, six roles, five control building blocks, one unapproved example method, fifteen scales, one workbook-document record and nine template change-log entries. The six fictitious person names from each demo person register are absent from every XML part of its clean edition, including shared strings. This was a targeted residual-name check, not a universal privacy certification.

All 74,555 formula-cell positions, all 172 standard plus extended validation definitions, defined names and sheet-protection settings are retained within each language's demo/clean pair. Only the descriptive Instructions / Anleitung B8 formula changes between starting states.

DOC-MAP still references cleared object S-010 and person PERSON-01. The retained method references removed DOC-METH. Governance B11 still displays MS-AIMS. These dependencies and stale coverage labels explain why a cleared file is not yet an accepted first-use template.

Across languages, **63,568 explicit formula pairs** per starting state have matching normalized calculation structure; shared-formula locations and metadata also match. The analysis identifies 1,124 consistent literal translation pairs. Shared structure does not prove shared logic correct.

One operational numerical difference remains: the input-review count is 4 EN versus 5 DE in the demos and 3 versus 4 in clean-start. The German fixed object warning contributes one; the absent English validation contributes zero. Five other numeric differences concern language-edition change-log timestamps. See [the comparison summary](../validation/edition-comparison.json), [demo pairing](../validation/demo-language-parity.json), [clean pairing](../validation/clean-language-parity.json) and [reset evidence](../validation/reset-scope-evidence.json).

## Verification performed

| Check | Result |
| --- | --- |
| Source inventory, each of four files | 34 sheets, one hidden task sheet, 74,555 formula cells, 26 tables |
| Data validation, each file | 101 standard plus 71 x14 definitions |
| Saved Excel errors, VBA, external-workbook dependencies | None found |
| Portable static/cache assertions | 84 total: 62 pass, 22 documented failures |
| Changed-input source-formula scenarios | 46 total: 26 desired behaviors pass, 20 documented failures, zero evaluator errors |
| Disposable LibreOffice baseline | 298,220 formula-cell values compared across four files; no substantive differences or fresh errors |

The scenario split is explicit: 18 first-record/coverage/zero cases give 4 passes and 14 failures; 22 governance cases give 16 passes and 6 failures; 6 changed locale-sensitive branches all pass. Failures test the intended correct behavior. They are not counted as functionality passes merely because the defect was reproduced.

The baseline recalculation used **LibreOfficeDev 26.8.0.0.alpha0**, build 2c87e51eeaa2b413ff4ae097b2705eea1995d8e5. All 74,555 formula cells remain in each disposable export. There are 12 insignificant timestamp serialization differences in each demo and none in either clean-start. Numeric comparison uses relative tolerance 1e-12 and absolute tolerance 1e-9. Fontconfig reported an unavailable writable cache directory; no visual-rendering claim is made. [Recalculation evidence](../validation/recalculation-results.json) records the method and counts.

The optional evaluator reads source formulas and applies overrides in memory. It uses a bounded function set and is not Excel. No workbook is exported by either IMS test script.

## What remains before a stable release

Restore the three live-validation ranges, check linked governance status, finish clean initialization and correct edition-specific test instructions. Then perform the representative and boundary scenarios in the intended Microsoft Excel version, including input editing, dropdown behavior, recalculation, save/close/reopen and output layout.

Licensing remains unconfirmed. The fixed sample reporting date remains 8 October 2026. Standard conformity, substantive external evidence and empirical risk calibration were not certified. Concrete repair acceptance criteria are in [issues to open](issues-to-open.md).

## Publication preparation addendum — 26 October 2026

A subsequent repository-only inspection found Microsoft Information Protection label records in every supplied Office source in this repository. The identifiers are omitted from the [publication-metadata record](../validation/publication-metadata.json). Their presence alone is not a confidentiality determination. No source Office artifact was modified during this follow-up.

The GitHub workflow now runs both IMS checkers in their explicit known-defect mode and compares the generated reports with the recorded prerelease baseline. The [browser publishing guide](../PUBLISHING.md), [native Excel acceptance record](../validation/native-excel-acceptance.md), and release-evidence checks were added for publication preparation. These changes affect repository scaffolding and documentation; they do not change the functional findings or numerical/workbook baselines recorded above.

## Public-copy preparation and licensing addendum — 27 October 2026

All four public workbooks were cleaned directly at OOXML level. Absolute local paths and `lastModifiedBy` were removed and the Public sensitivity labels were retained. All 34 worksheets per edition, 74,555 formulas per edition and all saved cell values match the original sources. Sheet protection and data validations are unchanged. Regression and scenario baselines are reproduced.

The author selected MIT for the workbooks and Python scripts, and CC BY 4.0 for explanatory documentation, figures, the project mascot and illustrative examples. The root `LICENSE`, `LICENSE-STATUS.md`, `CITATION.cff` and related status records describe this allocation.

The third-party catalogue structure review was completed on 28 October 2026. The 193 references use identifiers, source links and short original topics of 9–47 characters rather than full ISO/IEC requirement text. The `K-...` controls are project-specific building blocks. See [third-party-rights-review.md](../validation/third-party-rights-review.md). The author's license allocation applies only to original material. Current public-copy identities and previous source hashes are recorded in [validation/manifest.json](../validation/manifest.json) and [validation/publication-metadata.json](../validation/publication-metadata.json).

