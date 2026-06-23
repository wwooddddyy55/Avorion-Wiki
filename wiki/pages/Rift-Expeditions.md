<!-- Hand-written mechanics page. Code lineage (kept out of the reader-facing text on purpose):
     dlc/rift/lib/{constraints,extractions,riftbonuses,riftguardian,riftmissionutility,riftobjects,
       secondaryobjectives,subsystemprotection,tradeableresearchdataitem,zach,yavana}.lua and
       dlc/rift/lib/constraints/{maxslotsconstraint,maxmassconstraint,cargospaceconstraint,
       dockingblockconstraint}.lua and dlc/rift/lib/extractions/{ripcordextraction,
       wormholespawnerextraction,wormholegeneratorextraction,inactivegateextraction}.lua.
     dlc/rift/sector/{riftmissiontimelimit,protectionenvironment,riftstartingposition,
       pathxsotanspawner,outofcoverxsotanspawner,xsotanlootgoonriftbonus}.lua and
       dlc/rift/sector/effects/{environmentaleffecttype,environmentaleffect,
       environmentaleffectutility}.lua.
     dlc/rift/items/{xsotancore,researchprobespawner,ripcord,extractionwormholespawner,
       wormholegeneratorspawner}.lua.
     Distinct from the base-game "Rifts" documented in World-and-Sector-Generation.md, which are
     impassable galaxy-generation line segments, not the dungeon content described here. -->
# Rift Expeditions

