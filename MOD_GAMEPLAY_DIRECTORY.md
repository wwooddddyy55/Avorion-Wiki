# 🛠️ Avorion Gameplay Mod Directory

## Overview

A total of **36 mod subfolders** under `Avorion/Avorion Mods/` were scanned, of which **10 were excluded** (9 ship/turret/plan blueprint folders containing only `.xml`/`.png` design data, and 1 pure-SFX sound swap with no scripts). The remaining **26 gameplay-altering mods** — spanning the LM13 "Xavorion / XSF" overhaul suite, modding frameworks, standalone server-side tweaks, and client-side UI/QoL tools — are mapped below with verbatim developer descriptions and per-mod script-hook analysis.

> **Path convention:** All script paths are relative to each mod's own folder root (`Avorion Mods/<ID>/`). All metadata is extracted directly from each folder's `modinfo.lua`.

---

## Exclusions

> Folders deliberately omitted from the gameplay index. These contain no Lua logic that hooks base-game loops.

| Folder / ID | Contents | Reason for Exclusion |
|---|---|---|
| `1222936504` | `plan.xml` (+ `.meta`, `.png`) | Ship blueprint — design data only |
| `951714493` | `plan.xml` (+ `.meta`, `.png`) | Ship blueprint — design data only |
| `1461094414` | `design.xml` (+ `.meta`, `.png`) | Ship design — design data only |
| `1528430491` | `design.xml` (+ `.meta`, `.png`) | Ship design — design data only |
| `1544930351` | `design.xml` (+ `.meta`, `.png`) | Ship design — design data only |
| `1990700241` | `design.xml` (+ `.meta`, `.png`) | Ship design — design data only |
| `2058413898` | `design.xml.meta` (+ `.png`) | Ship design — design data only |
| `1527748039` | `turretdesign.xml` | Turret design — design data only |
| `1527748654` | `turretdesign.xml` | Turret design — design data only |
| `3293405773` | `data/sfx/weapon/*.wav` (5 files) + thumbnail | **"Scout's Punchy Railguns"** — `clientSideOnly=true`, pure railgun SFX swap, **0 Lua scripts** |

---

## Active Gameplay Modifications

