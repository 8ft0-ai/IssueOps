# Local MkDocs validation

Use these checks before asking for review on documentation-site changes.

## Build the site

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install mkdocs
mkdocs build --strict
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Then run:

```powershell
python -m pip install mkdocs
mkdocs build --strict
```

## Preview the site

To preview the site locally:

```bash
mkdocs serve
```

Then open the local URL printed by MkDocs.

## Publishing validation

The GitHub Pages publishing workflow also runs:

```bash
mkdocs build --strict
```

The generated `site/` directory is uploaded as the Pages artifact only after the strict build succeeds. A failed MkDocs build should block deployment.

See [Publishing the documentation site](publishing.md) for the CI publishing path, workflow triggers, permissions and manual repository setting.

## Manual validation fallback

If MkDocs is not available in the current environment, record that clearly in the pull request and perform the best available manual checks:

- read changed Markdown files back from the branch;
- review `mkdocs.yml` navigation against the issue acceptance criteria;
- inspect internal documentation links;
- confirm the site distinguishes canonical docs from wiki/project-memory material;
- confirm existing Stage 1 workflow content remains accurate; and
- confirm no wiki cleanup, automation, branch protection, auto-merge or application code changes were introduced.

Do not mark the MkDocs build as complete unless `mkdocs build` actually ran successfully.
