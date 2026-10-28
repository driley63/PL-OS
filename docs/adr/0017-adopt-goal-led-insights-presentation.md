# ADR-0017: Adopt goal-led Insights presentation

Status: Connection-led design and capability scope accepted; documentation approved for publication; unreleased
Date: 2026-10-27
Owner: Product, Design System, and AI Working Groups
Proposal: [RFC-0011](../rfc/0011-goal-led-insights-presentation.md)

## Context

The owner approved the redesigned Today and Insights journey after reviewing the existing app, light and dark mockups, meaningful goal iconography, automatically tracked plan statuses, button treatment, and consistent card navigation. The previous October 25 studies no longer represent the approved information architecture.

## Decision

Adopt the [Insights Presentation specification](../specs/03-product/insights-presentation.md). Today shows compact plan tracking and one eligible finding. Insights uses the existing fixed goal catalog in one horizontally scrolling **Filter Insights** row. Cards show a short finding, supporting visual evidence where available, and **Explore more about [Goal Name]** as the footer. Use the exact product goal labels and the approved stomach icon for Better Digestion.

Lead with eligible habit/outcome relationships; ordinary period comparisons move into details or serve as a meaningful-change fallback. Goal chips filter the overview, while cards open their leading evidence directly. Provide optional AI review with concise takeaways and expandable explanation, followed by scoped chat. Keep privacy notices as supporting text rather than goal-navigation labels. Derive plan progress from qualifying records and use outlined Pause/Resume and End This Plan controls.

Use the approved woven shell, opaque reading cards, semantic icon/color roles, and detailed light/dark hierarchy. Preserve the hybrid local findings and optional cloud narrative model in ADR-0010. The presentation does not extend clinical interpretation, consent, or cloud eligibility.

## Consequences

This amends the Today/Insights hierarchy in the app visual standard. Other app screens, canonical artwork, and global theme foundations retain their existing authority. Older custom-goal and log-type-filter experiments remain historical material and must not guide implementation.

The written specification supplies interaction, data, state, accessibility, and acceptance requirements beyond the depicted examples. Store six current matching views per theme, reproducible reference sources, and a checksummed manifest. Preserve the earlier 19-view-per-theme package as historical. Browser-rendered design references do not certify native layout, persistence, analytics correctness, or assistive technology behavior.

Implementers must map the real goal, evidence, consent, and plan models to the display contract and complete the native acceptance criteria. The owner approved publication of this capability-scoped amendment after local review. App implementation, app deployment, and a tagged release remain separate work.

## Connection-led scope amendment

The owner approved [capability decisions](../specs/03-product/insights-findings-capabilities.md): G1 goal mapping and relationship-first selection, G2 evaluated maturity with a short reason, G3-lite distinct-period recurrence and stable identity, honest timing/coverage, and evidence adapters for surfaced families. Until evaluated criteria exist, screenshots use Possible Connection. Replace the unsupported walking/sleep example with existing activity/energy evidence. Keep device-only exclusions and current domain-based plans; defer new negative-outcome capture and relationship-native plans. Neither recurrence nor a maturity label establishes causation.
