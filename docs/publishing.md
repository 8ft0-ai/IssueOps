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

The build job uploads the generated `site/` directory as a Pages artifact, but it does not deploy the site.

The deploy job uses:

- `pages: write` to publish the Pages artifact; and
- `id-token: write` for the Pages deployment identity token.

The workflow does not grant write access to repository contents and does not change issues, pull requests, branch protection, labels or wiki content.

## Dependency pinning

The workflow installs documentation dependencies from `requirements.txt` instead of installing the latest MkDocs release on every run.

This keeps local validation and CI publishing aligned and reduces the risk that an upstream MkDocs release unexpectedly breaks Pages deployment.

## Production verification

The production publishing path was verified through GitHub Actions workflow run `28924550021`.

The run:

- built the MkDocs site successfully;
- installed the pinned documentation dependencies;
- completed `mkdocs build --strict` successfully;
- uploaded the GitHub Pages artifact;
- deployed commit `74a6c36f3d2e340f3969fe54b098098e688c5ad6`; and
- reported a successful deployment to `https://8ft0-ai.github.io/IssueOps/`.

The repository owner also confirmed that the live landing page and representative documentation pages rendered correctly. This verifies that the repository-level Pages source is configured for GitHub Actions and that the production publishing path is operational.

## Repository setting

GitHub Pages must use GitHub Actions as the build and deployment source. This setting is repository-level configuration and is not changed by the workflow file itself.

The production verification above confirms that the required setting is currently configured correctly. If a future deployment fails because the source setting changes:

1. Open repository settings.
2. Open Pages.
3. Under build and deployment, set the source to GitHub Actions.

## Local validation

Before changing publishing configuration, validate the site locally with:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

See [Local MkDocs validation](local-validation.md) for setup and fallback validation notes.

## Boundary

This publishing workflow only publishes the MkDocs documentation site to GitHub Pages. It does not add automatic Codex execution, auto-merge, branch protection changes, application code or deployment targets other than GitHub Pages.
