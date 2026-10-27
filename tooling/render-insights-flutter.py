#!/usr/bin/env python3
"""Render PL-OS Insights references using the local Plectara Flutter source."""
import argparse, hashlib, json, os, shutil, subprocess
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--app-root', type=Path, default=Path.home()/'Repos/Plectara')
parser.add_argument('--metadata-only',action='store_true')
parser.add_argument('--review-only',action='store_true')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
source=root/'tooling/flutter-insights-reference'
work=root/'outputs/insights-flutter-reference'
out=root/'docs/assets/app/insights-presentation/screens'
app=args.app_root.resolve()
if not args.metadata_only:
    (work/'test').mkdir(parents=True,exist_ok=True)
    (work/'pubspec.yaml').write_text((source/'pubspec.template.yaml').read_text().replace('APP_SOURCE_PATH',str(app)))
    for name in ['reference_scene.dart','refined_insights.dart','test/capture_test.dart','test/refined_capture_test.dart']:
        shutil.copyfile(source/name,work/name)
    if not (work/'assets').exists(): (work/'assets').symlink_to(app/'assets',target_is_directory=True)
    subprocess.run(['flutter','pub','get','--offline'],cwd=work,check=True)
    subprocess.run(['flutter','test','--no-pub','test/refined_capture_test.dart' if args.review_only else 'test/capture_test.dart','--reporter','expanded'],cwd=work,env={**os.environ,'PLECTARA_REFERENCE_OUTPUT':str(out)},check=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if args.review_only:
    metadata={'kind':'Local goal-driven composition proposal; profile goals supply labels and IDs; no application change','font':'Inter','renderer':'tooling/render-insights-flutter.py --review-only','screens':[{'screen':'insights-refined','theme':t,'png':f'screens/insights-refined-{t}.png','width':1179,'height':2556,'png_sha256':sha(out/f'insights-refined-{t}.png')} for t in ['light','dark']]+[{'screen':'insights-goals','theme':t,'png':f'screens/insights-goals-{t}.png','width':1179,'height':2556,'png_sha256':sha(out/f'insights-goals-{t}.png')} for t in ['light','dark']]}
    (out/'review.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print('Rendered one refined inventory composition in light and dark.')
    raise SystemExit(0)

components=['theme/app_theme.dart','theme/plectara_app_visuals.dart','widgets/woven/reading_card.dart','widgets/woven/woven_backdrop.dart','widgets/today_insights_region.dart','widgets/finding_summary_card.dart','widgets/insights_care_notice.dart','screens/finding_detail_screen.dart','widgets/select_chip.dart']
metadata={
 'kind':'Flutter-engine component captures from an isolated preview; not iOS simulator captures',
 'logicalSize':'393 x 852','pixelScale':3,'font':'Inter','renderer':'tooling/render-insights-flutter.py',
 'source_project':'Plectara working tree; no application source modified by this renderer',
 'source_components':{p:sha(app/'lib'/p) for p in components},
 'preview_source':'tooling/flutter-insights-reference/reference_scene.dart',
 'fixtures':'Illustrative seeded findings; local preview providers only; no cloud calls or real health data',
 'system_chrome':'System status and home indicators are omitted; actual iOS safe-area insets retained in the preview',
 'scope':'Today highlight, care, findings, detail, theme and backdrop reuse app components. Focus on/More filters and compact plan/log fixtures are preview compositions built with Flutter and shared app components.',
 'screens':[{'screen':n,'theme':t,'png':f'screens/{n}-{t}.png','width':1179,'height':2556,'png_sha256':sha(out/f'{n}-{t}.png')} for t in ['light','dark'] for n in ['today','insights','finding','today-plan','insights-ai-off','more-filters']]
}
(out/'references.json').write_text(json.dumps(metadata,indent=2)+'\n')
print('Recorded twelve Flutter component captures and source provenance.')
