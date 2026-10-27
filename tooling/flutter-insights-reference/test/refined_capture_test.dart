import 'dart:io';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:health_diary/theme/app_theme.dart';
import 'package:health_diary/widgets/select_chip.dart';

import '../reference_scene.dart';
import '../refined_insights.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('Review goal-driven Insights hierarchy', (tester) async {
    tester.view.physicalSize = const Size(1179, 2556);
    tester.view.devicePixelRatio = 3;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.runAsync(() async {
      final font = FontLoader('Inter')
        ..addFont(rootBundle.load('assets/fonts/Inter-Regular.ttf'));
      await font.load();
      final icons = FontLoader('MaterialIcons')
        ..addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'));
      await icons.load();
    });
    Future<void> capture(GlobalKey key, String name) async {
      expect(tester.takeException(), isNull);
      await tester.runAsync(() async {
        final boundary =
            key.currentContext!.findRenderObject() as RenderRepaintBoundary;
        final image = await boundary.toImage(pixelRatio: 3);
        final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
        File('${Platform.environment['PLECTARA_REFERENCE_OUTPUT']!}/$name.png')
            .writeAsBytesSync(bytes!.buffer.asUint8List());
        image.dispose();
      });
    }

    for (final dark in [false, true]) {
      final key = GlobalKey(), theme = dark ? 'dark' : 'light';
      await tester.pumpWidget(
        referenceApp(
          screen: 'insights-refined',
          brightness: dark ? Brightness.dark : Brightness.light,
          boundary: key,
        ),
      );
      await tester.runAsync(() async {
        await Future<void>.delayed(const Duration(milliseconds: 400));
      });
      await tester.pumpAndSettle();
      expect(find.text('Better Sleep'), findsOneWidget);
      expect(find.text('Hydration'), findsNothing);
      expect(find.text('More Filters'), findsNothing);
      expect(
        Scrollable.of(
          tester.element(find.byKey(const ValueKey('log-filter-Beverages'))),
        ).position.maxScrollExtent,
        greaterThan(0),
      );
      expect(
        tester
            .getSize(find.byKey(const ValueKey('profile-goal-selector')))
            .height,
        greaterThanOrEqualTo(44),
      );
      await capture(key, 'insights-refined-$theme');
      await tester.tap(find.byKey(const ValueKey('profile-goal-selector')));
      await tester.pumpAndSettle();
      expect(find.text('More Energy'), findsOneWidget);
      expect(find.text('Better Digestion'), findsOneWidget);
      expect(find.text('Fewer, Milder Symptoms'), findsOneWidget);
      await capture(key, 'insights-goals-$theme');
      await tester.tap(find.text('More Energy'));
      await tester.pumpAndSettle();
      expect(find.text('No findings for this goal yet.'), findsOneWidget);
      await tester.tap(find.byKey(const ValueKey('profile-goal-selector')));
      await tester.pumpAndSettle();
      await tester.tap(find.text('Better Sleep'));
      await tester.pumpAndSettle();
      final beverageFilter = find.byKey(const ValueKey('log-filter-Beverages'));
      await tester.ensureVisible(beverageFilter);
      await tester.tap(beverageFilter);
      await tester.pumpAndSettle();
      expect(find.text('1 Finding · Updated 4:15 PM'), findsOneWidget);
      expect(find.text('A little more rest'), findsNothing);
      expect(find.text('Better Sleep'), findsOneWidget);
      expect(tester.widget<SelectChip>(beverageFilter).selected, isTrue);
      await tester.tap(find.byKey(const ValueKey('log-filter-Sleep')));
      await tester.pumpAndSettle();
      expect(find.text('2 Findings · Updated 4:15 PM'), findsOneWidget);
      final allTypes = find.byKey(const ValueKey('log-filter-All Log Types'));
      await tester.ensureVisible(allTypes);
      await tester.tap(allTypes);
      await tester.pumpAndSettle();
      expect(tester.widget<SelectChip>(allTypes).selected, isTrue);
      expect(tester.widget<SelectChip>(beverageFilter).selected, isFalse);
      expect(find.text('Better Sleep'), findsOneWidget);
      expect(tester.takeException(), isNull);
      await tester.pumpWidget(const SizedBox.shrink());
      await tester.pumpAndSettle();
    }
    tester.platformDispatcher.textScaleFactorTestValue = 1.4;
    addTearDown(tester.platformDispatcher.clearTextScaleFactorTestValue);
    await tester.pumpWidget(
      referenceApp(
        screen: 'insights-refined',
        brightness: Brightness.light,
        boundary: GlobalKey(),
      ),
    );
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    // The actual profile label, not an invented built-in category, drives UI.
    await tester.pumpWidget(
      MaterialApp(
        theme: AppTheme.light(),
        home: const RefinedInsights(
          goals: [
            ReviewGoal(id: 'custom-1', label: 'understand my IBS patterns'),
          ],
          initialGoalId: 'custom-1',
          findingGoals: {},
        ),
      ),
    );
    await tester.pumpAndSettle();
    expect(find.text('Understand My IBS Patterns'), findsOneWidget);
    expect(find.text('No findings for this goal yet.'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