| Folder / ID | Mod Title | Author(s) | Functional Category | Core Mechanism Summary |
|---|---|---|---|---|
| `2918443067` | Xavorion: eXtended Scripting Framework | LM13 | Framework / Library | Core scripting framework (SystemUpgrade, ShipXAI, GalaxyGenerator, Core libs) required by all Xavorion modules |
| `1722652757` | AzimuthLib - Library for modders | Rinart73 | Framework / Library | UI + utility helper functions (config, UTF8, custom UI widgets) consumed by other mods |
| `2923179923` | Xavorion: eXtended Avorion | LM13 | Xavorion Suite – Galaxy/Economy Core | Overhauls galaxy distribution, economy, progression, ship/turret/upgrade generation; resources & tech spread galaxy-wide |
| `2992808561` | XSF: Sector Generator | LM13 | Xavorion Suite – Sector Gen | Advanced replacement for the vanilla sector generator (station database, merchant placement) |
| `2992808472` | XSF: Fleet Generator | LM13 | Xavorion Suite – Spawn Gen | Advanced replacement for the vanilla spawn system; staged fleet composition, roles, loadouts, scaling |
| `2992808396` | XSF: Arms Generator | LM13 | Xavorion Suite – Weapon Gen | Advanced replacement for the vanilla turret generator (barrel/material/rarity/tech functions) |
| `2992809109` | Xavorion: Weaponry | LM13 | Xavorion Suite – Combat | Complete weapons overhaul: turret database, weapon sounds, fighter squad system |
| `2992809240` | Xavorion: Sectors | LM13 | Xavorion Suite – World Content | Extension to galaxy generator adding sector variety, economy goods, trading, missions |
| `2992809036` | Xavorion: Mining | LM13 | Xavorion Suite – Mining | Mining rebalance: mine/harvest/salvage AI, harvest simulation, mining turrets, fleet commands |
| `2992808903` | Xavorion: Formations | LM13 | Xavorion Suite – Fleet AI | Replaces Escort command with formation flight (formation DB, order controller, XAI states) |
| `2992808843` | Xavorion: Flight Physics | LM13 | Xavorion Suite – Flight | Adds to vanilla flight with collision prevention; AI hard-turn/sprint states, flight caps |
| `2992809187` | Xavorion: Encounters | LM13 | Xavorion Suite – Spawning | Overhaul of spawn encounters into fleets of varied size/role/loadout; wave encounters, faction war, persecutors |
| `2992808719` | Xavorion: Docking | LM13 | Xavorion Suite – Docking | Minor docking-range tweak to roughly match tractor-beam reach |
| `2992808971` | Xavorion: Combat AI | LM13 | Xavorion Suite – Combat AI | Combat AI extension for NPC & player ships; RTS/TPP QoL via combat HUD and smart-attack states |
| `3165545472` | Xavorion: Class Upgrades | LM13 | Xavorion Suite – Upgrades/Systems | Rework of vanilla & eXtended upgrades; role-based ships via 125-script system/subsystem/torpedo rework |
| `2992808773` | Xavorion: Class System | LM13 | Xavorion Suite – Build/Progression | Extends flight model, build mode and ship progression (ship balancer, build-mode UI, class mod) |
| `2992808642` | Xavorion: Starter Ship | LM13 | Xavorion Suite – Start | Starter-ship module; allows using other ships at game start |
| `1692998037` | Laserzwei's simple asteroid respawn mod | Laserzwei | Standalone – World/Server | Simplifies & live-extends the vanilla resource-asteroid respawn mechanic (server-side) |
| `1819452708` | More Resources Mod | Deathreel | Standalone – World | Converts more asteroids into resource asteroids without changing resource-type availability |
| `1695671502` | Laserzwei's Advanced Shipyard | Laserzwei | Standalone – Economy | Extends vanilla shipyards to build custom player-made ship designs |
| `2109258268` | [2.0] - (SDK) Rebalance - Static Founding Cost | SDK | Standalone – Economy | Removes the scaling ship/station founding cost to ease economy growth |
| `1751798934` | System Scanner Upgrade | MassCraxx | Standalone – Equipment | Adds a new System Scanner upgrade module + ship system |
| `1769379152` | Resource Display | Rinart73 | UI / QoL | Always displays player resources on screen (depends on AzimuthLib) |
| `1751636748` | Detailed Turret Tooltips | lyravega, MrMors, MassCraxx, Mp70 | UI / QoL | Adds hull-DPS and shield-DPS-per-slot detail to turret tooltips |
| `3741814524` | Blueprint Stat Compare | SuurflieG | UI / QoL | Browse saved/workshop ship designs and compare stats side by side |
| `3739343155` | Trade Heatmap Alliance ship fix | CobaltStorm | UI / QoL (Bugfix) | Fixes base-game bug so the trading heatmap/overview works on alliance ships |

---

## Detailed Mod Deep-Dives

### A. Frameworks & Libraries

### Xavorion: eXtended Scripting Framework (Folder: 2918443067)

* **Developer Description:** "Requirement for Xavorion modules."
* **Metadata:** Author: LM13 · Version 2.6.5 · `serverSideOnly=false`, `clientSideOnly=false`, `saveGameAltering=true` · Depends on: Avorion 2.0–2.5.*
* **Impacted Script Hooks:**
  * `data/scripts/Core/` — foundational class library (battery, cohort, decorator, ship/sector libs, RNG) — backbone for all Xavorion logic.
  * `data/scripts/SystemUpgrade/` + `Properties/` (Armor, Base, Carrier, Crew, Energy, Hardpoint, Shield, Warp) — reworks the **upgrade/system-module framework** and all per-stat property providers.
  * `data/scripts/GalaxyGenerator/` + `Properties/` — hooks **procedural galaxy/sector generation** (tier, tech level, size, nebula, distribution).
  * `data/scripts/ShipXAI/` (Plugins, States, UI) — extensible **ship AI** state machine replacing/augmenting base AI behavior.
  * `data/scripts/Encyclopedia/` — extends the in-game **encyclopedia** system.
  * `data/scripts/entity/init.lua`, `entity/orderchain.lua`, `player/init.lua`, `sector/init.lua` — global **entity/player/sector init hooks**.
  * `data/scripts/sector/background/economyupdater.lua` — overrides the **background economy tick**.

