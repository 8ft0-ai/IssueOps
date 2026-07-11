# Stage 3 alpha prerelease

Recommended tag: `v0.3.0-alpha.1`

Release title: Stage 3 Alpha — Read-only Evidence-pack Assistance

Release classification: experimental prerelease.

Recommended stable baseline: [`v0.2.0`](stage-2.md).

## Summary

This prerelease captures the Stage 3 experiment in manually invoked, read-only pull-request evidence assistance. It is a fixed experimental snapshot for evaluation and controlled use; it is not the recommended IssueOps operating baseline and does not represent routine workflow adoption.

Stage 3 closed with decision **Adapt**. The collector proved that repository-native evidence can be assembled deterministically, with direct provenance and fail-closed handling of incomplete state, while preserving human authority over contract satisfaction, approval and merge. The experiment also exposed gaps that must be addressed before broader adoption.

## Included

- The `evidence-pack/v1` schema and evidence classifications.
- Deterministic JSON and Markdown rendering.
- A standard-library, read-only GitHub REST collector for one repository and one pull request.
- Manual GitHub Actions invocation through `workflow_dispatch`.
- Read-only access to repository contents, pull requests, issues, checks and Actions.
- Pull-request head resolution at the start and end of collection.
- Explicit pending, unavailable, conflicting and non-complete states.
- Bounded pagination and partial-failure handling.
- Run-summary output and seven-day downloadable artefacts.
- Repository-native tests for schema, rendering, collection, pagination, stale-head and error behaviour.

## Experimental proof

Live dogfood against PR #85 captured two reports for the same stable pull-request head:

- a pending report marked `incomplete` while relevant validation was still running; and
- a final report marked `complete` after validation finished.

The skipped Pages deployment remained an observed fact rather than approval advice. Live job evidence confirmed read-only permissions, and the collector performed no repository mutation.

The experiment reduced repeated mechanical evidence gathering, but human inspection and substantive contract interpretation remained necessary.

## Known limitations

- Execution-contract issue discovery depends on GitHub closing-keyword syntax.
- A PR that links its contract without `Closes`, `Fixes` or `Resolves` may omit that issue from the report.
- Unresolved inline review-thread state is not collected.
- PR conversation and submitted-review evidence is summarised rather than presented as a complete review narrative.
- The operator must navigate to Actions, select the workflow context, enter the pull-request number and coordinate collection timing.
- Artefacts expire after seven days.
- Collection remains bounded by configured pagination and workflow-run limits.
- Generated evidence still requires human assessment of scope, risk, sufficiency and contract fulfilment.

The first ordinary follow-up after Stage 3, PR #87, used manually assembled validation evidence rather than the collector as its primary mechanical evidence source. This demonstrated that technical operation and controlled usefulness were proved, but routine operational adoption was not.

## Authority boundaries retained

This prerelease does not authorise:

- automatic or scheduled evidence collection;
- issue readiness or implementation-plan approval;
- issue, pull-request, review, label, branch, commit, file, merge or repository-setting mutation by the collector;
- lifecycle-state transitions or remediation decisions;
- approval, merge, publication or deployment recommendations;
- bounded execution triggering;
- auto-merge;
- cross-repository rollout; or
- Stage 4 implementation.

Humans retain authority over contract interpretation, evidence sufficiency, risk acceptance, approval, merge and publication.

## Release status

`v0.3.0-alpha.1` is suitable only as an experimental snapshot for evaluating the Stage 3 collector and its evidence model. The current recommended stable IssueOps baseline remains `v0.2.0`.

The Stage 3 decision remains **Adapt**. Broader use should wait for separately planned improvements to explicit non-closing contract linkage, review completeness and invocation ergonomics.

The connected GitHub tooling used to prepare these notes does not expose tag or GitHub Release creation. After this documentation change is merged, creating the `v0.3.0-alpha.1` tag and marking the associated GitHub Release as a prerelease remain explicit repository-owner actions.
