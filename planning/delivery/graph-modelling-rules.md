# Delivery graph modelling rules

Status: active guidance.

## Purpose

The delivery graph explains causality and proof. It is a compact navigation layer over IssueOps delivery history, not a complete inventory of every issue, pull request, commit or workflow run.

```text
GitHub history                    -> what exactly happened
planning/delivery/*.md            -> what shipped and what proved it
planning/delivery/delivery.yaml   -> compact causal metadata
planning/delivery/graph.md        -> generated visual navigation
```

## Add a node only when it matters

Model a node when it materially explains:

- why the operating model changed direction;
- the strongest proof for a stage;
- an enduring autonomy or governance boundary;
- a produced artefact that later work depends on;
- a problem or lesson that motivated the next stage; or
- the decision boundary that future planning must resolve.

Good nodes answer one of these questions:

```text
Why did this happen next?
What proved the stage worked?
What artefact became a dependency?
What boundary remained intact?
What lesson carried forward?
```

## Do not model routine activity

Do not add nodes for:

- every Stage 1.x or Stage 2.x issue;
- every documentation pull request;
- every successful CI run;
- repeated evidence when one representative proof is enough;
- incidental navigation or wording cleanup;
- abandoned exploration with no carry-forward lesson; or
- public generated-site output as if it were committed source.

The Markdown delivery records and GitHub history retain the detail.

## Representative-proof rule

Prefer one representative issue, pull request, workflow run or release artefact for each major proof claim.

For example, Stage 2 has many successful documentation builds, but the graph needs only the repository-native validation proof that explains the corrected PR-versus-production lifecycle boundary.

## Boundary rule

Include a boundary node only when it is enduring and changes how future work may proceed. Examples include:

- human merge authority;
- no automatic agent execution in the current baseline; and
- Stage 3 execution work requiring an approved roadmap first.

Do not add a separate node for every repeated non-goal.

## Stage close-out rule

When a stage closes, update the graph only if the close-out changes the causal delivery story.

A close-out should normally preserve a small shape:

```text
stage
  -> strongest proof
  -> key lesson or produced dependency
  -> next decision boundary
```

## Generated output rule

`planning/delivery/graph.md` is generated from `planning/delivery/delivery.yaml` and must be regenerated in the same pull request whenever the metadata changes.

The graph renderer must produce stable ordering so repeated runs do not create noisy diffs.

## Validation boundary

The validator checks schema, references, vocabularies, required fields, local artefact paths and renderer freshness. It does not verify live GitHub state or decide whether an evidence claim is substantively true.
