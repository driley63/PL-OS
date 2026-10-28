# RFC-0011: Goal-led Insights presentation

Status: Connection-led design and capability scope accepted; documentation approved for publication; unreleased
Owner: Product, Design System, and AI Working Groups
Date: 2026-10-27

## Problem and approved proposal

Today and Insights expose too much narrative before users can understand what their records show. Earlier exploration also separated findings by log type and introduced custom-goal labels that do not match the app's fixed goal catalog. The owner requested a new approach based on the running app, reviewed the complete journey in both themes, and approved the detailed PL-OS specification after local review.

Adopt a brief Today highlight and compact, automatically tracked plan progress. Organize Insights around the user's selected goals from the existing catalog in one horizontally scrolling **Filter Insights** row. Use connection-led goal cards with named habit/outcome signals, succinct context, and the consistent footer **Explore more about [Goal Name]**. Use the approved stomach silhouette for Better Digestion.

Progressively reveal goal comparisons, connection evidence, optional AI review, scoped chat, and plan management. Keep direct period comparisons distinct from possible relationships. Show unavailable evidence honestly. Plans derive progress from qualifying records; the displayed statuses are not editable checkboxes. Pause/Resume and End This Plan use outlined buttons and confirmation where required.

## Alternatives and boundaries

The earlier custom-goal and log-type-filter studies are superseded. A wall of AI narrative delays access to the user's findings; collapsing all content without a useful summary also obscures the next step. The accepted design provides a concise takeaway with explicit routes to supporting information.

The approved hierarchy applies to Today and Insights within the existing app shell. Preserve canonical artwork, theme foundations, fixed goal eligibility, clinical rules, consent, and cloud exclusions. Local cycle and wellbeing goals remain excluded from cloud context, including their names. Presentation approval does not change analysis algorithms, establish causal conclusions, or authorize new data sharing.

## Specification and validation

The [Insights Presentation specification](../specs/03-product/insights-presentation.md) defines route behavior, data fields, sample context, empty and error states, plan lifecycle, accessibility, visual values, and acceptance criteria. Its 12 current app-only references cover six matched views in each theme at 1179 × 2556 pixels; the earlier comparison-first gallery is historical. The images are browser-rendered design references, not evidence of shipping native implementation.

[ADR-0017](../adr/0017-adopt-goal-led-insights-presentation.md) records the approved decision. Keep the source, capture observations, checksums, and paired gallery with the specification. Validate the strict documentation build, reference inventory, asset consistency, and existing contrast contracts. Native implementation and device/accessibility validation remain separate work. The owner approved publication of this capability-scoped amendment after local review.

## Connection-led scope amendment

The owner approved [capability decisions](../specs/03-product/insights-findings-capabilities.md): G1 goal mapping and relationship-first selection, G2 evaluated maturity with a short reason, G3-lite distinct-period recurrence and stable identity, honest timing/coverage, and evidence adapters for surfaced families. Until evaluated criteria exist, screenshots use Possible Connection. Replace the unsupported walking/sleep example with existing activity/energy evidence. Keep device-only exclusions and current domain-based plans; defer new negative-outcome capture and relationship-native plans. Neither recurrence nor a maturity label establishes causation.
