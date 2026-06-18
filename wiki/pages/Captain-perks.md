<!-- Hand-written page. Sourced from lib/captainutility.lua: PerkType (the 21 perk IDs) and
     PerkProperties() (the in-game one-line "summary" for each perk). Positive/negative/neutral grouping
     and the opposing-perk pairs are from lib/captaingenerator.lua (getPossiblePerks + addOpposingPerk).
     Salary effects of Humble/Greedy are from captaingenerator.lua:calculateSalary. -->
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
| **Connected** | Negotiates better prices |
| **Navigator** | Faster completion of commands |
| **Stealthy** | Lower risk of being ambushed |
| **Market Expert** | Higher profits and faster completion of trade commands |
| **Intimidating** | Lower risk of being ambushed, reduced costs for commands |
| **Lucky** | May find turrets or subsystems while on a command |

## Negative perks

| Perk | Effect |
|---|---|
| **Uneducated** | Gains less experience when fulfilling commands |
| **Greedy** | Demands higher salary (×1.1) |
| **Disoriented** | Slower completion of commands |
| **Gambler** | Reduced profits, smaller yields when refining |
| **Addict** | Slower completion of commands |
| **Arrogant** | Higher risk of being ambushed |
| **Unlucky** | Ship may suffer damage while on commands |

## Neutral perks

These cut both ways — each has an upside and a downside.

| Perk | Effect |
|---|---|
| **Reckless** | Higher ambush risk, **but** faster completion of commands |
| **Careful** | Lower ambush risk, **but** slower completion of commands |
| **Cunning** | Lower ambush risk, **but** attacking enemies are stronger |
| **Harmless** | Higher ambush risk, **but** attacking enemies are weaker |
| **Noble** | Lower ambush risk, **but** reduced profits |
| **Commoner** | Higher ambush risk, **but** increased profits |

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

- A perk's actual magnitude scales with the captain (tier/level) and with the **command** being run — for
  example *Connected*, *Market Expert* and *Navigator* show different numbers on a mining command versus a
  trade command. The summaries above are the in-game one-line descriptions.
- *Market Expert* explicitly has **no effect** on non-trade commands like mining and salvaging.
- Class restrictions can block some perks entirely — e.g. a Daredevil never rolls *Careful* or *Arrogant*.
  See the table on **[Captain classes](Captain-classes)**.

## See also

- **[Captains](Captains)** – how many perks each tier rolls, and the salary formula
- **[Captain classes](Captain-classes)** – class bonuses and forbidden perks
- **[Fleet commands](Fleet-commands)** – the commands perks modify

---
*Fleet & Captains: [Captains](Captains) · [Captain classes](Captain-classes) · [Captain perks](Captain-perks) · [Fleet commands](Fleet-commands) · [Ship orders](Ship-orders)*