### AzimuthLib - Library for modders (Folder: 1722652757)

* **Developer Description:** "A resource for modders that provides functions to make mod development easier. Mostly used in Rinart73 mods."
* **Metadata:** Author: Rinart73 · Version 1.5.1 · `serverSideOnly=false`, `clientSideOnly=false`, `saveGameAltering=false` · Depends on: Avorion 0.31+ · Contact: rinart73@gmail.com
* **Impacted Script Hooks:**
  * `data/scripts/lib/azimuthlib-basic.lua`, `azimuthlib-customstats.lua`, `azimuthlib-customtabbedwindow.lua`, `azimuthlib-uicollection.lua`, `azimuthlib-uicolorpicker.lua`, `azimuthlib-uiproportionalsplitter.lua`, `azimuthlib-uirectangle.lua`, `azimuthlib-utf8*.lua` — pure **library code** (config I/O, UTF8, custom UI widgets). No base-game loop is overridden directly; provides shared functions to dependent mods (e.g. Resource Display).

---

### B. Xavorion / XSF Overhaul Suite (LM13)

> All modules in this section declare `saveGameAltering=true` and depend on the eXtended Scripting Framework (`2918443067`).

### Xavorion: eXtended Avorion (Folder: 2923179923)

* **Developer Description:** "Galaxy is more diverse and dangerous. Resources and technology can be found almost anywhere, though the center of galaxy still holds the best of it."
* **Metadata:** Author: LM13 · Version 2.5.3 · `saveGameAltering=true` · Depends on: `2918443067` (≥2.3.9), Avorion 2.0–2.5.* · Declares incompatibility with 7 other mods (e.g. `1821043731`, `2914020453`).
* **Impacted Script Hooks:** (170 Lua scripts)
  * `data/scripts/GalaxyGenerator/Properties/` (Base, Distribution, Galaxy, Scaling) — overrides **material/weapon/rarity distribution, ship durability/volume/damage scaling, nebula** across the galaxy.
  * `data/scripts/lib/shipgenerator.lua`, `pirategenerator.lua`, `asyncshipgenerator.lua`, `sectorturretgenerator.lua`, `upgradegenerator.lua`, `waveutility.lua` — replaces core **ship/pirate/turret/upgrade generation** libraries.
  * `data/scripts/entity/merchants/` (turretmerchant, fighterfactory, equipmentdock, resourcetrader, torpedomerchant, buildingknowledgemerchant…) — **trading/NPC station behavior**.
  * `data/scripts/server/factions.lua`, `galaxy/server.lua` — **server-side faction & galaxy seeding**.
  * `data/scripts/Encyclopedia/` (Category, LEGACY) — large **encyclopedia** content rewrite.
  * `data/scripts/GalaxyScanner/`, `SectorScanner/` — galaxy/sector scanning UI & logic.

### XSF: Sector Generator (Folder: 2992808561)

* **Developer Description:** "Advanced replacement for vanilla sector generator."
* **Metadata:** Author: LM13 · Version 2.6.5 · `saveGameAltering=true` · Depends on: `2918443067`, `2923179923`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (59 Lua)
  * `data/scripts/GalaxyGenerator/SectorProperties.lua` + `Properties/TurretMerchant/`, `Properties/UpgradeMerchant/` — **sector composition & merchant stock generation**.
  * `data/scripts/StationDatabase/` (StationClass, StationDatabase, `Stations/Vanilla*`) — **station type registry** replacing vanilla station definitions.
  * `data/scripts/Merchant/` (Combat/Defense/Mining/Salvaging/Scrap/Missile turrets & upgrades, templates) — **merchant shop inventories**.
  * `data/scripts/lib/SectorGenerator.lua`, `asteroidfieldgenerator.lua`, `factorymap.lua`, `consumergoods.lua` — **sector & economy generation** libs.
  * `data/scripts/sector/background/rebuildstations.lua`, `respawndefenders.lua`, `respawnresourceasteroids.lua` — **background sector maintenance** loops.

### XSF: Fleet Generator (Folder: 2992808472)

