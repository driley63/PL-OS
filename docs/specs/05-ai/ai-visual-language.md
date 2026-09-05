# AI Visual Language

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-08-04

## Purpose

Defines how AI involvement, confidence, evidence, uncertainty, generated content, and AI-specific states are visually represented in Plectara product surfaces.

## Scope

- AI labels, badges, icons, confidence indicators, evidence summaries, generated text, assistant responses, overlays, disclosures, failure states, and notifications
- Mobile app, web app, documentation examples, design files, and future component libraries
- Product, design, AI, accessibility, brand, and engineering review

## Requirements

- AI involvement must be visible near AI-generated or model-assisted output.
- AI Purple must be reserved for AI-specific meaning and must not be used as generic decoration.
- AI visual cues must not rely on color alone.
- Confidence, evidence, and limitations must be visually distinct but not alarmist.
- AI output must remain subordinate to product hierarchy and health comprehension.
- AI visual states must use released Brand Identity and Design Language tokens, components, accessibility rules, and feedback patterns.

## AI Labeling

AI labels should be used when:

- Text, summaries, explanations, recommendations, or rankings are model-generated or model-assisted.
- A model interprets user health data.
- A model chooses what insight, recommendation, or next step to show.
- A user could reasonably misread the output as deterministic, clinician-authored, or manually reviewed.

AI labels may be omitted when:

- The behavior is deterministic and non-interpretive.
- AI is used only for internal quality checks that do not change user-facing meaning.
- The user-facing output is fully authored and reviewed outside the model.

## Visual Elements

| Element | Use | Rules |
| --- | --- | --- |
| AI badge | Identify model-assisted output | Place near the title or generated text |
| AI icon | Reinforce AI-specific state or assistant entry | Pair with text for unfamiliar or health-sensitive use |
| AI Purple | Highlight AI-specific affordance or generated state | Use semantic `color.ai.primary`; do not use for non-AI states |
| Confidence label | Communicate reviewed confidence class | Pair with evidence and limitations |
| Evidence summary | Show why output appeared | Include source and timeframe |
| Disclosure | Reveal detailed evidence, prompt limits, or data use | Do not hide material limitations only inside disclosure |
| Failure state | Explain unavailable, blocked, or low-confidence behavior | Use released state and feedback patterns |

## Hierarchy Rules

- AI labels should clarify authorship, not dominate the screen.
- Evidence and limitations should sit close enough to the claim to prevent overinterpretation.
- Recommended actions should be visually secondary to evidence when confidence is medium or low.
- Safety or privacy blocks should use standard warning/error patterns, with AI-specific context in text.
- Generated report narratives should preserve section labels, timestamps, and source context.

## Accessibility

- AI state must be conveyed through text, accessible names, and layout, not color alone.
- AI icons and badges must have meaningful labels when they carry information.
- Confidence labels must be readable by screen readers.
- Motion should not imply certainty, urgency, or clinical importance.
- AI disclosures must be keyboard accessible and preserve focus behavior.

## Copy Pairing

AI visual elements should pair with copy that answers:

- Is AI involved?
- What evidence did it use?
- How confident is this output?
- What is uncertain or missing?
- What can the user do next?

## Implementation Guidance

- Reuse released Design Language badges, chips, cards, banners, dialogs, sheets, and disclosure patterns.
- Use AI Purple sparingly and consistently.
- Avoid decorative AI sparkle, magic, or automation metaphors that imply hidden authority.
- Test AI states across light/dark themes, reduced motion, screen readers, and small screens.
- Keep AI visual changes traceable to Brand and Design token usage.

## Acceptance Criteria

- Users can identify AI-assisted output.
- AI-specific visuals use approved tokens and accessible labels.
- Confidence, evidence, and limitations are visually understandable.
- AI Purple is not used for non-AI meaning.
- Visual treatment does not overstate certainty or authority.

## References

- adr/0003-reserve-purple-for-ai.md
- specs/01-brand/design-tokens.md
- specs/02-design/iconography.md
- specs/02-design/empty-error-loading-states.md
- specs/02-design/overlays-and-feedback.md
- specs/05-ai/confidence-and-evidence.md
- specs/05-ai/failure-states.md

## Version History

- v1.6.0: Adds AI labeling, visual hierarchy, AI Purple usage, confidence display, and accessibility standards.
- v1.0.0: Initial repository baseline.
