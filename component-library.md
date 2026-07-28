---
title: Component Library — Project Context
version: "1.31"
updated: 2026-07-27
scope: components + design tokens (no demo shell, no page templates)
brands: [evernorth, tcg, chc, white-label]
depends_on: []
entry_point: design.md
machine_readable: components.json
source: Figma variables.json export (14 collections) + per-component artboard SVGs
audience: AI sessions / developers extending or consuming the library
companion: layout-module.md (demo shell + templates; depends on this file)
see_also: content-system.md (voice), failure-modes.md (traps)
roadmap: Project-roadmap.md
---

# Component Library — Reusable Context

Multi-brand HTML/CSS component library for The Cigna Group brand
family. Pure markup + CSS deliverables (no JS in components; the
one interactive pattern — Header's mobile menu — is a CSS-only
checkbox toggle). Components are "artifacts": copy-paste-ready
HTML files whose `<body>` contents ship as-is.

## Ground rules

- **File trio per component:** `components/<name>/<name>.html`
  (artifact: self-contained variant snippets + banner doc),
  `<name>.css`, `<name>.md` (annotations: title, short
  description, content section, marketing content notes — never
  spec descriptions).
- **Naming:** block class = folder = file name. BEM:
  `.block__element`, variant modifier `.block--variant`.
- **Artifact banner contract:** REQUIRED INCLUDES, REQUIRED
  CONTEXT, VARIANT API, CONTENT SLOTS, plus judgment-call NOTES.
  Every variant is a fully self-contained `<section>` snippet.
- **Responsive = container queries.** Every section is wrapped
  in `.component-viewport` (defined in base.css,
  `container-type: inline-size`). Breakpoints: 640px and 1024px
  (`@container (min-width: …)`). Never viewport media queries.
  Side effect: margins do not collapse through the viewport
  wrapper (it creates a formatting context).
- **No `!important` in component CSS.** Composition layers may
  use element+class specificity (`section.x`) to outrank
  component `.block` selectors regardless of stylesheet order.
- **Icons: Phosphor** (MIT), regular weight, inlined as
  `<svg viewBox="0 0 256 256" fill="currentColor">` with the raw
  path — never the `ph ph-*` icon-font classes (no webfont is
  loaded; they render empty). Source:
  raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/<name>.svg
  Sizes in use: 16 (arrow-right, inline with links), 32
  (list-item, horizontal-cards icons), 40 (card chips). Icons
  inherit brand color via currentColor; brand LOGOS keep literal
  fills and never use currentColor.
- **Fonts:** Google Fonts Montserrat / Inter / Nunito. CHC uses
  licensed Value Serif Pro / Value Sans Pro with Georgia /
  Helvetica fallbacks until the @font-face files are provided.
- **Versioning:** lockstep across the whole library; every
  change bumps (v1.x). Breaking changes get called out in
  artifact banners. v2.0 is reserved for the attribute-API
  refactor (see roadmap).

## Token architecture (theming)

Three layers, all in `css/tokens.css`:

1. **Semantic theme blocks** — `[data-theme="evernorth|tcg|chc|
   white-label"] { --color-…; --typography-…; }`. Values were
   resolved from the Figma variables.json by following alias
   chains (Semantic: All Brands collection → brand mode →
   primitive collections). Setting `data-theme` on ANY ancestor
   (body, or a single component root) themes everything below
   it; mixed-theme pages are legal.
2. **Component bridge variables** — each component claims a
   short namespace mapped to semantics, e.g.
   `.list-item { --li-ink: var(--color-content-default); }`.
   Bridges: --hd (header), --hero, --tai (text-and-image),
   --form, --li (list-item), --hb (heading-block), --hc
   (horizontal-cards), --elc (external-link-cards), --hlb
   (highlight-bar), --btn (button atom, thin: font+radius
   only — button color tokens are already button-scoped so the
   atom reads them directly).
3. **Component rules** consume bridge vars (or, for buttons,
   the semantic button tokens directly).

### Core semantic values per brand

