# Agent operating rules

These rules apply to Codex and any other coding agent used in this repository.

Codex is the preferred implementation agent. The workflow is built around contract-bound coding: the issue defines the work, the branch contains the implementation and the pull request provides the evidence for review.

## Core rule

Work from the issue contract.

Before changing files, the agent should know:

- which issue is being implemented;
- what is in scope;
- what is out of scope;
- how success will be assessed;
- what validation evidence is expected; and
- which branch contains the work.

If the issue is unclear, the agent should surface the ambiguity rather than inventing missing intent.

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
- merge changes without human approval.

## Branching

Use one branch per issue from `main`.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

If a tool cannot create the preferred branch name, use the closest safe fallback and record the caveat in the pull request.

## Pull requests

The pull request is the evidence pack.

It should explain:

- which issue contract it implements;
- what changed;
- what was deliberately excluded;
- how the acceptance criteria were satisfied;
- what validation evidence supports the change;
- what remains unchecked; and
- what assumptions or caveats remain.

Open the pull request as a draft while the work is still being reviewed or validation is incomplete.

## Contract verification

Before approval, verify the pull request against the issue contract.

Answer:

1. Did the pull request fulfil the contract?
2. Did the pull request stay inside the contract boundaries?

Use one final recommendation:

- Approve
- Approve after minor fixes
- Do not approve yet
