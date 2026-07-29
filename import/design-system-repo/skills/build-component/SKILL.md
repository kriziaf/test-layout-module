---
name: build-component
description: Build a new UI component (from a design file, screenshot, or spec) that conforms to this repo's Design Data Schema — token-driven, brand-agnostic, and registered correctly across all three Schema Sync Trio files. Use this any time the user wants to add, extend, or scaffold a component in a project that has design.md, components.json, component-library.md, content-system.md, and brands.md present — even if they just say "build a component," "add a new section type," or describe a UI pattern without naming the schema explicitly. Also use this when asked to add a variant to an existing component, since the same trio-update discipline applies.
compatibility: Requires design.md, components.json, component-library.md, content-system.md, and brands.md to already exist in the project. This skill does not create the schema itself — see the portable core export for that.
---

# Build Component

Builds one component that plugs into an existing Design Data
Schema correctly on the first try — token-driven, themeable
across every brand with zero component-level brand logic, and
registered in every place the schema requires so nothing drifts
out of sync the moment it ships.

**Before doing anything else, read `design.md`.** It is the
router for this entire schema and states the non-negotiables
this skill enforces. If `design.md` is not present in the
project, stop and tell the user this skill needs the portable
core schema files first.

## Why the discipline matters

Every failure this pattern has produced in practice traces back
to skipping one of the steps below under time pressure — not to
the steps being wrong. A documentation table that doesn't match
the code is worse than no documentation, because it's trusted.
Treat every step here as required, not optional polish.

## Step 1 — Understand the source

If given a design file (SVG, screenshot, Figma export), decode
it structurally before writing any code:
- Identify distinct **variants** (different layouts/treatments of
  the same concept) vs. distinct **states** (hover, pressed,
  focus, disabled — same layout, different styling).
- Extract real geometry and colors rather than guessing —
  measure, don't eyeball.
- Note anything that doesn't map cleanly to an existing token
  (a color, radius, or spacing value with no equivalent in
  `component-library.md`'s token architecture). Flag these
  explicitly to the user rather than silently inventing a value
  or silently reusing the nearest existing token — both hide a
  real gap.

If given only a spec or description, confirm the variant list and
content slots with the user before building — guessing wrong here
means redoing every later step.

## Step 2 — Resolve tokens, never hardcode

Read `component-library.md`'s token architecture section first.
Every color, font, radius, and spacing value the component needs
must resolve through the existing semantic token layer:

```
[data-theme="evernorth"] { --color-content-brand: #035C67; }   1. semantic (brand)
.your-component { --yc-accent: var(--color-content-brand); }   2. bridge (component)
.your-component__el { color: var(--yc-accent); }               3. rule
```

- Pick a short, unused bridge-variable prefix (`--<ns>-*`) for
  the new component and check it doesn't collide with an
  existing one in `components.json`.
- If a needed value has no existing token, do not invent one
  silently. Either derive it from the nearest existing semantic
  token (and say so, e.g. "derived from `content/brand`, not in
  the original token export") or ask the user. Both are fine;
  silently guessing is not.
- **Never write a functional `[data-theme="..."]` selector
  inside the component's own CSS.** Read `brands.md` section 4
  before doing this under any circumstances — there is exactly
  one sanctioned exception in the whole system (a brand-logo
  reveal), and a new component almost certainly isn't it. If you
  think you need one, the value belongs in the token layer
  instead.

## Step 3 — Build the artifact trio

Every component ships as three files, together:

| File | Contains |
|---|---|
| `components/<name>/<name>.html` | Shippable markup — one self-contained `<section>` per variant, plus a banner comment: required includes, required context (`data-theme` ancestor), variant API, content slots, and any judgment calls made in Step 1/2 |
| `components/<name>/<name>.css` | Component styles, consuming only the bridge variables from Step 2. No `!important`. Responsive via `@container` queries only (never viewport media queries), wrapped in `.component-viewport` |
| `components/<name>/<name>.md` | Content annotations: short description, content guidance per `content-system.md`'s technique table, marketing notes. Never spec/implementation details — that's what the `.html` banner is for |

Use BEM: block class = folder name = file name
(`.list-item` → `components/list-item/`). Variant = modifier
class on the section root (`.list-item--accent`), never a
separate element.

## Step 4 — Update the Schema Sync Trio (do not skip)

This is the step most likely to get skipped under time pressure,
and skipping it is exactly how documentation drift happens. All
three of these update in the **same** change, never one without
the others:

1. **`components.json`** — add the component's entry: variants,
   file paths, `dependsOn` (if it embeds or requires another
   component/atom), `bridgeNamespace`, `tokensConsumed`, `slots`,
   `grid` (if it has one), `contentJob`.
2. **`component-library.md`** — add a row to the Component
   Inventory table matching the `components.json` entry.
3. **`content-system.md`** — add a row to the component→content-job
   table stating which copywriting technique this component's
   content follows (see the existing table for the pattern —
   value proposition, wayfinding, proof-and-trust, etc.).

If a project has a `scripts/validate.py`, run it now — it checks
exactly this trio for consistency and will catch a missed step
immediately rather than letting it ship.

## Step 5 — Register for use

- If the project has a demo/browser tool (e.g. `demo.html`), add
  the component to its registry and copy each variant's markup
  into a `<template>` — remember this is a COPY of the artifact,
  not a second source of truth; re-sync it after any later
  artifact edit.
- If the component should appear in any page template, extract
  its markup the same way, and rewrite relative asset paths for
  the template's location (a common miss — verify images actually
  load, don't assume the path is right).

## Step 6 — Verify before calling it done

Do not consider the component finished from visual inspection
alone. At minimum:
- Render the artifact standalone and confirm every variant
  displays with no console/page errors.
- Cycle through every brand mode (`data-theme`) and confirm
  colors/fonts actually change and nothing stays hardcoded.
- Cycle through mobile/tablet/desktop breakpoints.
- If the component has interactive states (hover, pressed, focus,
  disabled), trigger each one and check the computed style
  changed — a state that "looks right" in a screenshot can still
  be unreachable in real interaction.
- Check for nested `<a>` tags if any card/section is both a link
  and contains inner links — this is invalid HTML and a repeat
  offender. If a card needs both, make the outer element a `<div>`
  and put real `<a>` tags inside it, not the reverse.

## Common pitfalls (from real failures on this pattern)

- **Assuming a "generic" file still has placeholder content.**
  If a component or shared file has been through a content
  rollout already, its "Label Text"-style placeholders may be
  gone. Check the actual current content before writing a
  find-and-replace against it.
- **Non-greedy regex/string matching across repeated structures.**
  If a document has multiple similar blocks (e.g. several cards
  with the same class name), a loose match can grab the wrong
  boundary. When editing generated or templated markup
  programmatically, scope the edit to one section at a time and
  verify the resulting count, not just "did it run without
  erroring."
- **Margin vs. padding for painted gaps.** A margin between two
  elements is transparent — if the space needs to show a
  background color, it must be padding on the element that owns
  that background, not margin on the next element.
- **Named vs. unnamed container queries.** Check which convention
  the project's `.component-viewport` (or equivalent) actually
  uses before writing `@container <name> (...)` — an unnamed
  query never matches a named one and vice versa, silently.

## When you're done

Report back: the component name, its variants, which token
values were resolved vs. derived vs. flagged as gaps, and
confirmation that all three Schema Sync Trio files were updated
in this change. If `scripts/validate.py` exists, report its
result.
