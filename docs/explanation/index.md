# Explanation

Explanation pages help maintainers and interested readers understand why IssueOps is designed this way, how its concepts relate and which trade-offs its controls preserve. Start here when the question is “why?” rather than “what exact field?” or “what do I do next?”.

## Understand the model

- [Why the issue is the execution contract](execution-contract-model.md) — why durable repository intent bounds agent execution, how planning differs from implementation and why authority remains human.
- [Why evidence is not approval](pr-evidence-and-approval.md) — why evidence presence, contract satisfaction and the human approval decision remain separate.
- [Why repository-native validation is preferred](repository-native-validation-model.md) — what direct evidence proves, when fallback is limited and why pending checks remain visible.
- [Documentation architecture](documentation-architecture.md) — how Tutorials, How-to, Reference and Explanation divide responsibility, and why project records remain outside that tree.
- [Delegated batch mode](../delegated-batch-mode.md) — why bounded owner delegation can reduce routine confirmation without removing validation and merge gates.
- [Site and wiki boundaries](../site-vs-wiki.md) — why canonical documentation and project memory have different authority.

## Project direction and history

Project records are not a fifth Diátaxis mode and are not duplicated into Explanation. Use their canonical repository locations:

- [Planning control surface](https://github.com/8ft0-ai/IssueOps/blob/main/planning/README.md)
- [Roadmap index](https://github.com/8ft0-ai/IssueOps/blob/main/planning/roadmap/index.md)
- [Delivery records](https://github.com/8ft0-ai/IssueOps/blob/main/planning/delivery/index.md)
- [Historical evidence and compatibility decisions](https://github.com/8ft0-ai/IssueOps/blob/main/planning/evidence/index.md)

Compatibility pages preserve existing public URLs but do not become alternative sources of project intent, delivery evidence or history.