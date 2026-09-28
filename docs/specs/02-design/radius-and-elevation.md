# Radius and Elevation

Status: Approved for PL-OS v2.6.0
Owner: Design System Working Group
Version: 2.6.0
Last updated: 2026-09-28

## Purpose

Defines corner radius, borders, shadows, layering, and surface separation rules.

## Scope

- Product cards, panels, controls, modals, sheets, menus, and data containers
- Mobile, web, and documentation examples
- Visual hierarchy and accessibility review

## Requirements

- Default UI cards use 8 px radius unless a platform component or approved named variant requires a different value.
- Buttons, inputs, chips, and controls must use stable tokenized radii.
- Elevation must communicate layering or interaction, not decoration.
- Do not use nested cards as a page-section layout strategy.
- Shadows must remain subtle enough for dense operational screens.

## Radius Scale

| Token | Value | Use |
| --- | --- | --- |
| `radius.0` | 0 px | Tables, charts, flush containers |
| `radius.1` | 4 px | Small chips, badges, compact fields |
| `radius.2` | 8 px | Default cards, panels, buttons, inputs |
| `radius.3` | 12 px | Sheets, prominent panels, mobile surfaces |
| `radius.4` | 16 px | Dialogs and limited high-emphasis containers |
| `radius.full` | 999 px | Circular avatars, pills, progress handles |

## Elevation Scale

| Token | Use |
| --- | --- |
| `elevation.0` | Flat surfaces and dense dashboard panels |
| `elevation.1` | Interactive cards or controls on same-level backgrounds |
| `elevation.2` | Sticky headers, menus, popovers |
| `elevation.3` | Modals, sheets, and blocking overlays |

## Surface Rules

- Prefer border and background contrast over heavy shadow in dense views.
- Use elevation for temporary layering such as menus, popovers, modals, and sheets.
- Keep report, chart, and data cards calm; avoid glow, bokeh, or ornamental depth.
- Use consistent radius within a component family.
- Avoid combining strong border, shadow, gradient, and high radius on the same component.

## Implementation Guidance

- Map radius and elevation to design tokens before production use.
- Test elevation in light and dark themes.
- Verify focus rings remain visible when applied to rounded controls.
- Document any radius larger than 16 px for product UI.

## Acceptance Criteria

- Radius and elevation values map to named tokens.
- Layering communicates state, priority, or interaction.
- Dense screens avoid decorative stacking and nested cards.
- Focus, hover, active, and modal states remain visible.

## References

- core/SPEC.md
- specs/02-design/cards.md
- specs/02-design/buttons.md

## Approved woven app geometry

The [app visual variant](app-visuals.md) uses named local aliases: 14-unit reading cards, 9-unit tiles/buttons, 12-unit Log corners, and a 28-unit Quick Log pill. Thin copper edges are decorative; required control/focus boundaries use tested roles. The phone's 26-unit preview mask is presentation framing and does not replace native device masks.

Opaque reading cards separate content from the photo without heavy shadow or layered decorative frames. Only Your Progress uses the approved display-only metric group exception. Foundation radius and elevation tokens remain the baseline for other variants.

## Version History

- v2.6.0: Integrates the approved screenshot-matched woven app visual contract.
- v1.2.0: Adds radius scale, elevation scale, and surface rules.
- v1.0.0: Initial repository baseline.
