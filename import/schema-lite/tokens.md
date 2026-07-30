---
title: Design Data Schema — Tokens
version: 2.0-draft
kind: layer-1-schema
schemaVersion: '1.0'
generates: css/tokens.css (build output — do not hand-edit)
namingGrammar: --{context}-{role}-{variant}-{state}  (e.g. --color-button-primary-bg-hover; not all segments
  always present)
global:
  note: Theme-independent — same value regardless of [data-theme]. Added 2026-07-29 per Leaf Design System
    review (spacing-borders-shadows-breakpoints.md); library previously had no spacing scale, no shadow
    scale beyond one brand-varying color, and no breakpoint tokens.
  spacing:
    --spacing-0: 0rem
    --spacing-8: 0.5rem
    --spacing-16: 1rem
    --spacing-24: 1.5rem
    --spacing-32: 2rem
    --spacing-48: 3rem
    --spacing-64: 4rem
  shadow:
    --shadow-small: 0 1px 2px 1px rgb(0 0 0 / 20%)
    --shadow-default: 0 8px 6px 0 rgb(0 0 0 / 10%)
    --shadow-large: 0 10px 12px 0 rgb(0 0 0 / 20%)
  breakpoints:
    note: Reference values only — cannot be injected as CSS custom properties into @container or @media
      conditions. Documented here so component authors use one consistent pair rather than re-deriving
      per component.
    --breakpoint-tablet: 640px
    --breakpoint-desktop: 1024px
