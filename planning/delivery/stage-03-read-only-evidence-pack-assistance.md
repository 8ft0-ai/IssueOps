# Stage 3 — Read-only evidence-pack assistance

Status: completed.

Record type: contemporaneous.

## Original documented intent

Stage 3 was shaped through [planning issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) and the approved roadmap at `planning/roadmap/stage-03-read-only-evidence-pack-assistance.md`.

The stage selected one bounded automation capability: manually invoked, read-only collection of provenance-linked evidence for one pull request. The intended outcome was to reduce repetitive evidence assembly while preserving the written issue and pull-request record, making incomplete state visible, and leaving readiness, sufficiency, approval, merge and publication decisions with a human.

## Retrospective interpretation

Not applicable. Stage 3 was planned contemporaneously through an approved roadmap and delivered in four ordered slices.

The close-out decision is **Adapt**, not unconditional adoption. The stage is complete because the capability was implemented, dogfooded, measured and explicitly decided; the decision records the limitations that prevent broader adoption in its current form.

## What shipped

### Approved roadmap and authority boundary

- A reviewed Stage 3 roadmap with one-repository, one-pull-request scope.
- Explicit read-only permissions and prohibited repository mutations.
- A proof plan covering pending/final state, safe failure, effort comparison and authority audit.

### Deterministic evidence model

- `evidence-pack/v1` with repository-observed, contributor-reported, derived, pending, unavailable and conflicting classifications.
- Strict provenance and schema validation.
- Stable JSON and Markdown rendering.
- Stale-head, partial-failure and non-complete status semantics.

### Manually invoked GitHub integration

- Standard-library GitHub REST collector for one pull request.
- Manual `workflow_dispatch` execution from the repository.
- Read-only access to contents, pull requests, issues, checks and actions.
- Run-summary and seven-day artefact output only.
- Repository-native fake-transport and core validation.

### Live dogfood and close-out

- A qualifying pending report and final report for PR #85 on the same head.
- Manual-versus-assisted comparison.
- Live authority-boundary audit.
- Recorded premature-merge incident and recovery.
- Evidence-based **Adapt** decision.

## Linked issues and pull requests

