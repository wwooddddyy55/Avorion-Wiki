<!-- Hand-written page. Sourced from lib/captainclass.lua (the 9 class IDs) and lib/captainutility.lua:
     ClassProperties() (display names + descriptions) and makeTooltip() (the concrete per-class bonus
     lines: turret slots, highlights, durations, fire rate, deep scan, licenses, rift research/hunter).
     Mining/Salvaging duration bonus = 0.5 + tier + level*0.5 hours; Scientist data interval =
     80 - (tier+level)*5 seconds. "Forbidden perk" column is from getImpossiblePerksOfClass(). -->
# Captain classes

A captain's **class** is their specialization. It grants concrete bonuses to the ship they command and an
affinity for certain **[fleet commands](Fleet-commands)**. There are **nine** classes. A captain has one
primary class at tier 1–2, and a primary **plus** a secondary class at tier 3 (tier‑0 captains are
unspecialized until they reach level 5). See **[Captains](Captains)** for tiers and levels.

## At a glance

| Class | Role | Headline bonus |
|---|---|---|
| **Commodore** | Combat fleet leader | +2 armed turret slots, +4 auto‑turret slots |
| **Smuggler** | Illicit hauling | Can carry **any** cargo (stolen / dangerous / suspicious) |
| **Merchant** | Trading | Best trade prices; only class that can fly **trade routes** |
| **Miner** | Mining | +2 unarmed turret slots, highlights hidden ores, longer mining |
| **Scavenger** | Salvaging | +2 unarmed turret slots, highlights valuable wreckage, longer salvaging |
| **Explorer** | Exploration | +3 deep‑scan range |
| **Daredevil** | Aggressive combat | +10% turret fire rate |
| **Scientist** | Rift research | Collects research data inside subspace rifts |
| **Xsotan Hunter** | Rift combat | Attracts rare rift Xsotan that drop special loot |

## Class details

### Commodore
An experienced fleet commander; enemies think twice before attacking. Built for combat ships.
- **+2 Armed Turret Slots**
- **+4 Auto‑Turret Slots**

### Smuggler
An expert in shady deals who can move goods of all kinds.
- Cargo **"License": Everything** — can transport stolen, dangerous and suspicious goods, and is immune
  to the usual penalties for carrying stolen cargo.

### Merchant
A gifted trader with superior powers of persuasion.
- Cargo **License: Suspicious + Dangerous** goods (no permits needed)
- Secures the best deals (better buy/sell prices)
- **The only class that can run the Trade command** — i.e. fly automated buy‑low/sell‑high
  **[Trade Contracts](Trade-Contracts)** routes.

### Miner
An experienced miner with a good eye for rocks.
- **+2 Unarmed Turret Slots**
- **Highlights hidden ores** in the sector
- **+Mining Duration**: `0.5 + tier + (level × 0.5)` hours — lets the ship mine longer per command

### Scavenger
A passionate scavenger who knows scrap and metals.
- **+2 Unarmed Turret Slots**
- **Highlights valuable wreckage** in the sector
- **+Salvaging Duration**: `0.5 + tier + (level × 0.5)` hours — lets the ship salvage longer per command

### Explorer
On a mission to map the galaxy and collect data.
- **+3 Deep Scan Range** (reaches more hidden sectors)
- Speeds up exploration-type commands such as **Scout**.

### Daredevil
Always in trouble, never down for long, and shares loot with allies.
- **+10% Turret Fire Rate**

### Scientist
Part of a guild that explores **Rifts**. While inside a subspace rift the ship:
- **Collects research data** automatically, once every `80 − (tier + level) × 5` seconds
- Drops **+200%** research data
- **Highlights rift research data** in the sector

### Xsotan Hunter
Devoted to fighting the Xsotan, with deep knowledge of Rifts. While inside a subspace rift:
- **Attracts rare rift Xsotan**
- Those rare Xsotan yield **special loot** rewards

## Forbidden perks per class

When a captain is generated, their class blocks certain perks from ever rolling — usually ones that would
contradict the class. (See [Captain perks](Captain-perks) for what each perk does.)

| Class | Cannot have |
|---|---|
| Commodore | Careful |
| Smuggler | Noble, Unlucky |
| Merchant | Noble |
| Miner | Noble |
| Scavenger | Noble |
| Explorer | Disoriented |
| Daredevil | Arrogant, Careful |
| Scientist | Uneducated |
| Xsotan Hunter | Harmless |

## See also

- **[Captains](Captains)** – tiers, levels and salary
- **[Captain perks](Captain-perks)** – the 21 perks
- **[Fleet commands](Fleet-commands)** – which commands each class is best at
- **[Trade Contracts](Trade-Contracts)** – Merchant trade routes

---
*Fleet & Captains: [Captains](Captains) · [Captain classes](Captain-classes) · [Captain perks](Captain-perks) · [Fleet commands](Fleet-commands) · [Ship orders](Ship-orders)*
