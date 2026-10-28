# ADR-0018: Adopt the Preferences Section Hub

Status: Design and detailed specification accepted; unreleased
Date: 2026-10-27
Owner: Product and Design System Working Groups
Proposal: [RFC-0012](../rfc/0012-preferences-organization.md)

## Context

The existing Preferences screen exposes up to 22 destinations across broad configuration groups. The owner requested a calmer, better organized design, reviewed Section Hub and Direct List alternatives, and explicitly selected Section Hub. The middle group heading was changed from Your Experience to Settings.

## Decision

Adopt nine destinations under **Your Health**, **Settings**, and **Connections & Account** as defined in [Preferences Organization](../specs/03-product/preferences-organization.md). Health Profile, Tracking & Routines, Quick Log & Widgets, and Account & Privacy collect related existing editors. AI Insights & Chat, Reminders, Appearance, Your Progress, and Health Connections open their specific preferences surfaces.

Preserve Preferences as a pushed utility screen with native Back. Use grouped opaque reading panels, concise row summaries, leading icons, and whole-row navigation over the existing woven background. Keep the exact Settings heading. Direct List is a historical alternative, not a production mode.

## Consequences

Existing preferences and conditional destinations remain reachable; the specification provides a complete migration inventory. Reminder routes share existing schedules. Cloud consents remain separate, platform permissions remain authoritative, and account actions retain their established confirmations. Navigation approval does not authorize new sharing, tracking eligibility, clinical behavior, or changes to data retention.

The reference package contains 14 matched views in each theme, editable sources, and capture provenance. Browser-rendered design references illustrate organization and presentation; existing form rows and incomplete permission/connection states require their own detailed review. They do not certify native implementation or accessibility.

The owner authorized adding this design to PL-OS. The owner approved the detailed specification after local review on October 27, 2026. The owner approved publication to main on October 27, 2026. Application implementation, application deployment, and a tagged release remain separate work.
