# How to Reuse This Design System Schema

This folder is the **portable core** — the reference layer plus
the build-component skill, exported from the canonical repo. No
component code, no CSS, no images. It describes the *system*,
not one implementation of it.

## What's in here

| File | What it is |
|---|---|
| `design.md` | **Start here.** Router: non-negotiables, ecosystem map, task-routing table |
| `components.json` | Machine-readable component inventory (schema + data), includes boundaryCheck |
| `component-library.md` | Token architecture, composition taxonomy, interaction states, accessibility standard |
| `content-system.md` | Voice and per-component-type content technique |
| `layout-module.md` | Demo/template composition patterns, sync contracts |
| `brands.md` | Brand boundary, sanctioned exceptions, per-brand deviations |
| `Project-roadmap.md` | What's planned, parked, and known-incomplete |
| `skills/build-component/SKILL.md` | **Reusable Agent Skill** — the step-by-step procedure for building a new component correctly against this schema |

## To reuse in a new Claude session (chat)

1. Create (or open) a **Project** in Claude.
2. Upload all the files above (including the `skills/` folder) to
   that Project's **Project Knowledge**.
3. Start a new chat. `design.md` will be searchable automatically,
   and you can ask Claude to build a component "using the
   build-component skill."

## To reuse as an actual Agent Skill (Claude Code, or Skill-aware tools)

Drop the `skills/build-component/` folder into the project's
skills directory as-is. It's self-contained except for its
listed dependency: `design.md`, `components.json`,
`component-library.md`, `content-system.md`, and `brands.md`
must also be present in the same project for the skill to have
anything to build against.

## To reuse in a different tool (Cursor, VS Code, ChatGPT, etc.)

Same files — drop them into whatever context/file mechanism that
tool provides. Nothing here is Claude-specific.

## To adapt for a different brand or company

Everything transfers except the brand-specific values inside
`component-library.md`'s token-architecture section and
`brands.md`'s registry (section 2). `brands.md` section 6 has the
exact fork procedure. The skill itself needs no changes — it
already works purely in terms of "whatever tokens exist."

## What this does NOT include

Component artifacts, `tokens.css`, images, the demo, and page
templates. Those live in the full repo
(`design-system-repo.zip`), which is the canonical, git-tracked
source this export was generated from.

## Canonical source

This is a generated export, not an independently maintained
copy. The canonical, editable source is the git repo. If this
export and the repo ever disagree, the repo wins — regenerate
this folder from it rather than hand-editing these files
directly.
