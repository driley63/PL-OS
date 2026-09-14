# Flutter theme integration

Use `assets/flutter/plectara_colors.dart` as the source adapter. Apply colors to the existing theme rather than replacing its component geometry.

```dart
import 'package:flutter/material.dart';
import 'plectara_colors.dart';

ThemeData applyPlectaraColors(ThemeData existing) {
  final dark = existing.brightness == Brightness.dark;
  final colors = existing.colorScheme.copyWith(
    primary: dark ? PlectaraDarkColors.primary : PlectaraLightColors.primary,
    onPrimary: dark ? PlectaraDarkColors.onPrimary : PlectaraLightColors.onPrimary,
    primaryContainer: dark ? PlectaraDarkColors.selected : PlectaraLightColors.selected,
    onPrimaryContainer: dark ? PlectaraDarkColors.text : PlectaraLightColors.text,
    secondary: dark ? PlectaraDarkColors.link : PlectaraLightColors.link,
    onSecondary: dark ? PlectaraDarkColors.onPrimary : PlectaraLightColors.onPrimary,
    secondaryContainer: dark ? PlectaraDarkColors.selected : PlectaraLightColors.selected,
    onSecondaryContainer: dark ? PlectaraDarkColors.text : PlectaraLightColors.text,
    tertiary: dark ? PlectaraDarkColors.info : PlectaraLightColors.info,
    onTertiary: dark ? PlectaraDarkColors.onPrimary : PlectaraLightColors.onPrimary,
    tertiaryContainer: dark ? PlectaraDarkColors.surfaceMuted : PlectaraLightColors.surfaceMuted,
    onTertiaryContainer: dark ? PlectaraDarkColors.text : PlectaraLightColors.text,
    surface: dark ? PlectaraDarkColors.surface : PlectaraLightColors.surface,
    onSurface: dark ? PlectaraDarkColors.text : PlectaraLightColors.text,
    onSurfaceVariant: dark
        ? PlectaraDarkColors.textSecondary : PlectaraLightColors.textSecondary,
    outline: dark ? PlectaraDarkColors.border : PlectaraLightColors.border,
    outlineVariant: dark ? PlectaraDarkColors.divider : PlectaraLightColors.divider,
    error: dark ? PlectaraDarkColors.critical : PlectaraLightColors.critical,
    onError: dark ? PlectaraDarkColors.onPrimary : PlectaraLightColors.onPrimary,
    errorContainer: dark ? PlectaraDarkColors.surfaceMuted : PlectaraLightColors.surfaceMuted,
    onErrorContainer: dark ? PlectaraDarkColors.text : PlectaraLightColors.text,
    inverseSurface: dark ? PlectaraLightColors.surface : PlectaraDarkColors.surface,
    onInverseSurface: dark ? PlectaraLightColors.text : PlectaraDarkColors.text,
    inversePrimary: dark ? PlectaraLightColors.link : PlectaraDarkColors.link,
    // Keep elevated Material surfaces on checked roles; verify any later tint.
    surfaceDim: dark ? PlectaraDarkColors.background : PlectaraLightColors.background,
    surfaceBright: dark ? PlectaraDarkColors.surfaceMuted : PlectaraLightColors.surface,
    surfaceContainerLowest: dark ? PlectaraDarkColors.background : PlectaraLightColors.surface,
    surfaceContainerLow: dark ? PlectaraDarkColors.surface : PlectaraLightColors.surface,
    surfaceContainer: dark ? PlectaraDarkColors.surface : PlectaraLightColors.surface,
    surfaceContainerHigh: dark ? PlectaraDarkColors.surfaceMuted : PlectaraLightColors.surfaceMuted,
    surfaceContainerHighest: dark ? PlectaraDarkColors.surfaceMuted : PlectaraLightColors.surfaceMuted,
    surfaceTint: Colors.transparent,
  );
  return existing.copyWith(
    colorScheme: colors,
    scaffoldBackgroundColor: dark
        ? PlectaraDarkColors.background : PlectaraLightColors.background,
  );
}
```

This is an integration example, not an app runtime in this repository. Audit explicit color overrides in existing buttons, fields, cards, and chart components; `copyWith` does not replace those overrides. Use the theme-specific hover, border, link, AI, and state roles without changing component shape or behavior. Consuming apps must run their own Flutter tests.

Import `package:flutter/material.dart` alongside the adapter. Preserve the existing component geometry while updating these required overrides:

| Flutter component | Mapping to check |
| --- | --- |
| `InputDecorationTheme` | `hintStyle` → `textSecondary`; fill → `surface` or `surfaceMuted`; enabled boundary → `border`; error and focused-error borders → current `critical` |
| `RadioThemeData` / checkbox / switch | Resolve selected color from the current theme's `primary`; keep `onPrimary` for marks on a filled primary background |
| Buttons | Resolve foreground and background together, including hover, pressed, focus, and disabled states; `onPrimary` also pairs with the specified `ai` and `critical` fills |
| Status badges | Resolve success/warning/critical/info by brightness; use a tested opaque surface or measure the actual tint |
| Charts | Resolve the [semantic chart roles](../../02-design/dark-mode.md#charts-and-health-data), including labels and non-color distinctions |
| Focus | `ThemeData.focusColor` is a Material state color, not a guarantee of an accessible focus outline; verify the actual focused component |

Do not use the legacy `LifestyleIQColors.background`, `surface`, or `text` aliases in dark components: those aliases point to light values. Keep System/Light/Dark behavior in the app's theme controller. The [dark mode standard](../../02-design/dark-mode.md) defines the full contract and release checks.
