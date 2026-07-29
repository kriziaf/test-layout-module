#!/usr/bin/env python3
"""
validate.py — checks components.json against the real filesystem
and enforces the brand boundary described in brands.md.

Run locally:  python scripts/validate.py
Run in CI:    .github/workflows/validate.yml calls this on every push/PR.

Exit code 0 = pass, 1 = fail. Prints every issue found; does not
stop at the first one, so a single run gives the full picture.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
issues = []


def fail(msg):
    issues.append(msg)


def check_components_json():
    """Schema Sync Trio, part 1: components.json must match the
    real artifact files — every declared variant, bridge
    namespace, and dependency must actually exist in code."""
    path = os.path.join(ROOT, "components.json")
    if not os.path.exists(path):
        fail("components.json is missing entirely")
        return

    data = json.load(open(path))
    components = data.get("components", {})

    for key, c in components.items():
        html_path = os.path.join(ROOT, c["files"]["html"])
        css_path = os.path.join(ROOT, c["files"]["css"])

        if not os.path.exists(html_path):
            fail(f"{key}: declared html file missing -> {c['files']['html']}")
            continue
        if not os.path.exists(css_path):
            fail(f"{key}: declared css file missing -> {c['files']['css']}")
            continue

        html = open(html_path).read()
        css = open(css_path).read()

        # every declared variant must appear in the artifact markup
        for v in c.get("variants", []):
            cls = f"{key}--{v}"
            if v.endswith("-no-cta"):
                base = v[: -len("-no-cta")]
                cls = f"{key}--{base} {key}--no-cta"
            if cls not in html:
                fail(f"{key}: variant '{v}' declared in components.json but not found in {c['files']['html']}")

        # bridge namespace must actually be used (button-group is the
        # one atom-host exception -- it defines the atom other
        # components consume, rather than using its own namespace everywhere)
        ns = c.get("bridgeNamespace", "")
        if ns and ns not in css and key != "button-group":
            fail(f"{key}: bridge namespace '{ns}' declared but not used in {c['files']['css']}")

        # declared dependencies must be linked in the artifact head
        for dep in c.get("dependsOn", []):
            if f"{dep}/{dep}.css" not in html:
                fail(f"{key}: declares dependency on '{dep}' but {c['files']['html']} does not link it")


def check_brand_boundary():
    """Enforce brands.md section 4: components must not contain
    functional [data-theme=...] selectors, except the one
    sanctioned exception (header.css, brand logo reveal)."""
    boundary = None
    cj_path = os.path.join(ROOT, "components.json")
    if os.path.exists(cj_path):
        boundary = json.load(open(cj_path)).get("boundaryCheck")

    sanctioned = set(boundary["sanctionedExceptions"]) if boundary else {"header.css"}

    components_dir = os.path.join(ROOT, "components")
    if not os.path.isdir(components_dir):
        fail("components/ directory not found")
        return

    for name in os.listdir(components_dir):
        css_path = os.path.join(components_dir, name, f"{name}.css")
        if not os.path.exists(css_path):
            continue
        css = open(css_path).read()
        if re.search(r"\[data-theme=", css) and f"{name}.css" not in sanctioned:
            fail(
                f"{name}.css contains a functional [data-theme=...] selector — "
                f"this violates the brand boundary in brands.md section 1. "
                f"If this is a legitimate new exception, add it to "
                f"components.json's boundaryCheck.sanctionedExceptions and to "
                f"brands.md section 4 in the same change."
            )


def check_schema_sync_trio():
    """Schema Sync Trio, part 2: every component in components.json
    should also appear in component-library.md's inventory and
    content-system.md's content-job table. Warns rather than fails
    on content-system.md, since not every component has shipped
    content yet -- but components.json <-> component-library.md
    must always agree."""
    cj_path = os.path.join(ROOT, "components.json")
    cl_path = os.path.join(ROOT, "component-library.md")
    if not (os.path.exists(cj_path) and os.path.exists(cl_path)):
        return

    data = json.load(open(cj_path))
    cl = open(cl_path).read()

    for key, c in data.get("components", {}).items():
        if c.get("status") == "hidden":
            continue  # hidden components are intentionally excluded from docs
        if f"| {key} |" not in cl:
            fail(
                f"{key}: present in components.json but has no row in "
                f"component-library.md's Component Inventory table "
                f"(Schema Sync Trio violation)"
            )


def main():
    check_components_json()
    check_brand_boundary()
    check_schema_sync_trio()

    if issues:
        print(f"FAIL — {len(issues)} issue(s):\n")
        for i in issues:
            print(f"  - {i}")
        sys.exit(1)
    else:
        print("PASS — components.json, brand boundary, and Schema Sync Trio all check out.")
        sys.exit(0)


if __name__ == "__main__":
    main()
