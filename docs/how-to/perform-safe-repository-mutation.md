# Perform a safe repository mutation

Use this guide immediately before a repository write such as creating a branch, changing a file, opening a pull request or merging.

For exact phase permissions, evidence formats and circuit-breaker rules, use [Operation permissions and evidence](../reference/operation-permissions-and-evidence.md).

## 1. Confirm the current phase

Identify whether the work is in issue setup, branch setup, implementation, PR creation/remediation, or merge/post-merge verification.

Do not use a tool merely because it is available. The phase determines which side effects are permitted.

## 2. Name the intended side effect

State what should change next and what must not change.

For example:

```text
Phase: Branch setup
Intended operation: Create the issue-specific feature branch
Selected tool: create_branch
Target: 8ft0-ai/IssueOps
Expected side effect: one new branch from the verified main commit
Forbidden side effects: no file, issue, PR, label or merge mutation
```

Use the full format for high-leverage or ambiguous operations. Use compact evidence only for a routine, low-risk and unambiguous mutation.

## 3. Verify the target and input

Check:

- canonical repository identity;
- issue and branch number;
- base or expected head SHA;
- file path or repository object;
- write content or state transition; and
- tool schema or command semantics.

Do not infer a target from a similarly named repository or stale conversation context.

## 4. Check prerequisites

Confirm that:

- the issue authorises the mutation;
- readiness and dependencies allow the current phase;
- the implementation plan names the operation or affected area;
- required validation or review gates before this mutation are satisfied; and
- repository policy and human authority permit it.

## 5. Execute one bounded operation

Perform only the intended mutation. Avoid combining unrelated file changes or repository transitions in one opaque action.

For file writes, read the file back. For issue, branch or PR operations, fetch the resulting object and confirm the expected state.

## 6. Verify the side effect

Compare the result with the expected and forbidden effects.

Examples:

- branch exists at the expected base;
- only the intended file changed;
- draft PR points to the planned branch and base;
- merge used the validated head SHA; or
- issue closed only through the intended PR.

## 7. Stop on unintended mutation

If the operation changes the wrong object or causes an unplanned side effect:

- stop normal writes;
- perform only the minimum safe remediation;
- record the event and impact; and
- require explicit repository-owner direction before continuing.

Do not continue the normal issue loop after an accidental mutation simply because it was repaired.

## Common failure modes

- selecting a write tool from name alone;
- using a stale branch or head SHA;
- creating a branch before dependencies are satisfied;
- opening a PR before changed files and validation status are known;
- merging a changed head without revalidation; or
- performing an incidental workflow, permission or setting change.
