# IssueOps operating protocol

This page is the authoritative lifecycle and gate map for the repository's manual IssueOps workflow. It explains how an executable issue becomes a bounded repository change, how the pull request carries evidence and how a human decides whether the change may merge.

Use the focused documentation for detail:

- [Tutorials](tutorials/index.md) teach the workflow through a guided experience.
- [How-to guides](how-to/index.md) explain how to complete a specific task.
- [Reference](reference/index.md) defines exact fields, formats, permissions, validation rules and decision vocabulary.
- [Explanation](explanation/index.md) describes the model, rationale and authority boundaries.

This protocol is deliberately manual. It does not authorise automatic agent execution, automatic lifecycle transitions, required status checks, branch-protection changes, auto-merge configuration or autonomous approval and publication decisions. Any such change requires its own planning and execution contracts, validation evidence and human review.

## Protocol boundary

The protocol applies to repository changes implemented through GitHub issues, branches and pull requests.

The repository record is the source of truth:

- the issue defines the execution contract;
- the readiness comment records whether the contract is executable and identifies a safe starting point;
- the implementation-plan comment records the proposed execution path;
- the feature branch contains the implementation;
- the pull request carries the evidence pack;
- review records contract verification and remediation; and
- merge records the human acceptance decision.

Labels are optional visibility aids and never replace written evidence. See [Manual lifecycle labels](labels.md).

## Lifecycle

### 1. Create or select an issue contract

Every implementation change starts with a GitHub issue that is specific enough to execute without inventing missing product, engineering or repository-policy intent.

At minimum, the contract defines the problem, expected outcome, scope, non-goals, acceptance criteria, expected validation evidence and change risk. Conditional fields and agent instructions should be included when the work requires them.

Use [Write an executable issue contract](how-to/write-executable-issue.md) for the task and [Execution-contract fields](reference/execution-contract-fields.md) for the exact requirements.

### 2. Check readiness before implementation

Before creating a branch, refresh relevant repository state and post a readiness decision.

The readiness check must confirm that:

- the expected outcome and boundaries are clear;
- the acceptance criteria are reviewable;
- validation expectations are explicit;
- the work is small enough to review safely;
- dependencies and ordering constraints have been checked;
- a safe base branch or commit has been identified; and
- implementation can proceed without guessing.

If the contract is unclear or a blocking dependency is unsatisfied, post a clarification or blocked-dependency comment and do not create a branch.

Use [Check readiness and dependencies](how-to/check-readiness-and-dependencies.md) for the procedure and [Readiness and dependency formats](reference/readiness-and-dependency-formats.md) for the exact comment structures and decisions.

### 3. Post the implementation plan

When the issue is ready, post the implementation plan before creating the branch or changing files.

The plan must make the proposed branch, safe starting point, likely files or areas, implementation sequence, validation, assumptions, caveats and explicit exclusions visible before execution begins.

Use [Prepare an implementation plan](how-to/prepare-implementation-plan.md) and the [Implementation-plan format](reference/implementation-plan-format.md).

### 4. Create one branch per issue

Create one feature branch for the issue from the recorded safe starting point.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

Do not commit directly to `main` unless the repository owner explicitly authorises a hotfix or bootstrap exception. Dependent work must begin from the final merged state of its prerequisite work rather than from a stale parallel branch.

### 5. Check tool operations before mutation

Before every mutating repository operation, verify the current phase, intended operation, exact tool, target, expected side effect and forbidden side effects.

If the tool or target does not match the intended operation, stop before making the call. If an unintended mutation occurs, stop further writes except for minimum remediation, report the event and do not resume normal execution without appropriate authority.

Use [Perform a safe repository mutation](how-to/perform-safe-repository-mutation.md) for the procedure and [Operation permissions and evidence](reference/operation-permissions-and-evidence.md) for phase permissions, evidence formats and the circuit breaker.

### 6. Implement only the contract

Make the smallest coherent change that satisfies the issue.

Do not add unrelated refactoring, speculative improvements, future-stage work, new automation, permission changes, branch-protection changes, repository-setting changes or application code unless the contract explicitly includes them.

When the issue becomes contradictory, incomplete or unsafe to validate, surface the caveat and stop or narrow the work rather than silently expanding intent.

### 7. Validate and record evidence

Validation must match the change type, risk and acceptance criteria. Record what actually ran, what did not run and what remains pending.

Required principles:

- prefer repository-native evidence when available;
- never mark an unavailable or unrun check complete;
- distinguish pre-merge validation from legitimate post-merge verification;
- treat failing required validation as a merge blocker;
- apply documentation-currency checks when factual repository claims change; and
- rerun affected validation after material remediation.

Use [Validation by change type](reference/validation-by-change-type.md) to select required evidence and [Validation status and fallback policy](reference/validation-status-and-fallback-policy.md) to classify repository-native, representative, pending and post-merge evidence. Task-specific procedures are available for [documentation changes](how-to/validate-documentation-change.md), [workflow changes](how-to/validate-workflow-change.md) and [publishing](how-to/publish-and-verify-documentation-site.md).

