# Layout Grid

Status: Released
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-08-04

## Purpose

Defines responsive layout rules, grid structure, content widths, and screen organization for Plectara product surfaces.

## Scope

- Mobile, tablet, and desktop product layouts
- Dashboards, timelines, reports, forms, settings, and onboarding flows
- Documentation examples and design-system component previews

## Requirements

- Layouts must support repeated daily use before editorial expression.
- Primary workflows must remain visible without requiring users to decode decorative layout.
- Important health data must not be split across unrelated visual regions.
- Responsive changes must preserve content order and relationship.
- Layouts must support keyboard, screen reader, and zoom behavior.

## Breakpoints

| Token | Range | Use |
| --- | --- | --- |
| `layout.mobile` | 0 to 599 px | Single-column flows, bottom-safe controls |
| `layout.tablet` | 600 to 1023 px | Two-column opportunities, persistent side context |
| `layout.desktop` | 1024 px and up | Multi-column dashboards, side navigation, comparison views |

## Grid Rules

- Mobile uses one content column with 16 px default gutters.
- Tablet may use two columns only when content remains independently understandable.
- Desktop dashboards may use 12-column grids, but cards should align to clear 3, 4, 6, or 12 column spans.
- Reading pages should use a constrained text column rather than full-width paragraphs.
- Charts should align with the content grid but preserve axis labels and legends.

## Page Structure

| Region | Requirement |
| --- | --- |
| Navigation | Stable location and predictable labels |
| Primary content | One clear task or decision focus per view |
| Secondary content | Adjacent context, filters, metadata, or supporting insights |
| Actions | Primary action visible near the relevant decision point |
| System status | Non-blocking status visible without covering core content |

## Layout Constraints

- Do not place operational dashboards inside decorative hero layouts.
- Do not nest UI cards inside other cards.
- Use full-width bands or unframed layouts for page sections.
- Preserve visible next-step content on onboarding and report pages.
- Keep fixed-format elements stable with explicit dimensions or aspect ratios.

## Implementation Guidance

- Use CSS grid, Flutter layout primitives, or design-system grid helpers instead of manual absolute positioning.
- Prefer responsive constraints over viewport-scaled type.
- Test long labels, empty states, loading states, and error states at each breakpoint.
- Document any layout exception that changes content order across breakpoints.

## Acceptance Criteria

- Layout behavior is defined for mobile and desktop.
- Primary actions and health interpretation remain clear at all supported widths.
- Text and controls do not overlap or resize unpredictably.
- Layout choices reinforce the workflow rather than brand decoration.

## References

- core/SPEC.md
- specs/02-design/spacing-system.md
- specs/02-design/accessibility.md

## Version History

- v1.2.0: Adds breakpoints, grid rules, page structure, and layout constraints.
- v1.0.0: Initial repository baseline.
