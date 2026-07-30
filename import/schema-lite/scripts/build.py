#!/usr/bin/env python3
"""
THE actual build step: tokens.md -> css/tokens.css.
Run this; tokens.css is never hand-edited again.
"""
import yaml
import re
import sys

def load_front_matter(md_path):
    with open(md_path) as f:
        text = f.read()
    m = re.match(r'^---\n(.*?)\n?---\n', text, re.S)
    if not m:
        print("ERROR: no front matter found"); sys.exit(1)
    return yaml.safe_load(m.group(1))

BRAND_ORDER = ["evernorth", "tcg", "chc", "white-label"]

def build(md_path, out_path):
    fm = load_front_matter(md_path)
    out = []
    out.append("/* ============================================================")
    out.append(f"   {out_path.split('/')[-1]} — GENERATED from tokens.md. Do not hand-edit.")
    out.append("   Regenerate with: python3 build.py")
    out.append("   ============================================================ */")
    out.append("")

    glob = fm.get("global")
    if glob:
        out.append('/* ---- Global tokens (theme-independent) ---- */')
        out.append(":root {")
        for group_key in ("spacing", "shadow", "breakpoints"):
            group = glob.get(group_key, {})
            for prop, val in group.items():
                if prop == "note":
                    out.append(f'  /* {val} */')
                    continue
                out.append(f'  {prop}: {val};')
        out.append("}")
        out.append("")

    for theme_id in BRAND_ORDER:
        brand = fm["brands"][theme_id]
        notes = brand.get("notes") or {}
        out.append(f'/* ---- Mode: {brand["label"]} ---- */')
        out.append(f'[data-theme="{theme_id}"] {{')
        for prop, val in brand["values"].items():
            line = f'  {prop}: {val};'
            if prop in notes:
                line += f'   /* {notes[prop]} */'
            out.append(line)
        out.append("}")
        out.append("")

    for selector, bridge in fm["bridges"].items():
        if bridge.get("note"):
            out.append(f'/* {bridge["note"]} */')
        out.append(f'{selector} {{')
        for prop, val in bridge["values"].items():
            out.append(f'  {prop}: {val};')
        out.append("}")
        out.append("")

    with open(out_path, "w") as f:
        f.write("\n".join(out).rstrip() + "\n")
    print(f"Built {out_path} from {md_path}")

if __name__ == "__main__":
    build("/home/claude/wp1/tokens.md", "/home/claude/wp1/tokens.built.css")
