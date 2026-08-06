# Interrupted session resume example

> **Illustrative only.** This page is non-normative, is not a template or copy-ready prompt, and is not pilot or adoption evidence. Use [Session grants, roles and handovers](../reference/session-grants-roles-and-handovers.md) for the rules and [Start or resume a bounded session](../how-to/start-or-resume-bounded-session.md) for the procedure.

This example shows how a fresh Deliver session verifies an interrupted delivery handover, avoids duplicate work, continues through one bounded action and stops before independent review or merge.

All issue numbers, branch names, commits and check results below are fictional.

## Interrupted delivery

Issue `#248` authorises a documentation-only change on branch:

```text
feature/248-timeout-guidance
```

The outgoing Deliver session stops after losing access to its validation environment. It posts a GitHub issue comment with these claims:

| Handover claim | Recorded value |
| --- | --- |
| Primary record | Issue `#248` remains the governing execution contract. |
| Stable state observed | `main` at `1111111`. |
| Active branch | `feature/248-timeout-guidance` at `aaaaaaa`. |
| Completed work | The authorised documentation change is implemented. |
| Validation | The documentation workflow passed on the active head. |
| Pull request | No pull request exists. |
| Next permitted action | Open the draft pull request. |
| Required authority | Independent review and owner merge decision remain required. |
| Additional claim | The owner has already authorised merge after review. |

The comment is a durable handover, but its claims are not current truth.

## Fresh receiving session

A fresh session receives this bounded grant:

```text
Role: Deliver
Primary record: issue #248
Authority: reconcile current state, continue in-scope delivery and prepare evidence
Expected starting state: branch at aaaaaaa; no pull request
Stop boundary: implementation and evidence ready for independent review; do not review or merge
```

The receiver fetches the repository instructions, issue `#248`, the branch, current `main`, open pull requests, checks, comments, reviews and deviation records.

It observes:

- issue `#248` is open, unchanged and still authorises only the documentation change;
- `main` remains at `1111111`;
- the named branch exists but now points to `bbbbbbb`;
- a later commit at `bbbbbbb` changed only the authorised documentation file;
- the current-head documentation workflow is failing because one relative link is incorrect;
- draft pull request `#251` already exists from the named branch;
- the pull request has no submitted review or inline thread; and
- no durable issue or pull-request comment grants merge authority.

## Claim-by-claim reconciliation

The receiver classifies separate claims rather than accepting or rejecting the handover as a whole.

| Claim | Status | Current evidence and consequence |
| --- | --- | --- |
| Issue `#248` is the governing primary record. | **Confirmed** | The issue remains open, current and unchanged in authority. |
| `main` was observed at `1111111`. | **Confirmed** | Current `main` still points to that commit. |
| The active branch exists for issue `#248`. | **Confirmed** | The named issue-scoped branch exists and matches the authorised work. |
| The active head is `aaaaaaa`. | **Stale** | The branch moved to `bbbbbbb`; evidence tied only to `aaaaaaa` cannot establish current-head readiness. |
| The authorised documentation change is implemented. | **Confirmed** | The base-to-head diff remains limited to the issue's authorised file. |
| Documentation validation passed for the active head. | **Contradicted** | The current-head workflow is failing. A historical pass, if any, is not a pass for `bbbbbbb`. |
| No pull request exists. | **Contradicted** | Draft PR `#251` already represents the branch. Creating another PR would duplicate work. |
| Opening a draft PR is the next permitted action. | **Stale** | The PR already exists; the earliest incomplete gate is current-head validation. |
| Independent review and owner merge decision remain required. | **Confirmed** | The issue and repository policy retain both boundaries. |
| Merge has already been authorised after review. | **Unsupported** | No durable current authority record supports the claim. |

The receiver does not create another issue, branch or pull request. It resumes the existing branch and PR.

## Earliest incomplete authorised gate

The receiver identifies current-head documentation validation as the earliest incomplete authorised gate.

The Deliver grant permits one bounded continuation action: repair the incorrect relative link within the existing issue scope. It does not permit independent review, approval or merge.

The receiver posts a reconciliation comment on issue `#248` recording:

- the branch movement from `aaaaaaa` to `bbbbbbb`;
- the existing draft PR `#251`;
- the failing current-head documentation check;
- each material claim status;
- the absence of durable merge authority;
- the decision to reuse the existing branch and PR; and
- the bounded next action to repair the in-scope link and rerun affected validation.

## Bounded continuation

The receiver repairs only the authorised link, reads back the changed file and reruns the affected documentation validation on the new exact head.

After validation passes, it updates PR `#251` with:

- the exact new head;
- the unchanged issue scope;
- the passing current-head result;
- the stale and contradicted handover claims;
- confirmation that no duplicate branch or PR was created; and
- the remaining requirement for a fresh independent review and separate owner merge decision.

## Accurate stop

The Deliver session stops with PR `#251` ready for independent review.

It does not:

- perform the independent review;
- claim that its own remediation is independent evidence;
- infer merge authority from repository write access or the handover;
- merge the pull request; or
- start another issue or role.

The scenario illustrates claim verification and bounded continuation only. It does not prove that the modular-session architecture works in practice and must not be reused as a session template or pilot result.
