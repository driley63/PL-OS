import 'dart:io';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

import '../reference_scene.dart';

import 'package:health_diary/widgets/finding_summary_card.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('Capture real Flutter components', (tester) async {
    tester.view.physicalSize = const Size(1179, 2556);
    tester.view.devicePixelRatio = 3;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.runAsync(() async {
      final l = FontLoader('Inter');
      for (final font in ['Inter-Regular.ttf'])
        l.addFont(rootBundle.load('assets/fonts/$font'));
      await l.load();
      final icons = FontLoader('MaterialIcons');
      icons.addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'));
      await icons.load();
    });
    for (final dark in [false, true])
      for (final screen in [
        'today',
        'insights',
        'finding',
        'today-plan',
        'insights-ai-off',
        'more-filters',
      ]) {
        print("Rendering $screen ${dark ? 'dark' : 'light'}");
        final key = GlobalKey();
        await tester.pumpWidget(
          referenceApp(
            screen: screen,
            brightness: dark ? Brightness.dark : Brightness.light,
            boundary: key,
          ),
        );
        await tester.runAsync(() async {
          await Future<void>.delayed(const Duration(milliseconds: 400));
        });
        await tester.pumpAndSettle();
        if (screen == 'finding') {
          await tester.tap(find.byType(FindingSummaryCard).first);
          await tester.pumpAndSettle();
        }
        if (screen == 'more-filters') {
          await tester.tap(find.byKey(const ValueKey('more-filters')));
          await tester.pumpAndSettle();
        }
        expect(
          tester.takeException(),
          isNull,
          reason: 'No render errors in $screen',
        );
        await tester.runAsync(() async {
          final boundary =
              key.currentContext!.findRenderObject() as RenderRepaintBoundary;
          final image = await boundary.toImage(pixelRatio: 3);
          final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
          final file = File(
            '${Platform.environment['PLECTARA_REFERENCE_OUTPUT']!}/$screen-${dark ? 'dark' : 'light'}.png',
          );
          file.writeAsBytesSync(bytes!.buffer.asUint8List());
          image.dispose();
        });
        print('Saved $screen');
      }
  });
}
