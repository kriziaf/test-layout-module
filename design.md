---
title: Design System — Entry Point
version: "1.31"
updated: 2026-07-27
kind: manifest
brands: [evernorth, tcg, chc, white-label]
delivery: html + css artifacts, no JavaScript in components
license: { icons: "Phosphor (MIT)", fonts: "Google Fonts; CHC uses licensed Value Serif/Sans Pro" }
entryPoint: true
---

# Design System — Entry Point

**Read this file first. Load the others on demand.**

Multi-brand HTML/CSS component library. Components are
copy-paste-ready artifacts: everything inside an artifact's
`<body>` ships as-is. One `data-theme` attribute re-themes an
entire page across four brands.

## Non-negotiables

1. **No JavaScript in components.** The one interactive pattern
   (Header's mobile menu) is a CSS-only checkbox toggle.
2. **Never hardcode a color, font, or radius outside
   `css/tokens.css`.** Components read semantic tokens through
   their `--<ns>-*` bridge variables.
3. **Artifacts are the source of truth for markup.** `demo.html`
   and `templates/*.html` contain COPIES; re-extract after any
   artifact edit.
4. **No `!important` in component CSS.** Composition layers may
   use element+class specificity (`section.x`) instead.
5. **Container queries only** — never viewport media queries.
   Every section wraps in `.component-viewport`.
6. **Accessibility rules are requirements, not preferences.**
   See the Accessibility Standard in `component-library.md`.

## Ecosystem map

| File | What it is | Load when |
|---|---|---|
| `design.md` | This manifest + task router | Always |
| `components.json` | Machine-readable inventory: variants, deps, slots, tokens, grids, states | Any component work |
| `css/tokens.css` | Resolved runtime tokens, one block per brand | Any styling work |
| `variables.json` | Upstream design-tool export (alias chains) | Adding/resolving tokens |
| `component-library.md` | System reference: token architecture, taxonomy, interaction states, a11y standard | Building or extending components |
| `content-system.md` | Voice, per-component content jobs, canonical copy sets | Writing any user-facing copy |
| `layout-module.md` | Demo shell + page templates + section rhythm + sync contracts | Template or demo work |
| `failure-modes.md` | Catalogued traps and their fixes | Before any bulk edit or refactor |
| `Project-roadmap.md` | Parked work, phases, known gaps | Planning |
| `components/<name>/` | Artifact trio per component | Working on that component |
| `templates/` | Page compositions (all content instances) | Building pages |

## Task routing

| I want to… | Load | Key constraint |
|---|---|---|
| **Build a new component** | `components.json`, `component-library.md`, `failure-modes.md` | Ship the artifact trio; register in demo; verify variant × brand × breakpoint |
| **Add a variant to an existing component** | `components.json` (that entry), its artifact trio | Variant = modifier class on the section root; update `components.json` |
| **Change a component's styling** | `css/tokens.css`, that component's `.css` | Change the token, not the rule, if it's a color/type/radius |
| **Add or change a brand** | `variables.json`, `css/tokens.css`, `component-library.md` (token architecture) | Add one `[data-theme]` block; touch no component CSS |
| **Add a new token** | `variables.json` → `css/tokens.css` → the consuming bridge | Document as spec'd, derived, or provisional |
| **Build a page template** | `layout-module.md`, `components.json`, `templates/` | Extract markup from artifacts; rewrite img paths; register in demo |
| **Write or revise copy** | `content-system.md`, that component's `.md` | Match the component's content job; reshape shared content, don't reinvent |
| **Wire something into the demo** | `layout-module.md` (demo shell + sync contracts) | Registry entry + `<template>` copies + annotation copy |
| **Verify a change** | `layout-module.md` (verification pattern), `failure-modes.md` | Measure computed styles and paint, not just geometry |
| **Understand why something is the way it is** | `component-library.md` (judgment calls), `Project-roadmap.md` | Distinguish spec'd from inferred before "fixing" it |

## Quick reference

**Token architecture — three layers:**

```
[data-theme="evernorth"] { --color-content-brand: #035C67; }  1. semantic, per brand
.list-item { --li-accent: var(--color-content-brand); }        2. component bridge
.list-item__heading { color: var(--li-accent); }               3. component rule
```

Setting `data-theme` on any ancestor themes everything below it.
Mixed-theme pages are legal.

**Artifact trio — every component ships three files:**

| File | Contains |
|---|---|
| `<name>.html` | Shippable markup, one self-contained section per variant, plus a banner documenting required includes, variant API, and content slots |
| `<name>.css` | Component styles, consuming `--<ns>-*` bridge variables |
| `<name>.md` | Content annotations: short description, content guidance, marketing notes — never spec descriptions |

**Composition taxonomy:** atom → component → pattern-module →
template. See `component-library.md` for what belongs at each
level.

## Status & provenance

- **Stable:** 10 components, 3 page templates, 4 brand modes.
- **Hidden:** `icon-cards` — files intact, commented out of the
  demo and omitted from docs (v1.27).
- **Provisional values** are marked inline where they occur.
  Anything labelled *derived* or *inferred* was not in the design
  source and is a candidate for replacement when specs arrive.
- **Versioning:** lockstep across the library; every change
  bumps. Breaking changes are called out in artifact banners.
  v2.0 is reserved for the attribute-based variant API
  (`data-variant`), see `Project-roadmap.md` Phase 3.
