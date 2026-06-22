<!-- Hand-written page. Sourced from the NPC behaviour scripts under data/scripts/entity/ai/
     (patrol.lua, patrolpeacefully.lua, evade.lua, persecutor.lua, dock.lua, docktostation.lua,
     trade.lua, tradeutility.lua, salvage.lua, harvest.lua, mine.lua, refineores.lua,
     landfighters.lua, passgate.lua, flythroughgate.lua, passsector.lua) and lib/persecutorutility.lua.
     These are the autonomous AI "states" a ship runs; the docking/timeout numbers are in engine units. -->
# Enemy AI

Every NPC ship in **Avorion** — a patrolling guard, a passing freighter, a mining drone, a pirate
hunting you down — runs a small set of autonomous **AI behaviour states**. A ship is in exactly one
state at a time and switches between them as the situation changes (an enemy appears, cargo fills up,
it reaches a gate). The *same* states power the [Ship orders](Ship-orders) and self-running
[Fleet commands](Fleet-commands) you give your own captained ships, so understanding them tells you
both how enemies behave and what your fleet is doing when you're not watching.

> **In short:** NPCs aren't scripted set-pieces — they react. A peaceful patrol turns hostile if its
> faction takes enough damage; workers flee when threatened; **persecutors** will chase you across several
> jumps. Reading a ship's current behaviour tells you whether it's about to fight, flee or ignore you — and
> the same states drive your own captained ships.

This page covers the behaviour states themselves. For the named special enemies (teleporters,
summoners, loot carriers) and how enemy waves are sized, see [Special enemies](Special-enemies); for
the unique boss encounters see [World bosses](World-bosses).

## Combat & patrol states

| State | What the ship does |
|---|---|
| **Patrol** | Aggressive patrol. Flies a loop of random waypoints around the sector centre and **attacks any enemy or non-aligned ship** it detects. NPC guards drop into this the moment a threat appears. |
| **Patrol Peacefully** | Passive patrol. Flies the same kind of loop but **ignores enemies** — until one of its own faction takes real damage (more than ~5% of a ship's hull, or ~1% of a station's), at which point it flips to aggressive Patrol and fights back. |
| **Evade** | Runs away. Picks the waypoint **farthest from hostiles** and flees there, but keeps **firing back passively** while it retreats rather than turning to chase. |
| **Persecutor** | Hunts a specific player or alliance ship and **chases it across sector jumps**. This is the behaviour behind the "persecutor" pirates — see [Persecutors](#persecutors) below. |

> "Non-aligned" matters: a full-aggression Patrol will engage ships that merely aren't allied to its
> faction, not only declared enemies. Flying an unknown ship through a patrolled sector can start a
> fight on its own.

## Work & economy states

NPC haulers and your own captained ships use these to *do a job*. The dock-based ones are multi-stage
(fly to the docking line → get tractored in → wait → undock) and each gives up if it's kept waiting
too long.

| State | What the ship does |
|---|---|
| **Trade** | Flies to a station, docks, waits at the dock (~40 s) to run its buy/sell, then undocks. Skips stations whose docks are disabled or whose minimum population isn't met. |
| **Refine Ores** | Docks at a **refinery**, waits for the refine job to finish, then docks a second time to collect the refined materials. Picks refineries by faction relations. |
| **Mine** | Mines visible asteroids with **mining turrets**. Hands-off mining on your own ships needs a **captain**. |
| **Harvest** | The general gather loop — mines asteroids or salvages wreckage depending on the turrets fitted. Also needs a captain for fully automatic operation. |
| **Salvage** | Strips wreckage with **salvage turrets** (or armed turrets as a fallback). Needs a **salvage licence** from a scrapyard; unlike mining it can run without a captain. |
| **Land Fighters** | Recalls every deployed fighter squad back into the hangar. Runs automatically before a ship jumps through a gate. |
| **Dock / Dock to Station** | The raw docking manoeuvre: fly to the dock's light-line, get pulled in by tractor beams, hold at the dock. Aborts the attempt if the tractor pull can't seat it within ~120 s. |

Across the harvesting states, a ship only bothers with wreckage or asteroids holding at least ~10
units of resources, and it scoops nearby loot (money or resources) within roughly **150 m**, ignoring
piles smaller than ~10 units. When there's nothing left to work it idles and, after several minutes,
reports the sector exhausted.

## Travel states

| State | What the ship does |
|---|---|
| **Pass Gate** | Navigates an NPC through a **gate** into the neighbouring sector. If the gate is destroyed mid-approach it falls back to wandering (Pass Sector). |
| **Fly Through Gate** | The player-fleet version of gate transit. **Lands its fighters first**, then flies through — and **aborts if the ship is too large** to fit through the wormhole. |
| **Pass Sector** | Transient traffic. The ship crosses toward a destination and **auto-despawns** once it arrives or after ~9–10 minutes, so passing convoys don't pile up. (Player/alliance ships are never deleted this way.) |

## Persecutors

**Persecutors** are pirate ships the game sends specifically to *hunt you* — and they are a deliberate
"comeback" / punishment mechanic, not random traffic. The trigger is **mismatch**: the game estimates
how long your ship would survive the sector's threats versus how long you'd take to kill them, and if
your survival time is far below your kill time (you're badly outgunned for where you are), you become
**eligible for persecution**. Build up enough effective DPS, shields and hull for the region and you
stop qualifying.

Where and when they appear is gated:

- **Never in Beginner** difficulty; on **Easy/Normal** only within a limited band of the galaxy (a
  radius out from the core), and the threat scales up the higher the difficulty.
- **Not** in neutral zones, **not** in rift sectors, and **not** if a persecutor is already active in
  your sector.

Once one locks onto you it is persistent but finite. The persecutor **follows you through jumps** —
taunting over chat as it does ("We can track you!" … "Last time we jump") — up to **4 times**, with a
cooldown (~30 s) between jump attempts, before it finally gives up. So fleeing buys time but won't shake
a persecutor forever; out-running the *eligibility* (getting stronger, or reaching a safe zone) is the
real escape.

> Persecutors are close cousins of the **headhunters / bounty hunters** described on [Events](Events).
> The difference: headhunters come from **reputation** (you went to war with a faction or tanked your
> standing), persecutors come from **relative weakness** (you're under-gunned for the sector).

How persecutor ships are actually *spawned* (their composition and cadence) is covered on
[Special enemies](Special-enemies#persecutor--behemoth-spawners).

## See also

- [Special enemies](Special-enemies) – teleporters, summoners, loot carriers, and how enemy waves scale
- [World bosses](World-bosses) – the unique named boss encounters
- [Ship orders](Ship-orders) – the immediate orders you give your own ships (these reuse the states above)
- [Fleet commands](Fleet-commands) – the self-running captain commands (mine, salvage, trade…)
- [Events](Events) – distress calls, ambushes and the reputation-based headhunters
- [Combat](Combat) – damage types and how to win the fights these behaviours start

---
*Enemies & Bosses: [Enemy AI](Enemy-AI) · [Special enemies](Special-enemies) · [World bosses](World-bosses)*
