# Publishing the documentation site

The IssueOps documentation site is published to GitHub Pages by a GitHub Actions workflow.

## Workflow

The publishing workflow is `.github/workflows/pages.yml`.

It runs when:

- changes are pushed to `main`; or
- a maintainer starts it manually with `workflow_dispatch`.

## Build and deploy path

The workflow uses the standard GitHub Pages action path:

1. Check out the repository.
2. Configure GitHub Pages.
3. Set up Python.
4. Install pinned documentation dependencies from `requirements.txt`.
5. Run `mkdocs build --strict`.
6. Upload the generated `site/` directory as a Pages artifact.
7. Deploy the artifact to GitHub Pages.

The strict MkDocs build is the publishing gate. If MkDocs cannot build the site, the workflow should fail before deployment.

## Permissions

The workflow uses job-scoped permissions so each job receives only what it needs.

The build job uses:

- `contents: read` to read the repository contents.

The deploy job uses:

- `pages: write` to publish the Pages artifact; and
- `id-token: write` for the Pages deployment identity token.

The workflow does not grant write access to repository contents and does not change issues, pull requests, branch protection, labels or wiki content.

## Dependency pinning

The workflow installs documentation dependencies from `requirements.txt` instead of installing the latest MkDocs release on every run.

This keeps local validation and CI publishing aligned and reduces the risk that an upstream MkDocs release unexpectedly breaks Pages deployment.

## Manual repository setting

The repository may still need GitHub Pages configured to use GitHub Actions as the Pages source.

If the site does not publish after this workflow is merged, check the repository settings:

1. Open repository settings.
2. Open Pages.
3. Under build and deployment, set the source to GitHub Actions.

This setting is repository-level configuration and is not changed by the workflow file itself.

## Local validation

Before changing publishing configuration, validate the site locally with:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

See [Local MkDocs validation](local-validation.md) for setup and fallback validation notes.

## Boundary

This publishing workflow only publishes the MkDocs documentation site to GitHub Pages. It does not add automatic Codex execution, auto-merge, branch protection changes, application code or deployment targets other than GitHub Pages.
