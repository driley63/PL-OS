# Plectara app visual kit

Status: Owner-approved design reference; PL-OS v2.6.0 release
Approval date: 2026-09-28

The [App Visual Specification](https://pl-os.plectara.com/specs/02-design/app-visuals/) defines the approved woven shell and screenshot-matched Today, Timeline, Charts, and Insights in both themes. [ADR-0014](https://pl-os.plectara.com/adr/0014-adopt-woven-app-visuals/) records the accepted exceptions.

## Files

- `previews/`: eight populated-screen PNGs, two empty Today PNGs, and four comparison sheets, exported at 2× illustrative composition size.
- `reference/approved-mockup-fragment.html`: exact approved editable review source, with embedded yarn/logo/font.
- `reference/approved-app.html`: standalone, offline-capable reference with the icon library embedded. Bottom navigation switches both themes. Appearance, filters, timeframe, and local dialogs support review only.
- `textures/`: exact gentle-focus WebP (900 × 700) and PNG (1422 × 1106) reused from the approved capture widget kit.
- `logos/`: canonical full-color reversed lockup, unchanged.
- `fonts/`: native Inter variable font, the review subset, and SIL OFL license.
- `app-visual-tokens.json`: app-local colors, crop, header gradient, divider, geometry, and typography.
- `adapters/`: generated component-color CSS and Flutter mapping examples.
- `specification.md`: bundled copy of the canonical specification, with local asset links.
- `source/`: owner approval, provenance, original pattern approval, and edit prompts.
- `verification/`: browser checks, offline reference checks, and measured app-local color pairs.
- `manifest.json`: file dimensions, sizes, and SHA-256 checksums.
- `plectara-app-visuals-v1.zip`: reproducible download containing the kit and manifest.

## Reuse

Keep the photo vibrant and reuse the exact saved texture. The shade is horizontal, darker on the left. Light uses opaque mint reading cards; dark uses opaque ink. Copper card/tile edges and horizontal rules are decorative. Required control outlines and state/focus cues use tested roles.

Render real logo artwork, live text, real chart data, and native controls. Do not flatten an app screen into a background image. Foundation tokens remain governed by their own source; these aliases apply to the woven app variant. The capture widget's dark grouping has a separate transparent treatment.

## Reference limits

The owner supplied the app screenshots and approved this visual review for PL-OS. Their displayed names, medication quantities, dates, cycle estimate, progress totals, findings, and chart summaries are review fixtures, not a clinical dataset or production defaults. The chart geometry was visually traced. Unseen data, selector options, and workflows are not specified by the reference.

Phone framing and OS decoration are presentation context. Native safe areas, device heights, System/Light/Dark preferences, text scaling, localization, VoiceOver/TalkBack, and state/contrast checks remain required in the consuming app. Browser measurements do not certify ADA compliance.

## Packaging

Run `python tooling/build-app-visual-kit.py` from the repository root. It verifies exact artwork and review-source approval, refreshes adapters/contrast fixtures and bundled specification, writes a deterministic ZIP and checksum manifest, and mirrors the kit to `docs/assets/app/plectara/`. It does not regenerate artwork or screenshots.
