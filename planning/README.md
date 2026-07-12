# IssueOps planning

This directory is the management control surface for IssueOps.

It is separate from `docs/` on purpose. Public contributor and operating guidance belongs in `docs/`. Stage planning, delivery reconstruction, close-out evidence, historical project evidence and causal delivery records belong in `planning/`.

GitHub issues, pull requests, reviews, commits and workflow runs remain the canonical detailed audit trail. Planning files provide a curated navigation and management layer over that history.

## Start here

```text
planning/README.md                 -> operating rules
planning/roadmap/index.md          -> intended stage outcomes and boundaries
planning/delivery/index.md         -> completed delivery evidence
planning/evidence/index.md         -> historical snapshots and compatibility decisions
planning/delivery-log.md           -> concise chronological ledger
planning/delivery/graph.md         -> generated causal navigation
```

## Planning, delivery and evidence

```text
planning/roadmap/                  -> forward-looking intent, boundaries and acceptance gates
planning/delivery/*.md             -> what actually shipped, what proved it and what was learned
planning/evidence/                 -> curated links to immutable historical project records
planning/delivery-log.md           -> short chronological summary
planning/delivery/delivery.yaml    -> compact causal graph metadata
planning/delivery/graph.md         -> generated Mermaid navigation
GitHub history                     -> exact source records and detailed execution evidence
```

A roadmap specification must not become the completed delivery narrative. A delivery record must not rewrite what was intended before the work began. A historical evidence index must link immutable records rather than copying them into current user guidance.

See the [historical evidence index](evidence/index.md) for former roadmap, release, contributor-review and delivery-history pages whose public `docs/` paths are retained only as compatibility surfaces.

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

## Adoption decision

The planning model is adopted for future multi-issue stages.

The adoption applies proportionately. A stage pack is the default only when work crosses issue boundaries, changes authority or governance, requires an end-to-end proof, or needs an explicit close-out decision. It is not a mandatory wrapper for ordinary bounded work.

The adopted model keeps five questions separate:

```text
What did we intend?       -> roadmap record
What actually shipped?    -> delivery record
What proved it?           -> linked GitHub and workflow evidence
What exact history remains? -> immutable record linked from planning/evidence
Why did that lead onward? -> compact delivery graph
```

See [the planning-process adoption record](delivery/planning-process-adoption.md) for the evidence, limitations and final decision.

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

## Delivery graph

The delivery graph explains why one stage led to the next, what provided the strongest proof, which artefacts became dependencies and which boundaries carried forward.

It is not an issue or pull-request inventory. Add a node only when it explains direction, proof, an enduring boundary, a produced dependency or a future decision point.

Update the graph when an item:

- explains why delivery changed direction;
- is the strongest proof for a stage or increment;
- becomes a dependency for future work;
- preserves an enduring authority or governance boundary; or
- creates the next decision point.

Routine issues, pull requests and CI runs remain in the delivery record and GitHub history.

When `planning/delivery/delivery.yaml` changes:

```bash
python scripts/validate_delivery_graph.py
python scripts/render_delivery_graph.py
python scripts/render_delivery_graph.py --check
```

Commit the regenerated `planning/delivery/graph.md` in the same pull request.

## Close-out

A stage closes when:

- the intended proof boundary is reached or an unresolved finding is accepted;
- linked implementation and proof evidence is recorded;
- a delivery record explains intended versus actual delivery;
- limitations, friction and preserved boundaries are explicit;
- the concise delivery log is updated; and
- the next decision boundary is recorded without creating speculative execution work.

Update the delivery graph only when close-out changes the causal delivery story. Routine activity belongs in the Markdown record and GitHub history, not as graph nodes.
