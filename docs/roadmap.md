# Roadmap

This roadmap is intentionally conservative. The project starts by proving the manual execution-contract workflow before adding automation.

## Current baseline: Stage 1

Stage 1 establishes the manual execution-contract IssueOps baseline.

It includes:

- structured issue contracts;
- readiness checks before implementation;
- implementation plans before file changes;
- safe tool-operation checks before repository mutations;
- one branch per issue;
- Codex-assisted implementation within the contract;
- lightweight validation evidence;
- pull requests as evidence packs; and
- human contract verification before merge.

The first baseline release is [`v0.1.0`](releases/stage-1.md).

## Stage 2.1: Canonical documentation site

Stage 2.1 creates the MkDocs/GitHub Pages documentation track. The goal is to give readers a stable, curated entry point for the project thesis, workflow, controls, examples and release notes.

This stage keeps the wiki separate as project memory. It does not clean up or rewrite the wiki.

## Stage 2.2: GitHub Pages publishing

Stage 2.2 adds the publishing path for the MkDocs documentation site.

It introduces a GitHub Actions workflow that builds the site with `mkdocs build --strict`, uploads the generated `site/` directory as a Pages artifact and deploys it to GitHub Pages. The workflow runs on pushes to `main` and can also be started manually.

See [Publishing the documentation site](publishing.md) for the workflow, permissions and manual repository setting.

## Stage 2.3: Operating protocol hardening

Stage 2.3 documents the manual IssueOps operating protocol as a first-class process contract.

It makes the issue-to-PR lifecycle easier to follow by describing the readiness gate, implementation plan, branch discipline, safe tool-operation check, validation evidence, PR evidence pack, contract verification, review remediation and post-merge verification boundary in one canonical place.

See [IssueOps operating protocol](issueops-protocol.md) for the process overview.

## Stage 2.4: Dependency-aware readiness

Stage 2.4 strengthens the readiness gate by requiring dependency state and a safe starting point to be recorded before branch creation.

It documents how to handle issues with no dependency, satisfied dependencies, unsatisfied blocking dependencies and repository-setting or environment dependencies. This remains a manual readiness control and does not add automated dependency detection or branch enforcement.

See [IssueOps operating protocol](issueops-protocol.md#dependency-check-format) for the dependency-check format.

## Stage 2.5: Documentation currency checks

Stage 2.5 adds a reusable checklist for documentation currency and factual consistency.

It covers release tags, completed versus future stages, merged versus open PRs, repository settings, workflow availability, public site status and unsupported automation claims. This remains a manual documentation review aid and does not add automated fact checking, release automation, Pages publishing changes or wiki cleanup.

See [Documentation currency checklist](documentation-currency.md) for the detailed guidance.

## Stage 2.6: Workflow-change review checklist

Stage 2.6 adds a focused checklist for pull requests that add or change GitHub Actions workflows.

It covers trigger scope, job-scoped permissions, pinned or bounded dependencies, build/deploy separation, artifacts, environments, secrets, OIDC permissions, manual repository settings, failure behaviour and unsupported automation claims. This remains a manual review checklist and does not add workflow linting, required checks, branch protection or workflow behaviour changes.

See [Workflow-change review checklist](workflow-changes.md) for the detailed guidance.

## Stage 2.7: PR review remediation protocol

Stage 2.7 defines how review feedback should be classified, addressed and evidenced.

It covers required fixes, optional improvements, clarification-needed items, out-of-scope feedback, validation reruns, thread replies, thread resolution and remediation summaries. This remains a manual review protocol and does not add review bots, required review rules, permission changes or automatic thread resolution.

See [PR review remediation](review-remediation.md) for the detailed guidance.

## Stage 2.8: Material remediation evidence updates

Stage 2.8 defines when material review remediation must update the PR body or add a clearly labelled remediation evidence comment.

It covers materiality criteria, final contract checks, validation reruns, scope impact and the distinction between minor comment replies and material evidence updates. This remains a manual evidence protocol and does not add PR automation, templates, branch protection or required checks.

See [Pull requests as evidence packs](pr-evidence-packs.md#remediation-evidence) and [PR review remediation](review-remediation.md#material-remediation) for the detailed guidance.

## Stage 2.9: Pre-merge and post-merge validation protocol

Stage 2.9 strengthens validation evidence by separating checks that must be completed before merge from checks that can only be verified after merge, deployment, release or environment configuration.

It documents when pending validation should block merge, when post-merge verification can be acceptable and how the PR evidence pack should record both states. This remains a manual evidence protocol and does not add labels, automation, required checks or branch protection.

See [Pull requests as evidence packs](pr-evidence-packs.md#validation-status) and [Contract verification](contract-verification.md#pre-merge-versus-post-merge-checks) for the detailed guidance.

## Stage 2.10: Lifecycle labels

Stage 2.10 defines a minimal advisory label set for the manual IssueOps lifecycle.

It covers draft contracts, ready contracts, posted plans, review changes requested, pending validation and post-merge verification needs. These labels support visibility only; they do not trigger automation or replace written issue and PR evidence. The labels are documented as recommended until the repository label definitions are created through GitHub UI/API tooling.

See [Manual lifecycle labels](labels.md) for the detailed guidance.

## Stage 2.11: Change-type validation guidance

Stage 2.11 defines lightweight validation expectations by change type.

It covers documentation, workflow, publishing/deployment, process-label and future application-code changes. The guidance explains expected, optional and not-applicable validation so PR evidence can be specific without overstating checks that did not run.

See [Change-type validation guidance](change-type-validation.md) for the definitions of done.

## Future work

Future stages may explore:

- richer documentation examples;
- lightweight release documentation;
- carefully bounded Codex execution triggers; and
- stronger review evidence gates.

These items are future possibilities, not implemented capabilities.

## Non-goals for the current baseline

The current baseline does not include automatic review bots, automatic dependency detection, automatic Codex execution, automatic label transitions, automatic workflow linting, automatic post-merge verification, automated fact checking, auto-merge, branch protection changes, required status checks for agent work or application code.

Any future automation should be introduced through its own execution contract, implementation plan, validation evidence and human review.
