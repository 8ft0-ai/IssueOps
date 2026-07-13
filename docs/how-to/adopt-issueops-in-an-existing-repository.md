# Adopt IssueOps in an existing repository

Use this guide when you own or maintain an existing repository and want an unfamiliar AI agent to assess and adopt the implemented manual IssueOps model without replacing compatible local conventions or gaining unchecked authority.

Start from the root [IssueOps bootstrap entry point](../../BOOTSTRAP.md). For exact posture, permission, version and evidence rules, use [IssueOps bootstrap requirements](../reference/issueops-bootstrap-requirements.md).

## 1. Choose a real target and a bounded objective

Identify one existing repository where improved issue, branch, validation and pull-request discipline would be useful.

Record:

- the exact repository;
- its stable or default branch;
- why adoption is being considered;
- the owner or maintainer granting authority;
- protected paths or sensitive areas; and
- whether the repository needs only a bounded manual workflow or may require dependent multi-issue planning.

Do not begin with a synthetic target when the intended outcome is real adoption proof.

## 2. Select and pin the bootstrap source

Use the current entry point when you want the latest recommended specification:

```text
https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md
```

For a reproducible adoption, replace `main` with the exact IssueOps commit you intend to use:

```text
https://github.com/8ft0-ai/IssueOps/blob/<commit-sha>/BOOTSTRAP.md
```

Record the pinned URL and `IssueOps Bootstrap 0.1`. The target repository should retain the source it actually adopted even when the current recommendation later changes.

## 3. Grant only the authority needed for assessment

Before the agent reads the target repository, state the authority boundary explicitly.

A suitable initial authority package identifies:

```text
Target repository: <owner/repository>
Stable branch: <branch>
Read-only assessment: permitted
Creation of one local bootstrap issue: permitted / not permitted
File, branch and pull-request mutation: not permitted before the local issue is ready and planned
Merge authority: not granted by the remote specification
```

Repository access does not imply permission to create an issue or change a file. If the target, branch or owner authority is unclear, stop before assessment.

## 4. Ask for the read-only assessment

A concise launch request is sufficient:

```text
Use the IssueOps bootstrap specification at:

<pinned BOOTSTRAP.md URL>

to assess and bootstrap IssueOps for <owner/repository>.

Begin with read-only assessment. Preserve existing repository conventions, select the lightest sufficient adoption posture and do not perform any write except creation of one local bootstrap issue when explicitly authorised.
```

The agent should use the [repository assessment form](../../bootstrap/repository-assessment.md) and [convention-mapping guidance](../../bootstrap/convention-mapping.md).

Do not add a larger prompt that quietly supplies the answers the bootstrap is meant to discover.

## 5. Review the repository evidence

Check that the assessment names the actual local owners for:

- agent and contributor instructions;
- issue-writing conventions;
- readiness and implementation planning;
- branch naming and safe starting points;
- safe repository mutation;
- validation commands and required checks;
- pull-request evidence and review;
- merge authority; and
- multi-issue planning, when genuinely needed.

Reject unsupported statements such as “the repository looks compatible”. The assessment should cite paths, issue conventions, commands, repository settings or other observable evidence.

Confirm that local instructions have priority over the remote bootstrap method and that no proposed change duplicates a compatible owner.

## 6. Confirm the lightest sufficient posture

