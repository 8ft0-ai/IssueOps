# Modular IssueOps session architecture

Status: completed.

Decision: **Adopt**.

## Original documented intent

The initiative was approved through [issue #113](https://github.com/8ft0-ai/IssueOps/issues/113) and later adapted after the portable-bootstrap proof through [issue #131](https://github.com/8ft0-ai/IssueOps/issues/131).

The exact adapted roadmap immediately before final integration is preserved at commit [`bb3dfdd6e446c59fea1fde3955062993dd404f3d`](https://github.com/8ft0-ai/IssueOps/blob/bb3dfdd6e446c59fea1fde3955062993dd404f3d/planning/roadmap/modular-issueops-session-architecture.md). That roadmap proposed a deliberately small manual architecture:

```text
thin session grant
  -> repository-native state reconciliation
  -> role-specific work
  -> durable handover or evidence record
```

The intended architecture consumed the portable bootstrap, canonical IssueOps protocol and repository-local execution contract rather than repackaging them. The GitHub issue remained the manifest; repository facts were to be discovered from current state; each session received one bounded role; handover claims remained untrusted until verified; and Version 0.1 required manual proof before any automation.

## Retrospective interpretation

Not applicable as a reconstructed roadmap: the initiative used contemporaneous planning and separate execution contracts throughout. This record distinguishes that documented intent from the actual delivery and later evidence-led changes.

The final decision was not a clean first-pass `Adopt`. Pilot evidence first produced an **Adapt** decision. Three bounded corrections were then implemented and exercised before the post-adaptation comparison supported **Adopt**. The completed sequence is therefore:

```text
Adapt
  -> bounded correction and proof
  -> Adopt
  -> completed modular-session baseline
```

That sequence preserves the historical defects that motivated adaptation rather than rewriting them as if adoption had always been the outcome.

## What shipped

The completed baseline consists of the existing manual Version 0.1 guidance plus the accepted bounded adaptation. The normative operational owners remain:

- [`docs/reference/session-grants-roles-and-handovers.md`](../../docs/reference/session-grants-roles-and-handovers.md) for session grants, role invariants, durable handovers and receiving-session verification;
- [`docs/how-to/start-or-resume-bounded-session.md`](../../docs/how-to/start-or-resume-bounded-session.md) for starting and resuming bounded sessions;
- [`docs/reference/review-decisions-and-merge-blockers.md`](../../docs/reference/review-decisions-and-merge-blockers.md) for review and merge-authority boundaries; and
- [`docs/how-to/review-pr-against-contract.md`](../../docs/how-to/review-pr-against-contract.md) for independent review practice.

The accepted adaptation tightened three observed weaknesses without creating a second operational state system:

1. an independent `Review or evaluate` model context terminates for merge purposes after its durable final recommendation; later human approval does not reopen that reviewer context and merge execution occurs elsewhere;
2. human merge authority is durably recorded before merge, tied to the exact pull request, accepted head and accepted review state, and becomes stale after material movement; and
3. a receiving/continuation session explicitly reclassifies superseded action-relevant `Confirmed` observations as `Stale`, while retaining the existing `Confirmed / Stale / Contradicted / Unsupported` vocabulary.

The initiative did **not** add a second kernel, mandatory repository profile, initiative manifest, evidence database, telemetry system, schema, launcher, coordinator, prompt pack or programme-specific workflow/settings change.

## Linked issues and pull requests

Planning and Version 0.1 delivery:

- [#113 — Modular IssueOps session architecture](https://github.com/8ft0-ai/IssueOps/issues/113)
- [#131 — Adapt the modular-session roadmap after portable-bootstrap proof](https://github.com/8ft0-ai/IssueOps/issues/131)
- [#133 — Slice 1 ownership and decomposition](https://github.com/8ft0-ai/IssueOps/issues/133) / [PR #134](https://github.com/8ft0-ai/IssueOps/pull/134)
- [#135 — Slice 2 minimal manual guidance](https://github.com/8ft0-ai/IssueOps/issues/135) / [PR #136](https://github.com/8ft0-ai/IssueOps/pull/136)
- [#137 — Slice 3 role-and-resume pilot programme](https://github.com/8ft0-ai/IssueOps/issues/137)
- [#138 — Pilot A](https://github.com/8ft0-ai/IssueOps/issues/138)
- [#139 — Pilot B](https://github.com/8ft0-ai/IssueOps/issues/139) / [PR #140](https://github.com/8ft0-ai/IssueOps/pull/140)

Comparative decision and bounded adaptation:

- [#142 — Slice 4 comparative close-out](https://github.com/8ft0-ai/IssueOps/issues/142)
- [original Slice 4 `Adapt` recommendation](https://github.com/8ft0-ai/IssueOps/issues/142#issuecomment-5222662829)
- [post-adaptation reassessment — `Adopt`](https://github.com/8ft0-ai/IssueOps/issues/142#issuecomment-5223755907)
- [owner acceptance of `Adopt`](https://github.com/8ft0-ai/IssueOps/issues/142#issuecomment-5223825564)
- [#143 — bounded role/merge-provenance/stale-state adaptation](https://github.com/8ft0-ai/IssueOps/issues/143) / [PR #145](https://github.com/8ft0-ai/IssueOps/pull/145)
- [independent review of PR #145](https://github.com/8ft0-ai/IssueOps/pull/145#pullrequestreview-4887418940)
- [pre-action human merge authority](https://github.com/8ft0-ai/IssueOps/pull/145#issuecomment-5223507689)
- [#143 close-and-reconcile](https://github.com/8ft0-ai/IssueOps/issues/143#issuecomment-5223628197)
- [#146 — baseline integration and close-out](https://github.com/8ft0-ai/IssueOps/issues/146)

Accepted adaptation implementation identity:

```text
accepted PR #145 head: 5db85d00a181c2a86b10ed6b80d8bb7579ee3da0
merge commit:             bb3dfdd6e446c59fea1fde3955062993dd404f3d
```

## Proof runs, checks and artefacts

Pilot A showed that a compact Shape grant could reconstruct authority, select genuine work, avoid duplicate or unauthorised mutation and stop at the owner-decision boundary.

Pilot B showed that one issue, one branch and one PR could deliver a bounded implementation; that a receiving Deliver session could verify rather than trust a handover, recover the earliest incomplete gate and avoid duplicate work; and that validation and post-merge publication remained explicit.

The pilot evidence also contained material negative and incomplete findings. Those findings drove the original Slice 4 **Adapt** recommendation rather than being normalised away.

PR #145 then supplied the representative bounded correction/proof. Independent review [`4887418940`](https://github.com/8ft0-ai/IssueOps/pull/145#pullrequestreview-4887418940) reviewed exact head `5db85d00a181c2a86b10ed6b80d8bb7579ee3da0` and recorded **Approve**, while explicitly terminating that reviewer context for merge purposes. Owner record [`5223507689`](https://github.com/8ft0-ai/IssueOps/pull/145#issuecomment-5223507689) durably authorised merge of that exact state before the merge occurred. The merge commit `bb3dfdd6e446c59fea1fde3955062993dd404f3d` retained the accepted implementation tree, and post-merge documentation run [`31230048021`](https://github.com/8ft0-ai/IssueOps/actions/runs/31230048021) completed successfully on that exact `main` commit.

The post-adaptation reassessment on #142 then recommended **Adopt**, and the owner accepted that recommendation subject to this separately governed integration/close-out.

## Intended versus actual delivery

The architecture retained its intended core shape: compact grants point to durable owners; each receiving session reconstructs current GitHub state; one bounded role performs the authorised work; and transition evidence is durable and independently checked rather than supplied by private chat history.

Actual delivery differed materially from the nominal plan in several ways:

- the initiative first adapted its direction after portable-bootstrap proof, removing the earlier kernel/profile/manifest/launcher concept from the Version 0.1 target;
- the Slice 3 evidence did not support immediate adoption and instead exposed role-boundary, merge-provenance and stale-classification defects;
- the final baseline required one bounded corrective implementation and proof cycle through #143 / PR #145 before adoption;
- the pilot/evaluation execution cost exceeded the nominal design; and
- some evidence remained unavailable or only procedurally observable and was retained as such.

The completed baseline therefore represents **Adopt after adaptation**, not a claim that every original target was proved cleanly on the first attempt.

## Observed limitations and friction

The following material evidence remains part of the completed record:

- **Historical B3 reviewer-context-to-merge failure.** Pilot B's independent review was substantively valid, but the same conversation context later invoked merge after human approval instead of terminating at the `Review or evaluate` boundary. The adapted guidance and PR #145 lifecycle corrected the pre-adoption blocker; the historical failure remains negative evidence.
- **Original merge-authority provenance weakness.** Pilot B had explicit human authority according to retained first-party evidence, but that decision was not durably posted to GitHub before merge. PR #145 later exercised the corrected pre-action durable authority boundary; the earlier weakness remains historical evidence.
- **Earlier stale-state classification imprecision.** A Pilot B continuation used current evidence correctly but did not explicitly reclassify superseded observations as `Stale`. The adaptation added that precision and PR #145 naturally exercised it.
- **Initial receiving-boundary mismatch cases remain not fully proved.** `Stale`, `Contradicted` and `Unsupported` at the initial receiving boundary were not all naturally exercised. They are **not proved**, not silently converted into passes.
- **Fresh-session/model-context separation remains procedural evidence.** GitHub can establish separate grants, roles, durable records and observable action ordering; it cannot cryptographically establish absence of inaccessible prior conversational context.
- **Pilot B process cost was material.** **Two validation-blocked stops occurred** because the connector could not directly dispatch the required workflow. Those interruptions required **one manual workflow-dispatch intervention** and **one additional fresh Deliver continuation**. This contributed to **seven actual model sessions versus the nominal six-session design**, excluding readiness, detailed planning and pre-execution gates from that nominal comparison.
- The extra pilot/evaluation and remediation ceremony is historical process-cost evidence. It must not automatically become mandatory steady-state policy where the same safety/evidence outcome can be achieved more proportionately.
- The connector workflow-dispatch limitation is not solved by this initiative. The narrow execution-bridge design remains separately governed by [#141](https://github.com/8ft0-ai/IssueOps/issues/141), with implementation issue [#144](https://github.com/8ft0-ai/IssueOps/issues/144) independently gated.

These findings are not reinterpreted as failures of the corrected adopted baseline. They explain why adaptation was required, what remains unproved and where process cost should inform later simplification.

## Boundaries preserved

The completed initiative preserves:

- the portable bootstrap as the owner of external assessment and first-local-issue handoff;
- the canonical IssueOps protocol and repository-local issue as the owners of execution authority;
- one primary role per session and explicit stop boundaries;
- current GitHub state over handover claims or private chat context;
- exact-head validation and honest pending/unavailable states;
- independent review as a separate recommendation boundary;
- durable human merge authority as a later, exact-state decision boundary;
- human merge and publication authority unless separately delegated;
- no automatic lifecycle transition or auto-merge authority;
- no second operational state system, evidence database or telemetry store; and
- no requirement for a schema, launcher, prompt pack, coordinator or programme-specific workflow.

Issue [#90](https://github.com/8ft0-ai/IssueOps/issues/90) remains the owner of the broader Stage 5 operational-evidence-assistance question and any later Stage 5 adoption decision. Issue [#141](https://github.com/8ft0-ai/IssueOps/issues/141) remains the design authority for the connector-triggered execution bridge, and [#144](https://github.com/8ft0-ai/IssueOps/issues/144) remains its separately governed bounded implementation issue. None is a prerequisite for the adopted modular-session baseline, and this close-out does not implement, absorb, supersede or grant authority to any of them.

## Decisions and lessons

Decision: **Adopt** the corrected manual modular-session architecture into the recommended IssueOps operating baseline.

The evidence supports adoption because the corrected architecture preserves repository-native authority, bounded roles, independent state reconstruction, exact validation and explicit human decision boundaries without requiring a parallel state or orchestration system. The bounded adaptation removed the material pre-adoption regressions observed in Pilot B, and PR #145 supplied representative durable proof of the corrected reviewer stop, exact-state human merge authority and explicit stale-state reclassification.

Lessons that carry forward:

- thin invocation works only when durable GitHub owners remain authoritative;
- a handover is a navigation and transition record, not trusted state;
- role boundaries need observable stop behaviour, not only descriptive wording;
- human authority should be durable and bound to exact current state before the protected action;
- later state movement should be explicitly reclassified rather than silently overwritten;
- unavailable or unexercised evidence is useful when represented honestly;
- connector limitations can create material ceremony without being defects in the architecture itself;
- experimental controls should not become steady-state requirements without evidence that they remain necessary; and
- the absence of a second state system, schema, launcher, telemetry layer or prompt pack is a positive proportionality result rather than missing implementation.

## Implications for the next stage

This initiative is complete. Completion does not start Stage 5, a connector bridge, another modular-session slice or cross-repository rollout.

The next decisions remain separately governed:

- [#90](https://github.com/8ft0-ai/IssueOps/issues/90) may continue shaping whether operational evidence assistance should become a later Stage 5 capability;
- [#141](https://github.com/8ft0-ai/IssueOps/issues/141) and [#144](https://github.com/8ft0-ai/IssueOps/issues/144) govern the narrow connector-triggered evidence-collection bridge independently; and
- any future templates, schema, launcher, coordinator or automation for modular sessions requires new evidence and its own authority rather than inheriting permission from this **Adopt** decision.
