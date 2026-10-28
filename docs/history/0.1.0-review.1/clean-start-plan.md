> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

# Plan for a genuine clean-start edition

The supplied file named Clean-Start has the same populated cell contents as the EN workbook. This document specifies a future reset. **It has not been applied to either source file.**

The aim is to preserve the useful structure while removing fictitious organisational activity and approvals. A clean-start should retain formulas, styles, navigation, tables, validation, the 30 common topics, their AI reviews, five additional AI topics and the 193 external catalogue entries.

## Decide the starting configuration

The author should decide whether the starting edition retains two incomplete scope skeletons for N27 and N42 and an explicitly unapproved example method. If retained, they must be visibly drafts with missing organisation-specific data. They must not carry released scope, active memberships, approved evidence or authorised decisions.

The hidden TaskBase contains generated task infrastructure and source-location labels. Its constants are not all demonstration inputs. Do not clear that sheet as part of a blanket removal of sample data.

## Reset the operational inputs

The following are **candidate input ranges to inspect**, not a blind deletion script. Preserve formula and native-feature structure throughout. Resolve the existing Objects K8 defect before validating the reset.

| Area | Candidate demo-input ranges | Preserve |
| --- | --- | --- |
| Actions | A8:S207 | Calculations T:W and table structure |
| Checks | A8:P507 | Calculations Q:S |
| Implementations | A8:H207 | Calculations I:Q |
| Risks | A8:P127 | Calculations Q:Y |
| Safeguards | A8:D157 | Calculations E:F |
| Decisions | A8:R157 | Calculations S:W |
| Issues | A8:N207 and S8:T207 | Calculations O:R |
| Obligations | A8:N127 | Calculations O:P |
| Objectives | A8:N87 | Calculations O:Q |
| Assessments | A8:N307 | Calculations O:V |
| Coverage | A8:K1007 | Calculations L:P |
| CoverageRules | A8:H157 and O8:O157 | Calculations I:N |
| Scope | A8:J17 and A25:H174 | Calculations K:L and I:M respectively |
| Objects | A8:J82 and Y8:Y82 | Validation and hierarchy formulas K:X, after repair of K8 |
| Controls | A8:H157 | Calculation I |
| Mappings | A8:G407 | Calculations H:M |
| Documents | A8:K507 | Calculations L:M; deliberately replace the workbook's own procedure record |
| ChangeLog | A8:J507 | Calculation K; add an accurate initial reset/release entry |
| Requirements | Sample internal requirements A201:G202 | External catalogue A8:G200 and formula column H |
| MasterData roles | A8:C27 | Validation column D |
| MasterData persons | A35:E74 | Validation column F |
| MasterData methods | A82:L91 | Validation column M; any retained method must be clearly unapproved |
| MasterData mandates | A99:I158 | Validation column J |
| MasterData scales | A166:E185 | Validation column F; retain only with an explicitly defined draft method |

Clear dependent demonstration records together. Removing a person, object or method while retaining a demonstration approval or linked finding would create dangling references rather than a clean start.

## Reset foundational cards individually

ISMS-Foundations and AI-Supplements use individual cards rather than a single uniform input table. For each card, inspect and reset the editable definition, document, responsibility, applicability, checked-source version, release, next-step and date fields.

Set workflow selections to `Open`. Preserve card labels, topic links, formulas and the summaries. Apply the known `Offen` → `Open` correction before validating that the reset shows `Still open`.

Governance should start open, with no claimed confirmation, approval evidence or dates. Preserve the distinction between an internal risk register and an externally governed risk source.

## Replace demonstration metadata and guidance

Set an explicit reporting-date policy for the starting edition. A fixed user-selected date supports reproducible evaluation. Do not invent an approval date or substitute today's date for a historical decision.

Replace the demo data-state identifier, owner instructions, visible version and stale core metadata. Keep release status accurate. A new working copy has not been approved merely because it was generated successfully.

Remove or revise sample-specific deep links and the example procedures. Prefer directing readers to the separate EN demonstration workbook for worked cases. Preserve guidance on stable IDs, new evidence records and the separation between current operations and historical closure.

## Validate the resulting edition

1. Verify that there are no fictitious operational records, named assignments, evidence approvals or authorisations left in the starting file.
2. Confirm that empty required inputs produce explicit incomplete states, not apparent conformity or unjustified positive results.
3. Compare formulas, table definitions, styles, navigation, sheet protection and validation with the agreed baseline. The source has 101 standard and 71 extended x14 validation definitions; inspect preservation against the [inventory](../../../validation/history/0.1.0-review.1/extended-validations.json).
4. Create one complete scope–object–control–implementation–check–coverage chain in a disposable copy. Confirm that every relevant output updates and that deleting a prerequisite exposes the gap.
5. Test the first action closure and a deliberately mismatched closure, then a valid zero measurement and a blank measurement.
6. Recalculate in Microsoft Excel, save, close and reopen. Inspect the actual status displays and dropdowns.
7. Preserve the final clean-start and its separately tested demo counterpart with hashes and release notes.

The source-specific [IMS checker](../../../validation/history/0.1.0-review.1/check_ims.py) assumes the demonstration IDs. It should remain attached to the example. A genuine clean-start requires its own empty-state and first-record regression cases rather than reusing expected demo totals.
