# Insights Presentation

Status: Today overview design and detailed documentation approved November 5; publication and native implementation pending

Owner: Product, Design System, and AI Working Groups

Version: Unreleased

Last updated: 2026-11-05

Decision: [ADR-0019](../../adr/0019-adopt-today-insights-overview.md) / [RFC-0013](../../rfc/0013-today-insights-overview.md) amend Today and finding review state; [ADR-0017](../../adr/0017-adopt-goal-led-insights-presentation.md) / [RFC-0011](../../rfc/0011-goal-led-insights-presentation.md) retain the broader Insights journey.

## Purpose and authority

Make findings easy to scan, understand, and act on. **Today** answers “do I need to dive into anything, and what would I be opening?” **Insights** answers “what connections are appearing between my habits, symptoms, and wellbeing?” Today uses one compact card with a row for every selected, available fixed goal. Insights retains relationship-led summaries and complete evidence in the drilldown.

The November 5 amendment replaces the single Today finding and its plan-first order. It adds distinct unread, reviewed, updated, and no-finding states. It does not redesign the Insights landing page, change care rules, broaden cloud sharing, or introduce new analyzers or relationship-native plans. Fixed goal filters, the stomach icon, automatic plan statuses, outlined plan buttons, and **Explore more about [Goal Name]** footers on Insights remain part of the design.

