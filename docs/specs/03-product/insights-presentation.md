# Insights Presentation

Status: Connection-led design, capability scope, and documentation approved for publication; implementation pending

Owner: Product, Design System, and AI Working Groups

Version: Unreleased

Last updated: 2026-10-27

Decision: [ADR-0017](../../adr/0017-adopt-goal-led-insights-presentation.md), proposed in [RFC-0011](../../rfc/0011-goal-led-insights-presentation.md)

## Purpose and authority

Make findings easy to scan, understand, and act on. **Today** answers “what deserves my attention now?” **Insights** answers “what connections are appearing between my habits, symptoms, and wellbeing?” A goal card leads with a useful association and a short explanation; detailed evidence and ordinary period comparisons follow in the drilldown.

This amendment carries the approved connection-led visual direction into PL-OS using the owner's [capability decisions](insights-findings-capabilities.md). It supersedes the earlier October 27 comparison-first landing page. Fixed goal names, **Filter Insights**, the stomach icon, automatic plan statuses, outlined plan buttons, and **Explore more about [Goal Name]** footers remain part of the design. Clinical rules, consent, cloud exclusions, and other app features retain their governing contracts.

Goal mapping, evidence-based maturity assessment, and distinct-period recurrence are approved implementation requirements, **not claims about the shipping model**. The current reference uses **Possible Connection** until evaluated maturity criteria exist. It does not depict a walking/sleep analyzer, verified symptom-free meal follow-ups, or a plan that tracks a specific pair of signals. Those capabilities are deferred.

Sustained logging can improve the chance of identifying useful connections and understanding how consistently they appear. It never guarantees a finding, a symptom-free conclusion, or proof of causation. The [consistency review](insights-presentation-review.md) separates this amendment's checks from historical capture validation. The owner approved this documentation amendment for publication on 2026-10-27.

## Production intent screen references

[Open the full-resolution reference gallery](../../assets/app/insights-presentation/index.html){ .md-button }

The current gallery contains **12 app-only JPEGs: six views in each theme**, rendered at **393 × 852 logical units / 1179 × 2556 pixels**. Fonts, icons, charts, and layout are rasterized directly at 3×, without resizing a thumbnail. The canonical woven artwork continues behind the scroll area; reading surfaces stay opaque. Light and dark show identical fixture evidence.

These are high-fidelity **browser-rendered design references**, not shipping Flutter screenshots or analyzer-verified personal records. Status bars, dates, records, and plan state are illustrative. No chat transcript, browser chrome, or review caption is embedded in the app images. Details and longer pages scroll naturally; an image does not imply the entire page must fit one viewport.

[Manifest and source hashes](../../assets/app/insights-presentation/connections-first-2026-10-27/references.json) record capture dimensions, state, and provenance. [Inspectable reference](../../assets/app/insights-presentation/connections-first-2026-10-27/reference.html?scene=insights&theme=light&scale=1) supports the principal navigation for design review. Individual diary records and AI responses are not implemented by this reference.

<!-- CONNECTIONS_GALLERY_START -->
### Insights Overview

Potential habit/outcome links lead; fixed goals filter the overview. Counts and comparisons are in details.

