# Operation permissions and evidence

The execution contract controls intent, the implementation plan controls approach, and the operation check controls the repository mutation about to occur.

This page is the canonical reference for operation phases, forbidden side effects, operation evidence formats and the circuit-breaker trigger. The [Execution-deviation policy](execution-deviation-policy.md) owns classification, stale-evidence, resumption and escalation rules after the circuit breaker is triggered.

## Core rule

Before any mutating repository operation, verify:

- the current workflow phase;
- the intended operation;
- the exact selected tool or command;
- the target repository object;
- the one expected side effect; and
- forbidden side effects for that phase.

If the selected operation does not match the intended side effect, stop before mutation.

## Full operation evidence

```text
Phase: <workflow phase>
Intended operation: <what should happen next>
Selected tool: <exact tool or command>
Target: <repository object>
Expected side effect: <one intended mutation>
Forbidden side effects: <changes that must not occur>
```

Use the full format when:

- creating or merging a pull request;
- changing workflow files, labels, settings or permissions;
- the target is ambiguous;
- a previous operation failed or behaved unexpectedly; or
- the change is high risk enough to require a complete actuation record.

## Compact evidence

```text
Safe operation: <intended operation>; no <forbidden side effects>.
```

The compact format is acceptable only when the operation is routine and low risk, the target is unambiguous, the issue and plan already exist, and forbidden side effects are named.

Compact evidence shortens the record. It does not remove the pre-mutation check.

## Phase permissions

### Issue setup

Allowed:

- fetch the issue and related repository state;
- inspect dependencies, branches, pull requests and files;
- add readiness, dependency and implementation-plan comments.

Forbidden:

- create a branch before readiness and planning are complete;
- change files;
- open or merge a pull request; or
- create unrelated issues.

### Branch setup

Allowed:

- refresh dependency state and the safe starting commit;
- create the planned feature branch;
- fetch files and branches for context.

Forbidden:

- change files before the branch exists;
- open or merge a pull request; or
- modify unrelated issues.

### Implementation

Allowed:

- fetch, create and update files on the issue branch;
- inspect the branch and diff;
- run validation.

Forbidden:

- commit directly to `main` unless a separately authorised hotfix requires it;
- mix another issue into the branch;
- open the PR before changed-file read-back and an honest validation status exist; or
- merge the PR.

### Pull-request creation and remediation

Allowed:

- open a draft PR;
- inspect checks, comments, reviews and threads;
- apply scoped remediation on the same branch;
- refresh evidence.

Forbidden:

- mark incomplete validation as passed;
- resolve required threads before fixes exist;
- merge while a blocker remains; or
- use review feedback to introduce unapproved scope.

### Merge and post-merge verification

Allowed only when the PR satisfies the canonical [review decisions and merge blockers](review-decisions-and-merge-blockers.md), repository policy and human authority.

After merge, observe the merged repository, workflow, deployment or setting required by the PR evidence. Do not treat merge success as proof that all post-merge behaviour worked.

## High-leverage operations

Workflow, permission, setting, production, release and merge operations require explicit issue scope and a full operation check. Do not perform one as an incidental fix for a documentation or code issue.

Apply the [workflow-change review checklist](../workflow-changes.md) before a PR changes `.github/workflows/*`.

## Dependency boundary

Do not create a branch while a blocking dependency is unresolved. Record the dependency on the issue and refresh the safe starting state after it is satisfied.

## Circuit breaker

If an unintended repository mutation occurs:

1. stop normal write operations;
2. continue only the read-only investigation and minimum authorised remediation needed to make the situation safe;
3. fetch and verify the resulting repository state; and
4. use the [Execution-deviation policy](execution-deviation-policy.md) to determine recording, severity, stale evidence, resumption and escalation.

Do not conceal the accidental mutation or continue as though it were part of the plan. A successful remediation response is not proof that repository state or evidence is restored.

Use [Handle an execution deviation](../how-to/handle-execution-deviation.md) for the recovery procedure.

## Related guidance

- [Perform a safe repository mutation](../how-to/perform-safe-repository-mutation.md)
- [Handle an execution deviation](../how-to/handle-execution-deviation.md)
- [Execution-deviation policy](execution-deviation-policy.md)
- [Review decisions and merge blockers](review-decisions-and-merge-blockers.md)
- [IssueOps operating protocol](../issueops-protocol.md)