### 8. Open the pull request as the evidence pack

Open a draft pull request while implementation, validation or evidence remains incomplete.

The final evidence pack must allow a reviewer to compare the pull request with the issue without relying on chat history or memory. It records:

- the linked execution contract;
- what changed and what was deliberately excluded;
- how the acceptance criteria were satisfied;
- validation completed, unavailable or pending;
- post-merge verification, if any;
- assumptions, risks and caveats; and
- a groundedness review answering whether the PR did what was needed and only what was asked.

Use [Prepare a pull-request evidence pack](how-to/prepare-pr-evidence-pack.md), [Pull-request evidence requirements](reference/pr-evidence-requirements.md) and [PR evidence templates](reference/pr-evidence-templates.md).

### 9. Review against the contract

Review compares the final pull-request state and evidence with the issue contract. It is not merely a judgement of whether the diff looks reasonable in isolation.

The reviewer must determine:

1. Did the pull request do what was needed?
2. Did the pull request only do what was asked?

Review must consider issue alignment, scope control, validation, remaining checks, risks and caveats. Use one final recommendation:

- **Approve**
- **Approve after minor fixes**
- **Do not approve yet**

Required validation failures, incomplete implementation, unresolved material findings, misleading evidence and scope drift block approval and merge.

Use [Review a pull request against its contract](how-to/review-pr-against-contract.md) and [Review decisions and merge blockers](reference/review-decisions-and-merge-blockers.md).

### 10. Remediate review feedback inside the contract

Collect pull-request conversation comments, submitted reviews and inline review threads. Classify each finding before changing files.

Required fixes must be addressed within the contract. Optional improvements may be applied only when they remain small and in scope. Clarification must be resolved before acting, and out-of-scope work must be deferred or separately authorised.

After material remediation, read changed files back, rerun affected validation, refresh the evidence pack, reply to findings and resolve threads only when the fix is present and validation is not failing.

Use [Remediate pull-request review feedback](how-to/remediate-review-feedback.md) and [Review decisions and merge blockers](reference/review-decisions-and-merge-blockers.md).

### 11. Merge only after human approval

The agent may implement the contract and prepare evidence, but a human owns approval and merge authority.

Do not merge while required validation is failing, the implementation is incomplete, material review findings remain unresolved, the evidence pack is stale or the change does not satisfy the issue contract.

Explicit owner-authorised delegated batch mode may remove routine per-PR confirmation, but it does not remove readiness, validation, groundedness, review or merge-qualification gates. See [Delegated batch mode](delegated-batch-mode.md).

### 12. Track post-merge verification when needed

Some evidence can only be collected after merge, deployment, release or environment-specific configuration.

When post-merge verification is legitimate, the PR must identify the exact remaining checks and the reviewer must explicitly accept the residual risk. After merge, record the result on the pull request, issue or appropriate project record. Do not silently treat a pending check as complete.

Use [Validation status and fallback policy](reference/validation-status-and-fallback-policy.md) for the boundary and [Publish and verify the documentation site](how-to/publish-and-verify-documentation-site.md) for the documentation publishing path.

## Compact checklist

Use this lifecycle checklist before requesting final review:

- [ ] The issue contract is clear, bounded and reviewable.
- [ ] Readiness, dependencies and the safe starting point are recorded.
- [ ] The implementation plan was posted before branch creation.
- [ ] One issue-scoped feature branch was used.
- [ ] Safe-operation checks preceded repository mutations.
- [ ] The implementation stayed inside scope and non-goals.
- [ ] Changed files were read back.
- [ ] Validation matched the change type and actually ran as recorded.
- [ ] Pre-merge and post-merge evidence are distinguished honestly.
- [ ] The pull request records scope, exclusions, evidence and caveats.
- [ ] Review considered the final head and all material findings.
- [ ] The groundedness review answers both contract questions.
- [ ] The final recommendation is supported by evidence.
- [ ] Merge occurs only under human approval or explicit bounded owner delegation after all gates pass.
- [ ] Required post-merge verification is recorded and completed.

## Relationship to focused documentation

This page owns the lifecycle sequence, mandatory gates and authority boundary. It does not own exhaustive procedures, reusable templates, validation matrices or conceptual rationale.

- [Tutorials](tutorials/index.md) provide guided learning.
- [How-to guides](how-to/index.md) own task procedures.
- [Reference](reference/index.md) owns normative fields, formats, permissions, evidence and decision rules.
- [Explanation](explanation/index.md) owns rationale and trade-offs.
- [Examples](examples/README.md) illustrate artefacts but are not normative.
- [Planning records](https://github.com/8ft0-ai/IssueOps/blob/main/planning/README.md) preserve stage intent, delivery evidence and historical project records outside the substantive Diátaxis tree.

The central contract remains unchanged: the issue bounds the work, the pull request carries evidence and a human retains approval and merge authority.