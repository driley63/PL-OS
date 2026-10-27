# Insights Presentation

Status: Approved direction; implementation pending
Owner: Product and Design System Working Groups
Version: Unreleased
Last updated: 2026-10-25

## Purpose and authority

Define a brief overview of findings on Today, a browsable inventory on Insights, and a detail route for evidence, optional AI explanation, and user-controlled next steps. The approved presentation contract defines the intended experience; native implementation and verification remain required. Clinical rules are unchanged.

This specification supersedes the long-form Today and Insights hierarchy in the v2.6/v2.7 screenshot references. Retain their canonical artwork, theme roles, shell geometry, accessibility requirements, and historical fixtures. Existing capture actions, unrelated Today content, navigation, consent, and analysis eligibility remain governed by their respective contracts.

## Goal-Focused Review (Local Proposal)

This local composition proposal uses **Focus on** to select a goal supplied by the profile, displayed in **Capital Case**. The fixture profile selects Better Sleep; these are demonstration profile values, not a capture of the owner's account. The primary card links Caffeine and Sleep with a non-directional association marker and shows both recorded groups on one zero-to-ten sleep-quality scale. Supporting findings are visually subordinate and explicitly tied to the selected saved goal. Supporting log types are available directly in one horizontally scrolling chip row beneath Focus on, with immediate filtering and no More Filters sheet.

The review verifies profile-supplied labels, custom goal wording, saved goals with no findings, combined goal/log filters and enlarged text. The composition is pending visual approval and has not been implemented in the app. The saved-goal selection rule below reflects the owner's correction and supersedes the older generic outcome filters.

| Local review | Light | Dark |
| --- | --- | --- |
| Goal-Focused Insights | [![Goal-Focused Insights in light appearance](../../assets/app/insights-presentation/screens/insights-refined-light.png?v=flutter-7801479092){ width="240" }](../../assets/app/insights-presentation/screens/insights-refined-light.png?v=flutter-7801479092) | [![Goal-Focused Insights in dark appearance](../../assets/app/insights-presentation/screens/insights-refined-dark.png?v=flutter-cffaee5be7){ width="240" }](../../assets/app/insights-presentation/screens/insights-refined-dark.png?v=flutter-cffaee5be7) |
| Your Goals Picker | [![Your Goals Picker in light appearance](../../assets/app/insights-presentation/screens/insights-goals-light.png?v=flutter-62e6d23d40){ width="240" }](../../assets/app/insights-presentation/screens/insights-goals-light.png?v=flutter-62e6d23d40) | [![Your Goals Picker in dark appearance](../../assets/app/insights-presentation/screens/insights-goals-dark.png?v=flutter-384cbe5482){ width="240" }](../../assets/app/insights-presentation/screens/insights-goals-dark.png?v=flutter-384cbe5482) |

## Production intent screen references

