# Plectara Android icons — PL-OS v2.3.0

Owner-approved on September 11, 2026. This package contains the native Android resources and editable SVG sources for the approved adaptive icon.

The woven figure is uniformly enlarged about 13% from the previous Android foreground and repositioned for optical balance. The original ribbon paths, gaps, circular head, and full-color palette are preserved. All foreground artwork remains inside a 32 dp radius on the 108 dp canvas, leaving 1 dp inside the central safe circle.

## Contents

| Path | Use |
| --- | --- |
| `res/drawable/plectara_foreground.xml` | Full-color VectorDrawable with the jade head and original ribbon colors |
| `res/drawable/plectara_monochrome.xml` | Matching opaque white silhouette for system theming |
| `res/values/plectara_colors.xml` | Opaque ink background |
| `res/mipmap-anydpi-v26/` | Standard and round adaptive icon definitions for Android 8+ |
| `res/mipmap-anydpi-v33/` | Standard and round definitions with a monochrome layer for Android 13+ |
| `res/mipmap-{density}/` | Standard and round legacy PNG icons at 48, 72, 96, 144, and 192 px |
| `source/` | Unmasked SVG foreground, monochrome, and background |
| `previews/svg/` | 21 shape/appearance examples as SVG |
| `previews/png/` | The same 21 examples at 1024, 192, and 48 px |
| `asset-manifest.json` | Source provenance, placement, dimensions, and per-file SHA-256 checksums |

The three illustrated shapes are circle, squircle, and rounded square. Each is shown in full color and six themed examples: jade, clay, and slate in light and dark appearances. Theme colors and masks are illustrative. Android and the launcher determine the actual theme colors, mask, and supported effects. These are vector-based previews, not device screenshots.

## App integration

1. Replace the app's matching launcher resources with this package's `res/` files, resolving existing resource definitions first.
2. Remove old density-specific `plectara_foreground.png` files when adopting the vector of the same name. Otherwise a density bitmap can override the vector. Do not retain duplicate names in the same resource configuration.
3. Keep the manifest references `android:icon="@mipmap/ic_launcher"` and `android:roundIcon="@mipmap/ic_launcher_round"`.
4. Compile with Android API 33 or newer for the monochrome element. Versioned resources retain the foreground/background definition on Android 8–12; legacy PNGs cover earlier versions.
5. Review launcher masks, light/dark themed icons, supported OS versions, and small-size rendering in the consuming app.

Use the unmasked XML resources for adaptive icons. Rounded preview PNGs are for presentations and design review. Do not bake preview tints, masks, or shadows into the native foreground. No app-store listing asset or shipping app is changed by this PL-OS publication.

## Regeneration

Run `python tooling/build-plectara-brand.py` from PL-OS with `tooling/requirements-brand.txt` installed. The brand build invokes `tooling/build-plectara-android.py`, updates source/PNG copies, removes the five superseded foreground bitmaps, and refreshes both Android and complete brand-kit downloads. Then run `python tooling/validate-brand.py`.

References: [Android adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive) and [VectorDrawable](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable).
