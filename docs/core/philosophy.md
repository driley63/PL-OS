# Product Philosophy

Status: Released
Owner: PL-OS Maintainers
Version: 1.7.0
Last updated: 2026-08-20

## Purpose

Codifies "Translating daily habits into a plan towards optimal health."

## Scope

- Design lens
- Product lens
- Engineering lens
- AI lens

## Requirements

- Daily habit data must be translated into useful plans.
- Recommendations must be understandable and practical.
- The system must avoid implying diagnosis.
- Repeated observations should become easier to capture as Plectara learns the user's routine.
- Insights should explain relationships between captured behavior, learned habits, and how the user feels.

## Product Pillars

Plectara product decisions should be evaluated through three connected pillars:

| Pillar | Meaning | Product role |
| --- | --- | --- |
| Capture | Effortlessly record what happened | Feeds the system with observations from daily life |
| Habits | Learn what repeats for this user | Personalizes surfaces, shortcuts, nudges, and review |
| Insights | Reveal what appears to matter | Helps the user understand relationships between habits, symptoms, and outcomes |

Capture feeds Habits. Habits give context to Insights. Insights create the user value that makes Capture worth doing.

Plectara should adapt to the user faster than the user adapts to Plectara. The product should not force people to redesign their routines around the app; it should learn recurring behavior, reduce repeated effort, and make the next useful capture easier to reach.

## Implementation Guidance

- Use the philosophy when evaluating scope.
- Use the One Sentence Test as the gate for feature proposals: "How does this help users understand how their lifestyle affects how they feel?"
- Reject features that increase tracking without improving understanding.
- Treat every additional step in recurring capture as a cost against the product's value.
- Prefer adaptive product behavior over configuration-heavy setup when the user can still retain control.

## Acceptance Criteria

- Reviewers can explain how a change supports the philosophy.
- Specs avoid empty tracking requirements.

## References

- core/SPEC.md

## Version History

- v1.7.0: Adds the One Sentence Test as a product philosophy gate.
- v1.7.0: Adds Capture, Habits, and Insights as the product pillars for Plectara UX decisions.
- v1.0.0: Initial repository baseline.
