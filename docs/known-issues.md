# Known issues in v2.6.1

Package 0.1.0-review.2 contains four public copies cleaned only of publication metadata. The main English locale defects are corrected. The following remaining findings prevent a stable operational release. English and German ranges use the same row and column addresses. Formulas, saved cell values, sheet protection and data validations match the original sources.

| ID | Status / priority | Affected area | Consequence |
| --- | --- | --- | --- |
| IMS-013 | Newly identified inherited blocker | CoverageRules I8:I157 / Deckungsregeln I8:I157 | No live rule validation; new clean rules cannot become valid, and duplicate existing rules keep OK. |
| IMS-014 | Newly identified inherited blocker | Coverage L8:L1007 / Deckung L8:L1007 | Static validation values accept invalid changed rows and omit valid new rows. |
| IMS-005 | Unresolved blocker | Objects K8 / Objekte K8 | English validation is blank; German validation is a fixed message. The first complete object cannot establish a current membership. |
| IMS-008 | Partly repaired; validation gap remains | Governance L9:L10 / Informationsführung L9:L10 | Unique referenced IDs are checked, but invalid linked method/mandate states and unreleased evidence can still produce Defined / Festgelegt. |
| IMS-006 | Reset materially improved; initialization incomplete | Starting editions | Operational records are cleared, but stale calculated labels and dangling template references remain. |
| IMS-007 | Partly repaired; release-test correction needed | ReleaseChecks C14:E14 and D15 / Freigabetests | Wrong zero/blank IDs remain; the correct demo task total is still copied into empty editions. |
| IMS-009 | Minor localization residue | English labels and sample text | Some explanatory labels remain German; repaired calculation literals are consistent. |

## Static validation columns

CoverageRules / Deckungsregeln I8:I157 contains no formulas. Demo rows have stored OK values; the clean first rows are blank. Since J tests I=OK, a complete new rule can report zero expected targets and zero missing assignments despite a valid current member.

Coverage / Deckung L8:L1007 also contains no formulas. The first 13 rows retain 12 OK values and one mode-mismatch message, even in clean-start. Later prepared rows are static blanks. The bounded scenario tests demonstrate that:

- Moving a valid assignment from row 8 to row 21 makes the valid-coverage count fall from 1 to 0.
- Duplicating a coverage ID and rule/target pair leaves both validation cells at OK and counts 2 valid coverages for 1 target.
- Replacing an implementation reference with an absent ID leaves the assignment counted as valid, even though the current-evidence output says Reference missing / Referenz fehlt.

These columns were already static in v2.6. This review newly identified their full extent; they are not regressions introduced by v2.6.1. No OOXML table has a calculated-column-formula fallback.

## First-object validation and operating mode

Objects K8 has no value or formula in English. Objekte K8 contains the fixed text Betriebsmodus fehlt in German, including Leerstart. The corresponding validator at row 9 works with the same complete input data. Simply clearing the old warning does not restore validation.

Rows 9–82 do not validate the operating-mode field in column Y. The dropdown permits blanks. The author should define which object types require a mode and how invalid pasted modes are rejected. Blank mode is not independently classified as a defect in this review because the current dropdown allows it.

## Governance: existing IDs versus usable prerequisites

The revised formulas correctly reject missing responsible-person, method, mandate, evidence-document and confirming-person IDs. Duplicate responsible IDs and expired confirmation dates are also rejected in the tested cases.

However, a complete reference set still reports Defined / Festgelegt in these synthetic changed-input cases:

| Changed prerequisite | Its own calculated state | Governance result |
| --- | --- | --- |
| MasterData / Stammdaten E82 = 0 | M82: Review method limits / Methodengrenzen prüfen | Defined / Festgelegt |
| MasterData / Stammdaten B99 = MISSING | J99: Review person ID / Personen-ID prüfen | Defined / Festgelegt |
| Documents / Dokumente G8 = Draft / Entwurf | M8: Not released / Nicht freigegeben | Defined / Festgelegt |

The other governance inputs and confirmation dates are complete in each scenario. This finding concerns the definition gate; it does not claim that every downstream risk acceptance bypasses its own independent checks.

## Cleared starting editions

The reset removes 1,677 nonempty constants per language and clears the operational IDs, persons and mandates. It preserves the catalogue, six roles, five controls, one explicitly unapproved example method, 15 scales and nine template history records.

Remaining setup work includes:

- DOC-MAP at Documents / Dokumente row 23 still points to removed S-010 and PERSON-01.
- The example method still points to removed DOC-METH and correctly requests a method-document review.
- Governance / Informationsführung B11 retains MS-AIMS despite the empty scope register.
- Coverage validation labels remain from the demo.
- Several walkthroughs and embedded tests still assume demo IDs.

The empty-edition review count is 3 in English and 4 in German. The difference is the additional fixed German object warning. Zero operational tasks does not mean setup has passed. See [the reset evidence and plan](clean-start-plan.md).

## Embedded test instructions

ReleaseChecks / Freigabetests C14 still asks for Z-001 and nonexistent Z-00X and E14 points to P8. The actual measured-zero and missing-measurement examples are Z-002 at row 10 and Z-004 at row 11. Their underlying formulas behave correctly.

D15 now correctly expects 24 tasks in the demos, repairing the old 23-task claim. The clean editions also retain that text but contain zero operational tasks. Give each edition its own acceptance guidance.

## Other limits

Native Microsoft Excel interaction, recalculation after edits, save/reopen, dropdown behavior, print layout and visual acceptance have not been completed. The fixed demonstration date remains 8 October 2026. All prepared capacities are finite. Sheet protection is accident prevention, and the manual change log is not an append-only technical audit trail.

The [review](review.md) separates resolved defects from current ones. [Issues to open](issues-to-open.md) provides repair acceptance criteria; [remediation-plan.json](../validation/remediation-plan.json) records the current proposal. No formula or cell-content changes have been applied to a supplied workbook.

## PUB-01 — Office sensitivity-label metadata — resolved

The publication-metadata review was completed on 27 October 2026. The visible Public classifications were deliberately retained. Document properties, `lastModifiedBy` and absolute local paths were removed directly from the OOXML packages.

All 34 worksheets per edition, 74,555 formulas per edition and all saved cell values match the original sources. Sheet protection and data validations are unchanged. Regression and scenario baselines are reproduced. Current public-copy hashes are recorded in [validation/manifest.json](../validation/manifest.json), and the review decision is documented in [validation/publication-metadata.json](../validation/publication-metadata.json). Full native Excel acceptance remains a separate release requirement.

## RIGHTS-01 — Standards-derived catalogue rights — resolved

The catalogue structure review was completed on 28 October 2026. The 193 references consist of identifiers, source links and short original topics of 9–47 characters, not full ISO/IEC requirement text. The `K-...` controls are project-specific building blocks. The author's MIT/CC BY 4.0 allocation applies to original material; cited standards and third-party works retain their terms. See [third-party-rights-review.md](../validation/third-party-rights-review.md). Future additions of verbatim or substantially similar standard text require a renewed review.
