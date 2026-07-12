# Complete your first small IssueOps change

This tutorial teaches the complete manual IssueOps loop through one low-risk documentation change.

You will create an issue, prove that it is ready, plan the implementation, make one file change, validate it, prepare a pull-request evidence pack, review it against the contract, merge it through human authority and verify the result after merge.

## What you will produce

In a personal fork or authorised training copy of IssueOps, you will add:

```text
docs/tutorials/exercise-result.md
```

with this exact content:

```md
# First IssueOps exercise

This training repository completed one documentation-only IssueOps delivery loop.
```

Do not create this exercise issue or file in the canonical `8ft0-ai/IssueOps` repository unless a maintainer has explicitly authorised it. A fork or disposable training repository lets you complete the full loop without adding exercise artefacts to the project.

## Before you start

You need:

- a GitHub account;
- a personal fork or authorised training copy of IssueOps;
- permission to create issues, branches and pull requests in that repository;
- permission for a human repository owner to merge the pull request;
- Git and Python available locally, or a repository-native documentation workflow that can run the strict build; and
- a clean `main` branch based on the current repository.

Clone your training repository and enter it:

```bash
git clone https://github.com/<your-account>/IssueOps.git
cd IssueOps
git switch main
git pull --ff-only
```

Replace `<your-account>` once with the owner of your fork.

**Expected outcome:** `git status --short` prints nothing and `git branch --show-current` prints `main`.

```bash
git status --short
git branch --show-current
```

If the working tree is not clean, stop and resolve or discard the unrelated work before continuing.

## 1. Create the execution-contract issue

Create one GitHub issue in the training repository with this title:

```text
Add the first IssueOps exercise result
```

Use this body:

```md
## Problem

The training repository does not yet contain evidence that a learner completed one documentation-only IssueOps delivery loop.

## Expected outcome

`docs/tutorials/exercise-result.md` exists with the exact tutorial completion text.

## Scope

- Add `docs/tutorials/exercise-result.md`.
- Use the exact content specified by the tutorial.

## Non-goals

- Do not change any existing documentation page.
- Do not change MkDocs navigation.
- Do not change workflows, scripts, tests or repository settings.
- Do not add automation or application code.

## Acceptance criteria

- The new file exists at the required path.
- Its content matches the tutorial exactly.
- The documentation site builds successfully with strict validation.
- The pull request contains only the bounded documentation change.

## Validation evidence expected

- Read the changed file back from the feature branch.
- Review the final diff.
- Run `mkdocs build --strict` locally or through the repository documentation workflow.
- Confirm no existing file changed.

## Change risk

Low. This is one new Markdown file in a training repository.

## Agent instructions

Keep the change to the single exercise file. Do not update navigation or infer additional improvements.
```

Record the issue number shown by GitHub. The examples below use `<issue-number>` as that value.

**Expected outcome:** the issue is open, its scope is one new file, and a contributor can understand the required result without this chat or any private context.

The exact field definitions remain in [Execution contracts](../execution-contracts.md).

## 2. Record readiness and dependencies

Before creating a branch, add this comment to the issue:

```md
## Planning readiness

- Expected outcome: add the exact exercise-result file defined by this issue.
- Scope boundaries: one new Markdown file; no existing page, navigation, workflow or setting changes.
- Acceptance criteria: explicit and directly reviewable.
- Validation expectations: file read-back, final diff review and strict MkDocs build.
- Change risk: low.
- Decision: Ready to implement.

## Dependency check

Required prior work:

- Issue/PR/release: None identified.
- Required state: Not applicable.
- Current state: Not applicable.

Safe starting point:

- Base branch or commit: latest clean `main` in the training repository.
- Reason this is safe: the issue is documentation-only and has no dependency on pending work.

Decision:

- Ready to implement.
```

**Expected outcome:** the repository record shows why the issue is executable and which starting point is safe.

If the expected file already exists or another open pull request adds it, change the decision to `blocked pending dependency` and stop. Do not create a branch for a known conflict.

See the current [operating protocol](../issueops-protocol.md) for the complete readiness and dependency rules.

## 3. Post the implementation plan

Add a second issue comment:

