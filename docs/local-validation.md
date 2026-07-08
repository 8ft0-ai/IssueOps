# Local MkDocs validation

Use these checks before asking for review on documentation-site changes.

For broader validation expectations by change type, see [Change-type validation guidance](change-type-validation.md). For factual consistency checks, see the [Documentation currency checklist](documentation-currency.md).

## Build the site

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs build --strict
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Then run:

```powershell
python -m pip install -r requirements.txt
mkdocs build --strict
```

The `requirements.txt` file pins the documentation tooling used by both local validation and the GitHub Pages publishing workflow.

## Preview the site

To preview the site locally:

```bash
mkdocs serve
```

Then open the local URL printed by MkDocs.

## Publishing validation

The GitHub Pages publishing workflow also installs the pinned documentation dependencies and runs:

```bash
mkdocs build --strict
```

The generated `site/` directory is uploaded as the Pages artifact only after the strict build succeeds. A failed MkDocs build should block deployment.

See [Publishing the documentation site](publishing.md) for the CI publishing path, workflow triggers, permissions and manual repository setting.

## Pre-merge and post-merge validation boundaries

Some checks can be completed before merge. Others can only be completed after the change is merged, deployed, released or configured in the repository environment.

Use the PR evidence pack to separate these states.

| Change type | Pre-merge validation examples | Post-merge verification examples |
| --- | --- | --- |
| Documentation-only change | Read changed files from the branch, review links, apply the [documentation currency checklist](documentation-currency.md), review `mkdocs.yml`, run `mkdocs build --strict`. | Usually none, unless the published site needs to be checked after merge. |
| Workflow change | Review YAML, triggers, permissions, dependency installation, artifact paths and local build where available. Apply the [workflow-change review checklist](workflow-changes.md). | Observe the workflow run after merge or manual dispatch. |
| Publishing change | Run MkDocs build, review Pages workflow path, apply the [workflow-change review checklist](workflow-changes.md) when workflow files change, and confirm manual settings are documented. | Check Pages deployment, public URL and repository Pages source setting. |
| Release change | Review release notes, tag wording, version references and changelog links. Apply the [documentation currency checklist](documentation-currency.md). | Confirm tag or release publication after it is created. |
| Environment-specific change | Review configuration files and document expected environment state. | Confirm the external setting or environment state after it is available. |

Pending validation should block merge when it is needed to decide whether the issue contract was satisfied. Post-merge verification can be acceptable when the implementation is complete, available validation is not failing and the remaining check cannot run before merge or deployment.

## Manual validation fallback

If MkDocs or the pinned dependencies are not available in the current environment, record that clearly in the pull request and perform the best available manual checks:

- read changed Markdown files back from the branch;
- review `mkdocs.yml` navigation against the issue acceptance criteria;
- inspect internal documentation links;
- apply the [documentation currency checklist](documentation-currency.md) when docs mention releases, roadmap stages, workflows, repository settings, labels, PRs, issues or automation;
- apply the [workflow-change review checklist](workflow-changes.md) when workflow files or workflow descriptions changed;
- apply the [change-type validation guidance](change-type-validation.md) to avoid claiming irrelevant validation;
- confirm the site distinguishes canonical docs from wiki/project-memory material;
- confirm existing Stage 1 workflow content remains accurate; and
- confirm no wiki cleanup, automation, branch protection, auto-merge or application code changes were introduced.

Do not mark the MkDocs build as complete unless `mkdocs build` actually ran successfully.
