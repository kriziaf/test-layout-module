---
title: Ecosystem Flow — Reference Files, Data, and Artifacts
version: "1.36"
updated: 2026-07-27
kind: diagram
entry_point: design.md
---

# Ecosystem Flow

How `design.md`, the context layer, the data layer, and the
component artifacts relate. Five layers, one feedback loop.

```mermaid
flowchart TD
    subgraph L1["Layer 1 — Entry Point"]
        DESIGN["design.md<br/><i>router · non-negotiables · task table</i>"]
    end

    subgraph L2["Layer 2 — Context Layer (human + AI readable)"]
        CL["component-library.md<br/><i>taxonomy · states · a11y standard</i>"]
        CS["content-system.md<br/><i>voice · content jobs</i>"]
        LM["layout-module.md<br/><i>demo shell · templates · sync contracts</i>"]
        BR["brands.md<br/><i>brand boundary · sanctioned exceptions</i>"]
    end

    subgraph L3["Layer 3 — Data Layer (machine readable, authoritative)"]
        CJ["components.json<br/><i>inventory · deps · slots · states</i>"]
        TC["tokens.css<br/><i>resolved runtime tokens, per brand</i>"]
        VJ["variables.json<br/><i>upstream design-tool export</i>"]
    end

    subgraph L4["Layer 4 — Artifact Layer (the deliverable)"]
        ART["components/&lt;name&gt;/<br/><i>.html + .css + .md trio, x11</i>"]
    end

    subgraph L5["Layer 5 — Delivery Layer"]
        DEMO["demo.html<br/><i>live component + template browser</i>"]
        TPL["templates/*.html<br/><i>Homepage · Insights · Contact Us</i>"]
    end

    DESIGN -- routes to --> CL
    DESIGN -- routes to --> CS
    DESIGN -- routes to --> LM
    DESIGN -- routes to --> BR

    CL -- describes --> CJ
    CL -- describes --> TC
    BR -- governs --> TC
    LM -- describes --> TPL

    VJ -- resolved into --> TC
    CJ -- documents --> ART
    TC -- styles --> ART

    ART -- composed into --> DEMO
    ART -- composed into --> TPL

    ART -. "validated against<br/>(boundary + drift checks)" .-> CJ

    classDef entry fill:#0B5FFF,color:#fff,stroke:#0B5FFF
    classDef context fill:#EAF2FF,color:#0B2A5C,stroke:#0B5FFF
    classDef data fill:#0B2A5C,color:#fff,stroke:#0B2A5C
    classDef artifact fill:#FFF4E5,color:#5C3A00,stroke:#C77700
    classDef delivery fill:#E9F9EE,color:#0F5C2E,stroke:#1E9E4A

    class DESIGN entry
    class CL,CS,LM,BR context
    class CJ,TC,VJ data
    class ART artifact
    class DEMO,TPL delivery
```

## Reading the diagram

**Downward arrows (solid)** are the normal path: `design.md`
routes to the context layer, the context layer describes the
data layer, the data layer documents and styles the artifacts,
and the artifacts compose into what ships.

**The dashed arrow is the loop that makes this a system rather
than a pile of docs.** `components.json` isn't just descriptive —
it's checked against the real artifact files (do the declared
variants actually exist in the HTML? does the declared bridge
namespace actually appear in the CSS? are the declared
dependencies actually linked?). When that check fails, the data
layer is wrong and gets fixed — not the other way around. This
loop is what prevented the inventory-table drift that happened
repeatedly before `components.json` existed.

**Two things never point upward:** artifacts never describe
themselves back into the context layer (a component's own `.md`
file documents *content*, not architecture), and the delivery
layer (demo, templates) never feeds back into anything — it's a
pure consumer, disposable and regenerable at any time.

## Layer summary

| Layer | Files | Authoritative for | Consumed by |
|---|---|---|---|
| 1 — Entry | `design.md` | Task routing, non-negotiables | Anyone/anything starting work |
| 2 — Context | `component-library.md`, `content-system.md`, `layout-module.md`, `brands.md` | System reasoning, standards, voice | Humans, AI sessions |
| 3 — Data | `components.json`, `tokens.css`, `variables.json` | Structured facts, resolved values | Layer 2 docs, Layer 4 artifacts |
| 4 — Artifact | `components/<name>/` (×11) | The actual deliverable | Layer 5 |
| 5 — Delivery | `demo.html`, `templates/*.html` | Nothing — pure composition | End users, stakeholders |
