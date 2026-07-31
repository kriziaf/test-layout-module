# Reusing the Draft Room UI Shell

Two files: `shell.css` (the styles) and `preview.html` (a live reference showing every component — open it in a browser to see what each class looks like).

This is the **app-chrome layer only** — page background, cards, toolbar, step indicator, buttons, inputs, sidesheet, toggle. It's deliberately separate from any product's brand tokens (colors, fonts specific to a client). Everything here is its own self-contained visual language: off-white page, white bordered cards, Montserrat headings, Inter body text, one teal accent color.

## What to tell Claude to reuse it in another project

Copy/paste something like this at the start of a new conversation:

> I have a UI shell stylesheet (`shell.css`) with a specific visual style: off-white page background (#F7F7F5), white cards with a light gray border and 12px radius, Montserrat for headings/labels/buttons, Inter for body text, and one teal accent color (#035C67) used for primary buttons, active states, and links. It includes reusable classes for: a page heading block (`shell-eyebrow` + `shell-title`), a toolbar bar with pill buttons (`shell-toolbar`), a numbered step indicator (`shell-steps`), card containers (`shell-card`), three button styles (`shell-btn-primary`, `shell-btn-outline`, `shell-btn-text`), inputs (`shell-input`, `shell-textarea`), a slide-in sidesheet panel (`shell-sidesheet`), and a toggle switch (`shell-toggle`). I've attached the CSS file — please use these classes/tokens for [describe your new UI] rather than inventing new styling from scratch. Reference `preview.html` if you want to see what each component looks like.

Attach both `shell.css` and `preview.html` to that message.

## What's inside

| Class | What it's for |
|---|---|
| `.shell-page` | Max-width, centered page wrapper |
| `.shell-eyebrow` / `.shell-title` | Small uppercase teal label + bold heading, used above every major screen |
| `.shell-card` | The base white bordered container — forms, panels, previews all use this |
| `.shell-toolbar` + `.shell-toolbar__group/label/pill/spacer` | A horizontal bar of pill-button groups (used for breakpoint/brand switchers, but works for any filter/view toggle) |
| `.shell-steps` + `.shell-steps__item/num` | Numbered progress indicator, with `.is-active` / `.is-done` states |
| `.shell-btn-primary` / `.shell-btn-outline` / `.shell-btn-text` | Filled, outlined, and text-only button variants |
| `.shell-input` / `.shell-textarea` | Text field styling |
| `.shell-sidesheet` + overlay | Slide-in panel from the right, with dimmed backdrop |
| `.shell-toggle` | On/off switch |

## Retheming

Everything reads from CSS custom properties at the top of the file (`--shell-accent`, `--shell-bg`, `--shell-surface`, etc.). To reskin for a different brand, override those variables — nothing else needs to change. For example, to swap the accent color:

```css
:root {
  --shell-accent: #7C3AED;
  --shell-accent-hover: #6D28D9;
  --shell-accent-wash: #F3EEFF;
}
```

## Setup

1. Add the Google Fonts link (Montserrat + Inter) to your `<head>` — included as a comment at the top of `shell.css`.
2. Link `shell.css`.
3. Add `class="shell"` to your `<body>` tag.
4. Use the classes from the table above.
