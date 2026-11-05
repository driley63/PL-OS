# Insights Presentation — Consistency Review

Reviewed: 2026-11-05
Status: Today design and documentation approved after local review; native implementation and publication pending

## November 5 Today amendment

The [specification](insights-presentation.md#today-insight-region) now defines the approved compact Today overview with every selected fixed goal, one useful preview/status per row and prominent unread cues. Required care context remains above it; the plan follows. The full Insights overview and evidence/AI/plan contracts retain their prior scope.

The [gallery](../../assets/app/insights-presentation/index.html) leads with 14 new app-only captures and retains ten October 27 Insights/evidence/plan images with historical-label notes. The old single-finding Today images are archived, rather than presented as current. [ADR-0019](../../adr/0019-adopt-today-insights-overview.md) and [RFC-0013](../../rfc/0013-today-insights-overview.md) explicitly amend the older hierarchy and review rule.

### Consistency findings resolved

- Updated the controlling Today order and removed the one-highlight limit. The new card's goal rows do not use the full Insights summary-card footer/anatomy; Explore Insights is the compact card's shared footer.
- Reconciled current fixed goal labels against app source: Reduce Symptoms, Improved Digestion, Improved Sleep and Improved Mood. The approved Today icon set includes the stomach silhouette. Old captions are dated historical evidence, not the current catalog.
- Separated raw evidence versions from meaningful review revisions. A routine metrics refresh is not an Updated notification; successful entry to the actual finding reviews only its displayed revision. Shared goal mappings retain one review identity/count.
- Distinguished adequate assessment with no clear pattern, a confirmed missing input and insufficient context. Empty arrays and generic gathering hints cannot establish these states. Failure and stale results retain their own contract.
- Documented light unread Jade fill with deep-green border/icons/badges, preserving the approved dark treatment. The scoped aliases reuse existing palette colors. The lower-contrast ordinary light link color is explicitly excluded on the Jade fill.
- Retained automatic plan status, existing domain templates, care notices, local-only wellbeing exclusions and consent rules. New/Updated is reading state, not AI attribution or evidence maturity.
- Updated product, app-visual, disclosure, confidence/evidence, ADR/RFC and migration guidance. The app visual-kit specification/package is regenerated from its canonical source.

### Artifact and behavior checks

| Check | Result and scope |
| --- | --- |
| Capture inventory | 14 original RGB JPEGs at 1179 × 2556, from the approved 393 × 852 design rendered directly at 3×; no resampling |
| Paired scenes | Initial unread, partial review, all reviewed, two goal-list states, deduplicated unread list, and updated-finding explanation |
| Theme parity | Identical text and fixture state for each of seven light/dark pairs |
| Readiness | Fonts loaded, imagery available, icons rendered, zero unrendered icon placeholders and no horizontal body overflow across all captures |
| Provenance | Approved source fragment, builder/input hashes, capture observations, runtime hashes and image checksums retained; packager validates them before updating galleries |
| Component colors | Ten scoped unread role checks pass: ordinary text at least 6.17:1; essential marks at least 4.10:1; these are resolved component checks, not native accessibility certification |
| Shared checks | 64 generated palette checks, 152 component checks, 37 wearable fixtures, six contrast-validator tests, approved brand validation, widget-kit parity and 60 app visual-kit contrast checks pass |
| Packaged interaction | Two-finding goal opens without review; opening dairy/bloating changes the global count 4→3 once and updates both shared goal rows; the unread list shows three distinct remaining findings |
| Visual review | Approved artwork, card proportions, goal iconography, unread inversion and representative Today/list/update screenshots inspected; both appearances retain matching fixture content |
| Documentation and local preview | Strict MkDocs build passes; the local specification displays the new November 5 image pair and detailed sections; built screenshot bytes match the validated source package |

[Capture manifest](../../assets/app/insights-presentation/today-overview-2026-11-05/references.json), [capture observations](../../assets/app/insights-presentation/today-overview-2026-11-05/capture-observations.json), and [contrast checks](../../assets/app/insights-presentation/today-overview-2026-11-05/contrast-checks.json) are the evidence for this package. Source and capture instructions are in `tooling/today-insights-reference/`; `tooling/package-today-insights-reference.py` owns the current gallery and specification blocks. Older packagers cannot overwrite them.

### Source support and limits

The [November 5 capability audit](insights-findings-capabilities.md#november-5-source-audit-and-today-contracts) checks local Plectara `9e4fb3d`. Existing mappings, relationship-first selection, maturity/identity support and evidence adapters supersede parts of the October 27 gap baseline. Separate meaningful-review persistence and precise goal assessment states still need implementation/verification. This is not proof of deployment or complete analyzer correctness.

The reference simulates navigation and review state in memory. It does not implement durable native storage, actual analyzer eligibility, missing-input assessment, account/cloud behavior, logging forms, or all app routes. Focused finding examples demonstrate the reading flow; the full evidence contract still requires visible material limitations, actual dates, source attribution, maturity reasons and supporting records. An Explore the evidence disclosure in a navigation example does not supersede that contract.

Native targets, screen readers, enlarged text/localization, safe-area behavior, persisted review state, meaningful-change evaluation, concurrent updates and complete evidence rendering remain acceptance work. Fixtures are illustrative, and no health conclusions were verified. The owner approved this documentation update after local review. Publication and native implementation remain separate.

---

# Historical connection-led review — October 27

Reviewed: 2026-10-27
Status: Connection-led reference review complete; documentation approved for publication; native implementation pending

## October 27 connection-led amendment

The current [specification](insights-presentation.md), [capability scope](insights-findings-capabilities.md), and [reference gallery](../../assets/app/insights-presentation/index.html) incorporate the owner's feasibility decisions. This section supersedes the prior review's comparison-first hierarchy and fixture assumptions. Historical results below apply only to the earlier package.

### Scope and content alignment

- Eligible relationships lead goal cards, with named signal pairs and a short contextual sentence. Counts and complete comparisons live in details. Filter Insights uses fixed profile goals; chips filter in place and consistent footers open details.
- G1 mapping, G2 assessed maturity and G3-lite distinct-period recurrence are explicit implementation requirements. Current captures use Possible Connection and do not pretend the evaluated labels already exist.
- Meal evidence says near / within four hours before or after, uses actual logged-meal denominators, and treats missing symptoms as unknown. The fixture uses 3 of 8 versus 3 of 12; it no longer implies explicit symptom-free meal follow-up.
- Activity/energy replaces the unsupported walking/same-night-sleep example. Values use /10 and rated-day groups; missing activity logs do not establish inactivity. The local-only detail has no finding-specific AI action.
- Plans retain existing domain templates and care eligibility. The meal/symptom plan shows automatic statuses and conditional symptom logging. Pause/Resume and End remain outlined buttons. Relationship-native planning is deferred.
- Updated ADR/RFC, product, confidence/evidence and app-visual guidance agree on the new hierarchy. The regenerated app visual-kit specification includes the same amendment.

### October 27 verification

| Check | Result |
| --- | --- |
| Reference inventory | 12 original RGB JPEG captures, six states in both themes; each 1179 × 2556 from 393 × 852 at 3×, no resampling |
| Theme content parity | Identical text, values, counts, timing and limitations across all six light/dark pairs |
| Capture readiness | Fonts ready, imagery loaded, icons rendered, and no horizontal body overflow in all 12 states |
| Visual inspection | Both appearances checked for overview, Today, meal evidence, energy evidence, gathering context and plan management; canonical artwork and opaque surfaces retained |
| Rendered content contrast | 164 sampled text-role instances across the current captures; minimum 5.06:1 against their resolved opaque surfaces; no sampled ordinary-text failures |
| Existing component contracts | 152 component contrast checks pass, including the newly registered backing roles; app visual-kit rebuild verifies 60 contrast checks and source/artwork/package parity |
| Reference interaction | Goal chips filter in place; shared meal evidence uses the selected symptom goal in header/footer; More Energy lacks AI action; Pause/Resume and End confirmation/cancellation routes verified |
| Artifact integrity | Capture-time source hashes, file dimensions, theme parity, unsupported-fixture exclusions and image hashes checked by the current packager |
| Documentation | Strict MkDocs build passes; generated visual-kit specification and package are synchronized; local publication preview checked separately |

[Current manifest](../../assets/app/insights-presentation/connections-first-2026-10-27/references.json) and [capture observations](../../assets/app/insights-presentation/connections-first-2026-10-27/capture-observations.json) contain reproducible evidence. Editable sources are in `tooling/insights-connections-reference/`. The previous packager is guarded against replacing this amendment's gallery or image block.

### Shared color registration

The owner approved central registration of the icon/relationship backing, AI backing and decorative divider. The reference builders now resolve these roles from `assets/tokens/color.tokens.json`. Rendered Insights and Preferences stylesheet bytes were verified identical before and after registration; the appearance is unchanged. Generated CSS/Flutter exports, brand-kit downloads, and the 152-check component contrast report are synchronized. This registers design tokens, not consuming-app code.

### Limits

This review validates design artifacts and documentation, not native rendering, complete app navigation, saved state, real analysis output or clinical interpretation. Values are illustrative fixtures based on supported analyzer families. The audit baseline is Plectara `3044e87`; it is dated evidence, not a claim that G1/G2/G3-lite have shipped. The six current scenes cover this amendment; AI/care/other lifecycle states retain detailed written requirements rather than being falsely certified by the older 38 captures.

Native 48 dp Android targets, 320-unit layouts, enlarged text, localization, screen readers, safe areas, persistence, consent enforcement, and assessment correctness remain implementation acceptance work. The sampled contrast results are not a complete accessibility certification. The owner approved publication of the documentation and shared color registration after this review. Native app implementation remains separate.

---

# Historical comparison-first review

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

- [Historical paired gallery](../../assets/app/insights-presentation/previous-goal-comparison-gallery.html)
- [Approved decision](../../adr/0017-adopt-goal-led-insights-presentation.md)
- [Native acceptance criteria](insights-presentation.md#acceptance-criteria)
