---
title: Brand Boundary — Reference
version: "1.36"
updated: 2026-07-29
kind: standard
entry_point: design.md
depends_on: [component-library.md]
---

# Brand Boundary — Reference

## 1. The brand contract

A brand in this system is exactly one `[data-theme="..."]` block
in `css/tokens.css` — nothing else. Components read tokens
through their `--<ns>-*` bridge variables and must never contain
a brand name. This is what makes one component render correctly
across every brand without a single `if` statement: the theme
attribute changes, the tokens it resolves to change, nothing in
the component's own CSS does.

There is exactly one sanctioned exception to this rule (see
§4), and it exists for a structural reason — logos are brand
assets, not values a token can hold.

## 2. Registry

| `data-theme` value | Display name | Kind |
|---|---|---|
| `evernorth` | Evernorth | Production brand |
| `tcg` | The Cigna Group | Production brand |
| `chc` | Cigna Healthcare | Production brand |
| `white-label` | White Label | **Neutral skin** — not a named brand. Exists as the architecture's proof that it works with zero brand identity attached |

Character notes (see `tokens.css` for exact values — this file
never repeats them):

- **Evernorth** — square-leaning geometry (smaller border radii),
  teal-family brand color.
- **The Cigna Group / Cigna Healthcare** — pill-shaped buttons,
  larger container radii, blue-family brand color. The two share
  the same shape language; they differ in typography and a few
  content-color specifics.
- **White Label** — the most neutral geometry, and the only mode
  where section and item headings are deliberately desaturated
  rather than brand-colored (see §5).

## 3. Required token surface

**Known gap:** the four theme blocks currently define different
numbers of tokens (checked against `tokens.css` directly, not
hardcoded here — counts will drift from this file over time,
which is exactly why this section is a category checklist and
not a number). There is no enforced checklist today of what a
brand block must define, which means a brand can silently fall
back to an unset token's default rather than an intentional
choice.

Every `[data-theme]` block should define a value for each of
these categories:

- **Content colors** — default, subtle, brand, brand-strong,
  list-title, link, link-hover
- **Border colors** — default and any component-specific border
  variants in use
- **Button state colors** — primary and secondary, each across
  default / hover / active / focus / disabled, plus the inverse
  (accent) set where applicable
- **Background surfaces** — page/component backgrounds, chip
  backgrounds, any brand-dark or brand-xstrong surfaces
- **Typography** — headline and body font families, and any
  brand-specific type ramp overrides
- **Shadow** — the default shadow color

This checklist is the thing to run a new brand against before
considering it complete — not a substitute for `tokens.css`.

## 4. Sanctioned exceptions

**The Header logo pattern is the only currently-approved case.**
`components/header/header.css` contains four functional
`[data-theme="..."]` selectors, one per brand, that reveal the
correct inline logo SVG. This is allowed because:

- Logos have literal, brand-owned fills — they are assets, not
  themeable values, and there is no token that could hold "which
  of four inline SVGs to show."
- No component other than Header currently needs this pattern.

**The rule for adding a future exception:** a brand-named
selector is only acceptable for a brand-owned *asset*
(logo, wordmark, or similar) — never for a color, typography
value, spacing value, or any other styleable property. Anything
styleable belongs in the token layer, full stop.

## 5. Per-brand deviations

- **White Label neutralizes headings.** Both section-level
  headings (`color/content/brand-strong`) and item-level headings
  (`color/content/list-title`) resolve to a neutral gray in White
  Label, while the other three brands keep headings in their
  brand color. This is intentional — a neutral skin with
  brand-colored headings would defeat the purpose.
- **CHC's headline font is licensed and not yet supplied.** Value
  Serif Pro / Value Sans Pro are the intended fonts; the system
  currently falls back to Georgia/Helvetica until the actual font
  files are provided.
- **The inverse (accent) button set is fully specified for
  Evernorth only.** TCG, CHC, and White Label derive a
  white-on-brand fallback because no accent color spec exists yet
  for those brands.
- **Evernorth's card-chip background came from a mockup**, not
  the original design-token export, and has no equivalent token
  ID. The other three brands derive their chip color from an
  existing token instead.
- **White Label's Header logo is a text placeholder** — no real
  logo asset has been supplied for that mode.

## 6. Procedures

**Add a new brand**
1. Add a new `[data-theme="<id>"]` block to `tokens.css`,
   defining every category in §3.
2. Do not touch any component `.css` file — if you find yourself
   needing to, something belongs in the token layer instead.
3. Add the new mode to `components.json`'s brand list and to
   every artifact's brand-mode documentation reference.
4. Register the new logo in `header.css` (the one sanctioned
   exception) if the brand has a distinct logo.

**Swap or rename an existing brand's theme key**
1. Rename the `[data-theme="..."]` block in `tokens.css`.
2. Update the four `header.css` selectors (they're the only
   functional references to a brand name in any component).
3. Update `components.json` and all artifact default
   `data-theme` attributes.

**Remove a brand**
1. Delete its `[data-theme]` block from `tokens.css`.
2. Delete its selector from `header.css`.
3. Remove it from `components.json` and this file's registry.

**Fork the system for a different company entirely**
1. Copy the taxonomy and token *structure* from
   `component-library.md` and this file's §1, §3, and §4 — the
   rules, not the values.
2. Replace every value in `tokens.css` with the new company's
   design tokens, following the §3 checklist so nothing is
   silently missing.
3. No component file needs to change. If one does, the boundary
   described in §1 was already broken before the fork.
