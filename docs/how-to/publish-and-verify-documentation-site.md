# Publish and verify the documentation site

IssueOps publishes the MkDocs site through `.github/workflows/pages.yml`.

Use this guide to validate the site artefact before merge and verify the public Pages deployment afterwards. It does not authorise workflow or repository-setting changes unless the execution contract explicitly includes them.

## 1. Validate the documentation before PR approval

Run:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

For significant reader-path changes, inspect the generated site locally with `mkdocs serve` or download the PR workflow’s Pages artefact.

## 2. Inspect the PR workflow

The documentation workflow should:

1. check out the repository;
2. configure GitHub Pages;
3. install Python and committed dependencies;
4. run `mkdocs build --strict`;
5. upload the generated `site/` directory; and
6. skip production deployment for the pull request.

Confirm the successful build belongs to the final PR head. A successful artefact build is pre-merge evidence; it is not production deployment proof.

## 3. Review permissions and settings

The build job requires repository read access. The production deploy job requires Pages and identity-token permissions as configured in the workflow.

GitHub Pages must use GitHub Actions as the repository build and deployment source. That setting is outside the workflow file. Do not claim it was changed through a documentation PR.

When the setting cannot be observed before merge, record it as post-merge verification or repository-owner confirmation.

## 4. Merge only after documentation gates pass

Before merge, confirm:

- strict build passed;
- navigation and links were inspected;
- generated artefact is valid where material;
- no required check is failing;
- the PR evidence reflects the final head; and
- repository policy and human authority permit merge.

## 5. Verify the merged workflow

After merge, inspect the workflow run for the merge commit. Confirm:

- build job succeeded;
- Pages artefact uploaded;
- deploy job ran successfully;
- the deployment references the expected merge commit; and
- no permission or environment failure occurred.

## 6. Verify the public site

Open the published site and inspect:

- the home page;
- changed navigation;
- representative changed pages;
- compatibility routes when URLs were preserved; and
- rendered code blocks, tables and links that matter to the issue.

Record the deployed URL, workflow run, commit and representative pages checked.

## 7. Handle failure honestly

When build or deployment fails:

- do not mark post-merge verification complete;
- diagnose whether the cause is content, workflow or repository setting;
- use a bounded issue and PR for any required fix; and
- record the failed and successful follow-up evidence.

Do not change Pages source, workflow permissions or deployment targets as an undocumented recovery action.

## Historical evidence

Past delivery evidence belongs in project records rather than this current procedure. See the [Stage 2 delivery and release records](https://github.com/8ft0-ai/IssueOps/tree/main/planning/delivery) and the repository’s workflow history for the original production verification.

## Related guidance

- [Validate a documentation change](validate-documentation-change.md)
- [Validation status and fallback policy](../reference/validation-status-and-fallback-policy.md)
- [Workflow-change review checklist](../workflow-changes.md)
