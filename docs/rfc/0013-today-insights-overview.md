# RFC-0013: Compact Today Insights overview

Status: Design and detailed documentation accepted after local review; unreleased
Date: 2026-11-05
Owner: Product, Design System, and AI Working Groups
Decision: [ADR-0019](../adr/0019-adopt-today-insights-overview.md)

## Problem

Today needs a useful, visually distinct Insights centerpiece without becoming a second detailed Insights page. A single prose-heavy finding does not show whether the app has considered the user's other goals. A count alone does not explain what deserves attention.

## Accepted approach

Use one compact card containing a row for every selected, available fixed goal. Show its exact current label/icon, one useful short preview or honest no-finding state, an unread cue when applicable and a clear drilldown. Keep stable goal order. Put this card after care notices and before plan/routine content. Retain the existing woven shell and complete evidence in Insights.

Make unread rows conspicuous through the approved fill, leading accent, icon and badge. In light appearance, use Jade fill with existing deep-green markers/icons/badges and Ink body text. Dark appearance uses deep-green fill, Jade accent/badges and Ivory text. These are scoped roles built from registered colors, with text/non-text contrast checks and redundant text cues.

Opening an actual finding reviews only that meaningful revision. Lists and overviews review nothing. Shared findings count once globally and update all mapped rows. Preserve useful previews after review. Updated requires a material evidence/interpretation change and a What changed explanation; ordinary refreshes do not reset attention.

No clear pattern yet, a known missing-input request and Gathering context are separate assessed states. Do not infer them from an empty array or generic hint. Loading/failure/stale states and care/privacy rules remain independent.

## Scope and alternatives

This amends the single-finding Today approach in RFC-0011. It retains the relationship-first Insights landing page, fixed-goal filter row, detailed evidence, optional AI review, existing domain plans and data-sharing exclusions. Separate full cards per goal, a bare notification count, bulk-read-on-entry behavior and raw-version notifications were rejected because they undermine concise, useful attention guidance.

The design does not approve new analyzers, treatment guidance, negative-outcome capture, clinical thresholds or relationship-native planning. The local source audit distinguishes existing support from remaining presentation/review contracts; screenshots are representative fixtures.

## Specification and validation

The [detailed specification](../specs/03-product/insights-presentation.md#today-insight-region) governs states, destinations, counts, exact copy, material revision semantics, visual roles and TO-01–TO-14 acceptance criteria. The [capability audit](../specs/03-product/insights-findings-capabilities.md#november-5-source-audit-and-today-contracts) records implementation prerequisites.

Seven scenes in each theme demonstrate initial unread, partial review, all reviewed, two goal-list states, the distinct unread list and an updated finding. Store original 1179 × 2556 captures, source hashes, readiness/theme-parity observations and contrast evidence. Validate the local gallery and strict documentation build; native persistence, real analyzer output, accessibility and release remain separate work. The owner approved the detailed documentation after local review. Remote publication remains a separate action.
