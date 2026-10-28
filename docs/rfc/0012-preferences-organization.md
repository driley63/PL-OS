# RFC-0012: Preferences organization

Status: Design and detailed specification accepted; unreleased
Owner: Product and Design System Working Groups
Date: 2026-10-27

## Problem and selected proposal

Preferences is visually busy and asks users to scan many unrelated settings. Reduce the initial choice set to nine destinations grouped by intent: **Your Health**, **Settings**, and **Connections & Account**. The owner explicitly selected the Section Hub design and requested the Settings heading.

Use concise summaries and recognizable leading icons inside opaque grouped panels. Related settings open collection pages; specific preferences open directly. Preserve native Back, scroll position, and existing form editing behavior. Keep all current destinations and eligible conditional controls reachable.

## Alternatives

- **Section Hub — selected:** nine root destinations with related editors one level deeper. This reduces initial scanning while requiring an additional navigation step for some editors.
- **Direct List — not selected:** exposes the individual destinations immediately but retains a longer, denser root page. Preserve this alternative only in the historical design study.

## Behavior and scope

The [Preferences Organization specification](../specs/03-product/preferences-organization.md) maps all 22 existing root destinations and nested controls. It defines navigation, conditional visibility, shared reminder schedules, independent AI consents, privacy, theme geometry, accessibility, state boundaries, and acceptance criteria. [ADR-0018](../adr/0018-adopt-preferences-section-hub.md) records the selected direction.

The 28 app-only references show 14 matched views in both themes. They use the canonical woven artwork and local Inter fonts. They are browser-rendered design references, not shipping native screenshots or a redesign of every existing form. Permission-state layouts, complete health-connection controls, final consent treatment, and editor-specific refinements remain separate design work.

## Review and validation

Validate the documentation build, destination coverage, paired image inventory, fonts, artwork, and clipping. Native implementation must independently validate persistence, real permissions, consent transitions, adaptive text, assistive technology, and error recovery. The owner approved the detailed specification after local review on October 27, 2026. The owner approved publication to main on October 27, 2026.
