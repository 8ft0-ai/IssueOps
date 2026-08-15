# Post-v0.3.0 consolidation, proportionality and operational hardening

Status: approved.

Record type: contemporaneous.

Approved through [planning issue #197](https://github.com/8ft0-ai/IssueOps/issues/197) on 15 August 2026.

This is an unnumbered consolidation initiative after the `v0.3.0` stable baseline. It is deliberately **not Stage 6** and does not assume that IssueOps needs more features. Its purpose is to test whether any concrete adaptation is justified by evidence after the stable baseline was consolidated.

The active delivery/evaluation records are:

- [#198 — Evaluate minimum mechanical safeguards for IssueOps repository mutations](https://github.com/8ft0-ai/IssueOps/issues/198)
- [#199 — Measure IssueOps operating cost and evaluate lifecycle proportionality](https://github.com/8ft0-ai/IssueOps/issues/199)
- [#200 — Evaluate IssueOps portability across independent repository contexts](https://github.com/8ft0-ai/IssueOps/issues/200)
- [#201 — Assess post-v0.3.0 consolidation evidence and decide Maintain / Adapt / New shaping question](https://github.com/8ft0-ai/IssueOps/issues/201)

Creating or listing those issues does not itself authorise their substantive evaluation sessions or any implementation that might later be recommended.

## Problem statement

`v0.3.0` is a coherent stable operating baseline. It preserves the IssueOps thesis that repository/GitHub records hold current operational truth, issues bound intent and authority, implementation plans describe the proposed path, pull requests carry exact-candidate evidence, substantive review remains distinct from mechanical completeness, and humans retain approval and merge authority.

The post-baseline review nevertheless identified three areas where further evidence would materially improve confidence in the operating model:

1. **Mechanical enforcement versus procedural control.** The written authority model is strong, but many controls remain procedural. The project needs to determine whether any small deterministic safeguard would prevent meaningful mistakes without turning IssueOps into an automated lifecycle or approval system.
2. **Process cost and proportionality.** Prior modular-session evidence recorded real session, decision and intervention cost. The project needs to measure where that cost is incurred and which gates actually produce safety/review value before proposing any shorter path.
3. **Portability breadth.** Portable bootstrap/adoption is adopted and has a genuine Level 3 external proof, but one target repository does not establish broad generalisability across different engineering contexts or independent operators.

The project also has previously deferred/adapted ideas around mechanical review preflight, drift detection and operator-tool expansion. Those must not be reopened merely because a consolidation initiative exists. They should be reconsidered only if fresh deterministic recurrence demonstrates a concrete residual gap.

The problem is therefore not “what should IssueOps build next?” It is:

> What, if anything, should IssueOps change after `v0.3.0` to improve safeguards, reduce unnecessary operating cost and strengthen portability evidence without weakening the human-governed execution contract?

## Outcome to prove

Produce enough durable evidence to make one defensible end-of-initiative decision:

- **Maintain** the current `v0.3.0` operating model;
- **Adapt** it through one or more narrowly evidenced corrections; or
- open a **New shaping question** only where the evidence demonstrates a genuinely new capability or stage-level problem that should not be hidden inside maintenance work.

`Maintain` is an explicitly successful outcome. The initiative is not required to produce implementation work.

If the final decision is `Adapt`, implementation must be split into the minimum separately governed issue or issues justified by the evidence. If the final decision is `New shaping question`, stop at the question and require a new owner decision before roadmap or implementation work begins.

## Stable kernel to preserve

The initiative treats these as presumptive operating-model invariants:

1. **Bounded issue contract** — the work begins from durable, reviewable intent and scope rather than hidden chat context.
2. **Current-state reconciliation** — action-relevant GitHub/repository state overrides stale summaries, prompts and handovers.
3. **Explicit proposed path** — implementation approach is visible before meaningful mutation.
4. **Durable human implementation authority where required** — a proposed plan is not self-authorising.
5. **Bounded candidate implementation** — implementation stays within the governing contract.
6. **Exact-candidate validation and evidence** — decision-relevant evidence is tied to the state actually being reviewed.
7. **Substantive contract review** — mechanical completeness does not decide whether the candidate satisfies the issue.
8. **Separate human merge authority** — implementation authority and merge authority remain distinct later decisions.

The proportionality work may test whether low-risk transitions, presentation or session boundaries can be collapsed. It must not silently erase these distinctions.

## Non-goals

This initiative does not authorise:

- a shared `issueops` CLI, package or framework;
- implementation of issue #182 as a standalone mechanical review-preflight tool;
- implementation of issue #184 as a standalone baseline/documentation drift command;
- a new programme-state manifest created to make checking easy;
- automatic readiness, planning, remediation, substantive approval, merge or release decisions;
- automatic lifecycle transitions;
- generic workflow, ref, input, command or shell execution;
- broader PR-comment command-router scope;
- auto-merge or automated release publication;
- repository ruleset, branch-protection or required-check changes without separate evidence-backed implementation authority;
- workflow changes merely because a possible safeguard can be imagined;
- speculative expansion of the primary-record inspector;
- speculative expansion of the static workflow auditor;
- broadening the workflow auditor's handwritten YAML recogniser until it becomes an accidental general YAML parser;
- an external-repository rollout programme;
- replacement of target-local conventions for IssueOps naming symmetry;
- claiming human usability evidence from agent-only walkthroughs; or
- rerunning completed experiments merely to obtain cleaner or more favourable evidence.

The initiative also does not alter the published `v0.3.0` compatibility boundary merely by existing.

## Operating and autonomy boundary

The initiative is evidence-led and issue-driven.

```text
approved consolidation roadmap
  -> bounded evaluation contracts
  -> durable evidence and limitations
  -> final comparison
  -> human decision
  -> separate implementation only when justified
```

The roadmap authorises creation and tracking of the bounded evaluation issues. Each substantive evaluation still requires repository-standard readiness, a detailed evaluation plan and separate owner execution authority.

A child recommendation is not implementation authority.

External pilot mutation is additionally governed by the target repository. No IssueOps parent or child issue can transfer authority into another repository. Each target pilot must identify the exact repository, stable branch/base, local governing record, local instructions, validation/merge conventions and explicit human permission before the first target mutation.

The final comparison issue is decision-only and cannot implement its own recommendation.

## Target state

The desired programme flow is:

```text
roadmap formalisation
  -> #198 mechanical-safeguards evaluation
  -> #199 process-cost/proportionality evaluation
  -> #200 portability-breadth evaluation
  -> #201 final consolidation comparison
  -> Maintain / Adapt / New shaping question
```

#198 and #199 may proceed independently after their own gates.

#200 may be shaped and planned before #199 completes, but real pilot execution should reuse #199's measurement model where practical so portability work does not invent a competing cost/yield scorecard.

#201 remains blocked on sufficiently complete durable evidence from #198–#200.

## Workstream 1 — minimum mechanical safeguards

Governing issue: [#198](https://github.com/8ft0-ai/IssueOps/issues/198).

### Question

What is the minimum useful mechanical safeguard, if any, for IssueOps repository mutations after `v0.3.0`?

### Evidence approach

Reconstruct a representative sample of recent ordinary PR changes, exceptional/direct-main changes and relevant execution deviations.

For each candidate safeguard, determine:

- which concrete failure it would have prevented or detected;
- whether the existing human/process control already caught the problem;
- which legitimate workflow it could block or complicate;
- whether an explicit owner exception remains auditable;
- whether the safeguard is deterministic rather than a disguised approval decision; and
- whether it belongs in workflow validation, GitHub repository controls, written guidance or nowhere.

At minimum compare:

1. no mechanical change;
2. baseline validation on pushes to `main`;
3. ordinary-change PR enforcement with an explicit exceptional owner path;
4. selective deterministic required checks; and
5. a smaller combination if the evidence supports one.

The review should also assess whether unsigned Git-data commits materially weaken provenance for authorised exceptional direct-main changes, or whether verified ancestry plus durable owner authority is sufficient.

### Decision boundary

The workstream must recommend one of:

- **Maintain procedural controls**;
- **Adopt one bounded mechanical safeguard**;
- **Adapt through a small combination of safeguards**; or
- **Collect more evidence**.

It must distinguish observed value from hypothetical benefit and identify false-positive/blocking cost.

No safeguard is implemented in #198 itself.

## Workstream 2 — process cost and lifecycle proportionality

Governing issue: [#199](https://github.com/8ft0-ai/IssueOps/issues/199).

### Question

Is the current `v0.3.0` lifecycle proportionate across change types, and if not, which transitions or presentation mechanics could be simplified without weakening the stable kernel?

### Sample

Reconstruct approximately 20–30 completed changes where durable evidence is sufficient, spanning as available:

- tiny documentation corrections;
- normal documentation work;
- small code/tool changes;
- workflow/security-sensitive changes;
- governance/architecture changes;
- experiments/pilots;
- blocked validation or execution-deviation cases; and
- successful ordinary PRs.

Do not manufacture missing historical precision.

### Measurement model

For each sampled change, record where reconstructable:

- change/risk type;
- issues and durable planning records;
- human decisions;
- model/session transitions;
- branches and pull requests;
- blocked stops;
- manual interventions;
- validation executions/reruns;
- review findings;
- scope-drift findings;
- stale-state detections;
- execution deviations;
- duplicate work prevented;
- post-merge defects or follow-up repairs; and
- elapsed time only when timestamps support a meaningful comparison.

For each gate or transition, assess two dimensions separately:

```text
Cost  = interaction/session/human-attention/delay burden
Yield = meaningful risk, defect, stale state, authority or scope problem caught
```

Use the resulting evidence to classify controls conceptually as:

```text
high value / low cost   -> retain
high value / high cost  -> optimise
low value / low cost    -> low priority
low value / high cost   -> strongest simplification candidate
```

This classification is analytical, not an automatic policy decision.

### Decision boundary

The workstream may recommend:

- **Retain the current uniform lifecycle**;
- **Adapt presentation/session structure only**;
- **Shape one explicit risk-proportionate path for later controlled proof**; or
- **Collect more evidence**.

A proposed shorter path is a hypothesis for later proof, not a stable policy change inside #199.

## Workstream 3 — portability breadth

Governing issue: [#200](https://github.com/8ft0-ai/IssueOps/issues/200).

### Existing evidence boundary

Portable IssueOps adoption is already legitimately adopted. The completed initiative proved a Level 3 fresh independent-agent walkthrough in `8ft0-ai/mri-fourier-lab`, followed by a genuine subsequent target issue/PR and separate human merge decisions.

This workstream does not rerun that proof. It evaluates breadth and generalisability.

### Question

Can a competent engineer or fresh agent adopt and operate IssueOps correctly across materially different repository contexts without relying on the framework author to interpret undocumented assumptions?

### Proposed pilot properties

Shape up to three bounded proof positions, with each external mutation separately authorised by the target repository.

#### A. Ordinary service/application context

Prefer a repository with real application or service code, CI, tests and ordinary maintenance work.

Question: can IssueOps integrate with an existing engineering workflow without becoming the workflow?

#### B. Concurrent-contributor context

Prefer a repository where multiple branches/issues/PRs or moving state create genuine concurrency.

Question: does repository-native authority reconstruction remain reliable when action-relevant state changes between sessions?

#### C. Independent operator context

Prefer an operator/maintainer who did not design IssueOps.

Question: can they correctly discover authority, perform a genuine bounded change, produce sufficient evidence, stop at human decision boundaries and resume later without undocumented help from the framework author?

These properties may be combined in fewer repositories only if the evaluation plan demonstrates that evidence remains distinguishable and reviewable.

### Additional evidence

Reuse #199's cost/yield model where available and also record:

- target repository type and existing controls;
- adoption posture and rationale;
- setup decisions required;
- local conventions preserved or adapted;
- IssueOps-specific artefacts introduced;
- misunderstood or ambiguous guidance;
- assistance required from an IssueOps author/designer;
- unsafe or duplicate actions avoided;
- fresh-session reconstruction quality;
- first-change versus second-change friction;
- human decisions/interventions;
- blocked stops and deviations;
- evidence level reached; and
- already-compatible/no-change outcomes where applicable.

### Success criterion

Success is not “files were adopted”.

The strongest desired evidence is that a competent engineer unfamiliar with IssueOps can correctly discover target-local authority, perform a genuine bounded change, generate sufficient evidence, stop at the correct human decision boundaries and resume later without the framework author filling undocumented gaps.

### Decision boundary

Recommend one of:

- **Portability evidence sufficient**;
- **Adapt bootstrap/guidance through separately governed work**; or
- **More breadth required**.

## Recurrence-triggered watchpoints

The initiative retains three watchpoints but creates no scheduled implementation work for them.

### Mechanical review preflight — #182

The existing disposition remains: defer a separate implementation and absorb into the inspector/evidence path unless a concrete residual gap emerges.

A revisit requires fresh evidence that existing tooling repeatedly fails to expose a deterministic mechanical-currentness condition needed before substantive review.

### Baseline/documentation drift — #184

The existing disposition remains: no standalone drift command.

A revisit requires a fresh concrete contradiction with a clear canonical owner and a deterministic, low-false-positive relationship. Prefer one small assertion in an existing validator before a new command or state manifest.

### Operator-tool expansion

The primary-record inspector and static workflow auditor remain optional/advisory.

In particular, if a future workflow-auditor requirement needs materially broader YAML semantics, stop extending the bounded handwritten recogniser and reassess whether a standard YAML parser is the safer foundation. Do not grow a partial parser simply because additional syntax can be recognised.

## Final comparison — Maintain / Adapt / New shaping question

Governing issue: [#201](https://github.com/8ft0-ai/IssueOps/issues/201).

The final comparison begins only when #198–#200 contain sufficiently complete durable evidence.

It must answer:

1. Does the stable operating model remain sound?
2. Is any current control materially under-enforced?
3. Is lifecycle ceremony materially disproportionate for one or more classes of work?
4. Has portability been demonstrated broadly enough for current claims?
5. Did any repeated deterministic failure mode justify a new validator or bounded safeguard?
6. Is there evidence for a concrete implementation change, or only hypotheses?

The final recommendation is exactly one of:

- **Maintain**;
- **Adapt**; or
- **New shaping question**.

The final issue may identify the minimum next action, but cannot implement it.

## Acceptance gates

### Governance and scope

- [ ] The initiative remains an unnumbered consolidation programme rather than becoming Stage 6 by implication.
- [ ] Child issue creation is not treated as execution authority.
- [ ] #198–#201 each pass their own required gates before substantive work.
- [ ] No child recommendation becomes implementation authority automatically.
- [ ] `v0.3.0` remains the stable baseline unless a later separately governed release decision changes it.

### Mechanical-safeguard evidence

- [ ] #198 compares candidate controls against observed failure/prevention evidence and blocking cost.
- [ ] Procedural versus mechanical enforcement is distinguished explicitly.
- [ ] Any recommended safeguard remains deterministic and bounded.
- [ ] Settings/workflow implementation is deferred to a separate issue if recommended.

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

## Risks and controls

### Risk: consolidation becomes feature expansion

Control: the roadmap makes `Maintain` a successful result, creates evaluation rather than implementation children and prohibits speculative tooling/automation work.

### Risk: mechanical enforcement crowds out human judgement

Control: #198 evaluates deterministic safeguards only and keeps substantive review, approval and merge decisions human.

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
- [ ] #198 has a durable mechanical-safeguards conclusion;
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
