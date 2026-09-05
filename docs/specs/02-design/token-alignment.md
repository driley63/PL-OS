# Token Alignment Review

Status: Released
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-08-04

## Current palette authority

This is the historical v1.2.0 alignment review. Its old primitive names and gradient allowance are superseded by [Plectara color migration](plectara-color-migration.md) and Brand Identity v2.0.0. The new flat palette, generated CSS/Flutter adapters, and [contrast report](plectara-contrast-report.md) are current. Foundation-token ownership and component rules below still apply.

## Purpose

Documents the Volume 02 review against released Volume 01 Brand Identity tokens. This review makes token dependencies explicit before v1.2.0 is promoted from draft to released.

## Scope

- Design Language foundations, components, charts, icons, states, and accessibility rules
- Released Volume 01 color, typography, and design-token requirements
- Reviewable guidance for future CSS, Flutter, Figma, iOS, and Android mappings

## Review Outcome

Volume 02 is aligned with Volume 01 Brand Identity v1.1.0. No released Brand Identity token values need to change for v1.2.0.

The review adds one clarification: Volume 02 may define design-system foundation tokens such as spacing, radius, elevation, motion, layout, and component aliases, but product implementations must still resolve brand-owned color, typography, AI, and state meaning through the released Volume 01 token model.

## Required Alignment Rules

- Product UI must use semantic color roles before primitive color values.
- Component aliases must resolve through semantic or foundation tokens, not directly to one-off raw values.
- AI Purple must resolve through `color.ai.primary` and must only indicate AI-generated, model-assisted, or confidence-related behavior.
- Routine product buttons, dense charts, data cards, and repeated workflows must not use the signature brand gradient.
- Typography must inherit the approved Inter strategy and platform fallbacks from Volume 01.
- Color, typography, spacing, radius, elevation, motion, and icon tokens must remain portable to CSS, Flutter, Figma, iOS, and Android naming conventions.

## Brand Token Mapping

| Volume 01 token or rule | Volume 02 usage | Review decision |
| --- | --- | --- |
| `color.brand.primary` | Primary actions, active controls, selected states, and brand-accented product affordances | Allowed for standard product emphasis; do not use as decorative fill everywhere |
| `color.brand.highlight` | Positive emphasis, progress highlights, and limited supportive accents | Allowed when contrast is verified; do not use for small text on white |
| `color.text.primary` | Headings, body copy, labels, and dense health information on light surfaces | Required before raw Deep Navy values in product UI |
| `color.text.secondary` | Metadata, helper text, secondary labels, and quiet supporting information | Required before raw Slate Blue values in product UI |
| `color.ai.primary` | AI buttons, AI insight cards, confidence indicators, AI chart overlays, and AI icons | Required for AI-specific meaning only |
| `color.state.info` | Informational banners, neutral system guidance, and non-critical status context | Allowed with text or icon support |
| `color.state.warning` | Attention states that are unusual but not blocking | Allowed with accessible non-color cues |
| `color.state.critical` | Errors, destructive actions, blocked validation, and high-risk alerts | Required for destructive or critical meaning, with plain-language copy |
| Signature gradient | Onboarding, empty-state brand moments, app store graphics, and large identity surfaces | Not allowed for routine buttons, dense charts, card decoration, tables, or body text |
| Inter typography strategy | Product type styles, component labels, form text, chart labels, and documentation examples | Required; platform fallbacks must follow Volume 01 |

## Design-System Token Responsibilities

| Token family | Owner | Volume 02 responsibility |
| --- | --- | --- |
| `space.*` | Design System Working Group | Define product spacing scale and map it to platform exports |
| `layout.*` | Design System Working Group | Define responsive breakpoints and content constraints |
| `radius.*` | Design System Working Group | Define reusable shape tokens for controls, cards, panels, and overlays |
| `elevation.*` | Design System Working Group | Define layering semantics without ornamental depth |
| `motion.*` | Design System Working Group | Define duration tokens and reduced-motion behavior |
| `component.*` | Design System Working Group | Define aliases that resolve through approved brand or foundation tokens |
| `icon.*` | Design System Working Group | Define product icon sizing, stroke, state, and color aliases |

## Component Alias Guidance

| Component alias | Must resolve through | Notes |
| --- | --- | --- |
| `component.button.primary.background` | `color.brand.primary` | Standard primary action only |
| `component.button.ai.background` | `color.ai.primary` | AI-specific action only |
| `component.button.destructive.background` | `color.state.critical` | Destructive or irreversible action |
| `component.card.insight.accent` | `color.ai.primary` or a non-AI semantic state token | Use AI color only when the insight is AI-generated |
| `component.chart.ai.overlay` | `color.ai.primary` | Pair with labels, patterns, or annotations |
| `component.state.warning.accent` | `color.state.warning` | Must include text or icon cues |
| `component.state.error.accent` | `color.state.critical` | Must include recovery guidance |
| `component.icon.default.color` | semantic icon token mapped to text or state color | Do not use raw hex values |

## Review Findings

- No Volume 02 document introduces conflicting brand color values.
- Volume 02 correctly reserves AI Purple for AI-specific controls, overlays, icons, and insight surfaces.
- Volume 02 correctly prohibits decorative gradients in routine product buttons, dense charts, and cards.
- Spacing, radius, elevation, layout, and motion scales are Design System foundation tokens and do not conflict with Volume 01 token ownership.
- Typography remains dependent on Volume 01; Volume 02 does not introduce a competing typeface or type scale.
- Future generated CSS, Flutter, Figma, iOS, and Android exports remain pending implementation artifacts.

## Acceptance Criteria

- Reviewers can trace every Volume 02 color decision back to a Volume 01 semantic role.
- New component aliases identify the semantic or foundation token they resolve through.
- AI, warning, error, and success states remain understandable without color alone.
- Design-system foundation tokens can be exported without changing released Brand Identity values.
- Any future raw color, typography, spacing, radius, elevation, or motion value documents an explicit exception.

## References

- specs/01-brand/color-system.md
- specs/01-brand/design-tokens.md
- specs/01-brand/typography.md
- specs/02-design/SPEC.md

## Version History

- v1.2.0: Adds Volume 02 token alignment review against Brand Identity v1.1.0.