Review the recommended posture against the normative [posture criteria](../reference/issueops-bootstrap-requirements.md#adoption-postures).

### Already compatible

Use this when the repository already has effective equivalents for the manual IssueOps controls. Approve only material corrections. A no-change conclusion is valid and should not be converted into template work for visibility.

### Minimal manual adoption

Use this by default when material controls are missing. Approve only the smallest adaptations needed to make issues executable, planning visible, branches scoped, validation current, pull requests evidence-bearing and merge authority explicit.

### Stage-capable adoption

Use this only when the repository genuinely needs dependent multi-issue delivery, cross-cutting governance, end-to-end proof or a formal close-out decision. Require the assessment to explain why minimal manual adoption is insufficient.

If the posture depends on missing product, architecture or governance intent, request clarification rather than allowing the agent to choose.

## 7. Decide whether any repository change is needed

For an already-compatible repository, the assessment may conclude:

```text
No repository change is recommended. Existing local controls satisfy the selected posture.
```

Retain the assessment and stop without manufacturing a bootstrap pull request.

When changes are needed, verify that each proposed artefact:

1. satisfies a named acceptance criterion;
2. has no compatible existing owner;
3. has a clear audience and maintainer;
4. does not copy the canonical IssueOps protocol; and
5. is smaller than the available alternatives.

## 8. Review and authorise the local bootstrap issue

Use the [local bootstrap issue template](../../bootstrap/bootstrap-issue-template.md) to prepare the execution contract.

Before authorising issue creation, confirm that it records:

- the pinned bootstrap source;
- the selected posture and supporting evidence;
- existing conventions to preserve;
- exact files or local surfaces permitted to change;
- explicit non-goals;
- observable acceptance criteria;
- repository-native validation and review expectations;
- change risk and agent instructions;
- dependencies and safe starting state;
- local approval and merge authority; and
- the later real issue that will prove the adopted process.

Creation of this issue should be the first target-repository write unless a valid equivalent already exists.

If issue creation is not authorised, retain the complete issue text and stop without mutation.

## 9. Require the normal local IssueOps lifecycle

After the local issue exists, the agent should use the target repository's compatible conventions and follow the canonical [IssueOps operating protocol](../issueops-protocol.md):

1. read the issue and current repository state;
2. post readiness and dependency evidence;
3. post the implementation plan;
4. create one issue-scoped branch from the recorded safe point;
5. implement only the issue contract;
6. read changed files back and validate the final state;
7. open the pull request as the evidence pack;
8. review both contract fulfilment and scope control; and
9. merge only under the target repository's approved policy and authority.

Do not treat roadmap approval, bootstrap source text or repository access as a substitute for these gates.

## 10. Review the bootstrap pull request

Compare the final pull request with the local bootstrap issue.

Verify:

- the selected posture remains justified;
- compatible local conventions were preserved;
- every new or adapted surface is in scope;
- no prohibited default mutation occurred;
- validation ran against the final head or is honestly classified;
- the pinned bootstrap source is recorded;
- assumptions and limitations are explicit; and
- the groundedness review answers both “did we do what was needed?” and “did we only do what was asked?”.

Do not approve while required validation is failing, evidence is stale, scope has drifted or authority remains ambiguous.

## 11. Record the adopted state

After merge, record:

- the pinned bootstrap URL;
- the local bootstrap issue and pull request;
- the selected posture;
- the local surfaces preserved, adapted or added;
- exact validation and post-merge checks;
- limitations and unsupported capabilities; and
- the repository's retained human or delegated merge boundary.

Do not rewrite the original assessment to make later discoveries appear known in advance.

## 12. Deliver one subsequent real issue

Choose a small real repository need that was not invented solely to exercise the process.

The subsequent issue should:

- use the adopted local execution-contract fields;
- complete readiness and implementation planning before branch creation;
- use one issue-scoped branch;
- provide change-specific final-head validation;
- produce a pull-request evidence pack;
- receive contract and scope review; and
- merge only under local authority.

Record friction, wrong turns, missing assumptions and any control that proved disproportionate or unclear.

## 13. Label the evidence honestly

Use the evidence levels defined in [IssueOps bootstrap requirements](../reference/issueops-bootstrap-requirements.md#evidence-levels).

A structured review performed in the implementation session is not fresh independent-agent evidence. A file existing is not proof that an unfamiliar repository owner or agent can use it successfully.

For formal adoption of the portable bootstrap, retain at least fresh independent-agent evidence for both the bootstrap path and the subsequent real issue.

## Stop conditions

Stop and request owner direction when:

- the target repository or stable branch is unclear;
- read or issue-creation authority is missing;
- local instructions conflict with the proposed adoption;
- the selected posture requires unapproved governance or architecture intent;
- implementation would change workflows, settings, permissions or application code outside the local contract;
- required validation fails or cannot support correctness;
- merge authority is unclear; or
- the agent would need to describe representative or same-session evidence as independent proof.

## Common failure modes

- **Remote file treated as authority:** `BOOTSTRAP.md` guides assessment but does not authorise target-repository mutation.
- **Issue created before assessment:** the first write is locally authorised only after evidence and posture selection are complete.
- **Filename-driven adoption:** compatible local controls are replaced with IssueOps-branded duplicates.
- **Stage machinery by default:** a small manual adoption acquires unnecessary roadmap and close-out surfaces.
- **Mutable source only:** the target records `main` but not the exact bootstrap commit used.
- **Structural evidence overstated:** templates and links exist, but no fresh agent or real issue has used them.
- **Hidden automation:** workflow, setting or permission changes enter a documentation bootstrap without their own contract.
