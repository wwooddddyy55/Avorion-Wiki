<!-- Mod documentation. Code lineage (kept out of the reader-facing text on purpose):
     "Avorion Mods/2992809036/" (Xavorion: Mining, v2.5.3; modinfo: serverSideOnly=false, clientSideOnly=false,
     saveGameAltering=true; deps 2918443067/2992808396 min 2.3.9, Avorion 2.0–2.5.*) — modinfo.lua;
     data/scripts/TurretsDatabase/MiningTurrets.lua (WeaponType.MiningLaser/RawMiningLaser/SalvagingLaser/
     RawSalvagingLaser archetypes, TechDamageMult/RarityDamageMult=2.0/4.0, BarrelTweak[Medium]);
     ArmsGenerator/MaterialFunctions/MaterialFunction_{Mining,Salvaging}.lua (per-material Crew/Tracking/
     ShotDamage/Efficiency/EnergyPerSecond/Base+MaxPrice tables, M2–M8 name prefix, _EnergyTweak=0.64,
     _GetScrapDamageMultiplier); ArmsGenerator/BarrelFunctions/BarrelFunction_Mining.lua (_MorphCheck turning
     BarrelType.Medium into Ore/ScrapRefiner/ExtractorLauncher rocket variants, _RocketDamage/_ScrapRocketDamage/
     _RocketReload/_RocketShooting/_RocketEnergy); ArmsGenerator/TechFunctions/TechFunction_Mining.lua (Weapon()
     beam/projectile builders per TechType, stoneDamageMultiplier _StoneMultiplier()=40, metal/stoneRaw/Refined
     Efficiency wiring); companion ArmsGenerator.lua GetScaledShotDamage (tech/rarity formula, defaults 7/2
     overridden per-archetype) in "Avorion Mods/2992808396/" (see XSF: Arms Generator page);
     HarvestSimulation/HarvestSim.lua (IsAllowed/TurretRange=650, MineAsteroid/SalvageWreck, Extract/Refine
     DamageRatio+YieldRatio pairs incl. *Salvage variants, SimulationSpeed/SimulationSpeedSalvage=1/6,
     GatherMiningData/GatherSquadMiningData factor 0.1, SalvageTimer BatteryClass DamagePerItemRoll=5000/
     ItemChance=0.05/ItemUpgradeRatio=0.3, GetObjectDurability, CollectRawOre/CollectRawMetal);
     entity/ai/{mine,harvest,salvage}.lua (AIHarvest base class, GetCategory per order, canContinueHarvesting
     Galaxy:keepOrGetSector keep-alive, checkIfAbleToHarvest, updateHarvesting cargo-space gating);
     player/background/simulation/{minecommand,salvagecommand}.lua (calculateGatheredResources overrides:
     Mine refined/raw ×6.0; Salvage refined/raw ÷10, credits = resourcesPerWreckage × costFactor × 0.075);
     Config/GalaxyModule.lua (FighterMineDamageMult/FighterMineEffMult). Image assets: see wiki/ASSETS.md. -->
# Xavorion: Mining

**Xavorion: Mining** (by **LM13**) is a *"mining rebalance for Xavorion"* — it replaces the vanilla mining
and salvaging lasers with four purpose-built turrets, reshapes how those turrets scale with **material**
and **rarity**, and rewrites the math that runs your **unsupervised** mining and salvaging: ships left to
work asteroids or wreckage while you're not in the sector, and captained ships running a long-running **Mine**
or **Salvage** [fleet command](Fleet-commands). Like [Xavorion: Weaponry](Xavorion-Weaponry), it's built on
the [XSF: Arms Generator](XSF-Arms-Generator) stat engine, but the two mods are independent siblings — this
one doesn't require the weapon overhaul to be installed.

> **In short:** each mining/salvaging turret comes in a **Refiner** (slow, but pipes straight into your
> build-material stockpile — no cargo space, no refinery trip) and an **Extractor** (faster and more
> efficient, but fills your hold with raw ore/scrap you still have to sell or refine). Unlike combat
> turrets, these turrets get **more from rarity than from tech** — chase rarity if you want a faster
> miner. Off-screen, a simplified math model keeps your mining/salvage ships working **while you're not in
> the sector**, and an unsupervised **salvager** has a small chance to hand you a free turret or upgrade as
> it works. The mod also **buffs the Mine fleet command's haul (×6)** and **nerfs Salvage's (÷10, plus a
> credits cut)**.

## The four turrets

| Turret | Works on | What you get | Range |
|---|---|---|---|
| **Mining Refiner** | Asteroids | Refined material, straight into your build stockpile — no cargo used | 4 km |
| **Mining Extractor** | Asteroids | Raw Ore in your cargo hold (sell it, or refine it later) | 4 km |
| **Salvaging Refiner** | Wreckage | Refined material, straight into your build stockpile — no cargo used | 2 km |
| **Salvaging Extractor** | Wreckage | Raw Scrap in your cargo hold (sell it, or refine it later) | 2 km |

A **Refiner** skips the [refining](Refining) step entirely — it pulls material straight into the resource
pool you spend on building, the same pool a Resource Depot fills. An **Extractor** is the faster, more
efficient option at base stats, but it fills your hold with raw **Ore** or **Scrap** that still needs
selling or refining — and a ship that's *only* got Extractors is the one that calls home when its hold
fills up. A ship carrying only Refiners never runs out of space, because it never touches cargo at all.

