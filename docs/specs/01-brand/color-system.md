# Color System

Status: Approved for PL-OS v2.6.0
Owner: Brand Working Group
Last updated: 2026-10-27
Shared component registration: Approved; unreleased

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

The [Dark Mode & Accessibility standard](../02-design/dark-mode.md) defines surfaces, component states, transparency, charts, and the WCAG 2.2 AA engineering target. It extends this palette without changing the approved brand colors.

Light actions use teal with white labels; dark actions use jade with ink labels. Supporting text and links use adjusted tones so they remain legible on muted surfaces. Copper and jade are not suitable defaults for small text on white. Borders required to identify controls use the border role, not the decorative divider role.

## State and AI meaning

Success, warning, critical, and informational states have separate light/dark values. Pair every state with text, icons, or another non-color cue. Purple remains reserved for AI under ADR-0003: the identity primitive is `#7B61FF`; readable AI text uses `#6748D8` in light mode and `#B7A7FF` in dark mode.

Do not use purple for generic premium styling, navigation, or unrelated chart series. Charts must retain labels and distinguishable line styles or markers; these palette checks do not establish pairwise chart-series contrast.

## Verification and governance

The build checks 64 declared text/control pairs. See [contrast results](../02-design/plectara-contrast-report.md). This is not a complete accessibility audit of a consuming app.

An additional [152 component checks](../02-design/plectara-component-contrast-report.md) cover enabled states, hints, chart strokes, selected surfaces, and filled actions. Added surfaces and composited treatments require separate measurements.

Change colors in the JSON source, regenerate adapters, check the preview in both themes, and update migration notes. [ADR-0011](../../adr/0011-adopt-plectara.md) supersedes the previous palette. Historical release records preserve the old values.

## Woven app component aliases

The [App Visual Specification](../02-design/app-visuals.md) reuses the approved palette and saved yarn through local reading-card, navigation, chart, attention, and control-outline roles. [App design values](../../assets/app/plectara/app-visual-tokens.json) and measured fixtures define those variants without changing foundation primitives. Horizontal ink shading protects header content; it is not a new logo fill or replacement signature gradient.

## Shared component colors

The owner approved central registration of the existing Insights and Preferences supporting colors on October 27, 2026. They live in `component` within `assets/tokens/color.tokens.json`, alongside the foundation themes. This registers five previously unregistered shades; the light divider already used an approved app color. It does not recolor the approved designs or add brand primitives.

| Shared role | Light | Dark | Permitted use |
| --- | --- | --- | --- |
| `component.iconBacking` | `#E9F1ED` | `#24423F` | Small goal/section icon containers and non-causal relationship bands; pair with theme text or link foregrounds |
| `component.aiBacking` | `#F0ECF8` | `#263146` | Soft AI-specific backing; pair with the semantic AI foreground; never generic feature emphasis |
| `component.quietDivider` | `#D8DEDA` | `#45616A` | Decorative internal separators on opaque reading surfaces; never a required control boundary or focus indicator |

Use the generated `--plectara-component-icon-backing`, `--plectara-component-ai-backing`, and `--plectara-component-quiet-divider` variables, or the corresponding properties on `PlectaraLightComponentColors` / `PlectaraDarkComponentColors`. Insights and Preferences reference builders resolve the same registry. Consuming-app adoption remains implementation work.

The component contrast report includes 12 additional checks for text, supporting text, links and AI foregrounds on these backings across both themes. The divider remains decorative and has no claim of meeting control-boundary contrast.
