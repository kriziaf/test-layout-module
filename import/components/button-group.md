---
label: Button Group
status: stable
tier: atom-host
variants:
  - default
  - inverse
bridgeNamespace: --btn-
files:
  html: components/button-group/button-group.html
  css: components/button-group/button-group.css
  docs: components/button-group/button-group.md
dependsOn: []
tokensConsumed:
  - border-radius/default
  - typography/body/font-family
  - color/button/primary/*
  - color/button/secondary/*
  - color/button/accent/*
slots:
  - panel
  - note
contentJob: chrome
interactive:
  atom: .btn
  modifiers:
    - .btn--primary
    - .btn--secondary
    - .btn--inverse
  states:
    - default
    - hover
    - active
    - focus-visible
    - disabled
  disabledApi: aria-disabled="true" (anchors) or [disabled] (buttons)
  elements:
    - a
    - button
notes:
  - Delivers the shared .btn atom consumed by heading-block, form, hero, text-and-image
  - Section itself is a showcase; the atom is the real deliverable
---

# Button Group

**Layer 1. Read-only.** This file is the single source of truth
for Button Group. Its entry in `components.json` is generated
from the front matter above — never hand-edit that entry
directly; the build overwrites it.

## Short description

The button atom in both palettes: Primary (filled) and Secondary
(outline), each in Default and Inverse sets, with all five
states.

## Composition taxonomy — where this sits

| Level | Definition | Owns | May depend on |
|---|---|---|---|
| **Atom** | A single reusable element with no internal layout of its own. Defined once, consumed everywhere. | Its own states | Tokens only |

`.btn` (defined in `button-group.css`) is the atom. Button Group
the *component* is a showcase for it — the atom is the actual
deliverable, consumed by Heading Block CTAs, Form actions, Hero
actions, and Text and Image actions. Consumers must include
`button-group.css` in their REQUIRED INCLUDES.

Rule that follows from atom status: **atoms never import
component CSS.** `.btn` reads button tokens directly rather than
through a bridge, because those tokens are already
button-scoped — this is why `bridgeNamespace` above is thin
(font + radius only; color comes straight from the semantic
button tokens).

The `.btn` atom exists because four components had duplicated the
same button rules before it was extracted.

## Markup and states

`.btn .btn--primary|--secondary` (+ `.btn--inverse` on dark brand
surfaces). Works on `<a>` and `<button>`. Disabled =
`aria-disabled="true"` (anchors) or `[disabled]` (buttons); both
get `pointer-events: none`. Focus = `:focus-visible` only, 2px
ring, offset 2px. 2px border always present (transparent-border
technique keeps geometry stable across states). Padding
.75rem/1.75rem; radius = `border-radius/default` token (pill in
TCG/CHC).

### Standard set (spec values = Evernorth; other brands read their own semantic button tokens)

| state | primary bg / text | secondary text+border / bg |
|---|---|---|
| default | #035C67 / #FFF | #035C67 / transparent |
| hover | #024A52 | #00363D / #EAF4F6 |
| pressed (:active) | #012529 | #00171A / #CCE7EA |
| focus | hover bg + 2px #012529 ring | hover treatment + 2px #00171A ring |
| disabled | #EAEAEA / #949494 | #999999 text, #ABABAB border / #EAEAEA |

### Inverse (accent) set — `.btn--inverse`

Spec'd for Evernorth (mint on dark); other brands derive
white-on-brand (see `Project-roadmap.md` — non-Evernorth accent
buttons).

| state | primary bg / text | secondary text+border / bg |
|---|---|---|
| default | #00FEAF / #003034 | #3EFFC0 / transparent |
| hover | #12F3A9 | #12F3A9 / #003826 |
| pressed | #00D18D | #00D18D / #00171A |
| focus | hover + 2px #12F3A9 ring | hover + ring |
| disabled | #ABABAB / #003034 | #ABABAB / transparent |

## Accessibility (from the library-wide standard, as it applies here)

- Every interactive element has a visible `:focus-visible` state
  — never `:focus` alone, never `outline: none` without a
  replacement.
- 2px ring, `outline-offset: 2px`, colored by a dedicated
  focus-ring token per button type.
- Disabled interactive elements use `aria-disabled="true"`
  (anchors) or `[disabled]` (buttons), both paired with
  `pointer-events: none`.
- No JavaScript required for any state.

## Content

- Labels: verb-first, two to four words ("Register now", "Find
  care").
- Primary is the one action you want taken; Secondary is the
  alternative path.
- Inverse set exists only for dark brand surfaces (Hero Inverse
  and similar).
- Disabled buttons should be rare in marketing pages; prefer
  hiding an unavailable action.
- Never two Primaries side by side; the pair is always Primary
  plus Secondary.
- Button labels are not sentences: no punctuation, no "click
  here."
- Keep both labels in the same register (both actions, or both
  destinations).

## Provenance

Non-Evernorth accent (inverse) button sets are derived
white-on-brand, not separately spec'd — flagged in
`Project-roadmap.md` as a known gap pending real specs.