* **Developer Description:** "Advanced replacement for vanilla spawn system."
* **Metadata:** Author: LM13 · Version 2.6.6 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (56 Lua)
  * `data/scripts/FleetGenerator/` — `Stages/FGS_*` (spawn pipeline: role/loadout/material/plan select, add turrets/fighters/torpedos, validate), `Selectors/`, `Loadouts/`, `Composers/`, `Lib/ShipRoleDatabase.lua` — the full **fleet-spawn pipeline**.
  * `data/scripts/GalaxyGenerator/Properties/Scaling/SP_Scaling{DPS,TTK,STK,Damage}.lua`, `SP_MaxFleetsToSpawn.lua`, `SP_ShipSpawnLimit.lua` — **encounter difficulty/scaling math**.
  * `data/scripts/entity/ai/mineNPC.lua`, `harvestNPC.lua` — **NPC economic AI**.
  * `data/scripts/lib/factionpacks.lua`, `plangenerator.lua`, `shiputility.lua` — ship-plan & faction libs.

### XSF: Arms Generator (Folder: 2992808396)

* **Developer Description:** "Advanced replacement for vanilla turret generator."
* **Metadata:** Author: LM13 · Version 2.5.3 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (30 Lua)
  * `data/scripts/ArmsGenerator/` — `BarrelFunctions/`, `MaterialFunctions/`, `RarityFunctions/`, `TechFunctions/`, `CoolingFunction.lua`, provider classes — the **procedural turret stat engine**.
  * `data/scripts/lib/weapongenerator.lua`, `turretgenerator.lua`, `weapontype.lua`, `weapontypeutility.lua`, `inventoryitemprice.lua` — replaces **core weapon generation & pricing** libs.
  * `data/scripts/lib/fightergenerator.lua`, `sectorfightergenerator.lua`, `sectorturretgenerator.lua` — **fighter/sector turret generation**.
  * `data/scripts/TooltipMaker/`, `TurretsDatabase/` — turret tooltip rendering & database template.

### Xavorion: Weaponry (Folder: 2992809109)

* **Developer Description:** "Complete weapons overhaul for Xavorion."
* **Metadata:** Author: LM13 · Version 2.6.5 · `saveGameAltering=true` · Depends on: `2918443067`, `2923179923`, `2992808396`; optional `2992808561`/`2992808472`; Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (88 Lua, 43 `.wav`)
  * `data/scripts/TurretsDatabase/` (CombatArtillery, Blasters, Disruptors, Lasers, Launchers, Machineguns, ProtonTorpedos, Railguns, Defense, ReconstructionLasers) — **weapon type definitions**.
  * `data/scripts/ArmsGenerator/{Barrel,Material,Rarity,Tech}Functions/` — per-weapon **generation behavior**.
  * `data/scripts/weaponsounds/` (ac, eh, epg, hpe, lrm, machinegun, ppg, ril, srm, submachinegun, zap) + `data/sfx/weapon/` — **weapon fire behavior/SFX**.
  * `data/scripts/lib/torpedogenerator.lua`, `torpedoutility.lua`, `weapontype.lua` — torpedo/weapon libs.
  * `data/scripts/systems/fightersquadsystem.lua`, `shieldbooster.lua` — **ship system components**.
  * `data/scripts/entity/merchants/turretfactory.lua`, `fighterfactory.lua`; `server/factions.lua` — crafting stations & faction seeding.

### Xavorion: Sectors (Folder: 2992809240)

* **Developer Description:** "Extension to Galaxy generator, adding more variety to Sectors."
* **Metadata:** Author: LM13 · Version 2.5.2 · `saveGameAltering=true` · Depends on: `2918443067`, `2923179923`, `2992808561`; optional `2992808396`/`2992809109`/`1695671502`; Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (87 Lua)
  * `data/scripts/sectors/` (~36 templates: asteroidfield, colony, factoryfield, gates, neutralzone, piratestation, smugglerhideout, worldboss, xsotanbreeders, riftinvasionbase…) — **sector-type content generation**.
  * `data/scripts/Economy/` (EconomyGoods, EconomyLibrary, EconomyBlacklist) + `lib/productions.lua`, `productionsindex.lua`, `tradingmanager.lua`, `tradingutility.lua`, `shop.lua`, `factorypredictor.lua` — **economy/trade rules & production chains**.
  * `data/scripts/entity/merchants/` (shipyard, shipyardAdvanced/Extended, tradingpost, scrapyard, repairdock, travelhub, LocalTradeShip) — **station behavior**.
  * `data/scripts/Simulation/Function/Adapt{Economy,Population,Devastation,AsteroidBelt}.lua` — **background sector simulation**.
  * `data/scripts/player/missions/` (delivery, exploresector, FederalDelivery) — **mission content**.
  * `data/scripts/systems/valuablesdetector.lua` — ship system.

