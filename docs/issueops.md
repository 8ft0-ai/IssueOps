# Manual IssueOps workflow

Stage 1 defines the manual IssueOps flow for this repository. The purpose is to make agentic coding work visible, reviewable and bounded before introducing automation.

The operating principle is simple: the issue is the execution contract. The agent does not work from an informal prompt or a vague ticket. It works from an issue that describes the problem, scope, non-goals, acceptance criteria and validation expectations.

Codex is the preferred agentic coding tool for implementation, but the workflow is deliberately tool-agnostic. The repository should remain understandable to humans and portable to other agents if needed.

## Stage 1 scope

Stage 1 includes the manual process and repository artefacts needed to support issue-driven work.

It includes:

- structured implementation issues;
- readiness review before implementation;
- an implementation plan before branch creation;
- one feature branch per issue;
- Codex-assisted implementation within issue scope;
- draft pull requests while work is in progress;
- validation evidence in the pull request;
- pre-approval groundedness review; and
- explicit human approval before merge.

It does not include:

- automatic Codex execution;
- auto-merge;
- branch protection changes;
- required status checks;
- complex GitHub Actions orchestration; or
- application code.

## Flow

### 1. Create the issue

Every change starts with a GitHub issue. The issue should describe the work clearly enough that a human reviewer and a coding agent can understand the intended outcome without relying on private context.

A good issue includes:

- problem statement;
- scope;
- non-goals;
- acceptance criteria;
- validation expectations;
- assumptions or constraints; and
- notes for the agent where useful.

If the issue is unclear, implementation should not start. Ask for clarification in the issue instead.

### 2. Review readiness

Before implementation starts, add an issue comment stating whether the issue is ready.

A ready issue should have:

- clear intent;
- bounded scope;
- explicit non-goals or exclusions;
- reviewable acceptance criteria;
- validation expectations; and
- no unresolved decision that would materially change the implementation.

If the issue is not ready, add a clarification comment and leave the issue unimplemented.

### 3. Post the implementation plan

When the issue is ready, post a detailed implementation plan as an issue comment before creating the branch.

The plan should include:

- proposed branch name;
- files expected to change;
- implementation steps;
- validation to run;
- scope controls; and
- known risks or caveats.

This makes the planned work visible before the agent changes the repository.

### 4. Create the feature branch

Create one branch per issue from `main`.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

Example:

```text
feature/1-manual-issueops-foundation
```

Do not commit directly to `main` unless the repository owner explicitly requests a hotfix or bootstrap exception.

### 5. Implement within issue scope

Use Codex as the preferred implementation agent. Keep the work bounded by the issue and the implementation plan.

The agent should:

- follow existing repository conventions;
- avoid unrelated refactoring;
- avoid speculative future-stage work;
- preserve compatibility unless the issue requires otherwise;
- update documentation where needed; and
- record any assumptions that affected the implementation.

### 6. Open a draft pull request

Open a draft pull request while work is still being reviewed or validation is incomplete.

The pull request should link the issue and explain:

- what changed;
- what was intentionally not changed;
- what validation was performed;
- what validation remains pending;
- assumptions and caveats; and
- whether the change is ready for review.

### 7. Validate the change

Run the validation that is relevant to the change. For documentation-only changes, validation may be a manual Markdown and scope review. For code changes in later stages, validation should include the relevant tests and checks.

Do not mark validation complete unless it was actually completed. If validation is unavailable in the current environment, mark it as pending and explain exactly what remains to be done.

### 8. Perform the pre-approval groundedness review

Before approval, review the pull request against the issue contract.

The review must answer:

1. Did we do what was needed?
2. Did we only do what was asked?

It should check:

- issue alignment;
- scope control;
- validation evidence;
- risks and caveats; and
- final recommendation.

Use one of these final recommendations:

- Approve
- Approve after minor fixes
- Do not approve yet

Do not recommend approval if validation is incomplete, scope has drifted, or the implementation does not satisfy the issue.

### 9. Human approval and merge

A human reviewer approves the pull request and merges it when satisfied.

The merge decision should be based on the issue contract, validation evidence and groundedness review, not on whether the agent produced a plausible-looking change.

## Stage 1 success criteria

Stage 1 is successful when a contributor can:

- create a structured issue;
- determine whether it is ready for agent implementation;
- see the implementation plan before repository changes begin;
- review a small pull request linked to the issue;
- understand what validation was performed; and
- make an explicit approve-or-reject decision before merge.
