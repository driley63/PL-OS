"""Resolve shared component colors in static design-reference styles."""
import json
import re


def bind_component_colors(styles, root):
    tokens = json.loads((root / 'assets/tokens/color.tokens.json').read_text())['component']
    for name, values in tokens.items():
        replacement = f"light-dark({values['light'].lower()},{values['dark'].lower()})"
        styles = styles.replace('__COMPONENT_' + name + '__', replacement)
    unresolved = re.findall(r'__COMPONENT_\w+__', styles)
    if unresolved:
        raise ValueError(f'Unregistered component colors: {unresolved}')
    return styles
