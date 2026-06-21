<!-- Hand-written mechanics page. Code lineage:
     lib/shipgenerator.lua (createShip/Defender/Carrier/Military/Trading/Freighter/Mining),
     lib/plangenerator.lua + plangenerator/lib/generator.lua (procedural hull/station assembly, GeneratePlanFromStyle),
     lib/SectorGenerator.lua (positioning, station placement, asteroid fields, wormholes, gates),
     lib/galaxy.lua (Balancing_* curves: ship/station volume, turrets, HP, tech, richness, material).
     Block placement and GeneratePlanFromStyle are engine-side (C++); the numbers here are what the Lua curves compute. -->
# Ship generation

**Ship generation** is how Avorion builds every NPC craft and station you encounter: it takes a faction, a
target *volume*, and a galaxy position, asks a faction-specific **style template** to assemble a block plan,
then scales the result so ships get bigger, tougher and better-armed the closer you get to the galactic core.
Three layers cooperate — `shipgenerator.lua` (what kind of craft), `plangenerator.lua` (the hull plan), and
`SectorGenerator.lua` (where it goes) — all driven by the `Balancing_*` curves in `galaxy.lua`.

The same distance-from-core scaling that drives ships also governs [Combat](Combat) difficulty, drop
[Goods](Goods) value, and the [material](Building-knowledge) you can expect to salvage.

## Procedural assembly

A craft is never stored as a fixed model. `ShipGenerator.createShip` asks `PlanGenerator.makeShipPlan` for a
**block plan**, then calls the engine's `Sector():createShip` with it:

```
volume = Balancing_GetSectorShipVolume(sector) * Balancing_GetShipVolumeDeviation()
plan   = PlanGenerator.makeShipPlan(faction, volume)
ship   = Sector():createShip(faction, "", plan, position)
```

`makeShipPlan` resolves in three steps:

1. **Faction packs first.** `FactionPacks.getShipPlan(faction, volume, material)` is checked — if a faction
   ships hand-authored hulls (or a mod injects them), that plan is used verbatim and procedural generation is
   skipped.
2. **Style lookup / generation.** Otherwise `PlanGenerator.getShipStyle(faction)` returns a cached
   per-faction **style** (built once by `StyleGenerator` from a seed derived from the faction, then stored
   with `faction:addPlanStyle`). The style encodes that faction's silhouette, colors and block-shape grammar.
3. **Plan synthesis.** The engine call
   `GeneratePlanFromStyle(style, Seed(seed), volume, sizeCap, edgeFlag, material)` grows an actual block tree
   from the style until it reaches the requested `volume`. The size/complexity cap differs by craft role:

| Craft role | Generator call | Size cap |
|:--:|:--|--:|
| Warship hull | `makeShipPlan` | 6,000 |
| Freighter / Carrier / Miner | `makeFreighterPlan` etc. | 5,000 |
| Station | `makeStationPlan` | 10,000 |
| Fighter | `makeFighterPlan` | 200 |

The helper library `plangenerator/lib/generator.lua` supplies the block-grammar primitives the styles call —
`sphere`, `ring`, `rounded`, `stationDisc`, `smallHollowRing`, and so on — each of which lays down a
symmetric cluster of [hull, edge and corner blocks](Building-knowledge) around a parent block. This is why
generated ships look hand-built but never repeat: the *grammar* is fixed per faction, the *seed* varies per
ship.

**Material** is chosen by `PlanGenerator.selectMaterial`: it samples the sector's technology-material
probability distribution, and downgrades Avorion to Ogonite if the sector lies outside the barrier ring
($d > 147$). Material then sets both the look and the per-block durability multiplier (below).

### Stations

`PlanGenerator.makeStationPlan` is the same pipeline at a larger scale (size cap 10,000, volume from
`Balancing_GetSectorStationVolume`). `SectorGenerator:createStation` wraps it: it derives the style name from
the station's script (`shipyard.lua` → Shipyard, `factory.lua` + style arg → Factory/Mine/Farm/…), generates
the plan, finds a non-overlapping position, and attaches the station's economy scripts.

