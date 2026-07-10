# Stage 1 — Manual execution-contract foundation

Status: completed.

Record type: retrospective reconstruction.

This record reconstructs the intended Stage 1 shape from issues, pull requests and release evidence created during delivery. A formal stage roadmap did not exist before the work, and the later Stage 1.x increments were not all known when issue #1 was opened.

## Problem statement

Agentic coding work needed a bounded and reviewable repository operating model. A vague ticket or informal prompt did not provide enough control over scope, expected outcome, exclusions, validation or human approval.

The repository needed to prove that a GitHub issue could act as the execution contract, while a pull request could act as the evidence pack used for human contract verification.

## Outcome to prove

Demonstrate a usable manual loop in which an agent can implement bounded repository work from an explicit contract and a human can determine from the pull request whether the contract was fulfilled without introducing automation or weakening merge authority.

## Non-goals

- No automatic agent execution.
- No GitHub Actions orchestration.
- No required status checks or branch protection changes.
- No automatic merge.
- No application-code delivery.
- No release automation.
- No enforced lifecycle labels.

## Operating and autonomy boundary

The issue defines the authorised work. The implementation plan proposes the execution path. The agent may make changes only within that contract and must stop when scope, authority or safe tool operation is unclear.

A human retains authority to approve scope changes, accept incomplete validation and merge the pull request. Documentation and templates may guide behaviour, but Stage 1 introduces no automated enforcement.

## Target workflow or target state

```text
Issue = execution contract
  -> readiness check
  -> implementation plan
  -> safe tool-operation check
  -> contract-bound implementation
  -> lightweight validation
  -> pull request evidence pack
  -> human contract verification
  -> human merge decision
```

The safe tool-operation and lightweight-validation steps emerged during delivery rather than being fully specified in the initial issue.

## Acceptance gates

- [x] A reusable execution-contract issue structure defines problem, outcome, scope, non-goals, acceptance criteria, validation and risk.
- [x] The manual issue-to-branch-to-PR workflow is documented.
- [x] Pull requests carry evidence that allows contract verification.
- [x] The workflow is dogfooded through a real follow-up documentation change.
- [x] Accidental repository mutations produce an explicit safe-operation and circuit-breaker protocol.
- [x] Lightweight validation evidence is added without creating automated enforcement.
- [x] The resulting baseline is documented and released as `v0.1.0`.
- [x] Human merge authority and the manual operating boundary remain intact.

## Proposed implementation slices

The following slices are a retrospective grouping of the work that actually emerged:

```text
#1  -> establish the execution-contract foundation
#3  -> dogfood the workflow with examples
#10 -> add lightweight validation evidence
#14 -> add safe tool-operation and circuit-breaker guidance
#17 -> prepare the Stage 1 baseline release
```

This grouping must not be read as evidence that all five slices were planned when #1 began.

## Risks and controls

### Risk: the issue remains a vague ticket

Control: require explicit problem, outcome, scope, non-goals, acceptance criteria, validation evidence and change risk.

### Risk: the agent broadens scope during implementation

Control: require a plan before changes and review the final PR against the issue contract.

### Risk: the wrong mutating repository tool is invoked

Control: add a pre-mutation safe-operation check and stop immediately after any unintended mutation.

### Risk: evidence becomes performative rather than useful

Control: keep validation lightweight, specific to the change and honest about checks that did not run.

### Risk: manual guidance is mistaken for automation

Control: state the Stage 1 exclusions repeatedly in issues, pull requests, documentation and release notes.

## Definition of done

The reconstructed Stage 1 boundary is complete because:

- [x] the execution-contract model and manual workflow shipped;
- [x] the workflow was dogfooded;
- [x] safe-operation and validation gaps exposed during use were addressed;
- [x] representative pull requests contain reviewable evidence;
- [x] the baseline release notes exist;
- [x] `v0.1.0` records the first stable manual baseline; and
- [x] remaining automation and publication work was deferred to a later stage.

## Likely next decision boundary

Stage 1 established the language and manual controls. The next question was whether the model could become easier to discover, publish, validate and operate without turning human authority into automated enforcement. That became the Stage 2 planning boundary.
