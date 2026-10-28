> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

# Validation scope

Review date: 22 October 2026. Package: `0.1.0-review.1`. Source versions: IMS Compass v2.6 (both supplied copies).

## Three distinct checks

| Check | What it establishes | What it does not establish |
| --- | --- | --- |
| Package integrity | ZIP/XML structure, internal relationships, source hashes, local documentation links and saved Excel error cells | Fresh calculation or correct decision logic |
| Model and scenario checks | The specific arithmetic, reference calculations and recorded input scenarios in this project's review | Every possible input, valid evidence or real-world model calibration |
| Native application acceptance | Input editing, recalculation, save/reopen, dropdowns, charts and print behavior in the named Excel version | Not performed in native Microsoft Excel; remains a release task. |

Read the [full review](review.md) for exact counts, known defects, test methods and limitations. [release-status.json](../../../validation/history/0.1.0-review.1/release-status.json) records the current readiness status. Source checksums are in [manifest.json](../../../validation/history/0.1.0-review.1/manifest.json).

Run the portable package check with:

```bash
python3 tools/validate_repository.py
```

It is deliberately named Package integrity in GitHub Actions. Known logical defects do not necessarily cause an OOXML or cached-error failure. A green workflow must not be described as verification of all workbook decisions.

The workflow pins `actions/checkout` to the [v6.1.0 source commit](https://github.com/actions/checkout/commit/d23441a48e516b6c34aea4fa41551a30e30af803), uses a read-only token, and does not publish a release. The hosted workflow has not been run because this package has no remote repository yet. Its local check command was executed during preparation.

## Native Excel release acceptance

After correcting the documented issues, record the Excel build and platform, use a disposable working copy, test the stated normal and boundary scenarios, then save, close and reopen. Check affected output cells, retained formulas and dropdowns, charts and print views. Confirm source changes against a cell-level change list. Update the manifest only after that review. Keep a separate untouched source baseline for provenance.
