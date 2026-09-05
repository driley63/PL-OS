# Insights and Correlations

Status: Released
Owner: Product Working Group
Version: 1.7.0
Last updated: 2026-08-20

## Purpose

Defines product standards for insights, correlations, explanations, confidence, evidence, and user-facing next steps.

## Scope

- Rule-derived insights, AI-assisted insights, correlations, summaries, recommendations, and evidence cards
- Health timeline, reports, notifications, and dashboard surfaces
- Product, data, AI, safety, accessibility, and research review

## Requirements

- Insights must identify whether they are rule-derived, AI-assisted, imported, or manually authored.
- Correlations must not be presented as causation without reviewed evidence and policy support.
- Every insight must expose source data, timeframe, confidence or strength, and known limitations where relevant.
- Users must be able to dismiss, save, inspect, or provide feedback on recurring insights.
- Insight language must include a practical next step only when the step is safe, optional, and evidence-appropriate.
- AI-assisted insights must follow AI Principles and make model involvement visible.

## Relationship to Capture and Habits

Insights are the value layer created from Capture and Habits. Capture records what happened. Habits identify what repeats for the individual user. Insights explain which repeated behaviors, symptoms, contexts, or changes appear meaningfully related.

Insights should not imply that more logging is valuable on its own. When an insight asks for more data, the request should explain how the additional Capture will improve pattern quality, habit understanding, or confidence.

## Insight Types

| Type | Use | Required context |
| --- | --- | --- |
| Observation | A direct change or logged fact | Source and timeframe |
| Trend | Directional movement over time | Baseline, range, and missing data |
| Correlation | Relationship between two or more signals | Strength, timeframe, limitations |
| Reminder insight | Useful follow-up based on user intent | User control and dismissal |
| AI explanation | Model-assisted interpretation | AI label, confidence, and evidence |
| Report insight | Summary for a longer period | Covered period and export context |

## Evidence Requirements

Every interpretive insight should answer:

- What data was used?
- What period was reviewed?
- What changed or repeated?
- What is uncertain or missing?
- Why is this shown now?
- What can the user do next?

## Confidence and Limitations

- Use confidence labels only when they map to documented model, rule, or data-quality criteria.
- Low-confidence insights may be shown only when framed as exploration, not guidance.
- Do not bury limitations behind tooltips only.
- Do not use AI Purple for non-AI correlations.
- When evidence is insufficient, show an unavailable or learning state instead of forcing an insight.

## User Controls

- Users must be able to dismiss irrelevant insights.
- Users should be able to inspect evidence before acting.
- Feedback controls should distinguish “not useful,” “not accurate,” and “do not show this again” where meaningful.
- Recurring insights should avoid repeating unchanged information without new context.

## Implementation Guidance

- Use insight templates reviewed by Product, AI, and Safety before implementation.
- Keep insight titles short and evidence sections explicit.
- Use reports or detail pages when evidence is too dense for a card.
- Track insight usefulness, dismissal rate, and correction feedback.
- Require additional review for insights involving medication, diagnosis, clinical risk, or urgent symptoms.

## Acceptance Criteria

- Users can distinguish observation, trend, correlation, and recommendation.
- Evidence and limitations are visible before or alongside suggested action.
- AI-assisted behavior is labeled.
- Correlation language does not imply unsupported causation.
- Insight controls support dismissal, inspection, and feedback.

## References

- core/SPEC.md
- specs/03-product/daily-logging.md
- specs/03-product/health-language.md
- specs/05-ai/confidence-and-evidence.md
- specs/05-ai/safety-boundaries.md

## Version History

- v1.7.0: Connects insights to the Capture and Habits product pillars.
- v1.3.0: Adds insight types, evidence requirements, confidence rules, and user controls.
- v1.0.0: Initial repository baseline.
