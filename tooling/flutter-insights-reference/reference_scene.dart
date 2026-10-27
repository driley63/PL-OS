import 'package:health_diary/models/onboarding_options.dart';

import 'refined_insights.dart';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:health_diary/theme/app_theme.dart';
import 'package:health_diary/theme/plectara_app_visuals.dart';
import 'package:health_diary/theme/plectara_tokens.dart';
import 'package:health_diary/models/local_finding.dart';
import 'package:health_diary/models/health_insight.dart';
import 'package:health_diary/insights/finding_presentation.dart';
import 'package:health_diary/data/prefs_store.dart';
import 'package:health_diary/state/ai_narrative_preferences.dart';
import 'package:health_diary/state/ai_chat_preferences.dart';
import 'package:health_diary/state/live_ai_feature_preferences.dart';
import 'package:health_diary/widgets/today_insights_region.dart';
import 'package:health_diary/widgets/finding_summary_card.dart';
import 'package:health_diary/widgets/insights_care_notice.dart';
import 'package:health_diary/widgets/plectara_brand_mark.dart';
import 'package:health_diary/widgets/select_chip.dart';
import 'package:health_diary/widgets/woven/reading_card.dart';
import 'package:health_diary/widgets/woven/woven_route.dart';
import 'package:health_diary/widgets/woven/copper_rule.dart';
import 'package:health_diary/screens/finding_detail_screen.dart';

class FixturePrefs implements PrefsStore {
  final Map<String, Object> values = {};
  @override
  bool? getBool(String k) => values[k] as bool?;
  @override
  int? getInt(String k) => values[k] as int?;
  @override
  String? getString(String k) => values[k] as String?;
  @override
  Future<void> setBool(String k, bool v) async {
    values[k] = v;
  }

  @override
  Future<void> setInt(String k, int v) async {
    values[k] = v;
  }

  @override
  Future<void> setString(String k, String v) async {
    values[k] = v;
  }

  @override
  Future<void> remove(String k) async {
    values.remove(k);
  }
}

final fixture = HealthInsight(
  id: 'reference-oct25',
  generatedAt: DateTime(2026, 10, 25, 16, 15),
  summary: 'Some patterns in your recent record may be worth discussing.',
  urgency: CareUrgency.considerCare,
  entryCountAnalyzed: 48,
  aiNarrative: 'Caffeine timing is one possible factor to explore alongside other routines. This explanation adds context to your recorded findings and does not establish a cause.',
  suggestions: const [],
  findings: const [
    LocalFinding(
      code: 'beverage.caffeine_late_sleep',
      domain: FindingDomain.beverage,
      kind: FindingKind.correlation,
      label: 'Later caffeine, lower sleep quality. You rated sleep lower on days with caffeine after 2 PM.',
      evidenceWindowDays: 14,
      relatedTitles: ['Caffeine', 'Sleep'],
      metrics: {
        'beverage': 'caffeine',
        'afterHour': 14,
        'exposedQuality': 3,
        'otherQuality': 7,
      },
      suggestion: 'Record caffeine timing and sleep quality to explore this possible connection.',
    ),
    LocalFinding(
      code: 'beverage.water_intake',
      domain: FindingDomain.beverage,
      kind: FindingKind.trend,
      label: 'You’re logging more water: Recent average: 35.4 fl oz per day.',
      metrics: {'averageMl': 1047},
      evidenceWindowDays: 14,
    ),
    LocalFinding(
      code: 'sleep.short_duration_cluster',
      domain: FindingDomain.sleep,
      kind: FindingKind.trend,
      label: 'A little more rest. Your logged sleep quality has improved.',
      evidenceWindowDays: 14,
    ),
  ],
);
final items = fixture.findings
    .map((f) => FindingPresentation.fromFinding(f, fixture))
    .toList();

