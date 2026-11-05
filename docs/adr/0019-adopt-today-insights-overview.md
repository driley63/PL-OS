# ADR-0019: Adopt the compact Today Insights overview

Status: Design and detailed documentation accepted after local review; unreleased
Date: 2026-11-05
Owner: Product, Design System, and AI Working Groups
Proposal: [RFC-0013](../rfc/0013-today-insights-overview.md)
Amends: the Today hierarchy and finding-review behavior in [ADR-0017](0017-adopt-goal-led-insights-presentation.md)

## Context

The single Today finding remained too wordy and did not show whether other selected goals had useful information. The owner wants to glance at the app, decide whether to investigate, and understand what they will be opening. Showing all selected goals makes the app's coverage visible without repeating the complete Insights landing page.

The owner approved one compact card, brief goal rows, prominent unread treatment in both themes, a dark-green indicator and light-green fill in light appearance, and separate states for reviewed findings, meaningful updates and missing context. The approved examples were expanded to demonstrate shared findings, partial review and all-reviewed behavior before this documentation update.

## Decision

Adopt the [Today insight region contract](../specs/03-product/insights-presentation.md#today-insight-region). Required care context remains first; the compact Insights card precedes plan and routine Today content. Each selected, available fixed goal has a stable row with its current exact label/icon, brief preview or honest state, optional unread badge and clear destination. Full evidence and AI narrative do not appear in this card.

Count distinct unread findings, not goal mappings. A shared finding is one discovery with one review state. One eligible finding opens its detail; multiple findings open a goal list without marking them reviewed. Only successfully showing the actual finding marks its displayed meaningful revision reviewed. Reviewed rows keep useful previews. Meaningful updates explain What changed; raw metric refreshes and rewording do not become notifications.

Distinguish an adequately assessed window with no clear pattern, a confirmed missing input, and insufficient context without a precise known gap. An empty finding list cannot establish which applies. Retain loading, stale, failure, care and privacy contracts independently.

Use the approved scoped unread roles from existing palette colors, actual fixed goal labels, current app shell, canonical woven artwork and stomach icon. Preserve the broader relationship-first Insights landing page, goal-specific footers, evidence/AI contracts and existing domain plans in ADR-0017.

## Alternatives considered

- One large finding card: useful for one topic but obscures other goals and consumes too much Today space.
- A separate full card per goal: too much repeated structure for a concise overview.
- A single unread count without previews: does not tell the user what they are opening.
- Clearing all findings on goal entry: hides unread material the user has not actually opened.
- Treating each raw evidence version as Updated: routine logging would repeatedly demand attention without a meaningful change.

## Consequences and delivery

The detailed specification defines copy, transitions, routing, counts, meaningful revision semantics, required source fields, scoped geometry/colors and native acceptance criteria. The [capability audit](../specs/03-product/insights-findings-capabilities.md#november-5-source-audit-and-today-contracts) records support observed in local source `9e4fb3d` and remaining review/assessment contracts. No new analyzer, clinical threshold, cloud sharing or relationship-native plan is approved here.

Keep 14 original high-resolution browser captures across seven matched light/dark scenes, their approved source, capture observations, hashes and contrast checks. Archive the superseded Today reference; retain the other October 27 Insights/evidence views with explicit historical-label notes. Browser fixtures do not certify native analysis, persistence, accessibility or full evidence rendering.

The owner approved the detailed PL-OS update after local review. The approved documentation is recorded locally; remote publication, native implementation and release remain separate actions.
