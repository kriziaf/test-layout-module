---
title: Layout Module — Demo Shell & Page Templates
version: "1.31"
updated: 2026-07-27
scope: presentation layer — demo shell, page templates, section rhythm
brands: [evernorth, tcg, chc, white-label]
depends_on: [component-library.md]
entry_point: design.md
machine_readable: components.json
audience: AI sessions / developers working on the demo or template pages
roadmap: Project-roadmap.md
---

# Layout Module — Reusable Context

Everything that COMPOSES components without being one: the demo
shell (`demo.html`), the page templates (`templates/*.html`),
and the section-rhythm rules (`css/templates.css`). Depends on
component-library.md; components never depend on anything here.

## Demo shell (demo.html)

Single-file presentation app. Top bar controls:

- **Component dropdown** — populated from a `COMPONENTS`
  registry object `{ key: { label, version, variants: [{id,
  label}] } }`. Dropdown text shows "Label vX.Y".
- **Template dropdown** — Homepage, Insights Page, Contact Us
  + empty "—" option.
  Selecting a template hides the variant toggle, stacks the page
  from component templates, and resets when a component is
  picked (the two selectors never fight).
- **Variant segmented toggle** — radio group re-rendered per
  component from the registry.
- **Brand mode toggle** — sets `document.body.dataset.theme`;
  works in both component and template modes.
- **Breakpoint toggle** — mobile 400 / tablet 768 / desktop
  1440; sets a width-constrained stage frame so container
  queries fire (never resizes the window).
- **Annotations + View code buttons** — two modes of one 50%
  sidebar panel; `aria-pressed` tracks the active mode. Code
  mode shows paste-ready markup (template mode concatenates the
  whole stack); annotations are per-component (template mode
  shows a redirect message).

Stage: `#frame` on a #CFCFCF canvas. Status line:
`component--variant @ breakpoint @ theme`.

### Markup + annotation delivery

Each component variant lives in the demo as
`<template id="tpl-<component>-<variant>">` containing a copy of
the artifact's section (img paths rewritten `../../img/` →
`img/`). Annotations live as `<template id="md-<component>">`
holding escaped markdown. `<script>` inside `<template>` does
NOT execute when cloned — reason the Header hamburger is
CSS-only.

### Template mode internals

`TEMPLATES` object: `{ a|b|c: { label, stack: [[component,
variant, extraClass?], …] } }`. Cloner appends each component
template; optional third element adds a composition class
(`tpl-section-heading` / `tpl-card-section`) to the cloned
section at insert time.

## Page templates (templates/)

Templates A, B, and C (the CoverMyMeds-content solution/overview/
editorial set, v1.19–v1.24) were retired and deleted in v1.30 in
favor of a virtual-care-branded three-page set. No
artifact-pure/lorem reference template currently exists in the
library — if one is needed again (e.g. as a regeneration
sanity-check), rebuild one from the component artifacts directly
rather than reintroducing lettered naming.

- **template-homepage.html — Homepage — Virtual Care (CONTENT
  INSTANCE).** header → hero--default ("See a doctor today, from
  anywhere.") → wayfinding (heading-block +
  external-link-cards--quick-link) → Features & Benefits
  (list-item--accent, 6 items, embedded header) → News &
  Insights (horizontal-cards--image-small, 4 cards) →
  form--two-column ("Join us today").
- **template-insights.html — Insights Page (CONTENT INSTANCE).**
  Deliberately simple news/insights entry point, not a full
  archive: header → heading-block--center-no-cta ("News &
  Insights" intro) → horizontal-cards--image-small (8 articles,
  embedded header stripped since the intro above covers it) → a
  static "Load More Articles" button (no real pagination) →
  form--stacked trimmed to a single email field (newsletter
  signup). Two component gaps intentionally routed around
  rather than built: filter/tag pills and real pagination — see
  Project-roadmap.md.
- **template-contact.html — Contact Us (CONTENT INSTANCE).**
  header → hero--default with NO CTA (`.hero__actions` omitted)
  → external-link-cards--heading (3 cards; two use `<div>`
  containers with real nested `<a>` links rather than the
  card-as-`<a>` pattern, to avoid nesting anchors) →
  list-item--links adapted as a locations block (icon+label item
  + 3 plain city/address items, wrapped in an instance-only white
  card via inline style) → heading-block--center with CTA
  (practice-signup banner) → form--stacked customized as a
  Name/Email/Topic/Message contact form.

Template head loads: tokens.css, base.css, templates.css, then
every component CSS used (button-group.css and
heading-block.css are near-universal dependencies). Brand mode:
one `data-theme` on `<body>`.

## Section rhythm (css/templates.css)

Composition-only rules; components stay untouched.

- `.heading-block.tpl-section-heading` — a heading block that
  introduces a card zone. Carries the 48px gap as
  **padding-bottom** (padding paints the section's white
  background; a margin there is transparent and shows the
  page/stage background as a gray band — learned the hard way).
  Its `> :last-child` gets `margin-bottom: 0` for exactness
  (margins can't collapse through the container-query viewport
  wrappers).
- `section.tpl-card-section` — the card section that follows;
  `padding-top: 0 !important` (element+class specificity +
  important beats component breakpoint padding regardless of
  stylesheet load order).
- Current assumption: heading + cards sit on white. If a tinted
  band arrives, generalize to surface classes (roadmap).
- Verified contract: exactly 48px from the heading's last text
  element to the card section top, at desktop, in template
  files AND demo template mode.

## Sync contracts (drift risks — read before editing)

1. **Artifacts are the source of truth for markup.** Demo
   `<template>`s and template-page sections are COPIES. After
   any artifact edit, re-extract into demo.html and any template
   using that component. When copying into templates/, rewrite
   img paths to `../img/` (missing this broke a template once).
2. **Template stacks exist in three places:** templates/*.html,
   their banner STACK docs, and the demo `TEMPLATES` object.
   All manual. This caused three bugs (stale rename, missed
   restructure, path drift). A manifest/build script is the
   roadmap fix.
3. **All three current templates are content instances and are
   NOT regenerable** from artifacts by pure copy — re-apply
   their content after any component resync. There is currently
   no artifact-pure reference template in the library.
4. **Annotations** (`components/<n>/<n>.md`) are the source for
   demo `md-*` templates (escaped copies).
5. **Renames are full renames:** folder, files, classes, bridge
   vars, image assets, registry keys, template ids, template
   stacks, annotations. Grep for residuals including inside the
   demo JS (post-rename stale strings in TEMPLATES silently
   no-op string replacements).

## Verification pattern

Headless Playwright against `file://` — computed styles, geometry
(gap measurements, element order via getBoundingClientRect),
state simulation (hover/mousedown/Tab), image `complete &&
naturalWidth`, `pageerror` capture; run across the
variant × brand × breakpoint matrix and on standalone artifacts,
template files, and demo template mode. Measure paint-affecting
properties, not just geometry (the gray-gap bug passed geometry
checks).
