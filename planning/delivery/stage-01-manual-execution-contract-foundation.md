# Stage 1 — Manual execution-contract foundation

Status: completed.

## Original documented intent

[Issue #1](https://github.com/8ft0-ai/IssueOps/issues/1) defined the foundational problem: agentic coding work needed a structured issue contract, a manual workflow and a pull-request evidence model before automation.

The original intent centred on the issue as execution contract, the agent as contract-bound implementer, the pull request as evidence pack and a human as the merge decision-maker.

## Retrospective interpretation

Stage 1 is reconstructed from the foundational issue and the Stage 1.x work that followed. The complete stage pack did not exist contemporaneously.

Issues #3, #10, #14 and #17 emerged after the first foundation was delivered. They represent observed gaps and baseline hardening, not a backlog that was fully known when #1 began.

The strongest retrospective stage boundary is the work from issue #1 through the `v0.1.0` release preparation in issue #17.

## What shipped

Stage 1 delivered:

- a structured execution-contract issue model;
- the manual issue → readiness → plan → branch → implementation → validation → PR → review → merge loop;
- pull-request evidence and contract-verification language;
- worked execution-contract and review examples;
- manual label guidance;
- a safe tool-operation check and circuit-breaker protocol;
- lightweight validation expectations for documentation and template changes;
- agent operating rules in `AGENTS.md`; and
- the `v0.1.0` manual baseline release notes.

## Linked issues and pull requests

Foundation and proof:

- [Issue #1 — establish agentic execution-contract IssueOps](https://github.com/8ft0-ai/IssueOps/issues/1)
- [PR #2 — Stage 1 foundation](https://github.com/8ft0-ai/IssueOps/pull/2)
- [Issue #3 — dogfood the workflow](https://github.com/8ft0-ai/IssueOps/issues/3)
- [PR #9 — dogfood examples and contract verification](https://github.com/8ft0-ai/IssueOps/pull/9)

Hardening and release:

- [Issue #10 — lightweight validation](https://github.com/8ft0-ai/IssueOps/issues/10)
- [PR #16 — add lightweight validation](https://github.com/8ft0-ai/IssueOps/pull/16)
- [Issue #14 — safe tool-operation protocol](https://github.com/8ft0-ai/IssueOps/issues/14)
- [PR #15 — add safe tool-operation protocol](https://github.com/8ft0-ai/IssueOps/pull/15)
- [Issue #17 — prepare the baseline release](https://github.com/8ft0-ai/IssueOps/issues/17)
- [PR #18 — Stage 1 release preparation](https://github.com/8ft0-ai/IssueOps/pull/18)

## Proof runs, checks and artefacts

The strongest Stage 1 proof is the repository using its own manual contract model to deliver the follow-up Stage 1.x work.

Representative artefacts include:

- `README.md` describing the contract model;
- `AGENTS.md` defining agent operating rules;
- `docs/issueops.md` describing the Stage 1 workflow;
- `docs/tool-operations.md` defining the mutation check and circuit breaker;
- `docs/examples/` containing contract and verification examples;
- the pull-request template used as an evidence pack; and
- `docs/releases/stage-1.md` recording the `v0.1.0` baseline.

The Stage 1 pull requests were documentation and template changes. Validation was manual and review-oriented by design; no automated CI proof was claimed.

## Intended versus actual delivery

The initial issue established the core execution-contract thesis. Delivery then exposed two material gaps:

1. a correct contract and plan were insufficient when the wrong repository mutation tool could still be invoked; and
2. pull-request evidence needed a modest repeatable validation model.

The safe tool-operation protocol and lightweight validation guidance were therefore added before the baseline release. These were evidence-based additions to the stage, not part of a fully pre-planned roadmap.

The preferred slash-based branch naming also encountered connector limitations during the bootstrap. The repository documented the preferred convention while accepting the actual bootstrap branch evidence.

## Observed limitations and friction

- The workflow remained manual and depended on disciplined human and agent behaviour.
- Validation was guidance rather than repository-native enforcement.
- Labels were documented but not created or enforced.
- The process was dogfooded on bounded documentation work, not application code.
- Public documentation was still fragmented between repository files and broader project memory.
- The stage proved usability for a small loop, not every repository or risk level.

## Boundaries preserved

Stage 1 did not introduce:

- automatic agent execution;
- GitHub Actions orchestration;
- required checks or branch protection;
- automatic label transitions;
- auto-merge;
- release automation; or
- application-code changes.

A human retained scope, review and merge authority throughout.

## Decisions and lessons

The execution-contract model was adopted as the manual foundation.

The most important operational lesson was structural: issue and plan quality do not make unsafe mutations safe. Tool authority and operation verification need their own gate.

The second lesson was that evidence should be specific and modest. A checklist that records what was actually validated is more useful than claiming automation that does not exist.

## Implications for the next stage

Stage 2 needed to preserve the Stage 1 contract while making the model easier to discover, publish, validate and operate. The next stage therefore focused on canonical documentation, Pages publishing, consolidated protocol guidance, stronger evidence practices, bounded delegation and repository-native validation rather than immediate autonomous execution.
