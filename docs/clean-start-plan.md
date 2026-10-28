# Editions and clean-start initialization

The v2.6.1 starting editions are substantially reset. They are no longer populated duplicates of the demos. They still require live-validation repairs and an explicit initialization pass before operational use.

| Language | Learn from the worked example | Begin a cleared working copy |
| --- | --- | --- |
| English | [IMS-Compass-v2.6.1-EN.xlsx](../workbooks/IMS-Compass-v2.6.1-EN.xlsx) | [IMS-Compass-v2.6.1-EN-Clean-Start.xlsx](../workbooks/IMS-Compass-v2.6.1-EN-Clean-Start.xlsx) |
| German | [IMS-Kompass-v2.6.1.xlsx](../workbooks/IMS-Kompass-v2.6.1.xlsx) | [IMS-Kompass-v2.6.1-Leerstart.xlsx](../workbooks/IMS-Kompass-v2.6.1-Leerstart.xlsx) |

Use the same version and language when comparing a demo with its starting edition. IDs remain stable across languages, but display selections are localized.

## What the reset accomplished

Each language removes 1,677 nonempty constants. Operational records are cleared from actions, checks, implementations, risks, safeguards, decisions, issues, obligations, objectives, assessments, coverage, rules, management systems, memberships, objects, mappings, persons and mandates. External risk references are also empty.

The underlying structure is retained: 34 sheets, 74,555 formula cells, 26 tables, 101 standard validation definitions, 71 x14 definitions, defined names and sheet-protection settings. The only changed demo-to-clean formula is the descriptive Instructions / Anleitung B8 text.

The reset is intentionally more than deleting every constant. The following material remains:

| Retained material | Count in each starting edition | How to use it |
| --- | ---: | --- |
| External catalogue references | 193 | Controlled reference scaffolding; verify interpretation against your standards. |
| Roles | 6 | Review or replace the proposed responsibilities. No persons are assigned. |
| Control building blocks | 5 | Starting control definitions, not evidence that controls operate. |
| Example risk method | 1 | Explicitly marked for release before use. |
| Example method scales | 15 | Replace or approve the stated criteria before assessing risks. |
| Workbook-document record | 1 | Reconfigure its object/owner references. |
| Template change-log records | 9 | Preserve provenance and distinguish it from future organizational activity. |

The two internal sample requirements, five other sample controls and the fictitious person records are removed. A targeted scan also confirmed that the six demo person names do not remain in the clean XML/shared strings.

## Remaining defects and dependencies

**Repair first-object and coverage validation before attempting the first operational chain.** Objects / Objekte K8 has no formula. CoverageRules / Deckungsregeln I8:I157 and Coverage / Deckung L8:L1007 have no formulas. These are inherited defects, not missing setup input. Manually writing OK into a validation cell is not a repair.

Other retained dependencies need an explicit treatment:

- Documents / Dokumente row 23 keeps DOC-MAP, S-010, PERSON-01, demo dates and source-description text. The object and person IDs no longer exist. Either configure a valid self-documentation record during setup or make its pending fields explicit.
- MasterData / Stammdaten L82 references DOC-METH, which was removed. Supply the controlled method document and approval process, or deliberately replace the example method and dependent scales.
- Governance / Informationsführung B11 retains MS-AIMS. Make that display follow the selected/created AI management system or clearly mark it as unconfigured.
- Coverage / Deckung L8:L20 retains the old thirteen validation labels. Restored formulas must return blank when a row is empty.
- Embedded example procedures still refer to removed records. Keep the worked examples in the demonstration workbook and provide edition-specific first-record tests.

The current input-review total is 3 EN and 4 DE. In English it consists of the stale coverage mismatch at L15, the method-document dependency at M82 and the dangling document at L23. German adds the fixed first-object warning. Home / Start shows zero operational tasks because no operational work has been created; that is not evidence that the setup is complete.

## Intended first-use sequence after repair

1. Save a controlled working copy, set its owner, data-state identifier and reporting date, and keep the original source version available.
2. Review the six roles and create actual persons or units in MasterData / Stammdaten. Confirm required IDs are unique and active.
3. Create the management-system record, its controlled scope document, the first object and its membership. Validate the first prepared row as well as later rows.
4. Review the retained method and scales, supply its document, and establish applicable mandates. Keep the method unapproved until its local review is complete.
5. Record the shared foundation and AI-specific definitions. Their documentation status and standard conformity remain separate.
6. Define internal or external risk governance with existing, valid and current prerequisites. The current ID checks alone do not ensure that.
7. Create one applicable coverage rule. A single valid current member should produce one expected target and one missing assignment before a valid coverage is added.
8. Add a matching implementation, evidence/check and coverage. Confirm the counts and evidence state update. Remove a prerequisite in a disposable copy and confirm the gap is exposed.

The first-use scenarios in [scenario-results.json](../validation/scenario-results.json) show the current failure points. They are exact input fixtures, not an approved organization-specific configuration.

## Acceptance criteria for a finished starting edition

A release candidate should pass the following checks in both languages:

- No fictitious operational assignments or stale validation labels remain.
- Every retained reference is valid or is presented as an explicit unconfigured prerequisite.
- Empty inputs yield empty/incomplete states; no empty row claims OK.
- The first and first-unused rows behave consistently, including duplicate and absent IDs.
- A one-target rule counts one expected target and one missing assignment before coverage.
- Native Excel edit/recalculate/save/reopen, dropdown and visual checks pass.
- Source formulas, the 172 validation definitions, tables and protection are preserved except for the reviewed changes.

[Reset-region evidence](../validation/reset-scope-evidence.json) and [extended-validation inventory](../validation/extended-validations.json) are retained for comparison. The [historical plan](history/0.1.0-review.1/clean-start-plan.md) describes the previous v2.6 state; it is not the current reset assessment.
