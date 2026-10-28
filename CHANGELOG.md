# Changelog

## Third-party catalogue rights review — 2026-10-28

- Reviewed the structure of all 193 external catalogue references: 123 N27 and 70 N42, comprising 62 management requirements and 131 reference controls.
- Confirmed that entries use identifiers, source links and short original topics of 9–47 characters rather than full ISO/IEC requirement text. The `K-...` controls are project-specific building blocks.
- Added `validation/third-party-rights-review.md` and marked `third_party_rights_reviewed` and `public_visibility_recommended` as true. Updated the release gate to require that evidence file.
- Set `date-released` to 2026-10-28 and updated the license status, README, publishing guide, known issues, review, validation guide and issue drafts.

The documented IMS functional blockers and formal native Excel acceptance remain open. Future additions of verbatim or substantially similar standard text require a renewed rights review.

## Licensing and public-copy preparation — 2026-10-27

- Selected MIT for the workbooks and Python scripts, and CC BY 4.0 for explanatory documentation, figures, the project mascot and illustrative examples. Added the operative root `LICENSE` and full `LICENSES/CC-BY-4.0.txt`; updated license status, citation metadata, README, publishing guide, known issues, review, validation guide and issue drafts.
- Cleaned all four workbooks directly at OOXML level. Public sensitivity labels were retained; absolute local paths and `lastModifiedBy` were removed. All 34 worksheets per edition, 74,555 formulas per edition, saved cell values, sheet protection and data validations match the original sources.
- New SHA-256 identities: EN demo `a2a16d8b77bae0ddef4a693059bb3d18ad92743f22b014d4e0567d40549af696`; EN clean start `c14cca406fbc308bee022b72555aa51d7969b0dca23deb2d0b2efc180f71cc77`; DE demo `d99a3b65a7fbf8daf175c7cf299e71e85046d31d1d009d37ab99aa8a9c444b19`; DE Leerstart `6aab33eeda23dab14ab6e15b89557361ad2eab90684b10c17167b373c0c5fad0`.
- Updated the source manifest, recalculation and extended-validation records, publication-metadata record and release status. Regression and scenario baselines are reproduced.

The documented IMS functional blockers and formal native Excel acceptance remain open. Before public visibility, confirm redistribution rights for standards-derived catalogue wording, including the 193 external references and any ISO/IEC-derived text.

## Web-publication preparation — 2026-10-26

Repository-only update before the initial GitHub import. The unpublished package version and functional-review baseline remain unchanged.

- Replaced the command-line import guide with browser-only repository, upload, Actions, visibility, and release instructions.
- Expanded CI to run both known-defect-aware IMS checkers and compare their exact prerelease reports.
- Added an Office publication-metadata record, a native Excel acceptance template, and explicit evidence checks in the stable-release gate.
- Added the author ORCID to the primary citation metadata and clarified post-import repository status documentation.

No source workbook or manuscript bytes were changed. This preparation does not establish native Microsoft Excel acceptance, resolve licensing decisions, or close functional blockers.

## 0.1.0-review.2 — 2026-10-23

Updated the repository after the author supplied four IMS v2.6.1 editions.

- Replaced the two current v2.6 workbooks with unchanged English/German v2.6.1 demo and starting files.
- Confirmed repaired English coverage, target, report-count and open-status literals; updated metadata and genuine operational clearing.
- Expanded the audit to first-record, duplicate-key, new-row and governance linked-state behavior.
- Identified inherited missing validation columns and retained clean-start dependencies; kept stable-release readiness false.
- Added a four-edition standard-library checker, an optional portable source-formula harness, revised evidence and a concrete remediation plan.
- Preserved the prior audit, formula proposal, source hashes and results as historical evidence.
- Updated edition guidance, source manifest, citation, release status and existing-repository update instructions.

The uploaded workbook bytes were not edited. This package version describes the repository and review update, independently of source workbook version v2.6.1.

## 0.1.0-review.1 — 2026-10-22

Initial repository preparation and independent review package.

- Included IMS Compass v2.6 (both supplied copies) with original source bytes preserved.
- Added project orientation, methodology, quick start and cell-specific known issues.
- Added recorded verification evidence and reproducible read-only checks.
- Added a project mascot, citation metadata and contribution/issue templates.
- Added a source checksum manifest and package-integrity workflow.

This package version describes the repository scaffolding and review. It does not increment the supplied workbook versions. Proposed corrections have not been applied to the source workbooks. See [release status](validation/release-status.json) and the [review](docs/review.md).
