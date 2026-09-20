# IssueOps v2 — minimal authority protocol proof programme

Status: completed.

Decision: **Reject**.

## Original documented intent

The contemporaneous [IssueOps v2 roadmap](../roadmap/issueops-v2.md), shaped through issue [#212](https://github.com/8ft0-ai/IssueOps/issues/212) and merged through PR [#213](https://github.com/8ft0-ai/IssueOps/pull/213), asked whether a five-state / six-invariant architecture could preserve the complete stable IssueOps safety kernel while materially reducing operator-visible machinery and remaining correct on private GitHub Free.

The roadmap explicitly made **Adopt / Adapt / Reject** the allowed evidence-based terminal decisions. It did not adopt v2, replace `v0.3.0`, publish a release or authorise child consequences by itself.

## Retrospective interpretation

Not applicable. The initiative used a contemporaneous approved roadmap and separately governed proof records. This delivery record preserves the difference between the original preservation claim and the evidence that ultimately rejected the current architecture.

## What shipped

The programme shipped proof artefacts and negative architectural evidence rather than a new stable protocol.

- Issue [#214](https://github.com/8ft0-ai/IssueOps/issues/214) / PR [#215](https://github.com/8ft0-ai/IssueOps/pull/215) produced the accepted Proof A semantic specification for the five states, six invariants, authority meanings, freshness, retry, deviation and outcome rules.
- Issue [#216](https://github.com/8ft0-ai/IssueOps/issues/216) / PR [#217](https://github.com/8ft0-ai/IssueOps/pull/217) produced the accepted Proof B private-GitHub-Free operating profile, including the distinction between protocol correctness and optional paid/mechanical enforcement.
- Issue [#218](https://github.com/8ft0-ai/IssueOps/issues/218) performed Proof C and found the accepted semantics **NOT_COMPATIBLE** with legitimate stable case #196 at C4.
- Issue [#219](https://github.com/8ft0-ai/IssueOps/issues/219) / PR [#220](https://github.com/8ft0-ai/IssueOps/pull/220) implemented exactly one bounded exceptional-authority remediation and then re-proved C4.
- The fresh targeted re-proof in comment `5752779607` still concluded `C4_NOT_COMPATIBLE`; independent review `5752798842` approved that result and owner close-out `5752832794` accepted it.
- Issue [#221](https://github.com/8ft0-ai/IssueOps/issues/221), comment `5753118002`, selected **REJECT_CURRENT_V2_DIRECTION** and retained `v0.3.0` as the stable protocol.

No v2 stable-protocol replacement, dogfood, external pilot, migration, release or adoption shipped.

## Linked issues and pull requests

- Architecture/shaping: [#212](https://github.com/8ft0-ai/IssueOps/issues/212)
- Roadmap formalisation: [PR #213](https://github.com/8ft0-ai/IssueOps/pull/213)
- Proof A: [#214](https://github.com/8ft0-ai/IssueOps/issues/214) / [PR #215](https://github.com/8ft0-ai/IssueOps/pull/215)
- Proof B: [#216](https://github.com/8ft0-ai/IssueOps/issues/216) / [PR #217](https://github.com/8ft0-ai/IssueOps/pull/217)
- Proof C: [#218](https://github.com/8ft0-ai/IssueOps/issues/218)
- C4 remediation and targeted re-proof: [#219](https://github.com/8ft0-ai/IssueOps/issues/219) / [PR #220](https://github.com/8ft0-ai/IssueOps/pull/220)
- Roadmap disposition: [#221](https://github.com/8ft0-ai/IssueOps/issues/221)
- Programme close-out: [#222](https://github.com/8ft0-ai/IssueOps/issues/222)

## Proof runs, checks and artefacts

The strongest programme evidence is the durable proof chain rather than a later dogfood run.

- Proof A established the candidate five-state / six-invariant semantics and retained independent exact-candidate review, prospective authority, freshness, retry, deviation and outcome boundaries.
- Proof B established reusable private-GitHub-Free evidence: protocol correctness does not depend on branch protection, rulesets, required reviewers/checks, protected environments or other paid enforcement features.
- Proof C on #218 returned `NOT_COMPATIBLE` because C4 could not reconstruct legitimate stable case #196 under the accepted v2 authority semantics.
- The #219 remediation changed the accepted exceptional-path semantics once, then fresh targeted re-proof `5752779607` again returned `C4_NOT_COMPATIBLE`.
- Independent substantive re-proof review `5752798842` approved the fresh negative result.
- Owner #219 close-out `5752832794` accepted the negative proof without retroactively invalidating #196.
- Owner roadmap disposition `5753118002` selected **Reject**.

The durable compatibility truth is:

```text
#196 = legitimate stable-v0.3.0 behaviour
#196 = not compatible with accepted v2 semantics
v0.3.0 = stable retained
```

## Intended versus actual delivery

The roadmap intended to proceed from semantic specification and private-Free profiling through compatibility proof, real IssueOps dogfood, a genuine private-Free external pilot and final comparison.

Actual delivery stopped earlier for a valid evidence reason. The mandatory stable-kernel compatibility proof failed at C4. One bounded semantic remediation was attempted, independently reviewed and merged, but the targeted re-proof still found the architecture incompatible with legitimate stable behaviour. The owner therefore selected **Reject** rather than extending the programme into repeated remediation or weakening the compatibility claim.

Accordingly, real v2 dogfood, the external private-Free pilot, later adoption-only proof, release/version publication and migration/adoption work became unnecessary for this rejected direction. They are not marked passed and were not performed.

## Observed limitations and friction

The programme did not prove that the five-state / six-invariant architecture can replace the stable kernel. It also did not collect v2 dogfood or external-pilot evidence because the compatibility gate failed first.

The main design friction was exceptional direct-main compatibility. Historical #196 legitimately used the then-stable exception model, yet its durable sequence created a safe immutable candidate before `main` moved and did not contain the current-v2 separate consequence-authority event or independent exact-candidate review. The bounded #219 remediation did not resolve that mismatch without requiring broader semantic relaxation or additional exception machinery.

The negative result constrains future claims: Proof A and Proof B are useful evidence, but neither may be presented as proof that the rejected architecture is a compatible stable replacement.

## Boundaries preserved

The programme preserved the stable IssueOps authority and evidence boundaries throughout:

- `v0.3.0` remained the governing stable protocol;
- implementation and merge/consequence authority remained human-governed;
- exact-state freshness and independent substantive review remained decision-relevant;
- negative and unavailable evidence was retained rather than normalised away;
- #196 was not retroactively reclassified as invalid;
- no external repository inherited IssueOps authority;
- no dogfood, pilot, release or adoption consequence was inferred from proof acceptance; and
- no successor architecture or roadmap was created by close-out.

Proof B's private-Free findings, the six-invariant decomposition, exact-candidate/currentness controls, independent-review rule, consequence-authority consumption/retry lessons, execution-deviation circuit breaker and outcome-verification findings remain reusable design evidence without adopting the rejected architecture.

## Decisions and lessons

Decision: **Reject** the current IssueOps v2 direction and retain `v0.3.0` as stable.

The central lesson is that a simplification programme must be allowed to fail its own compatibility proof. A negative result is more valuable than preserving momentum by weakening historical truth or adding exception machinery until the candidate passes.

A second lesson is that private-GitHub-Free correctness findings are separable from the rejected lifecycle architecture. Proof B can inform future designs without implying that Proof A's state model should be adopted.

The programme also confirms an anti-loop boundary: after one bounded remediation failed to restore C4 compatibility, another semantic change requires a genuinely new separately governed architecture hypothesis rather than continued patching of this lineage.

## Implications for the next stage

No successor stage, simplification programme, release, migration or replacement roadmap is approved.

Any future IssueOps simplification effort must begin from a new concrete architecture question and a separately governed roadmap. It may reuse the durable findings above, including Proof B and the C4 negative evidence, but it must not treat this rejected programme as unfinished implementation work.
