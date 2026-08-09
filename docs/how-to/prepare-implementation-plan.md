# Prepare an implementation plan

Use this guide after an issue is ready and its dependencies are satisfied, but before creating the feature branch.

For the reusable structure, use [Implementation-plan format](../reference/implementation-plan-format.md).

## 1. Re-read the ready contract

Review the issue, readiness comment and dependency check together. The plan must implement the approved outcome and boundaries rather than reinterpret them.

Confirm the exact safe starting commit before planning file changes.

## 2. Choose one branch

Propose one issue-specific branch using:

```text
feature/<issue-number>-short-description
```

Do not reuse a branch from another issue. Dependent work starts from the latest safe `main` after its prerequisite merges.

## 3. Predict the change surface

List the files or areas expected to change and why.

For content movement, schema changes, generated output or URL changes, include the intended compatibility or migration treatment. A broad phrase such as “update docs” is not specific enough for later scope review.

## 4. Describe the implementation sequence

Break the work into coherent steps that expose ordering and safety. Include where existing sources will be read, where canonical ownership changes and when generated output must be refreshed.

The sequence should be detailed enough to compare with the eventual pull request, but it should not copy the issue or prescribe low-level edits that repository inspection may legitimately adapt.

## 5. Name validation before implementation

Record:

- exact repository-native commands;
- changed-file read-back;
- manual or rendered observations;
- scope and contradictory-guidance checks;
- generated-output checks; and
- post-merge verification that cannot run earlier.

Validation belongs in the plan because it affects implementation design and the evidence required for approval.

## 6. State assumptions, caveats and exclusions

Write down any fact the plan relies on, including current repository settings, expected file ownership or environmental limits.

Repeat the exclusions most likely to attract scope drift. When the plan discovers missing intent, return to contract clarification instead of turning the assumption into an unapproved decision.

## 7. Post the plan on the issue

Post the complete plan as a new issue comment. Do not rewrite the original readiness evidence or hide later adaptation inside an edited historical comment.

**Expected result:** a reviewer can identify the proposed branch, safe base, predicted files, intended sequence, validation, post-merge checks and explicit exclusions before implementation begins.

The implementation plan is a proposed execution path. It is not self-authorising and does not itself permit branch creation or repository mutation.

## 8. Obtain durable human approval of the plan

After the plan is posted, obtain explicit human approval as a separate durable GitHub-native issue record before creating the branch or changing repository files.

The approval must clearly apply to the detailed implementation plan and must exist before the action it authorises. Do not edit the plan to make it appear self-approved and do not create retrospective authority after implementation has already begun.

If approval is withheld, qualified in a way that changes the planned scope, or replaced by a request for amendment, stop and update or re-plan before implementation.

## 9. Create the branch only after plan approval

Refresh the base state one final time after plan approval. If it still matches the dependency check and no conflicting work has appeared, create the planned branch.

If `main` changed materially or a new conflicting PR appeared, refresh readiness and the plan before branching. Obtain fresh approval when the material change alters the approved execution path.

## 10. Record material adaptation

Implementation may reveal a different safe path. Record a material adaptation in the issue or PR evidence pack, explain why it remained inside the contract and rerun validation affected by the change.

Do not rewrite the original plan to imply that later discoveries were known from the start.

A material adaptation that changes the approved execution path or authority boundary requires fresh human approval before the newly authorised work proceeds.

## Common failure modes

- creating the branch before the plan is posted and durably approved;
- treating the implementation plan as self-authorising;
- creating retrospective approval after implementation has begun;
- using a vague base such as “latest” without a reviewed commit;
- listing no expected files or compatibility decisions;
- treating post-merge verification as completed pre-merge validation;
- omitting exclusions that protect the issue boundary; or
- expanding the plan into new product or governance intent.
