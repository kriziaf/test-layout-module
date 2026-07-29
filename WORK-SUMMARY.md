# Session Handoff — WP1–WP3 Summary + Parked Plan

**For:** picking this repo up in Claude Code
**Repo state at handoff:** v1.35, 3 commits on `main`, not yet pushed to GitHub
**Read `design.md` first** — this document is a one-time kickoff
note, not part of the standing schema reference set.

---

## WP1 — Component Library Build

The base product: a multi-brand HTML/CSS component library, no
JavaScript in components, everything token-driven.

- **10 active components** (11 built; `icon-cards` intentionally
  hidden — files intact, commented out of the demo, status
  `"hidden"` in `components.json`): Header, Hero, Text and Image,
  Form, List Item, Heading Block, Horizontal Cards, External Link
  Cards, Highlight Bar, Button Group.
- **4 brand modes:** Evernorth, The Cigna Group, Cigna
  Healthcare, White Label (neutral skin) — one `data-theme`
  attribute re-themes an entire page.
- **3 page templates** (content instances, not artifact-pure):
  Homepage — Virtual Care, Insights Page, Contact Us. An earlier
  set (Templates A/B/C, CoverMyMeds-themed) was built, then
  retired and deleted once these three shipped.
- **Content system:** one consistent virtual-care brand voice
  across 7 of the content-bearing components, each following a
  named copywriting technique (value proposition, wayfinding,
  proof-and-trust, etc.) — see `content-system.md`.
- **The `.btn` atom:** four components (Form, Hero, Text and
  Image, Heading Block) were refactored to consume one shared
  button atom instead of duplicating button CSS.
- **Verification discipline:** every change was checked with a
  headless browser across variant × brand × breakpoint, plus
  interactive-state simulation (hover/press/tab) — not visual
  inspection alone. See `layout-module.md`'s verification
  pattern.

**Real bugs hit and fixed along the way** (the reason WP3's CI
exists): stale-content regex assumptions after a content rollout,
non-greedy string matching grabbing the wrong HTML boundary,
transparent-margin vs. painted-padding for section gaps, named
vs. unnamed CSS container queries silently not matching, nested
`<a>` tags, and template-registry drift across three separate
locations. Full pitfalls list: `skills/build-component/SKILL.md`.

## WP2 — Design Data Schema (Context Foundation)

Turned the implicit knowledge from WP1 into a portable,
machine-checkable schema — the actual point of this project past
the component library itself.

- **`design.md`** — router: non-negotiables, ecosystem map,
  task-routing table. Read this before anything else.
- **`components.json`** — machine-readable inventory: every
  component's variants, file paths, dependencies, bridge
  namespace, tokens consumed, slots, grid behavior, content job.
  Includes a `boundaryCheck` block encoding the brand-boundary
  rule as data, not just prose.
- **`component-library.md`** — token architecture (3-layer
  model), composition taxonomy (atom → component →
  pattern-module → template), interaction-state specs, and a
  written Accessibility Standard (documented, not yet formally
  audited — see Parked Plan below).
- **`content-system.md`** — brand voice + per-component-type
  copywriting technique.
- **`layout-module.md`** — demo shell, template composition,
  sync contracts (the drift risks to watch for).
- **`brands.md`** — the brand boundary as a standing reference:
  the contract (one `[data-theme]` block per brand, nothing
  else), the registry, the one sanctioned exception (Header's
  logo reveal), and add/swap/remove/fork procedures.
- **`ecosystem-flow.md`**, **`executive-summary.md`**,
  **`quick-start.md`** — a Mermaid diagram of how all the above
  relate (with the `components.json` validation loop as the key
  thing to understand), a leadership one-pager with a staffing/
  timeline ask for Tiers 1–2, and a one-page doc-site glossary.