| token | evernorth | tcg | chc | white-label |
|---|---|---|---|---|
| content/default | #2D2D2D | #333333 | #333333 | #202427 |
| content/subtle | #6C6C6C | #5C5C5C | #5C5C5C | #4D5052 |
| content/brand | #035C67 | #0033FF | #0033FF | #0033FF |
| content/brand-strong | #035C67 | #110081 | #110081 | **#333333** |
| content/list-title | brand | brand | brand | **#333333** |
| content/link → hover | #035C67→#00363D | #0033FF→#110081 | same | same |
| border/default | #D5D5D5 | #D6D6D6 | #D6D6D6 | #D2D3D4 |
| border-radius: default / field / container | 8 / 8 / 16 | 900(pill) / 8 / 30 | 900 / 8 / 30 | 12 / 12 / 24 |
| headline font | Inter | Montserrat | Value Serif Pro | Nunito |
| shadow/default color | #2D2D2D1A | #3333331A | #3333331A | #0000001A |
| bg-chip (card icon chips) | #E8FFF8 (mockup; not in token JSON — flagged) | #E6EBFF | #E6EBFF | #E9E9E9 |

White Label is deliberately neutralized: ALL headings (section
`brand-strong` + item `list-title`) read #333333; brand blue
survives only in logos, links, icons, and buttons.

### Typography ramp (headings)

- Section titles: `typography/headline/small` — 28px mobile →
  32/40 desktop (all brands), weight 600–700, color
  brand-strong. Applied to Heading Block titles and to headings
  embedded via Heading Block.
- Item/card titles: 20–24px (headline/xsmall: 24/32; WL 28/40),
  color list-title.
- Stats figures: `typography/display/small` 48px, brand color.
- Eyebrows: label/default, uppercase, subtle color.

## Composition taxonomy

Four levels. Knowing which level a thing belongs to determines
where its styles live and what it may depend on.

| Level | Definition | Owns | May depend on | Examples |
|---|---|---|---|---|
| **Atom** | A single reusable element with no internal layout of its own. Defined once, consumed everywhere. | Its own states | Tokens only | `.btn` (defined in button-group.css) |
| **Component** | A self-contained section with a variant API. The unit of delivery — ships as an artifact trio. | Its layout, its slots, its `--<ns>-*` bridge | Tokens, atoms, pattern-modules | Hero, Form, List Item, Header |
| **Pattern-module** | A component that is *also* designed to be embedded inside other components, inheriting their content context. | Its layout and slots | Tokens, atoms | Heading Block |
| **Template** | A page composition. Owns no styles beyond rhythm classes. | Section order and content | Everything above | Homepage, Insights Page, Contact Us |

Rules that follow from this:

- **Atoms never import component CSS.** `.btn` reads button
  tokens directly rather than through a bridge, because those
  tokens are already button-scoped.
- **Pattern-modules must degrade when nested.** Heading Block
  strips its own section padding when embedded (see
  `.list-item__header`), because the host owns the spacing.
- **Components must not reach into each other's internals.** If
  two components need the same thing, it becomes an atom or a
  pattern-module. The `.btn` atom exists because four components
  had duplicated the same button rules.
- **Templates add no component styles.** Page-level spacing
  lives in `css/templates.css` as `tpl-*` composition classes.

## Accessibility standard

These are requirements, not defaults. The library already
satisfies all of them; a reuser who drops them is regressing the
system, not simplifying it.

**Focus**
- Every interactive element has a visible `:focus-visible` state.
  Never `:focus` alone, and never `outline: none` without a
  replacement indicator.
- Buttons: 2px ring, `outline-offset: 2px`, colored by a
  dedicated focus-ring token per button type.
- Cards: brand border plus a box-shadow ring (~3px total).
- Nav links: 2px outline with negative offset so the ring stays
  inside the 88px bar.

**Semantics and state**
- Active navigation is marked `aria-current="page"`, and the
  underline indicator is driven by that attribute — not by a
  presentational class.
- Disabled interactive elements use `aria-disabled="true"`
  (anchors) or `[disabled]` (buttons), and both get
  `pointer-events: none`.
- Decorative icons carry `aria-hidden="true"`. Icons that convey
  meaning on their own must have a text label beside them.
- Logo links have an accessible name (`aria-label="Home"`).

**Structure**
- One `<h1>` per page — it belongs to the Hero. Component
  headings start at `<h2>`; item-level headings are `<h3>`.
