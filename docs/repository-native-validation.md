# Repository-native validation

Repository-native validation is the preferred evidence path for IssueOps work.

It means validation ran against the actual repository state, from a real checkout, branch, pull request workflow, deployment environment or repository setting. Representative validation is a fallback when the current execution environment cannot access or run the repository directly.

## Preferred evidence

Use repository-native validation whenever available:

- fresh checkout of the target branch;
- repository dependency install from committed files;
- repository build or test commands;
- GitHub Actions workflow results for the branch or pull request;
- deployment or Pages verification after merge; and
- repository settings checked directly where relevant.

## Representative fallback

Representative fallback validation is acceptable only when repository-native validation is unavailable and the change is low risk.

A fallback must record:

- why repository-native validation was unavailable;
- what representative files or placeholders were used;
- which command actually ran;
- why the fallback is sufficient for the change type; and
- which validation, if any, remains pending.

Representative fallback should not be described as equivalent to repository-native validation.

## When fallback should block merge

Fallback validation should block merge when:

- the change affects workflow behaviour, deployment, permissions, branch protection or app code;
- the fallback does not exercise the changed behaviour;
- available validation is failing;
- correctness is uncertain; or
- the PR would be misleading without repository-native evidence.

## PR evidence wording

Use explicit wording:

```md
Repository-native validation:

- Not available: direct checkout failed in this environment.

Representative fallback validation:

- Ran `mkdocs build --strict` against a scratch MkDocs project assembled from branch read-back content and representative existing docs.

Remaining validation:

- None / post-merge verification listed below.
```

## Relationship to delegated batch mode

Delegated batch mode can use representative fallback only for low-risk changes where the fallback is sufficient and available validation is not failing.

If repository-native validation is required to judge correctness, delegated batch mode must stop for manual review.
