# Implementation-plan format

Post the implementation plan on the execution-contract issue after readiness and dependency evidence are complete and before creating the feature branch.

The plan records the proposed execution path. It is evidence of intended implementation, not permission to exceed the issue contract.

## Standard format

````md
## Implementation plan

Proposed branch:

- `feature/<issue-number>-short-description`

Safe starting commit:

- `<commit SHA>` on `main`.

Files or areas expected to change:

- ...

Intended content movement or behavioural change:

- ...

Link, compatibility or data-migration treatment:

- ... / Not applicable.

Implementation sequence:

1. ...
2. ...

Validation commands:

```text
...
```

Additional validation:

- ...

Post-merge verification:

- ... / None.

Assumptions:

- ... / None.

Caveats:

- ... / None.

Explicit exclusions:

- ...
````

Use `Not applicable` or `None` rather than omitting a heading when its absence could create ambiguity.

## Required information

| Item | Purpose |
| --- | --- |
| **Proposed branch** | Connects the issue to one planned feature branch. |
| **Safe starting commit** | Makes dependency and base-branch state reviewable. |
| **Expected files or areas** | Gives the later PR a scope prediction to compare against. |
| **Intended change** | States the proposed implementation without replacing the issue outcome. |
| **Implementation sequence** | Exposes ordering, intermediate safety and likely review boundaries. |
| **Validation** | Identifies commands and evidence before work begins. |
| **Post-merge verification** | Separates evidence that can exist only after merge. |
| **Assumptions and caveats** | Makes uncertainty visible before implementation. |
| **Explicit exclusions** | Reinforces the issue non-goals and prevents adjacent work. |

Add link, URL, migration, generated-output or compatibility treatment when the issue affects those concerns.

## Planning quality tests

The plan is specific enough when a reviewer can later answer:

- Did the branch start from the recorded safe state?
- Did the implementation touch the predicted areas for the stated reason?
- Did the work follow the intended sequence or record a justified adaptation?
- Did validation match what was planned and the behaviour changed?
- Were assumptions, caveats and exclusions preserved?

The plan is not ready when it says only “make the change and test it”, relies on unstated repository knowledge or lists broad areas that would allow unrelated work.

## Adaptation during implementation

A plan may need to adapt after repository inspection. Record a material change on the issue or pull request before expanding the implementation.

Do not edit the original plan to make later discoveries appear known in advance. Preserve the intended path and record the actual path separately in the PR evidence pack.

A change that expands product intent, authority, lifecycle semantics or issue scope requires contract clarification or a follow-up issue rather than a quiet plan update.

## Branch timing

The branch is created only after:

1. the issue is executable;
2. dependencies and safe starting state are recorded;
3. the implementation plan is posted; and
4. no blocking state remains.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

## Related guidance

- [Prepare an implementation plan](../how-to/prepare-implementation-plan.md)
- [Readiness and dependency formats](readiness-and-dependency-formats.md)
- [Execution-contract fields](execution-contract-fields.md)
- [IssueOps operating protocol](../issueops-protocol.md)
