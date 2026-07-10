# IssueOps planning

This directory is the management control surface for IssueOps.

It is separate from `docs/` on purpose. Public contributor and operating guidance belongs in `docs/`. Stage planning, delivery reconstruction, close-out evidence and causal delivery records belong in `planning/`.

GitHub issues, pull requests, reviews, commits and workflow runs remain the canonical detailed audit trail. Planning files provide a curated navigation and management layer over that history.

## Start here

```text
planning/README.md        -> operating rules
planning/roadmap/index.md -> intended stage outcomes and boundaries
planning/delivery/index.md -> completed delivery evidence
planning/delivery-log.md  -> concise chronological ledger
```

## Planning versus delivery

```text
planning/roadmap/  -> forward-looking intent, boundaries and acceptance gates
planning/delivery/ -> what actually shipped, what proved it and what was learned
planning/delivery-log.md -> short chronological summary
GitHub history     -> detailed execution and review evidence
```

A roadmap specification must not become the completed delivery narrative. A delivery record must not rewrite what was intended before the work began.

## Stage-pack operating model

Use a stage pack when work:

- spans several dependent execution issues;
- changes autonomy, merge, publication, validation or governance boundaries;
- introduces a cross-cutting operating-model capability;
- requires a real end-to-end proof before adoption; or
- needs an explicit evidence-based close-out decision.

Ordinary bounded documentation, validation and maintenance changes should continue to use normal execution-contract issues without stage-level ceremony.

A stage pack normally consists of:

```text
roadmap specification
  -> parent stage issue
  -> linked execution-contract issues
  -> implementation pull requests
  -> proof evidence
  -> completed delivery record
```

Native GitHub sub-issues are optional. Parent and child relationships may be explicit in issue bodies and planning records.

## Stage lifecycle

Use this status vocabulary:

```text
shaping     -> outcome and boundaries are being defined
approved    -> roadmap reviewed; execution decomposition may begin
delivering  -> approved execution issues are in progress
completed   -> proof and delivery close-out are recorded
superseded  -> replaced by a later approved direction
```

Execution issues should not be created before roadmap approval when the stage changes cross-cutting autonomy or governance boundaries.

## Retrospective records

Historical stages may be reconstructed after delivery, but they must say so explicitly.

A retrospective roadmap record must distinguish:

- documented original intent;
- reasonable retrospective interpretation; and
- verified delivery evidence.

It must not imply that the roadmap or complete issue decomposition existed before the work.

## Close-out

A stage closes when:

- the intended proof boundary is reached or an unresolved finding is accepted;
- linked implementation and proof evidence is recorded;
- a delivery record explains intended versus actual delivery;
- limitations, friction and preserved boundaries are explicit;
- the concise delivery log is updated; and
- the next decision boundary is recorded without creating speculative execution work.

Future delivery-graph metadata may be added only when it explains causality, proof or an enduring boundary more clearly than the Markdown records alone.
