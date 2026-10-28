# Native Microsoft Excel acceptance

Status: **PENDING**. No native Microsoft Excel acceptance has been recorded for IMS Compass.

Package: `0.1.0-review.2`. Sources: all four IMS v2.6.1 editions. This record was prepared on 2026-10-26; it is an acceptance template, not evidence that the checks have occurred.

## Environment and artifact identity

- Excel edition and full build:
- Operating system and version:
- Reviewer:
- Test date:
- Working-copy filenames:
- Working-copy SHA-256 hashes, if different from the manifest:
- Other applications used for secondary rendering, if any:

## Required application cycle

- [ ] Open a disposable working copy in the intended desktop Microsoft Excel build.
- [ ] Confirm automatic calculation and exercise the intended input controls.
- [ ] Force a full recalculation and inspect relevant outputs for errors or stale values.
- [ ] Save, close, and reopen the file; repeat the affected checks against the reopened file.
- [ ] Confirm formulas, validations, tables, conditional formatting, navigation, protection, charts, and print settings survived as intended.
- [ ] Inspect the intended report/print views rather than inferring them from the interactive display.

## Project-specific acceptance cases

- [ ] Test all four English/German and demonstration/clean-start editions through open, edit, recalculate, save, close, and reopen.
- [ ] After repairs, create and edit the first object, coverage rule, and coverage record; include duplicates, invalid references, inactive records, and valid zero values.
- [ ] Verify governance rejects invalid methods, missing mandate persons, and unreleased evidence while accepting a fully usable prerequisite set.
- [ ] Initialize each clean-start edition and confirm document, method, governance, coverage, and task-count references match its empty state.
- [ ] Check the corrected embedded ReleaseChecks/Freigabetests instructions, dropdowns, protection, navigation, and intended print views.

## Results and evidence

Record each result, unexpected behavior, screenshot/PDF evidence location, and follow-up issue here. Keep real organizational assessments and personal data out of the public repository.

## Completion

- [ ] All required cases pass. Any exception remains recorded as a release blocker and `stable_release_ready` remains false.
- [ ] The reviewer and test date are recorded above.
- [ ] `validation/release-status.json` has been updated only after reviewing this evidence.
- [ ] Source hashes, citation/version metadata, and the change log have been updated if an artifact intentionally changed.
Publication metadata cleanup was completed directly at OOXML level on 27 October 2026. This does not count as the native Microsoft Excel acceptance required below.
