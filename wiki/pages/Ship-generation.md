<!-- Hand-written mechanics page. Code lineage (kept out of the reader-facing text on purpose):
     lib/shipgenerator.lua (createShip/Defender/Carrier/Military/Trading/Freighter/Mining),
     lib/plangenerator.lua + plangenerator/lib/generator.lua (procedural hull/station assembly,
       GeneratePlanFromStyle, getShipStyle, selectMaterial, makeShipPlan/makeFreighterPlan/makeStationPlan/makeFighterPlan),
     lib/SectorGenerator.lua (positioning, station placement, asteroid fields, wormholes, gates,
       findStationPositionInSector, getPositionInSector, addAmbientEvents, createStation, createStationConstructionSite),
     lib/galaxy.lua (Balancing_* curves: GetSectorShipVolume, GetSectorStationVolume, GetShipVolumeDeviation,
       turrets, HP, tech, richness, material strength, GetDimensions).
     Block placement and GeneratePlanFromStyle are engine-side (C++); the numbers here are what the Lua curves compute.
     Image assets: see wiki/ASSETS.md. -->
# Ship generation

**Ship generation** is how Avorion builds every NPC craft and station you meet. The game never stores
ships as fixed models — it grows each one from a faction's visual "style", then scales the result by **how
close the sector is to the galactic core**. That single dial is why enemies near the rim are small and
weak, and why ships near the centre are huge, tanky and bristling with turrets.

> **In short:** distance from the core is the master difficulty dial. Move coreward and NPC ships get
> **bigger**, gain **more hit points**, carry **more turrets**, fight with **higher-tech gear**, and drop
> **better loot** — all at once. Faction home-defence ships (**Defenders**) are the spike: far tougher than
> the patrols around them.

The same distance-from-core scaling drives [Combat](Combat) difficulty, [drop value](Goods), and the
[material](Building-knowledge) you can expect to salvage.

## How a ship is built

Every craft is assembled on the spot from three ingredients: the **faction**, a target **size**, and the
**sector's position**.

1. **Hand-authored hulls first.** If a faction ships pre-made hulls (or a mod adds them), one of those is
   used as-is and the rest of this process is skipped.
2. **The faction's style.** Otherwise the game looks up that faction's **style** — its silhouette, colours
   and block-shape grammar, generated once from the faction's seed and then reused. This is why every ship
   of a faction looks related but no two are identical.
3. **Growing the hull.** The engine grows an actual block tree from that style, using a per-ship random
   **seed**, until it reaches the requested size. The grammar supplies shapes — spheres, rings, rounded
   hulls, station discs — each laying down a symmetric cluster of [hull, edge and corner
   blocks](Building-knowledge). Fixed grammar + varying seed = ships that look hand-built but never repeat.

How large a craft is allowed to get depends on its role:

| Craft role | Size cap |
|:--|--:|
| Warship hull | 6,000 |
| Freighter / Carrier / Miner | 5,000 |
| Station | 10,000 |
| Fighter | 200 |

**Material** is chosen from the sector's technology level: the closer to the core, the more likely the
higher-tier materials. Past the barrier ring (more than ~147 sectors out) Avorion is downgraded to Ogonite.
Material sets both the look and each block's durability (below).

### Stations

Stations use the same growth process at a larger scale (size cap 10,000). The game derives the look from
the station's type — a Shipyard, Factory, Mine, Farm and so on — grows the plan, finds a clear spot that
doesn't overlap a neighbour, and attaches the station's economy scripts.

A **construction site** is a finished station plan *degraded* back into scaffolding: outer blocks are
swapped to Framework roughly 1-in-5, interior blocks 1-in-14, and Framework struts are added around
1-in-3 blocks — producing the half-built look that finishes into the real station over time.

## Distance from the core is the master dial

*[📷 Screenshot needed — ASSETS.md: images/galaxy-map-regions.png]*

