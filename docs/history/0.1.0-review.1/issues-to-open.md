> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

# Issues to open

These are proposed implementation tasks. No issues have been sent to GitHub and no source workbook has been modified. The proposed formula changes are recorded in [formula-patch-plan.json](../../../validation/history/0.1.0-review.1/formula-patch-plan.json).

## 1. Restore expected coverage and missing-target calculations

**Priority:** release blocker. **Related findings:** IMS-001, IMS-002.

CoverageRules J8:J157 compares `Ja` with English `Yes` inputs. TargetCoverage G8:G157 additionally returns `Ja` and `Nein`, while downstream formulas expect `Yes`. Correct the exact literals in both formula families and preserve the existing scope, mode, date and validity logic.

**Acceptance criteria**

- With unchanged sample inputs, expected rule–object combinations total 13.
- REG-004 expects S-020 and S-021, counts two targets and exposes the one missing assignment for S-021.
- Overview G13 is 13 and C15 is 1.
- TargetCoverage identifies both expected targets and displays the missing assignment.
- Setting a rule inactive suppresses its expected population.
- A mode-specific rule changes only when the corresponding object's applicable mode changes.
- Standard and extended validation rules survive the edit and the Excel save/reopen cycle.

## 2. Correct the control count in Report

**Priority:** release blocker. **Related finding:** IMS-003.

Replace the German category literals in Report C10 with the actual English Requirements categories.

**Acceptance criteria**

- N27 produces 93 controls for the supplied catalogue.
- N42 produces 40 under the current definition: 38 reference controls and two sample internal requirements.
- Changing the selected management system updates the count and report content together.
- A newly added internal requirement with the relevant standard ID affects the count correctly within the supported capacity.

## 3. Make Open a valid foundational status

**Priority:** release blocker. **Related finding:** IMS-004.

Replace the exact `Offen` literal in the 30 ISMS status formulas and 35 AI status formulas. Preserve all other branches.

**Acceptance criteria**

- The 29 open ISMS topics and 34 open AI topics in the supplied example show `Still open`.
- Completed examples remain `Documented` when their evidence is current.
- An invalid selection remains visibly invalid.
- An overdue clarification shows its overdue state.
- A changed ISMS source version still requires the linked AI review to be repeated.

## 4. Restore live object validation and define mode requirements

**Priority:** release blocker. **Related finding:** IMS-005.

Objects K8 is a fixed string. Restore a formula and decide how operating mode applies to organisation, process, system and agent object types. The current neighbouring formulas do not enforce that field.

**Acceptance criteria**

- K8 updates when relevant row 8 inputs change.
- Blank, invalid and permitted mode values receive consistent treatment across the supported object types.
- Existing ID, owner, parent, date and hierarchy checks remain active.
- The agreed mode rule is documented rather than hidden in a special-case sample cell.

## 5. Produce a genuine clean-start workbook

**Priority:** distribution blocker. **Related finding:** IMS-006.

The uploaded Clean-Start workbook has the same populated cell contents as the EN example. Use the [clean-start plan](clean-start-plan.md) to create a separate, deliberately reset edition.

**Acceptance criteria**

- Demonstration operational records, people, evidence, releases and approvals are absent.
- Any retained scope or method skeletons are visibly incomplete drafts.
- The 193 external reference entries and the foundational topic structure remain available.
- There are no fake approvals or apparently fulfilled assessments produced by empty input.
- Sample-specific links point to the separate example workbook or are replaced with useful starting guidance.
- Formula, table, navigation and validation preservation checks pass, followed by native Excel tests of the first new record chain.

## 6. Validate governance references before marking a definition complete

**Priority:** important. **Related finding:** IMS-008.

Governance L9:L10 checks several IDs only for nonemptiness. Extend the rules to verify the actual referenced records and the status required for the confirmation.

**Acceptance criteria**

- Unknown method, mandate, person or evidence IDs cannot produce `Defined`.
- Duplicated, withdrawn, inactive or expired references are handled explicitly where relevant to the field's meaning.
- Internal and external modes continue to have their distinct required fields.
- An expired governance confirmation remains open for review.
- Documented acceptance of the data does not imply that an external system has been queried automatically.

## 7. Repair the embedded release-test instructions

**Priority:** important. **Related finding:** IMS-007.

ReleaseChecks contains stale task counts and incorrect zero-versus-blank record references. Align the written scenario, proof cells and actual output, then rerun it against the release candidate.

**Acceptance criteria**

- The zero-valued example is identified as Z-002 / Objectives row 10.
- The missing-measurement example is identified as Z-004 / Objectives row 11.
- Proof outputs show both P10 and P11, rather than unrelated P8.
- The filter-reset count matches the verified release-candidate sample state; the unchanged source baseline currently contains 24 operational tasks.
- Manual tests are clearly identified as requiring an intervention, rather than presented as already executed proof.

## 8. Finish the English edition and align release metadata

**Priority:** maintenance. **Related findings:** IMS-009, IMS-010.

Review the display-language proposals and remaining static German labels. Update the document metadata with the correct release version and an accurate owner/release state.

**Acceptance criteria**

- User-facing labels and formula messages are consistently English.
- Stable IDs and matching version strings are not changed without updating their dependencies.
- Filename, visible rule version, core title, description, change log and release documentation agree.
- The corrected candidate is recalculated, saved, closed and reopened in Microsoft Excel.
- Release notes distinguish corrected calculations, language changes and any separately agreed rule changes.