Widget referenceApp({
  required String screen,
  required Brightness brightness,
  required GlobalKey boundary,
}) {
  final prefs = FixturePrefs();
  final off = screen == 'insights-ai-off';
  prefs.values.addAll({
    'ai_narrative_consent_v1': !off,
    'ai_narrative_consent_version_v1': 3,
    'ai_chat_consent_v1': true,
    'ai_chat_consent_version_v1': 2,
  });
  return MultiProvider(
    providers: [
      ChangeNotifierProvider(
        create: (_) => AiNarrativePreferences(prefs: prefs),
      ),
      ChangeNotifierProvider(create: (_) => AiChatPreferences(prefs: prefs)),
      ChangeNotifierProvider(
        create: (_) => LiveAiFeaturePreferences(prefs: prefs),
      ),
    ],
    child: RepaintBoundary(
      key: boundary,
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: AppTheme.light().copyWith(platform: TargetPlatform.iOS),
        darkTheme: AppTheme.dark().copyWith(platform: TargetPlatform.iOS),
        themeMode: brightness == Brightness.dark
            ? ThemeMode.dark
            : ThemeMode.light,
        builder: (context, child) => MediaQuery(
          data: MediaQuery.of(context).copyWith(
            padding: const EdgeInsets.only(top: 59, bottom: 34),
            viewPadding: const EdgeInsets.only(top: 59, bottom: 34),
          ),
          child: child!,
        ),
        home: screen == 'insights-refined'
            ? RefinedInsights(
                goals: [
                  for (final goal in [
                    HealthGoal.betterSleep,
                    HealthGoal.moreEnergy,
                    HealthGoal.betterDigestion,
                    HealthGoal.resolveSymptoms,
                  ])
                    ReviewGoal(id: goal.name, label: goal.label),
                ],
                initialGoalId: HealthGoal.betterSleep.name,
                findingGoals: {
                  'caffeine': {HealthGoal.betterSleep.name},
                  'rest': {HealthGoal.betterSleep.name},
                  'water': {},
                },
              )
            : ReferenceHome(screen: screen == 'finding' ? 'insights' : screen),
      ),
    ),
  );
}

class ReferenceHome extends StatefulWidget {
  const ReferenceHome({super.key, required this.screen});
  final String screen;
  @override
  State<ReferenceHome> createState() => _ReferenceHomeState();
}

class _ReferenceHomeState extends State<ReferenceHome> {
  String focus = 'All';
  Set<String> logs = {};
  bool match(FindingPresentation item, Set<String> types) {
    final water = item.identity == 'beverage.water_intake';
    final outcome = focus == 'All' || (focus == 'Hydration' ? water : !water);
    final sources = water
        ? {'Beverages'}
        : item.identity.startsWith('beverage.')
        ? {'Beverages', 'Sleep'}
        : {'Sleep'};
    return outcome && (types.isEmpty || sources.intersection(types).isNotEmpty);
  }

