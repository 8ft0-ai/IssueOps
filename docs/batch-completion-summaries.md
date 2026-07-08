# Batch completion summaries

A batch completion summary gives readers one clear record of a delegated batch run.

Individual issues and pull requests remain the source of truth. The summary is a navigation aid that explains what was included, what merged, what validation was performed and what caveats remain.

## When to create one

Create a batch completion summary when:

- multiple issues are completed under delegated batch mode;
- the work spans several PRs;
- there are shared caveats across the batch;
- follow-up work was identified; or
- a reader would otherwise need to reconstruct the batch from many issue and PR threads.

A summary is usually unnecessary for a single PR or a very small change with no shared caveats.

## Where to record it

A batch summary can be recorded as:

- a top-level issue comment on the final issue in the batch;
- a standalone documentation note if the batch changes the process materially; or
- a release note when the batch represents a release-worthy milestone.

The summary should link to the relevant issues and PRs rather than duplicating every evidence pack.

## Reusable format

```md
## Batch completion summary

Goal:

- 

Issues completed:

- #N — title — PR #N

Merged PRs:

- PR #N — title — merge commit

Validation performed:

- 

Deliberately not changed:

- 

Caveats and pending checks:

- 

Follow-up work:

- None / listed below
```

## Relationship to delegated batch mode

Delegated batch mode authorises execution and merge of a bounded low-risk backlog. A batch completion summary records what actually happened.

The summary does not replace per-issue readiness, per-PR evidence, validation records or groundedness reviews.

## Safety boundary

Do not use a batch summary to hide failed validation, scope drift or unresolved caveats.

If a batch includes a stop condition, stop the batch and record the reason rather than summarising it as complete.
