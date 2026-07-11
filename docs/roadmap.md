# Roadmap

IssueOps develops the operating model in deliberate stages. Each stage must preserve the central contract: the issue bounds the work, the pull request carries evidence, and a human retains approval authority.

This page is the concise public roadmap. Detailed stage intent, delivery evidence and close-out records live in the top-level `planning/` control surface. GitHub issues, pull requests, reviews, commits and workflow runs remain the canonical detailed audit trail.

## Stage 1 — Manual execution-contract foundation

Status: complete.

Stage 1 established the manual execution-contract baseline: structured issue contracts, readiness and planning gates, branch discipline, safe tool operations, validation evidence, pull requests as evidence packs and human contract verification before merge.

The Stage 1 baseline is released as [`v0.1.0`](releases/stage-1.md).

## Stage 2 — Published and hardened operating model

Status: complete, with one explicitly deferred non-blocking limitation.

Stage 2 added the canonical MkDocs site and GitHub Pages path, consolidated the operating protocol, introduced repository-native validation and evidence controls, defined bounded delegated batch mode, and dogfooded the full workflow. Production deployment remains restricted to `main` and the additional lifecycle label definitions remain deferred.

The Stage 2 baseline is documented in the [`v0.2.0` release recommendation](releases/stage-2.md).

## Stage 3 — Read-only evidence-pack assistance

Status: complete; decision **Adapt**.

Stage 3 selected and delivered one bounded automation capability: manually invoked, read-only pull-request evidence collection for one repository and one pull request.

The implementation includes the [`evidence-pack/v1` schema](evidence-pack-schema.md), deterministic JSON and Markdown rendering, provenance validation, stale-head and partial-failure controls, and a manual GitHub Actions workflow using read-only permissions. Generated output is limited to the individual run summary and downloadable artefact.

Live dogfood against PR #85 captured the same stable head while documentation validation moved from in progress to completed. The pending report was `incomplete`; the final report was `complete`; the skipped Pages deployment remained an observation rather than approval advice. The collector made no repository mutation and retained the human-decision boundary.

The capability is retained for controlled use, but broader adoption requires separately planned adaptation because:

- issue-contract linkage currently depends on GitHub closing-keyword syntax;
- unresolved inline review-thread state is not collected;
- manual workflow branch and timing selection is error-prone; and
- generated evidence still requires human interpretation.

Stage 3 did not authorise automatic invocation, lifecycle transitions, execution triggering, merge authority, auto-merge, repository-setting changes or cross-repository rollout.

## Current exclusions

The current baseline does not include:

- automatic agent execution or dependency detection;
- automatic lifecycle transitions or review bots;
- automatic post-merge verification;
- required status checks or branch-protection changes for agent work;
- GitHub auto-merge configuration; or
- autonomous publication decisions.

Any future automation must be introduced through its own planning and execution contracts, validation evidence and human review.
