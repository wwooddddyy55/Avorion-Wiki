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

> **In short:** orders are the **here-and-now** instructions you give your other ships. A ship will carry
> them out **in the sector you're in**; to have a ship keep working **on its own in another sector** it
> needs a **[captain](Captains)** and a **[fleet command](Fleet-commands)** instead. Some orders need the
> right gear — **Mine** needs mining lasers, **Salvage** needs salvaging lasers, **Board** needs boarding
> crew.

## Order types

Grouped by what they're for. The **Needs** column lists any prerequisite beyond being one of your ships.

### Movement

| Order | What the ship does | Needs |
|---|---|---|
| **Jump** | Jump to a target sector. | — |
| **Fly to Position** | Move to a position within the current sector. | — |
| **Fly Through** | Fly through a wormhole / gate. | — |
| **Dock** | Dock to a station. | — |

### Combat

| Order | What the ship does | Needs |
|---|---|---|
| **Patrol** | Patrol the current sector, engaging threats. | — |
| **Loop** | Fly a repeating loop (patrol a set path). | — |
| **Guard** | Hold and guard a specific position. | — |
| **Aggressive** | Actively seek out and attack hostiles in the sector. | armed turrets |
| **Attack** | Attack one specific target craft. | armed turrets |
| **Escort** | Follow and protect a specific ship. | — |
| **Board** | Board an enemy ship to **capture** it instead of destroying it. | **boarding crew**; target's shields down |

### Work & maintenance

| Order | What the ship does | Needs |
|---|---|---|
| **Mine** | Mine asteroids in the sector. | **mining laser** |
| **Salvage** | Salvage wreckage in the sector. | **salvaging laser** |
| **Refine Ores** | Take mined ore to be refined into materials. | ore in cargo |
| **Repair Target** | Repair a specific friendly ship. | a repair beam |
| **Repair** | Go and get itself repaired. | a repair dock nearby |

## When to use which

- **Aggressive vs Attack:** *Aggressive* engages **anything** hostile it finds in the sector; *Attack*
  points the ship at **one** target. Use Aggressive to defend a sector, Attack to focus-fire a priority.
- **Patrol vs Guard:** *Patrol* roams the whole sector hunting threats; *Guard* holds one spot. Guard a
  mining op or a station; Patrol to sweep.
- **Board** is how you grow your fleet from enemies — knock the target's shields down first, then board
  with enough boarding crew to win. See boarding under [Combat](Combat).
- For anything you want a ship to do **while you're away** — mining a field for hours, running trade
  routes — give it a **captain** and a [fleet command](Fleet-commands), not a one-off order.
- The old **Buy Goods / Sell Goods** orders were removed and replaced by the captain trade commands and
  [Trade Contracts](Trade-Contracts).

## See also

- [Fleet commands](Fleet-commands) – the longer self-running captain commands (mine, trade, scout, expedition…)
- [Captains](Captains) – the captains that run those background commands
- [Trade Contracts](Trade-Contracts) – automated buy-low/sell-high routes flown by a Merchant captain
- [Missions](Missions) – the *Ships, Strategies & Captains* tutorial introduces orders
- [Combat](Combat) – the combat orders (Attack, Aggressive, Board) in context

---
*Fleet & Captains: [Captains](Captains) · [Captain classes](Captain-classes) · [Captain perks](Captain-perks) · [Fleet commands](Fleet-commands) · [Ship orders](Ship-orders)*
