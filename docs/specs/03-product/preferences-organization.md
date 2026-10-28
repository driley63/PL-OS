# Preferences Organization

Status: Section Hub design and detailed specification approved; unreleased; implementation pending

Owner: Product and Design System Working Groups

Version: Unreleased

Last updated: 2026-10-27

Decision: [ADR-0018](../../adr/0018-adopt-preferences-section-hub.md), proposed in [RFC-0012](../../rfc/0012-preferences-organization.md)

## Purpose and authority

Make Preferences easier to scan and make each setting's location predictable. The owner selected **Section Hub** and changed its middle group heading to **Settings**. This document adopts that organization, translates the approved design into navigation and presentation requirements, and identifies the existing behavior each destination must retain.

Section Hub is the selected design. Direct List was considered and is retained only as a historical alternative in the editable study; it is not a second production mode or user-selectable layout. This amendment covers Preferences organization and the pictured section layouts. It does not redesign every existing editor, implement application changes, or replace consent policies.

The current app's Preferences source exposes up to 22 destinations under Quick Log Configuration, Journal Configuration, and General. The new root has nine destinations under three groups. The 22-destination count includes the conditional Beverages and Saved Bowel Movements entries. Cycle Settings already exists deeper in tracking and does not add a new tracking capability here. Current app source was inspected; the simulator connection was unavailable, so this review does not claim a fresh native-device visual inspection.

Apply [Settings and Consent](settings-and-consent.md), [App Visual Specification](../02-design/app-visuals.md), [App Shell and Navigation](../02-design/app-shell-and-navigation.md), and [Lists and Tables](../02-design/lists-and-tables.md). This scoped navigation amendment does not authorize changes to clinical logic, tracking eligibility, cloud exclusions, data retention, or unrelated app screens.

## High-fidelity screen references

[Open the paired reference gallery](../../assets/app/preferences-organization/index.html){ .md-button }

The gallery contains **28 app-only PNGs: 14 matched views in both themes**, rendered from the reviewed design at **393 × 852 logical units and 1179 × 2556 pixels**. The images use the actual woven texture, Inter fonts, opaque reading surfaces, and approved colors; they are not enlarged thumbnails or screenshots of the conversation. Captures exclude review controls, browser chrome, and the alternative layout.

These are browser-rendered design references, not shipping-app screenshots. Rows representing existing forms are placement references; non-interactive example rows must become real native navigation targets. Sample switch values and System appearance selection are fixtures, not defaults or the user's current preferences. Complete consent, permission, editing, export, deletion, and device-specific states are governed by the written requirements below.

The [capture manifest](../../assets/app/preferences-organization/references.json) records file hashes, source provenance, dimensions, scroll positions, and the selected layout. Scrolled references keep the header visible and show the continuation of the same screen. Their captions identify what is pictured and what still needs detailed design.

<!-- PREFERENCES_GALLERY_START -->
### Section Hub

**Preferences · Section Hub** — Approved nine-destination hub. Your Health and Settings appear first; Connections & Account continues below.

