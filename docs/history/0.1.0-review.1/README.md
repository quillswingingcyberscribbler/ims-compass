> Historical audit, reviewed 22 October 2026 for package `0.1.0-review.1` and source v2.6. It does not describe the current v2.6.1 workbooks. Old workbook files are not included in the current distribution; their hashes remain in the historical manifest.

<img src="../../../assets/logo.png" alt="IMS Compass logo" width="160">

# IMS Compass

An Excel workbench for connecting information-security and AI management systems, scope, evidence, risks, actions and decisions.

**Status: reviewed prerelease.** Repository package `0.1.0-review.1` contains the unchanged v2.6 source workbooks, a detailed review, reproducible checks and proposed corrections. The review found blocking calculation defects. The proposed patches have **not** been applied, and verification in Microsoft Excel remains pending.

## Start here

1. Open `IMS-Compass-v2.6-EN.xlsx` in desktop Excel using a local working copy.
2. Read the [known issues](known-issues.md) before using coverage totals or report counts.
3. Begin on **Setup**, then use **JobAid** to follow an evidence or action example. **Home** provides the operational task view.

The workbook's reporting date is **8 October 2026**. Its records and named people are fictitious examples. Change the reporting date deliberately when evaluating a new working copy.

The second supplied file, `IMS-Compass-v2.6-Clean-Start.xlsx`, has the same populated cell contents as the EN workbook. Its filename does not describe an empty template. Both originals are preserved for provenance. A [clean-start plan](clean-start-plan.md) defines the work needed to produce a genuine starting edition.

## What it connects

| Question | Main views |
| --- | --- |
| Which existing definitions can the management systems share? | Setup, ISMS-Foundations, AI-Supplements, Governance |
| Which objects and controls belong in scope? | Scope, Objects, Requirements, Controls, Mappings |
| What evidence supports the current judgement? | CoverageRules, Coverage, Implementations, Checks, Assessments |
| What needs action, acceptance or a decision? | Home, Actions, Issues, Risks, Decisions, Obligations, Objectives |
| What can management or an assessor review? | Overview, StandardView, TargetCoverage, Report |

The model distinguishes input completeness, evidence, current operational status and historical closure. It does not automatically enforce an agent's permissions or determine standard conformity.

## Review findings that affect results

| Finding in the supplied example | Effect |
| --- | --- |
| German `Ja` / `Nein` literals remain in English coverage formulas | Expected coverage reports 0 instead of 13 combinations; a missing assignment is suppressed |
| The report counts German reference-type names | N27 control count is 0 instead of 93 |
| Foundation formulas test `Offen` against `Open` | 63 open topics incorrectly display `Review selection` |
| `Objects!K8` contains a fixed validation message | Correcting its inputs cannot update the message |

The [review](review.md) provides cell references, observed results and testing limits. The [formula correction plan](../../../validation/history/0.1.0-review.1/formula-patch-plan.json) specifies 366 functional edits and 849 optional English display-language edits. [Issues to open](issues-to-open.md) turns the findings into implementation tasks with acceptance criteria.

## Run the checks

Python 3 is optional for workbook users. The checks use only its standard library.

```bash
python3 tools/validate_repository.py
python3 tools/check_ims.py workbooks/IMS-Compass-v2.6-EN.xlsx --compare workbooks/IMS-Compass-v2.6-Clean-Start.xlsx
```

The repository validator checks package integrity, links, saved error cells and file hashes. The IMS checker checks the supplied sample state and **returns a failure status while the known defects remain**. Its recorded result is [7 passing and 9 failing assertions](../../../validation/history/0.1.0-review.1/regression-results.json). Neither script recalculates the workbook in Microsoft Excel or proves the correctness of all possible inputs.

## Documentation

- [Quickstart](quickstart.md) — a short route through the workbook and its checks.
- [Methodology](methodology.md) — objects, scope, evidence, dates and decisions.
- [Review](review.md) — findings and verification evidence.
- [Known issues](known-issues.md) — release blockers and practical limitations.
- [Clean-start plan](clean-start-plan.md) — a controlled reset of the demonstration data.

Licensing is pending; see [LICENSE-STATUS.md](../../../LICENSE-STATUS.md). Citation information is in [CITATION.cff](../../../CITATION.cff).
