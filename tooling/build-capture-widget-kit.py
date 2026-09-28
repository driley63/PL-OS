"""Package the approved capture-widget assets without regenerating artwork."""
import base64
import hashlib
import json
from pathlib import Path
import re
import shutil
from urllib.parse import unquote
import zipfile

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "assets/widgets/plectara"
PUBLIC = ROOT / "docs/assets/widgets/plectara"
VISUAL = ROOT / "docs/specs/02-design/capture-widget-visuals.md"
BEHAVIOR = ROOT / "docs/specs/02-design/capture-widgets.md"
ZIP_NAME = "plectara-capture-widgets-v1.zip"


def bundled_markdown(path):
    """Keep included links local; send other standards to their canonical page."""
    def link(match):
        target = match.group(1)
        if target.startswith(("https:", "http:", "#", "mailto:")):
            return match.group(0)
        file, separator, anchor = target.partition("#")
        resolved = (path.parent / unquote(file)).resolve()
        if resolved == VISUAL:
            replacement = "specification.md"
        elif resolved == BEHAVIOR:
            replacement = "capture-widgets.md"
        elif resolved.is_relative_to(PUBLIC):
            replacement = resolved.relative_to(PUBLIC).as_posix()
        elif resolved.is_relative_to(ROOT / "docs"):
            relative = resolved.relative_to(ROOT / "docs")
            if relative.suffix == ".md":
                relative = relative.parent if relative.name == "README.md" else relative.with_suffix("")
                replacement = "https://pl-os.plectara.com/" + relative.as_posix().rstrip("/") + "/"
            else:
                replacement = "https://pl-os.plectara.com/" + relative.as_posix()
        else:
            raise ValueError(f"Unmapped package link in {path}: {target}")
        return "](" + replacement + (separator + anchor if separator else "") + ")"

    return re.sub(r"\]\(([^\s)]+)\)", link, path.read_text())


def main():
    (KIT / "specification.md").write_text(bundled_markdown(VISUAL))
    (KIT / "capture-widgets.md").write_text(bundled_markdown(BEHAVIOR))
    fragment = (KIT / "reference/approved-mockup-fragment.html").read_text()
    assets = json.loads(re.search(r'<script type="application/json" id="pg-assets">([\s\S]*?)</script>', fragment)[1])
    texture = KIT / "textures/plectara-widget-yarn-gentle-focus-v1.webp"
    assert base64.b64decode(assets["texture"].split(",", 1)[1]) == texture.read_bytes(), "Embedded texture drift"
    assert 'data-action="Edit"' not in fragment, "Unsupported widget Edit action"
    for label in ["Overnight Oats", "Salmon Bowl", "Neighborhood Walk", "Evening Yoga"]:
        assert f'<span class="pg-label">{label}</span>' in fragment, label
    for key, name in [("color", "horizontal-reversed"), ("mono", "horizontal-white"), ("symbol", "symbol-white")]:
        canonical = ROOT / f"assets/brand/plectara/source/plectara-{name}.svg"
        assert base64.b64decode(assets[key].split(",", 1)[1]) == canonical.read_bytes(), name
        assert (KIT / f"logos/plectara-{name}.svg").read_bytes() == canonical.read_bytes(), name
    for family, size in [("small", (340, 340)), ("medium", (720, 340)), ("large", (720, 752))]:
        for appearance in ["light", "dark"]:
            path = KIT / f"previews/home-{family}-{appearance}.png"
            with Image.open(path) as image:
                assert image.size == size, path
                assert image.mode == "RGBA", path
                assert all(image.getpixel(point)[3] == 0 for point in [(0, 0), (size[0]-1, 0), (0, size[1]-1), (size[0]-1, size[1]-1)]), path
    inventory = []
    for path in sorted(KIT.rglob("*")):
        if not path.is_file() or path.name in ["manifest.json", ZIP_NAME, ".DS_Store"]:
            continue
        relative = path.relative_to(KIT).as_posix()
        entry = {"file": relative, "role": relative.split("/", 1)[0], "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        if path.suffix.lower() in [".png", ".webp"]:
            with Image.open(path) as image:
                entry.update(width=image.width, height=image.height, mode=image.mode)
        inventory.append(entry)
    manifest = {
        "asset_id": "plectara-capture-widgets",
        "version": 1,
        "status": "owner-approved design reference; PL-OS v2.5.0 publication pending",
        "approval_date": "2026-09-28",
        "design_review_revision": 13,
        "specification": "docs/specs/02-design/capture-widget-visuals.md",
        "default_texture": "textures/plectara-widget-yarn-gentle-focus-v1.webp",
        "native_source": "textures/plectara-widget-yarn-gentle-focus-v1.png",
        "screenshot_scale": 2,
        "native_implementation_included": False,
        "files": inventory,
    }
    (KIT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    # Fixed ZIP metadata makes packaging repeatable from the same approved files.
    with zipfile.ZipFile(KIT / ZIP_NAME, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for entry in inventory + [{"file": "manifest.json"}]:
            path = KIT / entry["file"]
            info = zipfile.ZipInfo(entry["file"], (2026, 9, 28, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    PUBLIC.mkdir(parents=True, exist_ok=True)
    shutil.copytree(KIT, PUBLIC, dirs_exist_ok=True)
    with zipfile.ZipFile(KIT / ZIP_NAME) as archive:
        for entry in inventory:
            source = (KIT / entry["file"]).read_bytes()
            assert archive.read(entry["file"]) == source, entry["file"]
            assert (PUBLIC / entry["file"]).read_bytes() == source, entry["file"]
    print(json.dumps({"files": len(inventory), "zip_bytes": (KIT / ZIP_NAME).stat().st_size, "exact_texture": True, "canonical_logos": True, "six_transparent_screenshots": True, "zip_and_docs_parity": True}))


if __name__ == "__main__":
    main()
