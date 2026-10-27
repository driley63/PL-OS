import 'package:flutter/material.dart';
import 'package:health_diary/theme/plectara_app_visuals.dart';
import 'package:health_diary/widgets/woven/reading_card.dart';
import 'package:health_diary/widgets/woven/copper_rule.dart';
import 'package:health_diary/widgets/select_chip.dart';

/// Values supplied by the user's profile; never a built-in filter taxonomy.
class ReviewGoal {
  const ReviewGoal({required this.id, required this.label});
  final String id;
  final String label;
  String get displayLabel => label
      .split(RegExp(r'\s+'))
      .map((word) {
        if (word.isEmpty) return word;
        if (word.length <= 4 && word == word.toUpperCase()) return word;
        return '${word[0].toUpperCase()}${word.substring(1).toLowerCase()}';
      })
      .join(' ');
}

/// Local composition proposal. The calling fixture supplies profile goals
/// and finding associations. No live app state or clinical rules are changed.
class RefinedInsights extends StatefulWidget {
  const RefinedInsights({
    super.key,
    required this.goals,
    required this.findingGoals,
    this.initialGoalId,
  });
  final List<ReviewGoal> goals;
  final Map<String, Set<String>> findingGoals;
  final String? initialGoalId;
  @override
  State<RefinedInsights> createState() => _RefinedInsightsState();
}

class _RefinedInsightsState extends State<RefinedInsights> {
  late String? selectedGoalId;
  Set<String> logTypes = {};
  @override
  void initState() {
    super.initState();
    selectedGoalId = widget.goals.any((g) => g.id == widget.initialGoalId)
        ? widget.initialGoalId
        : null;
  }

  String get selectedGoalLabel => selectedGoalId == null
      ? 'All Goals'
      : widget.goals.firstWhere((g) => g.id == selectedGoalId).displayLabel;
  bool shows(String id, [Set<String>? types]) {
    final matchesGoal =
        selectedGoalId == null ||
        (widget.findingGoals[id]?.contains(selectedGoalId) ?? false);
    final sources = switch (id) {
      'caffeine' => {'Sleep', 'Beverages'},
      'water' => {'Beverages'},
      _ => {'Sleep'},
    };
    final chosen = types ?? logTypes;
    return matchesGoal &&
        (chosen.isEmpty || sources.intersection(chosen).isNotEmpty);
  }

  int count([Set<String>? types]) =>
      ['caffeine', 'water', 'rest'].where((id) => shows(id, types)).length;
  TextStyle meta(PlectaraAppColors c, {double size = 12}) => TextStyle(
    fontFamily: 'Inter',
    fontSize: size,
    height: 1.5,
    color: c.textSecondary,
  );

