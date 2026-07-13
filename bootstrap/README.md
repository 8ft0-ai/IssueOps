# Portable IssueOps bootstrap source pack

This directory is the adaptable source area for **IssueOps Bootstrap 0.1**.

It exists to help an unfamiliar agent assess an existing repository, preserve its conventions, select the lightest sufficient adoption posture and prepare the first local bootstrap execution contract. It is not an installer, a second IssueOps protocol or remote authority to mutate another repository.

## Pack contents

- [Repository assessment and adoption-posture form](repository-assessment.md) — records read-only evidence, local capability mapping, posture selection and the proposed first write.
- [Convention-mapping guidance](convention-mapping.md) — maps IssueOps controls to existing repository owners before new artefacts are proposed.
- [Local bootstrap execution-contract template](bootstrap-issue-template.md) — prepares the first locally governed issue after assessment and explicit owner permission.

Start from the root [bootstrap entry point](../BOOTSTRAP.md).

## Implemented baseline

The bootstrap exports only the implemented manual IssueOps baseline:

- the GitHub issue is the execution contract;
- readiness and dependency evidence precede branch creation;
- an implementation plan records the proposed path;
- safe-operation checks govern mutation;
- one issue-scoped branch contains the change;
- validation matches the change and final state;
- the pull request is the evidence pack;
- review checks both contract fulfilment and scope control; and
- human approval or explicit bounded local delegation governs merge.

The authoritative lifecycle is the [IssueOps operating protocol](../docs/issueops-protocol.md). Exact fields, formats and boundaries remain in the focused [Reference documentation](../docs/reference/index.md).

The bootstrap does not export planned operational evidence assistance from issue #90 or planned modular session architecture from issue #113.

## Authority handoff

Reading a remote bootstrap specification authorises only this pre-contract sequence:

```text
read-only target-repository assessment
  -> adoption-posture recommendation
  -> one locally authorised bootstrap execution-contract issue
  -> normal local IssueOps lifecycle begins
```

Before a local issue exists and is ready, an agent may inspect repository instructions, contributor guidance, issue and pull-request templates, validation commands, branch conventions, merge policy and existing planning records. It may map capabilities, identify gaps and prepare the proposed local issue.

Creating that one local issue requires target-repository owner permission. The remote specification does not itself grant permission to create the issue.

Before the local issue is ready and planned, the agent must not:

- create or change repository files;
- create a branch or pull request;
- add workflows, bots, apps, generators, installers or schemas;
- change labels, settings, permissions, required checks or branch protection;
- configure auto-merge;
- change application code; or
- treat the remote specification as approval, merge or publication authority.

The target repository's local issue, instructions, validation rules and human authority govern every mutation.

## Adoption postures

The entry point and assessment material select one posture.

### Already compatible

Use when the repository already has effective equivalents for the manual IssueOps controls. Map the existing surfaces and propose only material corrections. A no-change recommendation is valid.

### Minimal manual adoption

Use by default when material controls are missing but dependent stage planning is not justified. Add or adapt only the minimum surfaces needed for execution contracts, agent guidance, pull-request evidence, validation and explicit human authority.

### Stage-capable adoption

Use only when the repository genuinely needs dependent multi-issue planning, cross-cutting governance, end-to-end proof or a formal adoption close-out. Stage machinery is not installed for symmetry.

## Adapt capabilities, not filenames

A target repository is not required to copy this repository's layout or terminology.

Before proposing a new artefact, map the local equivalent for:

- agent instructions;
- contributor guidance;
- issue contracts;
- readiness and implementation planning;
- branch naming and base selection;
- validation commands and required evidence;
- pull-request templates and review rules;
- merge authority; and
- multi-issue planning, when genuinely needed.

Reuse or adapt an existing owner when it is clear and compatible. Do not create a duplicate control surface merely to introduce IssueOps terminology.

## Source ownership

Each source has one primary responsibility.

| Surface | Primary owner |
| --- | --- |
| Root `BOOTSTRAP.md` | Concise external agent entry point, authority boundary, posture selection path, first-local-issue rule, prohibited defaults and version links. |
| `bootstrap/` | Adaptable assessment, mapping and local-issue source material. |
| `docs/how-to/adopt-issueops-in-an-existing-repository.md` | Human procedure for preparing, supervising, reviewing and proving an adoption. |
| `docs/reference/issueops-bootstrap-requirements.md` | Exact normative bootstrap inputs, capability requirements, posture rules, version fields, evidence levels and authority constraints. |
| `docs/issueops-protocol.md` and focused Reference pages | Canonical IssueOps lifecycle, fields, formats, validation, evidence and merge rules. |
| `planning/` | Approved intent, delivery relationships, pilot evidence, limitations and final Adopt, Adapt or Reject decision. |

These surfaces link to one another rather than copying complete content. If a proposed artefact does not own a distinct tested need, do not add it.

## Smallest coherent pack

Version 0.1 contains only the source material needed to:

1. assess the repository without mutation;
2. select and justify one adoption posture;
3. map existing conventions and identify material gaps; and
4. create a complete local bootstrap execution contract.

Separate agent-rule, issue-form, pull-request or stage templates should be added only when evidence shows that adapting existing repository surfaces is not sufficient.

## Version identity

Adoption records must distinguish:

- **Current recommended entry point:** the mutable `main` version of `BOOTSTRAP.md`.
- **Pinned reproducible entry point:** an immutable commit URL for the exact `BOOTSTRAP.md` used by the target repository.
- **Specification identity:** `IssueOps Bootstrap 0.1` and the implemented baseline it represents.

A target repository should record the pinned source it actually used even when the current recommendation later changes.

## Canonical supporting references

Use the focused sources rather than duplicating their rules:

- [Execution-contract fields](../docs/reference/execution-contract-fields.md)
- [Readiness and dependency formats](../docs/reference/readiness-and-dependency-formats.md)
- [Implementation-plan format](../docs/reference/implementation-plan-format.md)
- [Operation permissions and evidence](../docs/reference/operation-permissions-and-evidence.md)
- [Validation status and fallback policy](../docs/reference/validation-status-and-fallback-policy.md)
- [Pull-request evidence requirements](../docs/reference/pr-evidence-requirements.md)
- [Review decisions and merge blockers](../docs/reference/review-decisions-and-merge-blockers.md)
- [Delegated batch mode](../docs/delegated-batch-mode.md)

## Current delivery boundary

The approved roadmap is [Portable IssueOps bootstrap and adoption](../planning/roadmap/portable-issueops-bootstrap-and-adoption.md).

Human adoption guidance and exact normative bootstrap requirements are delivered separately under the adopted documentation architecture. External pilot execution remains separately governed and requires an exact target repository, stable branch, permitted scope and merge authority before any target-repository access or mutation.
