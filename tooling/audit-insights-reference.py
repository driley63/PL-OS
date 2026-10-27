"""Audit the design reference against PL-OS aliases and current app source.

No app mutation or native accessibility certification. Run from any directory;
--app points at the consuming checkout for current-source comparison.
"""
import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--app', type=Path, required=True)
args = parser.parse_args()
source = ROOT / 'tooling/insights-journey-reference'
dest = ROOT / 'docs/assets/app/insights-presentation/approved-2026-10-27'
css = (source / 'styles.css').read_text()
app = (args.app / 'lib/theme/plectara_app_visuals.dart').read_text()
goals = (args.app / 'lib/models/onboarding_options.dart').read_text()
tokens = json.loads((ROOT / 'assets/app/plectara/app-visual-tokens.json').read_text())
colors = {name: values for name, *values in re.findall(
    r'--p-([\w-]+):light-dark\((#[\da-f]+),(#[\da-f]+)\)', css)}

def normalized(value):
    value = value.lower()
    return '#' + ''.join(c * 2 for c in value[1:]) if len(value) == 4 else value

mapping = {'surface':'card','ink':'text','meta':'textSecondary',
    'control':'control','selected':'soft','primary':'primary',
    'on-primary':'onPrimary','link':'link','input':'controlOutline',
    'edge':'decorativeOutline','nav-selected':'navigationSelected',
    'nav-label':'selectedLabel','tile-edge':'tileOutline',
    'attention':'attention','attention-fill':'attentionBacking',
    'on-selected':'onSelected'}
dark_inherited = {'selectedLabel':'#8DC7B7','tileOutline':'#C88764',
    'attentionBacking':'#223D49','onSelected':'#8DC7B7'}
alias_checks = []
for mode_index, mode in enumerate(('light','dark')):
    for local, canonical in mapping.items():
        expected = tokens['themes'][mode].get(canonical, dark_inherited.get(canonical))
        actual = normalized(colors[local][mode_index])
        assert actual == normalized(expected), (mode, local, actual, expected)
        alias_checks.append({'theme':mode,'reference':local,'pl_os':canonical,'value':actual})

catalog = json.loads((source/'goal-catalog.json').read_text())['goals']
native_goals = dict(re.findall(r"HealthGoal\.(\w+) => '([^']+)'", goals))
assert len(catalog) == len(native_goals) == 11
for goal in catalog:
    assert native_goals[goal['key']] == goal['label'], goal
assert 'bool get deviceOnly' in goals and 'HealthGoalGroup.wellbeing' in goals

geometry = {'logoWidth':124,'bodyGutter':12,'bodyTopInset':10,
    'bodyBottomInset':14,'sectionGap':12,'cardPadding':14,'cardRadius':14,
    'cardBorder':1,'buttonRadius':9,'floatingActionHeight':54,
    'headerToolbarHeight':60}
for name, value in geometry.items():
    assert re.search(rf'static const double {name} = {value};', app), name
assert '.brand img{width:124px' in css
assert 'background:var(--p-primary);color:var(--p-on-primary)' in css
assert 'background:var(--p-nav-selected);color:var(--p-on-selected)' in css

contrast_spec = importlib.util.spec_from_file_location('component_contrast',ROOT/'tooling/check-component-contrast.py')
module = importlib.util.module_from_spec(contrast_spec)
contrast_spec.loader.exec_module(module)
uses = [('Body','ink','surface',4.5),('Metadata','meta','surface',4.5),
    ('Footer and secondary action','link','surface',4.5),
    ('Secondary action on control','link','control',4.5),
    ('Primary action','on-primary','primary',4.5),
    ('Selected filter','on-selected','selected',4.5),
    ('Selected navigation icon','on-selected','nav-selected',3),
    ('Selected navigation label','nav-label','surface',4.5),
    ('Control labels','ink','control',4.5),('Control metadata','meta','control',4.5),
    ('Attention','attention','attention-fill',4.5),('End Plan','attention','surface',4.5),
    ('AI text','ai','surface',4.5),('AI icon','ai','ai-wash',3),
    ('Goal icon','link','wash',3),('Input border','input','surface',3),
    ('Control border','input','control',3),('Current chart mark','link','control',3),
    ('Prior chart mark','previous','control',3)]
contrast = []
for idx, mode in enumerate(('light','dark')):
    for name, foreground, background, minimum in uses:
        pair = {'name':name,'foreground':normalized(colors[foreground][idx]),
            'background':normalized(colors[background][idx]),'minimum':minimum}
        ratio, passed = module.evaluate(pair)
        assert passed, (mode, name, ratio, minimum)
        contrast.append(dict(theme=mode,**pair,ratio=ratio,passed=passed))
# Header controls sit on 92% ink; white is the worst possible underlying image.
pair={'foreground':'#FAF8F4','background':'#FFFFFF',
    'backgroundLayers':[{'color':'#192D38','alpha':.92}],'minimum':4.5}
ratio, passed = module.evaluate(pair)
assert passed
contrast.append(dict(name='Header controls over brightest possible yarn',**pair,ratio=ratio,passed=passed))
files = ['lib/theme/plectara_app_visuals.dart','lib/theme/app_theme.dart',
    'lib/theme/plectara_tokens.dart','lib/screens/app_shell.dart',
    'lib/widgets/woven/reading_card.dart','lib/widgets/woven/woven_backdrop.dart',
    'lib/widgets/woven/copper_rule.dart','lib/widgets/preferences_button.dart',
    'lib/models/onboarding_options.dart','lib/widgets/rewards_card.dart','lib/widgets/badge_detail.dart']
report = {'date':'2026-10-27','scope':'Reference design consistency; current working-tree app source, not native runtime certification',
    'native_source_sha256':{f:hashlib.sha256((args.app/f).read_bytes()).hexdigest() for f in files},
    'alias_checks':alias_checks,'goal_labels_checked':len(catalog),
    'native_geometry_checked':geometry,'contrast_checks':contrast,
    'exclusions':['No native accessibility workflow certification','No analyzer or clinical policy validation','No app implementation or deployment']}
(dest/'consistency-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'Passed: {len(alias_checks)} PL-OS role mappings, {len(catalog)} current app goal labels, {len(geometry)} native geometry values, {len(contrast)} reference contrast pairs.')