### Xavorion: Mining (Folder: 2992809036)

* **Developer Description:** "Mining rebalance for Xavorion."
* **Metadata:** Author: LM13 · Version 2.5.3 · `saveGameAltering=true` · Depends on: `2918443067`, `2992808396`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (17 Lua)
  * `data/scripts/entity/ai/mine.lua`, `harvest.lua`, `salvage.lua` — **mining/harvest/salvage AI behavior**.
  * `data/scripts/HarvestSimulation/HarvestSim.lua` — **background harvest simulation** math.
  * `data/scripts/player/background/simulation/minecommand.lua`, `salvagecommand.lua` — **automated fleet mine/salvage orders**.
  * `data/scripts/ArmsGenerator/{Barrel,Material,Tech}Functions/*Mining*|*Salvaging*` + `TurretsDatabase/MiningTurrets.lua` — **mining/salvage turret generation**.

### Xavorion: Formations (Folder: 2992808903)

* **Developer Description:** "Replacement for Escort command. Adds simple formation flight to game."
* **Metadata:** Author: LM13 · Version 2.5.3 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (21 Lua)
  * `data/scripts/Formation/` (FormationClass, FormationDatabase, FormationSelector) — **formation definitions**.
  * `data/scripts/Orders/OrderController.lua`, `OrderHUD.lua`; `entity/orderchain.lua` — replaces the **fleet order/escort command** system.
  * `data/scripts/ShipXAI/States/` (NPCFlyFormation, NPCRegroup, NPCLostLeader, XAIFlyFormation, XAIRegroup, XAIFleetWarp, XAIFlee…) + `Plugins/FormationFlight.lua` — **formation flight AI states**.
  * `data/scripts/entity/ai/flythroughgate.lua` — gate-transit navigation override.

### Xavorion: Flight Physics (Folder: 2992808843)

* **Developer Description:** "Addition to vanilla flight, with collision prevention."
* **Metadata:** Author: LM13 · Version 2.5.3 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (12 Lua)
  * `data/scripts/ShipXAI/States/XAIHardTurn.lua`, `XAISprint.lua` + `Plugins/SmoothControlUnit.lua` — **AI flight maneuvering & collision avoidance**.
  * `data/scripts/GalaxyGenerator/Properties/Scaling/SP_AI{Acceleration,BoostAcceleration,Boost,Speed}Cap.lua`, `SP_AITechLevel*.lua` — **NPC flight-performance caps** by tech level.

### Xavorion: Encounters (Folder: 2992809187)

* **Developer Description:** "Overhaul of spawn system, replacing vanilla encounters with fleets of varied sizes, roles and loadouts."
* **Metadata:** Author: LM13 · Version 2.6.5 · `saveGameAltering=true` · Depends on: `2918443067`, `2992808472`; optional `2207469437`; Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (86 Lua)
  * `data/scripts/FleetGenerator/Composers/` (Boss, Brigade, Fleet, Squad, Military, Persecutor, Defender, Mission, Debug) — **encounter fleet composition** by difficulty/role.
  * `data/scripts/events/pirateattack.lua`, `traderattackedbypirates.lua`, `events/waveencounters/` (pirateking, mothershipwaves, pirateambush, treasure hunts…) — **dynamic event & wave encounters**.
  * `data/scripts/sector/factionwar/initfactionwar.lua`, `factionwarbattle.lua` — **faction war** logic.
  * `data/scripts/sector/background/spawnpersecutors.lua`, `spawnbehemoth.lua`; `galaxy/behemothevent.lua` — **persecutor/behemoth spawning**.
  * `data/scripts/player/events/` (alienattack, headhunter, distress signals) + `player/missions/` (bountyhunt, clearpiratesector, freeslaves, settlertreck…) — **player event/mission content**.
  * `data/scripts/lib/story/xsotan.lua`, `pirategenerator.lua`, `shipgenerator.lua`, `waveutility.lua` — spawn libs.