The following earlier captures remain for comparison. Their generic outcome filters and More filters sheet are superseded by the saved-goal selection and inline log-type row in the [local goal-focused proposal](#goal-focused-review-local-proposal).

These app-area captures are rendered by the Flutter engine at 393 × 852 logical points and 1179 × 2556 pixels. They reuse Plectara's actual `AppTheme`, `WovenBackdrop`, `ReadingCard`, `TodayInsightsRegion`, `FindingSummaryCard`, care notice and finding-detail route. Proposed goal filtering uses Flutter controls and the shared app theme. Compact plan/log content is a seeded preview composition. The woven background, fonts, icons, text wrapping and component sizing are rendered by Flutter rather than drawn as SVG approximations.

These captures come from an isolated local preview, not the released app or an iOS simulator screenshot. System status/home indicators are omitted; iOS safe-area insets are retained. Fixtures contain illustrative findings and no real health data or cloud calls. The written specification still controls adaptive behavior; native interaction, Dynamic Type and VoiceOver verification remain required. Tap an image to inspect it at full resolution.

| Screen | Light | Dark |
| --- | --- | --- |
| Today highlight | [![Today highlight in light appearance](../../assets/app/insights-presentation/screens/today-light.png?v=flutter-1a1e345ba9){ width="240" }](../../assets/app/insights-presentation/screens/today-light.png?v=flutter-1a1e345ba9) | [![Today highlight in dark appearance](../../assets/app/insights-presentation/screens/today-dark.png?v=flutter-202d16458b){ width="240" }](../../assets/app/insights-presentation/screens/today-dark.png?v=flutter-202d16458b) |
| Insights inventory | [![Insights inventory in light appearance](../../assets/app/insights-presentation/screens/insights-light.png?v=flutter-26380dc8cb){ width="240" }](../../assets/app/insights-presentation/screens/insights-light.png?v=flutter-26380dc8cb) | [![Insights inventory in dark appearance](../../assets/app/insights-presentation/screens/insights-dark.png?v=flutter-e1bc246031){ width="240" }](../../assets/app/insights-presentation/screens/insights-dark.png?v=flutter-e1bc246031) |
| Earlier More filters sheet (superseded) | [![More filters in light appearance](../../assets/app/insights-presentation/screens/more-filters-light.png?v=flutter-dc76f86f2d){ width="240" }](../../assets/app/insights-presentation/screens/more-filters-light.png?v=flutter-dc76f86f2d) | [![More filters in dark appearance](../../assets/app/insights-presentation/screens/more-filters-dark.png?v=flutter-5590d1bb9a){ width="240" }](../../assets/app/insights-presentation/screens/more-filters-dark.png?v=flutter-5590d1bb9a) |
| Finding details | [![Finding details in light appearance](../../assets/app/insights-presentation/screens/finding-light.png?v=flutter-d9b184c688){ width="240" }](../../assets/app/insights-presentation/screens/finding-light.png?v=flutter-d9b184c688) | [![Finding details in dark appearance](../../assets/app/insights-presentation/screens/finding-dark.png?v=flutter-90d0c7a5e8){ width="240" }](../../assets/app/insights-presentation/screens/finding-dark.png?v=flutter-90d0c7a5e8) |
| Today with active plan | [![Today with active plan in light appearance](../../assets/app/insights-presentation/screens/today-plan-light.png?v=flutter-223476e7cf){ width="240" }](../../assets/app/insights-presentation/screens/today-plan-light.png?v=flutter-223476e7cf) | [![Today with active plan in dark appearance](../../assets/app/insights-presentation/screens/today-plan-dark.png?v=flutter-71fb735cd3){ width="240" }](../../assets/app/insights-presentation/screens/today-plan-dark.png?v=flutter-71fb735cd3) |
| Insights with AI off | [![Insights with AI off in light appearance](../../assets/app/insights-presentation/screens/insights-ai-off-light.png?v=flutter-326a7ad768){ width="240" }](../../assets/app/insights-presentation/screens/insights-ai-off-light.png?v=flutter-326a7ad768) | [![Insights with AI off in dark appearance](../../assets/app/insights-presentation/screens/insights-ai-off-dark.png?v=flutter-da9e63bf68){ width="240" }](../../assets/app/insights-presentation/screens/insights-ai-off-dark.png?v=flutter-da9e63bf68) |

[Capture provenance and reference metadata](../../assets/app/insights-presentation/screens/references.json) list the imported app components, source hashes, dimensions and checksums for each capture. Editable Flutter scene sources are stored under `tooling/flutter-insights-reference/`. The care notice is a report-level fixture; its placement does not mean caffeine alone triggered it.

### Reference styling contract

Apply the named woven app variant from [App Visual Specification](../02-design/app-visuals.md#geometry-and-typography), [Cards](../02-design/cards.md#woven-app-reading-cards), [Spacing System](../02-design/spacing-system.md#approved-app-local-spacing), [Buttons](../02-design/buttons.md), and [Radius and Elevation](../02-design/radius-and-elevation.md). The generic 8-unit card radius and 16-unit mobile gutter do not override the app's approved local 14-unit radius and 12-unit gutter.

| Element | Reference rule |
| --- | --- |
| Main reading cards | 12-unit side gutters, 14-unit padding/radius, 1-unit themed decorative outline; zero extra outer card margin |
| Main section rhythm | 10-unit body top inset below the header; 12-unit gaps between adjacent groups; content continues in the scroll region behind navigation |
| Card headings and findings | Inter 18/25, weight 500; finding summary 16/25 regular; body 14/23; metadata 13/22; avoid hero-size or bold repeated card titles |
| Detail surface | One reading panel; evidence, care context and disclosures use unframed internal sections, not nested outlined cards |
| Inventory controls | Source/window and Focus on form one functional filter group; no separate decorative metadata card; filter controls at least 44 units high with selected check and state |
| Status labels | Display-only pills; no implication that their small visual height is a touch target |
| Today capture actions | 54-unit height; Quick Log radius 28, Log radius 12; keep bottom clearance above navigation |
| Other buttons and sheet | App button radius 9; sheet radius 12 from radius.3, standard 20-unit sheet content inset; no arbitrary 24-unit sheet corners |
| Attention and selection | Use theme attention backing and icon/text; light neutral outlines and dark copper decoration; dark selected foreground remains link |

The reference renderer is `tooling/render-insights-flutter.py`, with editable scene/capture sources in `tooling/flutter-insights-reference/`. It imports the current app components rather than approximating them with hand-positioned vectors. The capture metadata records source hashes so differences from the current app or PL-OS rules can be reviewed explicitly. Framework screenshots are visual references; native reflow, accessibility and full-app interaction validation remain required. The supplementary early exploration is historical and does not override these references or the component specifications.

## Presentation structure

Use the existing [app shell and theme](../02-design/app-visuals.md) with opaque reading surfaces. The following component structures define the presentation within PL-OS. They specify information order and behavior rather than a fixed screenshot or device size.

### Today insight region

| Order | Component | Presentation rule |
| --- | --- | --- |
| 1 | Applicable care notice | Separate attention surface with icon, full notice and report/finding scope; urgent context leads the region |
| 2 | Highlight heading | Insights label, actual finding count and freshness context |
| 3 | Finding preview | Topic, short factual title and one complete takeaway |
| 4 | Evidence context | Source, analyzed period and material uncertainty adjacent to the claim |
| 5 | Navigation | Explore opens this finding; View all findings opens the inventory |

Render active-plan status as a separate card, with actual title, day/status, concise step summary and View plan. Preserve the existing capture actions and unrelated Today content. Do not copy review-page headings or sample logs into the app.

### Insights inventory card

| Region | Content | Visual treatment |
| --- | --- | --- |
| Inventory header | On-device/source description, analyzed window and last successful analysis | Compact metadata above filters; no full narrative |
| Attention | Applicable care notice and its scope | Independent attention surface before the list |
| Filters | Focus on: All Goals and the user’s saved goals in Capital Case; one horizontally scrolling row of supporting log-type chips | Clearly selected, accessible controls with result count |
| Card heading | Topic and factual title | Strongest text hierarchy within the card |
| Card takeaway | One supported observation or comparison | Short readable text, retaining essential qualifiers |
| Card context | Type, period and material uncertainty | Secondary text; distinguish type from confidence |
| Open affordance | Entire card opens the finding | One accessible action with a clear directional cue |

### Finding detail composition

Place the complete claim and evidence context above optional explanations. Present an appropriate comparison only when the analyzer supplies the required values, groups, units and periods. Keep material uncertainty and care context visible before suggested action. Expandable sections contain supporting evidence, optional AI explanation and optional next steps. The [detail anatomy](#finding-detail-anatomy) defines the complete order.

For a connection between caffeine timing and sleep quality, show two explicitly labeled groups on the same sleep-quality scale: **Caffeine Logged After 2 PM** and **No Caffeine Logged After 2 PM** when the analyzer uses the 2 PM cutoff. The values describe sleep recorded for the nights following those days. The second group may include earlier caffeine or no caffeine entries; it does not establish that no caffeine was consumed. Exclude days with untimed caffeine entries unless a timed entry establishes caffeine after the cutoff, following the analyzer's eligibility rules. Explain this comparison basis and missing-log limitations in supporting evidence. Do not use a vague label such as "Other Recorded Days." Populate both values and their coverage from the actual evidence; adapt the labels when the analyzer supplies a different cutoff. A missing comparison produces an explanation of missing evidence, not a fabricated chart. This example defines the component's semantics, not a clinical conclusion or fixed numeric fixture.

### Appearance and adaptation

Use ink, teal and restrained semantic accents within existing light/dark reading surfaces. AI Purple identifies the optional AI explanation only. Reserve attention styling for actual care state. The card hierarchy must remain understandable without color, and content must expand for larger text and localization. Device frames, review controls, surrounding presentation copy and specification notes are not interface components.

## Three levels of disclosure

| Surface | User question | Primary content | Primary route |
| --- | --- | --- | --- |
| Today | Is there something useful to notice? | At most one highlighted finding, or a compact state message | Open that finding; view all findings |
| Insights | What patterns can I explore? | Individual eligible findings with type, topic and concise takeaway | Open a finding |
| Finding details | What supports this, and what could I do next? | Claim, evidence, limitations, explanation and optional actions | Supporting entries, follow-up chat, plan preview |

Do not repeat a full AI narrative on Today or above the Insights inventory. A brief card is a complete, understandable summary, not the first characters of a paragraph. The full evidence and explanation remain available in details.

## Today

1. Preserve applicable care notices as an independent, visible part of the insight region. Their urgency and wording come from existing rule state. A high-priority notice leads the region; it cannot be pushed below optional plan or promotional content. A report-level notice must identify its scope rather than implying that the highlighted finding alone triggered it.
2. Show one eligible finding using a topic, short factual headline, one concise takeaway, on-device/source attribution, actual analyzed period, material qualifier, and **Explore**. Show the count of current, non-dismissed findings and **View all findings** when an inventory exists.
3. Target a one- or two-line headline and a one- or two-line takeaway at default text size. These are editorial targets, not fixed heights or truncation limits. Large text, localization and necessary qualifiers expand naturally.
4. Do not show Correlations and Recommendations as separate long lists on Today. Do not place an acknowledgement/reward gate before access to findings.
5. Place active-plan status in its own compact card. Include title, actual day and duration, paused/completed status where applicable, and a concise supported step summary. **View plan** opens the plan, not a generic Insights landing page.
6. Keep Today useful for logging. Preserve existing Quick Log, Log, reminders, progress, and log content without fabricating additional widgets. Action clearance and content insets must prevent coverage of warnings or evidence.

### Highlight selection

Care urgency is evaluated separately from content ranking. From eligible, non-dismissed findings, prefer materially changed or not-yet-reviewed evidence, then relevance to selected goals, then evidence adequacy under the analyzer's documented criteria. Use a stable finding identity as the final tie-breaker. Do not rank by frightening wording, generated confidence, or length of AI text.

Do not show an unrelated tracking statistic merely to fill the slot. When there is no newly useful finding, show the appropriate compact state and retain access to existing findings. A user opening a finding records it as reviewed; this is distinct from saving, dismissing, acknowledging rewards, or completing a plan.

## Insights inventory

- Keep the Insights title and settings action in the existing shell. Use a compact on-device/source description, actual analyzed window and last-successful-analysis timestamp.
- Show applicable care notices before the inventory. Preserve the complete accessible notice and its scope.
- Render one card per eligible finding. Each card contains a topic, type, factual headline, one takeaway, relevant period/coverage qualifier, and a clear open affordance. A card is one accessible action; do not nest unrelated buttons inside it.
- Label the primary filter group **Focus on**. Restore the selected saved goal or use **All Goals** initially; show the profile’s actual goal labels in Capital Case. Show supporting log types in one horizontally scrolling chip row beneath Focus on, as defined below. Announce selected state and result count.
- Do not treat a topic as a diagnosis or a direction as a clinical outcome. Use **Possible connection**, **Recorded trend**, **Observation**, or **Goal progress** as appropriate.
- Preserve all eligible findings beyond the first screen. Do not hide findings behind a horizontal carousel or silently discard them to fit a card limit. Pagination must preserve ordering and disclose additional results.
- Preserve filter and scroll state when returning from details. Open a finding by stable identity, not list position.
- Consolidate equivalent observations by finding identity and evidence fingerprint. Do not display the same finding once as a local result and again as an AI result.

### Focus on and inline log-type filters

**Focus on** selects the user's saved goals, using the goal IDs and labels from their profile. It must not substitute log types or a fixed outcome catalog. A profile with Better Sleep, More Energy and Better Digestion shows those exact goal names; another profile shows its own saved goals. Include **All Goals** so findings without a goal association remain reachable. Keep saved goals visible even when they have no findings, with a distinct “No findings for this goal yet” state. If no goals are saved, show All Goals and an explicit route to manage goals; the inventory remains usable.

Display goal labels in **Capital Case**, preserving their wording, acronyms and identity. Capitalization is a display transformation; do not overwrite the saved label or derive identity from text. A custom saved label such as “understand my IBS patterns” displays as “Understand My IBS Patterns.” Restore the last valid selected goal; default to All Goals when none is selected. The review fixture explicitly selects its saved Better Sleep goal.

Associate findings with one or more actual saved goal IDs using reviewed structured mappings. Log-type IDs are independent supporting-evidence metadata. A caffeine/sleep finding may support a saved Better Sleep goal and have Sleep and Beverages as evidence types. Do not manufacture a goal from a finding, claim an unrelated water average supports Better Sleep, or associate by matching words in an AI narrative. A finding appears only once even if it supports several goals. Keep a selected goal stable through refresh; if its findings disappear, show the goal-specific empty state. Long user-entered labels wrap; the goal picker lists full labels without truncating their meaning.

Display supporting **Log types** as one horizontally scrolling row of shared app selection chips beneath Focus on. Remove the More filters button and log-type sheet. Use the app's actual entry-type catalog and familiar labels; display only supported types represented in eligible evidence. Do not confuse log types with finding kinds such as Recorded trend. Include **All Log Types** first; it is selected when no individual type is selected. Tapping it clears log-type selections while preserving the saved goal.

Tapping a log-type chip toggles it and updates results immediately, with no Apply, confirmation or modal steps. Selecting several log types matches findings supported by **any** selected type; combine that match with the selected saved goal using **AND**. Deselecting the last type restores All Log Types. A beverage filter must retain a sleep finding supported by beverage entries. Use structured evidence-type IDs, never a keyword search of the headline or AI narrative. Keep the row available with AI off; filtering does not require AI or change consent.

Keep the chips on one row at every text size; allow horizontal scrolling rather than wrapping, clipping full labels or reducing type size. Use the existing app SelectChip appearance, a visible selected mark and programmatic selected state, at least 44-unit touch targets, and 8-unit gaps. Leave the next chip partly visible when the row overflows to make scrolling discoverable. Keep keyboard and assistive-technology access to every chip; focused items scroll into view. Update and announce the result count without moving focus or resetting the horizontal position when a chip is toggled.

Preserve both applied selections and list position when returning from a finding. A deliberate filter change starts the result list at its first matching card. Preserve applicable care notices outside the filtered list. Distinguish **No findings match these filters** from insufficient data; **Clear filters** resets both Focus on to All Goals and all applied log types. Announce the new count without moving focus unexpectedly. All controls meet native touch-target and Dynamic Type requirements. The saved-goal picker contains focus until dismissed; inline chips expose selected state without opening a modal.

## Finding detail anatomy

| Order | Content | Visibility |
| --- | --- | --- |
| 1 | Back action, topic, complete factual title, type and source | Always |
| 2 | Exact observation window and analysis timestamp; stale/coverage state | Always |
| 3 | One concise statement and appropriate supported metric visual | Always when available |
| 4 | Material uncertainty, missing-data limitations, relevant care context | Before actions; never accordion-only |
| 5 | **What supports this finding** with counts, periods, comparison basis and supporting entries | Expandable supporting detail |
| 6 | Optional **AI explanation**, locally labeled AI-assisted | Expandable; consent and availability dependent |
| 7 | Optional **A next step to consider** with evidence-appropriate plan or tracking action | Expandable after limitations |
| 8 | Follow-up question, save/dismiss and usefulness/accuracy controls | Clearly labeled, secondary to understanding |

A report-level care notice remains report-level in details. If a specific finding supports a notice, preserve that association explicitly. Do not infer the relationship from co-location. Never weaken or omit urgent wording to meet a short-copy target.

### Visual selection by finding type

| Type | Preferred visual | Guardrail |
| --- | --- | --- |
| Possible connection | Two labeled values or groups on a common scale, with units and cohort context | Show association language, comparison counts and missing coverage when available; no causal arrows |
| Recorded trend | Matched-period comparison or a small real time series | Identify periods, units and baseline; do not invent an earlier value |
| Goal progress | Supported change related to a user-selected goal | No goal-completion ring unless a measurable target and denominator exist |
| Observation | One recorded count/value or short factual statement | Use an unavailable state for missing measurements, not zero |
| Plan status | Actual day/status and supported step completion | Elapsed days are not adherence, efficacy or health improvement |

Use charts only when they clarify the finding. A plain comparison is preferable to a decorative graph. Do not imply a continuous time series from aggregate values. Provide the same information as text for assistive technology. Respect the existing [Charts](../02-design/charts.md) contract for baselines, scales, labels and contrast.

## Finding display contract

The presentation layer must distinguish supplied facts from formatted copy. Each field must be traceable to the analyzer, record store or explicitly labeled explanation.

| Field | Requirement |
| --- | --- |
| Stable finding identity and evidence fingerprint | Identify the logical finding separately from the analyzed evidence version; do not derive identity from AI wording |
| Kind, domain/topics and related goal | Use supported taxonomy; a goal association requires an actual user goal |
| Related saved goal IDs and supporting log-type IDs | Reviewed many-to-many links to real profile goal IDs; labels come from the profile and display in Capital Case; log-type IDs come from structured evidence; unassociated findings remain in All Goals |
| Headline and takeaway | Use reviewed templates populated from structured facts; generated summaries require their own validated output contract |
| Source/authorship | Distinguish local detection, imported measurements and optional AI explanation |
| Observation window and generated timestamp | Store and display the actual relevant window, including domain-specific longer lookbacks |
| Metrics and units | Typed values, interpretation of scale and explicit missing values |
| Optional comparison | Named groups/periods, values, method, counts and comparable coverage; omit unsupported comparisons |
| Evidence references | Stable supporting-entry references or a reproducible evidence query, respecting deleted records and permissions |
| Coverage and limitations | Recorded/paired-day counts and missingness when the analyzer provides them; otherwise disclose that coverage is unavailable |
| Confidence/strength | Only when mapped to documented, evaluated criteria; never inferred from assertive wording or sample size alone |
| Care scope and urgency | Existing rule-derived state plus explicit report/finding association |
| Suggested action | Supported action type, eligibility and destination; no automatic plan start or consent change |
| Reviewed, saved and dismissed state | Per-finding state with evidence-version semantics; independent of rewards and care notices |

The current app's `LocalFinding` provides code, domain, kind, label, metrics, evidence-window days, related titles, optional suggestion and device-only controls. It does not guarantee all display fields above. Analyzer-specific adapters may be required. Never recover missing numeric evidence or links by parsing the AI narrative. Missing support must change the presentation, not trigger invented content.

### Authorship and confidence

Use plain attribution such as **Found on your device** for local findings. AI Purple and **AI-assisted** apply to generated explanations, not all findings. **Possible connection** is a type label, not a measured confidence level. AI off, failure or refresh must not change the authorship, evidence or care urgency of an existing local finding.

Follow [Confidence and Evidence](../05-ai/confidence-and-evidence.md). Do not display confidence percentages or high/medium/low badges until a reviewed method supplies them. Include material uncertainty beside the short claim. Detailed methodology may expand; decision-critical limitations may not be hidden exclusively in details or tooltips.

## Interaction contracts

| Action | Required result |
| --- | --- |
| Explore / open card | Open matching detail route and evidence version; Back restores origin state |
| View all findings | Open Insights; do not mark every finding reviewed |
| View supporting entries | Open timeline filtered to supporting evidence, with filter description and clear exit; unavailable/deleted references produce an explanation |
| Ask a follow-up | Open supported chat with the finding context and editable suggested question; preserve cloud exclusions and consent boundaries |
| Explore a tracking plan | Open eligible plan preview; show scope and requirements; starting remains explicit |
| View active plan | Open that plan's actual state and steps; paused, completed and unavailable progress are distinct |
| Save | Persist a bookmark independently of viewed/dismissed status; unavailable findings retain their historical context |
| Dismiss | Remove the selected evidence version from routine presentation, offer undo, and retain a route to dismissed items |
| Do not show this again | Explicitly suppress the logical finding until the user reverses that preference; do not silently apply this stronger action via Dismiss |
| Feedback | Distinguish not useful, not accurate and safety concern; no automatic alteration of evidence or clinical rules |

A materially changed evidence version may reappear after a normal Dismiss. An explicit recurrence suppression persists. Neither action suppresses applicable report-level or urgent care notices. A dismissed finding must not become “new” because an AI explanation was reworded.

Chat must preserve existing device-only domains and opt-in exclusions. The context must not silently expand from permitted structured findings to full diary notes, photos or excluded entries. When an eligible finding cannot be shared, explain the limitation and keep local details accessible.

## State matrix

| State | Today | Insights and details | Actions |
| --- | --- | --- | --- |
| Initial analysis loading | Compact loading status; preserve logging | Stable skeleton/status without fabricated findings | No false progress percentage |
| Insufficient evidence | Explain which missing records would support the relevant question | No invented finding or empty comparison chart | Relevant logging entry point; no universal entry-count threshold invented by UI |
| Analysis complete with no eligible findings | State that no clear patterns were found in the reviewed window | Distinguish from not analyzed and insufficient data | Continue normal use; do not require more logging without a reason |
| No newly changed findings | Compact status and access to earlier findings | Existing inventory remains browsable; no repeated “new” badge | Review earlier findings |
| AI turned off | Local overview unaffected | Local evidence remains available; explanation states it is off | AI preferences; enabling remains explicit consent |
| AI unavailable/offline | Local overview unaffected | Preserve facts and any separately dated last-successful explanation; unavailable AI is labeled | Explicit retry when appropriate; no filler narrative |
| Local analysis failed | State failure without replacing the last successful result | Retained results show their original dates and stale status | Retry; logging remains available |
| Older findings | Stale label before any retained claim | Original observation window and analyzed date remain visible | Refresh local analysis; do not imply cloud AI is also refreshed |
| Filter has no matches | Not applicable | Empty filter result distinct from empty inventory | Clear filters |
| Evidence removed or inaccessible | Re-evaluate eligibility before highlighting | Explain unavailable support; do not show a chart based on inaccessible evidence | Return to current inventory; refresh as appropriate |
| Active/paused/completed plan | Actual title, day/status and concise step summary | Plan details retain real completion and comparison eligibility | Preview/manage; never infer success from elapsed time |

Each analyzer defines evidence eligibility and stale-after rules. The display layer consumes them; it must not invent a universal age cutoff. Store the last successful analysis separately from attempt time and AI generation time.

## Accessibility and responsive behavior

- Preserve the canonical woven backdrop, header rule and opaque reading surfaces. Support System, Light and Dark. Reduce decoration under accessibility settings as defined by the app visual contract.
- Use native semantic headings, buttons, selected filters, expanded disclosures and navigation. Announce a card's type, claim, period and open action without reading decorative glyphs.
- Use minimum 44-point touch targets. Support keyboard focus, visible focus styling and logical reading order.
- Dynamic Type and localization must expand cards vertically. Phone-sized fixed heights and the review prototype's scaled canvas are not production geometry.
- Supply text equivalents for every comparison, including direction, values, units and periods. Never encode significance, selection or care urgency with color alone.
- Preserve reduced-motion behavior, scroll position, focus restoration and bottom safe-area clearance. Expanding evidence must not move focus to an unrelated card.

## Acceptance criteria

1. Today renders no more than one highlighted finding and no full AI narrative; all eligible findings remain reachable on Insights.
2. A compact card and its detail route resolve to the same finding identity, evidence version, source, observation window and values.
3. Material uncertainty and applicable care notices remain visible before optional action. Filtering, dismissing or AI toggles cannot remove required care context.
4. Every comparison has actual groups/periods, labeled units and supported values. Missing values, unavailable confidence or absent baselines never become zero or fabricated percentages.
5. Reviewed, changed, unchanged, saved, dismissed and recurrence-suppressed fixtures produce the specified ranking and disclosure behavior.
6. Every state in the matrix is reviewed in light/dark appearance, default and enlarged text. No card, warning or bottom action is clipped or obscured.
7. Focus on shows the actual saved goal list and displays labels in Capital Case; no saved goals leaves All Goals available. The inline log-type row uses evidence types with OR within that group and AND with the saved goal. Verify a caffeine/sleep finding survives a saved Better Sleep goal plus Beverages, several saved goal links never duplicate a card, AI off still permits filtering, one tap updates results, toggling the last selected type restores All Log Types, All Log Types clears only log-type selections, and Clear filters resets both groups. Verify horizontal scrolling at default and enlarged text sizes without label truncation or extra modal steps. Care notices remain visible for zero results. Filters announce selection and result count; Back restores origin, selected filters and scroll position. Evidence disclosures are operable by keyboard and VoiceOver.
8. Plan preview/start, chat opt-in and feedback remain explicit. No presentation action silently changes logging preferences, consent or clinical rules.
9. Local findings remain inspectable with AI off or unavailable. Device-only findings and excluded records never enter cloud context through the new detail route.
10. Approved native screenshots and interaction evidence replace the prototype as implementation verification; browser review alone does not establish native accessibility or production readiness.

## Dependencies and migration

Implement display adapters and evidence navigation before replacing the existing card. Preserve actual local findings and rule-derived care state throughout migration. Validate representative connection, trend, goal and observation fixtures plus missing/partial evidence. Retain the historical screenshot assets as versioned references.

The controlling references are [Insights and Correlations](insights-and-correlations.md), [App Visual Specification](../02-design/app-visuals.md), [Progress and Disclosure](../02-design/progress-and-disclosure.md), [Insight Types](../05-ai/insight-types.md), [Confidence and Evidence](../05-ai/confidence-and-evidence.md), and [Hybrid Local Findings](../../adr/0010-hybrid-local-findings-optional-llm.md). This specification introduces no clinical thresholds or new cloud-sharing permissions.

## Flutter reference viewer

The [Flutter reference viewer](../../assets/app/insights-presentation/index.html) shows the same full-resolution captures as this specification. It supports light/dark comparison, the primary Today → Insights → details flow, active-plan and AI-off states, and the earlier More filters sheet retained for comparison. The default local proposal shows the replacement inline log-type row. It uses the captured app pixels rather than recreating the interface with HTML/CSS. It is a visual viewer, not an interactive app implementation.

The former HTML exploration is retained as a historical source file (`legacy-exploration.html`) and is no longer the default preview. The written component contracts and acceptance criteria remain authoritative; native implementation and accessibility verification are separate work.

## Version History

- 2026-10-25: Replaces More filters and its sheet with one directly accessible, horizontally scrolling log-type chip row; filtering applies immediately and preserves the saved goal.

- 2026-10-25: Corrects Focus on to the user’s saved profile goals and Capital Case labels; generic outcome categories are superseded. Adds a local goal-focused hierarchy proposal for review.
- 2026-10-25: Replaces all twelve SVG-based images with Flutter-engine component captures; adds editable Flutter preview sources, source provenance and versioned gallery URLs. Local review only.
- 2026-10-25: Rebuilds all twelve references against app-local cards, spacing, typography and controls; removes nested detail frames and decorative metadata cards; saves reproducible renderer and group-spacing checks.
- 2026-10-25: Replaces primary log-type chips with outcome-focused Focus on; specifies evidence-based More filters sheet, matching, state and accessibility behavior, and adds light/dark sheet references.
- 2026-10-25: Adds app-only production-intent renders for Today, Insights, finding details, active-plan and AI-off states in light/dark appearance; includes editable vector sources and full-resolution exports.

- 2026-10-25: Replaces the embedded review-page capture with native PL-OS component structures and presentation rules; separates the supplementary prototype from normative specification content.

- 2026-10-25: Approved three-level presentation, visual references, display contract, state matrix and acceptance criteria; implementation pending.
