# Insights Presentation

Status: Design and specification approved; implementation pending

Owner: Product, Design System, and AI Working Groups

Version: Unreleased

Last updated: 2026-10-27

Decision: [ADR-0017](../../adr/0017-adopt-goal-led-insights-presentation.md), proposed in [RFC-0011](../../rfc/0011-goal-led-insights-presentation.md)

## Purpose and authority

Make findings easy to scan, understand, and act on without requiring the user to read a long narrative. Today answers **what deserves my attention now?** Insights answers **what are my records showing about my goals?** A selected goal explains its comparison, a connection opens its evidence, and optional AI review and chat help the user ask follow-up questions.

The October 27 approved design governs this next presentation. This document specifies the information architecture, content, visual hierarchy, interaction, data requirements, and state behavior. The references show the approved appearance; the written contract defines behavior beyond a single screenshot. The design and detailed specification were approved for publication on October 27, 2026. Consuming-app implementation and a tagged release remain pending.

The earlier October 25 custom-goal, log-type filter, caffeine/sleep, and Flutter composition studies are superseded. The fixed goal catalog, one **Filter Insights** goal row, stomach icon, automatic plan statuses, outlined plan-management buttons, and **Explore more about [Goal Name]** footers below replace those studies. Existing clinical rules, record eligibility, consent, cloud exclusions, and unrelated app features retain their governing contracts.

The [final consistency review](insights-presentation-review.md) checks this design against the released PL-OS component contracts and the current consuming-app source. It records corrections to shared chrome and controls, intentional Insights-specific extensions, and the remaining native validation boundary.

## Production intent screen references

[Open the full-resolution reference gallery](../../assets/app/insights-presentation/index.html){ .md-button }

The gallery contains **38 app-only PNGs: 19 views in each theme**, rendered directly from the approved design at **393 × 852 logical units and 1179 × 2556 pixels**. Fonts, icons, charts, and layout are rendered at 3×; these are not enlarged thumbnails. The canonical woven artwork continues behind the scrollable area. Both themes use opaque reading surfaces and the approved app geometry.

These are high-fidelity **browser-rendered design references**, not screenshots of a shipping app or native Flutter implementation. The capture contains no chat transcript, design-review caption, variant selector, browser chrome, or documentation page. The status bar and home indicator are illustrative. Scrolled references deliberately show the lower part of a screen with the header and navigation retained; they are not cropped substitutes for a complete screen.

Click an image to inspect its original pixels. The gallery pairs each light image with the same dark state and explains the pictured scroll position. [Reference manifest](../../assets/app/insights-presentation/approved-2026-10-27/references.json) records dimensions, hashes, scene state, source provenance, and capture method. A [single-screen reference](../../assets/app/insights-presentation/approved-2026-10-27/reference.html?scene=insights&theme=light&scale=1) preserves the inspectable layout. Numerical examples are review fixtures, not production defaults or clinical thresholds.

<!-- APPROVED_GALLERY_START -->
### Today and Insights

**Today** — Compact automatic plan tracking, one new finding, and the existing progress section.

