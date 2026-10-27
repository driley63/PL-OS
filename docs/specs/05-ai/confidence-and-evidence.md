# Confidence and Evidence

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-10-27
Presentation amendment: Approved; unreleased implementation contract in Insights Presentation

## Purpose

Defines how AI-assisted output communicates evidence, confidence, uncertainty, limitations, and missing data.

## Scope

- AI-assisted insights, explanations, recommendations, summaries, reports, assistant responses, and model-generated labels
- Confidence labels, evidence cards, limitation copy, source references, stale-data handling, and low-confidence states
- Product, design, engineering, evaluation, and safety review

## Requirements

- Interpretive AI output must include evidence context before or alongside the interpretation.
- Confidence labels must map to documented criteria, not subjective tone.
- Low-confidence output must be framed as exploratory or withheld.
- Limitations must be visible enough to affect user interpretation.
- Missing, stale, conflicting, or insufficient data must be disclosed.
- AI output must not imply causation, diagnosis, or treatment certainty unless separately reviewed and approved.

## Evidence Model

Every interpretive AI output should answer:

- What source data was used?
- What timeframe was reviewed?
- What changed, repeated, or stood out?
- What data is missing, stale, inconsistent, or excluded?
- Why is this shown now?
- What is the safe scope of the suggested next step, if any?

## Confidence Labels

| Label | Meaning | Allowed use |
| --- | --- | --- |
| High | Evidence is sufficient, current, consistent, and covered by evaluation | Summaries, observations, and low-risk optional next steps |
| Medium | Evidence is directionally useful but incomplete, noisy, or context-limited | Exploratory explanations and cautious suggestions |
| Low | Evidence is sparse, stale, conflicting, or outside strong evaluation coverage | Learning states, exploratory framing, or withheld recommendations |
| Unavailable | Required evidence, consent, model service, or safety criteria are missing | Failure states and unavailable states |

Confidence labels must not be shown as percentages unless the measurement method is documented and reviewed.

## Evidence Display Rules

- Show source and timeframe in plain language.
- Use labels, icons, layout, and text instead of color alone.
- Keep limitations visible in the main insight or one interaction away from the main claim.
- Do not hide material uncertainty in tooltips only.
- Separate facts from interpretation and next steps.
- Use timestamps for generated summaries, stale context, and reports.

## Limitation Language

Limitation copy should:

- Be specific about what is unknown or missing.
- Avoid blame, shame, fear, or false precision.
- Avoid generic disclaimers that do not explain the limitation.
- Explain what additional data or user action would improve confidence when appropriate.
- Avoid implying that more tracking is always required.

## Withholding Rules

AI output should be withheld or downgraded when:

- Required context is missing or consent is absent.
- Data is stale beyond the behavior's documented limit.
- The output would imply diagnosis, prescription, causation, or urgent clinical judgment.
- Evaluation coverage does not include the scenario.
- Safety filters, policy rules, or human review block the output.

## Implementation Guidance

- Store confidence criteria with the insight or output contract.
- Keep generated evidence summaries auditable against source data.
- Test confidence labels against sparse, conflicting, stale, and synthetic edge-case data.
- Review copy for overstatement whenever confidence gates change.
- Track low-confidence rates as product-quality signals, not just model-quality signals.

## Acceptance Criteria

- Users can see what evidence supports an AI output.
- Confidence labels have documented criteria.
- Missing or uncertain evidence changes the user-facing state.
- Limitations are visible enough to prevent overinterpretation.
- Reviewers can reproduce why an output was high, medium, low, or unavailable.

## Presentation integration

Apply the approved [Insights Presentation](../03-product/insights-presentation.md) contract, refined October 27, to Today, fixed-goal summaries, selected-goal comparisons, connection evidence, AI Review, and contextual chat. Preserve material limitations and care notices outside optional disclosures. Local findings remain available when AI is off or unavailable; AI attribution applies to the explanation only. Implementation is pending.

## References

- specs/03-product/insights-and-correlations.md
- specs/03-product/health-language.md
- specs/02-design/charts.md
- specs/05-ai/failure-states.md
- specs/05-ai/evaluation.md

## Version History

- v1.6.0: Adds confidence labels, evidence model, limitation language, and withholding rules.
- v1.0.0: Initial repository baseline.