Every structural number a generated craft has flows from one input: **how far the sector is from the
galaxy centre**. Picture three "core-ness" sliders that all read **1 at the very centre** and fall to **0**
toward the edge — one across the whole galaxy, two steeper ones that hit zero around 400 and 350 sectors
out. Size, hit points, turret count and gear quality are all read off those sliders.

### Size

Average ship size is nearly flat across the outer galaxy and then climbs sharply in the last stretch toward
the core:

| Region | Approx. average ship size |
|:--|--:|
| Galactic edge | 150 |
| Mid galaxy (≈ 350–400 sectors out) | ~1,000–1,500 |
| Galactic core | ~2,900 |

Within a sector, each ship rolls its own **size multiplier** from **×1 up to ×11**, heavily skewed toward
the low end — so most craft are modest, with the occasional giant. Stations reuse the ship size ×100
(capped at 150,000) with a gentler ×1–×3.5 roll.

### Hit points

A craft's durability isn't stored separately — it comes from **size × local material strength**. As a rule
each block carries about **4×** its volume in durability, and core-ward materials (Ogonite, Avorion) are
far stronger than rim materials (Iron, Titanium). So the *same-size* hull is dramatically tankier near the
core than at the rim — coreward ships are tougher twice over, from both size and material.

### Turret count

The number of weapon slots scales straight-line inward, from **2 turrets at the far edge to 25 at the
core**. Hostile and military craft get **×1.5** on top, and a craft's role stacks further multipliers:

| Craft type | Size basis | Turrets | Notes |
|:--|:--|:--|:--|
| **Civilian ship** | sector × roll | none | bare hull; crew + shields filled in |
| **Military** | sector × roll | full armed count | tagged as armed |
| **Trader / Freighter** | sector × roll | 50% chance of the armed count | civilian otherwise |
| **Miner** | sector × roll | full count, **unarmed** | mining lasers |
| **Defender** (home defence) | home sector × **7.5** | **2× + 3** | **×4 damage**; +50% turrets per careful trait |
| **Carrier** | sector × roll | full armed count | + 3 fighter squads |

**Defenders are the spike:** a 7.5× size hull, double-plus-three turrets, and a flat ×4 damage multiplier
make them far beefier than the patrols around them — the game's answer to a player attacking a faction's
home sector.

### Gear quality (tech level)

Salvage and drops are gated by a sector **tech level** that runs opposite to distance — from **1 at the
rim up to 52 at the core** — alongside a **richness** factor that makes core sectors yield far more
resources and credits. Together these are why coreward ships are bigger, tougher, more heavily armed
*and* drop better loot.

## What's in a sector

The galaxy also decides *where* things go and how busy a sector feels. Core sectors are physically roomier,
and stations always keep a buffer around each other so they never spawn overlapping.

Asteroid-field density depends on the field type, each multiplied by a random size factor:

| Field type | Base asteroid count | Spread |
|:--|--:|:--|
| Small field | 50 | ×0.5–1.5 |
| Normal field | 350 | ×0.75–1.25 |
| Dense field | 600 | ×0.75–1.25 |

Sectors also seed container fields, wreckage, gates and wormholes. Wreckage carries tunable chances —
**20%** to contain [goods](Goods), a settings-scaled chance to be left unstripped, and **20%** to hold a
captain's log; stash and history-book spawns roll **20%**. A sector's chance to host a **wormhole is about
1 in 60**, and gate/wormhole endpoints are checked against the [passage map](Maps-and-charts) so they never
illegally cross the barrier ring. Finally, the passing-ships, traders and faction-war background activity
that keep a populated sector feeling alive are attached.

## See also

- [System upgrades](System-upgrades) – the subsystem modules generated craft and players slot in
- [Building knowledge](Building-knowledge) – materials, block durability and size that feed these curves
- [Combat](Combat) – how the generated HP, turret and tech scaling translate into difficulty
- [Weapons](Weapons) – the armed and unarmed turrets bolted onto craft
- [Goods](Goods) – the cargo and richness rewards that scale with distance from the core

---
*Progression & Systems: [Ship generation](Ship-generation) · [System upgrades](System-upgrades) · [Building knowledge](Building-knowledge)*
