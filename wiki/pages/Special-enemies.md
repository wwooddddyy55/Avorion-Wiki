<!-- Hand-written page. Sourced from data/scripts/entity/enemies/blinker.lua, summoner.lua,
     lootgoon.lua and worldboss.lua; data/scripts/lib/waveutility.lua, spawnutility.lua and
     worldbossutility.lua; and data/scripts/sector/background/spawnpersecutors.lua and spawnbehemoth.lua.
     Numbers are taken from those scripts; distances/volumes are in engine units. -->
# Special enemies

Beyond ordinary pirates and Xsotan, Avorion seeds a handful of **special enemy types** with unique
gimmicks, and it scales every hostile encounter with a **wave system** and a set of **toughness buffs**.
This page covers those special enemies, how enemy waves are sized as you head toward the core, the
background spawners behind persecutors and the Behemoth event, and the shared rules that define a
"world boss". For the plain behaviour states all NPCs share see [Enemy AI](Enemy-AI); for the unique
named bosses see [World bosses](World-bosses).

## Special enemy types

| Enemy | Gimmick |
|---|---|
| **Blinker** (Quantum Xsotan) | **Teleports when hit.** Each blink jumps it 2–5× its own radius away, on a cooldown of ~3–5 seconds, after a short charge (a building orange glow warns you). If you're more than ~15 km off it blinks *toward* you, otherwise in a random direction. Occasionally it **cascades** — a burst of 3–4 rapid blinks ~0.4 s apart — making it briefly very hard to pin down. |
| **Summoner** (Xsotan Summoner) | **Spawns minions.** While attacking it conjures a new Xsotan Minion through a wormhole every **2–3 seconds**, up to **6 + difficulty** minions alive per summoner (so 6 on Normal, more on harder settings), capped at **25** minions across the whole sector. Kill the summoner first — the adds stop the moment it dies. |
| **Loot Goon** | **A flying treasure chest that runs.** It carries a hoard — roughly **15–18 turrets** and **9–12 subsystems** (a mix of low rarities plus a guaranteed high-rarity piece up to Legendary), and drops **~10,000 credits** (scaled by region) when killed. The catch: the instant you damage it, it **flees in a straight line and hyperspace-jumps away after ~60 seconds**. Intercept and burn it down fast or the loot escapes. |

> The Loot Goon broadcasts a countdown as it runs ("…we'll be safe in 60 seconds!" → "…almost there!").
> Treat that chat as your damage timer.

## How enemy waves scale

Pirate and Xsotan attacks arrive in **waves**, and both the number of waves and their strength are set
by your **distance to the galactic core** — the central rule behind Avorion's difficulty curve.

| Distance from core | Waves per attack | Ships per wave |
|---|:--:|:--:|
| Far rim (outer galaxy) | 2 | 2 |
| Mid galaxy | 3 | 3 |
| Near the core | 4 | 4 |

On top of *more* and *bigger* waves, the enemies themselves climb through ranks as you go in — from
**Outlaw** at the rim up through Bandit, Pirate, Marauder, Disruptor, Raider, Ravager to a **Boss**
ship, with Xsotan variants (long-range, short-range, "dasher") mixed in deeper. Boss waves are bumped
a rank harder than the regular wave that would follow them.

### Toughness, resistances and weaknesses

A portion of every spawned group is rolled up with **buffs** (more likely, and more severe, the closer
to the core and the higher the difficulty):

| Buff | Effect |
|---|---|
| **Tough** | ×1.5 hull and ×1.5 damage |
| **Savage** | ×2.25 hull and ×2 damage |
| **Hardcore** | ×3 hull and ×3 damage |

Some ships also roll a **resistance** to one [damage type](Combat) (taking far less of it) or a
**weakness** (trading extra hull for taking much more of one type). The practical lesson is the same as
in [Combat](Combat): probe a tough target's damage type and switch to whatever it *doesn't* resist.

> Every wave has a small chance (a few percent) to include a **Loot Goon**, with a pity rule that
> guarantees one if a long run of waves has produced none — so clearing waves is itself a loot source.
> Friendly factions may also send **backup ships** to help you, on a cooldown.

## Persecutor & Behemoth spawners

Two background scripts spawn special threats into a sector directly:

- **Persecutor spawner** — sends the hunters described on [Enemy AI](Enemy-AI#persecutors). Each attack
  is a pack of **2 Persecutors + 2 Disruptors** dropped in ~2 km out, on roughly a 5-minute cadence
  that's slowed at lower difficulties, with a long (~35-minute) cooldown before it will hit an
  *undefended* (player-owned but un-crewed-by-a-player) craft again. The lead ship opens with a dialog,
  and the targeted faction gets a chat warning naming the sector under attack.
- **Behemoth spawner** — the catastrophic **Behemoth** world event: one of four directional bosses
  (Behemoth of the North / East / South / West), each a unique hand-built ship guarding a huge cache of
  loot, including a **unique Legendary system upgrade** per variant. It's extremely dangerous, and if it
  spawns in a sector with no players to defend it, it **flattens the place into wreckage** before
  leaving.

## What makes a "world boss"

The unique encounters on [World bosses](World-bosses) are all built from one shared template, so they
share a recognisable rule set:

- **Far bigger and harder** than a normal ship — on the order of **20× the volume**, **double damage
  output**, and **1.5× the turret count**, including dedicated **anti-torpedo (PDC)** and **anti-fighter**
  guns so you can't trivialise them with torpedoes or strike craft.
- The fight **starts when you get within ~1000 units** of the boss (or its minions), or as soon as you
  damage it — at which point a **boss health bar** appears for everyone in the sector.
- On death it drops a generous loot pile — about **6 Rare-or-better items**, alternating between
  **system upgrades** and **turrets** (no common junk), *plus* the boss's signature reward — and leaves
  a **beacon** marking the spot.
- A defeated world boss **respawns after ~60 minutes**, so the good ones are farmable.

## See also

- [Enemy AI](Enemy-AI) – the behaviour states all NPCs run, and the persecutor mechanic in full
- [World bosses](World-bosses) – the catalog of unique named bosses built on the template above
- [Combat](Combat) – damage types, resistances and weaknesses these enemies roll
- [Events](Events) – the roaming bosses and ambushes that drop these enemies into your lap
- [Weapons](Weapons) / [Torpedoes](Torpedoes) – what the loot you pull off them actually does

---
*Enemies & Bosses: [Enemy AI](Enemy-AI) · [Special enemies](Special-enemies) · [World bosses](World-bosses)*
