# Design System Schema — Executive Summary

## The problem

Design decisions and their reasoning lived in scattered prose
across files, chat threads, and individual contributors' heads.
Hand-maintained inventories drifted from the actual code — as a
concrete example, a shipped component was missing from its own
documentation table for two release cycles before anyone
noticed. Reusing the system on another project meant
reverse-engineering it from scratch each time, because nothing
about it was portable by design.

## The solution

A **self-describing design system schema**: one entry file routes
any person or AI tool to exactly the reference material a given
task needs, a machine-readable inventory is **validated against
the real code** rather than hand-maintained, and brand-specific
content is walled off from the reusable architecture underneath
it. The system now checks itself — when documentation and code
disagree, that disagreement is caught automatically instead of
shipping silently.

## What's built today (Tier 0 — complete)

| | |
|---|---|
| Production components | 10, fully documented and cross-validated |
| Brand themes | 3 brands (Evernorth, The Cigna Group, Cigna Healthcare) + 1 neutral skin |
| Page templates | 3 (Homepage, Insights, Contact Us) |
| Accessibility | Standard documented and enforced by construction; formal audit not yet run |
| Reusability | Architecture and brand content are separated; the system is forkable for other brands or companies |

This tier is usable today by any designer, developer, or AI tool
pointed at the repository — no installation required.

## The maturity path

| Tier | What it adds | Status |
|---|---|---|
| **0 — Foundation** | Self-describing docs, machine-readable inventory, drift validation | ✅ **Done** |
| **1 — Zero-drift docs** | Documentation generated automatically from the data layer, so it can never go stale again; formal accessibility audit | Proposed next |
| **2 — Installable package** | npm package + CLI so any team can pull in the system and query it programmatically | Proposed next |
| **3 — Always-on AI integration** | A dedicated AI tool integration, the same pattern Adobe uses for its Spectrum design system today | Future |

Tiers 1–2 are the subject of this ask. Tier 3 mirrors an
approach already validated in production by a major design
system — this isn't speculative, it's a known destination.

## The ask

**2 FTE + part-time support, for 10–12 weeks**, to take the
system from Tier 0 to Tier 2:

| Role | Allocation | Responsibility |
|---|---|---|
| Design Systems Engineer (lead) | Full-time, all 6 sprints | Schema architecture, generator script, CLI, packaging |
| Component/Front-End Engineer | Full-time, sprints 1–3 | Component gaps, accessibility fixes, inventory accuracy |
| Content/Design Strategist | ~50%, sprints 1–3 & 6 | Voice and brand-boundary accuracy in generated docs |
| Design Systems Lead / PM | ~25%, all 6 sprints | Prioritization, review, sign-off (likely existing role) |

| Phase | Weeks |
|---|---|
| Tier 1 — zero-drift docs, accessibility audit | 6 |
| Tier 2 — package, CLI, publish pipeline | 6 |
| **Total** | **10–12 weeks** (8 weeks achievable with full dedication) |

**What this buys:** the accessibility gap closes, the
documentation-drift failure class is eliminated permanently, and
the system becomes something other teams can install and use
without reverse-engineering it — turning a one-off project asset
into reusable infrastructure.
