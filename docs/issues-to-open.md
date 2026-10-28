# Issues to open for the next IMS release

These are proposed author tasks. Copy the items you want to track into GitHub Issues; the issue tracker becomes authoritative once an item has been created there. All four v2.6.1 files remain unchanged. The [machine-readable remediation plan](../validation/remediation-plan.json) identifies the ranges, priority and acceptance conditions.

## IMS-013 — Restore rule validation throughout the prepared range

**Blocker.** CoverageRules / Deckungsregeln I8:I157 contains no formulas. Blank clean-start outputs exclude valid new rules; static OK labels let duplicate existing IDs continue counting targets.

Implement live validation for every prepared row. Preserve the unique-ID contract, required references, allowed selections, current scope and applicable mode policy. Empty rows must return blank; invalid input must return a useful rejection and be excluded from counts.

Acceptance must include the first rule, a later rule, the last prepared row, missing and duplicate IDs, invalid references, active/inactive selection, all modes and a specific mode. With one independently valid current membership, a valid rule must give I8=OK, J8=1 and L8=1 before coverage exists. Duplicate rules must not remain valid.

## IMS-014 — Restore coverage validation and prevent stale acceptance

**Blocker.** Coverage / Deckung L8:L1007 contains only stored values, including the thirteen old demo labels retained in clean-start.

Restore live validation over the complete prepared range. Validate the record ID, rule/target uniqueness, referenced rule, target, implementation, responsible person, versions and transferability/mode contract. Do not replace the column with a constant OK. Keep assignment validity separate from the current-evidence status.

Acceptance must include a valid coverage moved from row 8 to first-unused row 21, an absent implementation, duplicate coverage IDs, duplicate rule/target pairs, mismatched object/mode/version, and empty rows. A moved valid record should still count once. Two invalid duplicate records must not count as two valid assignments.

## IMS-005 — Restore the first object validator and specify operating mode

**Blocker.** English Objects K8 is blank; German Objekte K8 is a fixed message. Neither responds to input.

Restore a formula consistently with the prepared object validator rows. Separately decide which object types require an operating mode and how blanks or invalid pasted values are treated. Existing rows 9–82 do not validate Y, so copying the neighboring formula is not a complete mode-policy implementation.

Acceptance: identical complete object inputs at rows 8, 9 and 82 produce the same valid result, and a corresponding valid membership becomes current. Missing/duplicate object IDs, invalid owners, invalid parents, cycles and out-of-range hierarchy depth must still be rejected. Empty row 8 must not show a permanent warning.

## IMS-008 — Make governance completion account for linked validity

**High priority.** The new unique-ID checks should be retained. The remaining gap is that an invalid method, invalid mandate or unreleased evidence document can still yield Defined / Festgelegt.

Specify the definition's prerequisites explicitly: method validity, mandate validity and relevant management-system/authority/period context, responsible/confirming person status, and current released evidence. Reuse the owning register's validation rather than treating ID existence as complete proof.

Acceptance: retain all sixteen passing reference/date scenarios across EN and DE. Add rejection for the six linked-state failures, preserve a complete valid definition, and test the corresponding second governance block as well. Document which downstream decision checks remain separate.

## IMS-006 — Finish initialization and make retained template material explicit

**High priority.** Keep the improved reset. Resolve DOC-MAP's removed object/person references, the retained method's DOC-METH dependency, the fixed MS-AIMS display and the stale coverage labels. Roles, controls, example methods/scales and template history may remain if clearly identified as configurable, unapproved reference material.

Provide a short first-record walkthrough in each starting edition. Verify that it works without copying hidden status values or demo approvals. Preserve the 193 external references, formula locations, tables, all 172 validation definitions and intended protection.

Acceptance: no unexplained orphan reference remains, empty rows have no stale status, and the first person–scope–object–membership–rule chain succeeds in the intended Excel version.

## IMS-007 — Correct and separate embedded release tests

ReleaseChecks / Freigabetests C14/E14 must reference Z-002/P10 and Z-004/P11, or explicitly direct clean-start users to the demo. The old Z-00X does not exist.

Keep the corrected demo expectation of 24 tasks. The clean-start begins with zero operational tasks, so provide its own expected state and first-record scenario. Verify the embedded navigation targets and instructions against the actual edition.

## Release acceptance and housekeeping

After the repairs, rerun the standard-library checker and all changed-input scenarios. A stable candidate must pass the intended behavior checks without a known-defect allowance. Preserve the old review evidence as history and create new results for the changed sources.

Complete native Microsoft Excel editing, recalculation, save/close/reopen, dropdown, protection, navigation and visual/print acceptance. Record the exact Excel build and platform. The MIT/CC BY 4.0 allocation, publication-metadata review and third-party catalogue structure review are complete. Keep the manifest, version, citation, change log and release-status record aligned with the public copies.

Minor English label cleanup can be included in the same reviewed change, but should not obscure the functional differences. Resolve the issues in both languages and both starting states.

## Office publication metadata — completed

The publication-metadata review was completed on 27 October 2026. Public classifications were retained; document properties, `lastModifiedBy` and absolute local paths were removed directly from the OOXML packages. All formulas, saved cell values, sheet protection and data validations match the original sources. Regression and scenario baselines are reproduced. Current identities are recorded in `validation/manifest.json` and `validation/publication-metadata.json`.

## Standards-derived catalogue redistribution rights — completed

The catalogue structure review was completed on 28 October 2026. The 193 references use identifiers, source links and short original topics of 9–47 characters rather than full ISO/IEC requirement text. The `K-...` controls are project-specific building blocks. See `validation/third-party-rights-review.md`. Future additions of verbatim or substantially similar standard text require a renewed review.
