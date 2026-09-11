# PL-OS v2.3.0 — Adaptive Android icon downloads

Date: 2026-09-11
Status: Owner-approved artwork; publication through the repository's automatic deployment
Change class: Minor — Android platform assets and integration guidance

## What changes

Plectara's Android icon now uses a native vector foreground and a dedicated monochrome silhouette for themed home screens. The owner approved the full-color and themed preview set on September 11, 2026. The figure is uniformly enlarged approximately 13% and repositioned for optical balance; all six ribbon paths, the circular head, original colors, and six-unit separation channels are preserved.

The [Android gallery](../../specs/01-brand/plectara-brand-kit.md#adaptive-android-icons) shows circle, squircle, and rounded-square examples in full color and six light/dark themes. Each of the 21 combinations has an SVG preview and PNGs at 1024, 192, and 48 px. Theme colors and masks are illustrative rather than device screenshots.

The [Android download](../../assets/brand/plectara-android-icons.zip) includes the native color/monochrome VectorDrawables, opaque ink background, standard and round adaptive resources, ten legacy PNGs across five densities, three unmasked SVG sources, previews, usage notes, and a per-file manifest. The complete brand kit includes the same assets. Android-specific canonical foreground sources and PNG exports are updated; flat logo, wordmark, iOS, and store artwork retain their prior design.

| Before | After |
| --- | --- |
| Five density-specific foreground PNGs | One native color vector plus a matching monochrome vector |
| Smaller figure positioned higher in the tile | Owner-reviewed 13% uniform increase and balanced placement |
| Foreground/background adaptive definition | Standard and round definitions, with a monochrome layer on Android 13+ |
| Android resources available inside the full brand kit | Dedicated Android download and 21 appearance examples in the gallery |

## Consumer migration

Use the native `res/` resources in the app and replace any previous definitions of the same resource names. Remove the old density-specific `plectara_foreground.png` files so they cannot override the vector. The package provides versioned adaptive definitions for Android 8+ and monochrome definitions for Android 13+, plus legacy PNGs. Compile against API 33 or newer for the monochrome element.

The launcher chooses the final icon mask and theme colors. Do not use the masked or tinted preview images as adaptive foreground layers. Preserve the native unmasked layers and ink background. Review actual launchers, supported OS versions, and small-size rendering when integrating into the shipping application.

This release publishes assets in PL-OS; it does not change the shipping Plectara app or its store listing.

## Validation

The brand validator checks original geometry and fills, identical color/monochrome placement, the approved transform, central safe-circle clearance, resource references, all legacy densities, preview dimensions and alpha, per-file checksums, archive contents, and documentation copies. Native Android resources are also compiled and linked with AAPT2, and the documentation passes its strict build.

See the [verification record](verification.md), [release manifest](manifest.json), and [logo usage](../../specs/01-brand/logo-usage.md).
