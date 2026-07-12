# Validation by change type

Validation must match the behaviour and risk changed by the pull request. This page is the canonical validation matrix.

Use all applicable rows when a PR crosses change types. Record what ran, what did not run and what remains after merge.

## Evidence categories

- **Required:** normally completed before approval for this change type.
- **Risk-dependent:** added when scope, environment or consequences require it.
- **Not applicable unless scoped:** do not claim or perform it as unrelated work.

## Documentation

Required:

- changed Markdown and configuration files read back;
- final diff checked against the issue;
- MkDocs navigation reviewed when changed;
- internal links checked by strict build and targeted inspection;
- `python -m pip install -r requirements.txt`;
- `mkdocs build --strict`;
- documentation-currency checklist applied when current status, releases, issues, workflows, settings, labels or automation are mentioned;
- related pages checked for contradictory guidance.

Risk-dependent:

- `mkdocs serve` or generated Pages artefact inspection for significant navigation, tutorial or layout changes;
- representative reader walkthrough;
- spelling or editorial review.

Not applicable unless scoped:

- application tests;
- workflow execution beyond the documentation build;
- branch-protection or deployment changes.

## Workflow

Required:

- workflow files read back;
- YAML structure and expressions reviewed;
- triggers compared with the issue contract;
- permissions checked for least practical scope;
- dependencies pinned, locked or deliberately bounded;
- build, validation, artefact and deployment responsibilities identified;
- manual settings, secrets and environment dependencies documented;
- workflow-change checklist applied;
- safe pre-merge run completed where available;
- post-merge verification listed when the workflow cannot exercise the changed path earlier.

Risk-dependent:

- syntax linting;
- manual dispatch in a safe environment;
- comparison with earlier incidents or review findings.

Not applicable unless scoped:

- unrelated application tests;
- label or branch-protection changes;
- broad workflow refactoring.

## Publishing or deployment

Required:

- changed configuration and guidance read back;
- build command completed;
- generated artefact and deployment target inspected;
- permissions and environment dependencies reviewed;
- repository settings that are not code-controlled recorded;
- pre-merge validation and post-merge verification separated;
- deployed URL or environment verified after merge when required.

Risk-dependent:

- manual dispatch in a safe environment;
- rollback or recovery review;
- production logs or environment checks.

Not applicable unless scoped:

- new deployment targets;
- broad release automation;
- auto-merge or unrelated application changes.

## Process, labels or governance guidance

Required:

- changed guidance read back;
- strict documentation build when docs change;
- manual versus automated behaviour distinguished;
- lifecycle, label and recommendation terms compared with canonical Reference;
- any real label mutation recorded separately from documentation recommendations;
- scope checked for unapproved automation or authority change.

Risk-dependent:

- repository label availability confirmed;
- examples checked against recent repository records;
- search for contradictory terminology.

Not applicable unless scoped:

- workflow, branch-protection, deployment or application changes.

## Application code

The repository currently contains no main application product, so exact commands come from the future issue and repository conventions.

Required when application code is introduced:

- changed source files read back;
- relevant tests completed;
- build, type or static checks completed where available;
- affected behaviour checked against acceptance criteria;
- error handling reviewed for user-provided or external data;
- compatibility with existing conventions checked;
- validation gaps explicit.

Risk-dependent:

- smoke and regression tests;
- runtime or log verification;
- security and privacy review;
- performance or migration checks.

Not applicable unless scoped:

- unrelated documentation publishing, label or workflow refactoring.

## Planning and delivery records

Required:

- planning files read back;
- repository planning validator and tests completed;
- delivery-graph validation and generated-output checks completed when graph metadata changes;
- intended and actual delivery kept separate;
- roadmap status and issue/PR links checked for accuracy.

Typical commands when relevant:

```bash
python scripts/validate_delivery_graph.py
python scripts/render_delivery_graph.py
python scripts/render_delivery_graph.py --check
```

Use the repository planning workflow as the source of truth for any additional checks.

## Evidence wording

In the PR, record the applicable change types and results. A passing check for one type does not cover another changed behaviour automatically.

Use [Validation status and fallback policy](validation-status-and-fallback-policy.md) for unavailable checks, representative evidence and post-merge verification.