```md
## Implementation plan

Proposed branch:

- `feature/<issue-number>-first-exercise-result`

Safe starting point:

- latest clean `main` in the training repository.

Files expected to change:

- create `docs/tutorials/exercise-result.md`.

Implementation sequence:

1. Create the feature branch from `main`.
2. Add the exact tutorial completion text.
3. Read the file back and inspect the diff.
4. Run strict MkDocs validation.
5. Open a draft pull request with the evidence.

Validation:

- `cat docs/tutorials/exercise-result.md`
- `git diff --check`
- `mkdocs build --strict`

Post-merge verification:

- confirm the file exists on `main`;
- confirm the linked issue closed; and
- confirm the documentation workflow is not failing.

Explicit exclusions:

- no changes to existing files, navigation, workflows, scripts, tests or settings.
```

Replace `<issue-number>` with the real issue number before posting the comment.

**Expected outcome:** the later pull request can be checked against a specific branch, file list, sequence and validation plan.

## 4. Create the feature branch

Return to your local clone and refresh `main`:

```bash
git switch main
git pull --ff-only
git status --short
```

Confirm the exercise file does not already exist:

```bash
test ! -e docs/tutorials/exercise-result.md
```

Create the branch:

```bash
git switch -c feature/<issue-number>-first-exercise-result
```

Replace `<issue-number>` with the issue number.

**Expected outcome:** `git branch --show-current` prints the planned branch name, and `git status --short` remains empty.

```bash
git branch --show-current
git status --short
```

## 5. Make the bounded documentation change

Create the file exactly:

```bash
cat > docs/tutorials/exercise-result.md <<'EOF'
# First IssueOps exercise

This training repository completed one documentation-only IssueOps delivery loop.
EOF
```

Read it back:

```bash
cat docs/tutorials/exercise-result.md
```

Inspect the changed-file list and diff:

```bash
git status --short
git diff -- docs/tutorials/exercise-result.md
```

**Expected outcome:** the status contains only:

```text
?? docs/tutorials/exercise-result.md
```

and the file content matches the issue exactly.

If another file changed, stop and remove or separately account for that change. Do not hide unrelated work in this issue.

## 6. Validate the change

Install the documented dependencies when they are not already available:

```bash
python -m pip install -r requirements.txt
```

Run whitespace and strict documentation validation:

```bash
git diff --check
mkdocs build --strict
```

Read the file back once more after validation:

```bash
cat docs/tutorials/exercise-result.md
```

**Expected outcome:** both validation commands exit successfully and the generated site includes the page even though the exercise does not add it to canonical navigation.

The exact validation policy is in [Change-type validation](../change-type-validation.md) and [Repository-native validation](../repository-native-validation.md).

### When local validation is unavailable

Do not mark the strict build complete.

Commit and push only when the repository workflow can run the same documentation build. Open the pull request as a draft, record `Pending environment-specific validation`, and wait for the repository-native check. Do not merge while correctness depends on validation that has not run.

## 7. Commit and push

Commit only the exercise file:

```bash
git add docs/tutorials/exercise-result.md
git diff --cached --check
git diff --cached --name-only
git commit -m "Add first IssueOps exercise result"
git push -u origin feature/<issue-number>-first-exercise-result
```

**Expected outcome:** `git diff --cached --name-only` listed one file before the commit, and the branch is now available on GitHub.

## 8. Open a draft pull request

Open a pull request from the feature branch to `main`. Keep it as a draft until required validation is complete.

Use this body, replacing `<issue-number>` and the validation status:

```md
## Execution contract

Closes #<issue-number>

## Evidence pack

Changed:

- added `docs/tutorials/exercise-result.md` with the exact tutorial completion text.

Deliberately excluded:

- no existing page, navigation, workflow, script, test or setting changed.

Acceptance criteria:

- [x] required file exists;
- [x] content matches the issue;
- [x] diff contains only the bounded documentation change;
- [x] strict MkDocs build completed successfully.

## Validation status

- [x] changed file read back;
- [x] `git diff --check`;
- [x] `mkdocs build --strict`;
- [x] repository-native checks not failing.

Validation not performed or pending:

- None.

Post-merge verification required:

- confirm the file on `main`, issue closure and documentation workflow status.

## Risks and caveats

- Training-only documentation artefact; no runtime behaviour changes.

## Groundedness review

Did we do what was needed?

- Yes. The exact file requested by the issue was added and validated.

Did we only do what was asked?

- Yes. The final diff contains one new Markdown file.

Final recommendation:

- Approve.
```

