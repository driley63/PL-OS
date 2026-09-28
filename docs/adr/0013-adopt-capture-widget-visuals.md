# ADR-0013: Adopt the Plectara capture widget visuals

Status: Accepted for repository implementation
Date: 2026-09-28
Owner: Design System Working Group

## Decision

Adopt the owner-approved revision 13 as the visual reference for branded home screen Capture widgets. Use the saved gentle-focus yarn across the widget, horizontal ink shading beneath the unchanged logo, a soft copper rule, one mint light card or transparent copper outlined dark card, matching teal/white Capture and Sleep in light mode, and title case quick action labels.

Large includes acknowledged saved confirmation and does not include Edit. The pair of equally filled stable entry points is a widget-specific exception to the general single-primary-button guidance. The local card geometry is recorded without modifying global spacing or radius scales.

## Rationale

The yarn makes the surface recognizably Plectara. The gradient protects lettering while the card gives action text controlled backgrounds. A gentler focus progression avoids the abrupt blur transition in earlier concepts. Matching light Capture/Sleep buttons makes the stable entry points easier to scan. Removing Edit aligns the mockup with the production feature set.

## Consequences

- [Capture Widgets](../specs/02-design/capture-widgets.md) and [Widget Visual Specification](../specs/02-design/capture-widget-visuals.md) govern the component together.
- Screenshots, exact textures, source records, design values, and a downloadable kit are part of PL-OS.
- Default rendering follows system appearance. Accented/clear and accessory modes need native adaptation; full-color screenshots do not define those system materials.
- Individual screenshots are implementation references, not finished app code or evidence of native accessibility.
- Original artwork and the earlier fallback remain distinct from the accepted focus derivative. Routine reuse must not regenerate the approved asset.

This decision is accepted from the owner's review and PL-OS integration request. It does not publish or deploy the native application. See [RFC-0007](../rfc/0007-capture-widget-visuals.md).
