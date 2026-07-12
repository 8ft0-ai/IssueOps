# Change-type validation

Validation should match the behaviour and risk changed by the pull request.

The canonical validation matrix now lives in [Reference — Validation by change type](reference/validation-by-change-type.md).

## Use the matrix

The matrix covers:

- documentation;
- workflows;
- publishing and deployment;
- process, labels and governance guidance;
- future application code; and
- planning and delivery records.

Apply every relevant change type when a pull request crosses boundaries. Record what ran, what did not run and what can only be verified after merge.

## Complete the task

- [Validate a documentation change](how-to/validate-documentation-change.md)
- [Validate a workflow change](how-to/validate-workflow-change.md)
- [Publish and verify the documentation site](how-to/publish-and-verify-documentation-site.md)

## Exact status and fallback rules

- [Validation status and fallback policy](reference/validation-status-and-fallback-policy.md)

## What remains true

- Required validation is never marked complete unless it ran successfully.
- A check for one change type does not prove another changed behaviour.
- Repository-native evidence is preferred.
- Representative fallback is limited to sufficiently exercised low-risk changes and is described honestly.
- Validation needed to decide correctness blocks merge when unavailable.
- Post-merge verification is only for evidence that genuinely cannot exist earlier.

## Compatibility note

This URL remains for existing links. New documentation should link directly to the canonical matrix or relevant task guide.
