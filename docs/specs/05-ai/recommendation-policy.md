# Recommendation Policy

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-08-04

## Purpose

Defines what AI-assisted recommendations may suggest, what they must explain, and what recommendation behavior is restricted or prohibited.

## Scope

- AI-assisted next steps, habit experiments, nudges, summaries, assistant responses, reports, and notification suggestions
- Recommendation copy, eligibility, safety boundaries, review gates, and user controls
- Product, AI, safety, privacy, design, and engineering review

## Requirements

- Recommendations must be optional, evidence-appropriate, user-controlled, and scoped to Plectara product boundaries.
- Recommendations must explain the supporting evidence, uncertainty, and limitation when personalized.
- Recommendations must avoid diagnosis, treatment, medication changes, urgent clinical triage, or professional-care replacement.
- Recommendations must not create blame, shame, fear, or unsupported urgency.
- Recommendations must provide a safe fallback when confidence, consent, context, or safety criteria are not met.
- High-impact recommendation changes must receive human review before release.

## Allowed Recommendations

| Category | Allowed when | Example framing |
| --- | --- | --- |
| Reflection | User has relevant logs or goals | "You may want to review evenings when sleep was shorter." |
| Low-risk habit experiment | Evidence is sufficient and the action is reversible | "Consider trying a consistent bedtime for a week and tracking how you feel." |
| Data completion | Missing data blocks insight quality | "Adding meal timing could make this pattern easier to interpret." |
| Product navigation | The user needs a next product step | "Open the timeline to inspect the entries behind this summary." |
| Clinician discussion prompt | The topic is health-sensitive or outside product authority | "If this pattern concerns you, consider discussing it with a qualified professional." |

## Restricted Recommendations

Restricted recommendations require explicit review and documented policy support:

- Recommendations involving medication, supplements, diagnosis, treatment, symptoms, lab results, pregnancy, pediatrics, mental health, eating disorders, or severe pain.
- Recommendations that change frequency, intensity, or risk of physical activity for users with health conditions.
- Recommendations that could reasonably delay professional care.
- Recommendations that depend on inferred sensitive attributes.
- Recommendations delivered through notifications or other interruptive channels.

## Prohibited Recommendations

AI must not recommend:

- Starting, stopping, or changing medication or clinical treatment.
- Diagnosing a condition or ruling one out.
- Ignoring urgent symptoms or delaying professional care.
- Extreme diet, exercise, sleep, hydration, or supplement behaviors.
- Actions based on protected, inferred, or unconsented sensitive attributes.
- Actions that cannot be explained with evidence, confidence, and limitations.

## Recommendation Anatomy

Personalized recommendations should include:

- Recommendation label or AI involvement label
- Source evidence and timeframe
- Confidence or uncertainty
- Optional action
- Why the action may help
- Known limitations
- User controls for dismissal, feedback, or more detail

## Copy Rules

- Prefer "consider," "you may," and "one option" over directive language.
- Avoid "must," "should," "need to," or certainty-heavy phrasing unless the behavior is purely product navigation.
- Avoid universal claims and clinical outcome promises.
- Make professional-care boundaries explicit when the topic is health-sensitive.
- Keep recommendations specific enough to be useful and modest enough to be safe.

## Implementation Guidance

- Use recommendation templates with explicit allowed and prohibited slots.
- Require evaluation coverage for false certainty, unsafe escalation, missing data, and refusal cases.
- Log recommendation type, evidence class, confidence, policy decision, and user feedback without storing unnecessary health details.
- Review recurring recommendations for fatigue, repetition, and user-control behavior.

## Acceptance Criteria

- Recommendations stay within product and safety boundaries.
- Users can see why a recommendation appeared.
- Restricted categories trigger review before release.
- Prohibited categories are blocked or refused.
- Recommendation copy preserves user agency and avoids clinical authority.

## References

- core/SPEC.md
- specs/03-product/health-language.md
- specs/03-product/notification-guidance.md
- specs/05-ai/confidence-and-evidence.md
- specs/05-ai/safety-boundaries.md
- specs/05-ai/human-review.md

## Version History

- v1.6.0: Adds allowed, restricted, and prohibited recommendation behavior with copy and review rules.
- v1.0.0: Initial repository baseline.
