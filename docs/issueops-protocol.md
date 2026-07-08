# IssueOps operating protocol

This page defines the canonical operating protocol for this repository's manual IssueOps workflow.

The protocol is an execution contract for the process itself. It describes how an issue becomes a bounded repository change, how the pull request becomes the evidence pack and how a human reviewer decides whether the change should merge.

This protocol is deliberately manual. It does not add automatic Codex execution, auto-merge, branch protection, required status checks or application code. Any future automation should be introduced through its own issue contract, implementation plan, validation evidence and human review.

## Protocol boundary

The protocol applies to repository changes made through GitHub issues and pull requests.

It is designed for agent-assisted implementation, especially with Codex, where the repository needs visible controls around intent, scope, validation and review.

The source of truth is the repository record:

- the issue defines the execution contract;
- the readiness comment records whether the contract is executable;
- the implementation-plan comment records the proposed path;
- the branch contains the implementation;
- the pull request carries the evidence pack;
- the review records contract verification; and
- the merge records the human acceptance decision.

## Lifecycle

### 1. Create or select an issue contract

Every change starts with a GitHub issue.

The issue should state the problem, expected outcome, scope, non-goals, acceptance criteria, validation evidence expected and change risk. If the issue does not contain enough information for a contributor or agent to implement safely, implementation should not begin.

See [Execution contracts](execution-contracts.md) for the required contract shape.

### 2. Check readiness before implementation

Before a branch is created, the issue should receive a readiness comment.

The readiness comment should confirm that:

- the expected outcome is clear;
- the boundaries are explicit;
- the acceptance criteria are reviewable;
- the validation evidence is clear;
- the work is small enough to review safely;
- dependencies or ordering constraints have been considered; and
- the issue can be implemented without inventing missing intent.

If the issue is unclear, the correct action is to post a clarification comment, not to create a branch.

### 3. Post the implementation plan

If the issue is ready, post an implementation-plan comment before changing files.

The plan should record:

- the proposed branch name;
- the files or documentation areas expected to change;
- the intended sequence of work;
- the validation to perform;
- any assumptions or caveats; and
- the work explicitly left out.

This makes the execution path visible before implementation starts.

### 4. Create one branch per issue

Create one feature branch from `main` for the issue.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

Do not commit directly to `main` unless the repository owner explicitly asks for a hotfix or bootstrap exception.

### 5. Check tool operations before mutation

Before any mutating repository operation, perform the safe tool-operation check.

At minimum, identify:

- current phase;
- intended operation;
- selected tool;
- target repository object;
- expected side effect; and
- forbidden side effects.

If the selected tool does not match the intended operation, stop before making the call.

See [Safe tool operations](tool-operations.md) for the detailed protocol.

### 6. Implement only the contract

The implementation should make the smallest change that satisfies the issue.

Do not add unrelated refactoring, broad rewrites, speculative future-stage automation, branch protection, auto-merge, new workflows or application code unless the issue explicitly asks for them.

When the issue is incomplete, contradictory or impossible to validate in the current environment, surface the caveat rather than silently guessing.

### 7. Validate and record evidence

Validation should match the change type and the issue contract.

For documentation changes, useful evidence includes:

- changed files read back from the branch;
- MkDocs navigation checked;
- internal links checked by inspection or build output;
- `mkdocs build --strict` run with the pinned documentation dependency; and
- confirmation that no unrelated automation or application code was introduced.

If validation cannot be completed, record it honestly as pending or not performed. Do not mark validation complete unless it actually ran.

See [Local MkDocs validation](local-validation.md) for the current documentation-site validation path.

### 8. Open the pull request as the evidence pack

The pull request should allow a reviewer to verify the change against the issue without relying on chat history or memory.

The PR should include:

- the linked issue contract;
- what changed;
- what was deliberately excluded;
- how the acceptance criteria were satisfied;
- validation performed;
- validation not performed or still pending;
- assumptions, risks and caveats; and
- a pre-approval groundedness review.

See [Pull requests as evidence packs](pr-evidence-packs.md) for evidence-pack guidance.

### 9. Review against the contract

Human review should compare the PR evidence pack with the issue contract.

The reviewer should ask:

1. Did the pull request do what was needed?
2. Did the pull request only do what was asked?

The review should check issue alignment, scope control, validation evidence, risks and caveats.

Use one final recommendation:

- Approve
- Approve after minor fixes
- Do not approve yet

See [Contract verification](contract-verification.md) for the review model.

### 10. Remediate review feedback inside the contract

When review feedback is received, classify it before making changes:

- required fix;
- optional improvement;
- clarification needed; or
- out of scope for the issue.

Apply required fixes within the existing contract. Do not broaden the work during remediation unless the repository owner explicitly approves the scope change or a new issue is created.

After remediation, read changed files back, rerun available validation, reply to addressed comments and resolve review threads only when the fix is present.

Detailed remediation guidance is planned as follow-up work.

### 11. Merge only after human approval

The agent can implement the contract and prepare the evidence pack, but a human owns the approval and merge decision.

Do not merge while required validation is failing, the implementation is incomplete, the scope has drifted or the PR does not satisfy the issue contract.

### 12. Track post-merge verification when needed

Some work cannot be fully validated before merge. Publishing, release and environment-specific changes may need post-merge verification.

When that happens, the PR should distinguish:

- validation completed before merge;
- validation that remains pending after merge; and
- the specific post-merge checks required.

Post-merge validation should be recorded rather than ignored. Detailed post-merge validation guidance is planned as follow-up work.

## Compact checklist

Use this checklist before asking for review:

- [ ] Issue contract is clear and bounded.
- [ ] Readiness comment is posted.
- [ ] Implementation-plan comment is posted.
- [ ] Feature branch follows `feature/<issue-number>-short-description`.
- [ ] Safe tool-operation checks were used before repository mutations.
- [ ] Implementation stays inside scope and non-goals.
- [ ] Changed files were read back from the branch.
- [ ] Relevant validation was completed or clearly recorded as pending.
- [ ] Pull request explains changed scope, exclusions, validation and caveats.
- [ ] Pre-approval groundedness review answers whether the PR did what was needed and only what was asked.
- [ ] Post-merge verification needs are recorded if they exist.

## Relationship to existing docs

This page is the canonical process overview. The focused pages remain the detailed references:

- [Agentic IssueOps workflow](issueops.md) explains the Stage 1 workflow baseline.
- [Execution contracts](execution-contracts.md) explains how to write agent-ready issues.
- [Pull requests as evidence packs](pr-evidence-packs.md) explains PR evidence expectations.
- [Contract verification](contract-verification.md) explains human review.
- [Safe tool operations](tool-operations.md) explains repository mutation safety.
- [Local MkDocs validation](local-validation.md) explains documentation-site validation.
- [Publishing the documentation site](publishing.md) explains the GitHub Pages workflow and manual Pages setting.

## Current manual boundary

The current baseline remains deliberately manual.

It includes documentation, readiness checks, implementation plans, safe tool-operation checks, branch discipline, evidence-pack PRs, validation records and human review.

It does not include automatic Codex execution, auto-merge, branch protection changes, required status checks for agent work or application code.
