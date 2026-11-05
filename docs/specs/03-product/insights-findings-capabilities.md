# Insights Findings Capabilities

Status: Original capability scope approved October 27; November 5 source audit and Today design amendment approved after local review
Decision dates: 2026-10-27 capability scope; 2026-11-05 Today design
Applies to: [Insights Presentation](insights-presentation.md)

## Basis and product promise

The owner reviewed the findings-gap document and supplied feasibility decisions and expected-functionality deltas. This page carries those decisions into PL-OS. The originating document remains in `outputs/insights-connections-direction-2026-10-27/findings-capability-gaps.md`. The original source audit was against local Plectara commit `3044e87`. The November 5 update below checks local source `9e4fb3d`; neither audit proves a deployed build or native end-to-end behavior.

Help people identify potential links between habits and symptoms or wellbeing, understand how much comparable evidence supports them, and inspect the underlying records. Sustained logging can improve the chance of detecting a useful connection and assessing its consistency. It cannot guarantee a relationship or prove a cause.

## Approved scope and deltas

| ID | Decision | Required first scope | Delta / deferred work |
| --- | --- | --- | --- |
| G1 | Yes | Map existing finding codes, outcomes/measures and factors to fixed goals. Prefer eligible relationships over progress comparisons; preserve secondary evidence. | One relationship can serve several goals without becoming several discoveries. No AI-text matching. |
| G2 | Yes | Shared evaluated maturity: comparable coverage, consistency, conflict and freshness; return a status and a short UI-visible reason. | Developing Pattern / Consistent Pattern are gated on evaluated criteria. Until implemented, use neutral Possible Connection. Entry volume, AI wording and care urgency cannot substitute. |
| G3 | Partial | G3-lite: stable relationship key, separate evidence versions, and recurrence across actual distinct periods. Recompute affected support after edits/deletions. | No double-counting overlapping refreshes. Full long-horizon evidence storage and rich per-week panels deferred. “Three weeks” requires three genuinely assessed periods. |
| G4 | No | Replace the walking → higher same-night sleep example with an existing wellbeing/activity association. | Dedicated walk/sleep pairing analyzer deferred. No screenshot-driven analyzer requirement. |
| G5 | Yes | Match language to actual timing. The current design uses “near” and explains the ±four-hour window. | Exclusive “after” language requires directional matching, explicit lag/boundary rules and overlap attribution; that alternative is not implied by the current references. |
| G6 | Partial | Missing observations remain unknown; disclose current logged-co-occurrence denominators and coverage limits. | New meal-specific bloating/no-bloating follow-up capture and verified no-walk cohorts deferred. |
| G7 | Partial | Evidence adapters for the families actually surfaced: signals, time relation, named groups, values, units/scales, counts, limitations, and record IDs or a reproducible versioned selection. | Universal evidence normalization for every analyzer is deferred. Sparse supported findings receive honest text, without invented charts or precise-record links. |
| G8 | No | Retain existing domain-based local plans, eligibility, care gates and device/cloud exclusions. | Relationship-native plan selection, paired-signal tracking and plan/relationship recurrence integration deferred. |

## October 27 baseline — historical support and gaps

The existing `LocalFinding` contract contains code, domain, kind, label, flexible metrics, evidence window, related titles and local-only status. That flexibility does not supply missing calculations or establish evidence quality on its own.

- `goal_insights.dart` currently relies on explicit goal metadata / goal-family codes and favors direct comparisons. G1 adds reviewed mappings for useful existing meal and wellbeing relationships and changes lead selection.
- `meal_tag_analyzer.dart` uses absolute time distance around meals. It supplies tagged/untagged meal counts and nearby symptom counts, not explicit symptom-free meal follow-ups. Its care-related stronger result must not become a generic maturity badge.
- `wellbeing_analyzer.dart` supplies measure/factor, lag, group averages, rated-day counts and direction. Activity/energy is a supported family and stays device-only. Missing activity records do not establish inactivity.
- Ordinary analysis uses a 14-day window. Finding-family codes and report-content hashes are not sufficient stable relationship identities. G3-lite must distinguish the relationship definition from changing evidence and refreshes.
- Existing plan focus is a partial finding snapshot and domain template selection. G8 does not authorize replacing it with a relationship experiment engine.

