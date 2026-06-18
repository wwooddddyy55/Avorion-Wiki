<!-- Hand-written page. Sourced from lib/ordertypes.lua (the OrderType enumeration and the per-order
     names). These are the direct/manual orders you give a ship; the longer captain "commands"
     (procure/sell/explore/expedition etc.) are a separate system that replaced the old BuyGoods/
     SellGoods orders noted as removed in ordertypes.lua. -->
# Ship orders

Once you command more than one ship, you give the others **orders** — from the **strategy map** or the
ship's order menu — telling them what to do while you fly something else. This page lists the order
types the game defines. Orders are the short, immediate commands (jump, mine, attack, escort); the
longer self-running **captain commands** (procure/sell goods, expeditions, scouting) are a separate
captain system.

## Order types

| Order | What the ship does |
|---|---|
| **Jump** | Jump to a target sector. |
| **Fly to Position** | Move to a position within the current sector. |
| **Fly Through** | Fly through a wormhole / gate. |
| **Loop** | Fly a repeating loop (patrol a set path). |
| **Patrol** | Patrol the current sector, engaging threats. |
| **Guard** | Hold and guard a specific position. |
| **Aggressive** | Actively seek out and attack hostiles in the sector. |
| **Attack** | Attack a specific target craft. |
| **Escort** | Follow and protect a specific ship. |
| **Board** | Board an enemy ship to capture it (needs boarding crew). |
| **Mine** | Mine asteroids in the sector. |
| **Salvage** | Salvage wreckage in the sector. |
| **Refine Ores** | Take mined ore to be refined into materials. |
| **Repair Target** | Repair a specific friendly ship. |
| **Repair** | Go and get itself repaired. |
| **Dock** | Dock to a station. |

## Notes

- **Mine**, **Salvage**, **Patrol** and similar autonomous orders are what you assign to ships with a
  **captain** so they work a sector on their own while you're elsewhere.
- **Aggressive** vs **Attack**: *Aggressive* tells a ship to engage anything hostile it finds;
  *Attack* points it at one specific target.
- **Board** lets you capture rather than destroy an enemy — covered alongside boarding in
  [Combat](Combat).
- The old **Buy Goods / Sell Goods** orders were removed and replaced by the captain trade commands and
  [Trade Contracts](Trade-Contracts).

## See also

- [Fleet commands](Fleet-commands) – the longer self-running captain commands (mine, trade, scout, expedition…)
- [Captains](Captains) – the captains that run those background commands
- [Trade Contracts](Trade-Contracts) – automated buy-low/sell-high routes flown by a Merchant captain
- [Missions](Missions) – the *Ships, Strategies & Captains* tutorial introduces orders
- [Combat](Combat) – the combat orders (Attack, Aggressive, Board) in context

---
*Player Progression & Missions: [Missions](Missions) · [Story missions](Story-missions) · [Events](Events) · [Building knowledge](Building-knowledge) · [Ship orders](Ship-orders) · [Encyclopedia](Encyclopedia)*
