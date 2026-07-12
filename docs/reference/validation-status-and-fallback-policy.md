# Validation status and fallback policy

Validation evidence must identify what ran against which state, what could not run and what remains after merge.

This page is the canonical reference for repository-native validation, representative fallback, pending validation and post-merge verification.

## Evidence priority

Use the strongest available evidence in this order:

1. repository-native validation against the actual final branch or PR head;
2. repository-native validation against an equivalent controlled repository state;
3. representative fallback for a low-risk change when direct repository execution is unavailable; and
4. explicit pending or not-performed evidence when no safe substitute exists.

Do not describe a weaker form as equivalent to a stronger one.

## Repository-native validation

Repository-native evidence comes from the actual repository or its configured environment, including:

- a fresh checkout of the target branch;
- dependency installation from committed files;
- repository test and build commands;
- GitHub Actions results for the branch or pull request;
- generated artefacts from that run;
- deployment or Pages verification; and
- repository settings observed directly.

Tie the result to the relevant commit or head SHA when later changes could make the evidence stale.

## Representative fallback

Representative fallback is acceptable only when:

- repository-native execution is unavailable;
- the change is low risk;
- the fallback exercises enough of the changed behaviour to support review;
- no available validation is failing; and
- the PR states the limitation and any remaining check.

Record:

- why direct validation was unavailable;
- which representative files, data or environment were used;
- the exact command that ran;
- why it is sufficient for this change; and
- which repository-native check remains pending, if any.

Representative validation should block merge when the change affects workflow behaviour, permissions, deployment, branch protection, repository settings, application code or any behaviour the fallback does not exercise.

## Pending validation

Use pending validation when a named check has not completed or cannot run in the current environment.

Pending validation blocks approval when:

- it is required to decide correctness or contract satisfaction;
- available validation is failing;
- implementation is incomplete;
- the final head has not been validated; or
- the PR would be misleading without the result.

A draft PR may remain open with pending local or environment-specific validation when implementation is complete, available checks are not failing, the diff is small and reviewable, and correctness does not depend on pretending that validation exists.

## Post-merge verification

Post-merge verification is reserved for evidence that genuinely cannot exist before merge, such as:

- production-only Pages deployment;
- a repository setting that becomes observable after the merged workflow runs;
- a release or environment-specific state created by merge; or
- a live integration check unavailable to the feature branch.

Record the exact check, why it cannot run earlier, who will capture it and how failure will be handled.

Do not move an available strict build, test, final-diff review or required workflow check into post-merge verification.

## Standard wording

```md
## Validation status

Exact final head:

- `<commit SHA>`

Repository-native validation completed:

- ...

Representative fallback validation:

- None / exact fallback and limitation.

Validation not performed or pending:

- None / exact check and reason.

Post-merge verification required:

- None / exact follow-up.
```

## Failed validation

When required validation fails:

- do not mark the PR ready;
- diagnose and remediate inside the issue contract;
- rerun affected checks against the new head;
- update the evidence pack; and
- retain `Do not approve yet` until the failure is resolved.

Do not hide a failing run behind a later unrelated success or omit it when it materially explains remediation.

## Related guidance

- [Why repository-native validation is preferred](../explanation/repository-native-validation-model.md)
- [Validation by change type](validation-by-change-type.md)
- [Pull-request evidence requirements](pr-evidence-requirements.md)
