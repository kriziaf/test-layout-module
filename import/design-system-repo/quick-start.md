---
title: Design System — Quick Start & File Glossary
description: One-page reference to every artifact and reference file in the ecosystem
version: "1.31"
updated: 2026-07-27
---

# Design System — Quick Start

A multi-brand, token-driven HTML/CSS component library. Components
ship as copy-paste-ready artifacts (markup + CSS, no JavaScript);
one `data-theme` attribute re-themes an entire page across brands.

## Start here

1. **Read `design.md` first.** It's the entry point — a router,
   not a full reference. It maps every file below to the task
   you're trying to do.
2. **Need a component fact?** Check `components.json` before
   reading prose — it's the machine-readable inventory (variants,
   dependencies, tokens, slots) and is validated against the
   actual files, so it doesn't drift.
3. **Need a token value?** `css/tokens.css` is the only source of
   truth for colors, type, radii, and shadows. No other file
   repeats these values — if you see one elsewhere, it's stale.
4. **Building something new?** `design.md`'s task-routing table
   tells you exactly which files to load for components, brands,
   templates, content, or verification — not duplicated here.

## Maturity

This is a **Tier 0** documentation-first system: markdown +
JSON + CSS, meant to be loaded directly (project knowledge,
`@Files`, or pasted into context). It is not yet a generator, CLI,
or MCP server — see `Project-roadmap.md` for that ladder.

---

## File glossary

### A — Design side (reference & standards)

| # | Item | Form | Status |
|---|---|---|---|
| A1 | `design.md` — entry point, ecosystem map, task router | md | ✅ Live |
| A2 | `component-library.md` — token architecture, composition taxonomy, component inventory, interaction states, accessibility standard | md | ✅ Live |
| A3 | `content-system.md` — brand voice, per-component content jobs, canonical copy sets | md | ✅ Live |
| A4 | `layout-module.md` — demo shell, page templates, section rhythm, sync contracts | md | ✅ Live |
| A5 | `brands.md` — brand boundary contract, brand registry, sanctioned exceptions | md | 🔄 Building |
| A6 | `Project-roadmap.md` — phases, parked work, known gaps | md | ✅ Live |

### B — Coded assets

| # | Item | Form | Status |
|---|---|---|---|
| B1 | `variables.json` — upstream design-tool token export | json | ✅ Live |
| B2 | `css/tokens.css` — resolved runtime tokens (semantic → bridge → component) | css | ✅ Live |
| B3 | `components.json` — machine-readable component inventory, validated against the filesystem | json | ✅ Live |
| B4 | `components/<name>/` — artifact trio per component (`.html` / `.css` / `.md`) | files | ✅ Live (10 active, 1 hidden) |
| B5 | `css/base.css`, `css/templates.css` — composition layers (container-query wrapper, section rhythm) | css | ✅ Live |
| B6 | `templates/*.html` — page compositions | html | ✅ Live (3 pages) |
| B7 | `demo.html` — interactive component & template browser | html | ✅ Live |

### C — Reference files

| # | Item | Form | Status |
|---|---|---|---|
| C1 | Sync contracts (source-of-truth vs. copy rules) | section, in `layout-module.md` | ✅ Live |
| C2 | Judgment-call / provenance log (spec'd vs. inferred vs. derived values) | section, in `component-library.md` | ✅ Live |
| C3 | `failure-modes.md` — catalogued traps and their fixes | md | ⏳ Parked |
| C4 | `verification-checklist.md` — the QA pattern as a standalone checklist | md | ⏳ Parked |
| C5 | `glossary.md` — project vocabulary (artifact, bridge variable, content instance, atom vs. pattern-module) | md | ⏳ Parked |
| C6 | `BUILD-BRIEF-*.md` — self-contained task briefs for delegated builds | md | 🆕 Ad hoc, as needed |

### D — Foundation standards

| # | Item | Form | Status |
|---|---|---|---|
| D1 | Composition taxonomy (atom → component → pattern-module → template) | section, in `component-library.md` | ✅ Live |
| D2 | Accessibility standard (focus, semantics, structure, contrast) | section, in `component-library.md` | ✅ Live (not yet audited — see roadmap) |
| D3 | Content voice & per-component copywriting technique | section, in `content-system.md` | ✅ Live |
| D4 | Naming conventions (BEM, bridge namespaces, variant API) | section, in `component-library.md` | ✅ Live |
| D5 | Licensing (Phosphor MIT, licensed CHC fonts) | frontmatter + notes, in `design.md` / `component-library.md` | ✅ Live |
| D6 | Brand boundary contract | `brands.md` | 🔄 Building |

---

*Questions about where something lives? Start at `design.md`'s
task-routing table — it answers "I want to do X, what do I load."*