Every turret is a continuous beam with **perfect tracking** before tier and rarity adjust it — once you're
locked onto a rock or wreck, you don't lose the beam to it dodging. The mid-tier **barrel variant** turns
the beam into something different entirely: instead of just adding a second barrel, it **morphs the turret
into a slower rocket launcher** with a much bigger explosion — Ore-line rockets hit roughly ten times
harder per shot than the beam version, Scrap-line rockets about six times harder, both at an eighth the
fire rate. The other barrel variants (single heavy barrel, triple burst, quad gatling) apply the same way
as on combat weapons — see [XSF: Arms Generator](XSF-Arms-Generator#barrels) for the general rules.

## Rarity matters more than tech here

Combat turrets from this suite get most of their punch from **tech level** (up to ~7×) and a smaller boost
from **rarity** (up to ~2×, see [XSF: Arms Generator](XSF-Arms-Generator#tech--rarity-damage-scaling)).
Mining and salvaging turrets **flip that ratio**: tech only takes them up to **~2×**, while **rarity takes
them up to ~4×**. If you want a meaningfully faster miner or salvager, a high-rarity drop is worth more to
you than a high-tech one — the opposite of what you'd chase for a weapon.

## Material tiers

Each material tier also relabels the turret (an Iron Mining Refiner reads "M2 Mining Refiner," and so on up
to M8 Avorion). **Crew and energy draw climb sharply** with tier on both lines, but **salvaging turrets need
far less crew and about 64% of the energy** a mining turret of the same material costs:

| Tier | Material | Mining Crew | Salvaging Crew | Mining Energy | Salvaging Energy | Price (Base → Max) |
|---|---|--:|--:|--:|--:|---|
| M2 | Iron | 0 | 0 | 1.0 GW | 0.64 GW | 1k → 100k |
| M3 | Titanium | 2 | 1 | 3.5 GW | 2.24 GW | 10k → 250k |
| M4 | Naonite | 4 | 2 | 10 GW | 6.4 GW | 20k → 500k |
| M5 | Trinium | 8 | 3 | 24 GW | 15.36 GW | 40k → 800k |
| M6 | Xanion | 14 | 4 | 42 GW | 26.88 GW | 120k → 2M |
| M7 | Ogonite | 25 | 5 | 64 GW | 40.96 GW | 400k → 4M |
| M8 | Avorion | 50 | 6 | 80 GW | 51.2 GW | 500k → 5M |

The number that actually matters most for your wallet is **Efficiency** — how much of an asteroid's or
wreck's value you actually walk away with — and it's where the two lines diverge most. **Mining's Efficiency
bonus climbs steadily**, from Iron's baseline up to Avorion's **×5**. **Salvaging's doesn't climb in a
straight line**: it starts strong at Iron (**×3**) and actually *drops* through Titanium, Naonite, Trinium
and Xanion (**down to ×1.25**) before jumping back up at Ogonite and topping out at Avorion (**×5**) — so a
mid-tier salvager isn't necessarily a step up from a low-tier one on this stat alone. Tracking accuracy also
drops steadily with tier on both lines (Iron tracks fastest, Avorion slowest), which barely matters here
since the beam locks on perfectly regardless.

## Working while you're away

Normally, a ship you've set to mine or salvage only makes progress while you're nearby to watch it. This
mod adds a fallback: when you leave the sector (or it's simulated for a fleet ship that isn't where you
are), the game keeps that sector quietly running for a short window so the ship doesn't just freeze, and
switches to a **simplified math model** to estimate what it would have mined or salvaged instead of
calculating every shot. The target still has to be within roughly **6.5 km** of the ship for this to kick
in. Fighters in the ship's hangar pitch in too, each worth about a **tenth** of a crewed turret's
contribution.

This fallback model treats mining and salvaging very differently: **salvaging wrecks runs far more
conservatively** than mining asteroids — both the simulated damage rate and the resource yield per hit are
dialed down — so don't expect an unsupervised salvager to clear a wreck anywhere near as fast as an
unsupervised miner clears an equivalent asteroid.

**Bonus loot while salvaging unsupervised:** as the simplified model works through a wreck, it periodically
rolls a small (**5%**) chance to hand you a bonus item — **30%** of those rolls are a system upgrade, the
rest a turret, both generated at the sector's tier. Mining doesn't carry this bonus; only an unsupervised
**salvager** can hand you free gear while you're not watching.

## Mine and Salvage fleet commands

The captain-driven, long-running **[Mine](Fleet-commands#mine)** and **[Salvage](Fleet-commands#salvage)**
fleet commands use their own separate estimate of what a ship would bring home, and this mod rewrites both
estimates in opposite directions:

- **Mine** — the modeled haul of both refined material and raw ore is multiplied **×6**, a straight buff to
  how much a captained mining run brings back.
- **Salvage** — the modeled haul of both refined material and raw scrap is cut to **a tenth** of what it
  would otherwise be, but the command adds a **credits payout** instead, worth roughly **7.5%** of the
  wreckage's estimated material value. A Salvage run trades resource quantity for a smaller, steadier
  credit income.

## See also

- [XSF: Arms Generator](XSF-Arms-Generator) – the shared engine that scales these turrets by tech, rarity, material and barrel
- [Xavorion: Weaponry](Xavorion-Weaponry) – the sibling mod that overhauls combat turrets with the same engine
- [Refining](Refining) – what raw ore and scrap turn into, and the fee for doing it at a station
- [Fleet commands](Fleet-commands) – the captained Mine/Salvage/Refine jobs this mod's command overrides apply to
- [Fighters](Fighters) – squads can be built around mining/salvaging weapons and pitch in on the harvest

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry) · [Xavorion: Mining](Xavorion-Mining) · [Xavorion: Class System](Xavorion-Class-System) · [Xavorion: Encounters](Xavorion-Encounters) · [Xavorion: Combat AI](Xavorion-Combat-AI)*