| Light | Dark |
| --- | --- |
| [![Preferences · Section Hub in light appearance](../../assets/app/preferences-organization/screens/preferences-light.png?v=0403ab378352){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/preferences-light.png?v=0403ab378352) | [![Preferences · Section Hub in dark appearance](../../assets/app/preferences-organization/screens/preferences-dark.png?v=a5263d708c89){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/preferences-dark.png?v=a5263d708c89) |

**Preferences · Lower Groups** — The same hub scrolled to show Settings and Connections & Account.

| Light | Dark |
| --- | --- |
| [![Preferences · Lower Groups in light appearance](../../assets/app/preferences-organization/screens/preferences-lower-light.png?v=7e682767d31e){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/preferences-lower-light.png?v=7e682767d31e) | [![Preferences · Lower Groups in dark appearance](../../assets/app/preferences-organization/screens/preferences-lower-dark.png?v=d18fcf5b7534){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/preferences-lower-dark.png?v=d18fcf5b7534) |

??? example "Your Health — light and dark references"

    **Health Profile** — Your Goals, About You, Conditions, and Medications share one predictable destination. Existing editor rows are placement references.

    | Light | Dark |
    | --- | --- |
    | [![Health Profile in light appearance](../../assets/app/preferences-organization/screens/health-profile-light.png?v=1a76738a30b4){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/health-profile-light.png?v=1a76738a30b4) | [![Health Profile in dark appearance](../../assets/app/preferences-organization/screens/health-profile-dark.png?v=2605e99cecfa){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/health-profile-dark.png?v=2605e99cecfa) |

    **Tracking & Routines** — What to Track, Symptoms, logging preferences, and a contextual route to the shared reminder overview.

    | Light | Dark |
    | --- | --- |
    | [![Tracking & Routines in light appearance](../../assets/app/preferences-organization/screens/tracking-light.png?v=85e2b6d04875){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/tracking-light.png?v=85e2b6d04875) | [![Tracking & Routines in dark appearance](../../assets/app/preferences-organization/screens/tracking-dark.png?v=110f9d62d5cb){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/tracking-dark.png?v=110f9d62d5cb) |

    **Tracking · Cycle Available** — Cycle Settings is shown only when available and enabled. This example does not extend eligibility or cloud sharing.

    | Light | Dark |
    | --- | --- |
    | [![Tracking · Cycle Available in light appearance](../../assets/app/preferences-organization/screens/tracking-cycle-light.png?v=5b09100a14d1){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/tracking-cycle-light.png?v=5b09100a14d1) | [![Tracking · Cycle Available in dark appearance](../../assets/app/preferences-organization/screens/tracking-cycle-dark.png?v=66fc4c71542f){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/tracking-cycle-dark.png?v=66fc4c71542f) |

    **Quick Log & Widgets** — Saved reusable entries are separated from Quick Capture, which continues to widget pins, learned habits, and suggestions.

    | Light | Dark |
    | --- | --- |
    | [![Quick Log & Widgets in light appearance](../../assets/app/preferences-organization/screens/quick-log-light.png?v=bf4c4a9677f9){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/quick-log-light.png?v=bf4c4a9677f9) | [![Quick Log & Widgets in dark appearance](../../assets/app/preferences-organization/screens/quick-log-dark.png?v=cc2896d1beaf){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/quick-log-dark.png?v=cc2896d1beaf) |

??? example "Settings — light and dark references"

    **AI Insights & Chat** — Separate cloud explanation/plan, chat, and alcohol-sharing controls. Example values are not production defaults; native opt-in still requires complete consent disclosure.

    | Light | Dark |
    | --- | --- |
    | [![AI Insights & Chat in light appearance](../../assets/app/preferences-organization/screens/ai-light.png?v=6f9009f41c71){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/ai-light.png?v=6f9009f41c71) | [![AI Insights & Chat in dark appearance](../../assets/app/preferences-organization/screens/ai-dark.png?v=50f81ae3a93a){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/ai-dark.png?v=50f81ae3a93a) |

    **AI · Sharing Details** — Expanded sharing information illustrates disclosure grouping. Final consent wording and native authorization flows retain their existing governing contracts.

    | Light | Dark |
    | --- | --- |
    | [![AI · Sharing Details in light appearance](../../assets/app/preferences-organization/screens/ai-details-light.png?v=abf9dc8e408d){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/ai-details-light.png?v=abf9dc8e408d) | [![AI · Sharing Details in dark appearance](../../assets/app/preferences-organization/screens/ai-details-dark.png?v=f4156e3a104a){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/ai-details-dark.png?v=f4156e3a104a) |

    **Reminders** — One master preference with routes to the existing Sleep, medication, and Daily Check-In schedules. Permission-state and editor details require further design.

    | Light | Dark |
    | --- | --- |
    | [![Reminders in light appearance](../../assets/app/preferences-organization/screens/reminders-light.png?v=c1979970a08c){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/reminders-light.png?v=c1979970a08c) | [![Reminders in dark appearance](../../assets/app/preferences-organization/screens/reminders-dark.png?v=f49094f0366b){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/reminders-dark.png?v=f49094f0366b) |

    **Appearance** — System, Light, and Dark remain separate choices. Both references show the same illustrative System selection.

    | Light | Dark |
    | --- | --- |
    | [![Appearance in light appearance](../../assets/app/preferences-organization/screens/appearance-light.png?v=8bf72fa7ce7f){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/appearance-light.png?v=8bf72fa7ce7f) | [![Appearance in dark appearance](../../assets/app/preferences-organization/screens/appearance-dark.png?v=d894edd74b44){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/appearance-dark.png?v=d894edd74b44) |

    **Your Progress** — Logging points, streaks, and badges remain separate from health findings and AI.

    | Light | Dark |
    | --- | --- |
    | [![Your Progress in light appearance](../../assets/app/preferences-organization/screens/progress-light.png?v=1002810f0666){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/progress-light.png?v=1002810f0666) | [![Your Progress in dark appearance](../../assets/app/preferences-organization/screens/progress-dark.png?v=6c963ec0efca){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/progress-dark.png?v=6c963ec0efca) |

??? example "Connections & Account — light and dark references"

    **Health Connections** — iPhone organization example. Existing connection, consent, permission, and disconnection controls must remain in the complete native flow.

    | Light | Dark |
    | --- | --- |
    | [![Health Connections in light appearance](../../assets/app/preferences-organization/screens/connections-light.png?v=9b2fe9bb14ef){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/connections-light.png?v=9b2fe9bb14ef) | [![Health Connections in dark appearance](../../assets/app/preferences-organization/screens/connections-dark.png?v=018fb2315b1c){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/connections-dark.png?v=018fb2315b1c) |

    **Account & Privacy** — Account identity, provider-managed security, export, and policy routes. This is a navigation reference, not a replacement account form.

    | Light | Dark |
    | --- | --- |
    | [![Account & Privacy in light appearance](../../assets/app/preferences-organization/screens/account-light.png?v=af7614c2ec9e){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/account-light.png?v=af7614c2ec9e) | [![Account & Privacy in dark appearance](../../assets/app/preferences-organization/screens/account-dark.png?v=67a60462bc28){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/account-dark.png?v=67a60462bc28) |

    **Account · Privacy & Actions** — Contextual privacy links plus explicit Log Out and Delete Account buttons. Existing confirmation and deletion boundaries remain mandatory.

    | Light | Dark |
    | --- | --- |
    | [![Account · Privacy & Actions in light appearance](../../assets/app/preferences-organization/screens/account-actions-light.png?v=1c190ba9aaca){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/account-actions-light.png?v=1c190ba9aaca) | [![Account · Privacy & Actions in dark appearance](../../assets/app/preferences-organization/screens/account-actions-dark.png?v=34ab9e1da89a){ width="280" loading="lazy" }](../../assets/app/preferences-organization/screens/account-actions-dark.png?v=34ab9e1da89a) |

<!-- PREFERENCES_GALLERY_END -->

## Root hierarchy and labels

Keep **Preferences** as the page title and preserve its existing entry points from the app header. It opens as a pushed utility screen, with native Back to the originating app screen. Do not add it to the main bottom navigation or show the main tab bar beneath its section pages.

Use the following exact group labels, destination order, and reference summaries. Summaries describe scope without exposing health values, medication names, or account identity. Dynamic status may replace a scope summary only when it adds useful, non-sensitive information and has a real data source.

| Group | Destination | Reference summary | Opens |
| --- | --- | --- | --- |
| Your Health | Health Profile | Goals, personal details, and medications | Goals and health-context collection |
| Your Health | Tracking & Routines | Log types, symptoms, and daily routines | Tracking and logging-preference collection |
| Your Health | Quick Log & Widgets | Saved items, widget pins, and habits | Saved entries and Quick Capture collection |
| Settings | AI Insights & Chat | Optional AI and what you share | Existing AI controls, organized by feature and sharing |
| Settings | Reminders | Sleep, medications, and check-ins | Master preference and shared schedule destinations |
| Settings | Appearance | Light, dark, or your device setting | System / Light / Dark selection |
| Settings | Your Progress | Points, streaks, and badges | Existing logging-rewards preference |
| Connections & Account | Health Connections | Apple Health or Health Connect | Platform-appropriate health integration |
| Connections & Account | Account & Privacy | Sign-in, data export, and policies | Account, information, privacy routes, and account actions |

**Settings** is the middle group heading. Do not reintroduce Your Experience, General, or Journal Configuration. Section headings label their panels; they are not another layer of navigation. Keep all nine root rows available regardless of whether the user has saved entries or enabled a particular tracker. Conditional choices belong inside the applicable destination.

The root intentionally adds no search field, tabs, large profile hero, health metrics, promotional cards, or setup checklist. Do not shrink type to fit all groups into one viewport. Connections & Account remains reachable through ordinary vertical scrolling.

## Existing-destination mapping

Every existing destination remains reachable. This table is the migration inventory, not a request to create duplicate editors.

| Current root destination | Section Hub location | Required preservation |
| --- | --- | --- |
| Saved Meals | Quick Log & Widgets → Saved Items | Reusable meals and existing editing behavior |
| Saved Activities | Quick Log & Widgets → Saved Items | Reusable activities and existing editing behavior |
| Saved Bowel Movements | Quick Log & Widgets → Saved Items | Shown under existing bowel-tracking rule; discreet wearable/widget labels |
| Quick Capture | Quick Log & Widgets → Shortcuts & Habits | Pins, favorites, habits, suggestions, and privacy options |
| Your Goals | Health Profile → Your Direction | Existing fixed goal catalog, labels, eligibility, and local exclusions |
| What to Track | Tracking & Routines → What You Record | Symptoms always on; existing entries retained when another tracker is disabled |
| Medications | Health Profile → About You | Medication/supplement editors and their shared schedules |
| Conditions | Health Profile → About You | Current diagnosed-condition editor |
| Symptoms | Tracking & Routines → What You Record | Flare-Ups and Daily symptom configuration |
| Beverages | Tracking & Routines → Logging Preferences | Existing conditional visibility, units, and serving sizes |
| Activity Types | Tracking & Routines → Logging Preferences | Activity categories; distinct from Saved Activities |
| Sleep | Tracking & Routines → Logging Preferences | Default sleep times and morning reminder |
| Daily Check-In | Tracking & Routines → Logging Preferences | Due time, independent reminder preference, daily-symptom route |
| Account | Account & Privacy → Your Account / account actions | Account identity, provider-managed security, export, sign-out, deletion |
| About You | Health Profile → About You | Birthday, sex assigned at birth, and weight |
| Your Progress | Settings → Your Progress | Logging points, streaks, and badges; not health-outcome progress |
| Light/Dark Modes | Settings → Appearance | System, Light, and Dark; actual selected mode |
| AI Insights | Settings → AI Insights & Chat | Separate explanation/plan, chat, and alcohol-sharing choices |
| Notifications | Settings → Reminders | Existing master notification preference and OS-permission boundary |
| Health Apps | Connections & Account → Health Connections | Platform provider, read permissions, imports, disconnect behavior |
| Privacy Policy | Account & Privacy → Your Information | Complete existing policy |
| Terms of Use | Account & Privacy → Your Information | Complete existing terms |

Existing nested controls also remain reachable: eligible Cycle Settings; Export My Data; widget medication-name privacy; cycle tile visibility; pins and learned habits; hidden suggestions. Debug-only Seed Data and AI Scenario Import remain debug-only and must not appear in the production hierarchy.

## Navigation and return behavior

- Root rows are whole-row native navigation controls with a leading icon, label, optional summary/value, and trailing chevron. Do not create separate tap targets for the title, subtitle, and chevron.
- Health Profile, Tracking & Routines, Quick Log & Widgets, and Account & Privacy open collection pages. Existing editor rows then open their canonical forms. Other root destinations open their specific preferences surface directly.
- Preserve root scroll position when returning from a destination, and section scroll position when returning from an editor. Return focus to the row that opened the page when the platform supports it.
- Back from Preferences returns to the originating app screen and its state. Back from a section returns to Preferences. Back from a form returns to the actual caller, including the Reminders shortcut path.
- Contextual links reuse canonical destination identity and settings stores. Visiting Sleep through Reminders and visiting it through Tracking & Routines must not create different values or independent schedules.
- Preserve existing deep links and in-app settings routes through redirects/adapters where labels change. A missing or ineligible destination returns to a useful containing section with an explanation rather than silently changing eligibility.
- Existing form save, cancellation, dirty-state, and error behavior remains authoritative. Navigating between collection pages does not save or reset preferences. Do not add a global Save button to the hub.
- Unavailable data is not equivalent to Off, empty, or disconnected. Keep the destination reachable and explain loading or error in the appropriate surface.

## Section contracts

### Health Profile

Order the page as the brief introductory panel, **Your Direction** containing Your Goals, then **About You** containing About You, Conditions, and Medications. The introductory text is “The health context that helps Plectara understand your records.”

Keep account email and authentication separate in Account & Privacy. Retain the app's fixed goal catalog; this change adds no custom-goal editor. Do not expose current symptoms, diagnoses, medications, or weight in the root summary. Empty conditions/medications/goals must still offer the existing add/select paths.

### Tracking & Routines

Use **What You Record** for What to Track and Symptoms. Use **Logging Preferences** for Beverages, Activity Types, Sleep, Daily Check-In, and eligible Cycle Settings, in that order. Include a contextual Reminders route below these groups.

Keep the current dependency rules: Beverages is shown when beverage tracking is configured; Cycle Settings requires the existing availability and enabled-tracking rules. What to Track remains available as the recovery path when optional settings are hidden. Saved data must not be removed simply because a preference row disappears.

Symptoms remain always on. Disabling another tracker retains existing records and applies the existing import eligibility behavior. Daily symptoms, Flare-Ups, daily check-in due times, reminder preferences, sleep defaults, and activity categories keep their separate meanings. Do not confuse Activity Types with reusable Saved Activities.

### Quick Log & Widgets

Use **Saved Items** for Saved Meals, Saved Activities, and conditionally Saved Bowel Movements. Use **Shortcuts & Habits** for Quick Capture. The introduction is “Set up reusable entries and the shortcuts you use to log them.”

Saving an entry and pinning it are distinct actions. Quick Capture continues to contain the current widget privacy/options, cycle tile, pinned items, favorites, learned habits, dormant habits, and hidden suggestions. Preserve pin limits, ordering, adaptive behavior, and watch/widget propagation. Hide from Suggestions and Remove Habit remain distinct operations.

This amendment establishes the parent location and grouping. A detailed internal redesign of Quick Capture is future design work; the reference does not approve deleting, flattening, or silently changing its controls.

### AI Insights & Chat

Group explanation/plan and chat preferences under **Optional Cloud AI**, alcohol sharing under **Additional Sharing**, and explanatory content under disclosure rows. The reference's concise labels are Explanations & Plans, Chat About Insights, and Include Alcohol in AI Insights. Their accessible names and supporting copy must unambiguously identify each feature and its sharing impact.

Maintain independent consent values. On-device findings remain available when cloud AI is off. Alcohol sharing remains off by default under its existing policy; no preference migration may implicitly enable it. Cycle and other excluded local-only information remain excluded. AI provider/service unavailability, an off choice, and an authorization error are distinct states.

Before enabling a feature, preserve the complete current consent flow: recipient, data categories, purpose, frequency, exclusions, revocation, and any required acknowledgment. The mockup's local switch can change a synthetic value immediately; that behavior is **not** authorization to bypass native consent. Condensed disclosure copy in a design reference is not a legal-policy replacement. Retain full disclosures and policy links, and preserve existing revocation behavior.

Purple is scoped to AI meaning, particularly its leading icon. It does not color every Settings row or the whole Preferences screen.

### Reminders

Show the master **Allow Reminders** preference and a **Reminder Times** group containing Morning Sleep Reminder, Medication Reminders, and Daily Check-In. These routes open the same settings used by Sleep, Medications, and Daily Check-In. State that weekly check-in reminders also follow the master setting; do not invent a configurable weekly schedule without support from the app's existing behavior.

The master preference and OS notification permission are separate. The complete native design must show enabled/permitted, disabled, permission not requested, permission denied, unavailable, and scheduling-failure states distinctly. A permitted state is based on the actual OS result, not an optimistic toggle. Provide the existing OS settings recovery path when needed.

Turning the master off suppresses notifications while retaining schedules and daily check-in due times. Schedule summaries, if shown in the native design, use real localized times or explicit Off/Not Set states. Medication schedules may contain multiple times; do not fabricate one shared medication time or expose medication names in the hub. The existing editors remain responsible for saving and validation.

The new consolidated overview and contextual navigation are approved. Full permission-state layouts, schedule editing, and failure/retry presentation require detailed design and validation before implementation is complete.

### Appearance

Use the exact page name **Appearance**. Preserve System, Light, and Dark as one exclusive choice. System follows device appearance and is distinct from a user explicitly selecting Light or Dark. The root value shows the persisted preference; it does not infer that setting from the currently rendered palette. Both screenshot themes use System as an illustrative value.

Apply appearance changes consistently across the existing app surfaces. Preserve the canonical woven background and theme roles. Native dynamic type, reduced motion, accessibility appearance, and persistence must not depend on the fixed reference viewport.

### Your Progress

Keep the points, streaks, and badges preference separate from AI and health-goal findings. Preserve the current explanation that enabling it later scores only new logs rather than retroactively scoring earlier entries. This change introduces no clinical progress score, new reward system, or reset behavior.

### Health Connections

The hub label is **Health Connections**. Its destination names the actual platform provider: Apple Health on iOS or Health Connect on supported Android. Retain the complete existing optional connection, scoped permission, review-permissions, import, OS settings, and disconnect flow. The minimal reference is a placement/introductory layout, not a complete replacement for these controls.

Show connected, not connected, denied/partially permitted, syncing, failed, and unsupported states honestly. Respect What to Track import eligibility and existing cycle-data exclusions. Do not imply that Plectara writes diary records back to the health provider when the integration is read-only. Disconnect consequences must follow the existing data policy.

### Account & Privacy

Group Account identity and Sign-In Security under **Your Account**; Export My Data, Privacy Policy, and Terms of Use under **Your Information**; contextual AI Insights & Chat and Health Connections routes under **Privacy Controls**. Put Log Out and Delete Account in a final action group with explicit full-width buttons. Root summaries do not show email or other identifying data.

Provider-managed sign-in security must be described accurately and must not imply an editable Plectara two-factor switch. Preserve the export preview/scope and native share behavior, cancellation, errors, and user feedback. Export and deletion stay distinct.

Delete Account keeps the existing confirmation and scope: explain the affected account/device data, other accounts on the device, existing exports, and irreversibility. Never use a normal navigation row as immediate deletion. Preserve sign-out behavior separately. The reference buttons only display a preview message; production requires the actual established flows.

Development seeding and scenario imports belong in a debug-only developer area and are omitted from these production references.

## Visual specification

The approved references extend the current woven app language without redefining global tokens. Use [Cards](../02-design/cards.md), [Buttons](../02-design/buttons.md), [Dark Mode & Accessibility](../02-design/dark-mode.md), and the existing app shell. Preferences has an opaque grouped-list layout over the canonical continuous yarn artwork.

| Element | Reference geometry / treatment |
| --- | --- |
| Export surface | 393 × 852 logical units at 3×; illustrative status/home indicators, not native safe-area constants |
| Header | Existing protected ink gradient, 60-unit toolbar, 22-unit medium page title, copper rule fading at the ends |
| Back | 44 × 44 target, protected ink backing, 12 radius; native platform glyph/behavior in implementation |
| Body | 12-unit horizontal gutters; 10 top inset; 12 between panels; content scrolls vertically |
| Group panel | Opaque theme surface; 14 radius; 1 decorative outline; 14 horizontal inset; 12 top / 3 bottom around root lists |
| General reading panel | 14 padding and radius; no additional nested framed cards |
| Section heading | 12/18, weight 500, theme link role; Title Case |
| Row | Whole-row target; minimum 56 logical units in reference, expanding naturally for text; 12 vertical padding, 10 icon/text gap |
| Row title | 15/21.75, weight 500; complete readable label |
| Row summary/value | 12/18, weight 400, supporting-text role; summary 3 below title |
| Leading icon | 21 in a 34 × 34 backing, 10 radius; shared teal/jade family, purple only for AI |
| Section-introduction icon | 22 in a 38 × 38 backing, 11 radius |
| Row rule | Thin decorative neutral/light or quiet slate/dark internal separator; not a separate box around every row |
| Chevron | 16-unit decorative trailing indicator; belongs to the whole-row target |
| Action buttons | Minimum 48 height, 9 radius, full width; 12 gap; End/Delete attention styling retains explicit label |
| Switch | Reference visual track 46 × 28; entire labeled row is the interaction target; native accessible switch in production |
| Appearance choices | Exclusive native radio/selection group, minimum 58-unit rows in reference |

| Role | Light | Dark |
| --- | --- | --- |
| Opaque reading surface | `#FAF8F4` | `#192D38` |
| Primary text | `#192D38` | `#FAF8F4` |
| Supporting text | `#506F7E` | `#B8CBCB` |
| Link / section heading | `#206668` | `#8DC7B7` |
| Decorative panel outline | `#D8DEDA` | `#C88764` |
| Internal row separator | `#D8DEDA` | `#45616A` |
| Neutral control | `#F1F0EC` | `#264C4B` |
| Required control outline | `#567788` | `#8DA4A6` |
| Primary / foreground | `#287E80` / white | `#76B7A5` / `#192D38` |
| Icon backing / icon | `#E9F1ED` / `#206668` | `#24423F` / `#8DC7B7` |
| AI backing / icon | `#F0ECF8` / `#6748D8` | `#263146` / `#B7A7FF` |
| Attention foreground | `#845800` | `#E5B86A` |

Reuse existing native token adapters where available. Icon backing, AI backing and the quiet separator now resolve through the shared `component.iconBacking`, `component.aiBacking`, and `component.quietDivider` registry and its generated CSS/Flutter exports. These are the same approved shades used by Insights; consuming-app adoption remains pending. The reference uses consistent Lucide outline metaphors; native implementation maps them through the app's shared icon layer, preserving recognizability, weight, and optical size. Header/status glyphs and simulated home indicator are reference chrome, not replacements for OS UI.

## Accessibility and adaptive behavior

- Use semantic group headings, native navigation controls, switches, exclusive choices, and disclosure states. Leading icons and chevrons are decorative when the row label provides meaning.
- Keep at least 44 pt effective targets on iOS and 48 dp on Android. A 28-unit switch graphic is not its complete hit target. Group headers are not unlabeled buttons.
- Rows, descriptions, values, and buttons expand for large text and localization. Move a trailing value below its label when needed. Never clip a title, consent condition, or destructive-action consequence to preserve a one-screen composition.
- Maintain vertical scroll with native safe-area clearance. The backdrop may continue behind content, but reading panels remain opaque. Preserve reduced-transparency/quiet appearance support.
- Restore scroll and focus appropriately. Announce actual state changes and failures without reannouncing the whole Preferences page. Do not announce synthetic screenshot values as current account state.
- Maintain required text/control contrast and visible focus. Selection, consent, enabled state, and errors use text/native semantics as well as color.
- Test 320-unit widths, 200% text, VoiceOver/TalkBack, keyboard navigation, safe areas, long labels, and platform back before release. The reference is not certification of those native behaviors.

## State and scope matrix

| State or boundary | Required behavior |
| --- | --- |
| No goals or saved items | Keep root/collection route; existing select/add paths remain available |
| Optional tracker disabled | Hide only applicable inner rows under existing rules; keep What to Track reachable; preserve saved records |
| Cycle unavailable | Do not expose Cycle Settings or imply eligibility; preserve local-only handling when available |
| Data loading / error | Keep layout and route meaningful; do not label unknown values Off or empty |
| Cloud AI disabled / unavailable | Keep local findings available; separate user choice from service state and authorization errors |
| OS notifications denied | Show real permission state and recovery; retain schedules; do not claim reminders will deliver |
| Health integration unavailable | Explain platform/support limitation; keep manual logging available |
| Account export canceled / failed | Preserve data and distinguish cancellation, unavailable share, and failure |
| Delete/sign-out canceled | Remain in account context and preserve the account/data |
| Debug build | Developer tools remain separately labeled and absent from production builds |
| Existing editor routes | Reuse current form behavior; no new input fields or destructive semantics implied by navigation screenshots |

## Acceptance criteria

| ID | Reviewable requirement |
| --- | --- |
| PO-01 | Preferences uses Section Hub with nine destinations and exact Your Health, Settings, Connections & Account groups |
| PO-02 | All 22 original root destinations and existing nested controls are mapped; no settings are dropped |
| PO-03 | Light/Dark Modes, Notifications, Health Apps, and AI Insights receive their approved new navigation labels with preserved underlying identity |
| PO-04 | Whole-row navigation and native Back preserve caller, root/section scroll, focus, and existing form save/cancel semantics |
| PO-05 | Conditional Beverages, bowel, and cycle rows follow real eligibility; missing records do not hide configuration entry points |
| PO-06 | Saved items, activity categories, widget pins, and learned habits retain distinct meanings and existing behavior |
| PO-07 | Reminders uses one master preference and the same schedules as Sleep, medications, and check-ins; OS permission remains separate |
| PO-08 | AI choices remain independent and require complete existing consent before native enablement; local-only exclusions remain enforced |
| PO-09 | Your Progress remains logging rewards, separate from AI and health-outcome evidence |
| PO-10 | Account identity/security, export, policies, sign-out, and deletion remain accessible with accurate scope and confirmations |
| PO-11 | Root summaries do not expose health measurements, medications, diagnosis names, or account identity |
| PO-12 | Both themes retain canonical artwork, opaque panels, typography, spacing, semantic roles, and expandable native targets |
| PO-13 | Native large text, localization, assistive technology, permission states, error recovery, and platform-specific connections are validated |
| PO-14 | Production uses real state; reference switches, inactive editor rows, simulated chrome, and preview messages are not copied as implementation |

## Integration and remaining design work

Implement navigation mapping and aliases before removing old entry points. Reuse the existing preferences stores, editors, permissions, account services, and consent flows. Update any in-app instructional path text that still points directly to Preferences → Sleep, Medications, or Daily Check-In so it agrees with the new hierarchy or contextual shortcuts.

Section Hub organization is approved. Detailed Quick Capture internals, the full reminder permission/scheduling states, full health-connection states, form-specific presentation, and final consent-disclosure treatment still need their own design/implementation review. Existing behavior governs until those changes are separately designed. This specification does not mark those details complete solely because a screenshot exists.

Editable reference sources, the selected-layout decision, source inventory, and the historical two-option study live in `tooling/preferences-reference/`. The paired gallery contains only Section Hub and its section references. The owner approved publication of this PL-OS documentation amendment to main on October 27, 2026. Application implementation, application deployment, and a tagged release remain separate work.

## Version History

- 2026-10-27: Records the owner-selected Section Hub, Settings heading, complete destination migration, preserved behavior, paired references, and scoped native acceptance requirements. Detailed specification and publication to main approved after local review.
