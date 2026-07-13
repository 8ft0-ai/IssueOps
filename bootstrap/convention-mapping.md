# Map IssueOps to existing repository conventions

Use this guidance during the read-only assessment.

The goal is to identify effective local owners for the manual IssueOps controls, not to reproduce the source repository's filenames or directory layout.

## Precedence

Apply instructions in this order:

1. explicit target-repository owner authority;
2. target-repository agent and contributor instructions;
3. target-repository issue, validation, review and merge conventions;
4. the locally approved bootstrap execution contract; and
5. the remote IssueOps bootstrap method.

If remote guidance conflicts with explicit local instructions or authority, stop and surface the conflict. Do not silently override the target repository.

## Mapping rule

For each required capability, choose one treatment:

- **Preserve** — the existing surface is clear and compatible.
- **Adapt** — the existing surface remains the owner but needs a bounded correction.
- **Add** — no compatible owner exists and a new surface has a tested need.
- **Not needed** — the capability is not required for the selected posture.

Choose `Add` only after ruling out a compatible existing owner.

## Capability map

| Capability | Common local owners | Compatibility question |
| --- | --- | --- |
| Agent operating rules | `AGENTS.md`, `CLAUDE.md`, contributor guidance, tool-specific instructions | Can an agent identify the issue contract, branch, validation and authority rules without hidden context? |
| Executable issue contract | issue template, issue form, engineering ticket convention | Does the issue contain outcome, scope, non-goals, acceptance, validation, risk and instructions? |
| Readiness and dependencies | issue comments, ticket status, checklist or planning convention | Is executability and a safe starting point recorded before branch creation? |
| Implementation plan | issue comment, design note or work plan | Is the proposed path visible before mutation? |
| Issue-scoped branch | branch convention or contributor workflow | Can one issue be isolated from a known safe base? |
| Safe mutation | agent instructions, operational checklist or repository policy | Are operation, target, expected effect and forbidden effects considered before writes? |
| Validation | scripts, task runner, CI, contributor documentation | Are exact checks and unavailable evidence recorded against the final state? |
| Pull-request evidence | PR template, review checklist or change description convention | Can a reviewer compare final scope and evidence with the issue? |
| Contract review and merge | review policy, CODEOWNERS, branch rules or maintainer convention | Are fulfilment, scope, residual risk and merge authority explicit? |
| Multi-issue planning | roadmap, milestone, project board or design record | Is this genuinely needed for the selected posture? |

## Preserve local terminology

Equivalent local terms are valid. Examples:

- a work item may be called a ticket, story or change request;
- a readiness decision may be part of an existing triage or design-approval comment;
- a pull-request evidence pack may be an established change summary and validation section; and
- a roadmap may be a milestone or project plan.

Do not rename compatible surfaces merely to use IssueOps vocabulary. Record the mapping so an unfamiliar agent can find the local owner.

## Adapt rather than duplicate

Prefer a bounded addition to an existing owner when:

- the existing document already governs the relevant audience or task;
- the missing rule is small and compatible;
- a new file would force readers to reconcile two control surfaces; or
- the local repository has an established template or workflow.

Add a new surface only when no existing owner is clear or safe to extend.

## Resolve conflicts explicitly

Classify a mismatch before proposing a change.

### Compatible difference

The local convention uses different wording or structure but provides the same effective control.

Treatment: preserve and document the mapping.

### Bounded gap

The local owner exists but omits a required field, gate or authority statement.

Treatment: adapt the existing owner through the local bootstrap issue.

### Material conflict

The local convention permits behaviour that contradicts the selected IssueOps posture, such as branching before any executable issue or treating validation as optional without evidence.

Treatment: describe the conflict and request a local decision. Do not invent which rule should win.

### Unsupported capability

The platform or available tools cannot provide a desired surface or check.

Treatment: record the limitation honestly. Use a weaker evidence path only when local policy permits it and correctness does not depend on pretending stronger evidence exists.

## Proportionality checks

Before adding an artefact, answer:

1. Which acceptance criterion requires it?
2. Why can no existing local owner satisfy that criterion?
3. Who will use and maintain it?
4. Does it duplicate a canonical protocol or local instruction?
5. Would a smaller adaptation provide the same safety?

If these questions do not establish a distinct need, do not add the artefact.

## Posture-specific expectations

### Already compatible

- preserve local owners;
- record mappings and only material gaps;
- permit no change; and
- do not add IssueOps-branded templates for visibility alone.

### Minimal manual adoption

- adapt the fewest local surfaces needed to make the lifecycle executable and reviewable;
- keep issue, validation, PR and merge rules discoverable; and
- do not add planning machinery unless dependency or governance evidence requires it.

### Stage-capable adoption

- retain all minimal-manual controls;
- add only the planning and close-out surfaces needed for dependent delivery or formal proof; and
- keep intended roadmap state separate from actual delivery evidence.

## Mapping output

The assessment should retain a table containing:

- required capability;
- existing local owner and evidence;
- treatment: preserve, adapt, add or not needed;
- exact material gap;
- proposed local change;
- validation; and
- unresolved authority or compatibility question.

This mapping becomes evidence for the selected posture and the scope of the proposed local bootstrap issue. It is not permission to implement the changes.