A **construction site** (`createStationConstructionSite`) takes a finished station plan and *degrades* it back
into scaffolding: blocks far from the center are converted to Framework on a 1-in-5 cadence, interior blocks
1-in-14, and Framework strut blocks are added around 1-in-3 blocks — producing the half-built look that
finishes into the real station over time.

## Stat allocation — distance from the core is the master dial

Every structural number a generated craft has flows from one input: the sector's straight-line distance from
the galaxy center,

$$d = \sqrt{x^2 + y^2}$$

Let $d_{\max} = \tfrac{1}{2}\,\text{Balancing\_GetDimensions()}$ be the galaxy's half-extent, and define the
clamped linear falloffs used throughout `galaxy.lua`:

$$\ell = 1 - \frac{d}{d_{\max}}, \qquad
\ell_{\text{outer}} = \operatorname{clamp}_{[0,1]}\!\left(1 - \frac{d}{400}\right), \qquad
\ell_{\text{mid}} = \operatorname{clamp}_{[0,1]}\!\left(1 - \frac{d}{350}\right)$$

All three equal **1 at the core** and fall to **0** at the edge (or at 400 / 350 sectors out, respectively).

### Volume (the size of the ship)

`Balancing_GetSectorShipVolume` builds a curve that is nearly flat in the outer galaxy and rises sharply near
the core. With a quartic core term

$$\text{distFactor} = (3\ell + 1)^4 - 1 \qquad (0 \text{ at edge} \rightarrow 255 \text{ at core})$$

the average ship volume in a sector is

$$V_{\text{ship}} = \Bigl[\text{distFactor}\cdot\tfrac{1000}{255}
   \;+\; 1000\,\ell \;+\; 2500\,\ell_{\text{outer}} \;+\; 2500\,\ell_{\text{mid}}\Bigr]
   \cdot \frac{2750}{7000} \;+\; 150$$

| Region | Approx. average ship volume |
|:--:|--:|
| Galactic edge | 150 |
| Mid galaxy (≈ 350–400 out) | ~1,000–1,500 |
| Galactic core | ~2,900 |

Each individual ship then multiplies this average by a **deviation roll** so a sector holds a mix of small and
large hulls. The roll is heavily skewed toward small ships:

$$\text{deviation} = 1 + 10\,f^{4}, \quad f \sim U(0,1) \;\;\Rightarrow\;\; [\,1\times,\ 11\times\,]$$

Stations reuse the ship volume, ×100, capped, with a gentler deviation:

$$V_{\text{station}} = \min\!\bigl(150{,}000,\; V_{\text{ship}} \times 100\bigr), \qquad
\text{deviation}_{\text{station}} = 1 + 2.5\,f^{3} \;\Rightarrow\; [\,1\times,\ 3.5\times\,]$$

### Durability

A craft's hit points are not stored separately — they follow from its volume and the local material strength,
because each block's durability averages $4 \times$ its volume:

$$\text{HP} \approx V_{\text{ship}} \times \text{materialStrength} \times 4$$

`materialStrength` is the probability-weighted average of the strength factors of the materials available in
that sector, so the same volume of ship is tougher near the core (where Ogonite/Avorion dominate) than at the
rim (Iron/Titanium).

### Turret limits (tracking / weapon slots)

The number of weapon slots a generated craft carries scales linearly inward:

$$T_{\text{unrounded}} = \operatorname{lerp}\bigl(d;\ 460 \to 2,\ \ 0 \to 25\bigr), \qquad
T_{\text{enemy}} = \big\lfloor 1.5 \cdot T_{\text{unrounded}} \big\rfloor$$

So a baseline sector ranges from **2 turrets** at the far edge to **25 at the core**, and hostile/military
craft get **×1.5** on top. Role multipliers in `shipgenerator.lua` stack on this base:

