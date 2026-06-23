<!-- Hand-written mechanics page. Sourced from data/scripts/lib/galaxy.lua (Balancing_GetDimensions,
     blockRingMin=147/blockRingMax=150, Balancing_GetPirateLevel), data/scripts/sectorspecifics.lua
     (addBaseTemplates, determineFastContent, determineContent, initialize/selectByWeight,
     generatePlanets/generatePlanet/generateMoon/generateBlackHole, getRegularStationSectors),
     data/scripts/sector/init.lua (xsotanswarm/riftbackgroundthunder auto-attach), data/scripts/server/generatesector.lua,
     data/scripts/galaxy/init.lua, data/scripts/galaxy/server.lua (Xsotan Swarm + Wormhole Guardian timers),
     data/scripts/galaxy/behemothevent.lua + sector/background/spawnbehemoth.lua (the Behemoth world event),
     data/scripts/lib/passagemap.lua (the Rift line-segment system, PassageMap:passable/insideRing),
     data/scripts/lib/gatesmap.lua + lib/ancientgatesmap.lua (gate-network connection rules),
     data/scripts/lib/sectornamegenerator.lua (per-grid-cell name pool, easter-egg prefixes),
     data/scripts/sector/background/sectorcontentsupdater.lua (controlling-faction relation penalty),
     data/scripts/sector/background/rebuildstations.lua + respawndefenders.lua (background station/defender respawn),
     and every file in data/scripts/sectors/ (34 sector-type templates: colony, asteroidfieldminer,
     loneconsumer, lonescrapyard, loneshipyard, lonetrader, lonetradingpost, lonewormhole, factoryfield,
     miningfield, gates, ancientgates, neutralzone, riftinvasionbase, pirateasteroidfield, piratefight,
     piratestation, asteroidfield, containerfield, massivecontainerfield, smallasteroidfield,
     defenderasteroidfield, wreckagefield, stationwreckage, smugglerhideout, cultists, wreckageasteroidfield,
     researchsatellite, functionalwreckage, asteroidshieldboss, xsotanasteroids, xsotantransformed,
     xsotanbreeders, resistancecell, teleporter, worldboss — each exposing getProbabilityWeight/offgrid/
     gates/contents/generate). Numbers not covered here (ship/station size & HP scaling, asteroid-field
     density, wreckage-content odds, wormhole-spawn odds, gate-vs-passage-map checks) are already documented
     in Ship-generation.md and intentionally not repeated. Image assets: see wiki/ASSETS.md. -->
# World and Sector Generation

The galaxy in Avorion isn't drawn ahead of time — every sector is decided **the moment something first
asks about it**, by hashing the sector's coordinates together with the galaxy's seed. Nothing is stored
until then. That's why two players in the same galaxy who fly to a sector neither has visited yet will
always find exactly the same thing there, but a galaxy made with a different seed is a different universe.

> **In short:** the galaxy is a **1000×1000 grid of coordinates** centred on the galactic core. Every
> coordinate is hashed once to decide whether it's empty, lightly populated ("off-grid"), or a fully
> built-out sector — and, if populated, which of **34 sector types** it becomes. A ring **~147–150 sectors**
> from the core (**the Barrier**) gates the late game, and ~200 randomly scattered **Rifts** — impassable
> scar-lines through space — block gates and wormholes from crossing them, forcing detours. Background
> systems quietly keep the galaxy alive: factions rebuild lost stations, lost home defenders respawn, and
> a galaxy-wide **Behemoth** event roams between quadrants hunting for an empty AI sector to wreck.

## The shape of the galaxy

