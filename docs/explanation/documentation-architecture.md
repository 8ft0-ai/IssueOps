# Documentation architecture

IssueOps organises user-facing documentation around the reader’s need rather than the repository component that happens to contain the answer.

The four modes are distinct because learning, completing a task, checking an exact rule and understanding a design decision require different structures. A page may link to other modes, but it should have one primary purpose.

## The four modes

### Tutorials: learn through a controlled experience

A tutorial teaches a newcomer by guiding them through a complete, reliable journey. It minimises choices, states expected outcomes and uses only implemented capabilities.

A tutorial may repeat the minimum command or value needed for the experience, but it should link to reference for the full rule and to explanation for rationale.

### How-to guides: complete a task

A how-to guide assumes the reader has a goal. It provides the shortest safe procedure for that goal, including decision points and failure handling that materially affect completion.

A how-to guide should not become an exhaustive field catalogue or a history of why the process exists.

### Reference: check exact rules and formats

Reference owns normative facts: required fields, statuses, formats, permissions, evidence requirements, classifications, validation matrices, recommendation vocabulary and merge blockers.

Reference should be precise, neutral and easy to scan. Where a rule is mandatory, reference is its canonical home.

### Explanation: understand concepts and trade-offs

Explanation connects ideas and gives the reasoning behind the model. It may discuss alternatives, design history and consequences, but it must not be the only place where a mandatory rule appears.

## Primary-mode rule

Every user-facing page has one primary mode.

Use this test:

| Reader question | Primary mode |
| --- | --- |
| “Can you teach me by taking me through it?” | Tutorial |
| “How do I accomplish this task?” | How-to |
| “What exactly is required or allowed?” | Reference |
| “Why is it designed this way?” | Explanation |

A mixed legacy page may remain during migration, but its landing-page classification must identify the primary reader need and any later split that is still required.

## Canonical-source ownership

- Exact requirements belong in Reference.
- Task sequence belongs in How-to.
- Controlled learning flow belongs in Tutorials.
- Rationale and trade-offs belong in Explanation.
- Examples illustrate reference rules; they do not replace them.
- The operating protocol remains the authoritative lifecycle map while focused pages are introduced, then links to their canonical details.

When two pages need the same normative fact, one page owns the complete rule and the other links to it. Small repetition is acceptable only when it is necessary to complete a tutorial or procedure safely and is unlikely to drift.

## Cross-linking

Cross-mode links are expected:

- a tutorial links to how-to guidance when a learner later repeats the task independently;
- a how-to guide links to reference for exact formats and blockers;
- reference links to explanation when rationale helps interpretation; and
- explanation links to how-to or reference rather than embedding procedures or hidden requirements.

A link should move the reader to a different need, not duplicate the destination.

## Repository boundary

The substantive documentation tree contains only the four user-facing modes:

```text
docs/
├── tutorials/
├── how-to/
├── reference/
└── explanation/
```

Root-level `README.md` and `AGENTS.md` retain repository-level roles.

The following remain in their existing domains:

- `planning/` roadmaps, delivery records, logs and the delivery graph;
- tests and fixtures;
- scripts and generated artefacts;
- GitHub workflows and repository configuration;
- implementation-adjacent subsystem material; and
- historical evidence that is not current user-facing guidance.

Project records may be linked from the documentation. They are not copied into a fifth Project records category or forced into one of the four modes.

## Compatibility during migration

Stage 4 is incremental. Existing page paths remain available while focused pages are introduced.

A legacy path may become a concise landing or compatibility page when its content is split. Compatibility pages should:

- identify the new canonical destinations;
- preserve useful context or commonly linked anchors where practical;
- avoid duplicating complete rules or historical records; and
- be removed only after a deliberate URL review.

The migration does not add a redirect plugin solely for structural neatness.

## Authoring checklist

Before adding or materially changing a page:

1. Identify the reader’s primary question.
2. Choose one primary mode.
3. Confirm where normative facts are owned.
4. Link across modes instead of copying full sections.
5. Keep planning and implementation artefacts in their repository domains.
6. Preserve stable URLs or record the compatibility decision.
7. Check current stable and experimental capability claims.
8. Run the [documentation currency checklist](../documentation-currency.md) and strict MkDocs validation.

The purpose of this architecture is not four directory names. It is to make the correct path obvious while preserving a single, reviewable source for IssueOps rules and authority boundaries.
