<img src="assets/logo.png" alt="IMS Compass fox and compass logo" width="160">

# IMS Compass

**An Excel workbench connecting information-security and AI management systems, scope, evidence, risks, actions and decisions.**

**Reviewed prerelease 0.1.0-review.2 · source v2.6.1 · functional review 23 October 2026; public-copy preparation 27 October 2026.** The public workbooks were metadata-cleaned directly at OOXML level; the Public sensitivity labels are retained and absolute local paths and `lastModifiedBy` were removed. All 34 worksheets per edition, 74,555 formulas per edition and all saved cell values match the original sources. The inherited validation, governance, clean-start and release-instruction gaps still block reliable first use and edits. Read the [current review](docs/review.md) and [known issues](docs/known-issues.md) before using the results.

## Choose an edition

| Language | Edition | Workbook |
| --- | --- | --- |
| English | Worked example | [IMS-Compass-v2.6.1-EN.xlsx](workbooks/IMS-Compass-v2.6.1-EN.xlsx) |
| English | Cleared starting edition | [IMS-Compass-v2.6.1-EN-Clean-Start.xlsx](workbooks/IMS-Compass-v2.6.1-EN-Clean-Start.xlsx) |
| Deutsch | Worked example | [IMS-Kompass-v2.6.1.xlsx](workbooks/IMS-Kompass-v2.6.1.xlsx) |
| Deutsch | Cleared starting edition | [IMS-Kompass-v2.6.1-Leerstart.xlsx](workbooks/IMS-Kompass-v2.6.1-Leerstart.xlsx) |

Use a worked example to learn the relationships. The starting editions retain reference material, roles, controls and an unapproved example method; they still need the documented repairs and initialization. They are **not yet functionally accepted blank templates**. The [edition and setup guide](docs/clean-start-plan.md) explains exactly what was cleared and retained.

All four public files are metadata-cleaned copies. Current and previous source hashes are recorded in [validation/manifest.json](validation/manifest.json). The old v2.6 files have been removed from the current workbook directory; the [previous review](docs/history/0.1.0-review.1/review.md), results and source hashes remain historical evidence.

## What changed

The English demo now shows **13 expected rule–object combinations**, **one missing assignment**, **93 N27 controls**, and the correct open status for all **63 open topics**. Changing the standard selector to N42 produces **40** controls and sample internal requirements. The German edition agrees on these results.

Three live-validation gaps remain in every edition: the first object row, the entire coverage-rule validation column and the entire coverage validation column. New valid records can be omitted, and changed invalid records can retain a static OK. Governance now rejects nonexistent or duplicate referenced IDs, but does not propagate several invalid linked-record states. These are concrete release blockers, with [reproducible scenarios and correction tasks](docs/issues-to-open.md).

## Start and verify

Read the [quick start](docs/quickstart.md) and [methodology](docs/methodology.md). Python 3.10 or later runs the standard-library checks:

    python3 tools/validate_repository.py
    python3 tools/check_ims.py --report validation/local-regression-results.json

The package-integrity check should pass. The IMS checker currently exits 1: **62 assertions pass and 22 fail for documented issues**, across all four editions. The failures remain visible; a green integrity check is not functional approval.

An optional source-formula scenario harness has one explicit dependency:

    python3 -m pip install -r requirements-test.txt
    python3 tools/check_scenarios.py --output validation/local-scenario-results.json

It evaluates formulas with input changes held in memory and never saves a workbook. Its default nonzero exit records unresolved behavior. See [validation scope and exact results](docs/validation.md).

All **298,220 formula-cell results** across the four public files match the original sources and the previous disposable LibreOffice recalculations, allowing 24 insignificant timestamp serialization differences in the original review. This confirms the saved state, including the defects; formal native Microsoft Excel editing, save/reopen, dropdown and visual acceptance remain pending.

## Project files

- [Current review](docs/review.md): resolved, remaining and newly identified findings.
- [Known issues](docs/known-issues.md): affected cells and practical limits.
- [Issues to open](docs/issues-to-open.md): proposed repairs and acceptance criteria.
- [Source manifest](validation/manifest.json): exact workbook identities.
- [Publishing instructions](PUBLISHING.md): first import and updating an existing repository.

The workbooks and Python scripts use MIT; explanatory documentation, figures, the project mascot and illustrative examples use CC BY 4.0. See [LICENSE-STATUS.md](LICENSE-STATUS.md) for the allocation. The third-party catalogue structure review is complete: the 193 external references use identifiers, source links and short original topics of 9–47 characters rather than full ISO/IEC requirement text. See [validation/third-party-rights-review.md](validation/third-party-rights-review.md). Use [CITATION.cff](CITATION.cff) and identify the workbook version, language and edition when citing the project.

## Prepare publication

The [browser-only publishing guide](PUBLISHING.md) covers repository creation, file upload, Actions, visibility, and prerelease creation through GitHub's web interface. The [publication-metadata review](validation/publication-metadata.json) is complete. The standards-derived catalogue structure review is complete. For a stable release, complete the [native Excel acceptance record](validation/native-excel-acceptance.md) and address the functional issues described above.
