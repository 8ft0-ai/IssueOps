# Validate a documentation change

Use this guide for Markdown, MkDocs navigation, examples, release wording and other user-facing documentation changes.

For the canonical matrix, use [Validation by change type](../reference/validation-by-change-type.md). For unavailable checks, use [Validation status and fallback policy](../reference/validation-status-and-fallback-policy.md).

## 1. Read changed files back

Inspect every changed documentation and configuration file from the feature branch. Confirm the final content, headings, code fences, links and terminology.

Compare the changed-file list with the issue and implementation plan. Remove or explain unexpected files.

## 2. Check navigation and links

When `mkdocs.yml` changes, confirm each page appears once in its primary mode and each target exists.

Review internal links by source inspection and strict build output. For compatibility pages, inspect both the old path and the canonical destination.

## 3. Check documentation currency

Apply the [documentation currency checklist](../documentation-currency.md) when the change mentions releases, roadmap stages, issue or PR state, workflow behaviour, repository settings, labels, public site status or automation.

Distinguish current, experimental, planned, pending and historical capability accurately.

## 4. Check related guidance

Compare the changed page with canonical Reference and nearby procedures. Confirm that:

- no mandatory rule exists only in Explanation;
- no compatibility page becomes a competing source;
- human authority boundaries remain consistent; and
- project records are linked rather than duplicated.

## 5. Run the strict build

Install committed dependencies and build:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

A strict-build failure blocks approval until it is corrected and rerun.

## 6. Inspect rendered output when material

For significant navigation, tutorial, template or layout changes, use one of:

```bash
mkdocs serve
```

or the generated GitHub Pages artefact from the PR workflow.

Inspect the reader path, rendered code blocks, tables, navigation labels and relative links—not merely the existence of generated HTML.

## 7. Record the evidence

In the PR evidence pack, state:

- exact final head;
- files read back;
- strict-build run and result;
- navigation/link/currency checks;
- rendered pages inspected;
- contradictory-guidance or scope review; and
- post-merge publication checks, if any.

Do not mark local validation complete when only the repository workflow ran. Name the evidence source accurately.

## 8. Verify after merge when publishing changes

When the public site changes, confirm the merged workflow, deployed URL and representative pages. A passing PR build proves the artefact, not the production Pages deployment.

## Common failure modes

- relying on visual source review without strict build;
- checking navigation but not generated links;
- copying historical records into user guidance;
- claiming a planned capability is implemented;
- using a passing build from an earlier head; or
- treating merge success as published-site proof.
