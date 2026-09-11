# PL-OS v2.2.0 — Liquid Glass iOS icon downloads

Date: 2026-09-11
Status: Owner-approved direction; publication through the repository's automatic deployment
Change class: Minor — additive platform artwork and brand guidance

## What changes

Plectara now has an editable native Liquid Glass iOS icon. Seven SVG layers preserve the approved woven figure, jade head, ribbon palette, original placement, and six-unit separation channels. Apple supplies the material rendering, highlights, and depth.

The [brand kit gallery](../../specs/01-brand/plectara-brand-kit.md#liquid-glass-ios-icons) presents default, dark, clear light/dark, and tinted light/dark appearances. Each appearance has an individual 1024 px PNG download. The [iOS package](../../assets/brand/plectara-ios-liquid-glass.zip) includes the `Plectara.icon` source, seven SVG layers, and 18 native previews: six appearances at 1024 px, 60 pt at 3×, and 20 pt at 3×. The complete brand ZIP also includes these assets.

The owner approved the six-appearance concept on 2026-09-11. Production files use the original vectors and Apple's native renderer. The generative concept board is a review artifact; it is not substituted for production artwork.

## Usage and migration

Use `Plectara.icon` in the iOS application target and set the target's App Icon name to `Plectara`. Native previews are static communication/review images with transparent outer corners; they are not replacement asset-catalog inputs. Clear previews are flattened, while the native icon supplies system-dependent material behavior. Home Screen tint remains the device owner's choice.

Full-color source artwork retains the jade head. Clear and tinted system modes may render the complete figure monochromatically. This is a platform-specific treatment; flat website, document, in-app, and wordmark assets retain their existing rules. The legacy iOS catalog remains available.

This release publishes the assets in PL-OS. Updating the shipping Plectara app is a separate consumer integration, including checks on supported OS versions, devices, wallpapers, and accessibility settings.

## Validation

Apple's Icon Composer renderer produces the previews directly from the native document. The brand validator checks that all seven layers preserve the original paths and transforms, are unmasked, and contain no baked material effects. It also verifies document references, source and rendered-file checksums, PNG dimensions and corner transparency, both ZIP packages, and site-copy equality. The documentation must pass its strict build and the gallery is reviewed visually before publication.

See the [verification record](verification.md), [release manifest](manifest.json), [Logo Usage](../../specs/01-brand/logo-usage.md), and [Apple's Icon Composer guide](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer).
