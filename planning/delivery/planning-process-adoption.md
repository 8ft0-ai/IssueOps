# Planning-process adoption

Status: completed.

## Original documented intent

[Issue #63](https://github.com/8ft0-ai/IssueOps/issues/63) proposed adopting the underlying CryptoPulse planning model in IssueOps while preserving Stage terminology, public documentation boundaries and the proportional manual operating model.

The intended increment was to:

- create a separate top-level planning control surface;
- add reusable roadmap and delivery templates;
- reconstruct Stage 1 and Stage 2 honestly;
- add compact structural validation;
- add a causal delivery graph; and
- decide whether the model should govern future multi-issue stages.

## Retrospective interpretation

Not applicable to the adoption increment itself. This increment was managed contemporaneously through parent issue #63 and child issues #64 through #68.

The Stage 1 and Stage 2 records produced by the increment are retrospective reconstructions and are labelled separately as such.

## What shipped

The adoption increment delivered:

- `planning/README.md` as the management operating model;
- separate roadmap and delivery indexes;
- reusable stage-roadmap and delivery-record templates;
- a concise chronological delivery ledger;
- deterministic planning validation and focused tests;
- a read-only planning-validation workflow;
- an honest retrospective Stage 1 roadmap and delivery record;
- an honest retrospective Stage 2 roadmap and delivery record;
- compact delivery-graph modelling rules;
- validated `delivery-graph/v1` metadata;
- a stable Mermaid renderer and freshness check; and
- a generated causal graph covering Stage 1, Stage 2, enduring boundaries and the Stage 3 decision point.

## Linked issues and pull requests

- [Issue #63 — adoption parent](https://github.com/8ft0-ai/IssueOps/issues/63)
- [Issue #64](https://github.com/8ft0-ai/IssueOps/issues/64) / [PR #70](https://github.com/8ft0-ai/IssueOps/pull/70) — planning control surface, templates and validation.
- [Issue #65](https://github.com/8ft0-ai/IssueOps/issues/65) / [PR #71](https://github.com/8ft0-ai/IssueOps/pull/71) — Stage 1 reconstruction.
- [Issue #66](https://github.com/8ft0-ai/IssueOps/issues/66) / [PR #72](https://github.com/8ft0-ai/IssueOps/pull/72) — Stage 2 reconstruction.
- [Issue #67](https://github.com/8ft0-ai/IssueOps/issues/67) / [PR #73](https://github.com/8ft0-ai/IssueOps/pull/73) — compact structured delivery graph.
- [Issue #68](https://github.com/8ft0-ai/IssueOps/issues/68) — adoption proof and close-out.

## Proof runs, checks and artefacts

Representative repository-native evidence:

- PR #70: planning workflow run `29089546831` and MkDocs run `29089546800`.
- PR #71: planning workflow run `29089673694` and MkDocs run `29089673680`.
- PR #72: planning workflow run `29089885033` and MkDocs run `29089885025`.
- PR #73: planning workflow run `29090083905` and MkDocs run `29090083894`.

The final PR #73 proved:

- all planning tests passed;
- all seven graph-validator tests passed;
- all three renderer tests passed;
- the full planning tree passed validation;
- graph metadata passed schema and reference validation;
- generated `graph.md` matched the renderer exactly; and
- the strict MkDocs build and Pages artefact upload remained valid.

## Intended versus actual delivery

The adopted model kept the main CryptoPulse distinction between forward-looking roadmap intent and retrospective delivery evidence, but it was adapted for IssueOps:

- Phase terminology became existing Stage terminology.
- Public `docs/` remained separate from management `planning/`.
- GitHub remained the canonical detailed audit trail.
- Small bounded work remained outside mandatory stage ceremony.
- Historical stages were reconstructed with explicit uncertainty rather than rewritten as contemporaneous plans.
- The delivery graph was kept macro-level rather than representing every Stage 2.x issue.
- `delivery.yaml` uses JSON-compatible YAML so validation and rendering remain standard-library only.
- No interactive graph, live GitHub-state validation or separate planning platform was introduced.

No Stage 3 shaping issue was created during adoption. The evidence-based next question is recorded, but implementation remains deliberately unstarted.

## Observed limitations and friction

- A stage pack introduces several maintained artefacts: roadmap, delivery record, indexes, ledger and sometimes graph metadata.
- Retrospective reconstruction requires careful evidence selection and explicit uncertainty; it is not a cheap formatting exercise.
- The connected GitHub identity cannot formally approve its own pull requests, so independent review findings are recorded in PR comments before owner-authorised merge.
- Graph freshness adds a maintenance step when the causal delivery story changes.
- Structural validation can prove shape and references, not the substantive truth of historical interpretation.
- The approach would be excessive for ordinary single-issue documentation or maintenance work.

## Boundaries preserved

The adoption increment did not introduce:

- automatic agent execution;
- automatic issue or PR creation;
- automatic lifecycle transitions;
- required status checks or branch protection;
- automatic review or thread resolution;
- GitHub auto-merge;
- autonomous publication decisions;
- Stage 3 execution issues; or
- a replacement for GitHub history.

Public contributor guidance remains under `docs/`. Planning records do not authorise repository mutations by themselves.

## Decisions and lessons

Decision: adopt the model as implemented for future multi-issue stages.

Use a stage pack when work:

- spans several dependent execution issues;
- changes autonomy, merge, publication, validation or governance boundaries;
- introduces a cross-cutting operating-model capability;
- requires real end-to-end proof before adoption; or
- needs an explicit evidence-based close-out decision.

Do not use a stage pack for ordinary bounded documentation, validation or maintenance issues.

Update the delivery graph only when an item explains why delivery changed direction, provides the strongest stage proof, becomes a future dependency, preserves an enduring boundary or creates the next decision point. Routine issues, PRs and CI runs belong in the delivery record and GitHub history.

The cleanest benefit was not additional documentation. It was separating four different questions that had previously been entangled:

```text
What did we intend?
What actually shipped?
What proved it?
Why did that lead to the next stage?
```

## Implications for the next stage

Stage 3 should begin with one shaping issue and an approved roadmap, not an execution backlog.

The shaping question should be grounded in Stage 2 friction: which single bounded automation can reduce manual effort without weakening issue-contract authority, safe actuation, evidence quality, human contract verification, merge authority or publication boundaries?

Execution-contract issues should be created only after the Stage 3 roadmap is reviewed and approved.
