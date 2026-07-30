---
title: Design Data Schema — SCHEMA
version: "1.36"
updated: 2026-07-29
brands: [evernorth, tcg, chc, white-label]
themeAttribute: data-theme
componentCount: 12
---

# Design Data Schema

Load this file immediately after `design.md`. It replaces
`design-schema.json` and `reference/README.md` — everything an
agent needs to orient, route, and act is here.

---

## Non-negotiables

Break any of these and the build is wrong regardless of how good
the output looks:

1. **No JavaScript** in component CSS or HTML artifacts.
2. **Never hardcode a color** outside `tokens.md` / `css/tokens.css`.
3. **No `[data-theme]` selectors in component CSS** — the one
   sanctioned exception is `header.css` (brand logo reveal). Any
   new component that seems to need one is wrong; the value belongs
   in the token layer instead.
4. **Never edit `css/tokens.css` directly** — run
   `scripts/build.py` after editing `tokens.md`.
5. **Schema Sync Trio on every component change** —
   `components.json` + `component-library.md` + `content-system.md`
   always updated together, never one without the others.
6. **Artifacts are source of truth** — `demo.html` and
   `templates/*.html` are downstream copies, not originals.

---

## Layer map

| Layer | Name | Files | Editable? |
|---|---|---|---|
| Router | Entry point | `design.md` → `SCHEMA.md` | Maintainers only |
| **1** | Design Data Schema | `tokens.md`, `components.json`, `component-library.md`, `content-system.md`, `brands.md`, `components/<name>/<name>-spec.md` | **No — read only** |
| **2** | Coded Assets | `css/tokens.css` *(generated)*, `css/base.css`, `css/templates.css`, `components/<name>/<name>.html/css/md` | **No — generated or hand-authored against Layer 1** |
| **3** | Customization | `skills/`, `layout-module.md` | **Yes — user space** |

---

## File roles

| File | What it is | Load when |
|---|---|---|
| `tokens.md` | **Token source of truth** — all brand, spacing, shadow, breakpoint values. Generates `css/tokens.css`. | Any token, brand, or styling work |
| `components.json` | Machine-readable component inventory — variants, deps, slots, tokensConsumed, grids | Any component work |
| `component-library.md` | Token architecture, composition taxonomy, interaction states, a11y standard | Building or extending components |
| `content-system.md` | Content jobs, technique table, virtual-care voice content | Writing any user-facing copy |
| `brands.md` | Brand contract, boundary rules, per-brand deviations, add/swap procedures | Adding or changing a brand |
| `skills/build-component/SKILL.md` | Step-by-step build procedure + known pitfalls | Before building or extending any component |
| `layout-module.md` | Section rhythm, sync contracts, demo shell architecture | Template or demo work |
| `scripts/build.py` | `tokens.md → css/tokens.css` emitter | After any `tokens.md` change |
| `scripts/validate_roundtrip.py` | Round-trip diff check — wire into CI | After any token build |

---

## Task routing

| I want to… | Load | Key rule |
|---|---|---|
| **Build a new component** | `skills/build-component/SKILL.md`, `components.json`, `component-library.md`, `brands.md` | Ship artifact trio; update Schema Sync Trio; register in demo |
| **Add a component variant** | `components.json` (that entry), its artifact trio | Variant = modifier class on section root |
| **Change a token / add a new one** | `tokens.md` → `scripts/build.py` | Never touch `css/tokens.css` directly |
| **Add or change a brand** | `tokens.md` (brands block), `brands.md` | One `[data-theme]` block in `tokens.md`; no component CSS changes |
| **Write or revise copy** | `content-system.md`, that component's `.md` | Match content job; reshape shared content, don't reinvent |
| **Build a page template** | `layout-module.md`, `components.json` | Template skill not yet built — see parked work |
| **Understand a component's full spec** | `components/<name>/<name>-spec.md` | Button Group and Promo Banner migrated; others pending WP3 |

---

## Worked examples (Claude Code)

**Token pattern** — see `tokens.md` for values, `css/tokens.css`
for the generated output. Never copy from `css/tokens.css`; copy
the pattern and resolve values from `tokens.md`.

**Component artifact pattern** — Button Group is the simplest,
most self-contained example:
```
components/button-group/button-group.html   ← markup
components/button-group/button-group.css    ← styles + bridge vars
components/button-group/button-group.md     ← content notes
components/button-group/button-group-spec.md ← Layer 1 hybrid spec
```

**New component spec pattern** — Promo Banner shows the full
decision trail for a new candidate component:
```
components/promo-banner/promo-banner-spec.md
```

---

## Parked work (do not build)

| Item | Status |
|---|---|
| WP3 — 9 remaining component hybrid specs | Designed, not built |
| `content-standard.md` + `voices/` split | Designed, not built |
| `templates.json` + `skills/build-template/` | Designed, not built |
| Promo Banner artifact trio (HTML/CSS/MD) | Spec exists, code does not |
| Non-Evernorth accent button specs | Provisional / unverified contrast |
| TCG/CHC/White Label `bg-brand-xstrong` values | Extrapolated, not design-sourced |
