# Insight Types

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-10-27
Presentation amendment: Approved; unreleased implementation contract in Insights Presentation

## Purpose

Defines AI-assisted insight types, eligibility rules, required context, and review expectations.

## Scope

- AI-generated summaries, explanations, comparisons, correlations, recommendations, and educational context
- Insights shown in dashboards, timelines, reports, notifications, onboarding, and detail pages
- Rule-derived outputs that may be combined with model-assisted explanation

## Requirements

- Every AI-assisted insight must declare its type.
- Every interpretive insight must expose source data, timeframe, confidence, and limitations where relevant.
- Correlations must not be presented as causation without reviewed evidence and policy support.
- Recommendation-like insights must follow the recommendation policy.
- Insights must define user controls for inspection, dismissal, feedback, and recurrence where meaningful.
- Insights that fail eligibility requirements must show a learning, unavailable, low-confidence, or safety-blocked state instead of forcing output.

## Insight Taxonomy

| Type | Use | Required context | AI risk |
| --- | --- | --- | --- |
| Data summary | Condenses logged facts or report data | Source, timeframe, missing data | Low if no interpretation is added |
| Pattern observation | Describes repeated or changed behavior | Source, timeframe, comparison baseline | Medium if phrasing implies significance |
| Correlation hypothesis | Suggests a possible relationship | Variables, period, strength, limitations | High if causation is implied |
| Explanation | Makes an insight easier to understand | Evidence, confidence, limitation, plain-language reasoning | Medium |
| Suggested next step | Offers optional user-controlled action | Evidence, risk, reversibility, safety boundary | High |
| Educational context | Explains general wellness concepts | Source class, non-personalized framing, limits | Medium if personalized |
| Report narrative | Summarizes a period for review or export | Covered period, included data, exclusions | Medium |
| Assistant response | Answers a user question in context | User question, allowed context, refusal rules | High |

## Eligibility Rules

An AI-assisted insight is eligible only when:

- Required source data is present and current enough for the claim.
- The insight type has an approved output contract.
- Confidence and limitation language can be generated reliably.
- The behavior has evaluation coverage for expected, missing-data, and unsafe-input cases.
- The output does not require clinical authority, emergency triage, or unsupported diagnosis.
- The user has consented to the data use required for the insight.

## Required Insight Fields

AI insight records should define:

- `insight_type`
- `ai_involvement`
- `source_data`
- `timeframe`
- `confidence_label`
- `evidence_summary`
- `limitations`
- `recommended_action`
- `safety_boundary`
- `user_controls`
- `created_at`
- `stale_after`

## Display Rules

- Put the insight type or AI label near the generated output.
- Show evidence and limitations before or alongside recommendations.
- Keep titles factual and avoid overstating certainty.
- Use progressive disclosure for dense evidence, not for material limitations.
- Do not repeat unchanged insights without new data, user request, or meaningful context change.

## Implementation Guidance

- Prefer deterministic insight generation for simple summaries and counts.
- Use AI explanation only where it materially improves understanding.
- Require additional review for medication, clinical conditions, diagnosis-like language, urgent symptoms, pregnancy, pediatric contexts, or severe mental-health content.
- Track user feedback separately for usefulness, accuracy, safety concern, and repetition.

## Acceptance Criteria

- Users can distinguish summary, observation, correlation, explanation, and suggested action.
- AI-assisted insights include source, timeframe, confidence, and limitations.
- Ineligible insights fall back to documented states.
- Recommendation-like output follows the recommendation policy.
- Insight behavior is traceable to product, prompt, evaluation, and release records.

## Presentation integration

Apply the approved [Insights Presentation](../03-product/insights-presentation.md) contract, refined October 27, to Today, fixed-goal summaries, selected-goal comparisons, connection evidence, AI Review, and contextual chat. Preserve material limitations and care notices outside optional disclosures. Local findings remain available when AI is off or unavailable; AI attribution applies to the explanation only. Implementation is pending.

## References

- specs/03-product/insights-and-correlations.md
- specs/05-ai/confidence-and-evidence.md
- specs/05-ai/recommendation-policy.md
- specs/05-ai/safety-boundaries.md
- specs/05-ai/failure-states.md

## Version History

- v1.6.0: Adds AI-assisted insight taxonomy, eligibility rules, required fields, and display standards.
- v1.0.0: Initial repository baseline.
