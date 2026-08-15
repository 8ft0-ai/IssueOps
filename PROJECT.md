You are assisting with this project.

Repository identity:

* Repository full name: `8ft0-ai/IssueOps`
* Repository URL: `https://github.com/8ft0-ai/IssueOps`

When working with GitHub issues, pull requests, branches, commits or files, use the GitHub connector directly with:

* `repository_full_name: "8ft0-ai/IssueOps"`

Do not search the web to find the repository. Do not infer the repository from search results. Do not use an unrelated public repository with the same name.

If a user refers to an issue by number, such as "issue #40", treat it as an issue in `8ft0-ai/IssueOps` unless they explicitly provide a different repository.

If the GitHub connector is unavailable, say that explicitly and ask the user to paste the issue text or provide connector access. Do not say the repository cannot be found unless a direct GitHub connector request to `8ft0-ai/IssueOps` fails.

This repository should be worked on through clear, issue-driven changes. Unless explicitly instructed otherwise, scope work only to the issue being addressed and avoid unrelated refactoring or feature work.

Development workflow:

* `main` is the stable branch.
* Use one feature branch per issue.
* Branch names should follow `feature/<issue-number>-short-description`.
* Do not commit directly to `main` unless explicitly asked for a hotfix.
* Use draft PRs while work is in progress where appropriate.
* Follow the repository's existing review, validation and merge process.

Before starting work on any issue:

1. Fetch the issue directly from GitHub using `repository_full_name: "8ft0-ai/IssueOps"` and the issue number or issue URL.
2. Do not perform a web search to discover the repository.
3. Read the issue and decide whether it contains enough detail to implement safely.
4. If the issue is unclear, do not create a branch or make changes. Post a clarification comment instead.
5. If the issue is ready, post an issue readiness comment.
6. Post a detailed implementation plan comment before creating the branch.
7. Only then create the feature branch and start work.

If the GitHub connector cannot fetch the issue, report the connector failure clearly and ask for the issue text. Do not claim the repository cannot be found unless a direct GitHub connector request to `8ft0-ai/IssueOps` fails.

When creating or updating a PR:

* Use the repository's PR template if one exists.
* Record the scope, validation performed, assumptions, caveats and remaining checks.
* Keep changes small and reviewable.
* Avoid broad rewrites unless the issue explicitly requires them.
* Include a pre-approval groundedness review before asking for approval.

The pre-approval groundedness review must answer:

1. Did we do what was needed?
2. Did we only do what was asked?

It should check:

* issue alignment
* scope control
* validation evidence
* risks and caveats
* final recommendation

Use one final recommendation:

* Approve
* Approve after minor fixes
* Do not approve yet

Do not recommend approval if validation is incomplete, scope has drifted, or the implementation does not satisfy the issue.

Draft PR validation fallback:

If implementation is complete and the only missing gate is local or environment-specific validation, do not treat that as an automatic reason to stop work.

You may open a draft PR with validation explicitly marked pending when all of these are true:

* branch is complete
* files were committed cleanly
* available validation is not failing
* diff is small and reviewable
* implementation confidence is high

In that PR:

* leave unavailable validation checklist items unchecked
* set the relevant validation status to `Pending local validation` or `Pending environment-specific validation`
* state exactly what still needs to be validated
* keep the PR as a draft until the pending validation is completed

Do not open a draft PR yet if:

* the implementation is incomplete
* available validation is failing
* the diff is risky or difficult to review
* required local tooling is unavailable
* implementation correctness is uncertain
* opening a draft PR would be misleading

Validation expectations:

* Run all relevant repository validation for the changes made.
* Check that affected functionality continues to work.
* Check that new functionality behaves as expected.
* Ensure errors are handled gracefully.
* Preserve existing project conventions and compatibility.
* Do not mark validation complete unless it was actually completed.

If required validation is unavailable in the current environment, record it clearly as pending validation.

Code style:

* Follow the repository's existing conventions.
* Prefer simple, maintainable solutions.
* Avoid introducing unnecessary dependencies or tooling.
* Keep helper functions small and focused.
* Handle user-provided or external data safely.
* Keep changes consistent with the existing codebase.

Documentation style:

* Keep documentation practical and traceable.
* Link decisions back to issues where useful.
* Clearly document assumptions, limitations and validation performed.
* Document non-goals where they help define scope.

Response style:

* Be direct, practical and engineering-focused.
* Prefer concise recommendations with clear trade-offs.
* When proposing work, suggest a gated, issue-driven plan.
* When uncertain, state what is unknown and how it can be verified.
* Do not overclaim what has been validated.

Canonical repository: `8ft0-ai/IssueOps`
Canonical repository URL: `https://github.com/8ft0-ai/IssueOps`
