# Validate a workflow change

Use this guide when an execution contract explicitly authorises a change to `.github/workflows/*` or related workflow behaviour.

For exact requirements, use [Validation by change type](../reference/validation-by-change-type.md) and the [workflow-change review checklist](../workflow-changes.md).

## 1. Confirm workflow scope is authorised

Check that the issue and implementation plan identify the workflow file or behaviour. Do not add a workflow change as an incidental fix for another issue.

Record a full safe-operation check before the mutation because workflow files can change repository permissions, deployments and external side effects.

## 2. Read the workflow back

Inspect the complete YAML from the feature branch, including:

- triggers and filters;
- jobs and dependencies;
- permissions;
- environments and concurrency;
- actions and dependency versions;
- inputs, outputs and artefact paths;
- secret or OIDC usage; and
- failure and post-merge behaviour.

## 3. Apply the workflow checklist

Use the canonical [workflow-change review checklist](../workflow-changes.md). Verify least practical permissions, bounded dependencies, expected triggers and explicit manual settings.

Do not infer that branch protection, Pages source, secrets or environments are configured merely because the workflow references them.

## 4. Run available pre-merge checks

Use repository-native syntax, lint, test or safe workflow execution where available. Confirm the result belongs to the relevant final head.

When the changed trigger cannot run safely before merge, record that exact limitation. Do not replace it with a representative run that does not exercise the changed behaviour.

## 5. Separate settings and post-merge checks

Record repository or environment settings that are outside version control. Identify which behaviour can only be observed after merge or manual dispatch.

A production deployment or merged-branch trigger may be post-merge verification. YAML review, permissions review and any available safe pre-merge run are not.

## 6. Review the change boundary

Confirm the diff did not introduce:

- unapproved permissions;
- new secrets or production targets;
- branch-protection or required-check changes;
- automatic issue, review or merge behaviour;
- unrelated application or documentation rewrites; or
- an unbounded dependency installation.

## 7. Record evidence

The PR should identify:

- changed workflow files;
- trigger and permission scope;
- dependencies and settings;
- checklist completion;
- commands or workflow runs completed;
- validation unavailable before merge;
- post-merge verification; and
- recovery or rollback caveats.

Use the canonical [workflow evidence template](../reference/pr-evidence-templates.md#workflow-change-template).

## 8. Verify the merged behaviour

After merge, observe the required trigger, run, artefact, deployment or setting. Record the run and result on the issue or PR.

A successful merge without the expected workflow behaviour is not successful post-merge verification.

## Common failure modes

- changing a workflow without explicit issue scope;
- reviewing only YAML syntax and not permissions or side effects;
- assuming repository settings from code;
- treating a skipped production job on a PR as production proof;
- leaving action versions unbounded without rationale; or
- marking an unavailable final trigger as complete.
