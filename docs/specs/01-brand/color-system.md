# Color System

Status: Approved for PL-OS v2.0.0
Owner: Brand Working Group
Last updated: 2026-09-04

## Palette

| Primitive | Value | Purpose |
| --- | --- | --- |
| Teal | `#287E80` | Brand anchor and light-theme primary actions |
| Jade | `#76B7A5` | Woven strand and dark-theme primary actions |
| Copper | `#C88764` | Woven strand and decorative brand accents |
| Ink | `#192D38` | Main text, app tile, and dark foundation |
| Slate | `#567788` | Woven strand and supporting brand graphics |
| Ivory | `#FAF8F4` | Light canvas and reversed text |

The approved identity uses flat fills, not the former lime-to-teal gradient. The four colored strands represent distinct signals forming a more complete picture of a person. Their hues are not health scores or clinical categories.

## Semantic colors

Product components must use semantic roles from `assets/tokens/color.tokens.json`, not logo primitives directly. [Component migration](../02-design/plectara-color-migration.md) defines the roles; the [live preview](../02-design/plectara-component-preview.md) shows both themes.

Light actions use teal with white labels; dark actions use jade with ink labels. Supporting text and links use adjusted tones so they remain legible on muted surfaces. Copper and jade are not suitable defaults for small text on white. Borders required to identify controls use the border role, not the decorative divider role.

## State and AI meaning

Success, warning, critical, and informational states have separate light/dark values. Pair every state with text, icons, or another non-color cue. Purple remains reserved for AI under ADR-0003: the identity primitive is `#7B61FF`; readable AI text uses `#6748D8` in light mode and `#B7A7FF` in dark mode.

Do not use purple for generic premium styling, navigation, or unrelated chart series. Charts must retain labels and distinguishable line styles or markers; these palette checks do not establish pairwise chart-series contrast.

## Verification and governance

The build checks 64 declared text/control pairs. See [contrast results](../02-design/plectara-contrast-report.md). This is not a complete accessibility audit of a consuming app.

Change colors in the JSON source, regenerate adapters, check the preview in both themes, and update migration notes. [ADR-0011](../../adr/0011-adopt-plectara.md) supersedes the previous palette. Historical release records preserve the old values.
