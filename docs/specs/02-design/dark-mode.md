# Dark Mode & Accessibility

Status: Approved for PL-OS v2.4.0
Owner: Design System Working Group / Engineering Working Group
Last updated: 2026-09-14
Decision record: [RFC-0006](../../rfc/0006-dark-mode-accessibility.md)

## Purpose and accessibility target

Dark mode should feel calm, readable, and recognizably Plectara. Preserve the existing typography, spacing, rounded geometry, and woven identity. Use the ink foundation with ivory text and jade actions. Dark appearance must support the same tasks, information, and recovery paths as light appearance.

PL-OS uses **WCAG 2.2 Level AA as its technical accessibility target**. For native software, apply the relevant criteria using [WCAG2ICT](https://www.w3.org/TR/wcag2ict/). This specification covers appearance and related interaction requirements; it does not replace the full accessibility requirements or establish an ADA compliance determination. See [DOJ accessibility guidance](https://www.ada.gov/resources/web-guidance/) for the distinction between automated checks and a broader evaluation.

The requirements below apply in both themes unless a dark value is specified. Existing palette values remain unchanged.

## Contrast rules

| Content | Required minimum | How to apply it |
| --- | --- | --- |
| Body text, labels, values, placeholders, helper and validation text | 4.5:1 | Measure against the background directly behind the text |
| Qualifying large text | 3:1 | WCAG large text is at least 18 pt regular or 14 pt bold; on web, 24 CSS px or about 18.67 CSS px bold. For native UI, use 4.5:1 unless equivalent rendered size is established |
| Essential icons, chart marks, control and state indicators | 3:1 | Measure against relevant adjacent colors |
| Decorative separators and genuinely disabled controls | Exempt under the applicable contrast criteria | Do not classify helper text, read-only values, unselected tabs, or empty enabled inputs as disabled |

Thresholds use unrounded ratios. A displayed 4.50 can still fail if the underlying value is below 4.5. Prefer additional margin for small text and thin strokes. A 7:1 text target is an optional enhanced treatment, not the AA minimum. [Text contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

A boundary needs 3:1 when it is required to identify a control or its state. Decorative card edges do not automatically need 3:1. Adjacent parts needed to interpret a chart do. [Non-text contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Surfaces and color roles

Use `assets/tokens/color.tokens.json` and the generated theme adapters. Color names such as `stateInfo`, `aiPurple`, or `slate` do not guarantee suitability for dark UI: resolve the role for the current theme.

| Role | Dark value | Use |
| --- | --- | --- |
| `background` | `#192D38` | Page canvas |
| `surface` | `#223D49` | Cards, navigation, dialogs, sheets, standard inputs |
| `surfaceMuted` / `selected` | `#264C4B` | Nested groups and selected containers; selection also needs a visible cue |
| `text` | `#FAF8F4` | Body copy, headings, health values, input content |
| `textSecondary` | `#B8CBCB` | Supporting text, placeholders, chart labels, unselected navigation |
| `primary` / `onPrimary` | `#76B7A5` / `#192D38` | Filled primary action and its label or icon |
| `primaryHover` | `#8DC7B7` | Hovered or pressed primary fill, retaining `onPrimary` |
| `link` | `#8DC7B7` | Inline links, active navigation text, secondary button labels |
| `border` | `#8DA4A6` | Required input boundaries and outlined controls |
| `divider` | `#3C5762` | Decorative separators only |
| `focus` | `#76B7A5` | Focus and selected outlines |
| `success` / `warning` | `#87CBA7` / `#EAC477` | State text and icons |
| `critical` / `info` | `#FFAAAA` / `#8BCDE4` | Errors, important warnings, and information |
| `ai` | `#B7A7FF` | AI text, icons, and explicitly AI-derived chart content |

Use spacing, grouping, and these surfaces for depth. Where a boundary carries meaning, add the appropriate outline; shadow alone is insufficient. Dialogs and sheets retain an opaque `surface` background, with the scrim behind them. Do not brighten nested surfaces arbitrarily: a consuming app's `#2F5560` surface reduces approved AI text to 3.8564:1. Every added surface needs measured text, control, and state pairs before adoption.

The full-color logo keeps its exact colors and jade head. Use the supplied reversed wordmark on dark surfaces. Logo colors do not become UI text colors by association.

## Component and state contract

| Component / state | Required treatment |
| --- | --- |
| Primary button, default | `primary` fill with `onPrimary` text and icon |
| Primary button, hover / pressed | `primaryHover` fill with `onPrimary`; preserve size and label |
| Secondary / text button | `link` label on a tested surface; hover / pressed may use `selected` fill with `text` label |
| Secondary / information filled action | When a component uses these filled variants, pair `link` or `info` fill with `onPrimary` |
| AI filled action | `ai` fill with `onPrimary`; this pairing is separately tested in each theme |
| Destructive filled action | `critical` fill with `onPrimary`; include explicit action wording |
| Input, enabled / read-only | `surface` or `surfaceMuted` fill, `text` content, `textSecondary` hint, `border` boundary; read-only values remain fully readable |
| Input, error | Current theme's `critical` outline, icon, and error text; retain the label and explain how to recover |
| Input, focused error | Keep error text and add distinguishable focus treatment; error color alone cannot identify focus |
| Checkbox / radio / switch | Use theme-resolved `primary` for the selected mark; a mark on a solid primary fill uses `onPrimary`. Verify track, thumb, check, and outline adjacency separately |
| Selected chip / navigation item | `selected` fill, `text` label, `focus` outline or a separate sufficient check/indicator; retain a label and programmatic selected state |
| Unselected navigation | `textSecondary` label and icon; full readability requirements still apply |
| Status / health badge | `surface` or `surfaceMuted` fill and corresponding semantic state text; include a written state and icon |
| Loading | Keep the action name or a clear loading label, expose busy state, and keep any necessary indicator visible |
| Disabled | Expose disabled semantics and explain prerequisites in readable adjacent text when needed; never fade an entire form or its read-only content |

The matrix specifies the resolved colors. Framework defaults, tinting, hover layers, and local overrides must be checked against it. Native widget states are not automatically covered by importing palette constants.

### Focus, links, and interaction

- PL-OS's house treatment for custom focus is a 3 px outline with a 3 px offset on web, or an equivalent unclipped indicator in native logical units. Keep sufficient contrast against its adjacent surface. This geometry is a product standard, not a claim that WCAG AA prescribes those dimensions.
- Keep focused controls visible when a keyboard, sticky header, dialog, or bottom sheet appears. Preserve logical order and return focus after dismissal.
- Underline inline links. Give selected controls a check, shape, outline, or label as well as color, and expose the same state to assistive technology. [Use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).
- Use at least 44 by 44 pt targets on iOS and 48 by 48 dp on Android; Flutter uses logical pixels for layout. PL-OS web controls target 44 by 44 CSS px. These are product/platform targets, distinct from WCAG 2.2 AA's 24 CSS px minimum with exceptions. [Flutter accessibility testing](https://docs.flutter.dev/ui/accessibility/accessibility-testing), [WCAG target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

## Transparency, overlays, and motion

Text, required icons, and control outlines use opaque roles by default. A tint or translucent background requires compositing every layer over the actual base before measuring contrast. Never infer a pass from the source hex alone. Test the least favorable background for gradients, images, blur, and glass; put essential text on an opaque surface when the background is uncontrolled.

AI text on `surfaceMuted` is only 4.5022:1 at full opacity. Do not fade it or add a light state layer behind it. If an implementation needs a tint, provide a tested fixture or use ordinary `text` with an explicit AI label and suitable icon.

Respect reduced motion. Provide opaque alternatives when platform reduced-transparency settings apply; test increased-contrast settings where supported. A separate high-contrast theme is optional; the ordinary light and dark themes must meet the baseline without it.

## Charts and health data

The default two-series chart uses the existing semantic chart aliases:

| Series | Light | Dark | Additional encoding |
| --- | --- | --- | --- |
| `chart-primary` → `primary` | `#287E80` | `#76B7A5` | Solid line and circle markers |
| `chart-secondary` → `textSecondary` | `#506F7E` | `#B8CBCB` | Dashed line and square markers |
| `chart-ai` → `ai` | `#6748D8` | `#B7A7FF` | Only for AI-derived content; explicit AI label |

These colors are tested against approved backgrounds, not against one another. Each series needs a visible label and a distinguishable pattern or marker. For overlapping lines, use separation, a contrasting halo, or direct labels and verify the actual intersections. For stacked/touching areas, test adjacent boundaries or add sufficient separators. New series colors require their own fixtures; do not reuse dark teal or slate logo primitives as untested chart strokes.

Axis labels, units, values, legends, and tooltips use `text` or `textSecondary` on a tested surface. Decorative grid lines may use `divider`; an essential baseline or threshold must remain perceivable. Provide a usable text summary or accessible data table containing the represented values, units, and time range. Tooltips cannot be the only way to obtain information.

## Theme integration and migration

1. Keep System, Light, and Dark choices; default to System and persist an explicit choice. React to system appearance changes while System is selected.
2. Map every used foreground/background pair: primary/onPrimary, secondary/onSecondary, tertiary/onTertiary, error/onError, containers, inverse surfaces, outlines, and all used surface levels. See the [Flutter integration guidance](../01-brand/examples/flutter-theme-snippet.md).
3. Audit explicit colors and alpha values in buttons, inputs, badges, charts, snackbars, and system bars. A `copyWith` theme update does not replace widget-level overrides.
4. Replace legacy light-only state constants and custom untested surfaces. Use the state matrix above and the [component contrast report](plectara-component-contrast-report.md).
5. Check System/Light/Dark switching, text at 200% and supported larger platform sizes, keyboard/switch access, VoiceOver/TalkBack, reduced motion, and increased contrast with synthetic data.
6. Record the app version, source revision, platform, component state, resolved colors, measurements, and manual evidence before release. Follow [Accessibility Testing](../04-engineering/accessibility-testing.md).

## Acceptance criteria

- All used text and non-text combinations meet their applicable thresholds in both themes and every enabled state.
- A new surface, tint, or color override has measured evidence for all content placed on it.
- Health status and chart interpretation remain understandable without color alone.
- Large text fits without clipping or hiding actions; modal and input focus remain operable.
- Automated results and manual workflow evidence identify their scope. Passing palette checks never substitute for app testing.
- Any outstanding failure has an owner and remediation record; accessibility regressions in core workflows block release under the engineering standard.
