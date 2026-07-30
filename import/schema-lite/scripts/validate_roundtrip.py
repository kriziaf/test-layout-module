#!/usr/bin/env python3
import re, sys

def extract(path):
    with open(path) as f:
        text = f.read()
    blocks = {}
    for m in re.finditer(r'^([.\[][^\{\n]*)\s*\{([^}]*)\}', text, re.S | re.M):
        selector = m.group(1).strip()
        body = m.group(2)
        props = {}
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith("/*"):
                continue
            dm = re.match(r'(--[a-zA-Z0-9-]+)\s*:\s*([^;]+);', line)
            if dm:
                props[dm.group(1)] = dm.group(2).strip()
        blocks[selector] = props
    return blocks

orig = extract("/home/claude/wp1/tokens.original.css")
gen = extract("/home/claude/wp1/tokens.built.css")

all_selectors = sorted(set(orig) | set(gen))
mismatches = 0
for sel in all_selectors:
    o = orig.get(sel, {})
    g = gen.get(sel, {})
    if sel not in orig:
        print(f"EXTRA selector in generated: {sel}")
        mismatches += 1
        continue
    if sel not in gen:
        print(f"MISSING selector in generated: {sel}")
        mismatches += 1
        continue
    o_keys, g_keys = set(o), set(g)
    for k in o_keys - g_keys:
        print(f"[{sel}] MISSING prop in generated: {k}: {o[k]}")
        mismatches += 1
    for k in g_keys - o_keys:
        print(f"[{sel}] EXTRA prop in generated: {k}: {g[k]}")
        mismatches += 1
    for k in o_keys & g_keys:
        if o[k] != g[k]:
            print(f"[{sel}] VALUE MISMATCH {k}: original={o[k]!r} generated={g[k]!r}")
            mismatches += 1

print()
print(f"Selectors compared: {len(all_selectors)}")
print(f"Mismatches: {mismatches}")
sys.exit(1 if mismatches else 0)
