# Write an executable issue contract

Use this guide to turn an approved, bounded change into a GitHub issue that an agent or contributor can implement without inventing material intent.

For exact fields and their meaning, use [Execution-contract fields](../reference/execution-contract-fields.md).

## 1. State the current problem

Describe the unsatisfactory repository condition before proposing the implementation.

A useful problem statement identifies:

- who or what is affected;
- what is missing, incorrect or unsafe; and
- why the issue is worth changing now.

Avoid writing only a solution such as “add a new page”. Explain the reader or system problem that page must solve.

## 2. Define the observable outcome

Describe what should be true after the issue is complete.

Prefer an outcome a reviewer can inspect, such as:

- a reader can find a task from the documentation home;
- a command rejects an invalid input safely; or
- a workflow emits the required evidence without mutating repository state.

Do not hide acceptance rules inside a broad aspiration.

## 3. Bound the permitted change

List the files, behaviours or areas the contributor may change. Then list explicit non-goals for adjacent work that might otherwise appear reasonable.

Use non-goals to exclude matters such as:

- unrelated refactoring;
- future automation;
- repository-setting changes;
- authority changes;
- broad wording cleanup; or
- application code outside a documentation issue.

The scope must be large enough for one coherent result and small enough for one reviewable pull request.

## 4. Make success reviewable

Write acceptance criteria as observable conditions. A criterion should let a reviewer answer yes or no from the repository, pull request and validation evidence.

Good criteria describe behaviour or state. Avoid criteria such as “looks good”, “improve quality” or “follow best practice” without a concrete test.

## 5. Match validation to the change

Name the evidence the pull request should provide. Include repository-native commands and relevant manual observations.

For a documentation change, this commonly includes:

- changed files read back;
- navigation and internal links reviewed;
- `mkdocs build --strict`;
- documentation currency checked; and
- confirmation that unrelated code or automation was not introduced.

Do not require evidence that cannot prove the acceptance criteria, and do not omit a check because it is inconvenient in the current environment.

## 6. State risk and implementation constraints

Describe the consequence of error and any repository-specific instructions. Higher-risk changes need narrower boundaries, stronger validation and more deliberate review.

Agent instructions may identify conventions, safety constraints or a required source of truth. They must not delegate approval or merge authority implicitly.

## 7. Record dependencies and stage relationship

When ordering matters, name the required issue, pull request, release, setting or environment state.

When the issue is part of an approved roadmap, link the parent and explain how this slice contributes. A roadmap relationship does not expand the issue scope.

## 8. Review the contract before implementation

Before treating the issue as ready, ask:

- Could a contributor recognise the intended outcome without private context?
- Are allowed and forbidden changes explicit?
- Can every acceptance criterion be verified?
- Does expected validation match the changed behaviour?
- Are dependencies and authority boundaries visible?
- Is the work small enough for one branch and one pull request?

If any answer is no, revise the issue before posting readiness evidence.

## 9. Create the issue and preserve its intent

Create the GitHub issue with the complete contract. Later clarification should be recorded visibly in the issue discussion rather than silently relying on chat history.

Do not create a branch yet. Continue with [Check readiness and dependencies](check-readiness-and-dependencies.md), then [Prepare an implementation plan](prepare-implementation-plan.md).

## Common failure modes

- **Solution without problem:** the issue prescribes a file but does not explain the user or system outcome.
- **Scope without non-goals:** adjacent work can enter the branch unnoticed.
- **Unreviewable criteria:** completion depends on opinion or hidden context.
- **Generic validation:** “tests pass” does not identify which checks matter.
- **Unrecorded dependency:** the branch starts before required work is merged.
- **Implicit authority:** delivery delegation is mistaken for approval or merge permission.
