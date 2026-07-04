# Agentic IssueOps workflow

Stage 1 establishes a manual IssueOps flow for agentic coding with Codex.

This is not a general governance workflow for access requests, policy exceptions or operational approvals. It is a delivery model for using an agentic coding tool safely in a repository.

The central idea is that the issue is the execution contract. It defines what Codex may do, what it must not do, how success will be judged and what evidence the pull request must provide.

The pull request is the evidence pack. It should not merely describe the diff. It should show whether the contract was fulfilled, whether the boundaries were respected and what validation supports the result.

See [`docs/examples`](examples/README.md) for example execution contracts and contract verification reviews.

## Stage 1 boundary

Stage 1 is manual by design.

It includes:

- a structured execution-contract issue form;
- a readiness check before implementation starts;
- an implementation plan before file changes begin;
- one branch per issue;
- Codex-assisted implementation within the contract;
- a draft pull request as the evidence pack;
- contract verification before approval; and
- explicit human approval before merge.

It does not include:

- automatic Codex execution;
- auto-merge;
- branch protection changes;
- required status checks;
- GitHub Actions orchestration; or
- application code.

## Operating model

```text
Issue = execution contract
Readiness check = contract check
Implementation plan = proposed execution path
Codex = contract-bound implementer
Pull request = evidence pack
Human review = contract verification
Merge = human approval decision
```

## 1. Define the execution contract

Every change starts with an issue. The issue must be specific enough that a human reviewer can understand the intent and Codex can implement without inventing missing product or engineering decisions.

A good execution contract defines:

- the problem;
- the expected outcome;
- the included scope;
- explicit non-goals;
- acceptance criteria;
- expected validation evidence;
- change risk; and
- instructions for Codex, including anything the agent must not infer.

If the issue is vague, implementation should not begin. A weak contract should be clarified before Codex starts work.

## 2. Check the contract is executable

Before implementation, the issue should be checked for readiness.

The readiness check asks:

- Is the expected outcome clear?
- Are the boundaries explicit?
- Are the acceptance criteria reviewable?
- Is the expected validation evidence clear?
- Is there enough context for Codex to act without guessing?
- Is the work small enough to review safely?

If the answer is no, refine the issue rather than starting the branch.

## 3. Record the proposed execution path

When the contract is ready, record the implementation plan before changing files.

The plan should state:

- the branch name;
- the files expected to change;
- the intended sequence of work;
- the validation to perform;
- the work explicitly left out; and
- any assumptions or caveats.

This step makes the agent's proposed path visible before implementation.

## 4. Create one branch per contract

Create one branch from `main` for each issue.

Preferred branch format:

```text
feature/<issue-number>-short-description
```

Do not commit directly to `main` unless the repository owner explicitly requests a bootstrap exception or hotfix.

## 5. Execute the contract with Codex

Codex is the preferred implementation agent.

Codex should execute the contract, not reinterpret it. It should make the smallest change that satisfies the issue and should avoid unrelated refactoring, speculative improvements or future-stage automation unless the contract asks for them.

The agent should stop or surface a caveat when the contract is incomplete, contradictory or impossible to validate in the current environment.

## 6. Create the evidence pack

Open a draft pull request while the work is still being reviewed or validation remains incomplete.

The pull request should show:

- the linked execution contract;
- what changed;
- what was deliberately excluded;
- how the acceptance criteria were satisfied;
- what validation evidence exists;
- what remains unchecked; and
- any assumptions, risks or caveats.

## 7. Verify the contract

Before approval, review the pull request against the issue contract.

The review is not asking whether the change looks reasonable in isolation. It is asking whether Codex fulfilled the contract and stayed inside it.

The reviewer should answer:

- Did the PR satisfy the acceptance criteria?
- Did the PR avoid unrelated or speculative changes?
- Is the validation evidence sufficient for this stage?
- What uncertainty remains?

Use one final recommendation:

- Approve
- Approve after minor fixes
- Do not approve yet

Do not recommend approval if validation is misleading, the implementation is incomplete or the scope has drifted.

## 8. Own the merge decision

A human owns the final approval and merge decision.

The agent can produce the change and the evidence pack, but the human decides whether the contract was fulfilled and whether the repository should accept the result.

## Stage 1 success criteria

Stage 1 is successful when the repository can demonstrate this loop manually:

1. A human writes an execution contract.
2. The contract is checked before implementation.
3. Codex implements within the contract.
4. The pull request provides the evidence pack.
5. A human verifies the contract and decides whether to merge.
