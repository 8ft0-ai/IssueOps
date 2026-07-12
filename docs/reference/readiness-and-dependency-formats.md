# Readiness and dependency formats

Readiness is recorded on the execution-contract issue before branch creation. It confirms that the issue can be implemented without inventing missing intent and that the proposed starting point is safe.

This page is the canonical reference for readiness decisions and dependency evidence formats.

## Planning-readiness format

```md
## Planning readiness

- Expected outcome:
- Scope boundaries:
- Acceptance criteria:
- Validation expectations:
- Change risk:
- Decision: Ready to implement / clarification required.
```

The decision is `Ready to implement` only when the outcome, boundaries, review criteria, validation and risk are explicit enough for safe implementation.

Use `clarification required` when material intent is missing, contradictory or would have to be invented. Do not create a branch while clarification is required.

## Dependency-check format

```md
## Dependency check

Required prior work:

- Issue/PR/release:
- Required state:
- Current state:

Safe starting point:

- Base branch or commit:
- Reason this is safe:

Decision:

- Ready to implement / blocked pending dependency / clarification required.
```

Record every material prerequisite, including repository settings or environment state that cannot be inferred from code.

## Decision vocabulary

| Decision | Meaning | Branch creation |
| --- | --- | --- |
| **Ready to implement** | The contract is executable, required dependencies are satisfied and a safe starting point is known. | Permitted after the implementation plan is posted. |
| **Ready to implement with explicit pending environment validation** | Code work can start, but a named repository setting or environment fact must remain pending in PR evidence. | Permitted only when the unresolved fact does not make implementation correctness uncertain before merge. |
| **Blocked pending dependency** | A required issue, PR, release, setting or environment state is not yet satisfied. | Not permitted. |
| **Clarification required** | Material intent, scope, acceptance or validation expectations are incomplete or contradictory. | Not permitted. |

Pending evidence must not be used to disguise uncertainty. If the unresolved state determines whether the proposed implementation is correct or safe, the issue remains blocked.

## No dependency example

```md
## Dependency check

Required prior work:

- Issue/PR/release: None identified.
- Required state: Not applicable.
- Current state: Not applicable.

Safe starting point:

- Base branch or commit: latest `main`.
- Reason this is safe: the bounded documentation change does not depend on pending work.

Decision:

- Ready to implement.
```

## Satisfied dependency example

```md
## Dependency check

Required prior work:

- Issue/PR/release: PR #32.
- Required state: merged to `main`.
- Current state: closed and merged.

Safe starting point:

- Base branch or commit: `main` after the PR #32 merge commit.
- Reason this is safe: the required page now exists in the base branch.

Decision:

- Ready to implement.
```

## Unsatisfied dependency example

```md
## Dependency check

Required prior work:

- Issue/PR/release: PR #32.
- Required state: merged to `main`.
- Current state: open and under review.

Safe starting point:

- Base branch or commit: None yet.
- Reason this is safe: not applicable until PR #32 merges.

Decision:

- Blocked pending dependency. Do not create a feature branch yet.
```

## Environment dependency example

```md
## Dependency check

Required prior work:

- Issue/PR/release: repository Pages source setting.
- Required state: Pages source configured for GitHub Actions.
- Current state: manual repository setting not confirmed in code.

Safe starting point:

- Base branch or commit: latest `main`.
- Reason this is safe: the documentation change can proceed, but PR evidence must retain the setting as pending verification.

Decision:

- Ready to implement with explicit pending repository-setting validation.
```

## Evidence quality

A useful readiness record names the actual issue, PR, release, setting, commit or branch state that was checked. Avoid unsupported statements such as “dependencies look fine”.

When repository state changes before implementation begins, refresh the check. Readiness is evidence about a specific starting point, not permanent approval for a stale branch.

## Related guidance

- [Check readiness and dependencies](../how-to/check-readiness-and-dependencies.md)
- [Execution-contract fields](execution-contract-fields.md)
- [Prepare an implementation plan](../how-to/prepare-implementation-plan.md)
- [IssueOps operating protocol](../issueops-protocol.md)