  Future<void> more() async {
    var draft = Set<String>.from(logs);
    if (widget.screen == 'more-filters') draft = {'Beverages'};
    final result = await showModalBottomSheet<Set<String>>(
      context: context,
      isScrollControlled: true,
      useSafeArea: true,
      showDragHandle: true,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(12)),
      ),
      builder: (ctx) => StatefulBuilder(
        builder: (ctx, setSheet) {
          final n = items.where((i) => match(i, draft)).length;
          final t = Theme.of(ctx).textTheme;
          return SafeArea(
            top: false,
            child: Padding(
              padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: Text('More filters', style: t.titleLarge),
                      ),
                      TextButton(
                        onPressed: () => Navigator.pop(ctx),
                        child: const Text('Cancel'),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Text('Log types', style: t.titleMedium),
                  const SizedBox(height: 8),
                  Text(
                    'Show findings supported by these logs.',
                    style: t.bodyMedium,
                  ),
                  const SizedBox(height: 12),
                  for (final type in ['Sleep', 'Beverages'])
                    CheckboxListTile(
                      contentPadding: EdgeInsets.zero,
                      controlAffinity: ListTileControlAffinity.leading,
                      title: Text(type),
                      value: draft.contains(type),
                      onChanged: (v) => setSheet(() {
                        v == true ? draft.add(type) : draft.remove(type);
                      }),
                    ),
                  const SizedBox(height: 12),
                  Text(
                    '$n matching ${n == 1 ? 'finding' : 'findings'}',
                    style: t.bodyMedium,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Matches any selected log type within your chosen focus.',
                    style: t.bodySmall,
                  ),
                  const SizedBox(height: 20),
                  OutlinedButton(
                    onPressed: () => setSheet(draft.clear),
                    child: const Text('Reset'),
                  ),
                  const SizedBox(height: 12),
                  FilledButton(
                    onPressed: () => Navigator.pop(ctx, draft),
                    child: Text('Show $n ${n == 1 ? 'finding' : 'findings'}'),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
    if (result != null && mounted) setState(() => logs = result);
  }

  @override
  Widget build(BuildContext context) {
    final today = widget.screen.startsWith('today');
    final t = Theme.of(context).textTheme;
    final c = PlectaraAppColors.of(context);
    final filtered = items.where((i) => match(i, logs)).toList();
    return Scaffold(
      appBar: AppBar(
        title: today
            ? const PlectaraBrandMark(width: 124, reversed: true)
            : const Text('Insights'),
        actions: [
          IconButton(
            onPressed: () {},
            icon: const Icon(Icons.settings_outlined),
            tooltip: 'Settings',
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: PlectaraAppGeometry.bodyPadding.copyWith(
          top: PlectaraAppGeometry.bodyTopInset,
          bottom: today ? 88 : PlectaraAppGeometry.bodyBottomInset,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            InsightsCareNotice(insight: fixture),
            const SizedBox(height: PlectaraAppGeometry.sectionGap),
            if (today) ...[
              if (widget.screen == 'today-plan') ...[
                ReadingCard(
                  title: 'Your plan',
                  icon: Icons.flag_outlined,
                  trailing: Text('Day 6 of 14', style: t.labelMedium),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Text('Two-Week Drinks Check', style: t.titleSmall),
                      const SizedBox(height: 8),
                      Text(
                        'Record drinks and sleep today.',
                        style: t.bodyMedium,
                      ),
                      Align(
                        alignment: Alignment.centerLeft,
                        child: TextButton(
                          onPressed: () {},
                          child: const Text('View plan'),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: PlectaraAppGeometry.sectionGap),
              ],
              TodayInsightsRegion(insight: fixture),
              const SizedBox(height: PlectaraAppGeometry.sectionGap),
              ReadingCard(
                title: 'Today’s logs',
                trailing: Text('2 entries', style: t.bodySmall),
                child: Column(
                  children: [
                    ListTile(
                      contentPadding: EdgeInsets.zero,
                      leading: Icon(Icons.bedtime_outlined, color: c.link),
                      title: const Text('Sleep'),
                      subtitle: const Text('6 hr 50 min · Quality 7/10'),
                      trailing: Text('7:15 AM', style: t.bodySmall),
                    ),
                    ListTile(
                      contentPadding: EdgeInsets.zero,
                      leading: Icon(Icons.restaurant_outlined, color: c.link),
                      title: const Text('Breakfast'),
                      subtitle: const Text('Overnight oats'),
                      trailing: Text('8:10 AM', style: t.bodySmall),
                    ),
                  ],
                ),
              ),
            ] else ...[
              if (widget.screen == 'insights-ai-off') ...[
                ReadingCard(
                  child: Text(
                    'AI explanations are off. On-device findings remain available.',
                    style: t.bodyMedium,
                  ),
                ),
                const SizedBox(height: PlectaraAppGeometry.sectionGap),
              ],
              ReadingCard(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    Text('Found on your device', style: t.titleSmall),
                    const SizedBox(height: 4),
                    Text(
                      'Past 14 days · Updated today at 4:15 PM',
                      style: t.bodySmall?.copyWith(color: c.textSecondary),
                    ),
                    const SizedBox(height: 12),
                    Text('Focus on', style: t.titleMedium),
                    const SizedBox(height: 8),
                    Wrap(
                      spacing: 8,
                      runSpacing: 8,
                      children: [
                        for (final label in [
                          'All',
                          'Sleep & rest',
                          'Hydration',
                        ])
                          SelectChip(
                            label: label,
                            selected: focus == label,
                            onSelected: (_) => setState(() => focus = label),
                            centerLabel: true,
                          ),
                      ],
                    ),
                    Row(
                      children: [
                        TextButton(
                          key: const ValueKey('more-filters'),
                          onPressed: more,
                          child: Text(
                            logs.isEmpty
                                ? 'More filters'
                                : 'More filters · ${logs.length}',
                          ),
                        ),
                        const Spacer(),
                        Text('${filtered.length} findings', style: t.bodySmall),
                      ],
                    ),
                    if (logs.isNotEmpty)
                      Text('Log types: ${logs.join(', ')}', style: t.bodySmall),
                  ],
                ),
              ),
              const SizedBox(height: PlectaraAppGeometry.sectionGap),
              if (filtered.isEmpty)
                ReadingCard(
                  child: Column(
                    children: [
                      const Text('No findings match these filters.'),
                      TextButton(
                        onPressed: () => setState(() {
                          focus = 'All';
                          logs = {};
                        }),
                        child: const Text('Clear filters'),
                      ),
                    ],
                  ),
                ),
              for (final item in filtered) ...[
                FindingSummaryCard(
                  presentation: item,
                  onOpen: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => FindingDetailScreen(presentation: item),
                    ),
                  ),
                ),
                const SizedBox(height: PlectaraAppGeometry.sectionGap),
              ],
            ],
          ],
        ),
      ),
      floatingActionButton: today
          ? Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                OutlinedButton.icon(
                  style: OutlinedButton.styleFrom(
                    minimumSize: const Size(0, 54),
                    backgroundColor: c.control,
                    foregroundColor: c.text,
                    shape: const StadiumBorder(),
                  ),
                  onPressed: () {},
                  icon: const Icon(Icons.bolt_outlined),
                  label: const Text('Quick Log'),
                ),
                const SizedBox(width: 12),
                FilledButton.icon(
                  style: FilledButton.styleFrom(
                    minimumSize: const Size(0, 54),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                  ),
                  onPressed: () {},
                  icon: const Icon(Icons.add),
                  label: const Text('Log'),
                ),
              ],
            )
          : null,
      bottomNavigationBar: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const SeparatorRule(),
          NavigationBar(
            selectedIndex: today ? 0 : 4,
            onDestinationSelected: (_) {},
            destinations: const [
              NavigationDestination(
                icon: Icon(Icons.today_outlined),
                selectedIcon: Icon(Icons.today),
                label: 'Today',
              ),
              NavigationDestination(
                icon: Icon(Icons.format_list_bulleted_outlined),
                selectedIcon: Icon(Icons.format_list_bulleted),
                label: 'Timeline',
              ),
              NavigationDestination(
                icon: Icon(Icons.bar_chart_outlined),
                selectedIcon: Icon(Icons.bar_chart),
                label: 'Charts',
              ),
              NavigationDestination(
                icon: Icon(Icons.question_answer_outlined),
                selectedIcon: Icon(Icons.question_answer),
                label: 'Chat',
              ),
              NavigationDestination(
                icon: Icon(Icons.insights_outlined),
                selectedIcon: Icon(Icons.insights),
                label: 'Insights',
              ),
            ],
          ),
        ],
      ),
    );
  }
}