| Light | Dark |
| --- | --- |
| [![Today in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/today-light.png?v=7bcd65ccb042){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/today-light.png?v=7bcd65ccb042) | [![Today in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/today-dark.png?v=307fa920ee51){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/today-dark.png?v=307fa920ee51) |

**Insights · Overview** — Saved fixed goals in one Filter Insights row, optional AI review, and takeaway-first goal cards.

| Light | Dark |
| --- | --- |
| [![Insights · Overview in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-light.png?v=7dd484c2fe80){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-light.png?v=7dd484c2fe80) | [![Insights · Overview in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-dark.png?v=f05fc2a7110d){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-dark.png?v=f05fc2a7110d) |


??? example "Goal summaries and comparisons — light and dark references"

    **Insights · More Goal Cards** — Activity and energy summaries use the same Explore more about [Goal Name] footer.

    | Light | Dark |
    | --- | --- |
    | [![Insights · More Goal Cards in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-lower-light.png?v=670f79e19434){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-lower-light.png?v=670f79e19434) | [![Insights · More Goal Cards in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-lower-dark.png?v=b72c019c700e){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-lower-dark.png?v=b72c019c700e) |

    **Be More Active** — A complete period comparison with sample context, followed by a possible connection.

    | Light | Dark |
    | --- | --- |
    | [![Be More Active in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-activity-light.png?v=386878615198){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-activity-light.png?v=386878615198) | [![Be More Active in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-activity-dark.png?v=b458da546ddc){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-activity-dark.png?v=b458da546ddc) |

    **Better Digestion** — The approved stomach icon, supported percentages, and explicit missing sample context.

    | Light | Dark |
    | --- | --- |
    | [![Better Digestion in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-digestion-light.png?v=334d2506c781){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-digestion-light.png?v=334d2506c781) | [![Better Digestion in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-digestion-dark.png?v=7691f34d6645){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-digestion-dark.png?v=7691f34d6645) |

    **More Energy** — Local energy comparison; device-only information is supporting text, never a navigation label.

    | Light | Dark |
    | --- | --- |
    | [![More Energy in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-energy-light.png?v=def61dc5d770){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-energy-light.png?v=def61dc5d770) | [![More Energy in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-energy-dark.png?v=8ab81c19ebe1){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-energy-dark.png?v=8ab81c19ebe1) |

    **Better Sleep** — A missing direct comparison can coexist with a relevant connection and plan.

    | Light | Dark |
    | --- | --- |
    | [![Better Sleep in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-sleep-light.png?v=dcb463a8730f){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-sleep-light.png?v=dcb463a8730f) | [![Better Sleep in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-sleep-dark.png?v=184d735d0db4){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-sleep-dark.png?v=184d735d0db4) |


??? example "Evidence, plans, AI review, and chat — light and dark references"

    **Connection Evidence** — Sleep and activity linked without a causal arrow; explicit comparison groups and counts.

    | Light | Dark |
    | --- | --- |
    | [![Connection Evidence in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/connection-light.png?v=a88cb99b6eaf){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/connection-light.png?v=a88cb99b6eaf) | [![Connection Evidence in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/connection-dark.png?v=301ce71d7a2c){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/connection-dark.png?v=301ce71d7a2c) |

    **Plan · Today’s Records** — Automatic statuses derive from required log fields, with Add Entry and View Entry actions.

    | Light | Dark |
    | --- | --- |
    | [![Plan · Today’s Records in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-light.png?v=c90f76b679aa){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-light.png?v=c90f76b679aa) | [![Plan · Today’s Records in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-dark.png?v=8f62dd724004){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-dark.png?v=8f62dd724004) |

    **Plan · Manage** — Pause Plan and End Plan are full-width outlined buttons with distinct icons and emphasis.

    | Light | Dark |
    | --- | --- |
    | [![Plan · Manage in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-manage-light.png?v=b4a12db85634){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-manage-light.png?v=b4a12db85634) | [![Plan · Manage in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-manage-dark.png?v=80dbe0988d30){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-manage-dark.png?v=80dbe0988d30) |

    **AI Review · Takeaways** — Three short takeaways link back to the underlying goal comparison or connection evidence.

    | Light | Dark |
    | --- | --- |
    | [![AI Review · Takeaways in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-light.png?v=ecbaac60feb4){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-light.png?v=ecbaac60feb4) | [![AI Review · Takeaways in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-dark.png?v=55f09d8f5b0a){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-dark.png?v=55f09d8f5b0a) |

    **AI Review · Explanation** — Expanded explanation, explicit sharing scope, and suggested follow-up questions.

    | Light | Dark |
    | --- | --- |
    | [![AI Review · Explanation in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-more-light.png?v=2d71257f9243){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-more-light.png?v=2d71257f9243) | [![AI Review · Explanation in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-more-dark.png?v=ca105998a9f7){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/ai-review-more-dark.png?v=ca105998a9f7) |

    **Contextual Follow-Up Chat** — Visible finding context, a sample exchange, and an editable follow-up composer.

    | Light | Dark |
    | --- | --- |
    | [![Contextual Follow-Up Chat in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/chat-light.png?v=e9dca23b0b9e){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/chat-light.png?v=e9dca23b0b9e) | [![Contextual Follow-Up Chat in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/chat-dark.png?v=939fd54e120e){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/chat-dark.png?v=939fd54e120e) |


??? example "Empty, unavailable, and alternate states — light and dark references"

    **Goal · Gathering Context** — The exact fixed goal name and the specific missing evidence; no invented progress score.

    | Light | Dark |
    | --- | --- |
    | [![Goal · Gathering Context in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-waiting-light.png?v=03e36b0d8471){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-waiting-light.png?v=03e36b0d8471) | [![Goal · Gathering Context in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-waiting-dark.png?v=356c583a8491){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/goal-waiting-dark.png?v=356c583a8491) |

    **Plan · Paused** — Resume Plan replaces Pause Plan; diary records remain available.

    | Light | Dark |
    | --- | --- |
    | [![Plan · Paused in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-paused-light.png?v=678760cc3b29){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-paused-light.png?v=678760cc3b29) | [![Plan · Paused in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-paused-dark.png?v=4407f28a1eb7){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-paused-dark.png?v=4407f28a1eb7) |

    **Plan · Assessment** — Insufficient comparable records are an assessment outcome, not success or failure.

    | Light | Dark |
    | --- | --- |
    | [![Plan · Assessment in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-assessment-light.png?v=25def0e702e5){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-assessment-light.png?v=25def0e702e5) | [![Plan · Assessment in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-assessment-dark.png?v=9053b3342de9){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/plan-assessment-dark.png?v=9053b3342de9) |

    **Insights · AI Off** — Local goal summaries and plans remain available when AI features are off.

    | Light | Dark |
    | --- | --- |
    | [![Insights · AI Off in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-ai-off-light.png?v=9a74172d5f5e){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-ai-off-light.png?v=9a74172d5f5e) | [![Insights · AI Off in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-ai-off-dark.png?v=ad04fa3be7f3){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-ai-off-dark.png?v=ad04fa3be7f3) |

    **Insights · Early Records** — Saved goals remain discoverable while comparisons are still taking shape.

    | Light | Dark |
    | --- | --- |
    | [![Insights · Early Records in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-early-light.png?v=aaee09a0ec1a){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-early-light.png?v=aaee09a0ec1a) | [![Insights · Early Records in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-early-dark.png?v=82c3514baf7c){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/insights-early-dark.png?v=82c3514baf7c) |

    **Insights · Care Notice** — A report-level care notice remains above filtered content; this does not define a clinical trigger.

    | Light | Dark |
    | --- | --- |
    | [![Insights · Care Notice in light appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/care-light.png?v=53fdf59a3bcf){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/care-light.png?v=53fdf59a3bcf) | [![Insights · Care Notice in dark appearance](../../assets/app/insights-presentation/approved-2026-10-27/screens/care-dark.png?v=c9934e02ae82){ width="280" loading="lazy" }](../../assets/app/insights-presentation/approved-2026-10-27/screens/care-dark.png?v=c9934e02ae82) |


<!-- APPROVED_GALLERY_END -->

## Presentation structure

| Surface | Primary job | Content and destination |
| --- | --- | --- |
| Today | Brief daily orientation | Applicable care notice, compact active plan, one new/useful finding, existing Your Progress; See All Insights opens All Goals |
| Insights · All Goals | Compare what matters across saved goals | Filter Insights, optional overall AI entry, one summary per goal with findings, Still Gathering Context, Other Findings, active plan |
| Selected goal | Explain the result for this goal | Complete direct comparison where supported, missing-evidence state otherwise; relevant connections, relevant plan, eligible follow-up action |
| Connection evidence | Explain a possible relationship | Named signals and cohorts, common-scale values, counts, limitations, source records, optional scoped chat and plan |
| AI Review | Provide a brief overall interpretation | Up to three linked takeaways, expandable explanation and context scope, suggested follow-up questions |
| Chat | Ask follow-up questions | Explicit overall/finding context, permitted evidence scope, conversation, editable question, explicit Send |
| Plan | Collect and assess relevant records | Source finding, question, observation period, automatic record status, scope disclosures, Pause/Resume and End, eventual assessment |

A simple goal comparison is fully explained in the selected-goal view. Do not add another page that only repeats the same comparison. A relationship that needs cohort interpretation has its own connection-evidence route. AI review and chat are separate optional destinations, not additional layers required to understand local evidence.

### Navigation and return behavior

- Preserve the current five app tabs: **Today, Timeline, Charts, Chat, Insights**. Use the existing routes; this design does not reinstate the older four-tab shell.
- Preserve the app's Material navigation icons and their selected variants. Keep the existing **Preferences** gear on Today and Insights, with its protected ink backing. The new **Insights Options** overflow is a separate action for saved/hidden findings and related options; it does not replace Preferences. Prototype handoffs do not implement the existing Preferences screen.
- Selecting a goal chip or its summary opens the same selected-goal view. Preserve goal identity, finding identity, and evidence version across these entry points.
- The whole summary card is one accessible action. Its footer describes that action; do not nest a separate competing link inside the card.
- Returning from evidence, plan, or contextual chat restores the originating goal, scroll offset, and expanded disclosures. Returning to All Goals restores the originating card position when navigation came from that list.
- The chosen goal persists during refresh. If it loses findings, keep the selection and explain the data gap. If the goal is no longer saved/available, return to All Goals and explain the change without inventing a replacement goal.
- Opening a finding marks that evidence version reviewed; browsing All Goals does not mark every result reviewed. Review state is independent of rewards, saved state, hidden state, and plan progress.
- Theme changes preserve selection, scroll position, disclosures, draft questions, and plan state. They do not rerun analysis or change numbers.

## Fixed goals and Filter Insights

### Selection contract

**Filter Insights** is one horizontally scrolling, single-select row: **All Goals**, followed by the profile's saved and available goals from the app's fixed catalog. There is no custom-goal text entry, generic outcome substitution, More Filters button, log-type row, or filter sheet in this approved design. Supporting log types belong to evidence and Timeline destinations.

Use each exact catalog label in Capital Case, including punctuation and the lowercase **a** in **See If a Treatment Is Working**. Do not apply automatic title casing or derive identity from visible text. Profile selection determines which fixed labels appear; it does not supply arbitrary wording. **Fewer, Milder Symptoms** is always included by the current app profile contract. An uninitialized/invalid goal selection still leaves All Goals usable.

Selection updates immediately, with a check and an accessible selected state. Keep the full label; let the row scroll rather than abbreviating it or opening another step. Reveal the selected chip when needed. At larger text sizes, the row remains horizontally scrollable, while content below reflows vertically. A result count, if announced, counts the displayed goal summaries rather than misleadingly counting the same multi-goal finding twice.

The filter panel includes **Rule-Derived · On Your Device** as a shared source label for the local comparisons and connections below. The separately labeled AI entry opens an independently attributed review. Today includes **New Finding · Rule-Derived** on its highlight; connection detail includes **Rule-Derived · Possible Connection** and its period/device context. Source attribution must remain visible without forcing every summary to repeat a large badge.

### Goal labels and icons

Verified against `HealthGoal` in the consuming app's `lib/models/onboarding_options.dart` on October 27. This table maps stable production keys to the approved visual meaning; reference-library names are not a requirement to add a second icon runtime to the native app.

| Production key | Exact label | Approved icon metaphor / reference |
| --- | --- | --- |
| `resolveSymptoms` | Fewer, Milder Symptoms | Heart/pulse · `heart-pulse` |
| `betterDigestion` | Better Digestion | **Stomach outline** · supplied Health Icons asset; never meal cutlery |
| `betterSleep` | Better Sleep | Moon · `moon` |
| `beMoreActive` | Be More Active | Footsteps · `footprints` |
| `improveBloodPressure` | Improve Blood Pressure | Pressure gauge · `gauge` |
| `medicationConsistency` | Take Medications Consistently | Pill · `pill` |
| `seeTreatmentWorking` | See If a Treatment Is Working | Assessment clipboard · `clipboard-list` |
| `understandCycle` | Understand My Cycle | Calendar · `calendar-days` |
| `moreEnergy` | More Energy | Energy bolt · `zap` |
| `betterMood` | Better Mood | Face · `smile` |
| `lessStress` | Less Stress | Breath/wind · `wind` |

Reuse the same goal icon and label in its summary, selected view, gathering-context row, and Today finding. Goal icons convey identity, not measured success, diagnosis, adherence, or current mood. The stomach silhouette is the approved exception to the otherwise consistent outline family. Keep its supplied geometry and optical weight.

Cycle availability follows `HealthGoal.availableFor`; this presentation does not broaden it. Cycle, energy, mood, and stress remain device-only, including exclusion of their goal names from cloud profile context. The eleven-goal reference catalog is not an all-selected user profile.

## Today insight region

### Order and density

1. **Applicable care notice.** Rule-derived urgent context leads the region and keeps its required wording and scope.
2. **Today's Plan**, when relevant. Show actual plan title, day/status, concise automatic record rows, and View Plan. The sample is Sleep and Activity Check, Day 6 of 14.
3. **One new/useful finding.** Goal icon and exact label, New Finding when justified, factual takeaway, values and periods, sample context, relevant connection count, and the standard goal footer.
4. **Your Progress** and other existing Today content. Preserve actual rewards and logging controls; do not convert rewards into a health score.
5. **See All Insights**, opening Insights with All Goals.

No full AI narrative, separate long Correlations list, or long Recommendations list appears on Today. Aim for one or two lines of takeaway at default type size; this is a writing target, not a height clamp or ellipsis rule. Essential limitations expand the card.

### Highlight eligibility and reviewed state

Choose eligible, non-hidden, materially changed or not-yet-reviewed evidence relevant to saved goals. Use analyzer-defined evidence adequacy and stable identity to resolve ties. Care urgency is independent of this ranking. Do not rank by alarming wording, AI confidence tone, or narrative length. Do not fill a slot with an unrelated statistic.

If there is no newly useful finding, show **You're Up to Date** with access to existing findings. Early data uses **Your First Findings Are Taking Shape**. Neither state implies that all health is normal, that an analysis succeeded when it failed, or that more entries guarantee a finding. No reward acknowledgement gates access to Insights.

### Compact plan rows

Rows show a status icon, record type, and derived status text. They are **not editable checkboxes**. In the compact Today card, View Plan is the route to the record controls. Show **Tracked from your logs** to explain the automatic behavior. A check means the required record information exists for the applicable day; it never means a health outcome was achieved.

## Insights overview

### All Goals order

| Order | Region | Required behavior |
| --- | --- | --- |
| 1 | Care context | Remains visible regardless of goal selection or AI state |
| 2 | Filter Insights and freshness | One functional group; timestamp is the actual successful local analysis, not the last attempt or AI refresh |
| 3 | A Closer Look With AI | Compact purple-accent entry when the optional overall review is available; concise scope-specific subtitle |
| 4 | Goal summaries | One summary for each saved goal with eligible comparison or connection evidence |
| 5 | Still Gathering Context | Compact rows for saved goals without an eligible finding; exact labels and relevant missing-data destinations |
| 6 | Other Findings | Access to supported observations outside saved goals; never force an unrelated finding into a goal |
| 7 | Your Active Plan | Global access to the existing plan, preserving actual state |

Keep goal order stable using the product's saved/catalog order. Do not reshuffle on every AI generation. A supported comparison leads a goal card; a relevant connection can lead when no direct comparison is available. The Better Sleep example explicitly says that its sleep progress comparison is not yet available while still exposing the sleep–activity connection.

All Goals is organized by goal, not one card for every raw analyzer output. The same relationship may be relevant to Better Sleep and Be More Active, but retains **one finding identity and evidence version**. Do not count it as two independent discoveries or duplicate it inside a selected goal. All eligible results must remain reachable; a concise overview must not silently discard secondary evidence.

### Summary-card anatomy

| Region | Required content | Hierarchy |
| --- | --- | --- |
| Goal identity | Fixed goal icon and exact label | Stable semantic anchor; label at medium weight |
| Takeaway | One concrete observation | Strongest prose in the card; e.g. You logged 120 more active minutes |
| Comparison | Current value, unit, previous value when supported | Current value emphasized; previous period remains readable |
| Time and coverage | Actual windows, counts, unknown prior coverage, essential qualifier | Visible supporting text, never fabricated or tooltips only |
| Connection context | Actual count or brief relevance statement when present | Supporting content above the footer, not the navigation label |
| Footer | **Explore more about [Goal Name]** + trailing chevron | Consistent wording, alignment, color, and divider across all goal summaries |

Examples: **Explore more about Better Digestion**, **Explore more about Be More Active**, and **Explore more about More Energy**. Use the exact goal text after the prefix, even when it forms a less conversational phrase. Do not substitute View comparison, 1 possible connection, Explore this connection, or Stays on this device for this footer.

Device-only attribution is a non-interactive note in the selected-goal view. It is not an action label. Footer text wraps for long goal names and larger text without truncating meaning; the chevron remains visible. A screen-reader announcement includes the goal, takeaway, period, and destination without reading decorative glyphs.

## Selected-goal view

Keep the Filter Insights row and selected goal visible at the start of the view. Below it, show the following in order:

1. Goal icon and exact label, with **Change in Your Records** when a comparison exists.
2. Concrete takeaway and the **complete supported comparison**.
3. **About This Comparison**, an expandable plain-language explanation of measurement, periods, coverage, and local calculation.
4. **View Logs From This Period**, opening Timeline with relevant record types and dates. These are period records and can include entries outside the calculation; do not label them all as supporting evidence.
5. Device-only note when applicable.
6. Relevant **Possible Connection** cards, then the related plan if one exists.
7. **Ask About This Finding**, only when the finding is shareable and chat eligibility/consent permits that route.

The comparison and any material limitation are visible by default. Methodological detail may expand. Do not make the user open a second page solely to see the same two values. Do not show the sleep/activity plan under Better Digestion or More Energy solely because it is the account's active plan.

### Comparison rules

| Example | Rendered evidence | Required interpretation |
| --- | --- | --- |
| Be More Active | 560 min vs 440 min; 10 active days in each period | Recorded duration increased by 120 minutes; active-day count did not increase |
| Better Digestion | 20% vs 67%; 2 of 10 recent logs; earlier count unavailable | Percentages describe logged bowel movements; the earlier denominator remains unknown |
| More Energy | 5.9/10 vs 3.8/10; 12 rated days; earlier count unavailable | Recorded average ratings changed; missing ratings are not zero; device-only |
| Better Sleep | No direct progress comparison; sleep–activity relationship exists | Distinguish a missing comparison from absence of all relevant evidence |

Use two horizontal bars with a common zero baseline and scale, explicit period labels, values, units, and counts. Percentage scales end at 100%; rating scales use the actual scale endpoint; totals share a meaningful common maximum. Do not invent a time series from two aggregates or a progress ring without a real target. Earlier values use the secondary comparison role, not an arbitrary success/failure color.

If the comparator or required value is absent, explain the unavailable comparison rather than substituting zero. If a supplied percentage is valid but its historical sample count is unavailable, show the percentage with that explicit limitation. Use **recorded**, **logged**, or **rated** to avoid claiming complete knowledge of daily life. The screenshot's Bristol grouping and time periods are fixtures; production definitions come from the analyzer.

## Connection evidence and source records

### Finding detail anatomy

A connection card uses signal icons and names separated by a thin non-directional link: **Sleep — link — Activity**. Do not use a causal arrow, decorative correlation network, or confidence ring. The card states the association in plain language and exposes **Explore the evidence**; this differs from a goal footer because it opens a different destination.

The evidence screen presents source/type and observation period, the signal relationship, complete claim, two named comparison groups, values and counts, a visible limitation, **How to Read This Comparison**, **Browse Sleep and Activity Logs**, optional AI follow-up, and the related plan or eligible plan preview.

The reviewed example compares **After short or poor sleep** with **No short/poor-sleep flag**. Activity was logged on **1 of 5 days (20%)** in the first group and **9 of 9 days (100%)** in the second. These labels describe the analyzer's flag, not proof that the second group slept well. Retain that explanation. Do not rename the second group Other Recorded Days, Healthy Sleep, or No Sleep Problems.

The visible limitation is **This is an association, not evidence that sleep caused the difference.** Supporting explanation notes that missing records, symptoms, and other routines may affect the apparent relationship. Absence of an activity log is not proof of inactivity. No symptom record is not proof of being symptom-free.

### Evidence navigation

- Open by stable finding ID plus evidence version. A refresh cannot silently change the basis of a detail already being read; disclose when newer evidence exists.
- Browse actions open the existing Timeline with an explicit period/type filter and a clear exit. A general period query is distinct from the exact supporting-entry set.
- Use actual evidence references for an action labeled as supporting evidence. If entries have been deleted or become inaccessible, explain the gap and reevaluate the finding's eligibility.
- Do not parse numbers, dates, or entry IDs out of generated prose. A missing structured link changes the available action.

## AI Review and chat

### Overall review

**A Closer Look With AI** opens **AI Review**. The header inside the first reading surface is **AI-Assisted · Across Your Findings**, then **What Stands Out** and its own reviewed timestamp. Local analysis time and AI review time are independent.

Present up to three concise takeaways, each containing a relevant icon, short heading, one factual supporting sentence, and a link to the matching comparison or connection. Three is a maximum for the initial summary, not a requirement to manufacture content. The full explanation preserves additional eligible findings rather than dropping them to fit this summary.

Below the takeaways, provide **Read the Fuller Explanation** and **What This Review Includes** as expandable sections. Their content must remain legible paragraphs, not another dense uninterrupted block. Then show **Continue the Conversation** with editable suggested questions. Purple identifies AI authorship/scope; local evidence and goal icons retain their own meaning.

An earlier review begins with **Newer Records Are Available** and keeps its original timestamp. Its links resolve the evidence snapshot it interpreted, or explicitly explain that historical support is no longer available. Never pair yesterday's AI conclusion with today's changed chart as though they were one analysis.

### Follow-up flow

1. Open from the overall review or a permitted finding. Display **Discussing Your Overall Review** or **Discussing This Finding** with the actual context title.
2. **What AI Can Use** explains the permitted context. For a finding, the selected finding anchors the discussion; any other eligible shared findings are disclosed by the existing context policy.
3. A suggested question populates the composer as an editable draft. It is not sent by tapping the suggestion or opening chat.
4. **Send** explicitly submits the question. Empty, sending, disabled, failed, and unavailable states remain distinct. Prevent duplicate submission, preserve unsent drafts, and allow the existing retry flow.
5. Label assistant replies **AI-Assisted**. References in a response must resolve back to the same permitted evidence.
6. Back returns to the originating view. Switching context cannot silently attach an earlier draft or answer to an unrelated finding.

### Sharing and availability boundaries

AI Review and AI Chat are separate preferences. Turning either off does not remove local comparisons, connections, plans, or logging. A disabled or unavailable service provides its state and the appropriate preferences/retry destination; it does not insert filler explanation.

Only eligible structured findings permitted by the user enter AI context. The presentation does not grant new sharing permission for full diary records, notes, photos, excluded entries, or device-only domains. Energy, mood, stress, and cycle remain excluded, including indirectly through profile goal names, overall summaries, saved items, and suggested questions. More Energy therefore has local comparison details and a device-only note, but no finding-specific AI action. These rules also apply to deep links and restored navigation state.

## Plans and automatic record tracking

### Plan purpose and placement

A plan is a user-chosen observation process tied to a finding and a question. It is not a promise to confirm a cause, a prescribed treatment, or a health score. The review fixture is **Sleep and Activity Check**, asking **Does the sleep–activity pattern keep appearing?** Its 14-day duration and Day 6 display are examples, not universal plan policy.

Show the plan globally on Today and All Goals, and only under its related goals (Better Sleep and Be More Active in the fixture). Preserve its stable identity if reached from more than one goal. **View Plan** opens that plan, not a generic Insights page.

### Preview and start

**Preview a Plan** opens the source finding, question, observation period, required record details, what can be assessed, and important limitations. **Start This Plan** is explicit. Opening evidence, asking a question, or reading a preview never starts a plan. Existing safety/eligibility policy controls whether a new plan may be offered. No action changes medications or treatment preferences.

### Plan detail order

| Order | Content |
| --- | --- |
| 1 | Related goal names, plan title, actual phase/day, question |
| 2 | **Today's Records** and **Tracked Automatically**, or assessment state when the observation period ends |
| 3 | **Source Finding** link to the original evidence |
| 4 | **What This Plan Will Assess**: variables, comparison basis, and limits |
| 5 | **If You Notice Symptoms**: optional contextual logging, never a daily symptom-free task |
| 6 | **Manage This Plan** with full-width Pause/Resume and End buttons |

### Deriving row status

For the example, Sleep requires **duration and quality**; Activity requires **duration and effort**. A valid entry with missing required fields is partial. Imported entries count only if they meet the same field, validity, and date rules. The UI consumes the plan's explicit qualifying-record rules rather than assuming that any log of that type is enough.

| State | Appearance and meaning | Action |
| --- | --- | --- |
| Not Recorded | Open circle and visible label; no qualifying entry for the applicable day | Add Entry |
| Details Needed | Partial/attention cue and label; relevant entry exists but required fields are incomplete | Complete the existing entry |
| Recorded Today | Check-circle plus label; required valid fields are present | View Entry |
| Paused | Pause icon and label; plan tracking is paused | Diary entry remains available; Resume is in plan management |
| Loading or unavailable | Explicit pending/unavailable status | Never temporarily report Not Recorded or Recorded Today without evidence |

Status icons are display-only, not toggles. An entry save, edit, deletion, import, or synchronization updates derived status and assessment eligibility. Removing a qualifying record can return a row to partial/not recorded. Do not keep a stale green check as a reward. Multiple qualifying entries use the plan's aggregation rule; a single chosen entry must not hide conflicting or incomplete evidence.

Use the app's established record date, timezone, and sleep-day assignment rules. A day rollover refreshes Today rather than marking yesterday's record as today's. Pausing/resuming preserves the plan's actual calendar/phase rules and communicates any changed end date; the display must not invent a new pause-clock policy. Offline local entries can update local status; pending synchronization is separate from record completeness.

### Manage This Plan

**Pause Plan** and **End Plan** are stacked, full-width outlined buttons, not bare text links. Use the app's 9-unit button radius, 48-unit reference minimum height, 12-unit vertical gap, centered icon and label, and tested control outlines. Pause uses a pause icon and the neutral secondary control backing. End uses a stop-square icon and the theme attention foreground/outline; the action is also distinguished by its text and icon.

Paused state changes the first button to **Resume Plan** with a play icon. Pause/Resume changes the plan state only; logs remain available. Persist state before reflecting success; a failed save retains the previous state and a retryable explanation.

End opens **End This Plan?** with **Stop this plan's tracking? Your logs remain available.** Provide **Keep the Plan**, **End Plan**, and a dismiss control. The confirmation's End Plan button retains the attention outline/text rather than becoming a generic primary action. Dismissal/cancellation preserves the plan. Confirmed end stops tracking without deleting diary entries and shows **The Plan Ended Early**. Ending a plan is not a successful assessment. Restore focus to the triggering button when the sheet closes.

### Assessment outcomes

End of the observation period produces **Ready to Assess**, not automatic success. **Assess the Available Records** evaluates supported comparable records according to the existing plan/analyzer contract.

| Outcome | Required presentation |
| --- | --- |
| Pattern still detected | **The Pattern Still Appeared**, with supported comparison and limitations |
| Pattern not detected | **The Pattern Was Not Detected**; absence in assessed records is not proof that no relationship exists |
| Inadequate coverage | **Not Enough Comparable Records**, with the specific missing basis and a route to relevant records |
| Ended early | **The Plan Ended Early**; explain that tracking stopped and entries remain |

Elapsed days are not adherence, efficacy, or health improvement. Assessment never turns association into causation. The prototype's fixed examples and simulated result are not assessment logic.

## Finding display contract

| Field | Presentation requirement |
| --- | --- |
| Finding ID and evidence version/fingerprint | Stable finding separate from generated wording; links, reviewed state, saved state, and AI references resolve the correct version |
| Kind and source | Distinguish comparison, connection, observation, and optional AI explanation; local evidence is not relabeled AI-generated |
| Related goal keys | Reviewed many-to-many mappings to the fixed catalog; no natural-language matching or custom labels |
| Evidence types and references | Structured IDs and permitted records/query; record dates and measurement dates remain distinguishable |
| Windows and timestamps | Actual period boundaries, local analysis success time, and separate AI generation time; disclose stale evidence |
| Metrics | Typed value, unit, scale, aggregation, null/missing state; no unsupported conversions |
| Comparison | Named periods/cohorts, matching denominator and numerator, coverage, eligibility basis, common scale |
| Limitations and confidence | Material caveats visible beside the claim; confidence only if a documented evaluated method supplies it |
| Care scope and urgency | Rule-derived report/finding association and required wording; independent of filters and dismissals |
| Plan association | Stable plan ID, related finding/version/goals, question, phase, duration, record requirements and derived status |
| AI sharing eligibility | Domain exclusions, user consent, review snapshot, context scope; enforced beyond the visible button |
| Viewed/saved/hidden | Separate user states; AI rewording alone does not create new evidence |

Some fields require an adapter from the existing `LocalFinding` contract. Unsupported evidence changes the display; do not recover missing values by parsing AI narrative. **Possible Connection** is a type, not a confidence grade. Do not invent high/medium/low badges or confidence percentages.

Saving bookmarks a finding independently of review state. Hiding removes the selected evidence version from routine display and offers restoration; it cannot remove applicable care notices. Stronger recurrence suppression, if exposed by existing controls, must be explicitly labeled and reversible. Materially changed evidence may reappear after ordinary hiding, but not merely because an AI sentence changed. Feedback distinguishes usefulness, accuracy, and safety concerns without rewriting evidence or clinical rules.

## State matrix

| State | Required visible behavior | Available path |
| --- | --- | --- |
| Local analysis loading | Stable pending content; retain last-successful data with its date when appropriate | Logging remains available |
| Early or insufficient records | Still Gathering Context; identify the relevant data gap without an arbitrary entry-count promise | Open that goal and relevant records |
| Complete analysis with no eligible findings | Explain that no supported finding is available for the window; distinguish from failure and not-yet-analyzed | Existing history/logging |
| No new findings | You're Up to Date on Today; existing goal results remain on Insights | See All Insights |
| Goal has no direct comparison | Explain that comparison's missing basis; show relevant connections separately if available | Goal records and connection evidence |
| No clear connection | Explicit absence of a supported connection; retain a valid direct comparison | Compare records |
| AI review off | Compact preferences route; local summaries and plans unaffected | AI Preferences |
| AI unavailable/offline | Preserve local facts and separately dated prior review if available | Explicit retry; retain draft |
| Earlier AI snapshot | Newer Records Are Available before the old review; retain original timestamp and evidence scope | Current local findings |
| Local analysis failed | Failure state distinct from empty/healthy; dated last-successful results may remain | Retry |
| Stale evidence | Actual period and original successful date; analyzer-supplied stale state | Refresh permitted analysis |
| Hidden finding | Hidden/restore state rather than claiming no data exists | Restore Hidden Findings |
| Evidence deleted/inaccessible | Explain unavailable support; re-evaluate eligibility and suppress unsupported chart/action | Current findings/records |
| Care notice | Required message, scope, and urgency remain above relevant content in every filter/AI state | Existing care destination |
| Active/partial/paused plan | Derived row state and correct management action | Add/complete/view records; pause/resume/end |
| Ready/assessed/ended plan | Distinct phase and supported outcome; no automatic success | Assess or review records |

No universal stale-after threshold, clinical trigger, inference threshold, or minimum sample size is introduced by this presentation. These remain analyzer/policy responsibilities.

## Visual specification

### Shell, surfaces, and spacing

Use [App Visual Specification](../02-design/app-visuals.md), [Cards](../02-design/cards.md), [Spacing System](../02-design/spacing-system.md), [Buttons](../02-design/buttons.md), and [Dark Mode & Accessibility](../02-design/dark-mode.md). The following approved Insights-specific hierarchy is an additive local contract, not a global token restyle.

| Element | Approved reference geometry |
| --- | --- |
| Body gutters / section gaps | 12 / 12 logical units |
| Existing shell header | 124-unit Today logo; 60-unit toolbar below the platform status area; 44-unit iOS header controls with 12 radius and protected ink backing |
| Body top / bottom inset | 10 / 14, plus safe-area and capture-action clearance |
| Reading card | Opaque surface; 14 padding, 14 radius, 1 decorative outline; no extra outer margin |
| Goal identity | 38 × 38 tinted backing, 11 radius; 22-unit outline icon; stomach 26-unit optical box |
| Goal header | Icon/label gap 10; label 16/22.4, weight 500 |
| Summary takeaway | 18/25.2, weight 500; 12 above, 9 below; no fixed line count |
| Summary current value | 20/30, weight 500; unit and previous value remain explicit |
| Body / metadata | 14/22.4 regular / 12/18 regular; material limitations may use 13/20.8 |
| Detail takeaway / evidence value | 22/29.7 medium / 24/31.2 medium; use these to prioritize evidence, not every card heading |
| Summary footer | 1-unit separator; 11 top gap, 9 top padding; 12/18 text and trailing chevron |
| Filters | 44-unit minimum target; 9 radius; 8 gap; complete labels in a horizontal scroll row |
| Disclosures | 44-unit minimum trigger; label and plus/minus or equivalent expanded cue; 14 above separator |
| Evidence bars | 8 height, 3 radius, shared zero baseline; no decorative outline on quantitative marks |
| Plan-management buttons | 48 minimum height, 9 radius, 12 vertical gap, full width |
| Filled primary actions | 48 minimum height; 9 radius; 14/20 label at weight 600; primary/onPrimary colors, distinct from selected filters |
| Navigation | Existing Material icon variants at 22; labels 12/18, weight 400 unselected and 600 selected; native 72-unit bar plus actual bottom safe area |
| Capture actions | Existing 54 height; Quick Log radius 28, Log radius 12; reachable content clear of controls |

These numbers describe the reference at default text size. Native controls use at least **44 pt on iOS and 48 dp on Android**, including compact visual actions. Do not copy a 32-unit visual action as a smaller hit target. The screenshot's fixed 852 height, illustrative status bar, and preview frame are not production layout constraints. The general overlay contract governs native sheets; preview-only sheet geometry is not a new token exception.

Use Inter 400/500 for the approved Insights content hierarchy and Inter 600 for the existing selected navigation and primary-button roles, with approved fallbacks. Emphasis comes from takeaway size, data, icons, spacing, and grouping; avoid undifferentiated white text across nested layers. Comparison content uses unframed sections inside a reading surface. The existing three Your Progress metric tiles remain the bounded nesting exception. Preserve that component's current 20-unit heading icon, 18-unit value icons, 20-unit values, New badge, trailing chevron, and whole-group earned-badges destination; the display-only tiles are not separate actions. Its existing 700-weight New label does not establish a new Insights text role.

### Light and dark roles

| Role | Light | Dark |
| --- | --- | --- |
| Reading surface | Ivory `#FAF8F4` | Ink `#192D38` |
| Main text | `#192D38` | `#FAF8F4` |
| Supporting text | `#506F7E` | `#B8CBCB` |
| Link / current comparison | `#206668` | `#8DC7B7` |
| Neutral control backing | `#F1F0EC` | `#264C4B` |
| Selected control / foreground | `#192D38` / white | `#223D49` / `#8DC7B7` |
| Filled primary action / foreground | `#287E80` / white | `#76B7A5` / `#192D38` |
| Selected navigation pill / icon | `#192D38` / white; no contrasting pill outline | `#264C4B` / `#8DC7B7`; required outline `#8DA4A6` |
| Selected navigation label | `#192D38` | `#8DC7B7` |
| Unselected navigation content | `#192D38` | `#FAF8F4` |
| Decorative card outline | `#D8DEDA` | Copper `#C88764` |
| Display-only progress tile outline | `#DDDFDA` | Copper `#C88764` |
| Internal separator | `#D8DEDA` | `#45616A` |
| Required control outline | `#567788` | `#8DA4A6` |
| Attention text / backing | `#845800` / `#FAF8F4` | `#E5B86A` / `#223D49` |
| AI text / soft backing | `#6748D8` / `#F0ECF8` | `#B7A7FF` / `#263146` |
| Goal icon backing | `#E9F1ED` | `#24423F` |
| Previous-period bar | `#567788` | `#8DA4A6` |

Reuse existing native tokens/adapters for shared shell, controls, text, attention, and semantic AI foregrounds. Goal-icon backing, AI soft backing, the restrained internal divider, and previous-period evidence marks are named Insights-specific component roles; they are not claims that those aliases already exist in the shipping app. Register those local aliases during implementation rather than scattering literal colors across widgets. Decorative outlines do not substitute for required control boundaries. Purple indicates AI meaning, not the whole Insights feature. Selection, record completeness, and care urgency each retain a text/icon cue.

Retain the exact yarn texture, crop treatment, protected header ink shading, canonical logo, and copper header rule. The rule fades from transparent at 0% to full copper at 16–84% and transparent at 100%; dark navigation retains that soft rule while light navigation uses the neutral separator. Header actions use the existing 92%-ink backing; illustrative status icons receive protection too. Reading surfaces stay opaque over the artwork in both themes. A quiet/reduced-transparency appearance removes the decorative texture without removing content or contrast. Test text and controls against their resolved backgrounds rather than assuming a token's name guarantees contrast.

## Accessibility and responsive behavior

- Use semantic headings, native buttons, selected states, disclosures, tab navigation, and modal focus containment. Goal icons and chevrons are decorative when adjacent text carries their meaning.
- A goal card is one target with a meaningful destination name. Plan statuses are readable status text, not checkboxes. Announce a status change after an entry save without repeatedly announcing the whole screen.
- Allow larger text and localization to expand all cards, values, labels, footers, and controls. Main content scrolls vertically; only the Filter Insights row scrolls horizontally. Never clip a material limitation or hide an action behind the bottom navigation/capture controls.
- Expose comparison text including both values, units, periods/cohorts, and counts. No meaning depends only on bar length, color, icon, or relative position.
- Maintain 4.5:1 ordinary text contrast and the applicable 3:1 large-text/essential non-text requirements from the existing accessibility standard. Validate composited backgrounds and disabled/pressed/focused states separately.
- Support visible keyboard focus, native Back, VoiceOver/TalkBack order, focus restoration, reduced motion, reduced transparency, and System/Light/Dark appearances. Do not animate initial evidence as though values are still being calculated.

## Acceptance criteria

| ID | Reviewable requirement |
| --- | --- |
| IP-01 | Today has at most one brief new/useful finding, automatic plan summary when applicable, and existing progress/logging access; no full AI narrative |
| IP-02 | Filter Insights uses only All Goals plus saved/available fixed goal keys, exact labels, and the approved icons; no custom goals, log-type row, or More Filters step |
| IP-03 | Every goal summary uses Explore more about [Goal Name], wraps safely, and opens the same selected-goal destination as its chip |
| IP-04 | More Energy's device-only statement is non-interactive detail context; it is never a footer link or shared AI context |
| IP-05 | All Goals preserves meaningful goal order, gathering-context access, Other Findings, and global plan access without duplicating evidence identity |
| IP-06 | Selected-goal comparisons show exact values, units, windows, and counts; missing baselines/coverage stay explicitly unavailable |
| IP-07 | Sleep's missing direct comparison does not suppress its supported connection; unrelated goals do not show the sleep/activity plan |
| IP-08 | Connection groups explicitly describe the flag; bars use one scale; no causal arrow or Other Recorded Days label |
| IP-09 | Goal/connection/source-record routes preserve stable IDs, evidence versions, originating filters, scroll, and expanded disclosures |
| IP-10 | AI review exposes up to three linked takeaways, fuller explanation, context scope, and independent review time; earlier reviews are clearly stale |
| IP-11 | Suggested questions open editable drafts; Send is explicit; context is visible, consent enforced, exclusions maintained, drafts survive failure |
| IP-12 | Automatic plan statuses update after save/edit/delete/import/day rollover; no manual checkmark completion and no symptom absence inferred from silence |
| IP-13 | Pause/Resume and End are visibly framed buttons in both themes; End requires confirmation, keeps logs, and cannot imply assessment success |
| IP-14 | Ready to Assess, insufficient comparison, pattern present/not detected, paused, and ended states are distinct and data-driven |
| IP-15 | Required care context survives selection, hiding, AI-off/unavailable, stale, and empty states; original urgency and scope remain intact |
| IP-16 | Light/dark match the approved backdrop, card geometry, hierarchy, and exact icons; values and behavior are identical across themes |
| IP-17 | Test 320-unit width and enlarged text, long fixed goal labels, footer wrapping, keyboard focus, VoiceOver/TalkBack, modal dismissal, and safe-area clearance |
| IP-18 | Native implementation replaces simulated reference records, clocks, AI responses, and assessment outcomes with actual data; browser references alone are not release evidence |

## Integration and migration

Implement the finding/goal/evidence adapters before replacing the long-form UI. Reuse the fixed `HealthGoal` keys and profile availability rules. Translate icon metaphors to the app's shared icon components while retaining the approved stomach asset. Preserve existing log entry, Timeline, Charts, rewards, consent, care, and analysis services.

Resolve the following against the actual consuming-app contracts during implementation: stable evidence-version storage; historical AI review snapshots; plan date/aggregation and pause-clock rules; multiple-active-plan policy if supported; complete supporting-entry routes; persistence of hidden/saved state; actual AI context enforcement; native accessibility. The visual prototype does not implement these services and must not be used as an analyzer or health-data source.

The new default [reference gallery](../../assets/app/insights-presentation/index.html) is the October 27 design. The [previous Flutter gallery](../../assets/app/insights-presentation/previous-flutter-gallery.html) and earlier assets remain historical; their custom-goal/filter structures and numerical examples do not override this specification. The editable source and capture scene definitions are in `tooling/insights-journey-reference/`. This approved documentation amendment does not implement or deploy the consuming app.

Controlling references: [Insights and Correlations](insights-and-correlations.md), [App Visual Specification](../02-design/app-visuals.md), [Progress and Disclosure](../02-design/progress-and-disclosure.md), [Insight Types](../05-ai/insight-types.md), [Confidence and Evidence](../05-ai/confidence-and-evidence.md), and [Hybrid Local Findings](../../adr/0010-hybrid-local-findings-optional-llm.md).

## Version History

- 2026-10-27: Integrates the approved refined journey, fixed goal catalog/icons, consistent goal-specific footers, automatic plan tracking, outlined plan management, brief AI review and contextual chat. Adds 38 high-fidelity app-only references, detailed display/state/interaction contracts, and implementation acceptance criteria. Approved for publication after local review.
- 2026-10-25: Earlier overview/detail and filter experiments, including Flutter captures. Retained as historical references and superseded by the October 27 design.
