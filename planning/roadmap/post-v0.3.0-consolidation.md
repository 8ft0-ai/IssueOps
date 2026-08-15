# Post-v0.3.0 consolidation, proportionality and operational hardening

Status: approved.

Record type: contemporaneous.

Approved through [planning issue #197](https://github.com/8ft0-ai/IssueOps/issues/197) on 15 August 2026.

This is an unnumbered consolidation initiative after the `v0.3.0` stable baseline. It is deliberately **not Stage 6** and does not assume that IssueOps needs more features.

The active tracking/evaluation records are:

- [#198 — Evaluate minimum mechanical safeguards for IssueOps repository mutations](https://github.com/8ft0-ai/IssueOps/issues/198)
- [#199 — Measure IssueOps operating cost and evaluate lifecycle proportionality](https://github.com/8ft0-ai/IssueOps/issues/199)
- [#200 — Evaluate IssueOps portability across independent repository contexts](https://github.com/8ft0-ai/IssueOps/issues/200)
- [#201 — Assess post-v0.3.0 consolidation evidence and decide Maintain / Adapt / New shaping question](https://github.com/8ft0-ai/IssueOps/issues/201)

Creating or listing those issues does not itself authorise their substantive evaluation sessions or any implementation that might later be recommended.

## Problem statement

`v0.3.0` is a coherent stable operating baseline. The post-baseline review nevertheless identified three areas where more evidence would materially improve confidence in the operating model:

1. **Mechanical enforcement versus procedural control.** The authority and evidence rules are strong, but many are procedural. The project needs to determine whether small deterministic safeguards or gate-progress rules would prevent meaningful mistakes and avoid unnecessary human ceremony without turning IssueOps into an automated judgement or authority system.
2. **Process cost and proportionality.** Prior modular-session evidence recorded real session, decision and intervention cost. The project needs to measure where that cost is incurred and which gates actually produce safety/review value before proposing any shorter path.
3. **Portability breadth.** Portable bootstrap/adoption is adopted and has a genuine Level 3 external proof, but one target repository does not establish broad generalisability across different engineering contexts or independent operators.

Previously deferred/adapted ideas around mechanical review preflight, drift detection and operator-tool expansion must not be reopened merely because this initiative exists. They may be reconsidered only if fresh deterministic recurrence demonstrates a concrete residual gap.

The governing question is:

> What, if anything, should IssueOps change after `v0.3.0` to improve safeguards, reduce unnecessary operating cost and strengthen portability evidence without weakening the human-governed execution contract?

## Outcome to prove

Produce enough durable evidence to make one defensible end-of-initiative decision:

- **Maintain** the current `v0.3.0` operating model;
- **Adapt** it through one or more narrowly evidenced corrections; or
- open a **New shaping question** only where the evidence demonstrates a genuinely new capability or stage-level problem that should not be hidden inside maintenance work.

`Maintain` is an explicitly successful outcome. The initiative is not required to produce implementation work.

If the final decision is `Adapt`, implementation must move to the minimum separately governed issue or issues justified by the evidence. If the final decision is `New shaping question`, stop at the question and require a new owner decision before roadmap or implementation work begins.

### Stable kernel to preserve

Treat these as presumptive operating-model invariants during the evaluations:

1. bounded issue contract;
2. current-state reconciliation;
3. explicit proposed implementation path;
4. durable human implementation authority where required;
5. bounded candidate implementation;
6. exact-candidate validation and evidence;
7. substantive contract review; and
8. separate human merge authority.

The mechanical-safeguard and proportionality work may test whether deterministic gates, low-risk transitions, presentation or session boundaries can be collapsed. They must not silently erase these distinctions or convert evidence automation into judgement/authority automation.

## Non-goals

This initiative does not authorise:

- a shared `issueops` CLI, package or framework;
- implementation of #182 as a standalone mechanical review-preflight tool;
- implementation of #184 as a standalone baseline/documentation drift command;
- a new programme-state manifest created to make checking easy;
- implementation of automatic gate progression before #198 produces evidence and a separately governed implementation contract exists;
- automatic human judgement or authority decisions, including intent/scope choice, material risk/deviation acceptance, judgement-bearing plan approval, substantive approval, merge or human-governed release/publication decisions;
- lifecycle progression where the gate is not fully deterministic, current, unambiguous, fail-closed and already covered by existing authority;
- generic workflow, ref, input, command or shell execution;
- broader PR-comment command-router scope;
- auto-merge or automated release publication;
- ruleset, branch-protection or required-check changes without separate evidence-backed implementation authority;
- workflow changes merely because a possible safeguard can be imagined;
- speculative expansion of the primary-record inspector or static workflow auditor;
- broadening the workflow auditor's handwritten YAML recogniser until it becomes an accidental general YAML parser;
- an external-repository rollout programme;
- replacement of target-local conventions for IssueOps naming symmetry;
- claiming human usability evidence from agent-only walkthroughs; or
- rerunning completed experiments merely to obtain cleaner or more favourable evidence.

The initiative does not alter the published `v0.3.0` compatibility boundary merely by existing.

## Operating and autonomy boundary

The initiative is evidence-led and issue-driven:

```text
approved consolidation roadmap
  -> bounded evaluation contracts
  -> durable evidence and limitations
  -> final comparison
  -> human decision
  -> separate implementation only when justified
```

The roadmap authorises creation and tracking of the bounded evaluation issues. Each substantive evaluation still requires repository-standard readiness, a detailed evaluation plan and separate owner execution authority under the current protocol.

#198 may evaluate whether some of those existing gates should later be mechanically satisfied or progressed when the condition is deterministic and no new human judgement or authority is introduced. That evaluation does not itself change the current protocol or authorise such progression.

A child recommendation is not implementation authority.

External pilot mutation is additionally governed by the target repository. No IssueOps parent or child issue transfers authority into another repository. Each target pilot must identify the exact repository, stable branch/base, local governing record, local instructions, validation/merge conventions and explicit human permission before the first target mutation.

The final comparison issue is decision-only and cannot implement its own recommendation.

## Target workflow or target state

The intended programme flow is:

```text
roadmap formalisation
  -> #198 mechanical-safeguards / deterministic-gate evaluation
  -> #199 process-cost/proportionality evaluation
  -> #200 portability-breadth evaluation
  -> #201 final consolidation comparison
  -> Maintain / Adapt / New shaping question
```

#198 and #199 may proceed independently after their own gates.

#200 may be shaped and planned before #199 completes, but real pilot execution should reuse #199's measurement model where practical so portability work does not invent a competing cost/yield scorecard.

#201 remains blocked on sufficiently complete durable evidence from #198–#200.

### Workstream 1 target — minimum mechanical safeguards and deterministic gate progression

#198 evaluates the minimum useful mechanical safeguard and deterministic gate-progression model, if any, for IssueOps after `v0.3.0`.

It must reconstruct representative ordinary PR changes, exceptional/direct-main changes and relevant execution deviations, then compare at least these repository-mutation safeguards:

1. no mechanical change;
2. baseline validation on pushes to `main`;
3. ordinary-change PR enforcement with an explicit exceptional owner path;
4. selective deterministic required checks; and
5. a smaller combination if evidence supports one.

For every candidate safeguard, assess observed preventable/detectable failures, existing human-control effectiveness, blocking/false-positive cost, exception auditability and whether the safeguard is deterministic rather than a disguised approval judgement.

It must also assess whether unsigned Git-data commits materially weaken provenance for authorised exceptional direct-main changes or whether verified ancestry plus durable owner authority is sufficient.

The workstream must additionally classify lifecycle gates into:

- **candidate mechanical gates** — current evidence can prove the condition unambiguously, the next action is already authorised and progressing the gate creates no new human choice, risk acceptance or authority grant;
- **human-decision gates** — intent/scope choice, material risk/deviation acceptance, judgement-bearing plan approval, substantive contract review, authority-expanding exceptions, merge and human-governed release/publication decisions; or
- **not safely classifiable** — evidence or semantics are too ambiguous to automate safely.

At minimum, test whether readiness conditions, exact-candidate validation, evidence-currentness/preflight and other already-authorised deterministic transitions can be auto-satisfied or auto-progressed. A plan transition may be considered only when it is a mechanical instantiation of already-approved intent and introduces no new trade-off, risk or authority decision.

Any proposed automatic gate must define:

```text
exact proof facts
stale/ambiguous conditions
fail-closed behaviour
whether progression introduces new authority
how the automated result is durably evidenced
```

Green CI or complete mechanical evidence must never be treated as a substitute for a human-decision gate.

### Workstream 2 target — process cost and proportionality

#199 reconstructs approximately 20–30 completed changes where durable evidence is sufficient, spanning different risk/change types where available.

For each sampled change, record where reconstructable:

- change/risk type;
- issues and durable planning records;
- human decisions;
- model/session transitions;
- branches and pull requests;
- blocked stops;
- manual interventions;
- validation executions/reruns;
- review and scope-drift findings;
- stale-state detections;
- execution deviations;
- duplicate work prevented;
- post-merge defects or follow-up repairs; and
- elapsed time only where timestamps support a meaningful comparison.

For each gate or transition, assess separately:

```text
Cost  = interaction/session/human-attention/delay burden
Yield = meaningful risk, defect, stale state, authority or scope problem caught
```

The analysis may classify controls conceptually as:

```text
high value / low cost   -> retain
high value / high cost  -> optimise
low value / low cost    -> low priority
low value / high cost   -> strongest simplification candidate
```

This classification is analytical, not an automatic policy decision.

### Workstream 3 target — portability breadth

#200 does not rerun the already adopted `mri-fourier-lab` proof. It evaluates breadth and generalisability.

Shape up to three bounded proof properties, each with separately governed target authority before external mutation:

- **ordinary service/application context** — real code, CI, tests and ordinary maintenance;
- **concurrent-contributor context** — moving issue/branch/PR state that tests reconciliation; and
- **independent operator context** — an operator/maintainer who did not design IssueOps.

These properties may be combined in fewer repositories only when evidence remains distinguishable and reviewable.

Reuse #199's cost/yield model where available and additionally record target controls, adoption posture, setup decisions, conventions preserved/adapted, IssueOps-specific artefacts, ambiguous/misunderstood guidance, assistance required from an IssueOps author/designer, unsafe/duplicate actions avoided, fresh-session reconstruction quality, first-change versus second-change friction, human interventions, deviations and exact evidence level.

The strongest desired evidence is that a competent engineer unfamiliar with IssueOps can discover target-local authority, perform a genuine bounded change, generate sufficient evidence, stop at the correct human decision boundaries and resume later without the framework author filling undocumented gaps.

### Recurrence-triggered watchpoints

No scheduled implementation work is created for these areas:

- **#182 mechanical review preflight:** retain the existing defer/absorb disposition unless fresh evidence shows a repeated deterministic mechanical-currentness gap in the inspector/evidence path.
- **#184 baseline/documentation drift:** retain the no-standalone-command disposition unless a fresh contradiction has a clear canonical owner and deterministic low-false-positive assertion. Prefer an existing validator before a new command/manifest.
- **Operator-tool expansion:** keep the inspector and workflow auditor optional/advisory. If a future auditor requirement needs materially broader YAML semantics, reassess a standard parser rather than growing the bounded handwritten recogniser into a general parser.

## Acceptance gates

### Governance and scope

- [ ] The initiative remains an unnumbered consolidation programme rather than becoming Stage 6 by implication.
- [ ] Child issue creation is not treated as execution authority.
- [ ] #198–#201 each pass their own required gates before substantive work under the current protocol.
- [ ] #198 may evaluate deterministic automatic gate progression without treating that evaluation as present authority to use it.
- [ ] No child recommendation becomes implementation authority automatically.
- [ ] `v0.3.0` remains the stable baseline unless a later separately governed release decision changes it.

### Mechanical-safeguard evidence

- [ ] #198 compares candidate controls against observed failure/prevention evidence and blocking cost.
- [ ] Procedural versus mechanical enforcement is distinguished explicitly.
- [ ] Lifecycle gates are classified as mechanical, human-decision or not safely classifiable.
- [ ] Any candidate automatic gate has exact proof facts, stale/ambiguity handling, fail-closed behaviour and durable evidence.
- [ ] Automatic progression is considered only where the next action is already authorised and no new human judgement, risk acceptance or authority grant is introduced.
- [ ] Substantive review, judgement-bearing plan approval, material-risk/deviation acceptance, authority expansion, merge and human-governed release/publication remain human-decision gates.
- [ ] Any recommended safeguard or progression rule remains deterministic and bounded.
- [ ] Settings/workflow/protocol/lifecycle implementation is deferred to a separate issue if recommended.

### Proportionality evidence

- [ ] #199 reconstructs a representative sample without inventing unavailable data.
- [ ] Gate cost and gate yield are assessed separately.
- [ ] The stable kernel is preserved during analysis.
- [ ] Any shorter-path proposal is treated as a later proof hypothesis, not immediate policy.

### Portability evidence

- [ ] #200 uses materially different repository/operator contexts or explains why combined proof remains adequate.
- [ ] Every external mutation has exact target-local authority.
- [ ] Existing target conventions are preserved/adapted before adding IssueOps surfaces.
- [ ] Human usability evidence is labelled separately from agent-only evidence.
- [ ] #199's measurement model is reused where practical.

### Recurrence discipline

- [ ] #182 is not reopened without a demonstrated residual mechanical-preflight gap.
- [ ] #184 is not reopened without a fresh deterministic contradiction.
- [ ] Operator tooling is not expanded without a concrete need.
- [ ] No new central state manifest is introduced merely to support checking.

### Final decision

- [ ] #201 uses completed/current workstream records rather than stale summaries.
- [ ] Negative, unavailable and inconclusive evidence remains explicit.
- [ ] The final decision is exactly Maintain / Adapt / New shaping question.
- [ ] Any implementation implied by Adapt is deferred to separately governed issues.
- [ ] Any New shaping question stops for fresh owner direction before roadmap/implementation work.

## Proposed implementation slices

The initiative uses four bounded issue records rather than one broad execution issue.

### Slice 1 — mechanical safeguards and deterministic gate progression

Issue: [#198](https://github.com/8ft0-ai/IssueOps/issues/198)

Required output:

- **Maintain procedural controls**;
- **Adopt one bounded mechanical safeguard / deterministic gate-progression rule**;
- **Adapt through a small combination of safeguards and deterministic progression rules**; or
- **Collect more evidence**.

No safeguard or automatic gate progression is implemented inside #198.

### Slice 2 — lifecycle proportionality

Issue: [#199](https://github.com/8ft0-ai/IssueOps/issues/199)

Required output:

- **Retain the current uniform lifecycle**;
- **Adapt presentation/session structure only**;
- **Shape one explicit risk-proportionate path for later controlled proof**; or
- **Collect more evidence**.

A proposed shorter path is a hypothesis for later proof, not a policy change inside #199.

### Slice 3 — portability breadth

Issue: [#200](https://github.com/8ft0-ai/IssueOps/issues/200)

Required output:

- **Portability evidence sufficient**;
- **Adapt bootstrap/guidance through separately governed work**; or
- **More breadth required**.

No external pilot begins without separately recorded target-local authority.

### Slice 4 — final consolidation decision

Issue: [#201](https://github.com/8ft0-ai/IssueOps/issues/201)

The final comparison begins only when #198–#200 contain sufficiently complete durable evidence. It must answer:

1. Does the stable operating model remain sound?
2. Is any current control materially under-enforced?
3. Is lifecycle ceremony materially disproportionate for one or more classes of work?
4. Has portability been demonstrated broadly enough for current claims?
5. Did any repeated deterministic failure mode justify a validator or bounded safeguard?
6. Is there evidence for a concrete implementation change, or only hypotheses?

The final recommendation is exactly one of:

- **Maintain**;
- **Adapt**; or
- **New shaping question**.

#201 may identify the minimum next action but cannot implement it.

## Risks and controls

### Risk: consolidation becomes feature expansion

Control: `Maintain` is a successful result, the active children are evaluations rather than implementations and speculative tooling/automation work is prohibited.

### Risk: mechanical enforcement crowds out human judgement

Control: #198 explicitly distinguishes deterministic evidence/progression from judgement and authority. Any automatic gate must be current, unambiguous, fail-closed and already authorised; substantive review, material-risk acceptance, authority expansion, merge and human-governed publication remain human decisions.

### Risk: proportionality work becomes a pretext to remove safety gates

Control: #199 starts from the stable kernel, measures cost and yield separately and requires later controlled proof for any shorter path.

### Risk: portability pilots create remote authority

Control: every target repository retains local authority and must separately authorise each mutation boundary.

### Risk: unavailable historical evidence is normalised into precise metrics

Control: missing or qualitative data remains missing/qualitative and is carried into the final decision as a limitation.

### Risk: old deferred ideas are silently revived

Control: #182/#184/operator-tool changes are watchpoints only and require fresh recurrence evidence plus separate authority.

### Risk: final comparison implements its own recommendation

Control: #201 is decision-only; implementation or a new roadmap requires a later separately governed record.

## Definition of done

The initiative is complete when:

- [ ] this roadmap is approved, merged and indexed;
- [ ] #198 has a durable mechanical-safeguards / deterministic-gate conclusion;
- [ ] #199 has a durable cost/proportionality conclusion and reusable measurement model;
- [ ] #200 has a durable portability-breadth conclusion with exact evidence levels and target authority provenance;
- [ ] recurrence-triggered watchpoints are assessed without speculative implementation;
- [ ] #201 records the final Maintain / Adapt / New shaping question recommendation;
- [ ] the owner accepts, rejects or amends that final recommendation;
- [ ] any required implementation is moved to separately governed issues rather than absorbed into the comparison record;
- [ ] actual delivery/evidence is recorded separately from this intent roadmap; and
- [ ] the next decision boundary is explicit without automatically creating Stage 6.

## Likely next decision boundary

After #201, the repository owner should be able to answer one narrow question:

> Does the evidence support leaving `v0.3.0` as the operating model, making one or more narrowly justified compatible adaptations, or shaping a genuinely new problem separately?

No later stage, release, automation capability or repository-control change is implied by completion of this initiative alone.
