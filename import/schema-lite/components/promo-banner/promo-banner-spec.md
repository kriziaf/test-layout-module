---
label: Promo Banner
status: candidate
tier: component
variants:
  - cta-default
  - cta-inverse
bridgeNamespace: --pb-
files:
  html: components/promo-banner/promo-banner.html
  css: components/promo-banner/promo-banner.css
  docs: components/promo-banner/promo-banner.md
dependsOn:
  - button-group
tokensConsumed:
  - color/bg/brand-xstrong
  - color/content/inverse-default
  - color/content/subtle
  - color/content/default
  - color/bg/default
  - typography/headline/default
  - typography/body/default
  - typography/label/default
  - color/button/accent/*
  - color/button/primary/*
slots:
  - inner
  - eyebrow
  - heading
  - body
  - actions
contentJob: conversion
notes:
  - No image asset in v1 — purely token-driven surface, unlike the originally
    proposed full-bleed SVG/photo background (rejected; see provenance)
  - cta-inverse variant shares color/bg/brand-xstrong and
    color/content/inverse-default with Highlight Bar's entry — same tokens,
    first component to actually implement them (neither existed in
    hand-authored tokens.css before this addition)
  - cta-inverse CTA button falls back from color/button/accent/* to
    color/button/primary/* on TCG/CHC/White Label, since accent (inverse)
    buttons are only fully spec'd for Evernorth per brands.md §5 — contrast
    on the dark surface for those 3 brands is unverified, flagged for review
    before ship
  - "Eyebrow uses typography/label/default per the documented ramp
    (component-library.md: 'Eyebrows: label/default, uppercase, subtle
    color'), not an invented size"
  - cta-default and cta-inverse are both explicit modifier classes on the
    section root per the library's variantApi convention — no bare
    .promo-banner
provenance:
  - Originally proposed as a full-bleed SVG background (gradient + embedded
    photo + hardcoded Evernorth-only accent fills) based on an uploaded
    reference asset (banner-feature.svg) — rejected because the baked
    gradient/photo could not be re-themed per data-theme, violating design.md
    non-negotiable #2. Replaced with a flat --color-bg-brand-xstrong surface
    instead.
  - --color-bg-brand-xstrong and --color-content-inverse-default are NEW
    tokens added to tokens.md for this component. Evernorth's value reuses
    the existing .btn--inverse primary text color (#003034) rather than
    inventing a new one. TCG/CHC/White Label values are provisional
    extrapolations, not design-sourced — same status as the non-Evernorth
    accent button gap already tracked in Project-roadmap.md.
  - "#003034 independently confirmed: promo-banner-image-inverse.svg (a
    parked variant, see below) uses #003034 as a literal fill alongside the
    real .btn--inverse Evernorth spec colors (#00FEAF, #3EFFC0) — this is
    design-source confirmation, not just a value carried forward from the
    button spec by inference."

parkedVariants:
  - name: cta-default-image
    status: parked
    source: promo-banner-image.svg
    note: Image-backed light variant, same full-bleed concept as the
      rejected banner-feature.svg. Contains an embedded ~2.1MB raster —
      would need extraction to img/ + recompression per
      component-library.md's asset pipeline, and literal fills
      (#035C67, #2D2D2D, #EAF4F6) resolved through tokens before use.
  - name: cta-inverse-image
    status: parked
    source: promo-banner-image-inverse.svg
    note: Image-backed dark variant. Same extraction work needed. Literal
      fills confirmed match the real Evernorth inverse button spec.
---

# Promo Banner

**Layer 1. Candidate status** — new component, not yet built as an
HTML/CSS artifact. This file is its `components.json` entry plus
the full design-decision trail, ahead of implementation.

## Short description

A centered, token-driven promotional band with eyebrow, heading,
body copy, and a single CTA. Two variants: `cta-default` (light,
on the page's default background) and `cta-inverse` (dark, on
`color/bg/brand-xstrong`). No image or decorative asset — the
surface color is the only visual differentiator between variants.

## Composition — where this sits

Component tier, same as Highlight Bar and External Link Cards:
self-contained, no embedded Heading Block, depends only on the
`.btn` atom (Button Group) for its CTA.

**Relationship to Highlight Bar, not a duplicate of it:** both
consume the same dark-surface token pair
(`color/bg/brand-xstrong` / `color/content/inverse-default`), but
they serve different jobs. Highlight Bar is explicitly a *proof
band* — "No CTA slot by design... this is a proof band, not a
conversion surface" (its own entry's notes). Promo Banner is the
conversion surface that pairing implies is missing: same visual
register, opposite content job (`proof-and-trust` vs.
`conversion`).

## How this component's spec came together (decision trail)

1. Originally scoped as a `.cta-band`-style component from a
   separate content-architecture skill review, alongside two
   other structural gaps (`.stats`, `.feature-list`) found when
   comparing that skill's assumed component set against the real
   11-component inventory.
2. `.stats` resolved to the existing `list-item--stats` variant.
   `.feature-list` resolved to the existing `list-item` component.
   Only the CTA-band gap required a genuinely new component —
   Promo Banner.
3. First proposal used an uploaded reference SVG
   (`banner-feature.svg`) as a full-bleed background: linear +
   radial gradients, an embedded raster photo via pattern-fill,
   and literal Evernorth-only hex fills (`#035C67`, `#2D2D2D`,
   `#EAF4F6`). Rejected — none of that can be re-themed via
   `data-theme`; it would have shipped Evernorth-only in
   violation of the library's core token discipline.
4. Simplified to a flat `color/bg/brand-xstrong` surface, no
   image asset at all — the same surface-swap mechanism as every
   other themed component, no new asset pipeline needed.
5. A working visual preview (real generated `tokens.css`, all 4
   brands, both variants, a live token readout) was built and
   reviewed before this entry was finalized — caught two real
   token-discipline bugs in the preview itself (eyebrow and body
   copy were hardcoded pixel/rem values instead of the documented
   `typography/label/default` and `typography/body/default`
   presets) and one naming collision (this file originally used
   `color/content/knockout`; renamed to
   `color/content/inverse-default` to match Highlight Bar's
   already-committed, not-yet-implemented token name rather than
   introducing a second synonym for the same concept).

## Open items before this moves from candidate to stable

- TCG/CHC/White Label `cta-inverse` button contrast is unverified
  (accent button fallback issue, noted above) — check before ship.
- `color/bg/brand-xstrong` and `color/content/inverse-default`
  values for TCG/CHC/White Label are provisional extrapolations —
  real design-source values would supersede them.
- HTML/CSS artifact files don't exist yet — this entry describes
  the spec; building `promo-banner.html`/`.css`/`.md` is the next
  step, following the same artifact-trio contract as every other
  component.
