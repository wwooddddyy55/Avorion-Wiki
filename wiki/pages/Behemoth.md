<!-- Hand-written page. Sourced from data/scripts/galaxy/behemothevent.lua (the galaxy-wide timer/quadrant
     picker), data/scripts/sector/background/spawnbehemoth.lua (createBehemoth, makeRailgunTurret, loot
     tables, finish/destruction logic), data/scripts/lib/behemotheventutility.lua (quadrant naming),
     data/scripts/entity/background/behemothbehavior.lua (the salvaging-fighter hangar behaviour), and
     the four signature system upgrades: data/scripts/systems/behemothmilitarytcs.lua,
     behemothciviltcs.lua, behemothcarriersystem.lua, behemothhyperspacesystem.lua. Ship blueprints are
     data/plans/behemoth1.xml–behemoth4.xml. The Xavorion: Encounters mod overrides part of this event —
     see that page — but everything below is the vanilla behaviour. -->
# The Behemoth

**The Behemoth** is a galaxy-wide roaming world-boss event, separate from the ten named encounters
catalogued on [World bosses](World-bosses). Where those wait in a fixed sector for you to find them, the
Behemoth actively hunts: on a recurring timer it picks an undefended outpost somewhere in the galaxy and
threatens to wreck it, broadcasting a galaxy-wide warning and giving every player a limited window to
race there and stop it. Win, and you walk away with one of four huge, direction-locked **Legendary system
upgrades** you can't get any other way.

> **In short:** every **2 hours**, the Behemoth shows up at an empty AI-faction outpost in one of four
> compass quadrants (cycling **North → East → South → West**, in an order shuffled per galaxy) and gives
> players **20 minutes** to arrive and kill it before it wrecks the place and moves on. It's a single,
> enormous, slow-moving battleship escorted by a self-replenishing wing of salvage fighters, and on death
> it drops a huge loot pile plus a **unique Legendary system upgrade** tied to that quadrant — so chasing
> the full set means beating all four variants over multiple cycles.

## Where and when it appears

The event only starts counting once a galaxy has been running for **2 hours** of total server time; until
then, no Behemoth will spawn. After that, a **1-hour** countdown begins. When it expires, the game searches
a ring **180–500 sectors** out from the core, inside the quadrant whose turn it is, for an AI-faction
sector that has stations but **no player presence** — so it never targets a base you're actively
defending. A galaxy-wide chat warning announces the sighting and sector coordinates the moment it spawns.

Players then get **20 minutes** to reach that sector and engage. If someone does (or even just arrives),
the boss is removed without harming the sector and a "moved on" message is broadcast. If nobody shows up,
the Behemoth **wrecks the outpost** — its stations are turned into wreckage and any non-station property
in the sector changes hands — before the timer resets to **2 hours** and the cycle moves on to the next
quadrant in the (per-galaxy shuffled) order.

## The fight

Each quadrant has its own unique, hand-built hull — **Behemoth of the North / East / South / West** — so
the ship you face depends on which direction is currently active. Whichever hull it is, the boss arrives
with a full turret loadout of heavy, long-range **railgun batteries** (roughly an 8 km reach, firing in a
wide beam, slow-turning and crewless), plus dedicated **anti-torpedo point-defence** so torpedo spam alone
won't trivialise the fight. It launches at full crew and full shields, flying for a faction called simply
**"Behemoths"** that starts at **−100,000 relations** with every player and faction and never improves —
there's no diplomatic path around it, and its home base is untraceable on the galaxy map.