### Xavorion: Docking (Folder: 2992808719)

* **Developer Description:** "Minor tweak to Docking range. Extends to rougly match tractor beams."
* **Metadata:** Author: LM13 · Version 2.5.3 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.9.*
* **Impacted Script Hooks:** (8 Lua)
  * `data/scripts/entity/ai/dock.lua` — **docking behavior/range**.
  * `data/scripts/entity/merchants/repairdock.lua`, `entity/transfercrewgoods.lua` — dock station interaction.
  * `data/scripts/lib/tradingmanager.lua`, `lib/player.lua`; `player/missions/delivery.lua`, `organizegoods.lua` — trade/mission support.
  * `data/scripts/Config/DockingModule.lua` — module config.

### Xavorion: Combat AI (Folder: 2992808971)

* **Developer Description:** "Combat AI extension for NPC and Player ships. Includes some QoL improvements for RTS and TPP combat."
* **Metadata:** Author: LM13 · Version 2.6.5 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (11 Lua)
  * `data/scripts/ShipXAI/Plugins/CombatAI.lua` + `States/` (NPCAggressive, NPCSmartAttack, XAIFindTarget, XAIMoveAttack, XAISmartAttack, XAIAggressive) — **NPC & player combat AI** targeting/maneuver states.
  * `data/scripts/CombatHUD/CombatHUD.lua`; `player/init.lua` — **RTS/TPP combat HUD** QoL.

### Xavorion: Class Upgrades (Folder: 3165545472)

* **Developer Description:** "Rework of Vanilla and eXtended upgrades. Extends class system, combat and progression with non-random upgrades that allow building role-based ships."
* **Metadata:** Author: LM13 · Version 2.6.3 · `saveGameAltering=true` · Depends on the full XSF suite (`2918443067`, `2992808396`, `2992808472`, `2992808561`, `2923179923`, `2992809240`, `2992809109`, `2992808773`, `2992809187`); optional `2559654045`; Avorion 2.0–2.9.9
* **Impacted Script Hooks:** (125 Lua)
  * `data/scripts/systems/` — full **ship subsystem rework**: TCS variants (military/civil/auto/arbitrary + L/M sizes), boosters (battery/energy/engine/hyperspace/shield/radar/scanner/lootrange), `defensesystem`, `resistancesystem`, `weaknesssystem`, `shieldimpenetrator`, `energytoshieldconverter`, `velocitybypass`, `miningsystem`, `tradingoverview`, `transportersoftware`, `valuablesdetector`, `overchargemodule`, `torpedomod`.
  * `data/scripts/SystemUpgrade/Properties/Torpedo/UP_Torpedo*.lua`, `Properties/Perk/UP_EngineerPerk.lua` — **upgrade stat providers** (torpedo damage/range/velocity/split, perks).
  * `data/scripts/GalaxyGenerator/Properties/MerchantClass{Turrets,Upgrades}/`, `TurretMerchant/`, `UpgradeMerchant/` + `Merchant/` — **merchant upgrade/turret stock**.
  * `data/scripts/sectors/` (colony, factoryfield, gates, neutralzone, piratestation…) — sector overrides; `Simulation/Function/AdaptEconomy.lua` — economy sim.
  * `data/scripts/lib/weapongenerator.lua`, `upgradegenerator.lua`, `buildpermit.lua` — generation libs.

### Xavorion: Class System (Folder: 2992808773)