brands:
  evernorth:
    label: Evernorth
    values:
      --color-content-list-title: var(--color-content-brand)
      --color-content-default: '#2D2D2D'
      --color-content-subtle: '#6C6C6C'
      --color-content-brand: '#035C67'
      --color-bg-brand-xstrong: '#003034'
      --color-content-inverse-default: '#FFFFFF'
      --color-button-primary-bg-default: '#035C67'
      --color-button-primary-bg-hover: '#024A52'
      --color-button-primary-bg-focus: '#024A52'
      --color-button-primary-bg-active: '#012529'
      --color-button-primary-content-default: '#FFFFFF'
      --color-button-primary-border-default: '#035C67'
      --color-button-primary-bg-disabled: '#EAEAEA'
      --color-button-primary-content-disabled: '#949494'
      --color-button-primary-focus-ring: '#012529'
      --border-radius-default: 8px
      --border-radius-large: 16px
      --border-radius-component-button: 8px
      --typography-headline-font-family: '''Inter'', sans-serif'
      --typography-body-font-family: '''Inter'', sans-serif'
      --typography-headline-default-font-size: 2.5rem
      --typography-headline-default-line-height: 3.5rem
      --typography-headline-default-font-weight: '600'
      --typography-headline-default-mobile-font-size: 2rem
      --typography-headline-default-mobile-line-height: 2.5rem
      --typography-body-default-font-size: 1rem
      --typography-body-default-line-height: 1.5rem
      --typography-body-default-font-weight: '400'
      --typography-label-default-font-size: 1rem
      --typography-label-default-line-height: 1.5rem
      --typography-label-default-font-weight: '500'
      --typography-label-default-letter-spacing: '0'
      --color-border-default: '#D5D5D5'
      --color-content-error: '#D02525'
      --color-button-secondary-bg-default: transparent
      --color-button-secondary-bg-hover: '#EAF4F6'
      --color-button-secondary-bg-focus: '#EAF4F6'
      --color-button-secondary-bg-active: '#CCE7EA'
      --color-button-secondary-content-default: '#035C67'
      --color-button-secondary-content-hover: '#00363D'
      --color-button-secondary-border-default: '#035C67'
      --color-button-secondary-border-hover: '#00363D'
      --color-button-secondary-content-active: '#00171A'
      --color-button-secondary-border-active: '#00171A'
      --color-button-secondary-bg-disabled: '#EAEAEA'
      --color-button-secondary-content-disabled: '#999999'
      --color-button-secondary-border-disabled: '#ABABAB'
      --color-button-secondary-focus-ring: '#00171A'
      --border-radius-component-field: 8px
      --typography-headline-small-font-size: 2rem
      --typography-headline-small-line-height: 2.5rem
      --typography-headline-small-font-weight: '600'
      --typography-headline-small-mobile-font-size: 1.75rem
      --typography-meta-default-font-size: 1rem
      --typography-meta-default-line-height: 1.5rem
      --typography-meta-default-font-weight: '700'
      --color-content-link: '#035C67'
      --color-content-link-hover: '#00363D'
      --typography-display-small-font-size: 3rem
      --typography-display-small-line-height: '1.15'
      --border-radius-container: 16px
      --typography-headline-xsmall-font-size: 1.5rem
      --typography-headline-xsmall-line-height: 2rem
      --typography-headline-xsmall-font-weight: '600'
      --color-bg-chip: '#E8FFF8'
      --color-content-brand-strong: '#035C67'
      --shadow-default-color: '#2D2D2D1A'
      --color-bg-hero-canvas: '#F6F5F3'
      --color-content-inverse: '#FFFFFF'
      --color-button-accent-bg: '#00FEAF'
      --color-button-accent-bg-hover: '#12F3A9'
      --color-button-accent-bg-active: '#00D18D'
      --color-button-accent-bg-disabled: '#ABABAB'
      --color-button-accent-content: '#003034'
      --color-button-accent-focus-ring: '#12F3A9'
      --color-button-accent-outline: '#3EFFC0'
      --color-button-accent-outline-hover: '#12F3A9'
      --color-button-accent-outline-active: '#00D18D'
      --color-button-accent-outline-disabled: '#ABABAB'
      --color-button-accent-outline-bg-hover: '#003826'
      --color-button-accent-outline-bg-active: '#00171A'
    notes:
      --color-button-primary-bg-hover: button spec
      --color-button-primary-bg-active: button spec
      --typography-headline-default-font-weight: Semibold
      --typography-label-default-font-weight: Medium
      --typography-headline-small-font-size: '32'
      --typography-headline-small-line-height: '40'
      --typography-headline-small-mobile-font-size: '28'
      --typography-meta-default-font-weight: Bold
      --typography-display-small-font-size: '48'
      --typography-headline-xsmall-font-size: '24'
      --typography-headline-xsmall-line-height: '32'
      --color-bg-chip: mockup mint; not in token JSON — flagged
  tcg:
    label: The Cigna Group (TCG)
    values:
      --color-content-list-title: var(--color-content-brand)
      --color-content-default: '#333333'
      --color-content-subtle: '#5C5C5C'
      --color-content-brand: '#0033FF'
      --color-bg-brand-xstrong: '#000B33'
      --color-content-inverse-default: '#FFFFFF'
      --color-button-primary-bg-default: '#0033FF'
      --color-button-primary-bg-hover: '#001F99'
      --color-button-primary-bg-focus: '#001F99'
      --color-button-primary-bg-active: '#001466'
      --color-button-primary-content-default: '#FFFFFF'
      --color-button-primary-bg-disabled: '#EAEAEA'
      --color-button-primary-content-disabled: '#949494'
      --color-button-primary-focus-ring: '#001466'
      --color-button-primary-border-default: '#0033FF'
      --border-radius-default: 8px
      --border-radius-large: 30px
      --border-radius-component-button: 900px
      --typography-headline-font-family: '''Montserrat'', sans-serif'
      --typography-body-font-family: '''Montserrat'', sans-serif'
      --typography-headline-default-font-size: 2.5rem
      --typography-headline-default-line-height: 3.5rem
      --typography-headline-default-font-weight: '700'
      --typography-headline-default-mobile-font-size: 2rem
      --typography-headline-default-mobile-line-height: 2.5rem
      --typography-body-default-font-size: 1rem
      --typography-body-default-line-height: 1.5rem
      --typography-body-default-font-weight: '400'
      --typography-label-default-font-size: 1rem
      --typography-label-default-line-height: 1.5rem
      --typography-label-default-font-weight: '600'
      --typography-label-default-letter-spacing: '0'
      --color-border-default: '#D6D6D6'
      --color-content-error: '#BA0000'
      --color-button-secondary-bg-default: transparent
      --color-button-secondary-bg-hover: '#E6EBFF'
      --color-button-secondary-bg-focus: '#E6EBFF'
      --color-button-secondary-bg-active: '#CCD6FF'
      --color-button-secondary-content-default: '#0033FF'
      --color-button-secondary-content-hover: '#0033FF'
      --color-button-secondary-border-default: '#0033FF'
      --color-button-secondary-content-active: '#0033FF'
      --color-button-secondary-border-active: '#0033FF'
      --color-button-secondary-bg-disabled: '#EAEAEA'
      --color-button-secondary-content-disabled: '#999999'
      --color-button-secondary-border-disabled: '#ABABAB'
      --color-button-secondary-focus-ring: '#001466'
      --color-button-secondary-border-hover: '#0033FF'
      --border-radius-component-field: 8px
      --typography-headline-small-font-size: 2rem
      --typography-headline-small-line-height: 2.5rem
      --typography-headline-small-font-weight: '700'
      --typography-headline-small-mobile-font-size: 1.75rem
      --typography-meta-default-font-size: 1rem
      --typography-meta-default-line-height: 1.5rem
      --typography-meta-default-font-weight: '500'
      --color-content-link: '#0033FF'
      --color-content-link-hover: '#110081'
      --typography-display-small-font-size: 3rem
      --typography-display-small-line-height: '1.15'
      --border-radius-container: 30px
      --typography-headline-xsmall-font-size: 1.5rem
      --typography-headline-xsmall-line-height: 2rem
      --typography-headline-xsmall-font-weight: '700'
      --color-bg-chip: '#E6EBFF'
      --color-content-brand-strong: '#110081'
      --shadow-default-color: '#3333331A'
      --color-bg-hero-canvas: '#F6F5F3'
      --color-content-inverse: '#FFFFFF'
      --color-button-accent-bg: '#FFFFFF'
      --color-button-accent-bg-hover: '#E6E6E6'
      --color-button-accent-bg-active: '#CCCCCC'
      --color-button-accent-bg-disabled: '#ABABAB'
      --color-button-accent-content: '#202427'
      --color-button-accent-focus-ring: '#FFFFFF'
      --color-button-accent-outline: '#FFFFFF'
      --color-button-accent-outline-hover: '#E6E6E6'
      --color-button-accent-outline-active: '#CCCCCC'
      --color-button-accent-outline-disabled: '#ABABAB'
      --color-button-accent-outline-bg-hover: rgba(255,255,255,0.12)
      --color-button-accent-outline-bg-active: rgba(255,255,255,0.2)
    notes:
      --typography-headline-default-font-weight: Bold
      --typography-label-default-font-weight: Semibold
      --typography-meta-default-font-weight: Medium
      --color-bg-chip: 'derived: secondary hover wash'
  chc:
    label: Cigna Healthcare (CHC)
    values:
      --color-content-list-title: var(--color-content-brand)
      --color-content-default: '#333333'
      --color-content-subtle: '#5C5C5C'
      --color-content-brand: '#0033FF'
      --color-bg-brand-xstrong: '#000B33'
      --color-content-inverse-default: '#FFFFFF'
      --color-button-primary-bg-default: '#0033FF'
      --color-button-primary-bg-hover: '#001F99'
      --color-button-primary-bg-focus: '#001F99'
      --color-button-primary-bg-active: '#001466'
      --color-button-primary-content-default: '#FFFFFF'
      --color-button-primary-bg-disabled: '#EAEAEA'
      --color-button-primary-content-disabled: '#949494'
      --color-button-primary-focus-ring: '#001466'
      --color-button-primary-border-default: '#0033FF'
      --border-radius-default: 8px
      --border-radius-large: 30px
      --border-radius-component-button: 900px
      --typography-headline-font-family: '''Value Serif Pro'', Georgia, serif'
      --typography-body-font-family: '''Value Sans Pro'', ''Helvetica Neue'', Arial, sans-serif'
      --typography-headline-default-font-size: 2.5rem
      --typography-headline-default-line-height: 3.5rem
      --typography-headline-default-font-weight: '700'
      --typography-headline-default-mobile-font-size: 2rem
      --typography-headline-default-mobile-line-height: 2.5rem
      --typography-body-default-font-size: 1rem
      --typography-body-default-line-height: 1.5rem
      --typography-body-default-font-weight: '400'
      --typography-label-default-font-size: 1rem
      --typography-label-default-line-height: 1.5rem
      --typography-label-default-font-weight: '500'
      --typography-label-default-letter-spacing: '0'
      --color-border-default: '#D6D6D6'
      --color-content-error: '#BA0000'
      --color-button-secondary-bg-default: transparent
      --color-button-secondary-bg-hover: '#E6EBFF'
      --color-button-secondary-bg-focus: '#E6EBFF'
      --color-button-secondary-bg-active: '#CCD6FF'
      --color-button-secondary-content-default: '#0033FF'
      --color-button-secondary-content-hover: '#0033FF'
      --color-button-secondary-border-default: '#0033FF'
      --color-button-secondary-content-active: '#0033FF'
      --color-button-secondary-border-active: '#0033FF'
      --color-button-secondary-bg-disabled: '#EAEAEA'
      --color-button-secondary-content-disabled: '#999999'
      --color-button-secondary-border-disabled: '#ABABAB'
      --color-button-secondary-focus-ring: '#001466'
      --color-button-secondary-border-hover: '#0033FF'
      --border-radius-component-field: 8px
      --typography-headline-small-font-size: 2rem
      --typography-headline-small-line-height: 2.5rem
      --typography-headline-small-font-weight: '700'
      --typography-headline-small-mobile-font-size: 1.75rem
      --typography-meta-default-font-size: 1rem
      --typography-meta-default-line-height: 1.5rem
      --typography-meta-default-font-weight: '500'
      --color-content-link: '#0033FF'
      --color-content-link-hover: '#110081'
      --typography-display-small-font-size: 3rem
      --typography-display-small-line-height: '1.15'
      --border-radius-container: 30px
      --typography-headline-xsmall-font-size: 1.5rem
      --typography-headline-xsmall-line-height: 2rem
      --typography-headline-xsmall-font-weight: '700'
      --color-bg-chip: '#E6EBFF'
      --color-content-brand-strong: '#110081'
      --shadow-default-color: '#3333331A'
      --color-bg-hero-canvas: '#F6F5F3'
      --color-content-inverse: '#FFFFFF'
      --color-button-accent-bg: '#FFFFFF'
      --color-button-accent-content: '#0033FF'
      --color-button-accent-outline: '#FFFFFF'
    notes:
      --typography-headline-default-font-weight: Bold
      --typography-label-default-font-weight: Medium
      --color-bg-chip: 'derived: secondary hover wash'
  white-label:
    label: White Label
    values:
      --color-content-default: '#202427'
      --color-content-subtle: '#4D5052'
      --color-content-brand: '#0033FF'
      --color-bg-brand-xstrong: '#101214'
      --color-content-inverse-default: '#FFFFFF'
      --color-content-list-title: '#333333'
      --color-button-primary-bg-default: '#202427'
      --color-button-primary-bg-hover: '#1A1D1F'
      --color-button-primary-bg-focus: '#1A1D1F'
      --color-button-primary-bg-active: '#131617'
      --color-button-primary-content-default: '#FFFFFF'
      --color-button-primary-bg-disabled: '#EAEAEA'
      --color-button-primary-content-disabled: '#949494'
      --color-button-primary-focus-ring: '#131617'
      --color-button-primary-border-default: '#202427'
      --border-radius-default: 12px
      --border-radius-large: 24px
      --border-radius-component-button: 12px
      --typography-headline-font-family: '''Nunito'', sans-serif'
      --typography-body-font-family: '''Nunito'', sans-serif'
      --typography-headline-default-font-size: 2.5rem
      --typography-headline-default-line-height: 3.5rem
      --typography-headline-default-font-weight: '700'
      --typography-headline-default-mobile-font-size: 2rem
      --typography-headline-default-mobile-line-height: 2.5rem
      --typography-body-default-font-size: 1rem
      --typography-body-default-line-height: 1.5rem
      --typography-body-default-font-weight: '400'
      --typography-label-default-font-size: 1rem
      --typography-label-default-line-height: 1.5rem
      --typography-label-default-font-weight: '600'
      --typography-label-default-letter-spacing: '0'
      --color-border-default: '#D2D3D4'
      --color-content-error: '#BA0000'
      --color-button-secondary-bg-default: transparent
      --color-button-secondary-bg-hover: '#E9E9E9'
      --color-button-secondary-bg-focus: '#E9E9E9'
      --color-button-secondary-bg-active: '#D2D3D4'
      --color-button-secondary-content-default: '#202427'
      --color-button-secondary-content-hover: '#1A1D1F'
      --color-button-secondary-border-default: '#202427'
      --color-button-secondary-content-active: '#1A1D1F'
      --color-button-secondary-border-active: '#1A1D1F'
      --color-button-secondary-bg-disabled: '#EAEAEA'
      --color-button-secondary-content-disabled: '#999999'
      --color-button-secondary-border-disabled: '#ABABAB'
      --color-button-secondary-focus-ring: '#131617'
      --color-button-secondary-border-hover: '#1A1D1F'
      --border-radius-component-field: 12px
      --typography-headline-small-font-size: 2rem
      --typography-headline-small-line-height: 2.5rem
      --typography-headline-small-font-weight: '700'
      --typography-headline-small-mobile-font-size: 2rem
      --typography-meta-default-font-size: 0.875rem
      --typography-meta-default-line-height: 1rem
      --typography-meta-default-font-weight: '400'
      --color-content-link: '#0033FF'
      --color-content-link-hover: '#110081'
      --typography-display-small-font-size: 3rem
      --typography-display-small-line-height: '1.15'
      --border-radius-container: 24px
      --typography-headline-xsmall-font-size: 1.75rem
      --typography-headline-xsmall-line-height: 2.5rem
      --typography-headline-xsmall-font-weight: '700'
      --color-bg-chip: '#E9E9E9'
      --color-content-brand-strong: '#333333'
      --shadow-default-color: '#0000001A'
      --color-bg-hero-canvas: '#F6F5F3'
      --color-content-inverse: '#FFFFFF'
      --color-button-accent-bg: '#FFFFFF'
      --color-button-accent-content: '#202427'
      --color-button-accent-outline: '#FFFFFF'
    notes:
      --typography-headline-small-mobile-font-size: 32 (no smaller mobile step)
      --typography-meta-default-font-size: '14'
      --typography-headline-xsmall-font-size: '28'
      --typography-headline-xsmall-line-height: '40'
      --color-bg-chip: 'derived: secondary hover wash'
