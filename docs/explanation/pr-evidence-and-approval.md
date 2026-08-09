# Why evidence is not approval

IssueOps describes the pull request as an evidence pack because review needs more than a diff. The reviewer needs the authorising issue, the final scope, the validation record, the known limitations and the relationship between the implementation and the contract.

That evidence improves the decision. It does not make the decision automatically.

## The pull request connects implementation to intent

The issue states what was needed and what was forbidden. The branch contains the proposed implementation. The pull request gathers the evidence needed to compare them.

A useful evidence pack answers:

- What changed?
- What was deliberately excluded?
- Which acceptance criteria are satisfied?
- Which validation ran against the final state?
- What remains pending or can run only after merge?
- What risks, assumptions or caveats remain?

This makes review reproducible from the repository record rather than dependent on chat history or memory.

## Evidence presence and contract satisfaction are different

A pull request may contain complete evidence that shows the implementation is wrong, incomplete or outside scope. The evidence pack has still done its job: it made the mismatch visible.

A different pull request may appear to satisfy the issue but lack trustworthy validation or a current final-diff review. The implementation may be plausible, but approval would require guessing.

The human reviewer therefore asks two separate questions:

1. Is the evidence current, complete enough and trustworthy?
2. Does the final implementation satisfy the execution contract without exceeding it?

Neither answer can be replaced by a green status icon alone.

## Why collection is deliberate rather than automatic

IssueOps uses evidence collection as an intentional review aid, not as an automatic lifecycle event. An authorised session requests a snapshot when the governing issue/session grant permits that action and when the snapshot is useful to the decision being made.

That keeps two kinds of authority separate. IssueOps procedural authority answers whether the session is allowed to request collection for this review. GitHub platform eligibility answers whether the repository workflow will accept the request from that actor. Effective repository `write` or `admin` permission can satisfy the platform check, but it does not by itself authorise an IssueOps session to act.

This separation matters because repository access is broader than the process decision to invoke a particular governed action.

## Why the collector is still read-only assistance

Posting the request comment is a deliberate repository mutation by the already-authorised IssueOps session. The evidence collector itself remains read-only with respect to repository and lifecycle state.

The repository-owned workflow reads the target pull request and related GitHub evidence under explicit read permissions, then writes generated output only to the workflow run summary and short-lived Actions artifact surfaces. It does not edit the issue, pull request, review state, branch, commits, files, merge state or repository settings.

Keeping the request action and the collector's authority distinct prevents a convenient invocation path from quietly becoming a mutation or decision engine.

## Correlation improves reproducibility, not authority

The request comment, workflow run, run attempt, summary and artifact form a traceable evidence lineage. That lineage helps a later reviewer reconstruct which request produced which repository observations and whether the result was terminal, pending or stale.

Traceability makes evidence easier to verify. It does not elevate a generated observation into a conclusion about contract satisfaction or approval. A perfectly correlated evidence pack can still reveal a blocker, an unresolved risk or an implementation outside scope.

## Repository observations and assertions

Some evidence is observed directly from the repository: file contents, commits, diffs, workflow results, review threads and generated artefacts.

Other content is an assertion by the contributor or agent: why the change was made, what was excluded, which caveat matters and how the acceptance criteria were interpreted.

Assertions are useful, but they require review. An evidence pack should not make an inference look like a repository fact.

## Why submitted reviews and inline threads stay separate

A submitted review state and an inline review thread answer different questions. A review may be submitted as `APPROVED`, `COMMENTED` or with requested changes, while individual inline threads have their own resolved or unresolved state.

Collapsing those surfaces would turn one repository observation into an inference about another. The evidence pack therefore keeps them separate so the human reviewer can decide whether the underlying findings were substantively addressed rather than assuming that a review count or state proves thread resolution.

## Why recollection is a new snapshot, not lifecycle progression

Pull requests change during review. A new commit, rerun validation, remediation or changed review state can make an earlier evidence snapshot no longer representative of the next decision.

When current authority permits it, requesting collection again creates a fresh snapshot tied to the newer repository state. It does not approve remediation, resolve findings, mark the pull request ready, or advance the lifecycle automatically.

This is the same reason evidence must be refreshed after material remediation: approval applies to the decision-relevant final state, not to the fact that evidence was collected at some earlier point.

## Groundedness review

The pre-approval groundedness review asks whether the implementation did what was needed and only what was asked. It is a structured self-check that makes scope and evidence reasoning visible.

When an agent writes that review, it remains agent-generated analysis. It is not an independent human GitHub review, and it cannot grant itself approval or merge authority.

A human may use the analysis, verify it and make the decision.

## Human authority remains necessary

Approval includes judgement that cannot be reduced safely to evidence collection alone:

- whether the issue outcome was interpreted correctly;
- whether review findings were substantively resolved;
- whether validation is sufficient for the changed behaviour and risk;
- whether the residual risk is acceptable;
- whether a scope adaptation remained faithful to intent;
- whether post-merge verification is legitimately deferred; and
- whether the change should enter the stable branch now.

Repository-owner delegation may authorise an agent to continue through routine issue and merge operations after every gate passes. That delegation changes who performs the mechanics, not what qualifies as evidence or who owns the approval authority.

## Why post-merge verification exists

Some facts cannot be observed before merge, such as a production-only deployment or an environment setting applied after the branch enters `main`.

Recording those checks separately prevents two opposite errors:

- pretending that unavailable evidence already exists; and
- blocking a complete, validated implementation on a check that genuinely cannot run earlier.

Post-merge verification is not a general escape hatch. Any test or review that can determine correctness before merge remains pre-merge evidence.

## Why remediation must refresh the evidence pack

Review changes the proposed implementation. When remediation affects scope, validation, permissions, public claims, dependencies, review state or residual risk, the earlier evidence pack may no longer describe the final head and decision context.

Updating the evidence is part of the fix because approval applies to the final state, not the original submission.

## Canonical requirements

This explanation introduces no hidden recommendation or blocker.

Use:

- [Pull-request evidence requirements](../reference/pr-evidence-requirements.md) for exact linkage, collection and evidence rules;
- [PR evidence templates](../reference/pr-evidence-templates.md) for reusable formats;
- [Review decisions and merge blockers](../reference/review-decisions-and-merge-blockers.md) for the normative vocabulary;
- [Prepare a pull-request evidence pack](../how-to/prepare-pr-evidence-pack.md) for contributor preparation; and
- [Review a pull request against its contract](../how-to/review-pr-against-contract.md) for the review procedure.
