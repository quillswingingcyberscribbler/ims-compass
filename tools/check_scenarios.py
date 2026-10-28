#!/usr/bin/env python3
"""Bounded read-only IMS scenarios using existing audit evaluator.

All input changes are in memory. This script does not recalculate or save XLSX
files. The evaluator is purpose-limited and is not a native Excel engine.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re
import sys
import warnings

import excel_eval as ee


class AuditEvaluator(ee.Evaluator):
    def eval(self, node, sheet):
        if node[0] == "fn" and node[1] == "TRIM":
            value = self.eval(node[2][0], sheet)
            return ee.map1(lambda x: re.sub(r" +", " ", ee.text(x)).strip(" "), value)
        if node[0] == "fn" and node[1] == "MOD":
            values = [self.eval(a, sheet) for a in node[2]]
            return ee.num(values[0]) % ee.num(values[1])
        return super().eval(node, sheet)


def serial(value):
    return ee.to_excel(value) if isinstance(value, (datetime.datetime, datetime.date)) else value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook-dir", type=Path, default=Path(__file__).resolve().parents[1] / "workbooks", help="Directory containing the four original v2.6.1 filenames")
    parser.add_argument("--output", type=Path, required=True, help="JSON report path; no workbook is written")
    parser.add_argument("--allow-known-defects", action="store_true", help="Permit documented failed behaviors while keeping them visibly failed in the JSON.")
    args = parser.parse_args()
    files = {
        "en-demo": "IMS-Compass-v2.6.1-EN.xlsx", "en-clean": "IMS-Compass-v2.6.1-EN-Clean-Start.xlsx",
        "de-demo": "IMS-Kompass-v2.6.1.xlsx", "de-clean": "IMS-Kompass-v2.6.1-Leerstart.xlsx",
    }
    results = []
    for language in ("en", "de"):
        demo = AuditEvaluator(args.workbook_dir / files[language + "-demo"])
        clean = AuditEvaluator(args.workbook_dir / files[language + "-clean"])
        mapping = dict(zip(demo.cells if language == "en" else ["Setup", "Instructions", "StatusGlossary", "ISMS-Foundations", "AI-Supplements", "Governance", "Home", "JobAid", "ReleaseChecks", "Overview", "Report", "Actions", "Checks", "Implementations", "Risks", "Safeguards", "Decisions", "Issues", "Obligations", "Objectives", "StandardView", "TargetCoverage", "Assessments", "Coverage", "CoverageRules", "Scope", "Objects", "Controls", "Requirements", "Mappings", "MasterData", "Documents", "ChangeLog", "TaskBase"], demo.cells))
        sh = lambda name: mapping[name]
        def source_value(sheet, address):
            return serial(demo.cells[sh(sheet)].get(address, (None, "n"))[0])
        def inputs(sheet, source_row, columns, target_row=None):
            target_row = source_row if target_row is None else target_row
            return {(sh(sheet), column + str(target_row)): source_value(sheet, column + str(source_row)) for column in columns}
        def scenario(name, evaluator, changes, reads, expected, meaning, kind="functional"):
            evaluator.reset(changes)
            actual = {}
            errors = []
            for sheet, address in reads:
                try:
                    actual[sheet + "!" + address] = serial(evaluator.cell(sheet, address))
                except Exception as exc:
                    actual[sheet + "!" + address] = "EVALUATOR ERROR: " + str(exc)
                    errors.append(str(exc))
            def matches(value, expectation):
                if isinstance(expectation, dict) and "not_in" in expectation:
                    return value not in expectation["not_in"]
                return value == expectation
            result = {"name": language + "-" + name, "workbook": files[language + ("-clean" if evaluator is clean else "-demo")], "kind": kind,
                "changes": [{"sheet": s, "cell": a, "value": serial(v)} for (s, a), v in changes.items()],
                "actual": actual, "expected_correct": expected, "expected_behavior_met": not errors and all(matches(actual[k], value) for k, value in expected.items()),
                "interpretation": meaning, "evaluator_errors": errors}
            results.append(result)
            result["known_defect"] = kind == "functional" and not result["expected_behavior_met"]
        def expected_values(pairs):
            return {sh(s) + "!" + a: v for s, a, v in pairs}
        def reads(*pairs):
            return [(sh(s), a) for s, a in pairs]
        invalid = {"not_in": [None, "", "OK"], "meaning": "A nonblank rejection of an invalid/duplicate record"}
        # Create one complete membership using a second object row so that the
        # separate first-row object defect cannot mask the rule validation bug.
        first = {}
        first.update(inputs("MasterData", 35, "ABCDE"))
        first.update(inputs("Scope", 8, "ABCDEFGHIJ"))
        first.update(inputs("Scope", 25, "ABCDEFGH"))
        first.update(inputs("Objects", 9, "ABCDEFGHIJY"))
        first[(sh("Objects"), "D9")] = None
        first.update(inputs("CoverageRules", 8, "ABCDEFGHO"))
        first.update({(sh("Documents"), c + "8"): v for c, v in zip("ABCDEFGHIJK", ["DOC-MS-IS", "Procedure definition" if language == "en" else "Verfahrensfestlegung", "S-010", "Test scope", "v1", "PERSON-01", "Released" if language == "en" else "Freigegeben", 46023, 46387, "Test document location", "Test scope criteria"])})
        active = "In Scope" if language == "en" else "Im Geltungsbereich"
        # Read the actual membership selector rather than guess localisation.
        active = first[(sh("Scope"), "D25")]
        scenario("first-record-prerequisites", clean, first,
            reads(("MasterData", "F35"), ("Scope", "K8"), ("Objects", "K9"), ("Scope", "I25"), ("Scope", "L25"), ("Controls", "I8")),
            expected_values([("MasterData", "F35", "OK"), ("Scope", "K8", "OK"), ("Objects", "K9", "OK"), ("Scope", "I25", "OK"), ("Scope", "L25", active), ("Controls", "I8", "OK")]),
            "A complete person, MS, second-row object and membership form a valid one-object target population.", "control")
        scenario("first-new-rule", clean, first,
            reads(("CoverageRules", "I8"), ("CoverageRules", "J8"), ("CoverageRules", "L8")),
            expected_values([("CoverageRules", "I8", "OK"), ("CoverageRules", "J8", 1), ("CoverageRules", "L8", 1)]),
            "Valid input cannot turn the absent rule validator into OK: the rule remains excluded from its expected-target and missing-assignment counts.")
        object_first = {k: v for k, v in first.items() if not (k[0] == sh("Objects") and k[1].endswith("9"))}
        object_first.update(inputs("Objects", 9, "ABCDEFGHIJY", 8))
        object_first[(sh("Objects"), "D8")] = None
        scenario("first-object-row", clean, object_first,
            reads(("Objects", "K8"), ("Scope", "I25"), ("Scope", "L25")),
            expected_values([("Objects", "K8", "OK"), ("Scope", "I25", "OK"), ("Scope", "L25", active)]),
            "The first prepared object row lacks a live validator, so a complete first object prevents its membership from becoming current.")
        scenario("empty-coverage-register", clean, {}, reads(("Coverage", "L8"), ("Coverage", "L15")),
            expected_values([("Coverage", "L8", None), ("Coverage", "L15", None)]),
            "Empty clean-start coverage rows retain the old demo OK/mode-mismatch labels.")
        new_coverage = inputs("Coverage", 8, "ABCDEFGHIJK", 21)
        new_coverage[(sh("Coverage"), "A21")] = "COV-NEW-TEST"
        new_coverage.update({(sh("Coverage"), c + "8"): None for c in "ABCDEFGHIJK"})
        scenario("new-coverage-in-first-unused-row", demo, new_coverage, reads(("Coverage", "L21"), ("CoverageRules", "K8")),
            expected_values([("Coverage", "L21", "OK"), ("CoverageRules", "K8", 1)]),
            "A complete previously valid row is moved from row 8 to the first unused row 21, assigned a fresh ID, and removed from row 8. Row 21 has no validator, so a valid new assignment disappears from the valid-coverage count.")
        dup = {(sh("Coverage"), "A9"): source_value("Coverage", "A8"), (sh("Coverage"), "B9"): source_value("Coverage", "B8"), (sh("Coverage"), "C9"): source_value("Coverage", "C8")}
        scenario("duplicate-coverage-id-and-rule-target", demo, dup, reads(("Coverage", "L8"), ("Coverage", "L9"), ("CoverageRules", "K8")),
            expected_values([("Coverage", "L8", invalid), ("Coverage", "L9", invalid), ("CoverageRules", "K8", 0)]),
            "Both old coverage rows keep OK; the valid-coverages count rises to 2 for one target. Expected 0 follows the workbook's unique-ID contract, which makes both duplicate records invalid.")
        bad = {(sh("Coverage"), "D8"): "NO-SUCH-IMPLEMENTATION"}
        scenario("invalid-coverage-reference", demo, bad, reads(("Coverage", "L8"), ("Coverage", "M8"), ("CoverageRules", "K8")),
            expected_values([("Coverage", "L8", invalid), ("Coverage", "M8", "Reference missing" if language == "en" else "Referenz fehlt"), ("CoverageRules", "K8", 0)]),
            "The current-evidence formula sees the missing implementation, but the frozen OK validation still counts the row as a valid coverage assignment.")
        dup_rule = {(sh("CoverageRules"), "A9"): source_value("CoverageRules", "A8")}
        scenario("duplicate-rule-id", demo, dup_rule, reads(("CoverageRules", "I8"), ("CoverageRules", "I9"), ("CoverageRules", "J8"), ("CoverageRules", "J9")),
            expected_values([("CoverageRules", "I8", invalid), ("CoverageRules", "I9", invalid), ("CoverageRules", "J8", 0), ("CoverageRules", "J9", 0)]),
            "Both duplicate rule IDs retain OK and each continues counting its target population.")
        scenario("baseline-zero-versus-blank", demo, {}, reads(("Objectives", "P10"), ("Objectives", "P11")),
            expected_values([("Objectives", "P10", "Target value reached" if language == "en" else "Zielwert erreicht"), ("Objectives", "P11", "Measurement open" if language == "en" else "Messung offen")]),
            "Existing measured zero remains distinct from a missing measurement.", "control")
        # Recheck the corrected locale-sensitive branches with changed inputs.
        scenario("report-N42-selection", demo, {(sh("StandardView"), "B4"): "MS-AIMS"},
            reads(("Report", "C4"), ("Report", "C10")), expected_values([("Report", "C4", "N42"), ("Report", "C10", 40)]),
            "Changing the standard selector counts 38 N42 reference controls plus two sample internal requirements.", "control")
        scenario("production-only-coverage", demo, {(sh("CoverageRules"), "O11"): "Production" if language == "en" else "Produktivbetrieb"},
            reads(("CoverageRules", "J11"), ("CoverageRules", "L11"), ("TargetCoverage", "G9"), ("TargetCoverage", "G10")),
            expected_values([("CoverageRules", "J11", 1), ("CoverageRules", "L11", 0), ("TargetCoverage", "G9", "Yes" if language == "en" else "Ja"), ("TargetCoverage", "G10", "No" if language == "en" else "Nein")]),
            "A production-only REG-004 selects S-020 and excludes the draft test service.", "control")
        scenario("inactive-coverage-rule", demo, {(sh("CoverageRules"), "F11"): "No" if language == "en" else "Nein"},
            reads(("CoverageRules", "J11"), ("TargetCoverage", "G9"), ("TargetCoverage", "G10")),
            expected_values([("CoverageRules", "J11", 0), ("TargetCoverage", "G9", "No" if language == "en" else "Nein"), ("TargetCoverage", "G10", "No" if language == "en" else "Nein")]),
            "An inactive REG-004 contributes no expected targets in either language.", "control")
        # Governance now checks unique IDs. Linked record validity is separate.
        defined = "Defined" if language == "en" else "Festgelegt"
        base = {(sh("Governance"), "D9"): "In this workbook" if language == "en" else "In dieser Mappe",
                (sh("Governance"), "F16"): "PERSON-01", (sh("Governance"), "C19"): "METHOD-01",
                (sh("Governance"), "C20"): "AUTH-01", (sh("Governance"), "C22"): "DOC-METH",
                (sh("Governance"), "C23"): "PERSON-06", (sh("Governance"), "H22"): 46302,
                (sh("Governance"), "F23"): 46330}
        checks = [
            ("valid-reference-set", {}, defined),
            ("invalid-responsible-id", {("Governance", "F16"): "MISSING"}, "Review responsibility" if language == "en" else "Verantwortung prüfen"),
            ("invalid-method-id", {("Governance", "C19"): "MISSING"}, "Review risk method" if language == "en" else "Risikomethode prüfen"),
            ("invalid-mandate-id", {("Governance", "C20"): "MISSING"}, "Review mandate" if language == "en" else "Mandat prüfen"),
            ("invalid-evidence-id", {("Governance", "C22"): "MISSING"}, "Review evidence document" if language == "en" else "Belegdokument prüfen"),
            ("invalid-confirmer-id", {("Governance", "C23"): "MISSING"}, "Review confirming person" if language == "en" else "Bestätigende Person prüfen"),
            ("duplicate-responsible-id", {("MasterData", "A41"): "PERSON-01"}, "Review responsibility" if language == "en" else "Verantwortung prüfen"),
            ("expired-confirmation", {("Governance", "F23"): 46302}, "Review due" if language == "en" else "Überprüfung fällig"),
        ]
        for label, changes, wanted in checks:
            translated = {(sh(s), a): v for (s, a), v in changes.items()}
            scenario("governance-" + label, demo, {**base, **translated}, reads(("Governance", "L9")),
                expected_values([("Governance", "L9", wanted)]), "Unique reference and confirmation-date validation.", "control")
        bad_definition = {"not_in": [defined], "meaning": "An invalid linked prerequisite must not produce a completed definition."}
        linked = [
            ("invalid-linked-method", {("MasterData", "E82"): 0}, ("MasterData", "M82"), "Review method limits" if language == "en" else "Methodengrenzen prüfen"),
            ("invalid-linked-mandate", {("MasterData", "B99"): "MISSING"}, ("MasterData", "J99"), "Review person ID" if language == "en" else "Personen-ID prüfen"),
            ("unreleased-linked-evidence", {("Documents", "G8"): "Draft" if language == "en" else "Entwurf"}, ("Documents", "M8"), "Not released" if language == "en" else "Nicht freigegeben"),
        ]
        for label, changes, linked_cell, linked_status in linked:
            translated = {(sh(s), a): v for (s, a), v in changes.items()}
            scenario("governance-" + label, demo, {**base, **translated}, reads(("Governance", "L9"), linked_cell),
                expected_values([("Governance", "L9", bad_definition), (*linked_cell, linked_status)]),
                "The referenced record is invalid or unreleased, but the definition remains complete because only its ID is checked.")
    report = {"review_date": "2026-10-23", "package_version": "0.1.0-review.2", "method": "Purpose-limited read-only source-formula evaluator; all changes only in memory; no native Excel execution, no XLSX saves.",
              "input_sha256": {name: hashlib.sha256((args.workbook_dir / name).read_bytes()).hexdigest() for name in files.values()},
              "count": len(results), "behavior_passed": sum(r["expected_behavior_met"] for r in results), "evaluator_errors": sum(bool(r["evaluator_errors"]) for r in results), "scenarios": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    report["behavior_failed"] = len(results) - report["behavior_passed"]
    report["known_defect_failures"] = sum(r["known_defect"] for r in results)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("count", "behavior_passed", "behavior_failed", "known_defect_failures", "evaluator_errors")}, indent=2))
    failures = [r for r in results if not r["expected_behavior_met"] and not (args.allow_known_defects and r["known_defect"] and not r["evaluator_errors"])]
    return 1 if failures else 0


if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
    sys.exit(main())