  Future<void> chooseGoal() async {
    final result = await showModalBottomSheet<String>(
      context: context,
      useSafeArea: true,
      isScrollControlled: true,
      showDragHandle: true,
      builder: (ctx) => SafeArea(
        top: false,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text('Your Goals', style: Theme.of(ctx).textTheme.titleLarge),
              const SizedBox(height: 8),
              Text(
                'Focus on a goal you have saved.',
                style: Theme.of(ctx).textTheme.bodySmall,
              ),
              const SizedBox(height: 12),
              ListTile(
                contentPadding: EdgeInsets.zero,
                title: const Text('All Goals'),
                trailing: selectedGoalId == null
                    ? const Icon(Icons.check)
                    : null,
                onTap: () => Navigator.pop(ctx, ''),
              ),
              for (final goal in widget.goals)
                ListTile(
                  contentPadding: EdgeInsets.zero,
                  title: Text(goal.displayLabel),
                  trailing: selectedGoalId == goal.id
                      ? const Icon(Icons.check)
                      : null,
                  onTap: () => Navigator.pop(ctx, goal.id),
                ),
            ],
          ),
        ),
      ),
    );
    if (result != null && mounted)
      setState(() => selectedGoalId = result.isEmpty ? null : result);
  }

  Widget logTypeFilters() => Semantics(
    container: true,
    label: 'Filter by supporting log types',
    child: SingleChildScrollView(
      key: const ValueKey('inline-log-filters'),
      scrollDirection: Axis.horizontal,
      child: Row(
        children: [
          for (final filter in [
            ('All Log Types', Icons.layers_outlined),
            ('Sleep', Icons.bedtime_outlined),
            ('Beverages', Icons.coffee_outlined),
          ])
            Padding(
              padding: const EdgeInsets.only(right: 8),
              child: ConstrainedBox(
                constraints: const BoxConstraints(minWidth: 44, minHeight: 44),
                child: SelectChip(
                  key: ValueKey('log-filter-${filter.$1}'),
                  label: filter.$1,
                  icon: filter.$2,
                  selected: filter.$1 == 'All Log Types'
                      ? logTypes.isEmpty
                      : logTypes.contains(filter.$1),
                  onSelected: (selected) => setState(() {
                    if (filter.$1 == 'All Log Types') {
                      logTypes.clear();
                    } else if (selected) {
                      logTypes.add(filter.$1);
                    } else {
                      logTypes.remove(filter.$1);
                    }
                  }),
                ),
              ),
            ),
        ],
      ),
    ),
  );

  Widget bridge(PlectaraAppColors c) {
    Widget node(IconData icon, String label) => Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: BoxDecoration(
        color: c.control,
        borderRadius: BorderRadius.circular(999),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 18, color: c.link),
          const SizedBox(width: 6),
          Text(
            label,
            style: meta(c).copyWith(color: c.text, fontWeight: FontWeight.w500),
          ),
        ],
      ),
    );
    return Semantics(
      label: 'An observed association between caffeine timing and sleep quality. No cause is established.',
      child: ExcludeSemantics(
        child: Row(
          children: [
            node(Icons.coffee_outlined, 'Caffeine'),
            Expanded(
              child: Row(
                children: [
                  Expanded(
                    child: Container(height: 1, color: c.controlOutline),
                  ),
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 6),
                    child: Icon(Icons.link, size: 18, color: c.link),
                  ),
                  Expanded(
                    child: Container(height: 1, color: c.controlOutline),
                  ),
                ],
              ),
            ),
            node(Icons.bedtime_outlined, 'Sleep'),
          ],
        ),
      ),
    );
  }

  Widget comparison(PlectaraAppColors c) {
    Widget group(String label, int value, Color color) => Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          children: [
            Expanded(child: Text(label, style: meta(c))),
            Text(
              '$value',
              style: TextStyle(
                fontFamily: 'Inter',
                fontSize: 21,
                height: 1.2,
                fontWeight: FontWeight.w600,
                color: c.text,
              ),
            ),
            Text(' /10', style: meta(c)),
          ],
        ),
        const SizedBox(height: 6),
        SizedBox(
          height: 8,
          child: LayoutBuilder(
            builder: (ctx, bounds) => Stack(
              children: [
                Positioned.fill(
                  child: DecoratedBox(
                    decoration: BoxDecoration(
                      color: c.control,
                      borderRadius: BorderRadius.circular(2),
                    ),
                  ),
                ),
                Container(
                  width: bounds.maxWidth * value / 10,
                  decoration: BoxDecoration(
                    color: color,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
    return Semantics(
      label: 'Past 14 days. Average sleep quality on a zero to ten scale: caffeine logged after 2 PM, 3 out of 10; no caffeine logged after 2 PM, 7 out of 10.',
      child: ExcludeSemantics(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Average Sleep Quality',
              style: meta(c).copyWith(fontWeight: FontWeight.w500),
            ),
            const SizedBox(height: 8),
            group('Caffeine Logged After 2 PM', 3, c.textSecondary),
            const SizedBox(height: 12),
            group('No Caffeine Logged After 2 PM', 7, c.link),
            const SizedBox(height: 6),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                for (final value in ['0', '5', '10'])
                  Text(value, style: meta(c, size: 10)),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget featured(PlectaraAppColors c) {
    final t = Theme.of(context).textTheme;
    return ReadingCard(
      onTap: () => evidence('caffeine'),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          bridge(c),
          const SizedBox(height: 12),
          Text(
            'Later caffeine,\nlower sleep quality',
            style: t.titleMedium?.copyWith(
              fontSize: 22,
              height: 28 / 22,
              fontWeight: FontWeight.w600,
              color: c.text,
            ),
          ),
          const SizedBox(height: 16),
          comparison(c),
          const SizedBox(height: 12),
          Text('An association, not a proven cause.', style: meta(c)),
          const SizedBox(height: 12),
          Wrap(
            alignment: WrapAlignment.spaceBetween,
            crossAxisAlignment: WrapCrossAlignment.center,
            spacing: 12,
            runSpacing: 4,
            children: [
              Text('On Device · Past 14 Days', style: meta(c, size: 11)),
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    'View Evidence',
                    style: meta(c)
                        .copyWith(color: c.link, fontWeight: FontWeight.w600),
                  ),
                  const SizedBox(width: 4),
                  Icon(Icons.chevron_right, size: 18, color: c.link),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget secondary(PlectaraAppColors c) => ReadingCard(
    onTap: () => evidence('rest'),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          selectedGoalId == null
              ? 'ANOTHER FINDING'
              : 'ALSO FOR ${selectedGoalLabel.toUpperCase()}',
          style: meta(c, size: 10).copyWith(
            color: c.link,
            fontWeight: FontWeight.w600,
            letterSpacing: .5,
          ),
        ),
        const SizedBox(height: 6),
        Row(
          children: [
            Icon(Icons.nights_stay_outlined, size: 20, color: c.link),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                'A little more rest',
                style: Theme.of(context).textTheme.titleMedium,
              ),
            ),
            Icon(Icons.chevron_right, size: 20, color: c.textSecondary),
          ],
        ),
        const SizedBox(height: 6),
        Text('Your logged sleep quality has improved.', style: meta(c)),
        const SizedBox(height: 8),
        Text(
          'Recorded Trend · On Device · Past 14 Days',
          style: meta(c, size: 11),
        ),
      ],
    ),
  );

  void evidence(String id) => showModalBottomSheet<void>(
    context: context,
    showDragHandle: true,
    useSafeArea: true,
    builder: (ctx) => SafeArea(
      top: false,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Supporting Evidence',
              style: Theme.of(ctx).textTheme.titleLarge,
            ),
            const SizedBox(height: 12),
            Text(
              id == 'caffeine'
                  ? 'Your average logged sleep quality was 3/10 for nights following days with caffeine logged after 2 PM, compared with 7/10 when no caffeine was logged after 2 PM. The second group can include days with only earlier caffeine or no caffeine entries. Days with caffeine entries whose timing is unknown are excluded unless another entry confirms caffeine after 2 PM. Missing entries do not prove that no caffeine was consumed. This association does not show caffeine caused the difference.'
                  : id == 'water'
                  ? 'Your water logs average 35.4 fl oz per day over the past 14 days.'
                  : 'Your logged sleep quality has improved. A numeric baseline is unavailable in this fixture.',
            ),
            const SizedBox(height: 20),
            TextButton(
              onPressed: () => Navigator.pop(ctx),
              child: const Text('Close'),
            ),
          ],
        ),
      ),
    ),
  );

  @override
  Widget build(BuildContext context) {
    final c = PlectaraAppColors.of(context),
        t = Theme.of(context).textTheme,
        n = count();
    return Scaffold(
      appBar: AppBar(
        title: const Text('Insights'),
        actions: [
          IconButton(
            onPressed: () {},
            tooltip: 'Settings',
            icon: const Icon(Icons.settings_outlined),
          ),
        ],
      ),
      body: ListView(
        padding: PlectaraAppGeometry.bodyPadding.copyWith(
          top: PlectaraAppGeometry.bodyTopInset,
        ),
        children: [
          ReadingCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: InkWell(
                        key: const ValueKey('profile-goal-selector'),
                        onTap: chooseGoal,
                        child: ConstrainedBox(
                          constraints: const BoxConstraints(minHeight: 44),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text('Focus on', style: meta(c, size: 11)),
                              const SizedBox(height: 2),
                              Row(
                                children: [
                                  Flexible(
                                    child: Text(
                                      selectedGoalLabel,
                                      style: t.titleMedium?.copyWith(
                                        fontWeight: FontWeight.w600,
                                      ),
                                    ),
                                  ),
                                  const SizedBox(width: 6),
                                  Icon(
                                    Icons.expand_more,
                                    size: 20,
                                    color: c.link,
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                logTypeFilters(),
                const SizedBox(height: 8),
                Semantics(
                  liveRegion: true,
                  child: Text(
                    '$n ${n == 1 ? 'Finding' : 'Findings'} · Updated 4:15 PM',
                    style: meta(c, size: 11),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          if (shows('caffeine')) ...[featured(c), const SizedBox(height: 12)],
          if (shows('rest')) ...[secondary(c), const SizedBox(height: 12)],
          if (shows('water'))
            ReadingCard(
              onTap: () => evidence('water'),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text('Your recorded water intake', style: t.titleMedium),
                  const SizedBox(height: 8),
                  Text('35.4 fl oz per day', style: t.bodyLarge),
                  const SizedBox(height: 6),
                  Text(
                    'Recorded Average · On Device · Past 14 Days',
                    style: meta(c, size: 11),
                  ),
                ],
              ),
            ),
          if (n == 0)
            ReadingCard(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(
                    logTypes.isEmpty
                        ? 'No findings for this goal yet.'
                        : 'No findings match these filters.',
                    style: t.titleMedium,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Your other findings are still available under All Goals.',
                    style: meta(c),
                  ),
                  Align(
                    alignment: Alignment.centerLeft,
                    child: TextButton(
                      onPressed: () => setState(() {
                        selectedGoalId = null;
                        logTypes = {};
                      }),
                      child: const Text('View All Goals'),
                    ),
                  ),
                ],
              ),
            ),
        ],
      ),
      bottomNavigationBar: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const SeparatorRule(),
          NavigationBar(
            selectedIndex: 4,
            onDestinationSelected: (_) {},
            destinations: const [
              NavigationDestination(
                icon: Icon(Icons.today_outlined),
                label: 'Today',
              ),
              NavigationDestination(
                icon: Icon(Icons.format_list_bulleted_outlined),
                label: 'Timeline',
              ),
              NavigationDestination(
                icon: Icon(Icons.bar_chart_outlined),
                label: 'Charts',
              ),
              NavigationDestination(
                icon: Icon(Icons.question_answer_outlined),
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
