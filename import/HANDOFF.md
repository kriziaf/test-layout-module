# WP3 Handoff — Design Data Schema, Layer 1 Migration

## What's already proven (do not redo)

- `tokens.md` — Layer 1 source for all tokens. Round-trips
  cleanly to the hand-authored `tokens.css` via `scripts/build.py`
  (0 mismatches across 14 selectors: 4 brand blocks + 10 bridges).
  Also carries a new `global` block (spacing/shadow/breakpoint
  scales) added after a review against Cigna's Leaf Design System.
  **`tokens.css` is now a build output — never hand-edit it.**
  Regenerate with `python3 scripts/build.py` after any `tokens.md`
  change.
- `components/button-group.md` — the ONE hybrid component done so
  far (YAML front matter = its `components.json` entry, prose =
  everything relevant pulled from `component-library.md` +
  `button-group.md`). Proven to round-trip field-for-field via
  `scripts/export_entry.py` (currently hardcoded to button-group
  only — generalize before reuse).

## What's next (WP3, not started)

Migrate the remaining 9 components into the same hybrid shape:
`header`, `hero`, `text-and-image`, `heading-block`, `form`,
`list-item`, `horizontal-cards`, `external-link-cards`,
`highlight-bar`, `icon-cards`.

Then: `content.md` (Core Content Standard + voice registry,
extracted from `content-system.md`), full `components.json`
regeneration (not just per-entry diffing), `boundaryCheck`
re-verification, and `design.md` task-routing table updates.

## Effort tiering (grounded in dependsOn/slots/variants, not guessed)

| Tier | Components | Why harder |
|---|---|---|
| ~1x (same as button-group) | external-link-cards, highlight-bar, icon-cards | No deps, comparable variant count |
| ~1.5x | header, text-and-image | Header carries the ONLY sanctioned `[data-theme]` exception in any component CSS — get this prose exactly right |
| ~2x | hero, list-item, horizontal-cards | Depend on button-group and/or heading-block; list-item carries the `__header`/`__heading` naming trap |
| ~2.5x | heading-block, form | heading-block: 6 variants, `--no-cta` API-marker behavior. form: depends on BOTH heading-block + button-group, two-column vs. stacked is a documented "split ownership" decision — don't flatten it during extraction |

## The one real risk (found during button-group, not hypothetical)

Prose for each component is **scattered across `component-library.md`**,
not organized per-component — the composition-taxonomy table row,
the accessibility-standard subsection (where applicable), the
interaction-states section, and the inventory-table row are each
in different parts of the file. Extracting "by feel" risks silently
dropping content — exactly the doc-drift failure this whole
restructure exists to prevent.

**Recommend:** before running all 9, do ONE more component from a
different tier first (e.g. `form` — highest tier, dependency-heavy)
as a second data point, and write down the extraction checklist
that emerges, THEN batch the rest against that checklist.

## Files in this handoff

```
tokens.md                      — Layer 1 tokens source
scripts/build.py                — tokens.md -> tokens.css
scripts/validate_roundtrip.py   — round-trip diff checker (wire into CI)
scripts/export_entry.py         — hybrid .md -> components.json entry
                                   (currently button-group-only, generalize)
components/button-group.md      — the one proven hybrid component
```

Source repo for everything referenced above:
https://github.com/kriziaf/test-layout-module
