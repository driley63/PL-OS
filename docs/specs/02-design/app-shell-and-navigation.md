# App Shell and Navigation

Status: Released
Owner: Design System Working Group
Version: 1.5.0
Last updated: 2026-08-04

## Purpose

Defines app shell, navigation, route labels, hierarchy, and wayfinding standards for Plectara mobile, web, prototype, and documentation examples.

## Scope

- Top app bars, bottom navigation, side navigation, tabs, breadcrumbs, and contextual navigation
- Global app shell regions for authenticated and unauthenticated product surfaces
- Route labels, active states, back behavior, deep-link entry, and recovery navigation
- Mobile, tablet, desktop, and prototype implementation guidance

## Requirements

- Navigation must make the user's current location and available next steps clear.
- Navigation labels must describe user value, not internal implementation names.
- Primary product navigation must stay stable across high-frequency health workflows.
- Health-sensitive routes must avoid exposing private health details in visible route labels, URLs, or browser titles.
- Navigation state must be understandable without color alone.
- Platform conventions may be used when they do not conflict with PL-OS navigation hierarchy or privacy rules.

## Shell Regions

| Region | Purpose | Guidance |
| --- | --- | --- |
| Header or top app bar | Current context, global actions, search, account access | Keep compact; do not overload with page-specific actions |
| Primary navigation | Main product destinations | Use stable labels and one active state |
| Secondary navigation | In-section tabs or filters | Keep scoped to the current feature or page |
| Content header | Page title, summary, primary local action | Prefer one primary action and short context |
| Utility area | Sync, help, settings, export, profile, or support access | Keep privacy-sensitive controls explicit |
| Footer or legal region | Terms, privacy, version, support links | Use for low-frequency informational links |

## Navigation Patterns

| Pattern | Use | Constraints |
| --- | --- | --- |
| Bottom navigation | Mobile top-level app areas with 3 to 5 destinations | Do not use for actions or transient workflow steps |
| Side navigation | Tablet or desktop app areas with persistent sections | Keep labels short and group related destinations |
| Top tabs | Peer views within the same page or feature | Do not mix top-level and in-page destinations |
| Breadcrumbs | Deep desktop information architecture | Avoid on simple mobile flows where back behavior is enough |
| Step navigation | Multi-step workflows with known sequence | Show progress and allow safe backtracking |
| Contextual links | Related detail pages, reports, or settings | Keep secondary to the main task |

## Label Rules

- Use product language such as `Today`, `Timeline`, `Insights`, `Reports`, and `Settings`.
- Avoid engineering labels such as `Records`, `Entities`, `CRUD`, `Jobs`, or `Pipelines` in user-facing navigation.
- Use nouns for destinations and verbs for actions.
- Keep labels stable between mobile and desktop unless space forces an approved abbreviation.
- Pair icon-only navigation with accessible labels and visible selected state.

## States

Navigation components must define default, hover, active, focused, disabled, loading, unavailable, and permission-denied states when applicable.

Unavailable navigation should explain why the destination is blocked and how to recover. Signed-out, consent-revoked, missing-permission, deleted-data, and stale-data states must route users to recovery paths instead of dead ends.

## Implementation Guidance

- Use released Brand Identity color tokens and Design Language spacing/radius tokens.
- Use `color.brand.primary` for selected standard navigation state and reserve `color.ai.primary` for AI-specific destinations only.
- Keep mobile navigation touch targets at least 44 by 44 px.
- Preserve route identity across refresh, deep link, and platform back behavior.
- Test long labels, localization expansion, reduced motion, and high zoom.
- Document any route that intentionally changes content order across breakpoints.

## Acceptance Criteria

- Users can identify where they are and how to return to prior context.
- Top-level navigation remains stable across repeated daily use.
- Navigation labels do not expose sensitive health details.
- Active, disabled, blocked, and focused states are visible without color alone.
- Mobile, desktop, keyboard, screen-reader, and deep-link behavior are reviewable.

## References

- specs/01-brand/color-system.md
- specs/02-design/layout-grid.md
- specs/02-design/buttons.md
- specs/02-design/iconography.md
- specs/03-product/experience-principles.md
- specs/04-engineering/routing.md

## Version History

- v1.5.0: Adds app shell, navigation, route label, and wayfinding standards.