| Light | Dark |
| --- | --- |
| [![Insights Overview — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-light.jpg?v=15070eee405d){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-light.jpg?v=15070eee405d) | [![Insights Overview — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-dark.jpg?v=fcbc5b016708){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-dark.jpg?v=fcbc5b016708) |

### Today

Existing domain-based meal/symptom plan and one local activity/energy finding. Plan status comes from logs.

| Light | Dark |
| --- | --- |
| [![Today — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/today-light.jpg?v=50a5d1becd9e){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/today-light.jpg?v=50a5d1becd9e) | [![Today — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/today-dark.jpg?v=dcc62267f7aa){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/today-dark.jpg?v=dcc62267f7aa) |

### Better Digestion · Evidence

Logged meal/bloating co-occurrence with honest bidirectional timing, denominators and missing-observation limits.

| Light | Dark |
| --- | --- |
| [![Better Digestion · Evidence — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-light.jpg?v=473e515da51c){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-light.jpg?v=473e515da51c) | [![Better Digestion · Evidence — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-dark.jpg?v=1754b34c0816){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-dark.jpg?v=1754b34c0816) |

### More Energy · Evidence

Same-day activity/energy averages on the actual /10 scale, with rated-day counts. Device-only; no AI follow-up.

| Light | Dark |
| --- | --- |
| [![More Energy · Evidence — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-light.jpg?v=90c8b16f9faf){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-light.jpg?v=90c8b16f9faf) | [![More Energy · Evidence — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-dark.jpg?v=f5a2d6e9ae36){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-dark.jpg?v=f5a2d6e9ae36) |

### Still Gathering Context

The selected fixed goal has no eligible relationship yet. No promise that additional logs guarantee one.

| Light | Dark |
| --- | --- |
| [![Still Gathering Context — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-light.jpg?v=500dca845dec){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-light.jpg?v=500dca845dec) | [![Still Gathering Context — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-dark.jpg?v=a54c259d392b){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-dark.jpg?v=a54c259d392b) |

### Domain Plan · Management

Current meal/symptom plan, conditional symptom logging, automatic status, and outlined Pause/End controls.

| Light | Dark |
| --- | --- |
| [![Domain Plan · Management — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-light.jpg?v=3f9b63d780e3){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-light.jpg?v=3f9b63d780e3) | [![Domain Plan · Management — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-dark.jpg?v=6743feffda87){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-dark.jpg?v=6743feffda87) |

<!-- CONNECTIONS_GALLERY_END -->

The [previous comparison-first gallery](../../assets/app/insights-presentation/previous-goal-comparison-gallery.html) remains historical. Its 38 captures do not override the new hierarchy, fixtures, maturity requirements, or plan scope. The written AI, care, and plan-state requirements below continue to govern states not pictured in the current six-view gallery.

## Information architecture

| Surface | User question | Content order |
| --- | --- | --- |
| Today | What is useful today? | Applicable care notice, compact current plan, one useful relationship or meaningful-change fallback, existing Your Progress and logging |
| Insights overview | What links are appearing for my goals? | Care context, Filter Insights and freshness, connection-led summaries, gathering-context goals, optional eligible AI entry, Other Findings, active plan |
| Goal details | What supports this finding? | Leading relationship and short context, actual evidence and limitations, supporting records, secondary findings and period comparisons, permitted follow-up |
| Additional finding details | What supports another result? | Same evidence anatomy, with a distinct stable relationship identity and evidence version |
| AI Review / chat | What questions could I explore? | Independently attributed, eligible context and optional explanation; never needed to read local evidence |
| Plan | What records does this plan follow? | Existing domain-based local plan, automatic record status, scope, management, supported assessment |

The first goal-detail view explains its leading finding directly. Do not introduce a second required tap to reveal the same evidence. A secondary finding can open its own detail. Optional AI prose does not displace local findings.

### Navigation and return behavior

- Preserve the current five app tabs: **Today, Timeline, Charts, Chat, Insights**. Use the existing routes; this design does not reinstate the older four-tab shell.
- Preserve the app's Material navigation icons and their selected variants. Keep the existing **Preferences** gear on Today and Insights, with its protected ink backing. The new **Insights Options** overflow is a separate action for saved/hidden findings and related options; it does not replace Preferences. Prototype handoffs do not implement the existing Preferences screen.
- Selecting a goal chip filters the overview in place; it does not open a detail page. Selecting the summary (including its footer) opens that goal’s leading finding and detail. Preserve selected goal, relationship identity, and evidence version through navigation.
- The whole summary card is one accessible action. Its footer describes that action; do not nest a separate competing link inside the card.
- Returning from evidence, plan, or contextual chat restores the originating goal, scroll offset, and expanded disclosures. Returning to All Goals restores the originating card position when navigation came from that list.
- The chosen goal persists during refresh. If it loses findings, keep the selection and explain the data gap. If the goal is no longer saved/available, return to All Goals and explain the change without inventing a replacement goal.
- Opening a finding marks that evidence version reviewed; browsing All Goals does not mark every result reviewed. Review state is independent of rewards, saved state, hidden state, and plan progress.
- Theme changes preserve selection, scroll position, disclosures, draft questions, and plan state. They do not rerun analysis or change numbers.

## Fixed goals and Filter Insights

### Selection contract

**Filter Insights** is one horizontally scrolling, single-select row: **All Goals**, followed by the profile's saved and available goals from the app's fixed catalog. There is no custom-goal text entry, generic outcome substitution, More Filters button, log-type row, or filter sheet in this approved design. Supporting log types belong to evidence and Timeline destinations.

Use each exact catalog label in Capital Case, including punctuation and the lowercase **a** in **See If a Treatment Is Working**. Do not apply automatic title casing or derive identity from visible text. Profile selection determines which fixed labels appear; it does not supply arbitrary wording. **Fewer, Milder Symptoms** is always included by the current app profile contract. An uninitialized/invalid goal selection still leaves All Goals usable.

Selection updates immediately, with a check and an accessible selected state. Keep the full label; let the row scroll rather than abbreviating it or opening another step. Reveal the selected chip when needed. At larger text sizes, the row remains horizontally scrollable, while content below reflows vertically. A result count, if announced, counts distinct displayed relationships, not duplicate goal mappings. Changes and gathering-context states are not counted as new relationships.

The filter panel includes **Rule-Derived · On Your Device** as a shared source label for the local comparisons and connections below. The separately labeled AI entry opens an independently attributed review. Today includes **New Finding · Rule-Derived** on its highlight; connection detail includes **Rule-Derived · On Your Device**, a separate **Possible Connection** or evaluated maturity label, and its actual observation period. Source attribution must remain visible without forcing every summary to repeat a large badge.

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
2. **Today's Plan**, when relevant. Show actual plan title, day/status, concise automatic record rows, and View Plan. The sample is Two-Week Meal and Symptom Check, Day 6 of 14, using the existing meal/symptom domain template.
3. **One new/useful finding.** Goal icon and exact label, New Finding when justified, connection status, named signal pair, factual takeaway, short context/limitation, and the standard goal footer. Period totals and log counts are supporting detail, not the highlight’s main message.
4. **Your Progress** and other existing Today content. Preserve actual rewards and logging controls; do not convert rewards into a health score.
5. **See All Insights**, opening Insights with All Goals.

No full AI narrative, separate long Correlations list, or long Recommendations list appears on Today. Aim for one or two lines of takeaway at default type size; this is a writing target, not a height clamp or ellipsis rule. Essential limitations expand the card.

### Highlight eligibility and reviewed state

Choose eligible, non-hidden, materially changed or not-yet-reviewed evidence relevant to saved goals. Use analyzer-defined evidence adequacy and stable identity to resolve ties. Care urgency is independent of this ranking. Do not rank by alarming wording, AI confidence tone, or narrative length. Do not fill a slot with an unrelated statistic.

If there is no newly useful finding, show **You're Up to Date** with access to existing findings. Early data uses **Your First Findings Are Taking Shape**. Neither state implies that all health is normal, that an analysis succeeded when it failed, or that more entries guarantee a finding. No reward acknowledgement gates access to Insights.

### Compact plan rows

Rows show a status icon, record type, and derived status text. They are **not editable checkboxes**. In the compact Today card, View Plan is the route to the record controls. Show **Tracked from your logs** to explain the automatic behavior. A check means the required record information exists for the applicable day; it never means a health outcome was achieved. Conditional symptom logging says **When Noticed** rather than showing an overdue daily symptom task. The absence of a symptom log is unknown.

## Insights overview

### All Goals order and selection

1. Required care context, independently of filter or AI state.
2. **Filter Insights**, actual successful local analysis timestamp, and **Rule-Derived · On Your Device**.
3. Connection-led summaries. Prefer eligible relationships over simple progress comparisons, even when a direct goal comparison is available.
4. **Still Gathering Context** for selected goals without supported findings.
5. **A Closer Look With AI**, when available and scoped to eligible findings. It follows local findings and does not summarize excluded wellbeing goals.
6. **Other Findings** for useful results outside selected goals, followed by global active-plan access.

Use reviewed mappings from finding code, outcome/measure, factor, and timing to the fixed goal keys. Do not infer goal identity from AI prose. For example, meal/bloating evidence can serve Better Digestion and Fewer, Milder Symptoms; an activity/energy association serves More Energy and remains device-only. Unrelated findings must not be forced into a goal.

Preserve stable goal/catalog ordering. Within a goal, prefer an eligible relationship using evidence adequacy, goal relevance, freshness, and material change. Do not rank solely by log volume, dramatic wording, or a high AI confidence label. Care notices have separate precedence. If several relationships qualify, show one lead and expose the remainder in details.

**Shared relationships:** All Goals displays a relationship once, under its most specific eligible selected goal; use a deterministic mapping priority and catalog order for ties. Every other mapped goal still exposes that same relationship when selected. The detail identifies other related goals. Shared mappings retain one identity, evidence version, and review state. This is deduplication of presentation, not suppression of evidence. The reference shows the meal/bloating finding under Better Digestion in All Goals and under Fewer, Milder Symptoms when that chip is selected.

### Summary-card anatomy

| Region | Content and hierarchy |
| --- | --- |
| Identity | Exact goal label and its icon; stable anchor |
| Status | Possible Connection until assessment is available; evaluated Developing Pattern or Consistent Pattern with a concise reason when supported |
| Signal relationship | Named habit/factor and symptom/outcome linked without a directional arrow; iconography reinforces both endpoints |
| Takeaway | Strongest prose: one factual association, typically one or two lines at default size; never force a line clamp |
| Context | One short sentence naming the time/quality basis or important limitation; no unsupported causal or recurrence claims |
| Footer | **Explore more about [Goal Name]**, divider and chevron; entire card is one action |

**Examples:** “Bloating was logged near dairy-tagged meals.” / “Seen in the past 14 days. Unlogged symptoms could affect this pattern.” And “Energy ratings were higher on days with logged activity.” / “Seen in recent rated days. Missing activity logs can affect the comparison.”

Do not put two weeks of entry counts and the previous two weeks of counts at the center of a relationship card. Counts, scales, and chart denominators remain essential evidence and are visible in details. When no relationship qualifies, a supported meaningful change can lead with **Change Observed**, a specific outcome, and “No clear connection yet” when accurate. Do not manufacture a relationship to fill space. Logging activity alone is not health improvement.

An empty goal uses **Still Gathering Context** and a specific record suggestion without a promise that N more logs will create a finding. Keep its exact goal identity. Larger text expands cards and footers vertically; goal names are never truncated. Device-only text is a non-interactive detail note, never a footer label.

## Goal details and evidence

### Detail order

1. Exact goal, local source, connection status, named signal pair, complete takeaway, and short context.
2. Actual observation window, named comparison groups, values/units, numerator/denominator or rated-day counts, and a common scale where the adapter supplies them.
3. Essential limitations beside that evidence. **How to Read This Pattern** explains timing, eligibility, missing records, and other plausible influences. Extra methodology may expand; limitations cannot be hidden behind a disclosure.
4. **Browse the Supporting Records**, only when structured references or a reproducible, versioned selection identify the actual supporting set. Otherwise use **View Logs From This Period** and state that the broader period is not the exact evidence set.
5. Other mapped goals, additional findings, and secondary direct goal comparisons. Do not repeat the leading finding as another discovery.
6. Optional **Ask About This Pattern**, subject to shareability and consent. More Energy has a local-device note and no finding-specific AI action.
7. An existing related domain plan, or eligible domain-plan preview. A global unrelated plan stays on Today/overview, not under this detail.

### Surfaced evidence adapters and corrected fixtures

Only families actually surfaced need the first adapters. Required fields must come from structured evidence, never generated prose. When an analyzer has only a supported text observation, show it honestly without inventing averages or bars.

| Family | Current reference | Calculation meaning and limitation |
| --- | --- | --- |
| Meal-tag / symptom co-occurrence | Dairy-tagged meals: **3 of 8 (38% rounded)**. Meals without a dairy tag: **3 of 12 (25%)**. Oct 12–25. | Denominators are all eligible tagged/untagged logged meals. Numerators are meals with logged bloating within **four hours before or after**. The first bar uses the exact 37.5%, rounded only in text. No symptom log is unknown, not an observed symptom-free follow-up. |
| Wellbeing / activity association | Average energy **7.2/10** on **7 rated days with logged activity**, versus **5.1/10** on **6 rated days without an activity log**. Oct 12–25. | Same-day rated-day groups; missing energy ratings are excluded, not zero. No activity log is not verified inactivity. No claim about walking, same-night sleep quality, or causal order. Device-only. |

The values are illustrative fixtures shaped to existing analyzer families, not an end-to-end analyzer test. The meal example's 12.5 percentage-point gap does not meet the currently audited 25-point care-gap condition; production always consumes the analyzer's actual urgency. Do not change fixtures to bypass a real notice. The earlier 4-of-6 versus 2-of-12 fixture would require the applicable care treatment and cannot offer an otherwise ineligible plan preview.

Use “near” or “within four hours, before or after” for current bidirectional meal matching. “After” is permitted only after the calculation actually enforces an explicit directional lag, including boundary and overlapping-meal attribution rules. One symptom can be near multiple meals; matched-meal counts are not unique symptom episodes. A meal without a dairy tag is not verified dairy-free.

Bars share a zero baseline. Percentages use 0–100%; energy and sleep quality use the actual **0–10** scale. Include both group labels, units and counts in accessible text. Do not use “Other Recorded Days,” “No Walk Reported,” “Healthy Days,” or “No Symptoms” as unsupported comparator labels. A two-group aggregate cannot be rendered as an invented time series or target ring.

### Evidence identity, recurrence, and maturity

**G1, G2, and G3-lite are required implementation work.** Full scope and deferred work are recorded in [Findings Capabilities](insights-findings-capabilities.md).

A relationship key identifies its signals, outcome, timing/lag and calculation definition, independent of generated wording, current metrics, and refresh time. A separate evidence version records the actual observations, period and method version. Dairy/bloating and dairy/headache are distinct; correcting a source entry updates the evidence version without creating a new relationship identity unless the relationship definition changes.

| Display state | Required basis | UI behavior |
| --- | --- | --- |
| Possible Connection | Eligible analyzer association; no evaluated shared maturity result yet | Neutral link icon and the actual limitation; no implied consistency grade |
| Developing Pattern | Evaluated comparable evidence supports an exploratory association, but a documented coverage/recurrence limitation remains | Status plus short reason, such as a limited comparison period; reason must be supplied by the assessment |
| Consistent Pattern | Documented assessment finds adequate comparable coverage and repeatable direction across distinct periods, with conflicts and staleness accounted for | Status plus concise explanation of the assessed basis; not proof of cause |
| Conflicting / no longer supported | Assessed contradictory, removed, or inadequate evidence | Explain the changed basis; downgrade or withdraw the claim and chart as appropriate |
| Stale | Assessment says evidence is no longer current | Actual dates, clear stale qualifier, and refresh path; never retain an unqualified Consistent Pattern label |

A maturity result includes status, short reason, evaluated criteria version, comparable coverage, assessed distinct periods, consistency, conflicts, and freshness. Define and validate family-appropriate thresholds before enabling labels; this design does not invent a universal number of entries or weeks. Duplicates and overlapping refreshes cannot promote maturity. AI prose and a care-related analyzer `strong` flag cannot assign maturity. Care urgency and evidence maturity remain separate.

G3-lite stores or reproducibly reconstructs the actual distinct periods assessed, their support/contradiction, and evidence versions. Three reruns of the same fortnight are not three independent weeks. A numerical recurrence sentence appears only when those distinct periods support it. The rich per-week panel and general long-horizon evidence warehouse are deferred. Editing/deleting records must invalidate affected assessments and allow downgrades.

### Supporting records and return behavior

Open details by relationship key plus evidence version. Refresh must not silently replace evidence while it is being read; disclose newer evidence. Links to deleted/inaccessible records explain the gap and trigger reassessment. Preserve the originating goal filter, scroll position and disclosures on return. Browsing the overview does not mark all evidence reviewed. AI rewording alone is not a new finding.

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

Only eligible structured findings permitted by the user enter AI context. The presentation does not grant new sharing permission for full diary records, notes, photos, excluded entries, or device-only domains. Energy, mood, stress, and cycle remain excluded, including indirectly through profile goal names, overall summaries, saved items, and suggested questions. More Energy therefore has local relationship and comparison details and a device-only note, but no finding-specific AI action. These rules also apply to deep links and restored navigation state.

## Plans and automatic record tracking

### Plan purpose and placement

Retain the app's **existing domain-based local plans** and care eligibility. G8 relationship-native plans are deferred. A source finding can provide context, but the plan does not automatically become a test of its precise signal pair or share its new recurrence/maturity model.

The reference uses **Two-Week Meal and Symptom Check**, Day 6 of 14: log meals near eating and symptoms with severity when noticed. It follows meal/symptom records, without promising a controlled dairy/bloating test or verified symptom-free days. The previous “Sleep and Activity Check” fixture is superseded. Existing activity, sleep, and check-in domain templates retain their own requirements; do not add a walking/sleep plan for the visual example.

Show the plan globally on Today and the overview, and within a goal only when the existing domain/focus association warrants it. **View Plan** opens the existing plan instance. Preserve its identity and device/cloud exclusions; the new relationship identity is not a claim that legacy plan matching already uses it.

### Preview and start

**Preview a Plan** opens the source finding, domain-specific purpose, observation period, required record details, what the existing template can assess, and important limitations. **Start This Plan** is explicit. Opening evidence, asking a question, or reading a preview never starts a plan. Existing safety/eligibility policy controls whether a new plan may be offered. No action changes medications or treatment preferences.

### Plan detail order

| Order | Content |
| --- | --- |
| 1 | Related goal names, plan title, actual phase/day, question |
| 2 | **Today's Records** and **Tracked Automatically**, or assessment state when the observation period ends |
| 3 | **Source Finding** link using the existing focus snapshot; disclose if exact historical support is unavailable |
| 4 | **What This Plan Follows**: existing template record requirements, supported assessment and limits |
| 5 | **If You Notice Symptoms**: optional contextual logging, never a daily symptom-free task |
| 6 | **Manage This Plan** with full-width Pause/Resume and End buttons |

### Deriving row status

For the example, use the meal/symptom template’s actual qualifying fields: meal details and symptom severity when symptoms are noticed. Symptom logging remains conditional, not a daily completion requirement. A valid entry with missing required fields is partial. Imported entries count only if they meet the same field, validity, and date rules. The UI consumes the plan's explicit qualifying-record rules rather than assuming that any log of that type is enough.

| State | Appearance and meaning | Action |
| --- | --- | --- |
| When Noticed | Conditional symptom row; no qualifying symptom entry and no inference of absence | Optional symptom entry |
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

End of the observation period produces **Ready to Assess**, not automatic success. **Assess the Available Records** evaluates supported records according to the existing domain-plan/analyzer contract. It does not claim a new relationship-native experiment or inherit G2/G3-lite maturity automatically.

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
| Limitations and maturity | Visible material caveats; evaluated status/reason, criteria version, coverage, distinct periods, conflict and freshness; neutral Possible Connection when no assessment exists |
| Care scope and urgency | Rule-derived report/finding association and required wording; independent of filters and dismissals |
| Plan association | Existing stable plan ID and focus snapshot, domain/template, phase, duration, qualifying-record rules and derived status; no new relationship-native plan selection |
| AI sharing eligibility | Domain exclusions, user consent, review snapshot, context scope; enforced beyond the visible button |
| Viewed/saved/hidden | Separate user states; AI rewording alone does not create new evidence |

Implement evidence adapters for the surfaced families first; a universal schema for all analyzers is deferred. Some fields require an adapter or new assessment support beyond the existing `LocalFinding` contract. Unsupported evidence changes the display; do not recover missing values by parsing AI narrative. **Possible Connection** is the neutral association label, not an evaluated maturity grade. Developing Pattern and Consistent Pattern require the assessed contract above. Do not invent high/medium/low badges or confidence percentages.

Saving bookmarks a finding independently of review state. Hiding removes the selected evidence version from routine display and offers restoration; it cannot remove applicable care notices. Stronger recurrence suppression, if exposed by existing controls, must be explicitly labeled and reversible. Materially changed evidence may reappear after ordinary hiding, but not merely because an AI sentence changed. Feedback distinguishes usefulness, accuracy, and safety concerns without rewriting evidence or clinical rules.

## State matrix

| State | Required visible behavior | Available path |
| --- | --- | --- |
| Local analysis loading | Stable pending content; retain last-successful data with its date when appropriate | Logging remains available |
| Early or insufficient records | Still Gathering Context; identify the relevant data gap without an arbitrary entry-count promise | Open that goal and relevant records |
| Complete analysis with no eligible findings | Explain that no supported finding is available for the window; distinguish from failure and not-yet-analyzed | Existing history/logging |
| No new findings | You're Up to Date on Today; existing goal results remain on Insights | See All Insights |
| Goal has a supported relationship but no progress comparison | Lead with the relationship; do not make the absent secondary comparison the headline | Relationship details |
| No clear connection | Explicit absence of a supported connection; retain a valid direct comparison | Compare records |
| AI review off | Compact preferences route; local summaries and plans unaffected | AI Preferences |
| AI unavailable/offline | Preserve local facts and separately dated prior review if available | Explicit retry; retain draft |
| Earlier AI snapshot | Newer Records Are Available before the old review; retain original timestamp and evidence scope | Current local findings |
| Local analysis failed | Failure state distinct from empty/healthy; dated last-successful results may remain | Retry |
| Stale evidence | Actual period and original date, assessed stale state; no unqualified Consistent Pattern badge | Refresh permitted analysis |
| Conflicting / withdrawn support | Explain the changed evidence and downgrade or withdraw the relationship; never promote it by entry count | Current evidence and records |
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
| Goal identity | 32 × 32 tinted backing, 9 radius; 21-unit outline icon; retain stomach silhouette and optical balance |
| Goal header | Icon/label gap 9; label 15/21, weight 500; status 11/16 with a 12-unit icon |
| Summary takeaway | 18/25, weight 500; relationship band precedes it; context 13/19 with 5 above; no fixed line count |
| Signal relationship | Unbordered tinted band, 8 radius, 7 vertical / 9 horizontal padding; 17-unit icons, 12-unit labels; thin non-directional link |
| Body / metadata | 14/22.4 regular / 12/18 regular; material limitations may use 13/20.8 |
| Detail takeaway / evidence value | 20/27 medium / 22 medium; use these to prioritize evidence, not every card heading |
| Summary footer | 1-unit separator; 8 top gap, 8 top padding; 12/18 text and trailing chevron |
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

Reuse existing native tokens/adapters for shared shell, controls, text, attention, and semantic AI foregrounds. Goal/relationship backing, AI soft backing, and the restrained internal divider now resolve through the shared `component.iconBacking`, `component.aiBacking`, and `component.quietDivider` registry in `assets/tokens/color.tokens.json`. Use the generated CSS or theme-specific Flutter component exports; the registration preserves the approved shades. Previous-period evidence marks use existing slate/border values. Consuming-app adoption is still pending; do not scatter literal colors across widgets. Decorative outlines do not substitute for required control boundaries. Purple indicates AI meaning, not the whole Insights feature. Selection, record completeness, and care urgency each retain a text/icon cue.

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
| IP-03 | Every goal summary uses Explore more about [Goal Name], wraps safely, and opens goal details; its chip filters the overview in place |
| IP-04 | More Energy's device-only statement is non-interactive detail context; it is never a footer link or shared AI context |
| IP-05 | All Goals preserves meaningful goal order, gathering-context access, Other Findings, and global plan access without duplicating evidence identity |
| IP-06 | Eligible relationships lead over period comparisons; details show exact values, units, groups, windows, and counts; missing evidence stays unknown |
| IP-07 | Activity/energy evidence maps to More Energy and stays device-only; unsupported walking/sleep examples and relationship-native plans are absent |
| IP-08 | Meal evidence uses honest ±4-hour timing and logged-meal denominators; energy uses rated days and /10; bars share a scale and never imply verified absence |
| IP-09 | Goal/connection/source-record routes preserve stable IDs, evidence versions, originating filters, scroll, and expanded disclosures |
| IP-10 | AI review exposes up to three linked takeaways, fuller explanation, context scope, and independent review time; earlier reviews are clearly stale |
| IP-11 | Suggested questions open editable drafts; Send is explicit; context is visible, consent enforced, exclusions maintained, drafts survive failure |
| IP-12 | Automatic plan statuses update after save/edit/delete/import/day rollover; no manual checkmark completion and no symptom absence inferred from silence |
| IP-13 | Pause/Resume and End are visibly framed buttons in both themes; End requires confirmation, keeps logs, and cannot imply assessment success |
| IP-14 | Ready to Assess, insufficient comparison, pattern present/not detected, paused, and ended states are distinct and data-driven |
| IP-15 | Required care context survives selection, hiding, AI-off/unavailable, stale, and empty states; original urgency and scope remain intact |
| IP-16 | Light/dark match the approved backdrop, card geometry, hierarchy, and exact icons; values and behavior are identical across themes |
| IP-17 | Test 320-unit width and enlarged text, long fixed goal labels, footer wrapping, keyboard focus, VoiceOver/TalkBack, modal dismissal, and safe-area clearance |
| IP-19 | Maturity has evaluated criteria and a visible reason; duplicate logs, overlapping windows, AI wording and care flags cannot promote it |
| IP-20 | Stable relationship keys and separate evidence versions support distinct-period recurrence; changes/deletions can downgrade evidence; no fabricated weekly repetition |
| IP-21 | Only surfaced families require initial evidence adapters; sparse observations omit unsupported charts and exact-record actions |
| IP-22 | Plans retain existing domain templates, eligibility and conditional symptom logging; deferred capabilities are not implied by copy or screenshot fixtures |
| IP-18 | Native implementation replaces simulated reference records, clocks, AI responses, and assessment outcomes with actual data; browser references alone are not release evidence |

## Integration and migration

Implement G1 goal mappings and relationship-first lead selection; then G2 evaluated maturity and G3-lite stable identity/distinct-period recurrence. Add G7 evidence adapters for the surfaced families with G5 honest timing and G6 unknown/denominator disclosure. Neutral Possible Connection supports the first presentation slice; evaluated labels must remain disabled until their criteria are implemented and validated. The [capability scope](insights-findings-capabilities.md) is controlling for deferred work.

Reuse the app's fixed goals, native icons, stomach asset, logging, Timeline, Charts, rewards, consent, care and analysis services. Existing local plans retain their templates and eligibility. Native implementation must resolve evidence snapshots, record routing, saved/hidden state, timezone/aggregation rules, plan persistence, cloud exclusions, and accessibility. This documentation does not implement those services.

The default [reference gallery](../../assets/app/insights-presentation/index.html) now shows the scoped connection-led direction. Editable source is in `tooling/insights-connections-reference/`; `tooling/build-insights-connections-reference.py` builds assets and `tooling/package-insights-connections-reference.py` validates captures and updates the gallery. The earlier comparison-first and Flutter galleries are historical; their hierarchy and numerical examples do not override this specification.

Controlling references: [Insights and Correlations](insights-and-correlations.md), [App Visual Specification](../02-design/app-visuals.md), [Progress and Disclosure](../02-design/progress-and-disclosure.md), [Insight Types](../05-ai/insight-types.md), [Confidence and Evidence](../05-ai/confidence-and-evidence.md), and [Hybrid Local Findings](../../adr/0010-hybrid-local-findings-optional-llm.md).

## Version History

- 2026-10-27 (approved connection-led amendment): Incorporates G1–G3-lite, honest timing/coverage, surfaced-family adapters and deferred analyzer/plan scope. Replaces count-first summaries and unsupported fixtures with paired connection-led references; approved for publication after local review.

- 2026-10-27: Integrates the approved refined journey, fixed goal catalog/icons, consistent goal-specific footers, automatic plan tracking, outlined plan management, brief AI review and contextual chat. Adds 38 high-fidelity app-only references, detailed display/state/interaction contracts, and implementation acceptance criteria. Approved for publication after local review.
- 2026-10-25: Earlier overview/detail and filter experiments, including Flutter captures. Retained as historical references and superseded by the October 27 design.
