# Flutter theme integration

Use `assets/flutter/plectara_colors.dart` as the source adapter. Apply colors to the existing theme rather than replacing its component geometry.

```dart
import 'plectara_colors.dart';

ThemeData applyPlectaraColors(ThemeData existing) {
  final dark = existing.brightness == Brightness.dark;
  final colors = existing.colorScheme.copyWith(
    primary: dark ? PlectaraDarkColors.primary : PlectaraLightColors.primary,
    onPrimary: dark ? PlectaraDarkColors.onPrimary : PlectaraLightColors.onPrimary,
    surface: dark ? PlectaraDarkColors.surface : PlectaraLightColors.surface,
    onSurface: dark ? PlectaraDarkColors.text : PlectaraLightColors.text,
    onSurfaceVariant: dark
        ? PlectaraDarkColors.textSecondary : PlectaraLightColors.textSecondary,
    outline: dark ? PlectaraDarkColors.border : PlectaraLightColors.border,
    error: dark ? PlectaraDarkColors.critical : PlectaraLightColors.critical,
  );
  return existing.copyWith(
    colorScheme: colors,
    scaffoldBackgroundColor: dark
        ? PlectaraDarkColors.background : PlectaraLightColors.background,
    focusColor: dark ? PlectaraDarkColors.focus : PlectaraLightColors.focus,
  );
}
```

This is an integration example, not an app runtime in this repository. Audit explicit color overrides in existing buttons, fields, cards, and chart components; `copyWith` does not replace those overrides. Use the theme-specific hover, border, link, AI, and state roles without changing component shape or behavior. Consuming apps must run their own Flutter tests.
