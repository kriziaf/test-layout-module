# Cigna Group Multi-Brand Component Library

A self-describing HTML/CSS component library with a machine-
readable design data schema — read `design.md` first.

## Start here

```
design.md   ← router: non-negotiables, ecosystem map, task-routing table
```

Everything else is reached from there. If you're an AI tool or a
new contributor, read `design.md` before touching any other file.

## Repo layout

```
design.md                  entry point / router
components.json            machine-readable component inventory (validated)
component-library.md       token architecture, taxonomy, a11y standard
content-system.md          voice, per-component content technique
layout-module.md           demo shell, templates, sync contracts
brands.md                  brand boundary, sanctioned exceptions
Project-roadmap.md         parked work, phases, known gaps

css/                       tokens.css, base.css, templates.css
components/<name>/         artifact trio per component (.html + .css + .md)
templates/                 page compositions (content instances)
demo.html                  live component + template browser
scripts/validate.py        the CI check, runnable locally
```

## The two "trios" — read this before adding anything

**Component artifact trio** — every component ships as
`<name>.html` + `<name>.css` + `<name>.md`, together.

**Schema Sync Trio** — every component's entry in
`components.json`, its row in `component-library.md`'s Component
Inventory table, and its row in `content-system.md`'s content-job
table update **together, in the same change.** This is the exact
discipline that prevents documentation from drifting away from
the code — see `design.md`'s non-negotiables for the full rule.

## Validating locally

```bash
python scripts/validate.py
```

Checks: every component declared in `components.json` actually
exists on disk with the variants, bridge namespace, and
dependencies it claims; no component CSS contains a brand-named
selector outside the one sanctioned exception (`header.css`);
every active component has a matching inventory row. This same
script runs in CI on every push and pull request — see
`.github/workflows/validate.yml`.

## Brands

Three production brands (Evernorth, The Cigna Group, Cigna
Healthcare) plus one neutral skin (White Label). See `brands.md`
for the full contract, registry, and the procedure for adding,
changing, or forking to a new brand.

## Status

10 active components, 4 brand modes, 3 page templates. See
`Project-roadmap.md` for what's planned and what's known-gap.
