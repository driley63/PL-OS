# Health Language

Status: Released
Owner: Product Working Group
Version: 1.3.0
Last updated: 2026-08-04

## Purpose

Defines health-sensitive product language for Plectara workflows, insights, reports, errors, notifications, and consent surfaces.

## Scope

- Product UI copy, notifications, reports, onboarding, settings, and support content
- Health, habit, symptom, lifestyle, AI, and evidence language
- Product, clinical-risk, legal, AI, and research review where applicable

## Requirements

- Product language must be clear, calm, specific, and non-blaming.
- Product copy must not diagnose, prescribe, or imply clinical certainty without reviewed policy support.
- AI-generated or model-assisted interpretation must be labeled in plain language.
- Insight copy must distinguish observation, correlation, suggestion, limitation, and user action.
- Error and warning copy must explain scope, impact, and recovery when known.
- Sensitive moments must avoid playful, coercive, or celebratory wording.

## Language Rules

| Avoid | Prefer |
| --- | --- |
| You failed to log yesterday | Yesterday has no log yet |
| This proves your sleep caused fatigue | Sleep and fatigue moved together in this period |
| You should change your medication | Consider discussing medication questions with a qualified clinician |
| Perfect score | Logged consistently |
| Something went wrong | We could not save this log. Your entries are still here. |
| AI knows why this happened | AI found a possible pattern to review |

## Claim Classes

| Class | Allowed language | Review requirement |
| --- | --- | --- |
| Observation | What the user logged or what changed | Product review |
| Pattern | Repeated relationship across a timeframe | Product and data review |
| Correlation | Statistical or model-assisted relationship | Product, data, and AI review |
| Suggestion | Optional next action or exploration path | Product and safety review |
| Clinical claim | Diagnosis, treatment, or medical certainty | Out of scope unless explicitly approved |

## Tone Requirements

- Use everyday words before clinical language.
- Make uncertainty visible when interpretation is probabilistic.
- Prefer “may,” “might,” “is associated with,” or “appears” when evidence is limited.
- Do not use urgency unless the product has a reviewed escalation policy.
- Do not use reward language that implies moral success or failure.

## Implementation Guidance

- Pair health copy with source, timeframe, and next action where relevant.
- Keep notification and empty-state copy shorter than report copy.
- Use content review for new insight templates before implementation.
- Test sensitive copy with users when it may affect anxiety, shame, privacy, or care decisions.

## Acceptance Criteria

- Copy is understandable without clinical expertise.
- Users can distinguish facts from interpretations and suggestions.
- AI, uncertainty, and limitations are visible where relevant.
- Recovery language is specific and non-blaming.
- Unsupported medical advice is absent.

## References

- core/SPEC.md
- specs/03-product/insights-and-correlations.md
- specs/05-ai/safety-boundaries.md

## Version History

- v1.3.0: Adds health language rules, claim classes, tone requirements, and examples.
- v1.0.0: Initial repository baseline.
