# Repository-native validation

Repository-native validation is the preferred IssueOps evidence path because it runs against the actual repository, branch, workflow, deployment or setting under review.

This stable page now routes exact policy and rationale to focused guidance. The fallback and merge rules have not changed.

## Check the exact policy

- [Validation status and fallback policy](reference/validation-status-and-fallback-policy.md)
- [Validation by change type](reference/validation-by-change-type.md)

## Understand the model

- [Why repository-native validation is preferred](explanation/repository-native-validation-model.md)

## What remains true

- Use repository-native evidence whenever available.
- Tie results to the relevant final state or head SHA.
- Representative fallback is limited to sufficiently exercised low-risk changes.
- Record why direct validation was unavailable, what actually ran and what remains pending.
- Do not describe representative validation as equivalent to repository-native evidence.
- Missing validation blocks merge when correctness or contract satisfaction depends on it.
- Delegated delivery does not weaken these evidence requirements.

## Compatibility note

Earlier versions of this page combined rationale, fallback conditions and PR wording. Stage 4 separated those needs while preserving this URL as the repository-native validation entry point.
