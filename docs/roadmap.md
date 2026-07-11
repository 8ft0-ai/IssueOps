# Roadmap

IssueOps develops the operating model in deliberate stages. Each stage must preserve the central contract: the issue bounds the work, the pull request carries evidence, and a human retains approval authority.

This page is the concise public roadmap. Detailed stage intent, retrospective delivery evidence and close-out records live in the top-level `planning/` control surface. GitHub issues, pull requests, reviews, commits and workflow runs remain the canonical detailed audit trail.

## Stage 1 — Manual execution-contract foundation

Status: complete.

Stage 1 established the manual execution-contract IssueOps baseline:

- structured issue contracts;
- readiness checks before implementation;
- implementation plans before file changes;
- safe tool-operation checks before repository mutations;
- one branch per issue;
- agent-assisted implementation within the contract;
- lightweight validation evidence;
- pull requests as evidence packs; and
- human contract verification before merge.

The Stage 1 baseline is released as [`v0.1.0`](releases/stage-1.md).

## Stage 2 — Published and hardened operating model

Status: complete, with one explicitly deferred non-blocking limitation.

Stage 2 extended the manual baseline through five capability groups.

### Canonical documentation and publishing

Stage 2 introduced the MkDocs documentation site, GitHub Pages publishing, pinned strict builds, production deployment from `main`, and verified live-site evidence.

### Operating-protocol consolidation

The repository now has one canonical protocol covering readiness, dependency checks, planning, branch discipline, safe operations, validation, PR evidence, contract verification, remediation and post-merge verification.

### Evidence and validation controls

Stage 2 added documentation-currency checks, workflow-change review, change-type validation guidance, compact PR evidence templates, material-remediation updates, and a clear distinction between pre-merge validation and post-merge verification.

Repository-native validation is preferred. Pull requests automatically build the documentation site and upload the Pages artefact, while production deployment is skipped until the change reaches `main`.

### Bounded delegation and usability

Stage 2 defined owner-authorised delegated batch mode, batch completion summaries and compact safe-operation evidence for routine low-risk work. A complete dogfood run tested the protocol, and a contributor usability review improved the front door without removing specialised controls.

### Advisory lifecycle visibility

Stage 2 defines a small lifecycle label model, but the additional repository label definitions were not created because the connected tooling cannot create labels with descriptions and colours. Issue #54 was closed as a non-blocking deferred limitation.

Written issue and pull-request evidence remains canonical. No workflow depends on the missing labels.

The Stage 2 baseline is documented in the [`v0.2.0` release recommendation](releases/stage-2.md).

## Stage 3 — Read-only evidence-pack assistance

Status: delivering; deterministic schema and local renderer in progress.

Stage 3 selected one bounded automation capability through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75): manually invoked, read-only pull-request evidence collection and evidence-pack assistance.

The first implementation slice defines the [`evidence-pack/v1` schema](evidence-pack-schema.md), deterministic validation and stable JSON and Markdown rendering. This core is local and standard-library only. It does not yet collect live GitHub data or publish generated evidence.

The selected capability is intended to assemble a current, structured and provenance-linked evidence report for one pull request while preserving the written repository record and all human authority. It may report observed, contributor-reported, derived, pending, unavailable or conflicting evidence, but it may not:

- decide issue readiness or approve implementation plans;
- post or edit issue or pull-request content;
- change labels or lifecycle state;
- create branches, commits, issues or pull requests;
- classify material remediation;
- recommend or perform merge;
- approve publication or deployment; or
- infer success from missing, skipped, pending or contradictory evidence.

The detailed approved roadmap is recorded in [`planning/roadmap/stage-03-read-only-evidence-pack-assistance.md`](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/stage-03-read-only-evidence-pack-assistance.md).

The later live GitHub integration, end-to-end dogfood and adopt/adapt/reject decision remain separate execution-contract slices. Lifecycle assistance, post-merge verification automation, bounded execution triggering and auto-merge remain deferred and unauthorised.

## Current exclusions

The current baseline does not include:

- automatic agent execution;
- automatic dependency detection;
- automatic lifecycle transitions;
- automatic review bots;
- automatic post-merge verification;
- required status checks for agent work;
- branch protection changes;
- GitHub auto-merge configuration; or
- autonomous publication decisions.

Any future automation must be introduced through its own bounded planning and execution contracts, validation evidence and human review.
