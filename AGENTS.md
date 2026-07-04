# Agent operating rules

These rules apply to Codex and any other agentic coding tool used in this repository.

Codex is the preferred implementation agent, but the repository process is intentionally tool-agnostic. The issue, branch, pull request and validation evidence are the durable record of work.

## Core rule

Work from the issue contract, not from private assumptions.

Before changing files, the agent should be able to point to:

- the GitHub issue being implemented;
- the readiness review comment;
- the implementation plan comment;
- the intended feature branch; and
- the validation expectations.

## Scope control

The agent must stay within the issue scope.

Do:

- implement the smallest change that satisfies the acceptance criteria;
- preserve existing repository conventions;
- update documentation when required by the issue;
- record assumptions in the pull request; and
- call out validation that could not be performed.

Do not:

- refactor unrelated files;
- introduce unrelated tooling;
- change repository policy outside the issue scope;
- mark validation complete unless it was actually completed; or
- merge changes without human approval.

## Branching

Use one branch per issue from `main`.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

If a tool cannot create the preferred branch name, use the closest safe fallback and record the caveat in the issue or pull request.

## Pull requests

Open pull requests as drafts when work is still in progress or validation is incomplete.

The pull request should include:

- linked issue;
- summary of changes;
- non-goals and excluded work;
- validation performed;
- pending validation, if any;
- assumptions and caveats; and
- pre-approval groundedness review.

## Pre-approval groundedness review

Before approval, answer:

1. Did we do what was needed?
2. Did we only do what was asked?

The final recommendation must be one of:

- Approve
- Approve after minor fixes
- Do not approve yet

Do not recommend approval if the implementation is incomplete, validation is misleading, or scope has drifted.
