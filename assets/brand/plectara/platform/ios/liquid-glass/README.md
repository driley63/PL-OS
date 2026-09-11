# Plectara Liquid Glass iOS icons

Version: 2.2.0 · Direction approved: September 11, 2026

This package translates the approved woven figure into native Liquid Glass. The original vector outlines, jade head, full-color ribbon palette, placement, and separation channels are preserved. Apple applies lighting and material effects at rendering time.

## Choose a file

| File or folder | Use |
| --- | --- |
| `Plectara.icon/` | Editable Icon Composer document; use this for the iOS app |
| `layers/` | Seven unmasked 1024 × 1024 SVG layers with transparent backgrounds |
| `previews/*-1024.png` | Six native rendered PNG previews for design review and communications |
| `previews/*-180.png` | Home Screen previews, rendered at 60 pt and 3× |
| `previews/*-60.png` | Notification-size previews, rendered at 20 pt and 3× |
| `render-manifest.json` | Renderer version, export settings, and SHA-256 checksums |

## Add to the iOS app

1. Extract the download and open `Plectara.icon` in Icon Composer to inspect its layers and appearances.
2. Add the entire `Plectara.icon` document to the iOS application target in Xcode.
3. In the target's General settings, set App Icons and Launch Screen → App Icon to `Plectara` (without `.icon`).
4. Build and check the Home Screen, Settings, and notifications on the supported iOS versions and devices. Check light, dark, clear, and tinted appearances, multiple wallpapers, and accessibility settings.

Do not substitute the rounded preview PNGs for the native icon document. They are static renders with transparent outer corners; the icon artwork inside the tile is flattened. In particular, a clear-mode PNG does not dynamically refract a wallpaper. Native `.icon` rendering supplies the system behavior. The separate legacy `AppIcon.appiconset` in the complete brand kit remains available for older workflows.

Default and dark preserve the full-color source figure. A white fill specialization gives all seven layers consistent luminance for Apple's monochrome/tinted rendering, improving ribbon visibility without modifying their outlines. The jade tint shown in previews is an example; people choose their Home Screen tint. Actual lighting, background treatment, and translucency vary with the OS and appearance settings.

## Material and brand rules

The source document uses a solid ink background and one group of seven independently rendered foreground layers. The group uses 15% translucency and 20% neutral shadow, with native specular effects enabled. The SVGs contain no baked lighting, blur, shadows, or corner mask.

This is an approved platform treatment for app icons. Keep the existing flat master logos for documents, websites, and in-app branding. Preserve the custom wordmark and six-unit ribbon channels; do not redraw or independently recolor strands. Full-color artwork keeps the jade head. System-managed clear and tinted appearances may render the complete figure monochromatically.

## Rebuild

On a Mac with Xcode and Icon Composer installed, run from the PL-OS repository root:

```sh
python tooling/build-plectara-brand.py --render-ios
python tooling/validate-brand.py
python -m mkdocs build --strict
```

Install `tooling/requirements-brand.txt` first. Icon Composer must be available at the standard Xcode location and its first-run license accepted. Builds without `--render-ios` reuse the checked-in native previews and repackage downloads, so the documentation site can build on Linux.

The previews were checked with Apple's renderer and the vector/package validator. Integration into the shipping Plectara application is a separate consumer change; this PL-OS release does not assert a device or App Store build test.

Apple references: [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) and [App icon design guidelines](https://developer.apple.com/design/human-interface-guidelines/app-icons).
