> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

# Known issues

Package `0.1.0-review.1` preserves the supplied v2.6 source workbooks unchanged. The [proposed correction plan](../../../validation/history/0.1.0-review.1/formula-patch-plan.json) has not been applied. The current status is **reviewed prerelease**, with the following release blockers and limitations.

| ID | Priority | Issue | Effect / required next step |
| --- | --- | --- | --- |
| IMS-001 | Blocker | CoverageRules J8:J157 tests `Ja` while the inputs use `Yes` | Expected population is 0 instead of 13; the missing-assignment count is 0 instead of 1. Correct the literal and test active flags and modes. |
| IMS-002 | Blocker | TargetCoverage G8:G157 compares and returns `Ja` / `Nein`; dependents expect `Yes` | Expected targets and missing assignments disappear from the selected-rule view. Correct both comparisons and returned values. |
| IMS-003 | Blocker | Report C10 counts German requirement-type names | The selected N27 control total is 0 instead of 93. Use the actual English catalogue categories. |
| IMS-004 | Blocker | 65 foundational status formulas test `Offen` against `Open` | 63 currently open topics show `Review selection`. Correct the literal without changing source-version checks. |
| IMS-005 | Blocker | Objects K8 is a fixed message | Its validation state never responds to input changes. Restore a live formula and agree how mode validity applies to different object types. |
| IMS-006 | Distribution blocker | Clean-Start is a populated duplicate | Do not distribute it as an empty template. Build and validate a genuine starting edition using the [reset plan](clean-start-plan.md). |
| IMS-007 | Important | Embedded release-test instructions are stale | Correct the task-count expectation and zero-versus-blank sample IDs and proof cells. |
| IMS-008 | Important | Governance L9:L10 checks some reference fields only for nonemptiness | Invalid nonempty IDs can reach `Defined`. Validate the referenced method, authority, person and evidence records and their required status. |
| IMS-009 | Maintenance | English translation is incomplete | The plan contains 849 display-language formula corrections. Static labels also need review; preserve identifiers and matching version strings. |
| IMS-010 | Maintenance | Core metadata still says v2.4-EN | Align metadata and release documentation with the actual candidate version. The source's `Draft for release` status remains appropriate. |
| IMS-011 | Compatibility limit | No native Excel scenario verification was performed in this review | Test the corrected candidate in Microsoft Excel, including save/reopen and native dropdowns. A LibreOffice baseline is supporting evidence only. |
| IMS-012 | Design limit | Register capacities and formula ranges are fixed | Extend tables, formulas, validation, protection and outputs together. A new visible row is not sufficient. |

## What the current results mean

The source workbooks contain no saved Excel error cells or broken-reference errors, and the disposable LibreOffice baseline reproduces their values. That does not make the suppressed counts correct. The defects are logical mismatches inside otherwise executable formulas.

The IMS-specific checker deliberately reports the known defects as failed assertions. Its `--allow-known-defects` option exists to track the unchanged prerelease source alongside a hash manifest. It must not be used to certify a corrected release while blockers remain.

## Date and sample-state limits

The reporting date is 8 October 2026. A result that is valid at that date may be expired today. Change the date in a working copy when performing a new evaluation, and preserve the original sample snapshot for reproducibility.

All operational records are fictitious. Their task counts and closure examples provide useful regression cases, but their specific IDs and expected totals do not apply to another organisation's data.

## Native-feature preservation

The source contains 101 standard validation definitions and 71 additional x14 definitions. A tool that preserves only the ordinary validation list can silently remove important dropdowns. The [extended-validation inventory](../../../validation/history/0.1.0-review.1/extended-validations.json) records the original definitions. It is preservation evidence, not an installation script.

The full [review](review.md) describes the findings and what was actually tested. [Issues to open](issues-to-open.md) provides implementation-ready tasks and acceptance criteria.
