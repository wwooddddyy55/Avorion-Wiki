<!-- Hand-written page. Sourced from data/scripts/player/background/simulation/: commandtype.lua (the
     command list/UUIDs), and the individual *command.lua files for each command's player-facing
     description text and its captain-class checks (hasClass). Mine/Salvage equipment requirements and
     the "Trade requires Merchant" rule come straight from minecommand/salvagecommand/tradecommand.lua. -->
# Fleet commands

**Fleet commands** are the long-running jobs you hand to a ship that has a **[captain](Captains)**. Unlike
the immediate **[ship orders](Ship-orders)** you give in your current sector, a fleet command runs in the
**background simulation**: the ship goes off, works for a set duration (often hours), faces a chance of
ambush, and returns with the results — all while you're flying elsewhere, even in another sector. A ship
**must have a captain** to run these, and the captain's **[class](Captain-classes)** and
**[perks](Captain-perks)** decide how fast, safe, cheap and profitable each command is.

> **In short:** give a captained ship a fleet command and it works **on its own for hours** — mining,
> trading, scouting, expeditions — then returns with the haul, even from other sectors. **Match the command
> to the captain's class** (a Miner mines fastest, a Merchant is required to trade), and turn on **Safe
> Mode** when the cargo is worth more than the extra time. Every command carries an **ambush risk** that the
> captain's perks raise or lower.

Most commands share the same config knobs: a **Duration** slider, a **Safe Mode** toggle (slower but safer),
**Immediate Delivery**, a **budget**, and a predicted **attack chance** and **yield**.

## Command list

| Command | What the ship does | Best class(es) |
|---|---|---|
| **Travel** | Fly to another sector and wait there | Commodore, Explorer (faster/safer travel) |
| **Scout** | Explore and reveal nearby sectors | Explorer; also Smuggler, Miner |
| **Mine** | Mine asteroids for resources | **Miner** |
| **Salvage** | Salvage wreckages for resources | **Scavenger** |
| **Refine** | Refine mined ore / scrap into materials | Miner, Scavenger |
| **Trade** | Fly an automated buy‑low / sell‑high trade route | **Merchant** (required) |
| **Procure** | Buy a chosen good and bring it back | Merchant, Smuggler |
| **Sell** | Sell the ship's cargo | Merchant, Smuggler |
| **Supply** | Supply stations with goods | Merchant, Smuggler |
| **Expedition** | Send the ship on an expedition into no‑man's‑space | many (Explorer, Daredevil, Smuggler, Merchant, Miner, Scavenger) |
| **Maintenance** | Spend time repairing / maintaining the ship | — |
| **Escort** | Follow and protect another of your ships | — |

> *(A "Prototype" command exists in the files but is for development only and isn't available in normal play.)*

## Command details

### Travel
Sends the ship to a target sector and parks it there. A **Commodore** travels with less risk, and an
**Explorer** helps it get there faster. Useful for repositioning fleet ships without flying them yourself.

### Scout
The ship explores the area and reveals surrounding sectors on the map. **Explorer** captains are the
specialists (and benefit from the class's +3 deep‑scan range); **Smuggler** and **Miner** captains also
get scouting bonuses.

### Mine
*"Ship is mining resources."* The ship mines asteroids for ore over the chosen duration. **It needs mining
equipment** (mining turrets) or it can't run the command. A **Miner** captain knows where to find proper
asteroid fields, highlights hidden ores, and mines for longer (duration bonus scales with tier and level).

### Salvage
*"Ship is salvaging wreckages for resources."* The ship breaks down wreckage for resources. **It needs
salvaging equipment.** A **Scavenger** captain highlights valuable wreckage and salvages for longer
(duration bonus scales with tier and level).

### Refine
*"Ship is refining resources."* Turns mined ore or salvaged scrap into usable materials over time, so the
ship doesn't have to fly back to a refinery itself. **Miner** and **Scavenger** captains improve it, and
the *Connected* perk lowers the refinery tax. See **[Refining](Refining)** for the underlying mechanic.

### Trade
*"The ship is flying a trade route."* The captain runs a sequence of flights, buying goods cheap and
selling them dear for profit. **This command requires a Merchant captain** — no other class can fly a
trade route. This is the system behind automated **[Trade Contracts](Trade-Contracts)**.

### Procure
*"The ship is procuring goods."* The ship goes out and buys a specific good, then brings it back. A
**Merchant** gets better prices and licenses for suspicious/dangerous goods; a **Smuggler** can fetch
anything, including stolen goods. The *Connected*, *Market Expert* and *Intimidating* perks improve the
price.

### Sell
*"The ship is selling cargo."* The ship takes its cargo to market and sells it. **Merchant** captains
secure higher profits; **Smuggler** captains can offload restricted/stolen cargo.

### Supply
*"Ship is supplying stations with goods."* The ship keeps stations stocked with goods. **Merchant** and
**Smuggler** captains are best suited to the logistics.

### Expedition
*"The ship is on an expedition."* The ship heads into no‑man's‑space for a timed expedition and returns
with rewards. A wide range of classes shape the outcome — **Explorer**, **Daredevil**, **Smuggler**,
**Merchant**, **Miner** and **Scavenger** each tilt what an expedition can find.

### Maintenance
*"The ship is doing maintenance."* The ship spends time repairing and maintaining itself. While it's under
repair it **can't be recalled** until the work is done.

### Escort
*"The ship is escorting ship …"* The ship follows and protects a chosen friendly ship of yours, moving
with it through the galaxy.

## Risk & rewards

Every command (except passive ones like Escort) carries an **attack chance** — a risk the ship is ambushed
while working. The captain's perks and class push this up or down, **Safe Mode** lowers it at the cost of
speed, and neutral perks like *Cunning*/*Harmless* change how strong any attackers are. Commands also show
a **predicted yield** before you commit. For the perk-by-perk breakdown, see **[Captain perks](Captain-perks)**.

## See also

- **[Captains](Captains)** – the captain you need to run these commands
- **[Captain classes](Captain-classes)** – which class is best for which command
- **[Captain perks](Captain-perks)** – how perks change speed, safety and profit
- **[Ship orders](Ship-orders)** – the immediate, in-sector orders for any ship
- **[Trade Contracts](Trade-Contracts)** – Merchant trade routes

---
*Fleet & Captains: [Captains](Captains) · [Captain classes](Captain-classes) · [Captain perks](Captain-perks) · [Fleet commands](Fleet-commands) · [Ship orders](Ship-orders)*
