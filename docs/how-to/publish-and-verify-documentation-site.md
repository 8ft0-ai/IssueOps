# Publish and verify the documentation site

IssueOps publishes the MkDocs site through `.github/workflows/pages.yml`.

Use this guide to validate the site artefact before merge and verify the public Pages deployment afterwards. It does not authorise workflow or repository-setting changes unless the execution contract explicitly includes them.

## Verification evidence layers

Treat publication verification as four separate evidence layers. Evidence from one layer does not prove a later layer automatically:

1. **Candidate/source validation** — repository-native checks against the final branch or pull-request head, including the strict documentation build and generated candidate artefact.
2. **Production deployment evidence** — the post-merge production workflow and deployment result for the expected merged commit.
3. **Deployed artefact evidence** — evidence that the deployed site artefact contains the expected generated content, routes and links.
4. **Direct public/runtime observation** — inspection of the published URL in the environment readers actually reach, including representative rendered content and navigation.

When current machine-verifiable evidence already establishes an earlier layer, a human or external execution context performing the final direct observation does not need to repeat those checks. Record the remaining observation as its own evidence with its own provenance.

## 1. Validate the documentation before PR approval

Run:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

For significant reader-path changes, inspect the generated site locally with `mkdocs serve` or download the PR workflow’s Pages artefact.

This is candidate/source validation. It can establish that the final candidate builds and renders as expected, but it is not production deployment or public-runtime proof.

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

This is production deployment evidence. Where the deployment run or its artefact can also establish the generated content, routes or link integrity actually deployed, record that separately as deployed artefact evidence rather than describing it as direct public observation.

## 6. Verify the public site

Open the published site and inspect:

- the home page;
- changed navigation;
- representative changed pages;
- compatibility routes when URLs were preserved; and
- rendered code blocks, tables and links that matter to the issue.

This is direct public/runtime observation. Record it separately from source validation, deployment success and deployed artefact inspection.

When the observation is supplied by a human or another external execution context, the durable verification record should identify:

- the published URL or environment observed;
- the relevant immutable merge commit and deployment or workflow-run identity, where applicable;
- the observer or evidence source;
- the representative pages, routes or rendered behaviours checked; and
- the result as `PASS` or `FAIL`, with a material defect stated for a failure.

Describe the evidence source accurately. For example, record `repository owner in browser` or the named external execution context rather than implying that the agent performed an observation it could not perform.

A `PASS` or equivalent result satisfies only the named direct public/runtime verification check. It does not grant mutation, merge, production or issue-close authority. A `FAIL` remains failed verification evidence: do not mark post-merge verification complete, and route any required fix through the existing governed issue and remediation path.

Do not require the external observer to repeat candidate, deployment or deployed-artefact checks that are already current and sufficient. Narrow the external observation to the genuinely unavailable runtime evidence.

## 7. Handle failure honestly

When build, deployment, deployed artefact inspection or direct public/runtime observation fails:

- do not mark post-merge verification complete;
- diagnose whether the cause is content, workflow, deployment, repository setting or runtime rendering;
- use a bounded issue and PR for any required fix; and
- record the failed and successful follow-up evidence with its source and relevant immutable identity.

Do not change Pages source, workflow permissions or deployment targets as an undocumented recovery action.

## Historical evidence

Past delivery evidence belongs in project records rather than this current procedure. See the [Stage 2 delivery and release records](https://github.com/8ft0-ai/IssueOps/tree/main/planning/delivery) and the repository’s workflow history for the original production verification.

## Related guidance

- [Validate a documentation change](validate-documentation-change.md)
- [Validation status and fallback policy](../reference/validation-status-and-fallback-policy.md)
- [Workflow-change review checklist](../workflow-changes.md)