| Craft type (`shipgenerator.lua`) | Volume basis | Turrets added | Notes |
|:--:|:--|--:|:--|
| **Ship** (`createShip`) | sector × deviation | 0 | bare hull; crew + shields filled |
| **Military** (`createMilitaryShip`) | sector × deviation | $T_{\text{enemy}}$ armed | tagged `is_armed` |
| **Trading / Freighter** | sector × deviation | 50% chance of $T_{\text{enemy}}$ armed | civilian scripts |
| **Mining** (`createMiningShip`) | sector × deviation | $T_{\text{enemy}}$ **unarmed** | mining lasers |
| **Defender** (`createDefender`) | home sector × **7.5** | $2\,T_{\text{enemy}} + 3$ | ×4 damage; +50% turrets per `careful` trait point |
| **Carrier** (`createCarrier`) | sector × deviation | $T_{\text{enemy}}$ armed | + 3 fighter squads |

Defenders are the spike: a 7.5× volume hull, double-plus-three turrets, and a flat ×4 damage multiplier make
them far beefier than the patrol ships around them — the game's answer to a player attacking a faction's home.

### Tech level (gear quality)

Salvage and drops are gated by a sector **tech level** that runs opposite to distance:

$$\text{tech} = \operatorname{round}\bigl(\operatorname{lerp}(d;\ 0 \to 52,\ 500 \to 1)\bigr) \in [1, 52]$$

and a **richness factor** (cubic in $\ell$, default scale 20; reward factor uses scale 25) that makes core
sectors yield dramatically more resources and credits. Together these are why core-ward ships are bigger,
tougher, more heavily armed, *and* drop better loot.

## Sector coordination

`SectorGenerator.lua` decides *where* generated entities go and how dense a sector is. It is constructed with
the sector's coordinates and exposes placement and population helpers.

### Positioning

Sector physical size scales inward, so core sectors are roomier:

$$\text{maxDist} = \operatorname{lerp}\bigl(d;\ 450 \to 5000,\ \ 380 \to 8000\bigr)$$

`getPositionInSector` scatters entities within that radius. **Stations** use `findStationPositionInSector`,
which keeps a `radius × 1.75` buffer around every existing station and retries (expanding the search by 50 m
each miss) until it finds clear space — preventing stations from spawning inside one another.

### Spawn thresholds and fields

Asteroid-field density is set by per-instance baselines, each multiplied by a random size factor:

| Field type | Base asteroid count | Spread |
|:--:|--:|:--|
| Small field | 50 | ×0.5–1.5 |
| Normal field | 350 | ×0.75–1.25 |
| Dense field | 600 | ×0.75–1.25 |

The generator also seeds container fields, wreckage, gates and wormholes. Wreckage carries tunable chances —
**20%** to contain [goods](Goods), **10% × resource-wreckage setting** to be left unstripped, **20%** to hold
a captain's log. Stash/history-book spawns roll **20%**. A sector's chance to host a wormhole is **1/60**, and
gate/wormhole endpoints are validated against the [passage map](Maps-and-charts) so they never cross the
barrier ring illegally.

`addAmbientEvents` finally attaches the passing-ships, traders and faction-war background scripts that keep a
populated sector alive after generation.

## See also

- [System upgrades](System-upgrades) – the subsystem modules generated craft and players slot in
- [Building knowledge](Building-knowledge) – materials, block durability and volume that feed these curves
- [Combat](Combat) – how the generated HP, turret and tech scaling translate into difficulty
- [Weapons](Weapons) – the armed/unarmed turrets `shipgenerator.lua` bolts onto craft
- [Goods](Goods) – the cargo and richness rewards that scale with distance from the core

---
*Progression & Systems: [Ship generation](Ship-generation) · [System upgrades](System-upgrades) · [Building knowledge](Building-knowledge)*