bridges:
  .text-and-image:
    note: '---- Component bridge: text-and-image consumes semantic tokens ----'
    values:
      --tai-ink: var(--color-content-default)
      --tai-subtle: var(--color-content-subtle)
      --tai-accent: var(--color-content-brand)
      --tai-title-ink: var(--color-content-brand-strong)
      --tai-font: var(--typography-body-font-family)
      --tai-headline-font: var(--typography-headline-font-family)
      --tai-radius: var(--border-radius-large)
  .form:
    note: null
    values:
      --form-ink: var(--color-content-default)
      --form-subtle: var(--color-content-subtle)
      --form-accent: var(--color-content-brand)
      --form-title-ink: var(--color-content-brand-strong)
      --form-font: var(--typography-body-font-family)
      --form-headline-font: var(--typography-headline-font-family)
      --form-border: var(--color-content-subtle)
      --form-field-radius: var(--border-radius-component-field)
  .feature-list:
    note: null
    values:
      --fl-ink: var(--color-content-default)
      --fl-subtle: var(--color-content-subtle)
      --fl-accent: var(--color-content-brand)
      --fl-link: var(--color-content-link)
      --fl-link-hover: var(--color-content-link-hover)
      --fl-font: var(--typography-body-font-family)
      --fl-headline-font: var(--typography-headline-font-family)
      --fl-item-title: var(--color-content-list-title)
  .icon-cards:
    note: null
    values:
      --ic-ink: var(--color-content-default)
      --ic-accent: var(--color-content-brand)
      --ic-border: var(--color-border-default)
      --ic-font: var(--typography-body-font-family)
      --ic-headline-font: var(--typography-headline-font-family)
      --ic-radius: var(--border-radius-container)
      --ic-hover: var(--color-button-secondary-bg-hover)
      --ic-item-title: var(--color-content-list-title)
  .external-link-cards:
    note: null
    values:
      --elc-ink: var(--color-content-default)
      --elc-accent: var(--color-content-brand)
      --elc-link: var(--color-content-link)
      --elc-link-hover: var(--color-content-link-hover)
      --elc-border: var(--color-border-default)
      --elc-font: var(--typography-body-font-family)
      --elc-headline-font: var(--typography-headline-font-family)
      --elc-radius: var(--border-radius-container)
      --elc-chip-bg: var(--color-bg-chip)
      --elc-hover-bg: var(--color-button-secondary-bg-hover)
      --elc-pressed-bg: var(--color-button-secondary-bg-active)
      --elc-item-title: var(--color-content-list-title)
  .heading-block:
    note: null
    values:
      --hb-ink: var(--color-content-default)
      --hb-subtle: var(--color-content-subtle)
      --hb-accent: var(--color-content-brand)
      --hb-title-ink: var(--color-content-brand-strong)
      --hb-font: var(--typography-body-font-family)
      --hb-headline-font: var(--typography-headline-font-family)
  .header:
    note: null
    values:
      --hd-ink: var(--color-content-default)
      --hd-accent: var(--color-content-brand)
      --hd-font: var(--typography-body-font-family)
      --hd-shadow: var(--shadow-default-color)
  .horizontal-cards:
    note: null
    values:
      --hc-ink: var(--color-content-default)
      --hc-subtle: var(--color-content-subtle)
      --hc-accent: var(--color-content-brand)
      --hc-link: var(--color-content-link)
      --hc-link-hover: var(--color-content-link-hover)
      --hc-border: var(--color-border-default)
      --hc-font: var(--typography-body-font-family)
      --hc-headline-font: var(--typography-headline-font-family)
      --hc-radius: var(--border-radius-container)
      --hc-item-title: var(--color-content-list-title)
  .hero:
    note: null
    values:
      --hero-ink: var(--color-content-default)
      --hero-inverse-ink: var(--color-content-inverse)
      --hero-accent: var(--color-content-brand)
      --hero-font: var(--typography-body-font-family)
      --hero-headline-font: var(--typography-headline-font-family)
      --hero-panel-light: var(--color-button-secondary-bg-hover)
      --hero-panel-dark: var(--color-content-brand)
      --hero-canvas: var(--color-bg-hero-canvas)
      --hero-radius: var(--border-radius-default)
  .btn:
    note: null
    values:
      --btn-font: var(--typography-body-font-family)
      --btn-radius: var(--border-radius-default)
