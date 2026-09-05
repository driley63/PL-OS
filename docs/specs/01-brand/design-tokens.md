# Design Tokens

Status: Approved for PL-OS v2.0.0
Owner: Brand and Design System Working Groups

## Source and layers

`assets/tokens/color.tokens.json` is the color source of truth. Existing typography, spacing, and radius token files are unchanged.

| Layer | Source example | Consumer example |
| --- | --- | --- |
| Primitive | `brand.teal.hex` | `--plectara-teal` / `PlectaraColors.teal` |
| Theme semantic | `light.primary`, `dark.primary` | `--plectara-color-primary` |
| Component alias | Primary action background | `--plectara-button-primary-background` |
| State | `light.critical`, `dark.critical` | `--plectara-color-critical` |

CSS adapters respond to `data-theme="dark"` or the documentation site's slate theme. Flutter exports provide `PlectaraLightColors` and `PlectaraDarkColors`; consumers select the matching class when building their themes. Raw primitives are for brand artwork, not default component styling.

## Exports

Run `python tooling/build-plectara-tokens.py` to generate:

- `assets/web/plectara-tokens.css`
- `assets/flutter/plectara_colors.dart`
- Documentation-site CSS token copy and contrast report

Existing `assets/web/lifestyleiq-tokens.css`, `--liq-color-*`, and `LifestyleIQColors` remain deprecated compatibility adapters. They preserve imports and identifiers, not old visual colors. JSON legacy primitive names preserve their hex, RGB, HSL, and Flutter fields. The old gradient alias produces solid teal.

New components must use Plectara semantic names. No package or repository identifier is automatically renamed by this migration.

## Change control

Changes to primitive values must include regenerated adapters, contrast results, a visual review in both themes, and migration notes. Breaking changes require major-version review. The AI color reservation remains under ADR-0003; the new brand is recorded in ADR-0011.

See [CSS example](examples/css-tokens.md), [Flutter example](examples/flutter-theme-snippet.md), and [migration guidance](../02-design/plectara-color-migration.md).
