# PL-OS v2.1.0 — Consistent logo color and reusable samples

Date: 2026-09-07
Status: Owner-approved standard; publication through the existing Amplify workflow
Change class: Minor — brand usage standards and downloadable assets

## What changes

Every full-color Plectara logo now uses a jade head (`#76B7A5`), on both light and dark backgrounds. The light-background color logo previously had an ink head. The woven geometry, strand palette, transparent separation channels, and approved lettering shapes remain the same.

The lettering is ink (`#192D38`) on light backgrounds and white (`#FFFFFF`) on dark backgrounds. Complete monochrome versions use a single ink or white fill for the head, all strands, and lettering. Inter continues to serve UI and supporting copy; the Plectara lettering remains supplied outlined artwork.

The [brand kit](../../specs/01-brand/plectara-brand-kit.md) now presents nine visual samples: four horizontal logo treatments, three standalone symbols, and two lettering treatments. Each has a direct SVG and transparent PNG download. Stacked, app-icon, avatar, and complete ZIP downloads are also available.

## Migration

Replace cached or copied full-color horizontal, standalone, stacked, social-card, and brand-board files with the current kit. Their source paths stay the same. The dark-background color logo, app icons, and avatars already used jade heads; they retain that treatment.

Keep the jade head when switching themes; change only the lettering between ink and white. For one-color reproduction, choose the whole monochrome logo. Do not combine a jade head with monochrome strands or use an ink head with colored strands.

Earlier reference artwork and v2.0.0 release records remain historical provenance. Use the current `source/` and `png/` files for new work. Existing consumer copies must be refreshed separately from PL-OS.

## Review and validation

The product owner requested the jade-head rule, monochrome examples, lettering standards, and downloadable samples on 2026-09-07. This is a refinement of the established identity and an extension of its usage standards.

The brand validator checks jade heads for every full-color figure, matching fills in monochrome artwork, ink/white lettering, identical lettering outlines, transparent PNGs, platform constraints, source/site equality, inventory hashes, and ZIP contents. Publication also requires a strict documentation build and visual review of the gallery on light and dark backgrounds.

See the [release manifest](manifest.json), [Logo System](../../specs/01-brand/logo-system.md), [Logo Usage](../../specs/01-brand/logo-usage.md), and [Typography](../../specs/01-brand/typography.md).