## Minimum assessment and evidence contract

For every surfaced relationship, supply a stable key from signal/factor, outcome, timing/lag and calculation definition; a separate evidence version; related fixed goal keys; source family; actual period; structured claim; care urgency; local/cloud eligibility; and visible limitations. Add optional chart and supporting-record capabilities only where the adapter supplies their basis.

A G2 assessment adds its criteria version, comparable coverage, actual distinct periods assessed, support/conflict in those periods, freshness, maturity state and short reason. Thresholds must be defined and validated per applicable family before the UI uses evaluated labels. This document intentionally does not declare an arbitrary “N logs” or “N weeks” rule.

G3-lite may retain sufficient local assessment snapshots or reproducibly derive distinct-period results from historical source records. It need not build the deferred evidence warehouse. Record edits, deletions and changed eligibility invalidate the relevant evidence version and assessment. The same observations in overlapping windows cannot count as independent repeated support.

## October 27 reference corrections

- Use meal/bloating **3 of 8 versus 3 of 12**, with accurate rounded percentages and ±four-hour wording. These are illustrative numbers, not a verified user result. The older **4 of 6 versus 2 of 12** example crosses the audited care-gap condition and must not silently omit that care state.
- Use activity/energy **7.2/10 versus 5.1/10**, with seven and six rated days and accurate “without an activity log” wording. Do not describe walking, a verified no-walk group, or sleep ratings.
- Sleep-quality comparisons, if used elsewhere, retain the actual **0–10** scale.
- The October 27 captures use **Possible Connection**. November 5 illustrative fixtures include Developing Pattern, following the approved evaluated-state design; native labels and reasons must come from actual assessed G2/G3-lite evidence.
- Keep **Two-Week Meal and Symptom Check** as a domain plan. Symptoms are logged when noticed; silence is not successful symptom tracking.

## Acceptance examples

| Area | Required result |
| --- | --- |
| Goal mapping | Meal/bloating is reachable under appropriate symptom/digestion goals; activity/energy under More Energy. Plain log totals do not displace them. |
| Privacy | More Energy evidence and goal context stay local, including indirect overall AI summaries and suggested questions. |
| Maturity | Duplicates cannot promote a pattern; incomplete comparators cannot yield Consistent Pattern; contradictory/deleted support can downgrade it; the UI explains why. |
| Recurrence | Three refreshes of the same fortnight do not become three weeks. Dairy/bloating and dairy/headache have different identities. |
| Timing | A symptom before eating is never described as after eating. Current before/after co-occurrence is clearly labeled. |
| Coverage | No symptom entry remains unknown. Meal denominators are not relabeled explicit follow-up cohorts. |
| Evidence | Named groups, scales and denominators agree with the adapter. Unsupported numbers and exact-record routes are omitted. |
| Plans and care | Current domain rules and care eligibility control the plan; a maturity label cannot bypass care restrictions. |

## Original delivery order — October 27

G1 is the first presentation slice. Follow with G2 and G3-lite to support meaningful maturity and honest recurrence. Add G7 adapters for the surfaced families, with G5 timing and G6 coverage corrections throughout. Keep G4, new negative-outcome capture, universal evidence history, and G8 outside this scope.

The neutral connection display can precede evaluated maturity, but the approved final scope includes G2 and G3-lite. A limited initial display must not be recorded as completion of those requirements.


## November 5 source audit and Today contracts

**Audit scope:** local Plectara checkout `9e4fb3d`, read on November 5, 2026. This updates the historical gap list; it is source evidence, not a claim that all requirements have shipped, passed evaluation, or are wired into every screen. No consuming-app code was changed by the documentation update.