---

# Design Data Schema — Tokens

**Layer 1. Read-only.** This file is the single source of truth
for design tokens. `css/tokens.css` is generated from the
`brands` and `bridges` blocks above — never hand-edit it; the
build overwrites it.

## The brand contract

A brand is exactly one entry under `brands` — nothing else.
Components read tokens through their bridge (`--<ns>-*`)
variables and must never contain a brand name, with the single
sanctioned exception of the Header logo pattern (a brand-owned
asset, not a themeable value — see `header.css`'s four functional
`[data-theme]` selectors).

## Token architecture — three layers preserved

1. **Semantic** — the `brands.<id>.values` block above. Per-brand
   resolved values, generated into a `[data-theme="<id>"]` block.
2. **Component bridge** — the `bridges.<selector>` block above.
   Each component claims a short namespace (`--fl-*`, `--hero-*`,
   etc.) mapped to semantic values via `var()`. Unlike the
   semantic layer, bridges don't vary per brand — one definition,
   theme-independent, because they only ever reference semantic
   custom properties, which themselves resolve differently per
   `[data-theme]` ancestor.
3. **Component rule** — lives in each component's own CSS,
   consumes the bridge. Out of scope for this file.

## Naming grammar

`--{context}-{role}-{variant}-{state}`. Not all segments are
always present — `--color-bg-chip` is as short as it gets;
`--color-button-secondary-outline-bg-hover` uses all four. Written
down explicitly per the Leaf Design System review (Leaf's
`colors.md` documents the same discipline as
`--leaf-color-{context}-{role}-{variant}-{state}`) — this was
previously implicit convention in this library, not an enforced
rule.

