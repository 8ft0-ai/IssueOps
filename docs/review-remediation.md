# PR review remediation protocol

Review remediation is the controlled loop for responding to pull request feedback without losing the original issue contract.

The goal is not to make every suggested improvement. The goal is to understand the feedback, classify it, apply the fixes required to satisfy the issue, revalidate the result and leave enough evidence for the reviewer to see what changed.

This protocol is manual. It does not add review bots, required review rules, branch protection, permission changes or automatic review-thread resolution.

## When to use this protocol

Use this protocol whenever a pull request receives:

- inline review comments;
- submitted review summaries;
- top-level PR conversation comments;
- requested changes;
- reviewer questions that may affect scope; or
- feedback that changes validation, risk, permissions, dependencies or documented behaviour.

## Comment classifications

Classify review feedback before changing files.

| Classification | Meaning | Action |
| --- | --- | --- |
| Required fix | The feedback identifies a defect, missed acceptance criterion, inaccurate evidence, unsafe permission, broken link, failing validation or issue-contract gap. | Fix before approval or explain why it is invalid. |
| Optional improvement | The feedback improves clarity, style or future maintainability but is not needed to satisfy the issue. | Apply only if it stays inside scope and does not delay or broaden the issue unexpectedly. |
| Clarification needed | The feedback is ambiguous or asks a question that could change scope. | Ask or answer before changing files. |
| Out of scope | The feedback asks for work outside the issue contract. | Do not implement in the current PR unless the repository owner explicitly expands scope or a follow-up issue is created. |

If the classification is unclear, treat the item as clarification needed rather than guessing.

## Review remediation loop

Use this loop after review feedback arrives:

1. Fetch PR conversation comments, submitted reviews and inline review threads.
2. Classify each item as required fix, optional improvement, clarification needed or out of scope.
3. Apply required fixes only unless optional improvements are clearly safe and scoped.
4. Read changed files back from the branch.
5. Rerun available validation that could have been affected by the remediation.
6. Compare the branch with `main` to check scope.
7. Reply to each addressed inline comment or review question.
8. Resolve review threads only after the fix is present and validation is not failing.
9. Post or update remediation evidence when the remediation materially changes the PR.

## Avoiding scope drift

Remediation should stay inside the issue contract.

Do not use review feedback as a reason to add unrelated refactoring, new automation, branch protection, labels, app code or broader documentation rewrites unless the issue already allows that work.

If feedback is valuable but out of scope, record it as follow-up work rather than expanding the current PR.

## Material remediation

A remediation is material when it changes any of the following:

- validation evidence;
- security or permissions posture;
- dependency model;
- deployment behaviour;
- public documentation claims;
- files outside the original stated scope;
- assumptions, caveats or remaining checks.

Material remediation should update the PR body or add a clearly labelled top-level remediation evidence comment so the final state is visible without reconstructing it from commits and threads.

Minor typo, grammar or wording fixes do not require a full PR body update unless they change meaning, scope, validation or risk.

## Replying, resolving and updating evidence

Use inline replies when the feedback was inline or thread-specific.

Use a top-level remediation summary when multiple comments were addressed or when the reviewer needs a single summary of the final state.

Update the PR body when remediation changes any of the following:

- validation evidence;
- security or permissions posture;
- dependency model;
- deployment behaviour;
- public documentation claims;
- scope evidence;
- assumptions, caveats or remaining checks.

If remediation only fixes a typo or wording issue with no material evidence change, an inline reply may be enough.

## Compact remediation checklist

Before asking for review again, confirm:

- [ ] All review comments were collected.
- [ ] Each comment was classified.
- [ ] Required fixes were applied.
- [ ] Optional improvements stayed inside scope.
- [ ] Out-of-scope feedback was not implemented without explicit approval.
- [ ] Changed files were read back from the branch.
- [ ] Affected validation was rerun or recorded as pending/not performed.
- [ ] Branch diff was compared against `main` for scope drift.
- [ ] Inline comments were replied to where useful.
- [ ] Threads were resolved only after fixes were present.
- [ ] PR evidence was updated or a remediation evidence comment was posted where material.

## Evidence to record

A remediation summary can use this format:

```md
## Remediation evidence

Review feedback addressed:

- Comment/thread:
- Classification:
- Change made:
- Validation rerun:
- Scope impact:

Final contract check:

- Did the PR still do what was needed?
- Did the PR still only do what was asked?

Remaining items:

- None / follow-up issue required / clarification pending.
```

## Relationship to evidence packs and contract verification

The [pull request evidence pack](pr-evidence-packs.md) should remain accurate after remediation. The [contract verification](contract-verification.md) review should consider the final PR state, not only the original PR body.

Review remediation is complete only when the final evidence still supports the issue contract and the PR still does only what was asked.
