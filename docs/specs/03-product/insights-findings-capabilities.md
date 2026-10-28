# Insights Findings Capabilities

Status: Owner-approved scope and documentation; approved for publication; implementation pending
Decision date: 2026-10-27
Applies to: [Insights Presentation](insights-presentation.md)

## Basis and product promise

The owner reviewed the findings-gap document and supplied feasibility decisions and expected-functionality deltas. This page carries those decisions into PL-OS. The originating document remains in `outputs/insights-connections-direction-2026-10-27/findings-capability-gaps.md`. The source audit was against the local Plectara app at commit `3044e87`; this is a dated baseline, not a claim that these additions have shipped.

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

## Current support versus new work

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

## Reference corrections

- Use meal/bloating **3 of 8 versus 3 of 12**, with accurate rounded percentages and ±four-hour wording. These are illustrative numbers, not a verified user result. The older **4 of 6 versus 2 of 12** example crosses the audited care-gap condition and must not silently omit that care state.
- Use activity/energy **7.2/10 versus 5.1/10**, with seven and six rated days and accurate “without an activity log” wording. Do not describe walking, a verified no-walk group, or sleep ratings.
- Sleep-quality comparisons, if used elsewhere, retain the actual **0–10** scale.
- Use **Possible Connection** in current captures. Future Developing / Consistent Pattern labels and recurrence copy must come from evaluated G2/G3-lite results.
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

## Delivery order

G1 is the first presentation slice. Follow with G2 and G3-lite to support meaningful maturity and honest recurrence. Add G7 adapters for the surfaced families, with G5 timing and G6 coverage corrections throughout. Keep G4, new negative-outcome capture, universal evidence history, and G8 outside this scope.

The neutral connection display can precede evaluated maturity, but the approved final scope includes G2 and G3-lite. A limited initial display must not be recorded as completion of those requirements.
