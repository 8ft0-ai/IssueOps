# Stage N — Short stage name

Status: shaping.

Record type: contemporaneous.

Use `Record type: retrospective reconstruction.` only when rebuilding historical intent after delivery. Retrospective records must not imply that this artefact existed before the work.

## Problem statement

Describe the operational, evidence, usability or governance problem this stage exists to solve.

## Outcome to prove

State the observable outcome the stage must demonstrate. Do not use implementation activity as the outcome.

## Non-goals

List explicit exclusions.

```text
No automatic merge unless explicitly approved.
No automatic publication unless explicitly approved.
No weakened human contract-verification boundary.
No speculative next-stage implementation.
```

## Operating and autonomy boundary

State what agents or workflows may do, what requires human approval, and what repository or external mutations remain prohibited.

## Target workflow or target state

Describe the intended workflow, documentation state or operating model.

```text
step one
  -> step two
  -> evidence gate
  -> human decision
```

## Acceptance gates

- [ ] Gate one proves an outcome.
- [ ] Gate two proves a boundary.
- [ ] Gate three proves the real workflow.

## Proposed implementation slices

Use a small linked issue set rather than relying on one broad issue.

```text
1. Foundation or control surface
2. First bounded capability
3. Proof or dogfood
4. Close-out decision
```

## Risks and controls

### Risk: example risk

Control: explain how the stage limits, detects or recovers from it.

## Definition of done

The stage is complete when:

- [ ] approved execution issues are complete or explicitly resolved;
- [ ] the intended proof boundary has evidence;
- [ ] limitations and deviations are recorded honestly;
- [ ] a completed delivery record exists;
- [ ] the delivery log is updated; and
- [ ] the next decision boundary is recorded without speculative execution work.

## Likely next decision boundary

Describe the question that evidence from this stage should allow the project to answer next.