* **Developer Description:** "Extension to flight model, build mode and general progression of ships."
* **Metadata:** Author: LM13 · Version 2.5.2 · `saveGameAltering=true` · Depends on: `2918443067`, Avorion 2.0–2.5.*
* **Impacted Script Hooks:** (40 Lua)
  * `data/scripts/ShipBalancer/` (BalancerComponent, DroneBalancer, Lib/ShipStats, ShipsDatabase, BalancerAPI) — **ship class/stat balancing engine**.
  * `data/scripts/BuildModeUI/` (BuildModeUI, ShipClassWidget, ShipStatsWidget, Views) — **build-mode UI & class display**.
  * `data/scripts/systems/classmod.lua`, `coresubsystem.lua`, `enginebooster.lua`, `overchargemodule.lua`, `velocitybypass.lua`, `weaknesssystem.lua` — **class/flight ship systems**.
  * `data/scripts/SystemUpgrade/Properties/ClassSystem/UP_{Acceleration,Pitch,Roll,Yaw,Strafing,Velocity,ArcFlightBoost}Power.lua`, `Properties/Overcharge/` — **flight-model upgrade stats**.
  * `data/scripts/entity/startbuilding.lua`, `stationfounder.lua`; `ShipXAI/Plugins/ClassSystem.lua`, `EnergySubsystem.lua` — build/AI hooks.

### Xavorion: Starter Ship (Folder: 2992808642)

* **Developer Description:** "Starter Ship module for Xavorion. Ship included. Allows to use other ships."
* **Metadata:** Author: LM13 · Version 2.4.2 · `saveGameAltering=true` · Depends on: Avorion 2.0–2.9.9
* **Impacted Script Hooks:** (4 Lua, 4 XML)
  * `data/scripts/galaxy/server.lua` — **new-game/galaxy server hook** for starting ship.
  * `data/scripts/StarterShip/StarterShipModule.lua`, `StarterShips.lua`; `player/init.lua` — **starter-ship selection** logic.
  * `data/plans/StarterShipModule/*.xml` — bundled starter-ship blueprints (logic-driven, not standalone designs).

---

### C. Standalone Gameplay & Server-Side Mods

### Laserzwei's simple asteroid respawn mod (Folder: 1692998037)

* **Developer Description:** "This mod simplyfies the vanilla asteroid respawing mechanic and extends it for live updates."
* **Metadata:** Author: Laserzwei · Version 1.2 · **`serverSideOnly=true`**, `saveGameAltering=false` · Depends on: Avorion 0.23.*–2.5.* · Contact: lasernr2@gmail.com
* **Impacted Script Hooks:**
  * `data/scripts/sector/background/respawnresourceasteroids.lua` + `sector/respawnresourceasteroids.lua` — overrides the **background resource-asteroid respawn loop**.
  * `data/config/simpleasteroidRespawn.lua` — respawn configuration.

### More Resources Mod (Folder: 1819452708)

* **Developer Description:** "Version 3.1.  Changes more asteroids into resource asteroirds.  It does not change the availability of resource types."
* **Metadata:** Author: Deathreel · Version 3.1 · `saveGameAltering=false` · Depends on: Avorion 0.23–10.0 · Contact: JayHallid@gmail.com
* **Impacted Script Hooks:**
  * `data/scripts/lib/asteroidfieldgenerator.lua` — overrides **asteroid-field generation** to raise the resource-asteroid ratio.

### Laserzwei's Advanced Shipyard (Folder: 1695671502)

* **Developer Description:** "This mod extends vanilla shipyards to produce custom-made ships."
* **Metadata:** Author: Laserzwei · Version 1.19.2 · `saveGameAltering=false` · Depends on: Avorion 2.0.*–2.5.* · Contact: lasernr2@gmail.com
* **Impacted Script Hooks:**
  * `data/scripts/entity/merchants/shipyard.lua` — extends **shipyard station** to build custom blueprints.
  * `data/scripts/entity/timedFactionTransferer.lua`, `player/changeOwner.lua`, `commands/changeOwner.lua` — **ownership transfer** of produced ships.
  * `data/config/advshipyardconfig.lua` — configuration.

### [2.0] - (SDK) Rebalance - Static Founding Cost (Folder: 2109258268)

* **Developer Description:** "This Mod adds removes the very frustrating Founding cost which limits your ability to build an economy in the game."
* **Metadata:** Author: SDK · Version 1.0.1 · `saveGameAltering=true` · Depends on: Avorion 0.28–2.* · Contact: Discord "Shadow Doctor K#2203"
* **Impacted Script Hooks:**
  * `data/scripts/lib/shipfounding.lua` — overrides the **ship/station founding cost** formula to a static value.

### System Scanner Upgrade (Folder: 1751798934)

