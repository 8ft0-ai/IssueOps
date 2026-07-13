# Bootstrap IssueOps in an existing repository

Specification: **IssueOps Bootstrap 0.1**

Use this file to assess whether an existing repository can adopt the implemented manual IssueOps model and to prepare the first locally governed bootstrap issue.

This file is an entry point, not an installer and not a repository execution contract. It does not grant unrestricted authority to change another repository.

## Source identity

Current recommended entry point:

```text
https://github.com/8ft0-ai/IssueOps/blob/main/BOOTSTRAP.md
```

For reproducible adoption, replace `main` with the exact commit used:

```text
https://github.com/8ft0-ai/IssueOps/blob/<commit-sha>/BOOTSTRAP.md
```

Record both the pinned URL and `IssueOps Bootstrap 0.1` in the target repository's local bootstrap issue and pull request.

The bootstrap represents the completed manual IssueOps baseline documented in the [IssueOps operating protocol](docs/issueops-protocol.md). It does not include planned capabilities from issue #90 or issue #113.

## Authority boundary

Before a valid local bootstrap issue exists, the bootstrap authorises only:

```text
read-only repository assessment
  -> adoption-posture recommendation
  -> preparation of one local bootstrap issue
  -> creation of that issue only with repository-owner permission
```

The remote specification does not itself authorise issue creation.

Before the local issue is ready and its implementation plan is recorded, do not:

- create or change files;
- create a branch or pull request;
- add workflows, bots, apps, generators, installers or schemas;
- change labels, settings, permissions, required checks or branch protection;
- configure auto-merge;
- change application code; or
- claim approval, merge or publication authority.

The target repository's local instructions, issue, validation rules, review requirements and human authority govern every mutation.

## Required starting information

Identify before assessment:

- exact target repository;
- stable or default branch;
- repository-owner authority for read-only assessment;
- whether creation of one local bootstrap issue is permitted;
- relevant agent and contributor instructions; and
- any known protected paths or operational boundaries.

If the target repository or authority is unclear, stop without mutation.

## Bootstrap sequence

### 1. Inspect without mutation

Read the target repository's existing:

- agent instructions, such as `AGENTS.md` or an equivalent;
- contributor guidance;
- issue templates or issue-writing conventions;
- pull-request templates and review rules;
- validation commands, required checks and environment constraints;
- branch naming, base-branch and dependency conventions;
- merge authority and merge method; and
- planning or roadmap records, when present.

Use the [repository assessment and posture form](bootstrap/repository-assessment.md). Do not infer absent authority from repository access.

### 2. Map capabilities before proposing files

Use [convention mapping](bootstrap/convention-mapping.md) to identify local equivalents for the manual IssueOps controls.

Preserve or adapt an existing owner when it is clear and compatible. Do not introduce a duplicate document, issue template or pull-request surface merely to use IssueOps names.

### 3. Select one adoption posture

#### Already compatible

Use when effective local equivalents already exist. Propose only material corrections. A no-change outcome is valid.

#### Minimal manual adoption

Use by default when material controls are missing but dependent stage planning is not justified. Add or adapt only the minimum surfaces needed for executable issues, readiness and planning, scoped branches, safe mutation, validation, pull-request evidence and explicit human authority.

#### Stage-capable adoption

Use only when the repository genuinely needs dependent multi-issue planning, cross-cutting governance, end-to-end proof or an explicit adoption close-out. Do not add stage machinery for symmetry.

### 4. Prepare the local execution contract

Use the [local bootstrap issue template](bootstrap/bootstrap-issue-template.md).

The proposed issue must identify:

- the pinned bootstrap source;
- the selected posture and evidence;
- existing conventions to preserve;
- exact files or local surfaces permitted to change;
- explicit non-goals and prohibited mutations;
- validation and review expectations;
- dependencies and safe starting state;
- local approval and merge authority; and
- any post-merge verification.

### 5. Request the first local write

Creating the local bootstrap issue should be the first target-repository write unless a valid equivalent issue already exists.

Create it only when the target repository owner has authorised that operation. If issue creation is not permitted, return the completed assessment and proposed issue text without mutation.

### 6. Begin the normal local lifecycle

After the local issue exists:

1. read it back with all comments;
2. determine whether it is executable;
3. post readiness and dependency evidence;
4. post an implementation plan;
5. create one issue-scoped branch from the recorded safe starting point;
6. implement only the local contract;
7. validate against the final branch or pull-request head;
8. open the pull request as the evidence pack;
9. review both contract fulfilment and scope control; and
10. merge only under the target repository's approved authority and policy.

Use the target repository's conventions where they are compatible. The detailed lifecycle and evidence vocabulary are available in the [canonical IssueOps documentation](docs/issueops-protocol.md).

## Prohibited default changes

The bootstrap does not justify these changes by default:

- GitHub Actions or other automation;
- automatic issue creation or lifecycle transitions;
- CLIs, installers, prompt generators, schemas or GitHub Apps;
- auto-merge configuration;
- required-check, branch-protection, permission or repository-setting changes;
- new labels as a prerequisite;
- application-code changes;
- organisation-wide rollout; or
- a copied IssueOps protocol that can drift from its source.

A target repository may consider such work only through a separate local execution contract with its own authority, validation and review.

## Expected assessment output

Before requesting issue creation, provide:

1. the pinned bootstrap source and target repository;
2. the authority available for assessment and issue creation;
3. a map of existing repository conventions;
4. a capability assessment with evidence;
5. the selected posture and rejected alternatives;
6. proposed changes, or an explicit no-change recommendation;
7. risks, conflicts, unsupported capabilities and open questions; and
8. the complete proposed local bootstrap issue.

Do not describe same-session review as independent evidence. A real adoption claim requires separately governed proof in the target repository.

## Source pack

- [Source-pack contract and ownership](bootstrap/README.md)
- [Repository assessment and posture form](bootstrap/repository-assessment.md)
- [Convention-mapping guidance](bootstrap/convention-mapping.md)
- [Local bootstrap issue template](bootstrap/bootstrap-issue-template.md)

If the source pack conflicts with the target repository's explicit local instructions, stop and surface the conflict. Remote guidance does not override local authority.
