# Why repository-native validation is preferred

Validation is strongest when it exercises the actual repository state that will be reviewed and merged.

IssueOps therefore prefers repository-native evidence: committed dependencies, real branch content, configured workflows, generated artefacts and observable repository or deployment state.

## What repository-native evidence proves

A strict build on the actual PR head can show that the current files and configuration work together. A GitHub Actions result can show how the repository’s configured environment handled that head. A production Pages check can show that the merged workflow and repository setting produced a public site.

The evidence is close to the behaviour under review, which reduces assumptions about missing files, dependencies, settings and integration.

It still does not prove the whole issue automatically. A passing build may coexist with scope drift, incorrect content or an unsatisfied acceptance criterion. Contract verification remains a human judgement.

## Why representative validation exists

An agent environment may be unable to clone the repository, install a dependency, access a setting or run a protected integration. A low-risk documentation or deterministic transformation may still be partially testable using branch content read through the repository interface and a representative local environment.

Representative validation can reduce uncertainty. It cannot erase the difference between the representative environment and the repository.

The PR should state the difference so the reviewer can decide whether the fallback is sufficient.

## When fallback is unsafe

Representative evidence is weak when correctness depends on:

- workflow triggers and permissions;
- repository settings;
- deployment environments;
- secrets or identity;
- branch protection;
- application integration; or
- any changed behaviour the fallback does not exercise.

In those cases, the missing repository-native check remains pending or blocks merge.

## Pending validation is honest evidence

Recording that a check did not run is better than presenting a plausible substitute as complete.

A draft PR can carry pending environment-specific validation while implementation is reviewed, but the recommendation stays `Do not approve yet` when that check is needed to establish correctness.

## Post-merge verification has a narrow role

Some evidence only exists after merge, such as a production-only deployment. Separating it from pre-merge validation makes the residual risk visible and prevents a feature-branch limitation from being mistaken for a completed check.

The distinction should not be used to postpone a test that could run before merge.

## Delegated delivery does not weaken evidence

Repository-owner delegation can authorise routine mechanics after every gate passes. It cannot make representative evidence equivalent to repository-native validation or permit a required check to be skipped.

The agent must stop when correctness depends on unavailable evidence.

## Canonical rules

This explanation introduces no hidden fallback or merge rule.

Use:

- [Validation status and fallback policy](../reference/validation-status-and-fallback-policy.md) for exact decisions;
- [Validation by change type](../reference/validation-by-change-type.md) for required evidence; and
- [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md) for approval consequences.
