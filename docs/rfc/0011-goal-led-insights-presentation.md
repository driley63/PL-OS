# RFC-0011: Goal-led Insights presentation

Status: Design and detailed specification accepted; unreleased
Owner: Product, Design System, and AI Working Groups
Date: 2026-10-27

## Problem and approved proposal

Today and Insights expose too much narrative before users can understand what their records show. Earlier exploration also separated findings by log type and introduced custom-goal labels that do not match the app's fixed goal catalog. The owner requested a new approach based on the running app, reviewed the complete journey in both themes, and approved the detailed PL-OS specification after local review.

Adopt a brief Today highlight and compact, automatically tracked plan progress. Organize Insights around the user's selected goals from the existing catalog in one horizontally scrolling **Filter Insights** row. Use takeaway-first goal cards with meaningful icons, bounded comparisons, and the consistent footer **Explore more about [Goal Name]**. Use the approved stomach silhouette for Better Digestion.

Progressively reveal goal comparisons, connection evidence, optional AI review, scoped chat, and plan management. Keep direct period comparisons distinct from possible relationships. Show unavailable evidence honestly. Plans derive progress from qualifying records; the displayed statuses are not editable checkboxes. Pause/Resume and End This Plan use outlined buttons and confirmation where required.

## Alternatives and boundaries

The earlier custom-goal and log-type-filter studies are superseded. A wall of AI narrative delays access to the user's findings; collapsing all content without a useful summary also obscures the next step. The accepted design provides a concise takeaway with explicit routes to supporting information.

The approved hierarchy applies to Today and Insights within the existing app shell. Preserve canonical artwork, theme foundations, fixed goal eligibility, clinical rules, consent, and cloud exclusions. Local cycle and wellbeing goals remain excluded from cloud context, including their names. Presentation approval does not change analysis algorithms, establish causal conclusions, or authorize new data sharing.

## Specification and validation

The [Insights Presentation specification](../specs/03-product/insights-presentation.md) defines route behavior, data fields, sample context, empty and error states, plan lifecycle, accessibility, visual values, and acceptance criteria. Its 38 app-only references cover 19 matched views in each theme at 1179 × 2556 pixels. The images are browser-rendered design references, not evidence of shipping native implementation.

[ADR-0017](../adr/0017-adopt-goal-led-insights-presentation.md) records the approved decision. Keep the source, capture observations, checksums, and paired gallery with the specification. Validate the strict documentation build, reference inventory, asset consistency, and existing contrast contracts. Native implementation and device/accessibility validation remain separate work. The owner approved publication after local review on October 27, 2026.