The galaxy is a square grid running from roughly **−500 to +500** on each axis, so the farthest corner is
about **707 sectors** from the centre at (0,0) — which is always a black hole (see
[Planets and moons](#planets-and-moons) below). Two distances matter everywhere in generation:

- **The Barrier** — a ring **~147 to ~150 sectors** out. It's the wall between the "early game" galaxy and
  the deep-core endgame: it gates several sector types below, decides where the [Xsotan Swarm](#the-xsotan-swarm)
  event can trigger, and (if the barrier setting is enabled) blocks gates and wormholes from crossing it at all.
- **The centre and the home ring** are deliberately kept clear: sectors within **20** of the core, and a
  donut between roughly **440 and 460** sectors out (around where new players' home sectors land), are
  never blocked by anything — guaranteeing the core and fresh starts are always reachable.

## Rifts: the galaxy's scar lines

*[📷 Screenshot needed — ASSETS.md: images/galaxy-rift-passage-map.png]*

Scattered across the galaxy are roughly **200 Rifts** (configurable in the galaxy settings) — short,
randomly placed line segments, each a few sectors long and a few sectors wide, generated once when the
galaxy is created and never moved again. A sector that falls on top of a Rift line is **impassable**: no
gate or wormhole can connect through it, and ambient thunder plays in sectors flagged as being inside one.
This is what actually produces the dead zones and detours on your Galaxy Map — not the Barrier itself,
which is a separate, fixed ring.

Rifts can make a sector **completely impassable and contentless** even outside the Barrier, which is why
sector-content generation (next section) always checks the Rift map first. One specific sector type, the
**Rift Research Center** (below), only appears directly next to a Rift-blocked sector — it's the one
"front line" outpost that studies them.

> Don't confuse these galaxy-generation scar lines with **[Rift Expeditions](Rift-Expeditions)**, the paid
> DLC's separate timed dungeon-run content. The Rift Research Center sector above is the lore tie between
> the two, but the actual expedition missions are a different system entirely.

## How a sector decides what it contains

The first time anything needs to know what's in sector (x, y), the game hashes the coordinates and the
galaxy seed and works through a fixed decision order:

1. **Is it a faction's exact home coordinate?** If so, content is forced to **Home** — guaranteed full
   colony generation, no roll needed.
2. **Is the sector blocked by a Rift or the Barrier?** If so, it's **Empty** — no content at all, regardless
   of anything else.
3. **Roll for Regular content** — roughly a **3% chance**. Regular sectors get the full weighted sector-type
   roll below.
4. **If not Regular, roll for Off-grid content** — roughly a **6% chance**. Off-grid sectors get a lighter
   roll from a separate pool of sector types (the ones marked off-grid in the catalog below).
5. **Ownership check** — a sector with **no faction at all** claiming it can never be "Regular"; an
   unclaimed Regular roll is demoted down to Off-grid.
6. **Faction-core bonus** — an Off-grid sector that falls inside a faction's **central/core territory**
   (as opposed to its outer fringe) has a **75% chance** of being promoted back up to full Regular content.
7. **Everything else is Empty** — most of the galaxy, even inside friendly territory, is empty space.

A separate, independent roll picks the sector's **"dustyness"** (0–3, how thick the background nebula
looks) — weighted heavily toward 0 (roughly 62% / 23% / 12% / 4% across the four tiers).

## The sector-type catalog

Once a sector is Regular or Off-grid, every eligible sector-type **template** reports a probability
**weight** for that exact spot — split by whether the sector is inside a faction's core territory, in its
outer fringe, or unclaimed — and one is picked at random, proportional to those weights. A handful of
templates are faction-independent (Ancient Gates, Lone Wormhole, World Boss, Asteroid Shield Boss) and a
few only "unlock" past or before the Barrier. The table below groups the 34 templates by feel; weights are
*(core territory / outer fringe / unclaimed space)* — **0 means that template can never appear there**.

### Faction economy (claimed territory only)

| Sector type | Weight | Gates? | What's there |
|---|---|:--:|---|
| **Home colony** | 450 / 150 / 0 | Always | A faction's actual home sector: shipyard, resource depot, repair dock, equipment dock, 3 guaranteed factories, 50% chance each of a trading post and a neighbour-shared trading post, 33% chance each of a turret factory (+50% a supplier alongside it) and a fighter factory, one military outpost, one unarmed consumer ship, and — only here — the faction **Headquarters**. |
| **Factory field** | 1400 / 800 / 0 | Always | The single most common deep-territory sector: 5–6 factories plus a mix of trading post / turret factory+supplier / fighter factory / resource depot, each at 33–50%. |
| **Mining field** | 300 / 500 / 0 | Always | 6 fixed mines, 75% a resource depot, ~33% a trading post (which can itself roll as a neighbour-shared one). |
| **Neutral zone** | 500 / 400 / 0 | Always | Resource trader, trading post, repair dock, and a chance of a travel hub — plus it samples up to 10 *nearby* coordinates to pull in trading posts from neighbouring factions, making it a small multi-faction hub. Player-vs-player damage is disabled here. |
| **Gate junction** | 400 / 550 / 0 | Always | Nothing but a gate hub — pure network infrastructure. |
| **Lone consumer / scrapyard / shipyard / trader / trading post** | ~200 / ~400 / 0 each | ~33% chance | Small single-purpose stops (one consumer ship, a scrapyard with 200–250 wrecks, a shipyard, a resource trader + trading post, or a trading post that can become "planetary" if the sector rolled a planet). Each has a small (5–15%) bonus chance of an extra travel hub, fringe-territory only. |
| **Resistance cell** | 750 / 200 / 10 | No | A rebel outpost hiding *inside* hostile territory — a resistance outpost, a shipyard, one random secondary station (equipment dock, factory, turret factory, repair dock, resource trader, trading post, casino, research station, biotope, or military outpost), and 4–9 defenders. Only rolls in a band between 30 sectors out and the Barrier's inner edge. |
| **Smuggler hideout** | 350 / 250 / 0 | No | Spawns and owns its **own tiny one-sector faction** (a procedurally named "Syndicate"), with a Smuggler's Market, a shipyard, and 3–4 defenders that ignore anti-smuggling checks. An honourable nearby faction may schedule an attack on it ~2 hours after you find it. |

### Resources, wreckage and salvage

| Sector type | What's there |
|---|---|
| **Asteroid field / Small asteroid field** | Mixed filled and empty fields, occasional pirate ambush (35%), optional claimable asteroid. |
| **Asteroid field miner** | An asteroid field with 1–2 mining ships actively working it. |
| **Container field / Massive container field** | Drifting cargo containers (one container always carries a hidden stash script); the massive version adds ~10 fields at once. Both quietly respawn over time. |
| **Wreckage field** | ~30 wrecked hulls and a 75% pirate-ambush chance; wrecks in the band just past the Barrier (out to 180 sectors) have a small (5%) chance of carrying a hidden story clue. |
| **Wreckage asteroid field** | Asteroids plus one large abandoned-ship wreck with a beacon and a guaranteed "Traveler's Stash" nearby. |
| **Functional wreckage** | The same idea, but the hulk can be reactivated rather than just salvaged. |
| **Station wreckage** | A single station of a random type, generated and then immediately destroyed into wreckage — the burned-out husk is all that's left. |
| **Defender asteroid field** | An ordinary asteroid field that still gets a small home-faction defense squad, even out in the wild. |

### Pirates

| Sector type | What's there |
|---|---|
| **Pirate asteroid field** | A pirate-run mining claim with a rotating pool of wave-encounter scripts. |
| **Pirate fight** | Two pirate warbands fighting each other (both shrink the farther out from the core they are) — you can wade in and pick a side, or just loot the wreckage. |
| **Pirate station** | A pirate shipyard hideout — only within 410 sectors of the core — guarded by patrol and defender ships that scale with distance. |

### The Xsotan

| Sector type | Weight | What's there |
|---|---|---|
| **Xsotan asteroids** | 750 / 500 / 0 | An infected asteroid field with 10–15 roaming Xsotan ships. Only inside the Barrier. |
| **Xsotan transformed** | 2500 / 1500 / 50 | Picks a **random ordinary sector template**, generates it normally, then destroys and re-skins everything in it and repopulates it with Xsotan — a "corrupted" version of a normal sector. The highest-weighted Xsotan template by far. |
| **Xsotan breeders** | 750 / 500 / 0 | A deliberately hand-laid grid of small infected asteroids (three dense blocks) plus a few large infected asteroids — a Xsotan nest. |

> **Cultists** are a related but separate template: a single procedurally-named cult (e.g. "The *Something*
> Cult") guards a giant asteroid wrapped in 2–3 rings of small rocks. The cult's leader carries a random
> religious-leader title (Priest, Bishop, Ayatollah, Druid…) and noticeably better loot than its followers.

### One-of-a-kind sectors

| Sector type | Weight | What's there |
|---|---|---|
| **Lone wormhole** | 150 / 150 / **150** | A guaranteed wormhole and nothing else — the only "civilian" template that spawns at full strength even in totally unclaimed space. |
| **Ancient gates** | flat **5**, everywhere | A separate, much rarer long-range gate network (see [Gates](#gates-ancient-gates-and-the-rim-teleporters) below). |
| **Rift Research Center** | 2500 / 1500 / 0, but **0 unless next to a Rift** | A Rift Research Center plus a shipyard, repair dock and equipment dock — the only template gated by the Rift map rather than faction territory. |
| **Research satellite** | flat 300 in a ring | A lone science probe; only between 150 and 240 sectors from the core. |
| **Teleporter** | effectively forced when eligible | Found in a thin band (~1.2 sectors wide) just *outside* the Barrier's outer edge, on a 1-in-4 coordinate roll — see below. |
| **World boss** | flat **5**, everywhere | Spawns one of the ten named [World bosses](World-bosses) at random. |
| **Asteroid shield boss** | flat 50, unclaimed space only | A deliberately **empty** sector reserved for the asteroid-shield boss fight, which a player-side script spawns directly rather than the galaxy filling it in. |

## Planets and moons

The very centre of the galaxy, (0,0), is always a **black hole**. Every other sector has a flat **60%
chance** of generating exactly one planet, picked from seven types, each with its own size range —
Terrestrial, Rocky, Gas Giant, Smooth and Volcanic worlds, plus standalone Moons — and independent rolls
for atmosphere, cloud cover, habitation lights and rings. A planet can additionally gain **one moon or one
asteroid ring**, never both.

## Gates, Ancient Gates, and the rim teleporters

A sector's regular **gate network** connects to its nearest gate-bearing neighbours in up to four
directions, chosen from one of 24 fixed direction-orderings (picked by hashing the coordinates), within a
**45-sector range**. A link only becomes real if it's **mutual** — sector A reaching for B isn't enough
unless B is also reaching back for A — and a gate link can never cross from inside the Barrier to outside
it.

**Ancient Gates** run on a separate, much sparser network: a flat weight of 5 everywhere (independent of
faction territory) but a **150-sector range**, more than three times a normal gate's reach. A handful of
specific story-tied coordinates ("Exodus corner" points) are **always** guaranteed an Ancient Gate
regardless of the roll.

**Rim teleporters** are a third, much smaller network: in the thin band just past the Barrier's outer edge,
roughly 1-in-4 coordinates effectively always become a Teleporter sector — its weight is so high it
overrides every other roll. These feed the [Story missions](Story-missions) teleporter network rather than
the open gate grid.

## Naming the galaxy

Sector names aren't rolled per sector — they're rolled **per 8×8-sector grid cell**. Every sector inside
the same cell shares one base name (built from a word-pair pool, either "*Prefix Suffix*" or
"*Prefix* of *Suffix*"), and sectors within that cell are told apart with a trailing number, Roman numeral,
or Greek letter. Two specific grid cells on the innermost naming ring are hard-coded to carry a hidden
name-credit prefix instead of the normal roll — a small easter egg baked into the galaxy seed.

## Background systems that keep the galaxy alive

A handful of galaxy-wide and per-sector timers run continuously, independent of whatever sector you're
actually in:

- **The Xsotan Swarm.** Any sector within the Barrier ring is automatically eligible. On a timer, the
  swarm activates for **30 minutes**; success or failure both schedule the next swarm **2 hours** later,
  with a galaxy-wide chat announcement either way.
- **The Wormhole Guardian** has its own galaxy-wide respawn countdown; expiry is announced with a "strong
  subspace disturbances" warning broadcast.
- **The Behemoth.** A single roaming world-boss event, separate from the named [World bosses](World-bosses).
  After **2 hours** of total server runtime, a **1-hour** countdown begins; on expiry the game picks an
  AI-faction sector with stations but **no player presence**, in a band 180–500 sectors out, cycling
  through four compass quadrants (Behemoth of the North / East / South / West) one at a time. Players get a
  **20-minute** window to engage before it moves on; if nobody shows up, it visibly wrecks the sector's
  stations into wreckage before the next 2-hour cycle begins in the next quadrant.
- **Faction takeovers carry a grudge.** If a sector's controlling faction changes from an AI faction to
  someone else, the old owner's relations toward the new controller worsen — **−30,000** if it was their
  core territory, **−10,000** on the fringe — announced to the new owner directly.
- **Stations quietly rebuild.** Every faction-owned sector periodically compares its current stations
  against what it originally generated; after two consecutive checks confirming something is still
  missing, a construction site appears to rebuild it (never inside an active war zone, except in the
  faction's own home sector, and at most once every 30 minutes per faction).
- **Lost home defenders trickle back.** Destroyed Defender ships are checked roughly every 15 minutes and
  respawned to make up the shortfall — but only while the faction still holds at least one station in that
  sector, and never once the faction is eradicated.

## See also

- [Ship generation](Ship-generation) – how the ships and stations *inside* a sector are built and scaled
- [Rift Expeditions](Rift-Expeditions) – the DLC's separate timed dungeon-run content, not to be confused with these scar-line Rifts
- [World bosses](World-bosses) – the ten named encounters the World Boss sector type can roll
- [Events](Events) – the other roaming bosses and distress-call encounters
- [Maps and charts](Maps-and-charts) – how the Galaxy Map reveals faction territory and gate links
- [Diplomacy and Reputation](Diplomacy-and-Reputation) – neutral zones, hazard zones, and faction relations
- [Story missions](Story-missions) – the Barrier, the teleporter network, and what lies at the core

---
*Progression & Systems: [Ship generation](Ship-generation) · [World and Sector Generation](World-and-Sector-Generation) · [Ship stats](Ship-stats) · [System upgrades](System-upgrades) · [Building knowledge](Building-knowledge)*
