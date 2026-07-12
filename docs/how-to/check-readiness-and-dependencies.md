# Check readiness and dependencies

Use this guide before implementation to decide whether an execution-contract issue is safe to start.

For the exact comment formats and decision vocabulary, use [Readiness and dependency formats](../reference/readiness-and-dependency-formats.md).

## 1. Refresh the repository state

Read the issue and all later comments. Then inspect:

- the parent roadmap or initiative when one governs the issue;
- open pull requests that may conflict;
- prerequisite issues, pull requests or releases;
- the latest `main` commit;
- repository settings or environment state named by the contract; and
- the files or areas likely to change.

Do not assume a dependency remains satisfied because it was checked in an earlier session.

## 2. Test the contract for executability

Confirm that:

- the expected outcome is clear;
- scope and non-goals are explicit;
- acceptance criteria are directly reviewable;
- expected validation is specific;
- the risk is stated honestly;
- the work is small enough for one reviewable branch; and
- implementation does not require inventing product intent, architecture or policy.

When material intent is missing or contradictory, post `clarification required` and stop. Do not use the implementation plan to repair an incomplete contract silently.

## 3. Identify every material dependency

Check for:

- a prior issue or pull request that must merge first;
- a release or generated artefact the change relies on;
- a repository setting not visible in code;
- an environment or credential requirement;
- a current branch or commit that must be used as the base; and
- another active change that modifies the same canonical content.

Record the required state and the state actually observed.

## 4. Select the safe starting point

Name the exact `main` commit or other approved base state.

The safe starting point should contain every satisfied prerequisite and no known conflicting unmerged work. Dependent migrations should start from the latest `main` after the prerequisite merge rather than from stale parallel branches.

## 5. Record the readiness decision

Post the planning-readiness and dependency-check evidence on the issue.

Use:

- `Ready to implement` when the contract is executable and prerequisites are satisfied;
- `Ready to implement with explicit pending environment validation` only when implementation can proceed safely and the unresolved fact remains named in later PR evidence;
- `Blocked pending dependency` when required prior state is not satisfied; or
- `Clarification required` when material intent or review criteria are incomplete.

## 6. Stop safely when blocked

When the decision is blocked or clarification required:

- do not create a branch;
- do not change files;
- state the exact missing decision or dependency;
- resolve it from an approved roadmap or issue discussion where possible; and
- continue only when a refreshed check supports a ready decision.

A blocked issue may be skipped in a delegated batch only when it is not a prerequisite for remaining work and the skip is recorded explicitly.

## 7. Continue to implementation planning

When the decision is ready, post the implementation plan before creating the branch.

Continue with [Prepare an implementation plan](prepare-implementation-plan.md).

## Common failure modes

- checking only labels rather than the issue and repository record;
- treating an open prerequisite PR as satisfied;
- naming `main` without identifying which state of `main` was reviewed;
- proceeding because a missing environment check seems likely to pass;
- creating a branch before the plan is visible; or
- reusing a stale branch after dependent work merges.
