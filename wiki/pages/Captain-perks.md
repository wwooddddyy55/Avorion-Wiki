<!-- Hand-written page. Sourced from lib/captainutility.lua: PerkType (the 21 perk IDs),
     PerkProperties() (in-game one-line summaries), and all getPerk*Impact functions for
     exact magnitudes. Positive/negative/neutral grouping and opposing-perk pairs are from
     lib/captaingenerator.lua (getPossiblePerks + addOpposingPerk).
     Salary effects of Humble/Greedy are from captaingenerator.lua:calculateSalary.
     Numerical values verified directly from source — last updated from captainutility.lua. -->
# Captain perks

**Perks** are small traits a captain carries that tweak how their ship performs **[fleet commands](Fleet-commands)** —
how fast and cheaply a command finishes, how big the profit or yield is, how likely an ambush is, and how
much salary the captain demands. They are the main reason two captains of the same **[class](Captain-classes)**
behave differently. Higher-**tier** captains roll more positive perks and (from tier 2) no negative ones —
see **[Captains](Captains)**.

There are **21** perks in three groups: **positive**, **negative** and **neutral** (mixed blessings).

## Positive perks

| Perk | Effect |
|---|---|
| **Educated** | Gains more experience when fulfilling commands |
| **Humble** | Demands lower salary (×0.9) |
| **Connected** | Better trade prices (−2% buy / +2% sell), −10% maintenance cost, −2% refine tax |
| **Navigator** | Faster completion of commands (scales with level) |
| **Stealthy** | Lower risk of being ambushed (scales with level) |
| **Market Expert** | Faster completion of trade/sell commands (scales with level); no effect on mining or salvaging |
| **Intimidating** | Lower risk of being ambushed, better trade prices (−2% buy / +2% sell), −10% maintenance cost |
| **Lucky** | May find turrets or subsystems while on a command (more items at higher level) |

## Negative perks

| Perk | Effect |
|---|---|
| **Uneducated** | Gains less experience when fulfilling commands |
| **Greedy** | Demands higher salary (×1.1) |
| **Disoriented** | Slower completion of commands (penalty shrinks with level) |
| **Gambler** | Worse trade prices (+1% buy / −1% sell), +10% maintenance cost, +5% refine tax |
| **Addict** | Slower completion of commands (penalty shrinks with level) |
| **Arrogant** | Higher risk of being ambushed (penalty shrinks with level) |
| **Unlucky** | Ship may suffer damage while on commands (damage chance shrinks with level) |

## Neutral perks

These cut both ways — each has an upside and a downside.

| Perk | Effect |
|---|---|
| **Reckless** | Faster travel, scouting, and sell times — **but** +5% flat ambush chance |
| **Careful** | −10% flat ambush chance — **but** slower travel, scouting, and sell times |
| **Cunning** | Lower ambush chance (scales with level) — **but** ambushing enemies are stronger (scales with level) |
| **Harmless** | Higher ambush chance (scales with level) — **but** ambushing enemies are weaker (scales with level) |
| **Noble** | Worse trade margins (+1% buy / −1% sell), +10% maintenance cost, **×2.0 refine tax** |
| **Commoner** | Better trade margins (−2% buy / +2% sell), −10% maintenance cost, **×0.5 refine tax** |

> **Note:** Noble and Commoner have **no effect on ambush chance**. Their tradeoff is entirely economic.

## Perk effect reference

All values sourced directly from `captainutility.lua`. Level refers to captain level 0–5.

### Command speed
A negative value = faster (time reduction). A positive value = slower (time increase).
Navigator and Reckless apply to travel time, scout time, and sell time equally.
Market Expert applies to sell time only.

| Perk | Lvl 0 | Lvl 1 | Lvl 2 | Lvl 3 | Lvl 4 | Lvl 5 |
|---|---|---|---|---|---|---|
| **Navigator** | −1% | −5% | −10% | −15% | −20% | −25% |
| **Reckless** | −10% | −15% | −20% | −25% | −30% | −35% |
| **Market Expert** *(sell time only)* | 0% | −10% | −20% | −30% | −40% | −50% |
| **Disoriented** | +12.5% | +10% | +7.5% | +5% | +2.5% | +1% |
| **Addict** | +12.5% | +10% | +7.5% | +5% | +2.5% | +1% |
| **Careful** | +15% | +12.5% | +10% | +7.5% | +5% | +2.5% |