- **Never nest anchors.** If a card is a link, inner "link text"
  is a `<span>`. If a card needs real inner links, the card
  becomes a `<div>` (see the Contact Us template).
- Form inputs are associated with labels via `for`/`id`.
  Optional fields are marked in the label text, not by placeholder
  alone.
- Nav lists are real `<ul>`/`<li>`; the mobile drawer duplicates
  the nav rather than moving it, so both are always in the DOM.

**Independence from JavaScript**
- No component requires JavaScript to be usable. The mobile menu
  is a checkbox toggle, which also means it survives being cloned
  into `<template>` elements in the demo.

**Contrast**
- Inverse surfaces (Hero Inverse, Highlight Bar) use
  `color/content/inverse-default` (white) on brand-strong or
  brand-xstrong backgrounds — never mid-tone brand colors, which
  fail contrast against white text.
- Subtle text (`color/content/subtle`) is for supporting copy
  only, never for the sole instance of critical information.

**Not yet verified:** no automated axe/Lighthouse pass has been
run, and no screen-reader testing has been done. The rules above
are enforced by construction and by the Playwright checks, which
is not the same as audited. See `Project-roadmap.md`.

## Component inventory (10 active)

Dependency graph: **Heading Block** is embedded (left, no-CTA)
inside List Item, Horizontal Cards, and the two-column Form.
The **`.btn` atom** (defined in button-group.css) is consumed by
Heading Block CTAs, Form actions, Hero actions, and Text and
Image actions. Consumers must include the dependency CSS —
listed in each artifact's REQUIRED INCLUDES.

