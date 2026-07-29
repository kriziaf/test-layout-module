#!/usr/bin/env python3
import re
import json
import yaml

MD_PATH = "/home/claude/wp2/components/button-group.md"
ORIGINAL_ENTRY_PATH = "/home/claude/wp2/button-group.entry.json"

with open(MD_PATH) as f:
    text = f.read()

m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
front_matter = yaml.safe_load(m.group(1))

with open(ORIGINAL_ENTRY_PATH) as f:
    original = json.load(f)

print("=== EXPORTED (from components/button-group.md front matter) ===")
print(json.dumps(front_matter, indent=2))
print()

if front_matter == original:
    print("RESULT: IDENTICAL — round-trip clean, field-for-field.")
else:
    print("RESULT: MISMATCH")
    for key in set(front_matter) | set(original):
        if front_matter.get(key) != original.get(key):
            print(f"  DIFF at key '{key}':")
            print(f"    exported: {front_matter.get(key)!r}")
            print(f"    original: {original.get(key)!r}")