When local validation was unavailable, leave the relevant checkboxes unchecked and state the exact pending repository-native check. Change the recommendation to `Do not approve yet` until it passes.

**Expected outcome:** the pull request explains the contract, final scope, validation evidence, caveats and remaining post-merge check without relying on the branch author's memory.

See [PR evidence templates](../pr-evidence-templates.md) for the reusable repository formats.

## 9. Verify the pull request against the issue

A human repository owner or authorised reviewer should inspect:

- the issue and its readiness, dependency and plan comments;
- the final changed-file list;
- the file content;
- the strict documentation check or repository workflow;
- PR comments, reviews and unresolved threads; and
- the final head commit.

The review asks two different questions:

1. Is the evidence present and trustworthy?
2. Does the result satisfy the issue without exceeding it?

**Expected outcome:** the reviewer can recommend `Approve` only when the one-file contract is satisfied, required validation passed and no material finding remains.

A self-review in a personal training fork is still a human decision, but it is not independent review. Record that honestly. Evidence and an agent-generated groundedness review do not themselves provide approval or merge authority.

Use [Contract verification](../contract-verification.md) for the current review procedure.

## 10. Remediate findings

When the reviewer identifies a problem, classify it before changing the branch:

- required fix;
- optional improvement;
- clarification needed; or
- out of scope.

Apply required fixes that belong to the issue. Do not add unrelated optional improvements to the exercise PR. Read the file back, rerun affected validation and update the evidence pack.

**Expected outcome:** no material finding or unresolved required thread remains, and the PR body reflects the final head.

See [PR review remediation](../review-remediation.md) for the complete handling rules.

## 11. Mark ready and merge through human authority

Once the final recommendation is `Approve` and checks are not failing, mark the pull request ready for review.

The human repository owner may then merge it using the repository's accepted merge method. Platform auto-merge may be enabled only when repository settings already support it; otherwise the authorised human merges directly after the gates pass.

Do not bypass branch protection, required review or repository permissions.

**Expected outcome:** GitHub records the pull request as merged and the closing keyword closes the issue.

If you do not have merge permission, your tutorial execution stops safely at a ready, fully evidenced pull request. Ask the repository owner to make the merge decision; do not change settings or find a bypass.

## 12. Perform post-merge verification

Refresh local `main`:

```bash
git switch main
git pull --ff-only
cat docs/tutorials/exercise-result.md
git log -1 --oneline
```

In GitHub, confirm:

- the pull request is merged;
- the issue is closed as completed;
- the merge commit is recorded;
- the documentation workflow on the merged state is not failing; and
- the file is visible on `main`.

Add a short post-merge comment to the pull request or issue recording those facts.

**Expected outcome:** the repository, rather than a private conversation, contains the complete contract, implementation, evidence, review, merge and verification trail.

## What you have learned

You completed the core IssueOps control loop:

```text
bounded issue
  -> readiness and dependency evidence
  -> implementation plan
  -> one-issue branch
  -> scoped mutation
  -> validation
  -> PR evidence pack
  -> human contract verification
  -> human merge decision
  -> post-merge verification
```

The controls are deliberately manual. The value is not the amount of ceremony; it is that intent, scope, evidence and authority remain visible at the points where an agent-assisted change could otherwise become ambiguous.

Continue with [How-to guides](../how-to/index.md) for task-specific procedures, [Reference](../reference/index.md) for exact rules and [Explanation](../explanation/index.md) for the design rationale.

## Maintainer walkthrough checklist

When this tutorial or its destinations change, validate it from a clean representative training repository:

- [ ] the learner knows to use a fork or authorised training repository;
- [ ] the starting branch and clean-state checks are unambiguous;
- [ ] the issue body is executable without hidden context;
- [ ] readiness, dependency and plan evidence precede branch creation;
- [ ] commands create only the specified file;
- [ ] local and repository-native validation paths stop safely when unavailable;
- [ ] the PR evidence body does not claim checks that did not run;
- [ ] human approval and merge authority remain explicit;
- [ ] the post-merge checks prove the merged repository state; and
- [ ] all linked pages and commands match the current repository.
