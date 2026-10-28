# Quick start

This guide applies to the four v2.6.1 files in package 0.1.0-review.2. The workbook is still a reviewed prerelease. The corrected example calculations are useful for learning; [live-validation defects](known-issues.md) must be repaired before relying on edited coverage records or a new operational setup.

## Pick a working copy

Use [the English demo](../workbooks/IMS-Compass-v2.6.1-EN.xlsx) or [the German demo](../workbooks/IMS-Kompass-v2.6.1.xlsx) for the walkthrough. Desktop Microsoft Excel is the intended application. No macro execution or external-workbook connection is required.

The [English starting edition](../workbooks/IMS-Compass-v2.6.1-EN-Clean-Start.xlsx) and [German Leerstart](../workbooks/IMS-Kompass-v2.6.1-Leerstart.xlsx) now have the operational examples cleared. They retain template/reference content and unresolved setup dependencies. Follow the [edition and initialization guide](clean-start-plan.md); do not interpret zero operational tasks as completed setup.

## Find the main areas

| English sheet | German sheet | Purpose |
| --- | --- | --- |
| Setup | Aufbau | Reporting date and setup navigation |
| ISMS-Foundations | ISMS-Grundlagen | Thirty shared foundational definitions |
| AI-Supplements | KI-Ergänzungen | Thirty adaptations plus five additional AI topics |
| Governance | Informationsführung | Internal or external risk-information responsibility |
| Home | Start | Operational task filters |
| Overview | Übersicht | Summary counts and data-state metadata |
| StandardView | Normsicht | Standard-specific assessments |
| TargetCoverage | Sollabdeckung | Expected objects for a selected rule |
| Report | Bericht | Working statement of applicability |
| Scope / Objects | Geltung / Objekte | Management systems, memberships and objects |

The [edition comparison](../validation/edition-comparison.json) records the full structural review. IDs such as MS-ISMS, REG-004 and S-021 remain stable across languages.

## Walk through the example

1. **Set the evaluation context.** Setup / Aufbau C5 is fixed at 8 October 2026 for the demonstration. Read the data-state identifier, draft status and owner field on Overview / Übersicht. Change the date deliberately in a working evaluation.
2. **Inspect foundational definitions.** The first topic is documented. The other 29 shared topics and 34 AI topics are open. The English status is now Still open; the German status is Noch offen.
3. **Inspect risk governance.** Both risk-governance choices start open. The workbook distinguishes a local risk register from an authoritative external system. Filling five existing IDs and dates is not sufficient evidence of a valid definition: review the linked method, mandate and evidence status as well.
4. **Trace evidence and closure.** DOC-RIGHTS → P-007 → U-004 connects a document, verification record and implementation. P-007 also supports M-007. That action is Effectively closed / Wirksam abgeschlossen; finding V-007 is Closure confirmed / Abschluss bestätigt. M-002 remains Closure incomplete / Abschluss unvollständig despite its closed processing label.
5. **Distinguish zero from absence.** Z-002 in Objectives / Ziele row 10 contains a measured zero and reports Target value reached / Zielwert erreicht. Z-004 at row 11 has no measurement and reports Measurement open / Messung offen. The embedded test still names the wrong records; use these exact rows.
6. **Inspect expected coverage.** REG-004 selects S-020 and S-021. S-021 lacks an assignment. The demo now reports two expected targets for that rule, one missing assignment, and 13 expected rule–object combinations overall.
7. **Change the standard view.** StandardView / Normsicht B4 selects the management system. MS-ISMS gives N27 and 93 controls in Report / Bericht C10. MS-AIMS gives N42 and 40 under the formula's definition: 38 reference controls plus two internal sample requirements.

The corrected language branches were tested with N42 selection, a production-only rule and an inactive rule. The general input-validation gaps still apply when adding or changing records; passing those specific branches does not make all coverage edits safe.

## Use task filters

Home / Start filters by person, management system, task type and case. Clear the case filter with All cases / Alle Fälle, and return to page 1 after narrowing the selection. The shipped demo has 24 operational tasks. A cleared starting edition has zero; its embedded demo expectation of 24 must not be used as its acceptance test.

## Run the checks

From the repository root:

    python3 tools/validate_repository.py
    python3 tools/check_ims.py --report validation/local-regression-results.json

The second command checks all four editions and exits 1 while the known defects remain. To examine just one source:

    python3 tools/check_ims.py workbooks/IMS-Compass-v2.6.1-EN.xlsx

For changed-input source-formula scenarios:

    python3 -m pip install -r requirements-test.txt
    python3 tools/check_scenarios.py --output validation/local-scenario-results.json

Both IMS scripts accept an explicit known-defect option for tracking this unchanged prerelease baseline. That option leaves failures marked as failures in JSON and is not a release approval. The scenario evaluator is purpose-limited and is not native Excel. See [validation](validation.md) for the exact boundary.

Keep operational evidence and personal assignments in a controlled working copy. Before a stable release, repair the documented ranges and run edit/recalculate/save/reopen, dropdown and visual tests in the intended Excel version.