The [capability audit](insights-findings-capabilities.md#november-5-source-audit-and-today-contracts) distinguishes current local app source from remaining work. Goal mapping, relationship-first selection, assessed maturity and evidence identity now have source support. Per-finding review persistence, meaningful-update classification, and trustworthy goal-level no-finding states still require implementation/verification. Screenshots are illustrative design fixtures, not proof of analysis output or shipping behavior.

Sustained logging can improve the chance of identifying useful connections and understanding how consistently they appear. It never guarantees a finding, a symptom-free conclusion, or proof of causation. The [consistency review](insights-presentation-review.md) separates this amendment from historical checks. The design and detailed documentation are approved after local review. Publication and native implementation remain separate.

## Production intent screen references

[Open the full-resolution reference gallery](../../assets/app/insights-presentation/index.html){ .md-button }

**November 5 Today package:** 14 app-only JPEGs, seven scenes in both themes, rendered directly at **393 × 852 logical units / 1179 × 2556 pixels**. These reproduce the approved design, including the exact woven artwork, opaque reading surfaces, actual goal names, stomach icon and strong unread treatment. They are original browser screenshot bytes, without thumbnail enlargement or resampling.

These are high-fidelity **browser-rendered design references**, not shipping Flutter screenshots or analyzer-verified personal records. Status bars, dates, findings and plan states are illustrative. No chat transcript, browser chrome or review-page caption is embedded in the app images. Content scrolls naturally; one screenshot does not require the entire Today page to fit a viewport. The navigation-focused finding examples supplement, rather than replace, the complete evidence, limitations and attribution requirements below. Their “Explore the evidence” disclosure is not permission to hide material limitations in production.

[Today capture manifest](../../assets/app/insights-presentation/today-overview-2026-11-05/references.json) · [Inspectable light reference](../../assets/app/insights-presentation/today-overview-2026-11-05/reference.html?scene=today-new&theme=light&scale=1) · [Inspectable dark reference](../../assets/app/insights-presentation/today-overview-2026-11-05/reference.html?scene=today-new&theme=dark&scale=1)

<!-- TODAY_OVERVIEW_GALLERY_START -->
### Today · Unread and Goal States

All eight selected goals; four distinct unread findings, two shared across goals. Known missing input, no clear pattern, and gathering context remain distinct.

| Light | Dark |
| --- | --- |
| [![Today · Unread and Goal States — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-new-light.jpg?v=0df0abe5ce61){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-new-light.jpg?v=0df0abe5ce61) | [![Today · Unread and Goal States — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-new-dark.jpg?v=6c69cfd76160){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-new-dark.jpg?v=6c69cfd76160) |

### Today · One Finding Reviewed

Dairy/bloating is reviewed. The total drops from four to three once; the other finding remains unread under every related goal.

| Light | Dark |
| --- | --- |
| [![Today · One Finding Reviewed — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-partial-light.jpg?v=c581c500b7da){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-partial-light.jpg?v=c581c500b7da) | [![Today · One Finding Reviewed — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-partial-dark.jpg?v=c9ef505f9499){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-partial-dark.jpg?v=c9ef505f9499) |

### Today · All Findings Reviewed

Useful previews remain after review. The three no-finding states do not change when unrelated findings are read.

| Light | Dark |
| --- | --- |
| [![Today · All Findings Reviewed — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-reviewed-light.jpg?v=6b08d0650346){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-reviewed-light.jpg?v=6b08d0650346) | [![Today · All Findings Reviewed — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-reviewed-dark.jpg?v=f894db941bfd){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/today-reviewed-dark.jpg?v=f894db941bfd) |

### Goal · Two Unread Findings

Opening a goal with multiple findings does not review them. The list exposes each actual finding.

| Light | Dark |
| --- | --- |
| [![Goal · Two Unread Findings — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-unread-light.jpg?v=87d0d2e68e2d){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-unread-light.jpg?v=87d0d2e68e2d) | [![Goal · Two Unread Findings — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-unread-dark.jpg?v=d88e189faad9){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-unread-dark.jpg?v=d88e189faad9) |

### Goal · One Finding Still Unread

Only the opened dairy/bloating finding is reviewed. Activity/bowel remains unread and is prioritized in the list.

| Light | Dark |
| --- | --- |
| [![Goal · One Finding Still Unread — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-partial-light.jpg?v=1ec1d46c42e7){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-partial-light.jpg?v=1ec1d46c42e7) | [![Goal · One Finding Still Unread — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-partial-dark.jpg?v=108165ede389){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/goal-partial-dark.jpg?v=108165ede389) |

### Unread Insights · Distinct Findings

One row per unread finding with its related goals. Opening this list does not mark anything reviewed.

| Light | Dark |
| --- | --- |
| [![Unread Insights · Distinct Findings — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/unread-list-light.jpg?v=31abd9419a24){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/unread-list-light.jpg?v=31abd9419a24) | [![Unread Insights · Distinct Findings — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/unread-list-dark.jpg?v=824c428ea1cd){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/unread-list-dark.jpg?v=824c428ea1cd) |

### Finding · What Changed

A meaningful update explains the changed evidence. This focused navigation reference supplements the full evidence-detail requirements.

| Light | Dark |
| --- | --- |
| [![Finding · What Changed — light](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/updated-finding-light.jpg?v=cae55a297af3){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/updated-finding-light.jpg?v=cae55a297af3) | [![Finding · What Changed — dark](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/updated-finding-dark.jpg?v=aac790611918){ width="280" loading="lazy" }](../../assets/app/insights-presentation/today-overview-2026-11-05/screens/updated-finding-dark.jpg?v=aac790611918) |

<!-- TODAY_OVERVIEW_GALLERY_END -->

### Retained Insights and evidence references — October 27

The five pairs below retain the approved relationship-first Insights hierarchy, evidence and plan management. Their older labels **Fewer, Milder Symptoms**, **Better Digestion**, and **Better Sleep** are historical; use the current catalog table below in implementation. Their generic gathering example applies only when context is insufficient, not every empty result. The November 5 goal-state rules and Today package take precedence where they differ.

<!-- CONNECTIONS_GALLERY_START -->
#### Insights Overview

Potential habit/outcome links lead; fixed goals filter the overview. Counts and comparisons are in details.

| Light | Dark |
| --- | --- |
| [![Insights Overview — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-light.jpg?v=15070eee405d){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-light.jpg?v=15070eee405d) | [![Insights Overview — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-dark.jpg?v=fcbc5b016708){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/insights-dark.jpg?v=fcbc5b016708) |

#### Better Digestion · Evidence

Logged meal/bloating co-occurrence with honest bidirectional timing, denominators and missing-observation limits.

| Light | Dark |
| --- | --- |
| [![Better Digestion · Evidence — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-light.jpg?v=473e515da51c){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-light.jpg?v=473e515da51c) | [![Better Digestion · Evidence — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-dark.jpg?v=1754b34c0816){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/details-dark.jpg?v=1754b34c0816) |

#### More Energy · Evidence

Same-day activity/energy averages on the actual /10 scale, with rated-day counts. Device-only; no AI follow-up.

| Light | Dark |
| --- | --- |
| [![More Energy · Evidence — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-light.jpg?v=90c8b16f9faf){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-light.jpg?v=90c8b16f9faf) | [![More Energy · Evidence — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-dark.jpg?v=f5a2d6e9ae36){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/energy-dark.jpg?v=f5a2d6e9ae36) |

#### Still Gathering Context

The selected fixed goal has no eligible relationship yet. No promise that additional logs guarantee one.

| Light | Dark |
| --- | --- |
| [![Still Gathering Context — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-light.jpg?v=500dca845dec){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-light.jpg?v=500dca845dec) | [![Still Gathering Context — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-dark.jpg?v=a54c259d392b){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/gathering-dark.jpg?v=a54c259d392b) |

#### Domain Plan · Management

Current meal/symptom plan, conditional symptom logging, automatic status, and outlined Pause/End controls.

| Light | Dark |
| --- | --- |
| [![Domain Plan · Management — light](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-light.jpg?v=3f9b63d780e3){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-light.jpg?v=3f9b63d780e3) | [![Domain Plan · Management — dark](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-dark.jpg?v=6743feffda87){ width="280" loading="lazy" }](../../assets/app/insights-presentation/connections-first-2026-10-27/screens/plan-dark.jpg?v=6743feffda87) |

<!-- CONNECTIONS_GALLERY_END -->

The [October 27 connection-led gallery](../../assets/app/insights-presentation/connections-first-gallery-2026-10-27.html) retains all 12 original captures, including the superseded single-finding Today screen. The [earlier comparison-first gallery](../../assets/app/insights-presentation/previous-goal-comparison-gallery.html) is also historical. Neither overrides the current Today hierarchy, goal labels, review behavior, capability scope or written requirements for states not pictured.

## Information architecture

| Surface | User question | Content order |
| --- | --- | --- |
| Today | What is useful today? | Applicable care notice, compact Insights card covering every selected goal, relevant plan, existing progress/logging content |
| Insights overview | What links are appearing for my goals? | Care context, Filter Insights and freshness, connection-led summaries, gathering-context goals, optional eligible AI entry, Other Findings, active plan |
| Goal finding list from Today | Which finding should I open? | Distinct eligible findings for that goal; unread first; no review state changes on list entry |
| Goal details | What supports this finding? | Leading relationship and short context, actual evidence and limitations, supporting records, secondary findings and period comparisons, permitted follow-up |
| Additional finding details | What supports another result? | Same evidence anatomy, with a distinct stable relationship identity and evidence version |
| AI Review / chat | What questions could I explore? | Independently attributed, eligible context and optional explanation; never needed to read local evidence |
| Plan | What records does this plan follow? | Existing domain-based local plan, automatic record status, scope, management, supported assessment |

An Insights overview summary opens its leading finding directly. A Today goal row with exactly one eligible finding also opens that finding; a row with multiple findings opens the goal finding list so the user can choose. The list is a deliberate selection step, not a reviewed finding. Each selected finding then exposes its evidence directly. Optional AI prose does not displace local findings.

### Navigation and return behavior

- Preserve the current five app tabs: **Today, Timeline, Charts, Chat, Insights**. Use the existing routes; this design does not reinstate the older four-tab shell.
- Preserve the app's Material navigation icons and their selected variants. Keep the existing **Preferences** gear on Today and Insights, with its protected ink backing. The new **Insights Options** overflow is a separate action for saved/hidden findings and related options; it does not replace Preferences. Prototype handoffs do not implement the existing Preferences screen.
- Selecting a goal chip filters the overview in place; it does not open a detail page. Selecting the summary (including its footer) opens that goal’s leading finding and detail. Preserve selected goal, relationship identity, and evidence version through navigation.
- The whole summary card is one accessible action. Its footer describes that action; do not nest a separate competing link inside the card.
- Returning from evidence, plan, or contextual chat restores the originating goal, scroll offset, and expanded disclosures. Returning to All Goals restores the originating card position when navigation came from that list.
- The chosen goal persists during refresh. If it loses findings, keep the selection and explain the data gap. If the goal is no longer saved/available, return to All Goals and explain the change without inventing a replacement goal.
- Successfully opening an actual finding marks only its displayed meaningful revision reviewed; raw evidence refreshes are separate. Browsing Today, All Goals, a goal list, the unread list, or a status explanation marks nothing reviewed. Review state is independent of rewards, saved state, hidden state, and plan progress.
- Theme changes preserve selection, scroll position, disclosures, draft questions, and plan state. They do not rerun analysis or change numbers.

## Fixed goals and Filter Insights

### Selection contract

**Filter Insights** is one horizontally scrolling, single-select row: **All Goals**, followed by the profile's saved and available goals from the app's fixed catalog. There is no custom-goal text entry, generic outcome substitution, More Filters button, log-type row, or filter sheet in this approved design. Supporting log types belong to evidence and Timeline destinations.

Use each exact catalog label in Capital Case, including punctuation and the lowercase **a** in **See If a Treatment Is Working**. Do not apply automatic title casing or derive identity from visible text. Profile selection determines which fixed labels appear; it does not supply arbitrary wording. **Reduce Symptoms** is always included by the current app profile contract. An uninitialized/invalid goal selection still leaves All Goals usable.

Selection updates immediately, with a check and an accessible selected state. Keep the full label; let the row scroll rather than abbreviating it or opening another step. Reveal the selected chip when needed. At larger text sizes, the row remains horizontally scrollable, while content below reflows vertically. A result count, if announced, counts distinct displayed relationships, not duplicate goal mappings. Changes and gathering-context states are not counted as new relationships.

The filter panel includes **Rule-Derived · On Your Device** as a shared source label for the local comparisons and connections below. The separately labeled AI entry opens an independently attributed review. Today uses compact New/Updated/unread cues, which describe review status, not AI authorship. Its findings are local rule-derived results; AI narrative is not a Today row. Connection detail includes **Rule-Derived · On Your Device**, a separate **Possible Connection** or evaluated maturity label, and its actual observation period. Source attribution must remain visible without forcing every summary to repeat a large badge.

### Goal labels and icons

Verified against `HealthGoal` in the consuming app's `lib/models/onboarding_options.dart` on November 5 (local source `9e4fb3d`). This table maps stable production keys to the approved visual meaning; reference-library names are not a requirement to add a second icon runtime to the native app.

| Production key | Exact label | Approved icon metaphor / reference |
| --- | --- | --- |
| `resolveSymptoms` | Reduce Symptoms | Decreasing symptom trend · `trending-down` |
| `betterDigestion` | Improved Digestion | **Stomach outline** · supplied Health Icons asset; never meal cutlery |
| `betterSleep` | Improved Sleep | Bed · `bed` |
| `beMoreActive` | Be More Active | Footsteps · `footprints` |
| `improveBloodPressure` | Improve Blood Pressure | Heart/pulse · `heart-pulse` |
| `medicationConsistency` | Take Medications Consistently | Pill · `pill` |
| `seeTreatmentWorking` | See If a Treatment Is Working | Assessment clipboard · `clipboard-check` |
| `understandCycle` | Understand My Cycle | Calendar · `calendar-days` |
| `moreEnergy` | More Energy | Energy bolt · `zap` |
| `betterMood` | Improved Mood | Face · `smile` |
| `lessStress` | Less Stress | Breath/wind · `wind` |

Reuse the same goal icon and label in its summary, selected view, gathering-context row, and Today finding. Goal icons convey identity, not measured success, diagnosis, adherence, or current mood. The stomach silhouette is the approved exception to the otherwise consistent outline family. Keep its supplied geometry and optical weight.

Cycle availability follows `HealthGoal.availableFor`; this presentation does not broaden it. Cycle, energy, mood, and stress remain device-only, including exclusion of their goal names from cloud profile context. The eleven-goal reference catalog is not an all-selected user profile.

## Today insight region

### Order, purpose and density

1. **Applicable care notice.** Required urgency, wording and scope remain first and independent of review state.
2. **Insights.** One opaque reading card containing all selected, available goals in stable catalog order. It is the principal glanceable element on Today.
3. **Your Plan**, when relevant, followed by existing progress and logging content. Preserve real plan, reminder, reward and logging behavior; do not invent a health score or remove unrelated features because a cropped reference does not show them.

Each goal gets a section in the single card, not its own full summary card. Keep the goal icon, exact goal name, one brief useful preview or honest status, optional unread badge, and trailing chevron. Aim for one line of preview at default size; allow full wrapping at narrow widths and larger text. Do not clamp the goal label, preview or action. Avoid charts, log-count comparisons, evidence paragraphs, AI narrative and a filter strip here. Detailed evidence belongs in Insights.

The approved example shows eight selected goals, not eight mandatory goals or a maximum. Render the actual profile's available selection, including any goal required by the profile contract. Never silently drop a goal because it has no finding or move unread goals to the top; stable position helps people see that every goal remains accounted for. With more selected goals, the Today page grows and scrolls normally.

### Card anatomy and destinations

| Region / state | Visible content | Action |
| --- | --- | --- |
| Header | Insights icon and **Insights**; **4 Unread** in the example | Unread pill opens the deduplicated unread finding list |
| No unread, existing eligible findings | Quiet **All reviewed** status | Status is not a button; goal rows and footer remain available |
| Goal with one eligible finding | Icon, exact goal label, concise relationship preview; New/Updated when unread | Open that actual finding |
| Goal with multiple eligible findings | Same compact row; show one relevant unread preview first, else a relevant reviewed preview | Open the goal's finding list, even if only one of its findings remains unread |
| Goal without an eligible finding | Goal identity plus the truthful state defined below | Open that goal's status explanation and an appropriate next step |
| Footer | **Explore Insights** with trailing arrow | Open the existing Insights overview with All Goals; mark nothing reviewed |

The goal row is one accessible button. Its badge and chevron are not separate tap targets. The header unread pill is a separate button. The whole parent card is not a competing action. Preserve origin, scroll position, selected goal and evidence identity on return. From the global unread list, show each distinct finding once and list its related selected goals so the user knows what it concerns.

### Selecting the brief preview

Use existing eligible, non-hidden local findings and reviewed many-to-many goal mappings. Within a goal, show an unread finding ahead of reviewed findings, then use supported relevance, adequacy and freshness with a stable tie-break. A later routine render must not randomly change the preview. Use a concise structured association naming the relevant habit/outcome, such as **Possible dairy–bloating link** or **Higher energy on active days**. Avoid opaque claims such as “Something changed.” A brief preview is not an instruction to change treatment or a causal conclusion.

A supported meaningful outcome change may be used when no relationship qualifies; it must name the actual outcome and cannot turn log totals into health improvement. Maturity, missing-data limits and full time/context basis are shown in the actual finding. If a safe brief preview cannot preserve a material qualification, use a qualified preview and allow wrapping. Care context always remains visible outside optional disclosures.

### Unread, new and updated

| Cue | Exact meaning |
| --- | --- |
| **New** | One unread finding in this goal, and its relationship has never been reviewed |
| **Updated** | One unread finding in this goal whose previously reviewed relationship has a meaningful new revision |
| **2 Unread** (or actual number) | More than one distinct unread finding mapped to this goal; may mix new and updated |
| Header **4 Unread** (or actual number) | Unique unread relationship identities in the currently eligible, selected-goal result set; shared mappings count once |
| **All reviewed** | Eligible findings exist and all their current meaningful revisions have been reviewed; does not mean every goal has a finding or that health is normal |
| No unread badge or emphasis on a row | Current findings for that goal are reviewed, or it has a no-finding state; useful preview/status remains |

Do not show “0 Unread.” If no eligible findings exist at all, omit the header review status and keep each goal's truthful state. Pending/failed analysis must not create **All reviewed** from an empty result. Findings only in Other Findings remain reachable in Insights and do not inflate this selected-goal dashboard count. Ordinary hiding follows the existing restoration policy; it is not review, and it never dismisses care context.

**Review event:** after the actual finding's current content successfully appears, record its displayed meaningful revision as reviewed. No dwell timer, scroll-to-end requirement or explicit acknowledgement is required. Opening Today, Insights, a goal list, an unread list, a status explanation, or an inaccessible/failed finding does not count. Only the opened finding changes; other findings in that goal stay unread. A shared finding has one review state across all mapped goals and entry routes.

Persist the relationship/revision review state on the device across app restarts. Theme changes, filtering, sorting and reselecting a goal do not reset it. Review, saved, hidden, reward and plan states remain independent. This design does not authorize sending review metadata or excluded wellbeing findings to a cloud service. Preserve current account/data deletion behavior.

### Meaningful revision versus evidence refresh

A stable relationship key, raw evidence version, and meaningful review revision have different purposes. **Do not use every change to `evidenceVersion` as an unread update.** Counts, raw metrics and report hashes can change without changing what the user needs to know.

A meaningful revision requires a supported change to the relationship's interpretation, direction, evaluated maturity/coverage, material limitation, or supported next step. A weakening or withdrawn result can be meaningful too; describe that change rather than continuing an unsupported claim. Mere rewording, AI regeneration, formatting, a refreshed timestamp or inconsequential extra records cannot make a finding unread. Family-specific assessment policy determines materiality; the UI must not invent thresholds.

An updated finding includes a concise **What changed** explanation tied to the prior reviewed revision and current evidence. In the illustrative energy example, earlier mixed records now support a more consistent relationship. This sentence is a fixture, not evidence that a particular user's records meet the criteria. Never use Updated without being able to explain the substantive change. If the relationship has never been reviewed, retain **New** even if its raw evidence has refreshed.

Keep the detail snapshot stable while it is being read. Mark only the successfully displayed revision reviewed. If a newer meaningful revision arrives during viewing, disclose newer evidence and leave that newer revision unread until opened; do not silently acknowledge it. Multiple intermediate changes resolve to the latest eligible revision, with an accurate explanation relative to the user's last reviewed basis.

### Distinct states when no finding is available

| Row preview | Required basis | Detail and next step |
| --- | --- | --- |
| **No clear pattern yet** | Analysis completed successfully for this goal/window with adequate relevant coverage, but no supported connection was detected | Explain the assessed period and absence of a supported pattern; allow review of relevant records. It is not a healthy/normal result. |
| **Add symptom logs** (example of a specific request) | A structured assessment identifies symptom observations as a material missing input | Explain why that input matters and link to the existing log flow; symptoms are logged when noticed. Missing logs do not prove no symptoms. Use the actual missing input, not this text for every goal. |
| **Gathering context** | Relevant context is not yet sufficient, and a precise actionable gap is not established | Explain that more relevant context is needed; keep logging available without a guaranteed number of days or entries |

These are different product states, not alternative wording for an empty array. No eligible finding, a generic `gatheringHint`, and an analysis failure cannot establish adequate coverage. A static suggestion must not become a factual claim that a particular input is missing. When several confirmed gaps exist, show the most useful brief request and explain the rest in details. Do not invent an absence log or promise a pattern after N records.

Loading, never-analyzed, stale and failed analysis retain distinct existing states. Preserve clearly dated last-successful findings where appropriate; otherwise show a pending/failure explanation with retry. Do not mislabel these as No clear pattern yet, All reviewed, or symptom-free. Deleted/inaccessible evidence must be reassessed before retaining a claim. Applicable care notices remain visible throughout.

### Required transitions in the reference

| Step | Header and affected goal rows | What remains unchanged |
| --- | --- | --- |
| Initial fixture | **4 Unread**; Reduce Symptoms and Improved Digestion each show **2 Unread**; activity/sleep show New; energy shows Updated | Eight goals stay in stable order |
| Open a two-finding goal | The goal list shows two actual findings; unread remains four globally | No finding is marked reviewed by list entry |
| Open dairy/bloating, then return | Total becomes **3 Unread** once; both shared goals show the remaining activity/bowel preview with **New** | Activity/bowel, sleep and energy stay unread |
| Open global unread list | Three distinct remaining findings, with their related goals | Opening the list reviews none |
| Open each remaining finding | Total decreases once per distinct finding; related rows update together | The three no-finding goal states do not change |
| All eligible findings reviewed | **All reviewed**; ordinary row surfaces and useful previews remain | Goals are not removed, and no-finding statuses do not become successful health outcomes |

### Compact plan context

The reference's **Your Plan / Two-Week Activity Check / Day 6 of 14** is surrounding illustrative context using an existing domain plan. It does not introduce paired-signal planning or certify the plan's eligibility. Open the existing plan from its summary. If automatic record rows are shown, they are status icons/text, **not editable checkboxes**; **Tracked from your logs** explains their origin. A check means the required record information exists, never that health improved. Conditional symptoms remain **When Noticed**. The detailed plan contract below retains its authority.

### Today-specific geometry and color roles

These scoped values reproduce the approved compact card and take precedence over the full Insights summary-card anatomy only in this component. Use native layout and semantic controls; do not copy the preview's fixed phone height or minimum detail-panel height into production.

| Element | Approved reference |
| --- | --- |
| Outer card | Existing opaque surface and 14 radius; 12-unit page gutters and section gap; full-width rows within one card |
| Header | 14-unit inset; 19/25.65 semibold title; 23-unit Insights icon; unread pill with icon, semibold label and native minimum tap area |
| Goal row | 56-unit minimum at default text size; 8 vertical / 14 horizontal inset; 32-unit icon slot, 10 gap; content expands with text |
| Goal label / preview | Inter 14/19.6 semibold / 12.5/18.125 regular; one brief preview without forced truncation |
| New/Updated/count badge | Inter 11/15.4 semibold; 2 vertical / 7 horizontal padding; 6 radius; separate from the wrapping goal label |
| Unread marker | 4-unit inset leading accent; visible in addition to fill and text badge |
| Ordinary separator / footer | Existing quiet divider; 46-unit reference footer with 13-unit semibold Explore Insights and arrow |
| Icons | Existing Material shell; consistent outline goal icons and approved stomach asset; no emoji substitutes |

[Scoped unread role aliases](../../assets/app/insights-presentation/today-overview-2026-11-05/component-colors.json) reuse existing registered colors; they add no foundation palette values. Map these roles through a shared native component adapter, not independent widget literals. Semibold goal labels and these inverted unread roles are approved Today-specific additions, not global card restyling.

| Role | Light | Dark |
| --- | --- | --- |
| Unread background | Jade `#76B7A5` | Existing deep green `#264C4B` |
| Unread body/goal text | Ink `#192D38` | Ivory `#FAF8F4` |
| Leading marker | Deep green `#264C4B` | Jade `#76B7A5` |
| Goal icon / chevron | Deep green `#264C4B` | Existing light link green `#8DC7B7` |
| New/Updated/count badge background | Deep green `#264C4B` | Jade `#76B7A5` |
| Badge text | Ivory `#FAF8F4` | Ink `#192D38` |

Light text on the unread fill measures **6.17:1**; its icon/marker measures **4.10:1**; badge text measures **8.93:1**. Dark unread text measures **8.93:1**, icons **4.95:1**, marker **4.10:1**, and badge text **6.17:1**. [Ten component contrast checks](../../assets/app/insights-presentation/today-overview-2026-11-05/contrast-checks.json) cover those resolved roles. The ordinary light link green `#206668` must not replace the approved deep green on the Jade unread fill: its approximately 2.87:1 contrast is insufficient for these essential marks. Ordinary non-unread rows keep their existing text/link roles.

Color does not carry review meaning alone. Accessible row names include exact goal, New/Updated/unread count when present, preview and destination. Announce count changes concisely after return without re-reading the screen. Enlarge row height and wrap text at accessibility sizes; maintain 44 pt iOS / 48 dp Android target minima, visible focus, logical reading order and capture-action clearance. The screenshot and contrast checks do not certify native screen-reader or large-text behavior.

## Insights overview

### All Goals order and selection

1. Required care context, independently of filter or AI state.
2. **Filter Insights**, actual successful local analysis timestamp, and **Rule-Derived · On Your Device**.
3. Connection-led summaries. Prefer eligible relationships over simple progress comparisons, even when a direct goal comparison is available.
4. Honest goal states: distinguish inadequate context, a known missing input, and an adequately assessed window with no clear pattern. Do not label every empty result Still Gathering Context.
5. **A Closer Look With AI**, when available and scoped to eligible findings. It follows local findings and does not summarize excluded wellbeing goals.
6. **Other Findings** for useful results outside selected goals, followed by global active-plan access.

Use reviewed mappings from finding code, outcome/measure, factor, and timing to the fixed goal keys. Do not infer goal identity from AI prose. For example, meal/bloating evidence can serve Improved Digestion and Reduce Symptoms; an activity/energy association serves More Energy and remains device-only. Unrelated findings must not be forced into a goal.

Preserve stable goal/catalog ordering. Within a goal, prefer an eligible relationship using evidence adequacy, goal relevance, freshness, and material change. Do not rank solely by log volume, dramatic wording, or a high AI confidence label. Care notices have separate precedence. If several relationships qualify, show one lead and expose the remainder in details.

**Shared relationships:** All Goals displays a relationship once, under its most specific eligible selected goal; use a deterministic mapping priority and catalog order for ties. Every other mapped goal still exposes that same relationship when selected. The detail identifies other related goals. Shared mappings retain one identity, evidence version, and review state. This is deduplication of presentation, not suppression of evidence. The October 27 reference demonstrates this with its historical goal labels; use the current catalog names. Today deliberately repeats the short preview under each related selected goal to keep every goal visible, while counting and reviewing that relationship once.

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

An empty goal uses the assessed no-finding state defined above; **Still Gathering Context** in the retained October 27 example applies only to insufficient context. A specific record request requires a known missing input, without a promise that N more logs will create a finding. Keep its exact goal identity. Larger text expands cards and footers vertically; goal names are never truncated. Device-only text is a non-interactive detail note, never a footer label.

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

**G1, G2 and G3-lite remain required behavior.** The November 5 [source audit](insights-findings-capabilities.md#november-5-source-audit-and-today-contracts) records existing implementation support and remaining verification; the original October 27 gap list is a dated baseline.

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
| Relationship key and raw evidence version | Stable relationship separate from generated wording; links, saved state and AI references resolve the correct evidence snapshot |
| Meaningful revision and review state | Separate material revision, change kind/reason and last reviewed revision; raw metric changes alone do not trigger Updated |
| Goal assessment | Actual success/pending/failure state, assessed window/date, adequacy and confirmed missing inputs; distinguish no clear pattern from inadequate context |
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
| Early or insufficient records | Gathering context, or a specific missing-input request when confirmed; no arbitrary entry-count promise | Open that goal and relevant records |
| Complete analysis with no eligible findings | No clear pattern yet only if relevant coverage was adequate; otherwise the truthful data-gap state; distinguish failure and not-yet-analyzed | Existing history/logging |
| No unread eligible findings | All reviewed only when eligible findings exist; retain ordinary previews and distinct no-finding goal states | Goal rows and Explore Insights |
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

Use Inter 400/500 for the full Insights content hierarchy; the compact Today component uses the scoped semibold roles above. Use Inter 400/500 elsewhere and Inter 600 for the existing selected navigation and primary-button roles, with approved fallbacks. Emphasis comes from takeaway size, data, icons, spacing, and grouping; avoid undifferentiated white text across nested layers. Comparison content uses unframed sections inside a reading surface. The existing three Your Progress metric tiles remain the bounded nesting exception. Preserve that component's current 20-unit heading icon, 18-unit value icons, 20-unit values, New badge, trailing chevron, and whole-group earned-badges destination; the display-only tiles are not separate actions. Its existing 700-weight New label does not establish a new Insights text role.

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
| IP-01 | Today places one compact all-selected-goal Insights card after required care context and before plan/progress/logging content; one useful preview/status per goal, no full AI narrative |
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

### Today overview acceptance

| ID | Reviewable requirement |
| --- | --- |
| TO-01 | Every selected/available goal appears exactly once in stable order; changing unread state never reorders goals |
| TO-02 | A goal with one finding opens it; multiple findings open a list; a no-finding row opens its honest status; Explore Insights opens the overview |
| TO-03 | Header counts distinct eligible relationship keys; per-goal counts include shared mappings without duplicating discovery/review identity |
| TO-04 | Opening lists, filters, Today or failed detail loads marks nothing reviewed; opening an actual finding marks only the displayed meaningful revision |
| TO-05 | Reviewing dairy/bloating changes the fixture total 4→3 once and both related goals together; their second finding remains unread |
| TO-06 | Reviewed rows retain useful previews without highlight; all reviewed keeps no-finding states; no eligible results never produces All reviewed |
| TO-07 | New, Updated and multiple-unread badges follow their exact definitions; Updated explains a material change relative to reviewed evidence |
| TO-08 | Routine metric refresh, rewording and theme changes do not reset review; a genuinely newer revision arriving during detail reading stays unread |
| TO-09 | No clear pattern requires successful adequate assessment; specific missing-input copy requires a verified gap; failure and missing observations stay distinct |
| TO-10 | Persist review across restart and all mapped goals; saved/hidden/reward/plan states and cloud exclusions remain independent |
| TO-11 | Light/dark unread colors match the scoped aliases; all ten role checks pass; badge text and accessible labels supplement color |
| TO-12 | Validate 320-unit width, large text, full long goal labels, screen-reader destination/count announcements, focus and native targets without clipping |
| TO-13 | Required care context remains first; plan statuses remain record-derived; all Today content can scroll clear of floating capture controls |
| TO-14 | Replace illustrative fixtures with real eligible source data and validate source/maturity/limitations in actual finding details before release |

## Integration and migration

Reuse and verify the existing G1 goal mappings, relationship-first lead selection, G2 assessment, G3-lite identity and G7 surfaced-family adapters documented in the November 5 audit. Add the separate meaningful-revision/review-state contract and explicit per-goal coverage/outcome assessment needed by Today. Do not turn generic hints or raw evidence versions into those states. Preserve G5 honest timing and G6 unknown/denominator disclosure. Neutral Possible Connection supports the first presentation slice; evaluated labels must remain disabled until their criteria are implemented and validated. The [capability scope](insights-findings-capabilities.md) is controlling for deferred work.

Reuse the app's fixed goals, native icons, stomach asset, logging, Timeline, Charts, rewards, consent, care and analysis services. Existing local plans retain their templates and eligibility. Native implementation must resolve evidence snapshots, record routing, saved/hidden state, timezone/aggregation rules, plan persistence, cloud exclusions, and accessibility. This documentation does not implement those services.

The default [reference gallery](../../assets/app/insights-presentation/index.html) leads with the November 5 Today package and retains the five October 27 Insights/evidence/plan pairs. Editable Today source is in `tooling/today-insights-reference/`; run `tooling/build-today-insights-reference.py`, capture through the documented browser workflow, then `tooling/package-today-insights-reference.py`. The packager validates provenance, dimensions, loaded assets, theme parity, approved states and contrast, and updates the marked specification galleries. The earlier packagers are guarded against replacing the current gallery. Historical references do not override this specification.

Controlling references: [Insights and Correlations](insights-and-correlations.md), [App Visual Specification](../02-design/app-visuals.md), [Progress and Disclosure](../02-design/progress-and-disclosure.md), [Insight Types](../05-ai/insight-types.md), [Confidence and Evidence](../05-ai/confidence-and-evidence.md), and [Hybrid Local Findings](../../adr/0010-hybrid-local-findings-optional-llm.md).

## Version History

- 2026-11-05: Approved compact Today overview, all selected fixed goals, strong theme-specific unread treatment, distinct no-finding states, per-finding meaningful-review contract, 14 app-only references and current source audit. Detailed documentation approved after local review; publication and native implementation pending.

- 2026-10-27 (approved connection-led amendment): Incorporates G1–G3-lite, honest timing/coverage, surfaced-family adapters and deferred analyzer/plan scope. Replaces count-first summaries and unsupported fixtures with paired connection-led references; approved for publication after local review.

- 2026-10-27: Integrates the approved refined journey, fixed goal catalog/icons, consistent goal-specific footers, automatic plan tracking, outlined plan management, brief AI review and contextual chat. Adds 38 high-fidelity app-only references, detailed display/state/interaction contracts, and implementation acceptance criteria. Approved for publication after local review.
- 2026-10-25: Earlier overview/detail and filter experiments, including Flutter captures. Retained as historical references and superseded by the October 27 design.