* **Developer Description:** "Adds the System Scanner Upgrade to the game."
* **Metadata:** Author: MassCraxx · Version 1.3 · `saveGameAltering=true` · Depends on: Avorion ≤2.*
* **Impacted Script Hooks:**
  * `data/scripts/systems/systemscanner.lua` — adds a **new ship system module** (System Scanner).
  * `data/scripts/lib/upgradegenerator.lua` — extends **upgrade generation** so the new module can spawn as loot/stock.

---

### D. UI & Quality-of-Life

### Resource Display (Folder: 1769379152)

* **Developer Description:** "Always displays player resources."
* **Metadata:** Author: Rinart73 · Version 1.1.2 · **`clientSideOnly=true`**, `saveGameAltering=false` · Depends on: `1722652757` (AzimuthLib ≥1.5), Avorion 0.29+ · Contact: rinart73@gmail.com
* **Impacted Script Hooks:**
  * `data/scripts/player/client/musiccoordinator.lua` — hooks the **client HUD/update loop** to persistently render player resources.

### Detailed Turret Tooltips (Folder: 1751636748)

* **Developer Description:** "Displays more detailed turret information like hull dps and shield dps per slot."
* **Metadata:** Authors: lyravega, MrMors, MassCraxx, Mp70 · Version 4.3 · **`clientSideOnly=true`**, `saveGameAltering=false` · Depends on: optional `1821043731`, Avorion ≤2.* · Contact: MassCraxx
* **Impacted Script Hooks:**
  * `data/scripts/lib/tooltipmaker.lua` — overrides **turret tooltip generation** to add hull-DPS/shield-DPS-per-slot fields.

### Blueprint Stat Compare (Folder: 3741814524)

* **Developer Description:** "Browse your saved and workshop ship designs and compare their stats side by side, useful when trying to figure out which ship will work best for your next adventure. UI/quality-of-life mod. In multiplayer, the server needs the mod installed."
* **Metadata:** Author: SuurflieG · Version 1.1 · `clientSideOnly=false`, `saveGameAltering=false` · Depends on: Avorion 2.0–2.5.13
* **Impacted Script Hooks:**
  * `data/scripts/player/ui/blueprintcompare.lua` + `player/init.lua` — adds a **blueprint browser/comparison UI** window.

### Trade Heatmap Alliance ship fix (Folder: 3739343155)

* **Developer Description:** "THIS MOD IS NOT ACTIVELY MAINTAINED. This mod fixes a bug in the base game where the trading system is not able to be detected on alliance ships. With this mod, you can use the trading heatmap in the galaxy map and the trading overview in normal space."
* **Metadata:** Author: CobaltStorm · Version 1.0 · `clientSideOnly=false`, `saveGameAltering=false` · Depends on: Avorion ≤2.5.13
* **Impacted Script Hooks:**
  * `data/scripts/player/map/economyinfo.lua` — patches the **galaxy-map trade heatmap / trading overview** to detect the trading system on alliance ships.

---

## Appendix: Xavorion / XSF Suite Load Order

The LM13 suite is strongly interdependent. Derived from the `dependencies` blocks, the effective load order is:

```
2918443067  eXtended Scripting Framework   (base — no XSF deps)
   └─ 2923179923  eXtended Avorion          (galaxy/economy core)
   └─ 2992808396  XSF: Arms Generator
   └─ 2992808472  XSF: Fleet Generator
   └─ 2992808561  XSF: Sector Generator     (needs Arms + eXtended Avorion)
        └─ 2992809240  Xavorion: Sectors
        └─ 2992809109  Xavorion: Weaponry
        └─ 2992809187  Xavorion: Encounters (needs Fleet Generator)
        └─ 2992809036  Xavorion: Mining
        └─ 2992808903  Xavorion: Formations
        └─ 2992808843  Xavorion: Flight Physics
        └─ 2992808719  Xavorion: Docking
        └─ 2992808971  Xavorion: Combat AI
        └─ 2992808773  Xavorion: Class System
             └─ 3165545472  Xavorion: Class Upgrades  (depends on the entire suite above)
2992808642  Xavorion: Starter Ship          (independent; Avorion-only dependency)
```

> AzimuthLib (`1722652757`) is an independent library consumed by Resource Display (`1769379152`) and is unrelated to the XSF dependency chain.
