# Change-type validation guidance

Validation should match the kind of change being reviewed.

A documentation-only pull request, a workflow pull request, a publishing change, a process-label change and a future application-code change do not need identical evidence. They do need the same discipline: record what actually ran, identify what did not run and avoid marking unavailable validation as complete.

This page defines lightweight definitions of done by change type. It is not an exhaustive validation framework and does not add automated test runners, GitHub Actions, required status checks, branch protection or application code.

## How to use this page

Use the issue contract to identify the change type before implementation starts.

If a pull request covers more than one type, apply each relevant section and make the combined validation evidence clear in the PR body.

Use three evidence categories:

- **Expected:** validation that should normally be completed for this change type.
- **Optional:** validation that may be useful depending on risk or environment.
- **Not applicable:** validation that should not be claimed unless the change actually requires it.

Do not mark validation complete unless it actually ran.

## Documentation changes

Documentation changes include updates to Markdown files, MkDocs navigation, examples, release notes, process docs and repository-facing explanatory text.

Expected validation:

- changed documentation files read back from the branch;
- MkDocs navigation reviewed when navigation changes;
- internal links checked by inspection or build output;
- `mkdocs build --strict` run with the pinned documentation dependency;
- [documentation currency checklist](documentation-currency.md) applied where release, roadmap, PR, workflow, setting, label or capability status is mentioned;
- scope checked to confirm no unrelated automation, app code or repository settings changed.

Optional validation:

- local `mkdocs serve` preview for substantial page changes;
- spell, grammar or style review for user-facing pages;
- comparison with related pages to avoid contradictory guidance.

Not applicable unless explicitly scoped:

- application tests;
- workflow execution;
- branch protection checks;
- deployment validation.

## Workflow changes

Workflow changes include additions or edits to `.github/workflows/*`, workflow triggers, permissions, build jobs, deployment jobs, dependency installation, artifacts, environments, secrets or OIDC usage.

Expected validation:

- changed workflow files read back from the branch;
- YAML structure reviewed;
- trigger scope checked against the issue contract;
- permissions checked for least practical scope, preferably job-scoped where jobs need different authority;
- dependencies checked for pinned, locked or deliberately bounded installation;
- build, validation, artifact and deployment responsibilities reviewed;
- manual repository settings documented when they cannot be changed in code;
- post-merge verification needs identified where the workflow cannot run before merge;
- [workflow-change review checklist](workflow-changes.md) applied;
- scope checked to confirm no unsupported automation, branch protection, auto-merge or app code changed.

Optional validation:

- workflow syntax linting if available;
- dry-run or CI run if the workflow can safely run before merge;
- review against prior workflow incidents or review comments.

Not applicable unless explicitly scoped:

- unrelated application tests;
- label creation;
- branch protection changes.

## Publishing or deployment configuration changes

Publishing or deployment configuration changes include documentation publishing, Pages configuration, deployment artifacts, release publication paths and environment configuration that affects deployed output.

Expected validation:

- changed configuration and documentation files read back from the branch;
- build command run locally or in CI where available;
- artifact path reviewed;
- deployment target reviewed;
- manual repository or environment settings documented;
- pre-merge validation separated from post-merge verification;
- post-merge checks listed when deployment cannot be observed before merge;
- scope checked to confirm no unrelated deployment target or application code changed.

Optional validation:

- manual dispatch in a safe environment;
- published URL check after merge;
- repository settings screenshot or reviewer confirmation where appropriate.

Not applicable unless explicitly scoped:

- broad release automation;
- auto-merge changes;
- unrelated workflow refactoring.

## Process or label changes

Process or label changes include updates to IssueOps lifecycle docs, review protocols, PR evidence expectations, label guidance and any repository label creation or modification.

Expected validation:

- changed docs read back from the branch;
- MkDocs build run when docs change;
- label changes explicitly recorded as created, updated, removed or left as recommendations only;
- manual versus automated behaviour clearly distinguished;
- guidance checked for consistency with the operating protocol;
- scope checked to confirm no automation is implied unless implemented.

Optional validation:

- search for contradictory label names or process terms in existing docs;
- check examples against recent PRs;
- confirm repository label availability if labels are created or referenced as existing.

Not applicable unless explicitly scoped:

- GitHub Actions changes;
- branch protection changes;
- application tests;
- deployment checks.

If repository label creation is not available in the current tool environment, record the affected labels as recommended-only rather than claiming they were created.

## Future application-code changes

Application-code validation is intentionally general until the repository contains application code.

Expected validation for future app-code work:

- changed source files read back from the branch;
- relevant tests run and results recorded;
- build or type checks run where available;
- affected behaviour checked against acceptance criteria;
- error handling reviewed where user-provided or external data is involved;
- compatibility with existing conventions checked;
- validation gaps recorded as pending or not performed.

Optional validation:

- manual smoke test;
- targeted regression test;
- log or runtime check in a safe environment;
- security review for sensitive flows.

Not applicable unless explicitly scoped:

- documentation publishing checks;
- label lifecycle changes;
- unrelated workflow refactoring.

## PR evidence format

In the PR evidence pack, record the change type and validation performed.

Example:

```md
## Change type

- Documentation change
- Workflow change

## Validation status

Pre-merge validation completed:

- [x] Changed docs read back from branch
- [x] MkDocs build passed
- [x] Workflow checklist applied

Post-merge verification required:

- [ ] Workflow run observed after merge

Validation not performed:

- Application tests: not applicable; no application code changed.
```

See [Pull requests as evidence packs](pr-evidence-packs.md) for the broader evidence-pack structure and [Local MkDocs validation](local-validation.md) for documentation-site validation commands.
