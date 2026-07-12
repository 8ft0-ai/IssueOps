# Publishing the documentation site

The current maintainer procedure is [Publish and verify the documentation site](how-to/publish-and-verify-documentation-site.md).

## Current path

IssueOps publishes MkDocs through `.github/workflows/pages.yml`:

1. build the site with committed dependencies and `mkdocs build --strict`;
2. upload the generated Pages artefact;
3. deploy from `main` through GitHub Pages; and
4. verify the merged workflow and public site.

The pull-request workflow validates the artefact but skips production deployment. A passing PR build is not production Pages proof.

## Permissions and settings

Workflow permissions and Pages source configuration must match the repository’s current publishing design. The repository-level Pages source setting is not changed by the workflow file itself.

Any workflow, permission, environment or repository-setting change requires an explicit execution contract and relevant validation.

## Historical evidence

Historical production run IDs, deployed commits and original delivery observations belong in the repository’s planning and delivery records rather than this current procedure. They remain accessible through the [planning control surface](https://github.com/8ft0-ai/IssueOps/tree/main/planning) and GitHub Actions history.

## Related guidance

- [Validate a documentation change](how-to/validate-documentation-change.md)
- [Validate a workflow change](how-to/validate-workflow-change.md)
- [Validation status and fallback policy](reference/validation-status-and-fallback-policy.md)

## Compatibility note

This URL is retained for existing publishing links. Current procedure and historical evidence are now deliberately separated.
