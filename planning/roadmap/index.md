# IssueOps roadmap records

This directory contains stage-level intent records.

Roadmap records explain the problem, outcome to prove, exclusions, authority boundaries, target state, acceptance evidence and proposed delivery slices. Detailed implementation contracts remain in GitHub issues.

## Status vocabulary

```text
shaping
approved
delivering
completed
superseded
```

## Templates

- [Stage roadmap template](stage-template.md)

## Retrospective records

- [Stage 1 — Manual execution-contract foundation](stage-01-manual-execution-contract-foundation.md) — completed retrospective reconstruction.
- [Stage 2 — Published and hardened operating model](stage-02-operating-model-hardening.md) — completed retrospective reconstruction.

Retrospective records must not claim that the complete planning structure existed before delivery.

## Completed contemporaneous stages

- [Stage 3 — Read-only evidence-pack assistance](stage-03-read-only-evidence-pack-assistance.md) — completed with an **Adapt** decision.

Stage 3 delivered the deterministic evidence schema, local renderer and manually invoked read-only GitHub collection for one pull request. Live pending-to-final dogfood proved the core safety and usefulness, while missing non-closing issue linkage and manual-dispatch friction prevented unconditional adoption.

## Active approved roadmap

- [Stage 4 — Diátaxis documentation architecture](stage-04-diataxis-documentation-architecture.md) — approved through planning issue [#93](https://github.com/8ft0-ai/IssueOps/issues/93).

Stage 4 will incrementally organise the user-facing documentation around tutorials, how-to guides, reference and explanation. Planning, delivery history, tests, scripts, workflows and implementation-adjacent material remain outside the substantive Diátaxis tree, and all existing IssueOps authority boundaries remain unchanged.

## Future stages

Issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90) remains shaping-only for a possible Stage 5 — Operational evidence assistance. It has no implementation authority until independently reviewed and approved.

No roadmap authorises lifecycle automation, execution triggering, auto-merge, repository-setting changes or broader operational evidence assistance unless those capabilities are explicitly shaped, approved and delivered through their own execution contracts.
