"""Package the approved browser design for deterministic, app-only screenshot capture.

Does not run or modify the Flutter app. Screenshots are taken from reference.html
through the browser, at scene/theme query parameters. See the adjacent README.
"""
from pathlib import Path
import hashlib
import json
from component_color_tokens import bind_component_colors

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tooling/insights-journey-reference"
DEST = ROOT / "docs/assets/app/insights-presentation/approved-2026-10-27"
PUBLIC = DEST / "source"
PUBLIC.mkdir(parents=True, exist_ok=True)

replacements = {
    "__INTER_REGULAR__": "inter-regular.woff",
    "__INTER_MEDIUM__": "inter-medium.woff",
    "__INTER_SEMIBOLD__": "inter-semibold.woff",
    "__INTER_BOLD__": "inter-bold.woff",
    "__MATERIAL_CHROME__": "material-chrome.woff",
    "__STOMACH__": "stomach.svg",
    "__YARN__": "../../plectara/textures/plectara-widget-yarn-gentle-focus-v1.webp",
    "__LOGO__": "../../plectara/logos/plectara-horizontal-reversed.svg",
}
for key in ('__INTER_REGULAR__','__INTER_MEDIUM__','__INTER_SEMIBOLD__','__INTER_BOLD__','__MATERIAL_CHROME__','__STOMACH__'):
    filename = replacements[key]
    replacements[key] += '?v=' + hashlib.sha256((PUBLIC/filename).read_bytes()).hexdigest()[:12]
styles = (SOURCE / "styles.css").read_text()
styles = bind_component_colors(styles, ROOT)
script = (SOURCE / "journey.js").read_text()
for key, value in replacements.items():
    styles = styles.replace(key, value)
    script = script.replace(key, value)

scenes = json.loads((SOURCE / "scenes.json").read_text())
setup = """
  const params = new URLSearchParams(location.search);
  const scene = REFERENCE_SCENES.find(s=>s.id===params.get('scene')) || REFERENCE_SCENES[0];
  Object.assign(config, scene.config || {});
  Object.assign(views.today, {screen:scene.screen, goal:scene.goal||'all',
    finding:'sleep-activity', chatKey:scene.chatKey||'overall', y:scene.y||0, open:scene.open||[]});
  if(scene.conversation) views.today.conversations['sleep-activity']={draft:'',phase:'ready',turns:[
    {role:'user',text:'What should I record next?'},
    {role:'assistant',text:'Record sleep duration and quality alongside activity duration and effort. These records can help you assess whether the pattern appears again. Missing logs and other routines can affect the comparison; this does not establish a cause.'}
  ]};
  document.title = scene.label + ' — Plectara Design Reference';
  document.documentElement.dataset.scene = scene.id;
""".replace("REFERENCE_SCENES", json.dumps(scenes, ensure_ascii=False))
assert script.count("  const models=[];") == 1
script = script.replace("  const models=[];", setup + "\n  const models=[];")
(PUBLIC / "styles.css").write_text(styles)
(PUBLIC / "journey.js").write_text(script)
(PUBLIC / "scenes.json").write_text(json.dumps(scenes, indent=2, ensure_ascii=False)+"\n")
reference = (SOURCE / "reference.html").read_text()
for filename in ('styles.css','journey.js','lucide.js'):
    digest = hashlib.sha256((PUBLIC/filename).read_bytes()).hexdigest()[:12]
    reference = reference.replace('source/'+filename+'"', 'source/'+filename+'?v='+digest+'"')
(DEST / "reference.html").write_text(reference)
hashes = {}
for path in sorted(SOURCE.glob('*')):
    if path.is_file():
        hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
for dependency in ['assets/tokens/color.tokens.json', 'tooling/component_color_tokens.py']:
    hashes[dependency] = hashlib.sha256((ROOT / dependency).read_bytes()).hexdigest()
(DEST / "source-hashes.json").write_text(json.dumps(hashes, indent=2)+"\n")
print(f"Packaged {len(scenes)} scenes in {DEST.relative_to(ROOT)}")
