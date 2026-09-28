# Cards

Status: Approved for PL-OS v2.6.0
Owner: Design System Working Group
Version: 2.6.0
Last updated: 2026-09-28

## Purpose

Defines card purpose, anatomy, hierarchy, spacing, and usage limits for product surfaces.

## Scope

- Insight cards, metric cards, log cards, report cards, settings panels, and repeated collection items
- Mobile and web product screens
- Documentation examples and future component libraries

## Requirements

- Use cards for individual repeated items, framed tools, and grouped decision content.
- Do not use cards as decorative page sections.
- Do not place UI cards inside other UI cards, except the approved display-only Your Progress metric group defined in the app visual contract.
- Cards must have stable padding, radius, and content hierarchy.
- Health interpretation cards must identify data source, timeframe, confidence, or evidence when relevant.

## Card Types

| Type | Use |
| --- | --- |
| Metric card | One primary value with label, trend, and timeframe |
| Insight card | AI or rule-derived observation with evidence and next action |
| Log card | A daily or historical entry with metadata and edit affordance |
| Report card | Summary block that links to deeper analysis |
| Settings card | Bounded group of related settings |
| Tool card | Framed interactive mini-workflow |

## Anatomy

A card may include eyebrow, title, value, supporting copy, metadata, status indicator, chart preview, action row, and overflow menu. Repeated card sets should use the same anatomy within a view.

## Visual Rules

- Default radius: `radius.2` or 8 px.
- Default padding: `space.5` mobile, `space.6` desktop.
- Use borders or low elevation for separation.
- Avoid heavy shadows, glows, ornamental gradients, and stacked card frames.
- Keep card headings compact; reserve hero-scale text for real hero contexts.

## States

Cards may define default, hover, active, selected, focused, disabled, loading, empty, warning, and error states depending on interactivity.

## Implementation Guidance

- Make the whole card clickable only when there is one clear destination.
- Put destructive or secondary actions in explicit controls, not hidden full-card gestures.
- Keep card content order stable across loading and filled states.
- Use AI Purple only when the card communicates AI-generated insight.

## Acceptance Criteria

- Cards group meaningful content rather than decorating the page.
- Repeated cards remain scannable across mobile and desktop.
- Interactive affordances are explicit and accessible.
- AI, warning, loading, and error states are distinguishable without color alone.

## References

- core/SPEC.md
- specs/02-design/radius-and-elevation.md
- specs/05-ai/insight-types.md

## Woven app reading cards

The [App Visual Specification](app-visuals.md) adopts opaque mint `#E9F3EF` light cards and opaque ink `#192D38` dark cards over yarn, with 14-unit padding/radius and a 1-unit decorative copper outline. These are named app-local aliases. Required control outlines and focus indicators use tested roles.

Your Progress is a bounded exception: three display-only metric tiles inside one progress group. Tiles contain their own label/value and may show the existing New indicator; they do not become independent nested tool cards. Timeline uses one reading panel with rows; charts and findings use opaque reading cards. The transparent dark capture-widget group follows its separate visual contract.

## Version History

- v2.6.0: Integrates the approved screenshot-matched woven app visual contract.
- v1.2.0: Adds card types, anatomy, visual rules, states, and usage limits.
- v1.0.0: Initial repository baseline.
