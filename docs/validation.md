# Validation scope and reproduction

Review date: **23 October 2026**. Package: **0.1.0-review.2**. Sources: all four IMS v2.6.1 editions.

## What was verified

| Layer | Result | Boundary |
| --- | --- | --- |
| Package integrity | OOXML structure, internal relationships, local links and four source hashes | Does not establish decision logic or input recalculation |
| Static/cache regression | 84 assertions: 62 pass, 22 documented failures | Supplied editions and fixed sample IDs; not arbitrary organizational data |
| Changed-input formula scenarios | 46 cases: 26 desired behaviors pass, 20 documented failures, zero evaluator errors | Purpose-limited interpreter with input overrides in memory |
| Fresh independent baseline | 298,220 formula-cell results agree with disposable LibreOffice copies, allowing 24 timestamp serialization differences | Confirms the saved baseline, including defects |
| Native Microsoft Excel acceptance | Pending | Edit/recalculate/save/reopen, dropdown, visual and print behavior remain release tasks |

The scenario split is 18 first-record/coverage/zero cases (4 pass, 14 fail), 22 governance cases (16 pass, 6 fail), and 6 corrected-language branch cases (all pass). A reproduced defect remains a failed intended behavior.

## Commands

Python 3.10 or later is sufficient for the first two commands; they use only the standard library:

    python3 tools/validate_repository.py
    python3 tools/check_ims.py --report validation/local-regression-results.json

The second command defaults to all four sources. It can check one positional workbook or use a different --workbook-dir. It exits 1 while the documented defects remain.

The optional scenario harness requires the explicit dependency in [requirements-test.txt](../requirements-test.txt):

    python3 -m pip install -r requirements-test.txt
    python3 tools/check_scenarios.py --output validation/local-scenario-results.json

This command also exits 1 for the current sources. Both IMS scripts support --allow-known-defects for tracking this unchanged prerelease baseline. Failures remain false in the JSON; unexpected failures and evaluator errors still cause a nonzero exit. This option is not a stable-release gate.

Neither script edits or exports an XLSX. The evaluator uses openpyxl for read-only extraction, with no save operation; it does not round-trip or remove the source's extended validations.

## Recorded evidence

- [Main regression results](../validation/regression-results.json)
- [Changed-input scenario results](../validation/scenario-results.json)
- [LibreOffice recalculation results](../validation/recalculation-results.json)
- [Edition comparison](../validation/edition-comparison.json)
- [Reset-region evidence](../validation/reset-scope-evidence.json)
- [Validation-column inventory](../validation/validation-column-inventory.json)
- [Extended-validation preservation inventory](../validation/extended-validations.json)
- [Source manifest](../validation/manifest.json)
- [Release status](../validation/release-status.json)

These records describe the public v2.6.1 copies and their exact hashes. Previous source hashes are retained in [manifest.json](../validation/manifest.json). The [historical evidence](history/README.md) describes v2.6 separately.

## GitHub workflow and release gate

The default workflow is named Repository checks. It runs package integrity and both IMS checkers with their explicit `--allow-known-defects` option, then compares the generated reports exactly with the recorded prerelease evidence. Documented failures remain false in the JSON. An unexpected failure, evaluator error, missing known defect, or changed report fails the comparison. A green workflow therefore means that the same reviewed prerelease baseline reproduced; it is not acceptance of workbook decisions.

The workflow retains the pinned checkout action and read-only token. Local commands were executed during preparation. After import, the repository's Actions tab is the authoritative record of hosted runs.

Run the explicit stable-release declaration check with:

    python3 tools/release_gate.py

It intentionally fails while functional blockers, native Excel acceptance, licensing, or publication-metadata review remain unresolved. The MIT/CC BY 4.0 allocation and publication-metadata review are now complete. Before public visibility, confirm the standards-derived catalogue redistribution rights described in [LICENSE-STATUS.md](../LICENSE-STATUS.md). After functional repairs, complete the [native Excel acceptance record](../validation/native-excel-acceptance.md), test both languages and both starting states, verify save/reopen and native features, then update the source manifest and release record together. Current public-copy identities are recorded in [manifest.json](../validation/manifest.json) and [publication-metadata.json](../validation/publication-metadata.json).
