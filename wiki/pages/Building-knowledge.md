<!-- Hand-written page. Sourced from items/buildingknowledge.lua (tiers, names, prices, sockets,
     activation rules) and lib/buildingknowledgeutility.lua (regional material by distance, the
     Titanium/Naonite mails, the building-knowledge mission trigger). Material distances are the
     galaxy-radius thresholds in getLocalKnowledgeMaterial; reputation/acquisition routes are the
     bullet points in player/missions/tutorials/buildingknowledgemission.lua. -->
# Building knowledge

**Building knowledge** is how Avorion gates ship construction by material. You can only build with a
material once you've **unlocked** it, and each unlock comes as a **Building Knowledge** item you
activate from your inventory. Unlocking a material also **raises the maximum size** of ship you can
build (it grants more processing-power sockets). This page covers the tiers, what they cost, and how
to get them.

## What an unlock does

Activating a Building Knowledge item does two things for the player it's bound to:

1. **Unlocks building with that material** (and everything below it), so you can place those blocks in
   the build mode.
2. **Increases your buildable ship size** by raising your **subsystem socket** cap — bigger material =
   more sockets = larger ships. (This second effect only matters if the server isn't running with
   *unlimited processing power*.)

Building Knowledge items are **bound to you**, **can't be sold or dropped**, and are **consumed on
use** ("Depleted on Use").

## The tiers

There are seven tiers, one per buildable material from Iron up to Avorion. Higher tiers cost
dramatically more and unlock larger ships:

| Tier | Material | Price (buy) | Subsystem sockets |
|:--:|---|--:|:--:|
| I | Iron | 50,000 | 4 |
| II | Titanium | 250,000 | 5 |
| III | Naonite | 750,000 | 6 |
| IV | Trinium | 1,500,000 | 8 |
| V | Xanion | 3,000,000 | 10 |
| VI | Ogonite | 5,000,000 | 12 |
| VII | Avorion | 10,000,000 | 15 |

*(Selling/teardown value of the item is about 25% of the buy price.)* The socket counts are why
deeper materials let you fly bigger ships, not just sturdier ones.

### You can't skip a tier

Activation checks your progression: if a knowledge item is **two or more tiers** above the highest
material you can already build, it refuses to activate and tells you it *"Requires building knowledge
about [previous material]."* In practice you must unlock materials roughly in order — you can be one
step ahead, but you can't jump from Titanium straight to Xanion.

## Where the knowledge lives — it's regional

Which material a sector's building knowledge is *about* depends on how far that sector is from the
galactic **centre**. Closer to the core = higher material. The thresholds (by distance from the centre,
in sectors) are:

| Region (distance from centre) | Material |
|---|---|
| < 75 | Avorion |
| 75 – 145 | Ogonite |
| 145 – 210 | Xanion |
| 210 – 290 | Trinium |
| 290 – 360 | Naonite |
| 360 – 420 | Titanium |
| > 420 (the rim) | Iron |

So to unlock, say, **Trinium**, you go to the Trinium band of the galaxy and get it there — you won't
find Trinium knowledge out at the rim.

## How to get each material

**Iron** is free — you can build with it from the start. After that:

- **Titanium** is handed to you. Once you've mined some Titanium, **the Adventurer** mails you a free
  Titanium Building Knowledge item as a gift. (You later get a follow-up mail pointing you toward
  Naonite — and noting Naonite is what lets you build **shield generators**.)
- **Naonite and beyond** you have to earn or buy. When you reach a region whose material you haven't
  unlocked (Naonite or higher), the game gives you a **Building Knowledge mission** that lists your
  options:
  - **Fly toward the centre** to reach the material's region (or further out for a lower tier).
  - **Clear a pirate sector** in that region (the knowledge can drop as a reward).
  - **Buy it at a Shipyard** — requires **65,000 reputation** with that faction.
  - **Buy it for ores at a Resource Depot.**
  - **Buy it at a Smuggler's Market** for a *"ridiculously high price"* — the no-reputation shortcut.
  - Then **activate it from your inventory.**

> The mission only appears for materials you can't yet build and that are appropriate to the region —
> there's no mission for Iron or Titanium (you already have those routes), and none for a material
> you've already unlocked.

## See also

- [Refining](Refining) – turning the ore you mine into these materials
- [Production](Production) – material costs of founding and upgrading stations and ships
- [Missions](Missions) – including the Building Knowledge tutorial mission
- [Combat](Combat) – higher materials mean better hull, and Naonite unlocks shields

---
*Player Progression & Missions: [Missions](Missions) · [Story missions](Story-missions) · [Events](Events) · [Building knowledge](Building-knowledge) · [Ship orders](Ship-orders) · [Encyclopedia](Encyclopedia)*
