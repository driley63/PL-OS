# Insights Presentation — Final Consistency Review

Reviewed: 2026-10-27

Status: Design-reference review complete; approved for publication; app implementation pending

## Result and scope

The [Insights Presentation specification](insights-presentation.md) and its paired references have been aligned with the current PL-OS woven app contract and the consuming app's current theme/component source. The approved goal-led hierarchy, stomach icon, consistent goal footers, progressive disclosure, and automatic plan tracking remain the design direction.

This review found and corrected drift in shared chrome and controls. It did not treat the new Insights hierarchy as something already implemented in the app. The references remain browser-rendered design artifacts, with their original approved sources retained in the reference tooling's history folder.

## Corrections made

| Area | Correction | Governing contract |
| --- | --- | --- |
| Primary actions | Use teal/white in light and jade/ink in dark. Filter-selection fills are no longer reused for generic primary buttons. Preserve the attention treatment in End Plan confirmation. | [Buttons](../02-design/buttons.md); native filled-button theme |
| Navigation | Restore the current Material icon variants, 12/18 labels, selected 600 weight, correct dark pill and jade label, and the existing dark selection outline. | Native app shell and navigation theme; [App Visual Specification](../02-design/app-visuals.md) |
| Header | Restore the 124-unit Today logo, 60-unit toolbar, protected header-control backing, and fading copper rule. Keep Preferences separate from Insights Options. | Existing app geometry/chrome and PreferencesButton |
| Progress group | Preserve the existing heading/value icons, New badge, neutral/copper tile edges, trailing chevron, and whole-group earned-badges destination. Tiles remain display-only. | Existing RewardsCard; [Cards](../02-design/cards.md) |
| Attention surface | Restore ivory light backing; retain the established dark attention backing. | App-local attention roles |
| Source attribution | Show shared Rule-Derived/device context for local goal results, explicit source context on Today and connection detail, and separate AI-Assisted labeling. | [AI Visual Language](../05-ai/ai-visual-language.md) |
| Control states | Add a visible keyboard-focus treatment, distinguish disabled buttons, and keep all displayed control targets at least 44 × 44 logical units in the reference. | [Accessibility](../02-design/accessibility.md) |
| Export fidelity | Correct selected-chip scrolling at 3× scale and fingerprint font/script/style URLs so refreshed references cannot retain stale glyphs. | Selected-goal visibility and reproducible capture requirements |

All 19 light/dark pairs were recaptured after the shared-style corrections. The screenshot dimensions remain 1179 × 2556, rendered at 3× from the app-only reference surface. Hashes and source provenance are recorded in the [reference manifest](../../assets/app/insights-presentation/approved-2026-10-27/references.json).

## Confirmed agreements

- The app's eleven fixed goal keys and labels match the specification, including **Fewer, Milder Symptoms** and **See If a Treatment Is Working**. Cycle availability and device-only exclusions retain the existing model contract.
- One horizontal **Filter Insights** row contains All Goals and the selected/available fixed goals. Goal summary footers consistently use **Explore more about [Goal Name]**. Log types remain evidence/Timeline context.
- Reading cards retain 14-unit padding/radius, 12-unit gutters/gaps, opaque ivory/ink surfaces, and canonical woven artwork. The layout adds no nested framed cards beyond the existing display-only Progress tiles.
- Native semantic AI foregrounds match the reference. Purple remains confined to AI meaning. Local comparisons and possible connections are not presented as AI-authored or proven causes.
- Light and dark variants contain the same values, counts, limitations, labels, and navigation destinations. Missing historical sample counts remain explicit; they are not replaced with fabricated denominators.
- Pause/Resume and End retain the approved outlined-button treatment. Record-completeness symbols remain derived statuses rather than editable checkboxes.

## Intentional design extensions

The goal icon backings, stomach silhouette, takeaway-first card hierarchy, consistent footer, quieter internal divider, comparison bars, and concise AI review are approved Insights-specific extensions. They must be implemented through named component roles and shared components. They do not authorize a global restyle or replace existing shell/navigation/control roles.

The future plan states, selected-goal routes, contextual chat navigation, and evidence-version handling are written implementation requirements. The reference's fixture interactions and sample replies do not prove those features exist in the current app.

## Verification evidence

The [consistency audit](../../assets/app/insights-presentation/approved-2026-10-27/consistency-audit.json) records 32 matches to PL-OS theme aliases, all 11 goal labels, 11 native geometry values, and 39 passing reference-specific contrast pairs. It records hashes of the current app source used for comparison. These color checks include the new goal/AI backings, chart marks, attention controls, selected navigation, and header controls composited over the brightest possible image.

The [capture observations](../../assets/app/insights-presentation/approved-2026-10-27/capture-observations.json) verify loaded fonts/artwork/icons, fixed export dimensions, and no main-content horizontal overflow for all 38 captures. Light/dark main-content text was compared per scene. The [target audit](../../assets/app/insights-presentation/approved-2026-10-27/target-audit.json) checks 684 displayed controls across the 19 scenes in both themes. The [selected-goal audit](../../assets/app/insights-presentation/approved-2026-10-27/selected-goal-audit.json) verifies the selected chip is fully visible in all ten selected-goal captures. Cancellation of the End Plan confirmation was exercised and preserved the active plan while returning focus to the triggering control.

The strict documentation build, existing 140 component-contrast checks, six contrast regression tests, brand asset validation, screenshot packaging, and whitespace checks passed. Representative final captures were visually inspected in addition to the per-scene checks.

Current app source reviewed: `plectara_app_visuals.dart`, `app_theme.dart`, `plectara_tokens.dart`, `app_shell.dart`, `reading_card.dart`, `woven_backdrop.dart`, `copper_rule.dart`, `preferences_button.dart`, `rewards_card.dart`, `badge_detail.dart`, and `onboarding_options.dart`. The runtime simulator connection timed out, so this review does not claim a fresh native-device visual comparison. The source contracts and the browser references were inspected directly.

Native 48 dp Android targets, platform safe areas, 200% text scaling, localization, VoiceOver/TalkBack, real data/persistence, and production analysis/consent behavior remain the consuming app's acceptance work. A passing screenshot/documentation audit is not native accessibility or clinical certification.

## Related review material

- [Paired high-fidelity gallery](../../assets/app/insights-presentation/index.html)
- [Approved decision](../../adr/0017-adopt-goal-led-insights-presentation.md)
- [Native acceptance criteria](insights-presentation.md#acceptance-criteria)
