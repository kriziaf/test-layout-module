# Project Roadmap

Running shelf of deferred and planned work for the component
library. Current release: v1.23.

## Phase 2 — Consistency & Polish

- **`brands.md` — DONE (v1.34).** Brand boundary reference
  built: brand contract, registry (3 brands + 1 neutral
  skin), required token-surface checklist, the Header-logo
  sanctioned exception, per-brand deviations, and add/swap/
  remove/fork procedures. Boundary claim verified against
  the codebase (only header.css has functional [data-theme]
  selectors) and encoded as `components.json.boundaryCheck`.

- **Ecosystem flow diagram + executive summary — DONE (v1.32).**
  `ecosystem-flow.md` (Mermaid, five-layer flow + the
  components.json validation loop) and `executive-summary.md`
  (leadership one-pager: problem, solution, Tier 0 status, Tier
  1-2 timeline and staffing ask) both shipped. Doc-site quick
  reference is a separate deliverable, not yet started.

- **Accessibility audit (NEW).** The Accessibility Standard is
  now written down in `component-library.md` and is enforced by
  construction, but no automated axe/Lighthouse pass and no
  screen-reader testing has been done. Run both and record
  results; the standard currently documents intent, not
  verified conformance.
- **Design system schema — Tier 1+ (NEW).** `design.md` (entry
  point/router) and `components.json` (machine-readable
  inventory) shipped in v1.31 as Tier 0. Remaining tiers:
  Tier 1 — adopt the `llms.txt` convention and generate the
  markdown inventory tables FROM `components.json` instead of
  hand-maintaining them (this is the permanent fix for the
  doc-drift class of bug). Tier 2 — npm package + CLI
  (`resolve-token`, `describe-component`, `validate-usage`).
  Tier 3 — MCP server / Agent Skill, per the Adobe Spectrum
  Design Data pattern.

- **Documentation ecosystem expansion (NEW, PARKED).** Three
  procedural how-to guides to complement the existing reference
  docs (do not duplicate — component-library.md and
  layout-module.md already cover the "what exists" side):
  - `templates-building-guide.md` — how to build a new page
    template (content-instance vs artifact-pure, the
    extract-from-artifact pattern and its known failure modes,
    section rhythm, demo registration, version-bump checklist).
    The one genuine gap; nothing like this exists yet.
  - `component-building-guide.md` — how to build a new
    component (design decoding technique, token resolution from
    variables.json, Phosphor icon sourcing, the artifact-trio
    contract, verification checklist).
  - `theming-guide.md` — how to extend theming (adding a brand,
    the alias-resolution algorithm, the provisional-token and
    White-Label-neutralization conventions).
  - UI Shell Demo: no new file — add a short "wiring in a new
    component" section to layout-module.md instead.
  Also worth considering when this is picked up: a
  `lessons-learned.md` (recurring bug classes: stale-content
  regex assumptions, non-greedy over-matching, nested-anchor
  traps, margin-vs-padding paint bugs, named-vs-unnamed
  container queries, TEMPLATES-object drift, `__header`/
  `__heading` collisions), a `verification-checklist.md` (the
  Playwright QA pattern as a standalone reusable checklist), and
  a `glossary.md` (artifact, bridge variable, content instance,
  atom vs pattern-module, `tpl-*` composition class).

- **Content system rollout — DONE for 7 of 8 active
  content-bearing components** (v1.25–v1.26): Hero, List Item,
  Horizontal Cards, External Link Cards, Highlight Bar, Form,
  Text and Image all follow the single virtual-care voice
  documented in `content-system.md`. Remaining by request:
  **Heading Block** still carries generic placeholder content
  ("Your title here") — its content is inherited wherever it's
  embedded, so it may not need independent rewriting at all.

- **Grid-system consistency audit (NEW).** Column counts across
  grid-bearing components grew ad hoc rather than deliberately:
  `list-item` (links/stats/articles) runs 4-across at desktop,
  while `horizontal-cards`, `external-link-cards`, and
  `list-item--accent` all run 3-across. The
  `list-item--accent` mismatch (was rendering 4 instead of the
  intended 3) was fixed directly as a one-off override, but the
  underlying inconsistency across the rest of the library
  remains. Audit every grid component, decide per-component
  column counts deliberately (or standardize), and document the
  reasoning — rather than leaving it implicit in whichever CSS
  happened to get copied when the component was built.
- **Template-stack manifest / build script** — one source that
  generates both `templates/*.html` and the demo TEMPLATES
  object (drift between them has caused three bugs to date).
- **Section-rhythm generalization** — `templates.css` currently
  assumes white surfaces; add surface classes for tinted bands.
- **List Item naming trap** — `__header` (section) vs
  `__heading` (item) one-letter collision; candidate rename
  `__item-title`.
- **White Label logo** — Header ships a text placeholder.
- **CHC licensed webfonts** — Value Serif/Sans Pro @font-face
  drop-in (Georgia/Helvetica fallbacks today).