### Ambush chance
Negative = reduces chance of being attacked. Positive = increases it.

| Perk | Lvl 0 | Lvl 1 | Lvl 2 | Lvl 3 | Lvl 4 | Lvl 5 |
|---|---|---|---|---|---|---|
| **Careful** | −10% | −10% | −10% | −10% | −10% | −10% |
| **Stealthy** | −2% | −4% | −6% | −8% | −10% | −12% |
| **Intimidating** | −2% | −4% | −6% | −8% | −10% | −12% |
| **Cunning** | −2% | −4% | −6% | −8% | −10% | −12% |
| **Reckless** | +5% | +5% | +5% | +5% | +5% | +5% |
| **Arrogant** | +6% | +5% | +4% | +3% | +2% | +1% |
| **Harmless** | +6% | +5% | +4% | +3% | +2% | +1% |

### Attacker strength
Applies when an ambush occurs. Values are multipliers on enemy strength.

| Perk | Lvl 0 | Lvl 1 | Lvl 2 | Lvl 3 | Lvl 4 | Lvl 5 |
|---|---|---|---|---|---|---|
| **Cunning** | ×1.50 | ×1.45 | ×1.40 | ×1.35 | ×1.30 | ×1.25 |
| **Harmless** | ×0.95 | ×0.90 | ×0.85 | ×0.80 | ×0.75 | ×0.70 |

### Trade margins & maintenance
Flat values, no level scaling.

| Perk | Buy price | Sell price | Maintenance cost | Refine tax |
|---|---|---|---|---|
| **Connected** | −2% | +2% | −10% | −2% |
| **Intimidating** | −2% | +2% | −10% | — |
| **Commoner** | −2% | +2% | −10% | ×0.5 (halved) |
| **Gambler** | +1% | −1% | +10% | +5% |
| **Noble** | +1% | −1% | +10% | ×2.0 (doubled) |

### Lucky / Unlucky
Lucky: extra items (turrets or subsystems) that may be found during a command.
Unlucky: a damage chance that applies during commands.

| Perk | Lvl 0 | Lvl 1 | Lvl 2 | Lvl 3 | Lvl 4 | Lvl 5 |
|---|---|---|---|---|---|---|
| **Lucky** *(bonus items)* | 1 | 2 | 3 | 4 | 5 | 6 |
| **Unlucky** *(damage chance)* | 50% | 45% | 40% | 35% | 30% | 25% |

## Opposing perks

Certain perks are opposites; a captain can never have both, and rolling one removes the other from the
pool when the captain is generated:

| Perk | Opposes |
|---|---|
| Educated | Uneducated |
| Humble | Greedy |
| Reckless | Careful |
| Navigator | Disoriented |
| Stealthy | Arrogant |
| Cunning | Harmless |
| Noble | Commoner |
| Lucky | Unlucky |
| Intimidating | Harmless |

> *Harmless* opposes **both** *Cunning* and *Intimidating*.

## Notes

- Perks that scale with level generally become **more beneficial** for positive perks and **less punishing**
  for negative ones. A level 5 captain with Arrogant has only +1% ambush chance versus +6% at level 0.
- **Reckless** is the fastest travel perk in the game but is the only perk with a flat, unmitigated
  attack-chance penalty that does not shrink with level.
- **Market Expert** has no effect on non-trade commands (mining, salvaging, scouting, etc.).
- **Noble** and **Commoner** have no ambush effect — their tradeoff is entirely economic. Noble's ×2.0
  refine tax multiplier is particularly punishing for captains running refine commands.
- Class restrictions can block some perks entirely — e.g. a Daredevil never rolls *Careful* or *Arrogant*.
  See the table on **[Captain classes](Captain-classes)**.

## See also

- **[Captains](Captains)** – how many perks each tier rolls, and the salary formula
- **[Captain classes](Captain-classes)** – class bonuses and forbidden perks
- **[Fleet commands](Fleet-commands)** – the commands perks modify

---
*Fleet & Captains: [Captains](Captains) · [Captain classes](Captain-classes) · [Captain perks](Captain-perks) · [Fleet commands](Fleet-commands) · [Ship orders](Ship-orders)*