A few rules make it tougher than it looks: it can't be boarded or docked with, it won't drop its mounted
turrets when destroyed (so you can't just snipe turrets off the hull for easy loot mid-fight), and its
overall firepower is **normalised to a fixed total** regardless of which turrets it ends up carrying — so
every variant, every roll, hits with the same overall punch rather than one randomly ending up softer or
harder than the others.

## The salvage swarm

The Behemoth itself barely moves — its thrusters and engine are pinned to a crawl — so instead of chasing
anything itself, it runs its own internal carrier operation. It launches a wing of up to **10 fighter
squadrons** crewed via a huge built-in pilot bonus, and continuously builds **dedicated salvaging
fighters** (Exceptional-rarity, fitted with a raw salvaging laser) up to a cap of **120**, scaled to twice
the amount of wreckage currently floating in the sector. Those fighters ignore normal carrier orders
entirely: they autonomously hunt down and salvage the nearest wreck — including wrecks from ships *you*
lose in the fight — and only fall back to defending the mothership when there's nothing left to salvage.
Practically, this means a long fight against the Behemoth keeps recycling its own battlefield debris into
fresh fighters, so dragging the fight out doesn't starve it of escorts.

## Loot

On death, the Behemoth drops a large, escalating pile of loot split evenly between **system upgrades** and
**turrets**, plus a guaranteed bonus Legendary turret and a building-knowledge unlock — the same loot
hooks used by the named [World bosses](World-bosses):

| Rarity | Amount (each of upgrades & turrets) |
|---|--:|
| **Legendary** | 2 |
| **Exotic** | 3 |
| **Exceptional** | 3 |
| **Rare** | 5 |
| **Uncommon** | 8 |
| **Common** | 14 |

## The signature upgrade per direction

The real prize is a **quadrant-locked Legendary system upgrade** that only ever drops from that direction's
Behemoth — kill the Behemoth of the North enough times and you'll never see the other three:

| Quadrant | Boss | Signature drop | What it does |
|---|---|---|---|
| **North** | Behemoth of the North | **Behemoth Combat Subsystem** | Adds **armed turret slots** (3, rising to 4 at Exotic and 5 at Legendary) |
| **East** | Behemoth of the East | **Behemoth Civil Subsystem** | Adds the same number of **unarmed turret slots** |
| **South** | Behemoth of the South | **Behemoth Carrier Subsystem** *("Dozen-headed Behemoth")* | Adds a **fighter squadron** and a **production speedup** |
| **West** | Behemoth of the West | **Behemoth Exploration Booster** | Adds **jump range**, **radar range**, and cuts **hyperspace cooldown** |

All four share a quirk: **socketed**, they only grant their core bonus; **permanently installed**, each one
also unlocks a secondary bonus (defensive or auto-turret slots, extra fighter squadrons, jump/radar range)
*and* starts stacking with other, related upgrades you've also installed permanently:

- **Combat Subsystem** — a permanent install opens **defensive (point-defence) turret slots** equal to its
  armed-slot count, plus a batch of random **auto-turret slots**. Every other **Military** or
  **Auto Turret Control System** you also install permanently adds further armed-turret slots in climbing
  tiers (+1 each for the first four, +2 each for the next four, +3 each after that, +4 each beyond — up to
  **+32** total).
- **Civil Subsystem** — the same mechanic, but for **unarmed turret slots**, stacking with **Civil Turret
  Control**, **Auto Turret Control**, and the **Mining System**.
- **Carrier Subsystem** — grants one fighter squadron outright (a ship can hold **10 squadrons** max), and
  each other permanently-installed **Fighter Control**, **Shield**, or **Mining System** adds another
  squadron (up to **+9** more) plus **2.5%** production speedup apiece (up to roughly **+35%** total).
- **Exploration Booster** — only does anything meaningful permanently installed: a baseline **+2 jump and
  radar range**, plus the same **+2** for every permanently-installed **Hyperspace**, **Radar**, **Object
  Detection**, or **Trading System** (up to **+30** each), and a hyperspace recharge-cooldown cut that
  improves with rarity.

> Because the bonus only really pays off once you're stacking several matching permanent upgrades, these
> are best treated as the **capstone** of a themed build (a turret-slot ship, a carrier, an explorer) rather
> than a drop-in upgrade for any random ship.

## If nobody shows up

Losing the race has a visible cost: the targeted sector's stations are converted to wreckage and any
non-station property in the sector loses its owner, then a galaxy-wide message announces that the
Behemoth "left the sector in ruins." There's no second chance for that specific visit — the boss simply
resets its 2-hour timer and moves on to the next quadrant in the cycle.

## Tips

- The first Behemoth can't appear before **2 hours** of total server runtime, so don't expect one in a
  brand-new galaxy right away.
- The North → East → South → West order is **shuffled once per galaxy**, so don't assume the next
  quadrant follows the obvious compass order — watch the chat warning for the real sighting location.
- You only have **20 minutes** from the warning to arrive and tag the fight, so keep an eye on chat if
  you're hunting a specific direction's upgrade.
- Collecting all four signature upgrades means beating all four directional variants, which — since only
  one quadrant is "live" at a time — takes multiple 2-hour cycles at minimum.

## See also

- [World bosses](World-bosses) – the fixed-sector named bosses and the shared world-boss template
- [Special enemies](Special-enemies) – the background spawner that triggers persecutors and the Behemoth
- [World and Sector Generation](World-and-Sector-Generation#background-systems-that-keep-the-galaxy-alive) – the other galaxy-wide timers running alongside it
- [Events](Events) – the other roaming bosses and ambushes
- [System upgrades](System-upgrades) – how permanent installation and upgrade stacking work in general
- [Fighters](Fighters) – squadrons, hangars and carrier mechanics

---
*Enemies & Bosses: [Enemy AI](Enemy-AI) · [Special enemies](Special-enemies) · [World bosses](World-bosses) · [Rift Expeditions](Rift-Expeditions) · Behemoth*