**The core discipline this introduced: the Schema Sync Trio.**
`components.json`, `component-library.md`'s inventory table, and
`content-system.md`'s content-job table must update together,
every time a component is added — same change, not three
separate ones. This is the schema-level equivalent of the
component-level artifact trio (`.html`+`.css`+`.md`).

## WP3 — Repo Infrastructure & Reusability

Made the schema something that can leave this one project intact.

- **Git repo scaffolded**, `main` branch, 3 commits.
- **`.github/workflows/validate.yml`** + **`scripts/validate.py`**
  — CI that runs the Schema Sync Trio and brand-boundary checks
  on every push/PR. Tested against a deliberate violation before
  trusting it (confirmed it fails correctly, not just always
  passes).
- **`skills/build-component/SKILL.md`** — a reusable Agent Skill
  encoding the full "build one component correctly" procedure:
  source decoding → token resolution → artifact trio → Schema
  Sync Trio update → registration → verification, plus the
  pitfalls list from WP1's real bugs.
- **Portable core packaging** — the 7 schema docs + the skill,
  exportable independently of the component code, for dropping
  into a new Claude Project or a different tool entirely.
- **Consolidation:** an earlier working folder
  (`component-library/`) that had drifted from the repo was
  diffed, anything real merged in, then retired — the repo is
  now the single edited copy.

---

## Parked Plan — full detail lives in `Project-roadmap.md`

Condensed here for orientation; **read the actual file for the
complete reasoning behind each item** — this project's own rule
is "don't duplicate a source of truth in a second file," so this
table is intentionally the short version.

| Phase | Item | Status |
|---|---|---|
| Phase 2 | Accessibility audit (axe/Lighthouse, screen reader) | Not started — standard is documented, not verified |
| Phase 2 | Schema Tier 1 — generate markdown tables from `components.json` instead of hand-maintaining them | Not started; permanent fix for doc-drift class of bug |
| Phase 2 | Schema Tier 2 — npm package + CLI (`resolve-token`, `describe-component`, `validate-usage`) | Not started |
| Phase 2 | Schema Tier 3 — MCP server / Agent Skill distribution | Not started; Adobe Spectrum Design Data is the reference pattern |
| Phase 2 | Doc ecosystem expansion: `templates-building-guide.md`, `component-building-guide.md`, `theming-guide.md`, `lessons-learned.md`, `verification-checklist.md`, `glossary.md` | Parked; some overlap now covered by `skills/build-component/SKILL.md`'s pitfalls section |
| Phase 2 | Content rollout: Heading Block still has placeholder content | Deferred by request; may not need independent content since it's always embedded |
| Phase 2 | Grid-system consistency audit (4-across vs. 3-across across components) | Not started; one instance (`list-item--accent`) fixed as a one-off |
| Phase 2 | Template-stack manifest / build script | Not started; drift between `templates/*.html` and the demo registry has caused repeat bugs |
| Phase 2 | Section-rhythm generalization, List Item naming trap, White Label logo, CHC licensed fonts, non-Evernorth accent buttons, Text and Image cutout clip-path | All parked, individually small |
| **Phase 2.5** | **Re-map schema to Claude Design.** Empirical test first: point Claude Design's onboarding at this repo and record what it actually extracts vs. misses before building anything speculative. Depends on `brands.md` (done). | Not started — see `Project-roadmap.md` for the full reasoning (output-format gap, missing visual specimen) |
| Phase 3 | Attribute-based variant API (`data-variant`/`data-theme` replacing BEM modifier classes) — breaking, reserved as v2.0 | Not started |

## Suggested immediate next actions

1. Push to GitHub (`git remote add origin <url> && git push -u
   origin main`) if not already done.
2. Confirm the `validate` CI check actually runs on GitHub's
   Actions tab after the push.
3. Add branch protection on `main` requiring `validate` to pass
   — this is what makes the Schema Sync Trio *enforced*, not just
   documented.
4. Pick the next Phase 2 item based on priority — the
   accessibility audit and the Tier 1 generator script are the
   two with the clearest immediate payoff.
