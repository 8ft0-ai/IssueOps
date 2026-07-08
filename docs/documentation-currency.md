# Documentation currency checklist

Documentation changes should be accurate for the current repository state.

A page can build successfully and still mislead readers if it describes a planned release as complete, a future automation as implemented, an open PR as merged or a manual repository setting as code-managed.

Use this checklist for documentation pull requests, especially when the change mentions releases, roadmap stages, workflows, public publishing, repository settings, labels, PRs, issues or automation.

This is a manual review aid. It does not add automated fact checking, release automation, GitHub Pages changes or wiki cleanup.

## Checklist

Before review, confirm:

- [ ] Release tags mentioned in the docs exist or are clearly described as planned.
- [ ] Completed stages are described as complete only after merge or release.
- [ ] Future stages are described as future possibilities, not implemented capabilities.
- [ ] Open PRs and merged PRs are described with the correct state.
- [ ] Repository settings are described as manual where they cannot be changed in code.
- [ ] Workflow availability is accurate for the current branch or merge state.
- [ ] Public site status is described accurately, including any post-merge verification still required.
- [ ] Automation that has not been implemented is not described as available.
- [ ] Internal links point to the intended canonical docs.
- [ ] Wiki or project-memory material is not described as canonical unless that is explicitly true.

## Common factual-risk areas

### Releases and tags

If a release tag is mentioned, confirm whether it exists.

Acceptable wording:

- Current: `The first baseline release is v0.1.0.`
- Planned: `A future release may capture this baseline.`
- Pending: `The release tag has not yet been created.`

Avoid wording that describes a planned or recommended release as already published.

### Roadmap stages

Roadmap stages should distinguish current, completed, pending and future work.

Acceptable wording:

- Completed: `Stage 2.6 adds a workflow-change review checklist.`
- Future: `Future stages may explore carefully bounded Codex execution triggers.`
- Pending: `This remains pending post-merge verification.`

Avoid wording that turns a roadmap possibility into an implemented capability.

### Pull requests and issues

When PRs or issues are referenced, confirm the state being claimed.

Acceptable wording:

- `PR #22 added the GitHub Pages publishing workflow.`
- `Issue #30 proposes lightweight lifecycle labels.`
- `This issue is not implemented yet.`

Avoid using historical PRs as required reading unless they are genuinely necessary for the current process.

### Repository settings

Some repository behaviour cannot be changed through Markdown or workflow files.

Acceptable wording:

- `The repository owner may need to confirm the Pages source setting manually.`
- `This documentation records the expected setting; it does not change the setting itself.`

Avoid wording that suggests a setting was changed in code when it was only documented.

### Workflow availability

Workflow descriptions should be accurate for the branch and merge state.

Acceptable wording:

- Before merge: `This workflow will run after it is merged to main or manually dispatched where available.`
- After merge: `The workflow runs on pushes to main and can be manually dispatched.`
- Pending: `The first deployment still needs to be observed after merge.`

Avoid claiming a workflow has run if it has only been reviewed or added to a branch.

### Automation claims

Be explicit about the manual boundary.

Acceptable wording:

- `This checklist is manual.`
- `This protocol does not add required checks or branch protection.`
- `Future automation must be introduced through its own issue contract.`

Avoid implying that labels, checks, bots, Codex execution, auto-merge or enforcement exist unless they have actually been implemented.

## PR evidence

For documentation changes, record the currency check in the PR body.

Example:

```md
## Documentation currency check

- [x] Release tags mentioned are current or described as planned.
- [x] Roadmap stages distinguish completed work from future possibilities.
- [x] Workflow and repository-setting claims are accurate for the current branch state.
- [x] No unsupported automation is described as implemented.
```

If the check cannot be completed, state what remains unknown and whether that should block merge or become post-merge verification.

## Relationship to validation

The documentation currency check complements, but does not replace, MkDocs validation.

`mkdocs build --strict` confirms that the documentation site can build and that configured links are valid. It does not prove that claims about releases, workflows, labels, repository settings or roadmap state are factually current.
