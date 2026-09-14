# Plectara dark mode audit — 2026-09-14

Status: Source audit complete; app remediation and device verification outstanding
Scope: Plectara Flutter source `0.19.0+1`, revision `a5e636b043c3cda8bb96dec8990ade179eabd16f`
Reviewer: Codex, at the product owner's request
Standard: [Dark Mode & Accessibility](../02-design/dark-mode.md)

## Result

The inspected app uses the approved ink/card surfaces, ivory body text, and jade primary buttons, but several component overrides use light-only colors inside the dark theme. The source-resolved combinations below fail their applicable contrast thresholds. This report does not establish which revision is distributed through app stores or determine legal compliance.

The app checkout was clean when inspected. Measurements trace explicit foregrounds, backgrounds, and alpha layers in the listed files; no private user health data was used. No app code was changed by this standards update.

## Confirmed source findings

Priority P1 means address first because it affects health interpretation; P2 means fix in the component remediation pass. Ratios below are calculated from declared colors, not anti-aliased screenshot edges. Each finding must be retested in the actual rendered component after a fix.

| ID / priority | Component and source | Measured result | Required action |
| --- | --- | --- | --- |
| DM-01 / P1 | Health urgency badges: `lib/widgets/insight_card.dart:34–45,93–97` passes light state colors to `lib/widgets/liq_status_badge.dart:27–40` | Text over its 12% state tint on a dark card: critical **1.9526:1**, warning **1.8142:1**, info **1.7795:1**, success **1.7638:1**; text needs 4.5:1 | Resolve each semantic state by brightness. Use an approved opaque badge surface or remeasure the tint. Preserve the written urgency label and icon |
| DM-02 / P2 | Input placeholders: `lib/theme/app_theme.dart:91–93,348–355`; color definitions in `lib/theme/plectara_tokens.dart:35,44` | `#567788` on `#2F5560`: **1.6955:1**; needs 4.5:1 | Use dark `textSecondary` for hints and approved input surfaces; do not treat an empty enabled field as disabled |
| DM-03 / P2 | Error/focused-error borders: `lib/theme/app_theme.dart:376–385` | Light critical `#B53E3E`: **2.0327:1** against the card and **1.4381:1** against the input fill; required error indicator needs 3:1 | Use the theme's dark `critical` / `colorScheme.error`; retain readable error text and distinguish focused error from unfocused error |
| DM-04 / P2 | Selected appearance radios: `lib/theme/app_theme.dart:437–443`; used on a Card in `lib/screens/appearance_screen.dart:72–90` | Light teal `#287E80` on card `#223D49`: **2.3946:1**; needs 3:1 | Resolve the selected mark through `colorScheme.primary`, then verify all states and adjacent colors |
| DM-05 / P2 | Trend chart strokes: `lib/widgets/liq_trend_chart.dart:20,76,103–113` | Brand teal **2.3946:1** and slate **2.3966:1** on dark cards; meaningful strokes need 3:1 | Use theme-resolved `primary` and `textSecondary`, with distinguishable strokes/markers and accessible values; test intersections and tooltip surfaces |
| DM-06 / P2 | AI narrative heading and acknowledgement: `lib/widgets/insight_card.dart:104–114,183–187` | Primitive purple `#7B61FF`: **2.7275:1**; light success `#256F53`: **1.8984:1** on dark cards; text needs 4.5:1 | Use dark `ai` and `success`, or ordinary readable text with explicit labels. Preserve the distinction between AI and rule-derived content |

## Additional integration risks

These are definite failing theme/helper combinations, but this audit did not establish a visible screen using them. They are not counted as additional confirmed screen defects.

