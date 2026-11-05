"""Build the approved Today mockup as a standalone, app-only capture surface."""
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'tooling/today-insights-reference'
OUT = ROOT / 'docs/assets/app/insights-presentation/today-overview-2026-11-05'
OLD = ROOT / 'docs/assets/app/insights-presentation/connections-first-2026-10-27/source'
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'screens').mkdir(exist_ok=True)
fragment = (SRC / 'approved-fragment.html').read_text()
css = re.search(r'<style>(.*?)</style>', fragment, re.S).group(1)
script = re.search(r'<script>(.*?)</script>', fragment, re.S).group(1)
scenes = json.loads((SRC / 'scenes.json').read_text())
state_map = {s['id']:s['state'] for s in scenes}
bootstrap = """
const query = new URLSearchParams(location.search);
const referenceScenes = __SCENES__;
const scene = referenceScenes[query.get('scene')] ? query.get('scene') : 'today-new';
const theme = query.get('theme') === 'dark' ? 'dark' : 'light';
const phone = document.querySelector('.pt-phone');
phone.dataset.theme = theme;
phone.setAttribute('aria-label','Plectara Today Insights reference, '+theme+' theme');
document.getElementById('plectara-today-insights-nov5').style.zoom = query.get('scale')==='1' ? 1 : 3;
document.documentElement.dataset.scene = scene;
document.documentElement.dataset.theme = theme;
""".replace('__SCENES__',json.dumps(state_map))
script = script.replace('(()=>{','(()=>{'+bootstrap,1)
script = script.replace('const saved=savedViews(window.openai?.widgetState);','const saved={reference:referenceScenes[scene]};')
script = re.sub(r'^function persist\(\).*$', 'function persist(){}', script, flags=re.M)
script = re.sub(r'^if\(globalThis.Tweak\).*$', '', script, flags=re.M)
script = re.sub(r"^window.addEventListener\('openai:set_globals'.*$", '', script, flags=re.M)
assert 'window.openai' not in script and 'new Tweak' not in script
script += """
(async()=>{
 await document.fonts.ready;
 await Promise.all([...document.images].map(img=>img.decode().catch(()=>{})));
 const yarn=getComputedStyle(document.querySelector('.pt-yarn')).backgroundImage;
 const url=yarn.match(/^url\\([\"']?(.*?)[\"']?\\)$/)?.[1];
 if(url){const image=new Image();image.src=url;await image.decode();}
 await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
 document.documentElement.dataset.captureReady='true';
})();
"""
css += """
html,body{margin:0;padding:0;background:#192d38;width:max-content}
#plectara-today-insights-nov5{width:393px;zoom:3}
#plectara-today-insights-nov5 .pt-phone{width:393px;border-radius:0;box-shadow:none;margin:0}
#plectara-today-insights-nov5 .pt-phone button{cursor:pointer}
#plectara-today-insights-nov5 .pt-phone button:focus-visible{outline:3px solid var(--pt-text);outline-offset:-3px}
"""
(OUT/'styles.css').write_text(css)
(OUT/'reference.js').write_text(script)
for name in ['lucide.js','OFL.txt','LUCIDE-LICENSE','MATERIAL-ICONS-LICENSE','HEALTHICONS-LICENSE']:
 shutil.copy2(OLD/name,OUT/name)
html = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Plectara · Today Insights · Approved Design Reference</title><link rel="stylesheet" href="styles.css"><script src="lucide.js"></script></head><body><div id="plectara-today-insights-nov5"><div class="pt-phone" data-theme="light" data-case="reference"></div></div><script src="reference.js"></script></body></html>'''
for name in ['styles.css','lucide.js','reference.js']:
 digest=hashlib.sha256((OUT/name).read_bytes()).hexdigest()[:12]
 html=html.replace('"'+name+'"','"'+name+'?v='+digest+'"')
(OUT/'reference.html').write_text(html)
roles={
 'unreadBackground':{'light':'#76B7A5','dark':'#264C4B','source':'primitive.jade / dark.selected'},
 'unreadForeground':{'light':'#192D38','dark':'#FAF8F4','source':'primitive.ink / neutral.background'},
 'unreadMarker':{'light':'#264C4B','dark':'#76B7A5','source':'dark.selected / primitive.jade'},
 'unreadIcon':{'light':'#264C4B','dark':'#8DC7B7','source':'dark.selected / dark.link'},
 'unreadBadgeBackground':{'light':'#264C4B','dark':'#76B7A5','source':'dark.selected / primitive.jade'},
 'unreadBadgeForeground':{'light':'#FAF8F4','dark':'#192D38','source':'neutral.background / primitive.ink'}
}
(OUT/'component-colors.json').write_text(json.dumps(roles,indent=2)+'\n')
def lum(h):
 v=[int(h[i:i+2],16)/255 for i in (1,3,5)]
 return sum((x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4)*w for x,w in zip(v,[.2126,.7152,.0722]))
checks=[]
for theme in ['light','dark']:
 for name,fg,bg,minimum in [('text','unreadForeground','unreadBackground',4.5),('marker','unreadMarker','unreadBackground',3),('icon','unreadIcon','unreadBackground',3),('badge text','unreadBadgeForeground','unreadBadgeBackground',4.5),('badge boundary','unreadBadgeBackground','unreadBackground',3)]:
  a,b=sorted([lum(roles[fg][theme]),lum(roles[bg][theme])]);ratio=(b+.05)/(a+.05)
  assert ratio>=minimum,(theme,name,ratio)
  checks.append(dict(theme=theme,role=name,foreground=roles[fg][theme],background=roles[bg][theme],minimum=minimum,ratio=ratio,passed=True))
(OUT/'contrast-checks.json').write_text(json.dumps({'scope':'Unread component colors only; not native accessibility certification','checks':checks},indent=2)+'\n')
inputs=list(SRC.glob('*'))+[Path(__file__),ROOT/'assets/tokens/color.tokens.json']
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(inputs) if p.is_file()}
(OUT/'source-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(f'Built {OUT}; {len(checks)} contrast pairs passed.')