- [Issue #75](https://github.com/8ft0-ai/IssueOps/issues/75) — planning and capability selection.
- [Issue #76](https://github.com/8ft0-ai/IssueOps/issues/76) / [PR #77](https://github.com/8ft0-ai/IssueOps/pull/77) — formalised roadmap.
- [Issue #78](https://github.com/8ft0-ai/IssueOps/issues/78) / [PR #79](https://github.com/8ft0-ai/IssueOps/pull/79) — deterministic core.
- [Issue #80](https://github.com/8ft0-ai/IssueOps/issues/80) / [PR #81](https://github.com/8ft0-ai/IssueOps/pull/81) — read-only GitHub collection.
- [Issue #82](https://github.com/8ft0-ai/IssueOps/issues/82) / [PR #83](https://github.com/8ft0-ai/IssueOps/pull/83) — initial close-out target and premature merge.
- [Issue #84](https://github.com/8ft0-ai/IssueOps/issues/84) / [PR #85](https://github.com/8ft0-ai/IssueOps/pull/85) — recovery, live dogfood and close-out.

## Proof runs, checks and artefacts

Implementation proof:

- PR #79 evidence workflow run `29144625519` and final-head reruns proved schema, rendering, classifications and non-complete behaviour.
- PR #81 collector run `29145444610` proved collector integration, core compatibility and compilation.
- PR #81 planning run `29145444585` and documentation run `29145444592` passed.

Representative live proof on PR #85 head `0d1d6c1a1ef063b9d422599efa400f5d2a9f1ab2`:

- [Pending collector run `29148889955`](https://github.com/8ft0-ai/IssueOps/actions/runs/29148889955), artefact `evidence-pack-pr-85-29148889955`, ID `8247568476`: report status `incomplete`; documentation workflow and MkDocs job observed `in_progress`.
- [Final collector run `29149028492`](https://github.com/8ft0-ai/IssueOps/actions/runs/29149028492), artefact `evidence-pack-pr-85-29149028492`, ID `8247606971`: report status `complete`; documentation and planning observed successful and Pages deployment observed skipped.
- Both reports retained a stable target head, direct provenance, separated evidence classes, no collection errors and explicit human-decision warnings.
- Live job logs confirmed read-only Actions, Checks, Contents, Issues, Metadata and Pull Requests permissions.

The supporting dogfood detail is retained in `planning/closeout/stage-03-evidence-pack-dogfood.md`.

## Objective validation summary

Stage 3 achieved its stage-level objective: test one bounded automation capability through repository-native proof and reach an evidence-based adopt, adapt or reject decision without weakening IssueOps authority boundaries. It did not prove that the current implementation satisfies every gate required for broader adoption.

| Objective | Strongest evidence | Result |
| --- | --- | --- |
| Generate a structured, current evidence report for one pull request | PR #85 produced deterministic JSON and Markdown reports for the same stable head before and after validation completion | **Achieved** |
| Preserve direct provenance and distinguish assertions from observations | Both reports retained source links and separated contributor-reported content from repository-observed state | **Achieved** |
| Represent incomplete and final validation honestly | The pending run was `incomplete`; the final run was `complete`; the skipped Pages job remained an observation rather than approval advice | **Achieved** |
| Fail closed when evidence is stale, missing or unsafe | Repository-native tests covered moving-head, partial API failure, inaccessible targets, conflicting linkage and bounded pagination | **Achieved** |
| Reduce repetitive evidence assembly | Mechanical collection reduced seven manual source groups to one generated report per snapshot, but human inspection and interpretation remained necessary | **Partially achieved** |
| Preserve human decision and repository authority | Live permissions were read-only, the client used `GET` requests only, and collection produced no repository mutations or approval decisions | **Achieved** |
| Provide a complete execution-contract review view | PR #85's execution-contract issues were omitted because no closing keyword was present; unresolved review-thread state was also absent | **Not fully achieved** |
| Reach an evidence-based adoption decision | The close-out records **Adapt**, with the implementation retained for controlled use and broader adoption deferred pending targeted improvements | **Achieved** |

The **Adapt** decision follows directly from this assessment: the bounded capability is useful and safe enough to retain, but explicit non-closing contract linkage and invocation ergonomics must improve before broader adoption.

## Post-close operational observation

The first ordinary follow-up after Stage 3, [PR #87](https://github.com/8ft0-ai/IssueOps/pull/87), recorded planning and documentation validation directly in its pull-request evidence but did not use a generated collector run or evidence-pack artefact as its primary mechanical evidence source.

This shows that Stage 3 proved technical operation, safety and controlled usefulness, but did not establish routine operational adoption in the normal IssueOps review loop. The observation strengthens rather than changes the **Adapt** decision: operationalisation belongs to a separately shaped future stage and must retain the read-only, human-decision boundary unless new evidence justifies a different authority model.

## Intended versus actual delivery

The implementation remained within the approved read-only boundary and followed the four ordered slices.

Material differences and recovery evidence were:

- unresolved inline review-thread collection was not implemented;
- live issue linkage relied on GitHub closing-keyword syntax;
- PR #85 intentionally omitted closing keywords to avoid another automatic issue closure, so its generated reports did not identify Issue #82 or Issue #84;
- manual dispatch required branch selection and timing coordination;
- the first close-out PR was inadvertently merged while still draft and explicitly not recommended for approval;
- recovery reopened Issue #82 and created Issue #84 and PR #85 rather than reverting an accurate pending worklog.

These differences are recorded as evidence for adaptation, not rewritten into the original plan.

## Observed limitations and friction

- Explicit non-closing execution-contract linkage is absent.
- Unresolved review-thread state is absent.
- The operator must select `main`, provide the PR number and coordinate timing for a pending snapshot.
- Several live attempts were needed to obtain the qualifying pair.
- Artefacts expire after seven days.
- Collection is bounded to configured page and workflow-run limits.
- Generated evidence still requires human interpretation of contract alignment, skipped jobs, risks and sufficiency.
- Draft state and written review recommendations are advisory without enforcing repository controls.

The assisted path reduced mechanical gathering from seven separate source groups to one generated report per snapshot. Report generation took about two to three seconds, but human inspection and substantive interpretation remained required.

## Boundaries preserved

Stage 3 did not introduce:

- automatic or scheduled collection;
- issue readiness or plan approval;
- issue, PR, review, label, branch, commit, file, merge or settings mutation by the collector;
- lifecycle inference or remediation classification;
- approval, merge, deployment or publication recommendations;
- cross-repository rollout;
- broader agent orchestration; or
- Stage 4 implementation.

Human authority over contract satisfaction, risk interpretation, merge, publication and adoption remained intact.

## Decisions and lessons

Decision: **Adapt**.

The bounded collector is retained for controlled use because it safely represented pending and final evidence, reduced repeated transcription, preserved direct provenance and made no repository decisions or mutations.

Broader adoption should wait for separately planned improvements to explicit non-closing issue linkage and invocation ergonomics. The current report is useful evidence assistance, not a complete review view and not a review bot.

The main lessons are:

- collection completeness and approval readiness must remain separate;
- fail-closed provenance and stale-head controls are valuable;
- issue linkage must not depend solely on auto-closing syntax;
- run ergonomics materially affect the usefulness of manual automation; and
- advisory review gates can still be bypassed, so human discipline or separately authorised repository controls remain necessary.

## Implications for the next stage

No next-stage execution work is authorised.

The next planning question is whether broader-use evidence justifies adapting contract linkage and manual invocation while retaining the current read-only, human-decision boundary. Bounded execution triggering, auto-merge, lifecycle automation and repository-setting changes remain outside that question unless new evidence justifies their authority cost.