- **Non-Evernorth accent buttons** — TCG/CHC/WL inverse sets
  are derived white-on-brand; swap values when specs arrive.
- **Text and Image cutout** — clip-path version (currently a
  baked transparent PNG).

## Phase 2.5 — Re-map Design Data Schema to Claude Design

Claude Design's onboarding reads a team's codebase/design files
and builds a design system (colors, typography, components) that
every subsequent project uses automatically, and supports
maintaining more than one design system per team. That's
structurally the same job this schema already does manually —
worth testing directly rather than assuming fit.

- **Empirical test (do this first).** Point Claude Design at the
  current repo/zip and record what its onboarding actually
  extracts vs. misses, before building anything speculative.
- **Output-format gap.** This library ships static HTML+CSS with
  zero JavaScript, hand-authored BEM + CSS custom properties.
  Claude Design's generated output may be framework-flavored
  (React/Tailwind-leaning per public reporting). If the
  onboarding reader wants that shape, a mapping layer
  (components-as-React or a Tailwind config generated from
  `tokens.css`) may be needed — confirm via the test above before
  building it.
- **No visual specimen exists.** Everything in the schema today
  is text/code (md, json, css, html). A vision-capable onboarding
  flow may extract more reliably from a rendered style-tile or
  component screenshot sheet than from CSS alone. `demo.html` is
  the closest thing today but is a live app, not a static image
  asset. Candidate: a generated PNG/SVG specimen sheet, one frame
  per component per brand.
- **`brands.md` is the direct enabler** for "maintain more than
  one design system" — finish it (already planned) with this use
  case explicitly in mind: the brand/architecture split is what
  would let Claude Design apply one team's structure to a
  different brand's values without re-deriving the system.
- **Depends on:** `brands.md` (Phase 2), and is otherwise
  independent of Phase 3.

## Phase 3 — Attribute-Based Variant API

- **`data-variant` + `data-theme` on component roots**,
  replacing BEM modifier classes as the variant/theme API.
  Breaking change; reserved as v2.0. Open naming decision:
  `3-up` vs `three-up` as the attribute value style.



## Template concepts (virtual-care 3-page set — Homepage shipped as templates/template-homepage.html, v1.23)

**Page 2 — Services Page (parked, recommended architecture)**
Goal: let a visitor land on one specific service (e.g. Primary
Care, Mental Health, Urgent Care, Prescription Refills) and
convert. Recommended stack: Header → Hero (default, service-
specific headline: e.g. "Mental health support, on your
schedule") → Heading Block (left, no-CTA) + List Item (links
variant, "What's included" — 4 items with links to specifics) →
Highlight Bar (metrics — service-specific proof: "board-
certified providers", "avg. time to appointment", "member
rating") → Heading Block + Horizontal Cards (icon variant —
related services wayfinding) → Form (two-column, "Book a
[service] visit", with a service-specific select). Component
gap: none — fully buildable from the current library.

**Page 3 — News & Insights Page — BUILT as `templates/
template-insights.html`, "Insights Page" (v1.28), kept
deliberately simple as an entry point rather than a full
archive.**
Stack: Header → Heading Block (center, no-CTA: "News &
Insights" + intro) → Horizontal Cards (image-small, 8 articles,
embedded header removed since the intro above covers it) → a
**static "Load More Articles" button** (not a real pagination
control) → a trimmed Form (stacked, email-only) as a newsletter
signup. Deliberately skipped, still gaps if a fuller archive
page is ever needed: (1) **filter/tag pills** for category
browsing, (2) **real pagination** (the current button is
decorative, matching the library's markup-only/no-JS
philosophy). Revisit both if this page needs to scale past a
single static grid.


1. **Landing Page — Patient Experience Improvement Guide**
   Goal: single conversion (provider/exec lead capture).
   Content: downloadable resource ("Hospital Patient
   Satisfaction Playbook", "5 Ways to Improve HCAHPS Scores").
   Structure: no main nav; simple download form; value bullet
   points; strong CTA ("Download the Free Playbook").
2. **Campaign Page — Annual Patient Experience Open Forum**
   Goal: registrations for a time-bound event/webinar.
   Content: virtual roundtable promo ("Redefining Care: A
   Virtual Forum on Empathy in Clinical Communication").
   Structure: coordinated with LinkedIn/email; event date,
   speaker bios, countdown timer, "Reserve Your Seat" CTA.
3. **Success Story Page — St. Jude Regional Hospital Case Study**
   Goal: build trust via proven results.
   Content: case study of a hospital system transformation.
   Structure: bold metrics up top ("+35% HCAHPS Doctor
   Communication", "20% Reduction in Wait Times"), video
   testimonials, Challenge → Solution → Results narrative.

   Component gaps these imply: nav-less page chrome, download
   form variant, countdown timer, speaker-bio cards, video
   embed, metric callouts, testimonial block.
