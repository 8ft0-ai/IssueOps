# Why execution deviations are evidence

IssueOps treats an execution deviation as evidence about how delivery actually happened. That evidence should be preserved proportionately, but it should not automatically become a product bug, a new backlog item or a reason to abandon an otherwise sound change.

For the operating procedure, use [Handle an execution deviation](../how-to/handle-execution-deviation.md). For exact thresholds, classifications and resumption rules, use the canonical [Execution-deviation policy](../reference/execution-deviation-policy.md).

## A restored repository is not the same as an uneventful execution

An accidental branch can be deleted. An issue can be closed. A wrong-file commit can be reverted. Those actions may restore the repository state, but they do not make the earlier event disappear.

The event may still matter because it reveals:

- an authority boundary that was crossed;
- evidence that became stale;
- a recovery decision a reviewer must understand;
- a recurring execution weakness; or
- residual risk that is not visible in the final diff.

Recording the event preserves the difference between “nothing happened” and “something happened and was safely contained”.

## Evidence supports judgement; it does not dictate the outcome

A deviation record helps a reviewer decide whether the final change remains trustworthy. It does not automatically produce one conclusion.

A contained minor deviation may leave the implementation, scope and validation fully trustworthy after restoration and revalidation. A small-looking action may instead create material uncertainty about the head, approval or authority and therefore block progress.

The important question is not whether an error occurred. It is whether repository state, evidence and authority can be reconstructed confidently enough to support the next decision.

## Not every failed command is a meaningful deviation

Agent and tool-driven work includes harmless failures: a read command may use the wrong path, a search may return no results or a command may fail before changing anything.

Recording every such event as a formal incident would turn IssueOps into an activity log. It would add noise without improving review or safety.

The policy therefore focuses on failures that affect, or could reasonably affect, authoritative state, authority, scope, evidence, merge safety or repository integrity. Recurrence also matters because repeated harmless-looking failures may show that the execution path itself is unreliable.

## A deviation is not automatically a repository bug

A repository bug exists when repository code, configuration or documented behaviour is wrong.

An agent that selects `create_branch` when it intended to create an issue has not demonstrated a repository bug if the branch tool behaved exactly as documented. That is execution non-compliance or tool-selection failure. The local record should say so plainly.

A separate tooling defect is justified when the invoked operation behaves differently from its documented contract. A process issue is justified when the protocol lacks or ambiguously states a needed control. These sources may lead to different follow-up work even when the observed repository effect looks similar.

## Backlog items should represent unresolved work

A deviation record describes what happened in one delivery. A follow-up issue should describe an unresolved systemic problem worth changing.

Creating a separate issue for every accidental object duplicates evidence and pollutes the backlog. Creating no follow-up work when failures recur or controls are missing hides reusable lessons.

Proportionate escalation keeps those purposes separate:

- the active execution record preserves local evidence;
- the pull request explains effects on review and validation;
- a follow-up issue exists only when prevention, repair or policy improvement remains necessary.

## Severity is about impact and uncertainty

The initiating action does not determine severity by itself.

An empty branch created from the stable head may be minor when it is deleted, the state is verified and no evidence changed. A one-line settings mutation may be critical when it exposes credentials or changes production authority.

Classifying the observed impact and remaining uncertainty prevents both underreaction to dangerous small changes and overreaction to harmless reversible mistakes.

## Resumption should change the failing path

Stopping after a deviation is useful only when the next attempt is safer.

A corrective control should change the execution path: constrain the permitted action, verify the exact tool and target, require a different operator or environment after recurrence, or revise the plan. Merely restating the original intention does not address repeated selection failure.

This is why repeated minor deviations can become material. Their individual repository impact may remain small while their recurrence shows that the current control is not effective.

## Transparency protects human authority

Human approval depends on an accurate account of the final state and the path used to reach it.

Concealing a deviation deprives the reviewer of evidence about stale checks, recovery, residual risk or scope control. Overstating it as a repository defect also distorts the decision.

A factual, proportionate record lets the human reviewer distinguish:

- a complete and trustworthy recovery;
- a final implementation that still satisfies the contract;
- evidence that needs to be rerun;
- uncertainty that requires owner direction; and
- a systemic problem that warrants separate work.

## Canonical requirements

This explanation introduces no mandatory threshold, field, classification or resumption rule.

Use:

- [Execution-deviation policy](../reference/execution-deviation-policy.md) for normative rules; and
- [Handle an execution deviation](../how-to/handle-execution-deviation.md) for the task procedure.