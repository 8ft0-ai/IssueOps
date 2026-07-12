# Local MkDocs validation

Use the focused [Validate a documentation change](how-to/validate-documentation-change.md) guide for the complete procedure.

## Core commands

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs build --strict
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
mkdocs build --strict
```

For a local preview:

```bash
mkdocs serve
```

The committed `requirements.txt` aligns local and repository workflow dependencies.

## When local execution is unavailable

Do not mark the build complete. Record the limitation, read changed files back, inspect links and navigation, apply the relevant checklists and wait for repository-native validation when correctness depends on it.

Use [Validation status and fallback policy](reference/validation-status-and-fallback-policy.md) for the exact fallback and merge rules.

## Related guidance

- [Validation by change type](reference/validation-by-change-type.md)
- [Documentation currency checklist](documentation-currency.md)
- [Publish and verify the documentation site](how-to/publish-and-verify-documentation-site.md)

## Compatibility note

This URL is retained for existing local-build links. Exact validation ownership now belongs to the focused How-to and Reference pages above.