| Capability | Observed source support | Remaining design obligation |
| --- | --- | --- |
| Goal mapping and lead selection | `lib/insights/goal_insights.dart` maps existing relationship families to fixed goals; bundles expose a relationship-first lead and finding views with relationship identity | Use these reviewed mappings; verify all selected-goal routes and shared identity. Do not re-create goal matching from AI text. |
| Maturity | `lib/insights/pattern_maturity.dart` provides assessed states, reasons and distinct-period support fields; `finding_enrichment.dart` attaches assessment data | Consume the actual assessed state/reason and validate coverage, conflicts, staleness and family thresholds. A fixture label is not an assessment. |
| Relationship identity and raw version | `FindingRelationship.keyFor()` and `evidenceVersionFor()` separate relationship identity from changing evidence; enrichment reconstructs prior distinct-window support for supported families | Preserve method/timing identity and validate invalidation. Existing raw versions include changing metric values; they are not a meaningful-update notification contract. Prior-window support is not a universal long-horizon evidence warehouse. |
| Evidence adapters | `lib/insights/finding_evidence.dart` supplies structured display evidence for supported families | Keep honest timing, scales, missingness, eligibility and record scope. Do not infer unsupported evidence from prose. |
| Fixed goal labels | `lib/models/onboarding_options.dart` now uses Reduce Symptoms, Improved Digestion, Improved Sleep and Improved Mood, alongside the other unchanged fixed labels | Use stable keys and exact current labels. The dated October 27 screenshots retain old wording only as historical references. |
| Per-goal no-finding state | `GoalInsightBundle` exposes comparison, connections and a generic gathering hint; that alone does not distinguish successful adequate assessment from known missing input or inadequate context | Add/verify structured per-goal assessment status, actual window/date, adequacy and specific missing inputs before using No clear pattern yet or a factual missing-input request. |
| Meaningful review revision | Raw evidence versions exist; a separate material-change/reviewed-revision contract was not found in the inspected insights/model/service source | Define a stable meaningful revision and reason separate from raw metrics; distinguish never-reviewed New from a substantive Updated result. |
| Durable individual review | A persisted per-relationship reviewed-revision mechanism was not found in the inspected source | Implement/verify successful-detail-only review, persistence across restart, shared-goal deduplication and navigation return updates. Do not treat list entry as review. |

### Required Today presentation inputs

The following is a conceptual contract, not a claim that these fields already exist as an app API. Reuse real source models where they supply the value; add only the missing adapter/state contract.

| Input | Required meaning |
| --- | --- |
| Selected available goal keys | Exact fixed catalog identities in stable order; no custom-label matching |
| Eligible relationships per goal | Stable many-to-many mapping, visibility/shareability policy, useful concise preview and a route to the actual finding |
| Relationship key | One identity across all mapped goals and routes; independent of wording and current metrics |
| Raw evidence version | The actual snapshot used for values, dates, supporting records, maturity and AI references |
| Meaningful revision / change reason | Version of a substantive interpretation, coverage, direction, limitation or next-step change; family-assessed and explainable |
| Reviewed revision | Last successfully displayed meaningful revision for the relationship; stored independently from saved, hidden, reward and plan states |
| Goal assessment | Pending/success/failure, assessed date/window, relevant coverage adequacy, confirmed missing inputs, and whether a supported relationship was found |
| Finding detail capability | Successful resolution of the actual evidence snapshot, material limitations and source attribution; an inaccessible result is not reviewed |

A bare empty connection list cannot establish **No clear pattern yet**. A generic canned hint cannot establish **Add symptom logs**. A changing raw metrics string cannot establish **Updated**. These three distinctions are release gates for the approved Today behavior.

### Fixture and scope boundaries

The Today examples use four distinct relationships across eight selected goals: dairy/bloating, activity/bowel, poor sleep/subsequent activity and activity/energy. The sleep example follows the existing activity-barrier family; it does not revive the deferred walking → same-night sleep analyzer. Each example is a representative display fixture, not validated personal evidence. Native code must verify actual eligibility, timing, mapping, assessed maturity and care requirements before displaying it.

The More Energy update explanation is illustrative. Actual change copy must be grounded in the current and previously reviewed evidence; do not generate materiality merely to match the screenshot. The surrounding Two-Week Activity Check is an existing domain-plan example, not relationship-native planning. G4, explicit negative-outcome capture, universal history and G8's deferred plan extensions remain outside scope.

The [Today contract](insights-presentation.md#today-insight-region) and TO-01–TO-14 acceptance criteria govern the added presentation and review behavior. Preserve existing clinical thresholds, consent, local-only wellbeing exclusions and independent care notices. Native persistence, analysis correctness and accessibility still require implementation validation.