## Global tokens (theme-independent)

Spacing, shadow elevation, and breakpoints do not vary per brand —
same value regardless of `[data-theme]` ancestor. Added following
the Leaf Design System review; this library previously had no
spacing scale and no shadow scale beyond the single per-brand
`--shadow-default-color` (below).

- **Spacing** — 8px-based scale (`--spacing-8` through
  `--spacing-64`). Use for all padding, margin, and gap; never
  hardcode pixel values.
- **Shadow elevation** (`--shadow-small` / `--shadow-default` /
  `--shadow-large`) — offset/blur/spread only, colorless. The
  existing per-brand `--shadow-default-color` (see each brand's
  `values` block) supplies the brand-tinted color component.
  Compose the two where a themed shadow is needed:
  `box-shadow: var(--shadow-default) var(--shadow-default-color);`
  is not valid CSS shorthand as written — combine explicitly per
  component, e.g. `0 8px 6px 0 var(--shadow-default-color)`,
  reusing the elevation numbers from `--shadow-default` as the
  literal offset/blur values. (Flagged: the two shadow systems
  need a real merge pass before first use — noted here rather than
  silently resolved.)
- **Breakpoints** (`--breakpoint-tablet` / `--breakpoint-desktop`)
  — reference values matching `component-library.md`'s existing
  640px/1024px container-query breakpoints. Cannot be injected as
  custom properties into `@container` conditions (a real CSS
  limitation, not a tooling gap) — kept here so every component
  author reads the same two numbers instead of re-deriving them.



| id | label | kind |
|---|---|---|
| `evernorth` | Evernorth | Production brand |
| `tcg` | The Cigna Group | Production brand |
| `chc` | Cigna Healthcare | Production brand |
| `white-label` | White Label | Neutral skin — proof the architecture works with zero brand identity attached |

## Provenance

Every `notes` entry under a brand's `values` block flags a value
that is mockup-derived, inferred, or provisional rather than
sourced directly from the design-token export — carried forward
unchanged from `brands.md`'s per-brand-deviations section. Do not
resolve these silently; they're flagged so a real spec can
replace them later without an audit.

## Procedures

Unchanged from `brands.md` §6 — add/swap/remove/fork a brand by
editing this file's `brands` block only. Never touch a component
`.css` file for a token-layer change; if you find yourself
needing to, something belongs here instead.