| component | variants | notes |
|---|---|---|
| header | default | 88px bar; per-brand logo revealed by data-theme (all four ship in markup); 4px nav underline on hover/`aria-current="page"`; CSS-only hamburger <1024px (checkbox hack; nav+utils duplicated in drawer — edit both); shadow/default |
| hero | default, inverse | default: wash panel (#EAF4F6 = secondary bg-hover) left + photo right; inverse: photo left + brand panel right + `.btn--inverse` pair, floats on #F6F5F3 canvas at desktop, full-bleed panel-ABOVE-image stacked below 1024 (order properties override source order); buttons stack <640 |
| text-and-image | fixed-image, cutout, two-column | cutout = baked transparent PNG (clip-path on roadmap) |
| form | two-column, stacked | two-column embeds Heading Block left (heading, note, intro) with fields right; stacked keeps bespoke centered `.form__header` (deliberate split ownership) |
| list-item | links, stats, articles, accent | embeds Heading Block header (all four variants); links: 32px icon + brand heading + body + bottom-pinned link; stats: 48px figure; articles: 2-line clamp (`-webkit-line-clamp: 2`), ink heading; accent: circular brand-filled icon badge + white glyph, bordered card shell (folded in from the retired standalone List Cards component). TRAP: `.list-item__header` (section header wrapper) vs `.list-item__heading` (item h3) — one letter apart |
| heading-block | center, left, two-column, × with/without CTA (6) | `--no-cta` modifier is an API marker only; behavior = omit `.heading-block__actions`. CTA block = Primary+Secondary `.btn` pair; either slot omittable |
| horizontal-cards | icon, image-small (140px flush photo), image-large (375px, subtitle+link slot) | icon/image-small cards are whole-card `<a>` (inner link is `<span>`); image-large is `<div>` with a real `<a>` |
| highlight-bar | icon-list, metrics | themed dark surface (`color/bg/brand-xstrong` + `color/content/inverse-default`, re-themes per brand); metrics variant dividers flip top-border (stacked) → left-border (desktop columns) |
| external-link-cards | quick-link, heading, image | 72px icon chip (bg-chip token); heading variant has link below body; four interaction states (see below). Whole-card `<a>`s; nested link text is `<span>` (no nested anchors) |
| button-group | default, inverse | showcase for the `.btn` atom (the actual deliverable) |

## Interaction states (behavior rules)

### Buttons — the `.btn` atom (button-group.css)

Markup: `.btn .btn--primary|--secondary` (+ `.btn--inverse` on
dark brand surfaces). Works on `<a>` and `<button>`. Disabled =
`aria-disabled="true"` (anchors) or `[disabled]` (buttons); both
get `pointer-events: none`. Focus = `:focus-visible` only, 2px
ring, offset 2px. 2px border always present (transparent-border
technique keeps geometry stable across states). Padding
.75rem/1.75rem; radius = border-radius/default token (pill in
TCG/CHC).

Standard set (spec values = Evernorth; other brands read their
own semantic button tokens):

| state | primary bg / text | secondary text+border / bg |
|---|---|---|
| default | #035C67 / #FFF | #035C67 / transparent |
| hover | #024A52 | #00363D / #EAF4F6 |
| pressed (:active) | #012529 | #00171A / #CCE7EA |
| focus | hover bg + 2px #012529 ring | hover treatment + 2px #00171A ring |
| disabled | #EAEAEA / #949494 | #999999 text, #ABABAB border / #EAEAEA |

Inverse (accent) set — `.btn--inverse`; spec'd for Evernorth
(mint on dark), other brands derive white-on-brand (roadmap):

| state | primary bg / text | secondary text+border / bg |
|---|---|---|
| default | #00FEAF / #003034 | #3EFFC0 / transparent |
| hover | #12F3A9 | #12F3A9 / #003826 |
| pressed | #00D18D | #00D18D / #00171A |
| focus | hover + 2px #12F3A9 ring | hover + ring |
| disabled | #ABABAB / #003034 | #ABABAB / transparent |

Content rules: never two primaries side by side; verb-first
labels, 2–4 words, no punctuation; prefer hiding over disabling
in marketing pages.

### Form fields

- Inputs: 48px height, 1px border/default, field radius token,
  label above; optional fields marked `<span class="form__optional">(optional)</span>`.
- Focus: 2px brand outline, offset 1, border flips brand.
- Select (`.form__select`): 48px, custom inline-SVG chevron
  (background-image, `appearance: none`), same border/focus as
  inputs.
- Textarea: maxlength + `.form__meta` row (helper text left,
  char count right).
- Submit row `.form__actions`: Submit (`.btn--primary`,
  type=submit) + Clear (`.btn--secondary`, type=reset).
- Required note verbatim convention: "All fields are required
  unless marked optional".

### Cards (external-link-cards; the four-state spec)

| state | border | background |
|---|---|---|
| default | 2px border/default gray | white |
| hover | 2px brand | secondary bg-hover wash (#EAF4F6 ev) |
| pressed | 2px brand | secondary bg-active (#CCE7EA ev) |
| focus-visible | brand + box-shadow ring (≈3px total) | white |

Horizontal-cards `<a>` cards use the hover wash + brand border.
State washes are the secondary-button tokens, so they re-theme
automatically.

### Navigation (header)

- Nav link: 88px tall cell, 4px transparent bottom border;
  hover / `:focus-visible` / `[aria-current="page"]` fill it
  brand and tint the label.
- Utility links: brand color, underline on hover.
- Mobile: checkbox `#header-menu` + label button (Phosphor
  list/x swap); `:checked ~` sibling selectors open the drawer;
  drawer links use a 4px LEFT border for active.

### Links (inline / card links)

`content/link` color, 600 weight, no underline at rest;
hover/focus = link-hover color + underline; arrow icon
(Phosphor arrow-right, 16px, currentColor) nudges +3px on hover
where animated (list-item). Card-bottom links use
`margin-top: auto` so they baseline-align across unequal
columns.

## Assets

`img/`: text-and-image-boardwalk.jpg, text-and-image-cutout.png,
external-link-card-photo.jpg, horizontal-card-photo.jpg,
hero-default-photo.jpg, hero-inverse-photo.jpg. Extracted from
design SVGs (largest base64 blob = the real photo; 64×64 blobs
are Figma thumbnails — skip). Recompress to ≤1200px JPEG q82.

## Known judgment calls / provenance flags

- Mockup link tint #0F7885 and chip mint #E8FFF8 don't exist in
  the token JSON; library maps links to `content/link` and
  ships the chip mint literally (Evernorth) with derived values
  elsewhere — swap when official tokens are minted.
- External-link-cards being links is inferred from design
  intent (no affordance drawn); swap `<a>`→`<div>` if
  non-interactive.
- Hero light-variant ink #1E1E1E in mockup ≈ mapped to
  content/default.
- Focus states for cards and non-Evernorth accent buttons are
  inferred, not spec'd.
