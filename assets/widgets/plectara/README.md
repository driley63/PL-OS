# Plectara capture widget kit

Status: Owner-approved design reference, 2026-09-28

Design review: Revision 13
PL-OS bundle: Prepared v2.5.0

Start with the bundled [specification](specification.md), or the canonical [Widget Visual Specification](https://pl-os.plectara.com/specs/02-design/capture-widget-visuals/) after publication. The design uses full-widget yarn, a horizontal shaded logo region, a soft copper divider, a mint light card, and a transparent dark card with a copper outline. Light Capture and Sleep match in teal/white. Quick buttons use title case. There is no Edit action.

## File map

| Folder/file | Use |
| --- | --- |
| `textures/plectara-widget-yarn-gentle-focus-v1.png` | Exact full resolution edited source, 1422 × 1106 |
| `textures/plectara-widget-yarn-gentle-focus-v1.webp` | Exact 900 × 700 image embedded in the approved browser mockup |
| `previews/home-{small,medium,large}-{light,dark}.png` | Six individual 2× screenshots with transparent outside corners |
| `previews/overview-{light,dark}.png` | Complete review sheets |
| `previews/lock-screen-accessories.png` | Illustrative accessory concepts in phone context |
| `logos/` | Exact canonical reversed/monochrome logo copies for this component |
| `fonts/` | Inter variable font and its SIL Open Font License |
| `source/` | Approved original-focus working image, earlier approval record, edit prompts, crop/color records, and provenance |
| `reference/approved-widgets.html` | Standalone browser reference; illustrative controls create no records |
| `reference/approved-mockup-fragment.html` | Exact editable source of the approved in-conversation design |
| `widget-visual-tokens.json` | Widget-local theme roles, typography, reference geometry, gradients, and image placement |
| `verification/browser-review.json` | Current rendered checks and identified earlier header evidence |
| `manifest.json` | File roles, image dimensions, and SHA-256 checksums |

## Implementation

Use real text and native controls above the texture. Do not ship a flattened screenshot as the widget. Default to system appearance and support the platform's background removal and tint modes. The screenshots' canvas dimensions and outside radius are illustrative; actual host margins and masks take precedence. Remove optional content before shrinking text or targets.

`widget-visual-tokens.json` is a component contract, not a replacement for global palette or spacing tokens. Inter's license is bundled. The standalone reference also embeds Lucide under its bundled license in `reference/LUCIDE-LICENSE` and retains the visualization renderer's shell. It is a browser reference, not a WidgetKit or Android implementation.

## Artwork and source

Use the supplied gentle-focus texture without regenerating it. The WebP is byte-identical to the approved embedded texture. The native PNG and delivery WebP are different encodings; the original-focus working PNG is retained for provenance, not as the default background. See [provenance](source/provenance.md).

The original unmodified photograph remains in the internal source archive. This package distributes the modified Plectara design assets and source records for component implementation, not an unmodified stock-photo collection. The separate header-only fallback remains in the earlier review archive and is not the current production direction.

## Review limits

Browser text/icon contrast and layout measurements are bounded to these references. Native rendering, text scaling, VoiceOver/TalkBack, system appearances, and real-device behavior need implementation testing. This kit does not certify ADA compliance or establish that the native app already implements these designs.

## Package maintenance

The canonical specification lives in `docs/specs/02-design/capture-widget-visuals.md`. After changing approved inputs, run `python tooling/build-capture-widget-kit.py` from the repository root. It refreshes the bundled specification, manifest, ZIP, and documentation asset copies. Screenshot and artwork regeneration require a separate visual review; this command preserves the saved images.
