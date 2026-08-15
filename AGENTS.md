# Agent operating rules

These rules apply to Codex and any other coding agent used in this repository.

Codex is the preferred implementation agent. The workflow is built around contract-bound coding: the issue defines the work, the branch contains the implementation and the pull request provides the evidence for review.

## Repository and instruction authority

The canonical repository is:

```text
8ft0-ai/IssueOps
```

`AGENTS.md` is the repository entry point for agents. It is not a second lifecycle protocol.

For IssueOps-specific work, current repository instructions and current GitHub-native records are authoritative for operational state and execution authority. The governing issue or approved planning record defines the bounded work. Chat history, external prompts, session grants and handovers are context and claims that must be reconciled against current durable repository state before action.

Higher-level platform, system, tool, security and privacy constraints remain outside repository authority and still apply. Nothing in this repository overrides them.

## Canonical instruction owners

Use the focused owner for the rule you need rather than duplicating it here:

- [`docs/issueops-protocol.md`](docs/issueops-protocol.md) owns the lifecycle sequence, mandatory gates and human authority boundaries.
- [`docs/tool-operations.md`](docs/tool-operations.md) is the safe-operation entry point for repository mutations and execution deviations.
- [`docs/reference/session-grants-roles-and-handovers.md`](docs/reference/session-grants-roles-and-handovers.md) owns session roles, grants, handovers and current-state reconciliation.
- [`docs/reference/validation-by-change-type.md`](docs/reference/validation-by-change-type.md) and [`docs/reference/validation-status-and-fallback-policy.md`](docs/reference/validation-status-and-fallback-policy.md) own validation selection and truthful validation status.
- [`docs/reference/pr-evidence-requirements.md`](docs/reference/pr-evidence-requirements.md) owns pull-request evidence requirements.
- [`docs/reference/review-decisions-and-merge-blockers.md`](docs/reference/review-decisions-and-merge-blockers.md) owns review recommendations, blockers and merge-authority provenance.

If this file and a focused canonical owner appear inconsistent, stop and reconcile the current repository guidance before acting.

## Core rule

Work from the issue contract.

Before planning implementation or changing repository state, fetch the current `AGENTS.md`, the governing record and the action-relevant repository state. Do not rely on a stale conversation summary or handover as proof of current state.

Before changing files, the agent should know:

- which issue is being implemented;
- whether readiness and dependencies have been recorded;
- which detailed implementation plan was posted;
- whether required durable human approval of that plan predates implementation;
- what is in scope and out of scope;
- how success will be assessed;
- what validation evidence is expected; and
- which refreshed safe base and issue-scoped branch contain the work.

If intent, authority or current state is unclear, surface the ambiguity and stop rather than inventing missing intent or authority.

## Safe repository operations

Before any mutating repository operation, perform the safe tool-operation check in [`docs/tool-operations.md`](docs/tool-operations.md).

The agent should identify:

- the current workflow phase;
- the intended operation;
- the exact selected tool;
- the target repository object;
- the expected side effect; and
- the side effects that are forbidden in that phase.

If the selected tool does not match the intended operation, stop before making the call.

If an unintended repository mutation occurs:

- stop normal writes;
- continue only read-only investigation and minimum authorised remediation;
- verify the resulting repository state;
- record and classify the event when required by the canonical [execution-deviation policy](docs/reference/execution-deviation-policy.md); and
- follow [Handle an execution deviation](docs/how-to/handle-execution-deviation.md) before resuming.

A minor deviation may resume only when restoration is verified, authority and scope remain valid, affected evidence is current or rerun, a practical corrective control is in place and the resumption decision is recorded. Material, critical or uncertain deviations require explicit repository-owner direction before normal mutation resumes.

## Scope control

Do:

- make the smallest change that satisfies the acceptance criteria;
- preserve existing repository conventions;
- keep documentation and templates consistent with the issue;
- record assumptions in the pull request; and
- state any validation that could not be completed.

Do not:

- refactor unrelated files;
- tidy or optimise outside the issue scope;
- introduce unrelated tooling;
- add future-stage automation unless the issue asks for it;
- mark validation complete unless it was actually completed; or
- merge changes without separate later human authority.

## Branching

After readiness, the detailed implementation plan and its required durable human approval are recorded, refresh the safe starting point and use one branch per issue from that approved base.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

If a tool cannot create the preferred branch name, use the closest safe fallback and record the caveat in the pull request.

## Validation

Select validation from the canonical [validation-by-change-type](docs/reference/validation-by-change-type.md) guidance and classify unavailable or pending evidence using the [validation status and fallback policy](docs/reference/validation-status-and-fallback-policy.md).

Do not mark a check complete unless it actually ran against an appropriate state. Tie decision-relevant validation to the exact candidate head when later changes could make it stale.

## Pull requests

The pull request is the evidence pack.

It should explain:

- which issue contract it implements;
- the durable readiness, implementation-plan and human plan-approval records;
- what changed;
- what was deliberately excluded;
- how the acceptance criteria were satisfied;
- what validation evidence supports the change;
- what remains unchecked; and
- what assumptions or caveats remain.

Open the pull request as a draft while implementation, validation or evidence remains incomplete. Follow the canonical [pull-request evidence requirements](docs/reference/pr-evidence-requirements.md).

## Contract verification

Before approval, verify the pull request against the issue contract and current lifecycle authority.

Answer:

1. Did the pull request fulfil the contract?
2. Did the pull request stay inside the contract boundaries?

Check issue alignment, scope control, required lifecycle authority, validation evidence, risks and caveats. Use one final recommendation:

- Approve
- Approve after minor fixes
- Do not approve yet

A recommendation is not merge authority. Merge remains a separate later human decision governed by the current repository review and merge rules.

## Minimal external-session bootstrap

An external agent or project configuration should bootstrap into the repository-owned contract instead of copying it. A minimal vendor-neutral form is:

```text
Repository: 8ft0-ai/IssueOps.
Before planning or mutation, use authenticated repository-native GitHub access to fetch the current AGENTS.md, governing record and action-relevant repository state. Follow AGENTS.md and its linked canonical IssueOps guidance. Treat chat history, grants and handovers as claims that require reconciliation; current GitHub/repository records take precedence. Do not mutate without authority from the governing record.
```

A product-specific outer configuration may identify the authenticated GitHub tool to use, but it should not duplicate the IssueOps lifecycle or repository-state rules that are owned here.