# Logo Assets

> Historical assets and naming explorations. The current owner-approved Plectara master and exports are in [`../plectara/`](../plectara/README.md). The legacy files below are retained, but are not used by the PL-OS site.

The SVG files in `source/` are implementation placeholders based on the approved direction. Replace them with production vector masters after final optical refinement.

## Source Files

| File | Role | Status |
| --- | --- | --- |
| `source/lifestyleiq-icon.svg` | Full-color icon source | Reviewed placeholder; not production |
| `source/lifestyleiq-icon-monochrome.svg` | Single-color icon source | Reviewed placeholder; not production |
| `source/lifestyleiq-logo-horizontal.svg` | Horizontal lockup source | Reviewed placeholder; not production |
| `source/liq-os-logo-horizontal.svg` | LIQ OS documentation-site lockup | Reviewed placeholder-derived; not production |

Do not generate production exports from screenshots, prior PNG exports, or manually recreated artwork. Until final optical refinement is approved, generated outputs must remain labeled as placeholder-derived.

See `optical-refinement-review.md` for current review findings and production blockers.

## Required Exports

- Horizontal primary SVG
- Horizontal dark SVG
- Icon-only SVG
- Monochrome black SVG
- Monochrome white SVG
- PNG exports: 16, 32, 48, 72, 96, 120, 144, 152, 180, 192, 256, 512, 1024, 2048
- iOS AppIcon.appiconset
- Android legacy and adaptive icon resources
- Favicons and web manifest icons

## Future Production Structure

When production assets are approved, use this structure:

- `source/`: reviewed source SVG or vector masters
- `generated/`: generated PNG, favicon, and web manifest outputs
- `platform/ios/`: iOS `AppIcon.appiconset`
- `platform/android/`: Android adaptive icon and legacy density outputs
- `inventory.md`: source-to-export traceability table

## Review Requirements

- Preserve accessible SVG titles.
- Confirm icon safe area at 1024 px before generating platform outputs.
- Confirm full-color and monochrome marks on light and dark backgrounds.
- Update `docs/specs/01-brand/asset-production.md` when export requirements change.
