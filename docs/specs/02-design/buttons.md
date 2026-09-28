# Buttons

Status: Released
Owner: Design System Working Group
Version: 2.5.0
Last updated: 2026-09-28

## Purpose

Defines button roles, hierarchy, sizing, content rules, states, and accessibility requirements.

## Scope

- Product buttons, icon buttons, segmented controls, destructive actions, and AI-specific actions
- Mobile, web, and documentation examples
- Future Flutter and web component libraries

## Requirements

- Every view should have one primary action at most.
- Capture widgets use an approved component-specific exception: Capture and Sleep are paired stable entry points and share the same teal fill in branded light mode. Follow the [Widget Visual Specification](capture-widget-visuals.md); do not apply this exception to ordinary app forms.
- Button hierarchy must map to user intent, not visual preference.
- Destructive actions must be visually distinct and require context where risk is meaningful.
- AI actions must be labeled clearly and may use AI Purple only when the action invokes or explains AI behavior.
- Icon-only buttons must include accessible labels and tooltips where the icon is not universally understood.

## Variants

| Variant | Use |
| --- | --- |
| Primary | Main next step in a focused workflow |
| Secondary | Alternative action with similar scope but lower priority |
| Tertiary | Low-emphasis action, usually inline or in a toolbar |
| Destructive | Delete, revoke, reset, or irreversible actions |
| AI | Generate, explain, summarize, or inspect AI-derived content |
| Icon | Compact command where an established icon exists |

## Sizes

| Size | Minimum height | Use |
| --- | --- | --- |
| Compact | 32 px | Dense tables, toolbars, secondary inline actions |
| Default | 40 px | Standard forms and cards |
| Large | 48 px | Primary mobile actions and high-emphasis flows |

Touch targets must be at least 44 by 44 px on mobile, even when the visual button is smaller.

## Content Rules

- Use verb-first labels such as `Save`, `Review`, `Log`, `Export`, or `Compare`.
- Avoid labels that describe UI mechanics instead of user value.
- Keep button labels short enough to fit at mobile widths.
- Use icons only when they clarify the action or save necessary space.
- Do not use full-sentence instructions inside buttons.

## States

Buttons must define default, hover, active, focus-visible, disabled, loading, and success or error feedback when applicable. Loading buttons must preserve width to avoid layout shift.

## Implementation Guidance

- Use `color.brand.primary` for standard primary actions.
- Reserve `color.ai.primary` for AI-specific buttons only.
- Use icons from the approved icon library when available.
- Avoid arbitrary gradients on routine product buttons.
- Place primary mobile actions near the task completion point, not only in page headers.

## Acceptance Criteria

- Button hierarchy is clear without relying only on color.
- All interactive states are specified.
- Mobile touch targets meet minimum size requirements.
- AI and destructive actions are visually and semantically distinct.

## References

- core/SPEC.md
- specs/01-brand/color-system.md
- specs/02-design/component-taxonomy.md

## Version History

- v2.5.0: Records the approved paired Capture/Sleep treatment as a widget-specific exception.
- v1.2.0: Adds button variants, sizes, content rules, states, and accessibility requirements.
- v1.0.0: Initial repository baseline.
