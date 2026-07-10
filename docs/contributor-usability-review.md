# Stage 2 contributor usability review

This review walks the current Stage 2 process as a first-time contributor completing a small, low-risk repository change. It records concrete usability findings and the bounded improvements made during Stage 2 close-out.

## Walkthrough

### 1. Select an issue

The issue must be an execution contract with a clear outcome, scope, non-goals, acceptance criteria, validation expectations and change risk.

**Finding:** the contract model is clear and consistently described. No control change is required.

### 2. Check readiness and dependencies

Before creating a branch, post a readiness comment that confirms the issue is executable, identifies dependencies and records a safe starting point.

**Finding:** the readiness and dependency rules are clear in the canonical operating protocol, although the detailed examples make the page long. The examples remain useful reference material and should not be removed merely to shorten the page.

### 3. Post the implementation plan

Record the branch name, expected files, implementation sequence, validation, assumptions and exclusions before implementation begins.

**Finding:** the required content is clear and does not materially duplicate the issue contract because it describes the execution path rather than the requested outcome.

### 4. Create the branch and mutate safely

Create one branch per issue, then use the safe tool-operation check before repository mutations.

**Finding:** the safe-operation control is valuable, but contributors need an easy way to distinguish the compact format for routine low-risk work from the full format for ambiguous or high-risk operations. The canonical protocol now points contributors directly to the compact evidence path.

### 5. Implement only the contract

Make the smallest change that satisfies the issue and avoid unrelated refactoring or future-stage work.

**Finding:** scope language is consistent across the protocol and evidence guidance. No terminology conflict was found.

### 6. Select and run validation

Choose validation by change type, prefer repository-native evidence and record unavailable checks honestly.

**Finding:** the specialised validation pages are useful, but a first-time contributor must decide which page to open. The canonical protocol now provides a small-change path that directs contributors to change-type guidance first, then repository-native validation and workflow-specific review only when applicable.

The Stage 2.20 and Stage 2.21 runs also exposed a practical workflow gap: branch validation was initially manual and attempted production deployment. PR #61 corrected this by adding automatic pull-request validation and restricting deployment to `main`.

### 7. Open the pull request as an evidence pack

The PR should record scope, exclusions, acceptance evidence, validation, caveats and the pre-approval groundedness review.

**Finding:** the full evidence requirements are clear, while compact templates are easy to miss. The canonical protocol now links directly to the PR evidence templates as the starting point for routine changes, without weakening the full evidence requirements.

### 8. Review, remediate and merge

Review against the issue contract, classify feedback, rerun affected validation after material remediation and merge only after human approval.

**Finding:** review and remediation terminology is consistent. These specialised pages remain appropriate because they apply after feedback is received rather than to every small change.

### 9. Complete post-merge verification when required

Publishing, release and environment-specific changes may require evidence after merge.

**Finding:** applicability is clear, but contributors must avoid treating a skipped PR deployment as a failure. Pull requests should validate the build and skip production deployment; the push to `main` performs deployment.

## Changes made from this review

- The home page now directs contributors to the canonical Stage 2 operating protocol rather than the older Stage 1 workflow.
- The canonical protocol now includes a first-time contributor path for small changes.
- Compact safe-operation and PR evidence formats are linked directly from that path.
- This review is included in the documentation navigation as a Stage 2 project record.

## Findings deliberately not actioned

- The canonical protocol is long, but its detailed readiness and dependency examples are useful and were not removed without evidence that they cause unsafe duplication.
- Specialised pages were not consolidated solely to reduce page count; they remain focused references for validation, workflow changes, remediation and evidence.
- No new taxonomy, automation, required checks or Stage 3 design was introduced.

## Stage 3 follow-up boundary

Possible future improvements such as generated contributor checklists, automated evidence collection or required status checks belong to separately scoped Stage 3 issues. They are not Stage 2 close-out changes.