# Iconography

Status: Released
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-08-04

## Purpose

Defines product icon style, sizing, usage, accessibility, and relationship to Brand Identity icons.

## Scope

- Product UI icons, navigation icons, state icons, chart icons, and AI icons
- Mobile, web, and documentation examples
- Future component libraries and icon inventories

## Requirements

- Product icons must be simple, familiar, and functional.
- Use approved icon libraries when possible before creating custom icons.
- Icons must not replace text for unfamiliar or health-sensitive actions.
- AI icons must be visually associated with AI behavior and may use AI Purple.
- Brand logo assets must not be reused as generic product icons.

## Style

| Attribute | Standard |
| --- | --- |
| Base size | 24 px |
| Compact size | 16 or 20 px when labels remain readable |
| Stroke | 1.75 to 2 px for outline icons |
| Corners | Rounded where the source library supports it |
| Fill | Use sparingly for selected or high-emphasis states |
| Color | Semantic icon tokens, not raw hex values |

## Usage Rules

- Pair unfamiliar icons with text labels or tooltips.
- Use icon-only controls only for established actions such as close, search, edit, delete, download, or settings.
- Do not invent medical or clinical symbols without governance review.
- Use state icons consistently for success, warning, error, info, and AI.
- Avoid decorative icon clusters in dense product surfaces.

## Accessibility

- Decorative icons should be hidden from assistive technology.
- Meaningful icons must have accessible names or adjacent text.
- Icon color must not be the only state indicator.
- Icon buttons must meet focus and touch target requirements.

## Implementation Guidance

- Prefer shared icon components that enforce size, stroke, color, and accessible labeling.
- Review new icon metaphors with Product when they affect health interpretation.
- Keep AI iconography consistent with AI visual language.
- Document custom icons in an icon inventory before production use.

## Acceptance Criteria

- Icons have clear purpose and accessible behavior.
- New icon usage maps to component or state needs.
- Brand marks and product icons remain separate.
- AI and health-sensitive icons do not mislead or overstate certainty.

## References

- core/SPEC.md
- specs/01-brand/iconography.md
- specs/02-design/accessibility.md

## Unreleased wearable addition

[ADR-0016](../../adr/0016-adopt-wearable-visuals.md) approves the person outline with an inset health cross for `Log Symptoms` on both wearable platforms. Use the [shared vector motif and rendering rules](wearable-visuals.md#symptom-icon), preserve the adjacent label, and hide the icon from accessibility when the row already names its action. This replaces the concept's wave glyph and does not indicate diagnosis, a clinician or clinical risk. It is a product icon, not the Plectara logo.

## Version History

- Unreleased: Register the approved wearable Log Symptoms motif.

- v1.2.0: Adds product icon style, usage, accessibility, and governance rules.
- v1.0.0: Initial repository baseline.