- `AppTheme.aiFilledButton` at `lib/theme/app_theme.dart:449–452` pairs white with primitive `#7B61FF`: **4.2033:1**, below 4.5:1 for its normal-sized label. No call sites for this helper were found in `lib/`. Update it before reuse: light `ai` with white, dark `ai` with ink.
- Dark `tertiary` / `onTertiary` at `lib/theme/app_theme.dart:66–67` pair light info `#286A8A` with ink: **2.3876:1**. Map theme-specific info and its foreground together; inspect components that inherit this pair.
- The app adds `surfaceContainerDark = #2F5560` at `lib/theme/plectara_tokens.dart:44`, outside the tested PL-OS surfaces. Approved dark AI text is only **3.8564:1** on it; jade is **3.5096:1**, sufficient for essential non-text marks but insufficient for ordinary text. Adding palette imports alone cannot fix this surface mismatch.
- Existing theme tests check brightness, persistence, and header styling. The inspected `lib/` and `test/` contained no uses of Flutter's `textContrastGuideline`, `iOSTapTargetGuideline`, or `androidTapTargetGuideline`. This is a coverage observation, not proof that every component lacks all accessibility testing.

## Working foundations

- Dark body text on cards measures **10.8085:1**.
- Ink labels on jade primary buttons measure **6.1657:1**.
- Main dark secondary text and standard border roles match PL-OS.
- `lib/main.dart:318–320` wires both themes and the selected mode. `lib/state/theme_controller.dart` defaults to System and persists an explicit choice.
- Urgency badges already include text and icons. Trend cards already show time range, units, latest value, and change summaries; complete chart-data access and assistive-technology behavior still need review.

## Reproduce the measurements

The [JSON evidence](../../assets/audits/plectara-dark-mode-2026-09-14.json) includes the app revision, source-file SHA-256 hashes, exact colors, source locations, and ordered alpha layers. It is a fixed source snapshot, not a scanner of future app revisions.

```bash
python tooling/check-component-contrast.py --fixtures docs/assets/audits/plectara-dark-mode-2026-09-14.json
```

Expected result: **16 measurements, 14 failures and 2 passing control samples**. The 14 failed measurements include two latent helper/theme risks and multiple measurements for some findings; they do not mean 14 independently confirmed screen defects. A nonzero exit status is intentional for this failing evidence set. Badge compositing is calculated in sRGB without intermediate 8-bit rounding; final rendering and quantization may slightly change the displayed ratio without affecting these clear failures.

## Remediation order

1. **Health meaning:** fix urgency badges, AI labels, and acknowledgement text using current semantic roles.
2. **Shared controls:** fix hints, errors, radios, and inherited foreground/background pairs; replace or formally validate the custom nested surface.
3. **Charts:** map theme-aware strokes, verify adjacent series and labels, and provide complete accessible values.
4. **Regression protection:** add real component tests in both modes, then verify focus, disabled/selected states, and large text. Record exact fixtures rather than testing only that `brightness` is dark.
5. **Device review:** run the workflow matrix below against the build proposed for release.

Implementation ownership is the app's theme/component maintainers; a named assignee and retest build should be recorded when the fixes are scheduled. PL-OS's normal core-workflow accessibility release gate applies.

## Remaining device and interaction audit

| Area | Status / required evidence |
| --- | --- |
| Actual store/test build | Not inspected; identify build version and source revision |
| Rendered app states | Not inspected; capture default, selected, pressed, focused, error, and loading states after remediation |
| VoiceOver and TalkBack | Not tested; complete onboarding, logging, validation recovery, chart review, and insights |
| Text scaling | Not tested; verify 200% and supported larger OS settings without clipped values or actions |
| Keyboard / switch access | Not tested; check navigation, focus visibility, modal focus return, and keyboard occlusion |
| System appearance | Source wiring inspected; live OS switching and restore behavior not exercised |
| Increased contrast / reduced motion / reduced transparency | Not exercised on devices |
| Chart interpretation | Source summary exists; full data accessibility, series adjacency, and tooltip operation need manual review |

Record results using [Accessibility Testing](accessibility-testing.md#release-evidence-record). The source audit is complete within this stated scope; full app accessibility verification remains open until these observations are collected.
