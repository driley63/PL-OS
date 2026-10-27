# Approved Insights reference sources

The October 27 design was approved for PL-OS documentation. This folder preserves
the approved layout and its deterministic screenshot scenes. It does not implement
the Plectara Flutter app, health inference, persistence, synchronization, or AI.

## Source and generated files

- `journey.js` and `styles.css`: approved content hierarchy, goal-specific footer
  text and outlined plan-management buttons, with the October 27 final consistency
  corrections for the existing app shell and semantic component roles.
- `native-chrome-icons.json`: Material icon code points from the current Flutter
  app shell. These apply to navigation and header controls; approved goal icons
  remain distinct. The local WOFF is a subset of Flutter's Material Icons font.
- `goal-catalog.json`: fixed goal labels, native keys, and approved icon meanings.
- `scenes.json`: named review states and scroll positions, repeated in both themes.
- `reference.html`: app-only capture surface, rendered at 3x by default. A `scale=1`
  query option provides a logical-size interactive inspection surface.
- `gallery.html`: paired screenshot viewer template, separate from the app UI.
- `history/`: the superseded local October 25 written specification and exact
  approved source before consistency corrections. Earlier PNGs,
  Flutter scene sources, and the prior gallery remain intact in their old locations.

Public output is `docs/assets/app/insights-presentation/approved-2026-10-27/`;
the current gallery entry point is `docs/assets/app/insights-presentation/index.html`.

## Rebuild and capture

1. Run `python3 tooling/build-insights-journey-reference.py` to package the source.
2. Serve `docs/` on loopback. For every scene ID and theme, open
   `/assets/app/insights-presentation/approved-2026-10-27/reference.html?scene=ID&theme=light`
   (or `dark`) through the browser. The query fixture initializes the reviewed state;
   browser storage and conversation controls are not used.
3. Wait for `html[data-capture-ready="true"]`. Inspect the DOM/accessibility state,
   loaded images, generated SVG icons, and main-content horizontal overflow.
4. Capture the `.phone` bounds through the browser's full-page screenshot API.
   At the default scale these are x=0, y=0, width=1179, height=2556. Save the original
   bytes as `screens/ID-THEME.png`; do not resize, upscale, retouch, or screenshot a
   chat/documentation page. Record bounds, actual main scrollTop, image readiness,
   icon count, and overflow in `capture-observations.json`.
5. Run `.venv/bin/python tooling/package-insights-journey.py`. It verifies dimensions,
   records checksums, creates the gallery, and updates the marked image block in the
   written specification. This does not take screenshots or invent capture evidence.
6. Build PL-OS strictly, inspect the served specification and gallery, and validate
   dependent asset packaging before proposing release. Pushing requires separate
   user approval.

Run `.venv/bin/python tooling/audit-insights-reference.py --app PATH_TO_PLECTARA`
for current goal/geometry verification and independent PL-OS role/contrast checks.
The packaged font, script, and stylesheet URLs include content hashes. Retake
captures after source or asset changes; font readiness alone cannot detect a stale
cached font missing newly added glyphs. Verify selected goal chips are visible at
the actual export scale, as well as at logical size.

The PNGs are browser rasterizations at 3x, not resampled thumbnails. Cropping removes
only surrounding browser/review context; the app header, scroll viewport, and bottom
navigation remain. The capture-only surface removes the decorative outer phone mask
and scrollbars. It does not change the approved card, typography, or content design.

## Fixtures and licenses

Approved reference numbers carry forward the earlier simulator walkthrough; unknown
prior denominators remain explicitly unavailable. Plan timing, chat response, and
state variations are design examples. They must never seed production data or define
clinical rules.

The source package includes local Inter 400/500/600/700 WOFFs and its OFL, a Material
Icons chrome subset with its Apache license, Lucide 1.17.0 with its
upstream license, and the approved Health Icons stomach SVG with the upstream
license. The stomach optical adaptation is the existing approved asset; its source
coordinates were not regenerated. Canonical Plectara yarn and logo are referenced
from the existing app asset package. The icon libraries' metadata names describe the
visual references; native integration should use the existing shared icon system.

Upstream source URLs:

- https://unpkg.com/lucide@1.17.0/dist/umd/lucide.js
- https://unpkg.com/lucide@1.17.0/LICENSE
- https://healthicons.org/icons/svg/outline/body/stomach.svg
- https://raw.githubusercontent.com/resolvetosavelives/healthicons/main/LICENSE
