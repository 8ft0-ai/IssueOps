# Explanation

Explanation pages help maintainers and interested readers understand why IssueOps is designed this way, how its concepts relate and which trade-offs its controls preserve. Start here when the question is “why?” rather than “what exact field?” or “what do I do next?”.

## Understand the model

- [Why the issue is the execution contract](execution-contract-model.md) — why durable repository intent bounds agent execution, how planning differs from implementation and why authority remains human.
- [Why evidence is not approval](pr-evidence-and-approval.md) — why evidence presence, contract satisfaction and the human approval decision remain separate.
- [Documentation architecture](documentation-architecture.md) — how Tutorials, How-to, Reference and Explanation divide responsibility, and why project records remain outside that tree.
- [Delegated batch mode](../delegated-batch-mode.md) — why bounded owner delegation can reduce routine confirmation without removing validation and merge gates. This page remains mixed with operating rules until a later split.
- [Site and wiki boundaries](../site-vs-wiki.md) — why canonical documentation and project memory have different authority.

## Project direction and history

Project records are not a fifth Diátaxis documentation mode. They remain in their canonical repository locations and are linked when context is useful:

- [Approved Stage 4 roadmap](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/stage-04-diataxis-documentation-architecture.md)
- [Planning control surface](https://github.com/8ft0-ai/IssueOps/tree/main/planning)
- [Public roadmap compatibility page](../roadmap.md)
- [Stage 1 release notes](../releases/stage-1.md)
- [Stage 2 stable release notes](../releases/stage-2.md)
- [Stage 3 experimental alpha notes](../releases/stage-3-alpha.md)

These links preserve access to intent, delivery evidence and historical baselines without turning project history into current task or normative guidance.
