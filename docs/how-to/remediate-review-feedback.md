# Remediate pull-request review feedback

Use this guide to address review findings without losing the issue contract, evidence trail or scope boundary.

For exact feedback classifications and merge blockers, use [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md).

## 1. Collect the complete review state

Fetch:

- top-level PR conversation comments;
- submitted reviews;
- inline review threads;
- requested changes;
- current workflow and check results; and
- the final branch head.

Do not remediate only the latest visible comment when another unresolved thread materially affects the PR.

## 2. Classify each item

Use one classification:

- **Required fix** — a defect, missed criterion, inaccurate evidence, unsafe permission, broken link, failing validation or contract gap.
- **Optional improvement** — useful but unnecessary clarity or maintainability work.
- **Clarification needed** — ambiguity that could change scope or the correct fix.
- **Out of scope** — work not authorised by the issue.

When uncertain, clarify before editing.

## 3. Apply only scoped changes

Apply required fixes that belong to the issue. Apply an optional improvement only when it is clearly safe, small and inside scope.

Do not use review feedback to introduce unrelated refactoring, automation, repository settings, application code or a broader rewrite. Create a follow-up issue for valuable out-of-scope work.

## 4. Read the changed state back

After remediation:

- inspect each changed file;
- compare the branch with `main`;
- confirm no unexpected file entered the diff; and
- verify the original acceptance criteria and non-goals again.

## 5. Rerun affected validation

Rerun every check that the remediation could affect. A wording change may require only documentation validation; a permissions or workflow change may require the full relevant checklist and repository-native workflow.

Do not rely on a passing run from an earlier head when the remediation changed the behaviour or evidence it validated.

## 6. Reply and resolve accurately

Reply to each addressed review item with the change and validation evidence. Resolve an inline thread only when:

- the fix is present;
- affected validation is not failing; and
- no clarification remains.

Do not resolve a thread merely to make the PR appear clean.

## 7. Refresh material evidence

Remediation is material when it changes validation, permissions, dependencies, deployment behaviour, public claims, scope, assumptions, caveats or remaining checks.

For material remediation, update the PR body or post a clearly labelled remediation evidence comment using the canonical [template](../reference/pr-evidence-templates.md#remediation-evidence-template).

Minor typo fixes may use an inline reply when they do not change meaning, scope, validation or risk.

## 8. Repeat the groundedness review

Against the final head, ask again:

1. Did the PR do what was needed?
2. Did it only do what was asked?

Refresh the recommendation. Do not retain `Approve` automatically from an earlier state.

## 9. Request review again

Before returning the PR for approval, confirm:

- all review items were collected and classified;
- required fixes are complete;
- optional work remained scoped;
- out-of-scope work was not smuggled into the branch;
- changed files were read back;
- affected validation was rerun;
- evidence reflects the final head; and
- no required thread remains unresolved.

## Common failure modes

- implementing every suggestion without checking scope;
- changing files before resolving ambiguous feedback;
- replying without rerunning affected validation;
- resolving threads before the fix exists;
- leaving the PR body stale after material changes; or
- treating remediation completion as approval without a final contract review.
