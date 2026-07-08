# Safe tool-operation protocol

Agentic repository work has two parts: deciding what should change and safely carrying out the repository operation.

The issue contract controls intent. The implementation plan controls approach. The tool-operation check controls actuation.

This protocol is manual in Stage 1.3. It does not add automation, policy tooling or a gateway. It gives agents and reviewers a simple way to avoid accidental repository mutations.

## Core rule

Before any mutating repository operation, verify that the selected tool matches the intended operation.

Do not rely on the surrounding conversation, recent tool history or a plausible tool name. Check the operation directly before executing it.

## Pre-mutation check

Before a write operation, identify:

- Phase: the current workflow phase.
- Intended operation: what should happen next.
- Selected tool: the exact repository tool about to be invoked.
- Target: the repository object being changed.
- Expected side effect: the one change that should occur.
- Forbidden side effects: changes that must not occur in this phase.

Example:

```text
Phase: Branch setup
Intended operation: Create a feature branch for issue #14
Selected tool: create_branch
Target: 8ft0-ai/IssueOps
Expected side effect: one new branch
Forbidden side effects: no issues, no files, no pull requests
```

If the selected tool does not match the intended operation, stop before making the call.

## Compact evidence format

For routine low-risk operations, use this compact format:

```text
Safe operation: <intended operation>; no <forbidden side effects>.
```

Examples:

```text
Safe operation: readiness comment only; no branch/file/label/merge mutation.
```

```text
Safe operation: update docs file on feature branch; no issue/label/merge mutation.
```

The compact format is acceptable when:

- the operation is routine and low risk;
- the target is unambiguous;
- the issue contract and implementation plan are already recorded; and
- the forbidden side effects are obvious and named.

Use the full format when:

- the operation changes workflow files, labels, repository settings or permissions;
- the operation creates or merges a PR;
- the target is ambiguous;
- a previous operation failed or behaved unexpectedly; or
- the change is high risk enough that a reviewer needs the full actuation record.

The compact format shortens evidence. It does not remove the requirement to check the selected tool before mutation.

## Dependency state before branch setup

Before entering branch setup, the readiness comment should record dependency state and the safe starting point for the branch.

If a blocking dependency is not satisfied, do not create the branch. Post the dependency state on the issue instead and wait until the required prior work, release, repository setting or environment state is available.

This is a manual readiness control. It does not add automated dependency detection or branch enforcement.

## Workflow file changes

Workflow files are high-leverage repository mutations.

Before changing `.github/workflows/*`, confirm that the issue explicitly allows workflow changes and that the implementation plan names the workflow files or workflow behaviour expected to change.

Apply the [workflow-change review checklist](workflow-changes.md) before opening a PR that adds or changes workflow files. If the issue does not authorise workflow changes, do not modify workflow files as an incidental fix.

## Phase boundaries

### Issue setup

Allowed operations:

- fetch the issue;
- fetch related issues, pull requests, branches or files needed to confirm dependency state;
- add readiness or implementation-plan comments.

Not allowed in this phase:

- create new issues;
- create branches;
- change files;
- open pull requests.

### Branch setup

Allowed operations:

- create the feature branch after readiness and dependency state are recorded;
- search or fetch branches if needed;
- fetch files for context.

Not allowed in this phase:

- create issues;
- change issue bodies;
- change files;
- open pull requests.

### Implementation

Allowed operations:

- fetch files;
- create files;
- update files.

Not allowed in this phase:

- create issues;
- close issues;
- open pull requests before validation read-back;
- merge pull requests.

### Pull request creation

Allowed operations:

- create the pull request;
- fetch the pull request for verification.

Not allowed in this phase:

- create issues;
- change unrelated issues;
- merge the pull request.

## Circuit breaker

If an unintended repository mutation occurs, stop further write operations.

The agent may perform only the minimum remediation needed to make the accidental mutation safe, such as closing an accidental issue or reverting an accidental file change. After remediation, the agent must report what happened and wait for explicit instruction before continuing.

Do not resume normal implementation in the same flow after an unintended mutation unless the repository owner explicitly asks you to proceed.

## PR evidence

If the safe tool-operation protocol affected the work, record it in the pull request. Include any fallback branch names, blocked operations or recovery steps as caveats.
