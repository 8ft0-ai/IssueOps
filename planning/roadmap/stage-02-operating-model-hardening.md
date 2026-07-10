# Stage 2 — Published and hardened operating model

Status: completed.

Record type: retrospective reconstruction.

This record reconstructs Stage 2 as one coherent stage from the public roadmap, Stage 2.x issues, merged pull requests, workflow evidence and release notes. A complete Stage 2 stage pack did not exist before delivery, and the twenty-three increments were not all known at the start.

## Problem statement

Stage 1 proved the manual execution-contract loop, but the operating model remained fragmented and lightly evidenced.

The repository needed to make the model easier to discover and use, publish canonical documentation, consolidate process rules, strengthen readiness and review evidence, prove repository-native validation and support bounded delegated work without weakening human authority.

## Outcome to prove

Demonstrate that the Stage 1 contract can become a published, dogfooded and operationally validated repository operating model while preserving manual scope control, contract verification, merge authority and honest treatment of incomplete evidence.

## Non-goals

- No automatic agent execution.
- No automatic issue or pull-request lifecycle transitions.
- No automatic dependency detection.
- No required status checks or branch protection changes.
- No review bots or automatic review-thread resolution.
- No GitHub auto-merge configuration.
- No automatic publication decision beyond the approved documentation deployment path.
- No Stage 3 orchestration or enforcement implementation.

## Operating and autonomy boundary

Issues remain execution contracts and implementation plans remain proposed paths. Agents and workflows may prepare bounded changes and validation evidence, but they do not gain authority to broaden scope, merge, publish new product content, weaken controls or treat advisory labels as authoritative state.

Repository-native validation is preferred where available. Representative fallback evidence may be accepted only when its limitations are visible and the missing check does not invalidate the contract.

A human retains authority over contract readiness, scope changes, remediation decisions, merge, publication boundaries and acceptance of post-merge verification.

## Target workflow or target state

Stage 2 is reconstructed around five capability clusters:

```text
canonical documentation and Pages publishing
  -> consolidated operating protocol
  -> readiness, validation, evidence and remediation controls
  -> bounded delegation and completion summaries
  -> repository-native proof, dogfood and usability close-out
  -> Stage 2 baseline release
```

The intended end state is a contributor-visible protocol whose automated parts and manual parts are clearly separated.

## Acceptance gates

- [x] Canonical MkDocs documentation is published through GitHub Pages.
- [x] One operating-protocol page describes the lifecycle from issue readiness through post-merge verification.
- [x] Dependency-aware readiness, safe-operation, change-type validation and workflow-review guidance are documented.
- [x] PR evidence, remediation and post-merge boundaries are explicit.
- [x] Bounded delegated batch mode retains owner authority and stop conditions.
- [x] Repository-native pull-request validation checks the exact PR commit and does not deploy production from a PR.
- [x] A complete protocol dogfood run records real process friction and circuit-breaker evidence.
- [x] Contributor usability is reviewed and the front door is improved without removing higher-risk controls.
- [x] Production Pages deployment is verified from `main`.
- [x] Missing repository lifecycle labels are recorded as an explicit non-blocking limitation rather than falsely reported as complete.
- [x] Stage 2 release notes distinguish manual guidance from automated enforcement.

## Proposed implementation slices

The following is a retrospective capability grouping, not the original issue sequence:

```text
1. Canonical documentation and publishing
   #19, #21

2. Protocol and evidence hardening
   #23 through #30 and related guidance increments

3. Proportionate delegation and compact evidence
   delegated batch mode, PR templates, repository-native evidence,
   completion summaries and compact tool-operation evidence

4. Operational proof and close-out
   #53, #55, #56, #57, #58

5. Deferred repository-label creation
   #54, closed as a non-blocking limitation
```

The detailed Stage 2.x issue history remains canonical. This grouping exists only to explain the stage-level outcome.

## Risks and controls

### Risk: documentation becomes a second inconsistent process

Control: identify one canonical operating protocol and treat specialised pages as supporting guidance.

### Risk: more guidance creates disproportionate contributor friction

Control: add compact evidence formats, a small-change path and a usability review while retaining full controls for ambiguous or higher-risk work.

### Risk: workflow automation weakens publication or permission boundaries

Control: use job-scoped permissions, pinned dependencies, strict builds and explicit build/deploy separation.

### Risk: representative validation is mistaken for repository-native proof

Control: define repository-native evidence as preferred, label fallbacks explicitly and prove the actual PR workflow on the exact commit.

### Risk: delegated batch mode becomes implicit auto-merge

Control: require owner authorisation, eligibility constraints, stop conditions and explicit merge authority.

### Risk: advisory labels become false workflow state

Control: keep written evidence canonical and disclose that the additional repository label definitions were not created.

### Risk: process dogfood hides operational mistakes

Control: record the unintended mutation, circuit breaker and recovery rather than cleaning the history into a false success narrative.

## Definition of done

The reconstructed Stage 2 boundary is complete because:

- [x] canonical documentation and Pages publishing exist;
- [x] the operating protocol and supporting controls are published;
- [x] repository-native PR validation and production-deploy separation are proven;
- [x] the complete protocol has been dogfooded;
- [x] production Pages deployment has been verified;
- [x] contributor usability findings have been recorded and applied selectively;
- [x] the lifecycle-label gap is explicitly deferred;
- [x] Stage 2 baseline release notes recommend `v0.2.0`; and
- [x] Stage 3 remains a planning question rather than an implementation backlog.

## Likely next decision boundary

Stage 2 established a strong manual operating model and limited repository-native automation. The next question is which bounded automation would materially reduce friction without weakening issue authority, safe operation, evidence quality, human contract verification, merge control or publication boundaries.

That question should be shaped through a Stage 3 roadmap before any Stage 3 execution contracts are created.