**Rift Expeditions** are the paid DLC's timed dungeon runs: you teleport your ship away from normal
space into a sealed-off pocket sector crawling with Xsotan, explore it for loot and a rare currency
called Rift Research Data, then leave again before a swarm overwhelms you. This is a completely
different system from the galaxy-generation "Rifts" described in [World and Sector
Generation](World-and-Sector-Generation#rifts-the-galaxys-scar-lines) — those are simply impassable
scars in the map; the expeditions on this page are the actual playable content the DLC adds.

> **In short:** pick a mission off the rift board, accept its entry constraints, then survive inside
> the sealed sector. A 30-minute clock is always running — ignore it and Xsotan waves get sent after
> you. Environmental hazards (4 severity tiers) and a constant **Subspace Distortion** field make the
> ship's loadout matter as much as combat skill. Leave through whichever extraction the mission rolled
> (a portable Ripcord, a wormhole item, a deployable generator, or a defended Ancient Gate), and bring
> back a subsystem reward plus Rift Research Data to spend on more.

## Entering a rift

Each available expedition is shown on a mission board with its own **entry constraints** — fail one
and you can't accept the mission:

| Constraint | What it checks |
|:--|:--|
| Turret socket limit | your ship's number of subsystem sockets must stay at or below the cap |
| Free cargo space | you need a minimum amount of empty cargo hold |
| Docking capacity | at least 3 unobstructed docking points (obstructed docks don't count) |
| Mass limit | total ship mass must stay under a cap, or accept a malus (below) |

The mass limit is the one constraint you can choose to break. The teleporter screen offers a slider to
send **more** mass than the limit allows — "Overcharge" (+100% mass) or "Supercharge" (+200% mass) — at
the cost of a guaranteed stronger Xsotan presence once you arrive. If you teleport overweight without
using the slider's sanctioned overcharge, your ship instead takes a flat **durability penalty**
proportional to how far over the limit you are, applied before you're warned and asked to confirm.

The mass cap itself scales with how close the sector is to the galactic core (tighter near the rim,
far higher near the centre) and is relaxed by up to 50% for shallow, low-depth rifts — early expeditions
are forgiving; deep ones are not.

## Rift depth and threat level

Every expedition has a **rift depth** from 1 (shallow) to 75 (deepest) — this is the single biggest
driver of difficulty, controlling hazard intensity, Xsotan strength, which extraction methods are
available, and how good the reward can be.

Depth alone isn't the whole story: a mission's displayed **threat level** also factors in how much mass
allowance you gave up, whether the rolled extraction method is a riskier one, whether an environmental
hazard got bumped up a severity tier, and a mission-specific difficulty nudge. Taking on a harder version
of a rift (less mass leeway, a tougher extraction, a worse hazard roll) raises the threat level — and,
importantly, raises the *cap* on how good a reward you're allowed to win.

| Threat level |
|:--|
| Very Low |
| Low |
| Moderate |
| Challenging |
| Very Challenging |
| High |
| Very High |
| Extraordinary |
| Extreme |
| Death Sentence |
| Impossible |

## Environmental hazards

Rift sectors roll a handful of simultaneous environmental hazards from a pool of 17, grouped into four
severity tiers shown as colour-coded icons in the mission board. Shallower rifts draw mostly from the
mild tiers; deeper rifts increasingly draw from the dangerous ones, and any single hazard has a 50%
chance of being bumped up one whole tier on top of its scheduled severity — so even an otherwise tame
rift can hide one unpleasant surprise.

| Tier | Hazard | Effect |
|:--|:--|:--|
| Blue (mild) | Inertia Field | Cuts engine acceleration up to 45%; Xsotan are unaffected by it |
| Blue | Low Energy Plasma Field | Reduces energy-weapon damage in the sector |
| Blue | High Energy Plasma Field | Amplifies energy-weapon damage in the sector |
| Blue | Gravity Anomalies | Floating anomalies that pull ships in, then fling them back out |
| Green | Magnetic Interference Field | Impairs power generation — keep a healthy energy surplus over what you actually use |
| Green | Radiation | Crew workforce drops while shields are down; keep shields up or carry spare crew |
| Green | Acid Fog | Corrodes any exposed block below a material threshold; shields don't help |
| Green | Ion Interference | Shields cannot regenerate at all — enter with them already full |
| Orange | Lightning Field | Shields and hull take periodic lightning-strike damage |
| Orange | Shockwave Anomalies | Unstable anomalies that can discharge a shockwave if approached |
| Orange | Ion Storm | Shields slowly discharge over time |
| Orange | Radiating Asteroids | Same crew-workforce malus as Radiation, tied to glowing asteroids instead |
| Red (severe) | Xsotan Swarm | Warns of an especially large incoming Xsotan horde |
| Red | Xsotan Breeders | Dormant breeders nearby that wake up if disturbed by too much activity |
| Red | Minefield | Live mines — they won't trigger if you approach very slowly |

Two hazard pairs can never appear together in the same rift: Low Energy Plasma Field with High Energy
Plasma Field, and Radiation with Radiating Asteroids.

On top of whatever tier hazards get rolled, every rift sector always carries one more constant field —
**Subspace Distortion** — that scales directly with rift depth and damages your ship unless you've
installed enough **Subspace Distortion Protection**. The deeper the rift, the more protection you need
carried across your subsystems to stay safe; falling more than a handful of points short triggers an
explicit in-flight warning. Two more invisible, UI-hidden effects also scale with depth behind the
scenes — Xsotan deal more damage and have tougher hulls the deeper you go, on top of whatever hazards
you can actually see.

## Racing the clock

A rift mission runs on a **30-minute countdown**. The Rift Research Center radios in warnings as it
ticks down — at 20, 10, 7, 5, 2.5, 1, 0.5 and 0.1 minutes remaining — with the last two thresholds
each spawning an Xsotan wave of their own (2 ships, then 4) directly on top of your group. Once the
clock hits zero, a fresh wave spawns every 60 seconds for as long as the sector holds fewer than 20
Xsotan, each one stronger than the last. Stay roughly 15 minutes past the deadline and the mission
unlocks an "overstay" state. Every wave can include rare elite Xsotan variants, and none of these
forced spawns drop loot or research data — they're pure pressure, not opportunity.

A second, independent system punishes wandering away from the marked path between a sector's landmarks:
stray into open space for too long and the Rift Research Center warns you once, then starts a hidden
timer (faster the farther out you are) before dropping 1–3 Xsotan in behind you, cutting off retreat.
Staying within range of a landmark, buoy, or the path between them keeps this timer from ever starting.

## Leaving the rift

A mission grants exactly one of four ways to leave, gated by the rift's depth — shallow rifts favour
the simplest option, the deepest rifts favour the most dangerous one:

| Extraction | How it works | Best at depth |
|:--|:--|:--|
| Rift Ripcord | A reusable item bound to your home coordinates; activate it for an instant trip home | Shallow (fades out by ~35) |
| Wormhole Device | One-time item; punches an instant one-way wormhole near a sector landmark | Mid (peaks ~37–60) |
| Wormhole Generator | Deployable, indestructible device — drop it, wait for it to finish generating, then fly through | Mid-deep (peaks ~65) |
| Ancient Gate | Find an activator, plug in a battery, defend it while it charges, then fly through | Deep (dominant past ~45–75) |

The Ancient Gate is the only extraction that forces a real fight on your way out — and it's also the
only one that re-imposes the docking-capacity constraint, since you need to dock to wire in the battery.
If you lose a Ripcord, the Rift Research Center automatically issues you a replacement.

## Rewards and Rift Research Data

Clearing a rift offers a **choice between two subsystem rewards** (sometimes with a bonus turret
thrown onto the richer side), with rarity climbing from Rare at shallow depths all the way to a choice
between **two Legendary subsystems each** at depth 75 — the best non-boss reward in the game. The
reward you're offered is capped by the mission's threat level, so the rarity ceiling is earned by taking
on real risk (mass overcharge, a tougher extraction, a nastier hazard roll), not just by diving to a
high nominal depth with an easy loadout. These rewards are drawn from a pool of rift-exclusive **hybrid
subsystems** that combine two normal subsystem effects into a single slot — interceptor, overshield,
combat/mining/salvaging carrier hybrids, and similar combination upgrades not found outside rifts.

Defeated Xsotan also have a chance to drop **Rift Research Data**, a tradeable good rather than
credits. A leveled Scientist captain aboard roughly triples how much you collect per kill. Spend it at
the Rift Research Center to buy back subsystems and turrets you didn't personally loot — prices climb
steeply with rarity, from a handful of data for common gear up into the hundreds for Legendary pieces,
with plain Subspace Distortion Protection modules sold at a steep discount versus everything else.

## Secondary objectives

Most rifts also offer an optional side-objective worth extra Rift Research Data and/or faction
relations, on top of the main extraction goal:

| Objective | Goal |
|:--|:--|
| Strange Metal Formations | Scan several scattered metal formations |
| Rift Crystals | Mine a large quantity of Rift Crystal from glowing crystal asteroids |
| Ancient Artifacts | Loot a set of collectible relics out of old wreckage |
| Xsotan Samples | Destroy or loot several heavily defended Xsotan breeding sites |

A handful of further secondary objectives are tied directly to the Rift storyline missions (rescue,
combat, scouting, salvage and mining tasks) rather than appearing in generic expeditions.

## Sector-wide bonuses

Tougher rifts have an increasing chance — from roughly 1-in-40 at low threat up to a coin-flip at high
threat — of rolling one extra sector-wide bonus, flagged on the mission board:

- **Miner's Heaven** – noticeably richer asteroids throughout the sector
- **Salvage-O-Rama** – extra large wreckages scattered around
- **Aggregator Aggregation** – periodic extra Xsotan "loot goons" spawn over time
- **Weapon Chamber** – a guarded vault hidden in the sector, unlocked via three scattered switches that each need a battery wired in
- **Information Rich Space** – many extra scannable treasure objects

## Notable encounters

Two unusual, invincible ships can be found drifting inside rift sectors and never attack you: **Zach**,
tied to a faction called Von Überstein, and **Yavana**, tied to a faction called the Lone Hunter. Both
read as story-relevant figures rather than threats — they simply won't fight you.

The **Xsotan Rift Guardian** is a different matter: a unique, heavily armed boss ship guarding the
one-way wormhole out of its sector, ringed by five themed outposts (plain, resource-rich, crystalline,
metallic, and a mixed field) each manned by armed Xsotan defenders. Bringing it down guarantees a
Legendary turret and a top-tier hybrid subsystem on top of an already generous loot table spanning Rare
to Legendary gear.

## See also

- [World and Sector Generation](World-and-Sector-Generation) – the unrelated galaxy-generation "Rifts" (impassable line segments), and how normal sectors are built
- [Special enemies](Special-enemies) – the elite Xsotan variants (Quantum, Carrier, Shielded, Buffer, Summoner) that can show up in rift waves
- [World bosses](World-bosses) – named boss encounters outside the Rift DLC
- [System upgrades](System-upgrades) – how ordinary subsystem upgrades work, for comparison with rift-exclusive hybrids
- [Captains](Captains) – the Scientist captain class that multiplies Rift Research Data drops
- [Goods](Goods) – the wider trading-good catalog Rift Research Data and Rift Crystals belong to

---
*Enemies & Bosses: [Enemy AI](Enemy-AI) · [Special enemies](Special-enemies) · [World bosses](World-bosses) · Rift Expeditions*
