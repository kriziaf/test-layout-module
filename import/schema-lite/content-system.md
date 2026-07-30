---
title: Content System — Voice & Copywriting Guide
version: "1.35"
updated: 2026-07-27
kind: standard
entry_point: design.md
depends_on: [component-library.md]
---

# Content System — Voice & Copywriting Guide

The component library's default/demo content follows ONE brand
story so examples read as a coherent product rather than mixed
placeholder text. Page templates (A, B, C) are separate themed
case studies and intentionally use a different voice each; the
Homepage template (v1.23) already uses this same voice.

## The brand

A direct-to-consumer virtual care company (Zocdoc/Included
Health-style content genre; original copy, not reproduced from
any single company). Value proposition: same-day virtual visits,
transparent pricing, prescriptions handled end to end, and a
personal touch via health advocates and personalized programs.

## Component -> content job -> technique

| Component | Content job | Technique |
|---|---|---|
| Hero | Value proposition | Outcome-first headline (benefit, not feature); subhead = who it's for + how; ONE low-friction CTA verb (two only when a real secondary path exists, e.g. Hero Inverse's "Learn More") |
| Heading Block | Section framing | Short, connective; sets up what follows, makes no independent claim |
| List Item (links/stats/articles/accent) | Services & benefits | Benefit-led headers ("what's in it for you"); ALL FOUR variants share the same 6 underlying benefit ideas, reshaped per variant format, not rewritten from scratch |
| External Link Cards | Wayfinding | Answers "what do you want to do today?"; action-oriented |
| Horizontal Cards | News & insights / help content | Curiosity-driven headlines (how-to, numbers, questions) |
| Highlight Bar | Proof / trust | Confident, declarative stat claims, no hedging |
| Promo Banner **(candidate)** | Conversion | Same job as Form — value-exchange framing — but compressed to a single eyebrow + headline + body + one CTA; no field-level copy. Content inherited from whichever campaign surface it's embedded in, similar in spirit to Heading Block's connective-tissue role |
| Form | Conversion | Value-exchange framing, friction-reduction language |
| Header / Button Group | Chrome | Brand-neutral, generic labels — deliberately not narrative |

## The six canonical List Item benefits (shared verbatim across variants)

1. Integrated care networks — provider/specialist access, single platform, fewer referral delays
2. Transparent cost estimates — see cost before booking, no surprise bills
3. Prescription management — fill/refill/track via delivery or retail
4. 24/7 virtual care — board-certified clinicians, urgent/behavioral/chronic
5. Benefits made simple — one dashboard for deductibles, EOBs, spending accounts
6. Personalized health programs — condition management, coaching, preventive care

Links variant uses items 1–4 (with task-specific link labels).
Stats variant reframes items 1–4 with numbers (1.5M+, $0, 24/7,
5 min). Articles variant reframes items 1, 2, 3, 6 as editorial
headlines. Accent variant is the canonical full set (all 6).

## Status

Rewritten: Hero, List Item (pilot, v1.25); Horizontal Cards,
External Link Cards, Highlight Bar, Form, Text and Image
(rollout, v1.26).

Deliberately NOT rewritten: Heading Block — excluded from this
rollout by request. It's pure connective tissue reused inside
five other components, so its content is inherited from
whichever component embeds it and may not need independent
rewriting at all.

Header and Button Group were always out of scope by design
(chrome, not narrative content).
