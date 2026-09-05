# Experience Principles

Status: Released
Owner: Product Working Group
Version: 1.7.0
Last updated: 2026-08-20

## Purpose

Defines product experience principles for Plectara workflows, guidance, feedback, and user control.

## Scope

- Daily logging, onboarding, reports, settings, notifications, and insights
- Mobile and web product behavior
- Product, design, engineering, AI, and research review

## Requirements

- Every workflow must state the user goal before specifying UI behavior.
- Repeated daily actions must be optimized for low effort and fast correction.
- High-frequency entry points must prioritize Capture before summary, analysis, or navigation.
- Plectara should evolve repeated captures into user-controlled Habits where that reduces future effort.
- Health interpretation must be explainable from visible user data, evidence, or documented model behavior.
- Product copy must avoid shame, blame, diagnosis, and unsupported certainty.
- Users must retain control over reminders, permissions, sensitive data, and AI-assisted experiences.
- Product surfaces must identify when information is missing, delayed, estimated, or AI-generated.

## Principle Set

| Principle | Product rule |
| --- | --- |
| Understanding over tracking | Logging is valuable only when it helps the user understand patterns or next steps |
| Capture before dashboards | Widgets and shortcuts exist to record life quickly; the app exists to help users understand it |
| Adaptive over configured | The product should learn repeated behavior before asking users to manually design their workflow |
| Action over observation | Insights should point to practical options, not passive dashboards |
| Calm repetition | Daily workflows should stay predictable, compact, and forgiving |
| Evidence-first guidance | Interpretations must expose source, timeframe, and limitations |
| Consent in context | Ask for permission when the user understands why it matters |
| User agency | Let users edit, dismiss, pause, export, or delete where appropriate |

## The One Sentence Test

Every feature proposal must pass the One Sentence Test before implementation:

> How does this help users understand how their lifestyle affects how they feel?

If the answer is unclear, the feature should be redesigned, simplified, or rejected. A feature that adds capture, configuration, content, automation, or analysis without increasing user understanding is not aligned with Plectara's product philosophy.

Every proposal must explicitly identify:

- Which pillar it strengthens: Capture, Habits, Insights, or a clear combination of the three.
- Whether it reduces friction in the user's routine.
- Whether it increases the user's understanding of the relationship between lifestyle and how they feel.
- Whether it aligns with the North Star: "Plectara should disappear into the user's routine."

The One Sentence Test is a first-class product principle. It should be applied before design exploration, technical planning, or implementation work begins.

## Product Review Questions

- How does this help users understand how their lifestyle affects how they feel?
- What user decision or action does this experience support?
- What evidence does the product show before offering interpretation?
- What could be misunderstood as medical advice?
- What happens when data is missing, stale, wrong, or revoked?
- How does the experience behave for repeat use after the first week?
- Does this help users capture more naturally, help Plectara learn their habits, or help them discover meaningful insights?
- Which pillar does this strengthen: Capture, Habits, Insights, or a clear combination of the three?
- Does this reduce friction in the user's routine?
- Does this align with the North Star that Plectara should disappear into the user's routine?
- Is this surface trying to summarize when it should simply help the user capture?
- What control does the user have over reminders, privacy, or AI involvement?

## Implementation Guidance

- Define primary and secondary user outcomes before writing screen requirements.
- Prefer progressive disclosure over long upfront explanation.
- Keep high-frequency flows stable unless research shows a clear need to change them.
- Treat every extra tap, screen, field, or decision in a repeated capture as part of the friction budget.
- Pair positive feedback with useful context, not empty celebration.
- Treat unexpected friction in daily logging as a product quality issue.

## Acceptance Criteria

- Product requirements connect to an explicit user goal.
- Health-sensitive interpretation is evidence-backed and appropriately cautious.
- Users can recover from errors without losing work.
- Privacy, consent, and AI involvement are visible at relevant decision points.
- Repeat workflows remain useful after novelty fades.

## References

- core/SPEC.md
- specs/02-design/SPEC.md
- specs/03-product/health-language.md

## Version History

- v1.7.0: Adds the One Sentence Test as a first-class product principle for feature proposals.
- v1.7.0: Adds Capture-first, Adaptive Capture, and Habit evolution principles.
- v1.3.0: Adds product experience principles, review questions, and acceptance criteria.
- v1.0.0: Initial repository baseline.
