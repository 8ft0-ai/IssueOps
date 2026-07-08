# Workflow-change review checklist

Workflow changes can affect repository permissions, deployment behaviour, dependency stability and publishing reliability even when the diff is small.

Use this checklist for any pull request that adds or changes files under `.github/workflows/*`.

This is a manual review aid. It does not add workflow linting, required status checks, branch protection or automated enforcement.

For broader validation expectations across documentation, workflow, publishing, process-label and future application-code changes, see [Change-type validation guidance](change-type-validation.md).

## When to use this checklist

Use this checklist when a change:

- adds a new GitHub Actions workflow;
- changes workflow triggers;
- changes job or workflow permissions;
- changes dependency installation in CI;
- changes build, test, artifact or deployment jobs;
- changes environment configuration;
- changes secret, token or OIDC usage; or
- changes documentation that describes workflow behaviour.

If a PR does not change workflow behaviour but mentions workflows, apply the checklist to the wording being changed. The goal is to avoid overstating automation or implying gates that do not exist.

## Checklist

For any PR that adds or changes `.github/workflows/*`, confirm:

- [ ] The trigger is limited to the intended event and branch.
- [ ] Workflow or job permissions are the narrowest practical permissions.
- [ ] Permissions are scoped to the job that needs them where practical.
- [ ] Build, validation, artifact upload and deployment responsibilities are separated where practical.
- [ ] Deployment jobs depend on successful validation or build jobs.
- [ ] Dependencies are pinned, locked or deliberately bounded.
- [ ] Artifact paths are explicit and expected.
- [ ] Secrets, tokens and OIDC permissions are available only to jobs that need them.
- [ ] Environment usage is explicit and matches the deployment target.
- [ ] Manual repository settings are documented when they cannot be changed in code.
- [ ] Failure behaviour is clear: failed validation should prevent deployment where appropriate.
- [ ] The change does not imply unsupported automation exists.

## Permissions

Prefer job-scoped permissions when different jobs need different authority.

For example, a documentation publishing workflow may need:

- `contents: read` for the build job;
- `pages: write` for the deploy job; and
- `id-token: write` only where OpenID Connect is required for deployment.

Avoid granting deployment permissions to build-only jobs unless the workflow needs that authority and the PR explains why.

## Dependencies

Avoid installing latest unbounded dependencies in repeatable CI or publishing paths.

Prefer one of these approaches:

- install from a pinned `requirements.txt`, lockfile or equivalent project dependency file;
- pin a tool version directly in the workflow when there is no shared dependency file; or
- explicitly document why the dependency is intentionally unpinned.

For documentation workflows, local validation and CI should use the same dependency source where practical.

## Build, artifact and deploy responsibilities

Review whether the workflow separates concerns clearly.

A common safe shape is:

1. Check out the repository.
2. Install pinned dependencies.
3. Run validation or build.
4. Upload an explicit artifact path.
5. Deploy only after the build job succeeds.

Not every workflow needs separate jobs, but deployment authority should not be broader than necessary.

## Triggers and manual dispatch

Check that workflow triggers match the issue contract.

For example:

- publishing workflows should usually run on pushes to the publishing branch or be manually dispatched;
- validation workflows may run on pull requests, pushes or both;
- scheduled workflows should state why a schedule is needed; and
- broad triggers should be justified in the PR evidence pack.

## Manual repository settings

Some behaviour cannot be configured only through a workflow file.

If a workflow depends on repository settings, the PR should record what remains manual. For GitHub Pages, this may include confirming that Pages source is configured for GitHub Actions.

Manual settings should be listed as post-merge verification when they cannot be checked before merge.

## Evidence to include in the PR

For workflow changes, the PR evidence pack should include:

- the workflow files changed;
- trigger scope;
- permission scope;
- dependency pinning or bounding approach;
- build, artifact and deployment path;
- any required manual repository settings;
- pre-merge validation completed;
- post-merge verification required; and
- confirmation that no unsupported automation, branch protection, auto-merge or app code was introduced.

## Example review focus from PR #22

PR #22 added the GitHub Pages publishing workflow. Review feedback found two issues that this checklist is intended to catch earlier:

- deployment permissions were initially granted at workflow scope rather than only to the deployment job; and
- MkDocs was initially installed as the latest available version rather than through a pinned dependency file.

Both were corrected, but they are now standard checklist items for future workflow work.

## Current manual boundary

This checklist supports review. It does not enforce workflow policy automatically.

Future automation, workflow linting, required checks or branch protection must be introduced through their own issue contract, implementation plan, validation evidence and human review.
