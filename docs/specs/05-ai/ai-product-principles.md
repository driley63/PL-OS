# AI Product Principles

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-08-04

## Purpose

Defines product-facing principles for AI-assisted Plectara experiences.

## Scope

- AI-assisted summaries, explanations, insights, recommendations, reports, and user education
- Model-generated, model-ranked, model-summarized, and model-assisted product behavior
- Product, design, engineering, safety, privacy, and review decisions that shape user-facing AI

## Requirements

- AI must support the PL-OS philosophy by helping users translate daily habits into understandable, optional next steps.
- AI involvement must be visible when output is personalized, generated, inferred, summarized, ranked, or recommended by a model.
- AI must show evidence and uncertainty before asking the user to act.
- AI must not diagnose, prescribe, create unsupported urgency, or imply clinical certainty.
- AI must preserve user agency through inspection, dismissal, correction, feedback, and opt-out paths where meaningful.
- AI must degrade into documented failure states when evidence, confidence, context, consent, or safety requirements are not met.

## Principle Model

| Principle | Standard | Example review question |
| --- | --- | --- |
| Evidence first | Show source, timeframe, confidence, and limitations before or alongside interpretation | Can the user see why this appeared? |
| User control | Let the user inspect, dismiss, correct, save, or stop recurring AI output where meaningful | Can the user recover from a bad suggestion? |
| Bounded assistance | Frame AI as support for understanding, not authority | Does the copy avoid diagnosis and prescription? |
| Privacy minimum | Use the least sensitive context that can support the output | Is every context field necessary? |
| Calm uncertainty | Explain uncertainty without blame, fear, or false precision | Is low confidence handled plainly? |
| Reviewability | Keep AI behavior traceable to prompts, context, evaluations, and release metadata | Can a reviewer reproduce the intended behavior? |

## AI Involvement Rules

AI involvement is user-visible when:

- A model generates explanatory text, summaries, labels, or recommendations.
- A model infers relationships, ranks results, selects next steps, or chooses what to show.
- A model transforms user health data into an interpretation.
- A user could reasonably believe the product is making a personalized health judgment.

AI involvement may be background-only when:

- The model is used for non-user-facing classification that does not affect health interpretation.
- A deterministic rule fully controls what the user sees.
- The behavior is documented, evaluated, observable, and does not change user-visible meaning.

## User Agency

AI-assisted experiences must define:

- What the user can inspect.
- What the user can dismiss.
- What the user can correct.
- What feedback the user can provide.
- Whether the behavior can be paused, disabled, or made less prominent.
- How user feedback affects future behavior.

## Product Limits

AI must not:

- Present itself as a clinician, coach with clinical authority, or emergency responder.
- Convert weak correlations into causal claims.
- Recommend medication, diagnosis, treatment, or urgent action without separate reviewed clinical policy.
- Hide material limitations behind tooltips only.
- Use confident language when data is sparse, stale, inconsistent, or outside the evaluated scenario.

## Implementation Guidance

- Define the user-facing AI behavior before selecting a model, prompt, or data pipeline.
- Prefer simple rule-derived output when a model is not needed.
- Keep AI labels close to the output they describe.
- Use the smallest safe next step that matches the evidence.
- Capture review decisions for new or changed AI behaviors in PRs and release notes.

## Acceptance Criteria

- Users can identify when AI is involved.
- AI output includes appropriate evidence, confidence, limitation, and next-action context.
- AI behavior gives users meaningful control.
- Reviewers can distinguish rule-derived behavior from model-assisted behavior.
- Unsafe, unsupported, or low-confidence behavior falls back to a documented state.

## References

- core/SPEC.md
- specs/03-product/insights-and-correlations.md
- specs/03-product/health-language.md
- specs/05-ai/confidence-and-evidence.md
- specs/05-ai/recommendation-policy.md
- specs/05-ai/failure-states.md

## Version History

- v1.6.0: Adds product-facing AI principles, involvement rules, user agency requirements, and product limits.
- v1.0.0: Initial repository baseline.
