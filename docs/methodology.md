# Methodology

IMS Compass connects management-system definitions to the objects, evidence and decisions that give them operational meaning. The supplied source combines information-security management and AI management. Its catalogue uses N27 for ISO/IEC 27001:2022 and N42 for ISO/IEC 42001:2023.

This document describes the intended model and the supplied architecture. [Known calculation defects](known-issues.md) currently interrupt parts of that model.

## Shared foundations and specific assessments

ISMS-Foundations records existing definitions with their source, version, applicability, responsibility and approval evidence. AI-Supplements records whether each definition can be adopted unchanged, needs amendment, or should be governed separately. Five additional AI topics supplement the 30 shared topics.

`Documented` means that a foundational definition has been recorded with its required source information. It is not a standard-conformity judgement. The standard-specific assessments remain separate.

Governance identifies where risk information is managed for each management system. Internal mode enables direct use of the local risk register. External mode records references and reconciliation information while the specialised external system remains authoritative. The v2.6.1 confirmation formulas check unique referenced IDs and confirmation dates. They still need to propagate invalid method/mandate status and unreleased evidence before a definition can be treated as complete.

## The main relationships

| Layer | Records | What it establishes |
| --- | --- | --- |
| Applicability | Scope and Objects | Which objects belong to which management system, in which version and operating mode |
| Requirement | Requirements and Assessments | Which reference is considered and the expert's applicability and fulfilment judgement |
| Control contribution | Controls and Mappings | Which control contributes to which requirement, and what evidence it needs |
| Expected population | CoverageRules and scope memberships | Which objects should be covered, independently of the coverages already recorded |
| Implementation | Implementations and Coverage | Which concrete implementation covers each object and whether transfer is justified |
| Evidence | Documents and Checks | What was checked, against which object and version, with what result and release state |
| Follow-up | Issues, Actions and Obligations | What remains open and what evidence is needed for closure or fulfilment |
| Decision | Risks and Decisions | Which authorised resolution applies, with which conditions and time limit |

Parent-object relationships provide context. They do not automatically inherit evidence, fulfilment or scope. Central coverage requires an explicit transferability record and matching implementation and target-object versions.

## Expected coverage comes before recorded coverage

A coverage rule identifies a management system, control, object type and applicable operating mode. Its expected population comes from current valid scope memberships. The model then compares that population with recorded coverages.

This prevents the absence of a coverage row from making an object disappear from the assessment. In the supplied example, REG-004 applies to two IT systems. S-020 has a coverage record; S-021 lacks one. The expected result is therefore two objects and one missing assignment. The repaired v2.6.1 English formulas now show those counts. Separate missing live-validation formulas still make new or changed rule/coverage records unreliable; see the current issue list.

## Evidence and approval are different dimensions

A verification record identifies its subject, object, checked version, timestamp, depth, result, checking person, evidence location and release state. A released verification record can contain a negative result. Release means that the record is approved for use; it does not convert its result into positive evidence.

An implementation's current status also considers matching versions, required check depth, validity, newer or simultaneous checks, relevant counter-findings and due obligations. An older positive check should not conceal a newer negative observation.

The intended `OK` input-validation status indicates formal completeness under the implemented rules. The current coverage and rule columns contain static labels, so their `OK` is not reliable validation after input changes. Users still need to read the technical result and its evidence. The workbook does not inspect the substantive contents of an external document merely because its location is recorded.

## Current status and historical closure

The reporting date is a deliberate input in Setup. All four supplied files currently use 8 October 2026; this is the deliberate demo date and must be reviewed when initializing a new working file. Current evidence and authorisations are evaluated against that date, including the day itself where specified in the workbook's procedure.

An action's historical closure is assessed against the evidence valid at the time of closure. A later routine evidence expiry should not reopen a properly accepted action. The implementation's current operational assurance is evaluated separately. This distinction supports both reproducible past decisions and current work queues.

Preserve released check records with stable IDs. Create a new record for a new check rather than overwriting the original date, subject or result. The manual ChangeLog supports explanation but does not provide a complete technical audit trail.

## Risks, authority and agent autonomy

The demonstration risk method multiplies likelihood on a 1–5 scale by the higher of organisational and affected-party impact, also on a 1–5 scale. Its thresholds, decision classes and method definitions are explicit master data. It is an ordinal prioritisation method, not a monetary loss estimate or an empirically calibrated probability model. Scores should not be added or compared across incompatible method configurations.

Mandates specify person, role, management system, decision class, monetary limit, period and authority basis. An organisation chart level alone does not establish a mandate. A risk acceptance does not change the underlying evidence status of a control.

Autonomy approval combines permitted mode, amount limit, conditions, validity, technical enforcement and fallback state. The workbook records the decision and evidence. The actual system must implement and test the corresponding restrictions. The D-003 example permits draft operation only within its stated scope and dates.

## Boundaries of the implementation

Each v2.6.1 edition has 34 sheets and 74,555 formula cells. Prepared register capacities are finite and encoded in formulas, tables, validation and output ranges. Extending only a visible table can leave records outside the calculations. Review all dependent ranges as one change.

Sheet protection is intentionally passwordless and is meant to prevent accidental formula overwriting. File access and version retention need to be managed in the operating environment. The repository preserves source artifacts; it is not the operational record store.

Each demo catalogue contains 193 external references and two sample internal requirements. The starting editions retain the 193 external references and remove the two internal examples. Its short topic descriptions are described in the workbook as orientation text. Completeness and interpretation must be checked against the controlled standards used by the organisation. This project does not provide a certification decision or claim that a populated workbook establishes conformity.
