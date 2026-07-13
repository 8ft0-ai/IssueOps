# Repository assessment and adoption-posture form

Use this form before any target-repository mutation.

The assessment maps existing capabilities and proposes a posture. It does not authorise file changes, branch creation, pull-request creation or merge.

## Assessment identity

- Target repository:
- Stable or default branch:
- Assessment date:
- Assessor or session:
- Bootstrap specification: `IssueOps Bootstrap 0.1`
- Pinned `BOOTSTRAP.md` URL:

## Available authority

Read-only assessment:

- Authorised by:
- Scope:
- Restrictions:

Creation of one local bootstrap issue:

- Permitted: Yes / No / Unclear
- Authorised by:
- Conditions:

Other mutation authority:

- None before a local issue is ready and planned.

If the repository, branch or authority is unclear, stop and record the missing decision.

## Repository instructions consulted

| Surface | Path or location | Relevant rule | Authority or compatibility effect |
| --- | --- | --- | --- |
| Agent instructions |  |  |  |
| Contributor guidance |  |  |  |
| Issue templates or conventions |  |  |  |
| Pull-request template or review rules |  |  |  |
| Validation commands and required checks |  |  |  |
| Branch and dependency conventions |  |  |  |
| Merge authority and method |  |  |  |
| Planning or roadmap guidance |  |  |  |
| Protected or sensitive areas |  |  |  |

## Capability assessment

Use `Present`, `Partial`, `Missing`, `Conflicting` or `Not applicable`.

| Manual IssueOps capability | Local owner or evidence | Status | Material gap or conflict |
| --- | --- | --- | --- |
| An issue can act as an executable contract |  |  |  |
| Readiness and dependencies are checked before branch creation |  |  |  |
| An implementation plan is recorded before mutation |  |  |  |
| One issue-scoped branch contains the change |  |  |  |
| Mutating operations have an explicit safety check |  |  |  |
| Validation is change-specific and tied to the final state |  |  |  |
| The pull request carries scope and evidence |  |  |  |
| Review checks both fulfilment and scope control |  |  |  |
| Human approval or bounded local delegation governs merge |  |  |  |
| Dependent multi-issue planning exists when genuinely needed |  |  |  |

## Convention map

Record the local surface that should be preserved or adapted.

| Need | Existing local surface | Treatment: preserve / adapt / add / not needed | Reason |
| --- | --- | --- | --- |
| Agent operating rules |  |  |  |
| Execution-contract fields |  |  |  |
| Readiness and dependency evidence |  |  |  |
| Implementation-plan format |  |  |  |
| Branch naming and base selection |  |  |  |
| Safe mutation guidance |  |  |  |
| Validation commands and statuses |  |  |  |
| Pull-request evidence and review |  |  |  |
| Merge authority |  |  |  |
| Stage or roadmap planning |  |  |  |

Use the [convention-mapping guidance](convention-mapping.md) before selecting `add`.

## Adoption-posture decision

Selected posture:

- Already compatible / Minimal manual adoption / Stage-capable adoption

Evidence supporting the posture:

- 

Why the lighter posture is insufficient, when applicable:

- Not applicable / 

Why the heavier posture is unnecessary, when applicable:

- 

No-change outcome:

- Supported: Yes / No
- Reason:

## Proposed local changes

List only material changes needed to reach the selected posture.

| Local surface | Proposed change | Existing convention preserved | Why needed | Validation |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

If no change is required, state:

```text
No repository change is recommended. Existing local controls satisfy the selected posture.
```

## Prohibited or separately governed changes

Confirm that the proposed bootstrap does not include:

- [ ] workflows or automatic lifecycle transitions;
- [ ] a CLI, installer, generator, schema, bot or app;
- [ ] settings, permissions, branch-protection or required-check changes;
- [ ] auto-merge configuration;
- [ ] new labels as a prerequisite;
- [ ] application-code changes;
- [ ] organisation-wide rollout; or
- [ ] a copied canonical IssueOps protocol.

Any checked item requires a separate local decision and execution contract. It must not be hidden inside the bootstrap issue.

## Risks, conflicts and unsupported capabilities

- Local instruction conflicts:
- Platform or connector limitations:
- Validation limitations:
- Authority limitations:
- Sensitive or protected areas:
- Open questions:

## Proposed first local issue

Prepare the complete issue using [the local bootstrap issue template](bootstrap-issue-template.md).

- Proposed title:
- Proposed issue body completed: Yes / No
- Existing valid equivalent issue: None / link
- Requested first write: Create the local bootstrap issue / No write required

## Assessment decision

Choose one:

- **Ready to request local issue creation** — the assessment is complete, owner permission is explicit and the proposed issue is bounded.
- **Already compatible; no change recommended** — retain the assessment and stop without mutation.
- **Clarification required** — authority, scope, posture or local conventions are materially unclear.
- **Reject adoption** — the repository cannot safely support the manual IssueOps controls within the permitted scope.

Decision:

- 

Evidence and unresolved conditions:

- 
