<!-- Mod documentation. Code lineage (kept out of the reader-facing text on purpose):
     "Avorion Mods/2992809187/" (Xavorion: Encounters, v2.6.5; modinfo: serverSideOnly=false,
     clientSideOnly=false, saveGameAltering=true; deps 2918443067/2992808472 min 2.3.9, optional
     2207469437 (KH-ESCC, KnifeHeart's Extra Ship Classes Core), Avorion 2.0–2.5.*) — modinfo.lua;
     data/scripts/FleetGenerator/Lib/{AdaptiveComposerClass,CompositorPlugins,DebugComposerClass,
     ShipRoleDatabase,ShipTypeScripts}.lua (Composer prototype chain, Run() pipeline: ScaleMarker →
     ClassOffsetScaling FuzzyPick → SpawnTokens[max 12] → WingmenTokens → BossChance roll → role-table
     FuzzyPick); Composers/{BaseSquad,BaseFleet,BaseBrigade,BrigadeCore}.lua (Squad M1–M3/Fleet M3–M6/
     Brigade M4–M7 class bands); Composers/Squad/*.lua, Composers/Fleet/*.lua, Composers/Brigade/*.lua
     (Easy_/Medium_/Hard_ presets, SectorClassScaling[M1..M8], TechMin/TechMax gates); Composers/Debug/
     Debug_M1.lua…Debug_M8.lua (DebugComposerClass fixed-class test ladder); Composers/Defender/
     DefenderPatrol.lua, Composers/Military/MilitaryFleet.lua (faction Defender/Military patrols, not
     pirates); Composers/Persecutor/PersecutorSquad.lua (registered in CompositorPlugins.lua but no
     live caller found in this mod's own files); Composers/Boss/Boss_BountyHunt.lua, Composers/Mission/
     Mission_TransferVessel(Escort).lua, Composers/FakeFighters/Easy_Scouts.lua (all bEnabled=false,
     inert unless toggled externally); events/waveencounters/{mothershipwaves,pirateambushpreparation,
     pirateinitiation,pirateking,piratemeeting,pirateprovocation,pirateshidingtreasures,
     piratestationwaves,piratestreasurehunt,piratetraitorwaves,pirateasteroidwaves,
     tradersambushedwaves}.lua (override vanilla data/scripts/events/waveencounters/*; fakestashwaves.lua/
     hiddentreasurewaves.lua/respawnwaveencounters.lua left untouched/vanilla); player/missions/
     clearpiratesector.lua (SelectWaveEncounter() 10-entry pool), investigatemissingfreighters.lua
     (50% wave-encounter chance else entity/PirateBackup.lua fallback), bountyhuntmission.lua,
     transfervessel.lua, settlertreck/settlertreck.lua (disabled), freeslaves.lua (disabled),
     tutorials/strategymodetutorial.lua; entity/PirateBackup.lua (new file, no vanilla counterpart;
     15%-durability damage threshold, 3 scaled pirates, 180s cooldown); sector/background/
     spawnpersecutors.lua (overrides vanilla; entire SpawnPersecutors.update() body commented out —
     ambient "you're under-gunned" persecutor spawning disabled); player/events/headhunter.lua
     (overrides vanilla; entire HeadHunter.createEnemies() body commented out — reputation-triggered
     bounty hunters disabled); sector/factionwar/{initfactionwar,factionwarbattle}.lua (overrides
     vanilla; disabled); events/pirateattack.lua, traderattackedbypirates.lua, sectors/piratefight.lua,
     entity/events/piratesattackentity.lua (overrides vanilla; disabled); lib/story/xsotan.lua
     (overrides vanilla; body commented out, single live comment confirms Xsotan intentionally left on
     vanilla weapons); sector/background/spawnbehemoth.lua (overrides vanilla createBehemoth() +
     makeRailgunTurret(); CoreModule.IsEnabled("X2-Weaponry") gate swaps the boss's railgun for one of
     five Xavorion: Weaponry capstone archetypes — WeaponType.BigBang/SoulRipper/Deathray/Zeus/Rainfire
     — reach forced to 60km); galaxy/behemothevent.lua (overrides vanilla update(); engagement window
     data.countDown changed from vanilla's 20*60 to 120*60 — comment still reads "20 minutes", code is
     2 hours); Core/AICarrierComponent.lua (fake escort squad for hangar-less AI carriers); Core/
     ShipLibrary.lua, Config/CoreModule.lua (KH-ESCC optional role registry: Civilian Transport, Light/
     Heavy Defender, Heavy Carrier, AWACS, Scout, plus KH pirate roles Jammer/Stinger/Scorcher/Bomber/
     Sinner/Prowler/Pillager/Devastator/Executioner). Image assets: see wiki/ASSETS.md. -->
# Xavorion: Encounters

**Xavorion: Encounters** (by **LM13**) is *"an overhaul of the spawn system, replacing vanilla encounters
with fleets of varied sizes, roles and loadouts."* Its real contribution is a new **fleet-composition
engine** — the **FleetGenerator** — that builds named NPC squads, fleets and brigades out of weighted role
tables instead of vanilla's looser random rolls. That engine then gets wired into the game by overriding a
long list of vanilla pirate-encounter, persecutor, headhunter, faction-war and Behemoth scripts.

> **In short:** most pirate squads, fleets and patrols you fight are now built from named **role-based
> presets** (Easy/Medium/Hard tiers of Squads, Fleets and Brigades) instead of vanilla's generic rolls, each
> with a small (~4%) chance of a **named boss** taking the lead. A few vanilla nuisances get switched
> **off** entirely — the "you're under-gunned" persecutor spawner and the reputation-triggered headhunter
> event no longer fire. The galaxy-wide **Behemoth** boss event survives and gets buffed (its kill window
> goes from 20 minutes to **2 hours**), and if you also run **Xavorion: Weaponry**, the Behemoth's railgun is
> swapped for one of that mod's five named capstone weapons. A handful of side missions (Bounty Hunt, Clear
> Pirate Sector, Investigate Missing Freighters, Transfer Vessel) are rebuilt on top of the new engine too.
> Notably, **Faction War is shipped fully disabled** in this version — the files exist but do nothing.

## The FleetGenerator: how a Composer builds a fleet

A **Composer** is the mod's term for a fleet-building preset — a small Lua object that runs a fixed pipeline
every time the game asks it for ships:

1. Compute a **ScaleMarker** from the target's durability/damage budget, the sector's class, and a global
   difficulty multiplier.
2. Pick a **class range** (M1–M8) by weighted lookup against the preset's own `ClassOffsetScaling` table.
3. Pick a **fleet size** ("SpawnTokens," capped at **12** ships) from a `BaseSizeScaling` curve.
4. Split that size into offensive vs. defensive **Wingmen** via a `WingmenScaling` curve.
5. Roll a small chance (almost universally **4%**, the preset's `BossChance`) for the Leader to become a
   **named boss** instead of a generic ship.
6. Fill the **Leader**, **Wingmen** and **Flank** slots by weighted pick against the preset's own role table.

Every preset also carries a **`SectorClassScaling[M1..M8]`** table — a per-sector-class difficulty
multiplier — so the same composer plays very differently in a starter sector than deep toward the core. A
`TechMin`/`TechMax` gate further restricts *when* a preset is even eligible to be picked.

### Squad, Fleet and Brigade are the same engine at different scales

There's no nesting — a Brigade isn't literally "several Squads" in code. The three families are the same
Composer machinery, just narrowed to different class bands and tuned with harsher scaling curves:

| Family | Class band | Difficulty curve | Examples |
|---|---|---|---|
| **Squad** | M1–M3 | Gentle | `Easy_FighterSquad`, `Medium_HunterSquad`, `Medium_DestroyerSquad`, `Hard_BomberSquad`, `Hard_AssassinSquad`, `Hard_RatSquad` |
| **Fleet** | M3–M6 | Moderate | `Easy_MissileFleet`, `Medium_DestroyerFleet`, `Medium_CarrierFleet`, `Hard_RatFleet`, `Hard_ArtilleryFleet` |
| **Brigade** | M4–M7 | Steep, tech-gated | `Easy_FighterBrigade` (Tech ≥20), `Medium_CarrierBrigade` (Tech ≥25), `Hard_AssaultBrigade` (Tech ≥40), `Hard_NemesisBrigade` (Tech ≥48) |

Brigades are deliberately suppressed at low sector classes (their `SectorClassScaling` at M1 sits as low as
**0.02–0.1**), so you essentially won't meet one outside high-tier space even if the roll is otherwise
favorable. **Hard_NemesisBrigade** is the hardest preset in the mod: its boss class is locked to **M8**, its
`BossDifficultyScale` is **15.0** (versus the usual 10.0), and its boss arrives with an **8-ship** escort.

> **Easy/Medium/Hard isn't just flavor text** — each tier ships its own `SectorClassScaling` curve. A
> `Medium_HunterSquad`, for instance, ramps from 0.5 at M1 up to 55.0 at M8, while the gentlest squads barely
> climb at all — so two squads with the same role mix can still feel very different in a fight.

### The boss "Easter Egg" roll

Any composer with a non-zero `BossChance` can replace its Leader with a **named elite**, drawn from a pool
of flavor titles: *Elite Pirate, Bandit Leader, Assassin Leader, Frigate Hunter, Rat Leader, Mercenary
Leader, Bounty Hunter, Pirate Commander, Artillery Commander, Destroyer Commander, Pirate Flagship,
Rebellion Commander, Nemesis, Carrier Commander, Pirate Mothership,* and — specific to the Persecutor
preset — **Headhunter** (a 15% chance there). A boss roll also forces **Naonite** hull material, flags the
ship to display its boss banner, and bumps its class up one tier above the rest of the fleet.

### Roles drawn on

Composers pick ships from a shared role vocabulary (`ShipRoleDatabase.lua`): **Fighter, Bomber,
BomberCarrier, Missile, Artillery, RocketArtillery, Hunter, Support, Destroyer, Assassin, Carrier,
Disruptor.** If you also run the optional companion mod **KnifeHeart's Extra Ship Classes Core**, the role
table widens further with faction-flavored types — `Civilian Transport`, `Light/Heavy Defender`, `Heavy
Carrier`, `AWACS`, `Scout`, plus the pirate-specific `Jammer`, `Stinger`, `Scorcher`, `Bomber`, `Sinner`,
`Prowler`, `Pillager`, `Devastator`, `Executioner` — but none of that appears without the companion mod
active.

Two composers step outside the pirate theme entirely: **DefenderPatrol** and **MilitaryFleet** build
*faction* defender/military patrols rather than pirate squads, and `MilitaryFleet` carries a fixed,
boss-free 4–10 ship size regardless of difficulty.

### What's defined but not actually wired up

A few composers exist in the files but are shipped with `bEnabled = false`, so nothing currently spawns
them unless something else flips that flag: **Boss_BountyHunt** (a 100%-boss-chance, zero-escort encounter
built around a `"???"`-named target), both **Mission_TransferVessel** composers, and **Easy_Scouts**
(`FakeFighters`). **PersecutorSquad** — the dedicated Assassin/Destroyer-heavy bounty-hunter preset whose
boss is the "Headhunter" — is registered in the composer plugin list, but no script in this mod actually
calls it; whichever system was meant to trigger it isn't present here.

## Wave encounters

A pool of ten named **wave encounters** can be attached to a pirate-themed sector by the
[Clear Pirate Sector](#missions-rebuilt-on-the-new-engine) mission (and a smaller subset by Investigate
Missing Freighters): **Mothership Waves, Pirate Ambush Preparation, Pirate Initiation, Pirate King, Pirate
Meeting, Pirate Provocation, Pirate's Hiding Treasures, Pirate Station Waves, Pirate's Treasure Hunt,** and
**Pirate Traitor Waves.** (Vanilla's `fakestashwaves`, `hiddentreasurewaves` and the asteroid-wave variant
are left in the selection pool's source but commented out, so they no longer come up.)

Most of these are thin, near-identical hooks: on spawn they call the shared `addEnemyBuffs` difficulty
scaling, tag the ships `is_wave`, and either sit **idle** (an ambush waiting to be provoked) or wander on a
peaceful patrol until something sets them off — the actual sector placement and narrative trigger live
outside this folder. Two encounters carry real, distinct logic:

- **Mothership Waves** — the boss ship spawns **invincible** and passive until the fight properly starts,
  guarantees a **Legendary turret drop** plus a full turret loadout from the wave generator, and drops a
  Building Knowledge item alongside it.
- **Pirate Traitor Waves** — spins up a brand-new one-off faction named *"\<Pirates\> Traitor,"* reassigns
  the spawned traitor ship to it, and sets every other ship in the wave to **attack the traitor** — a
  pirate-on-pirate skirmish you can sit back and let finish itself, or jump into.

## PirateBackup: reinforcements for attacked AI stations

A new script (no vanilla equivalent) that any AI-faction entity — mainly stations — can carry. It tracks
cumulative damage taken; once that total passes **15% of the entity's max durability**, and the owning
faction isn't already eradicated, it spawns **3 scaled pirate ships** as reinforcements near the station and
starts a **3-minute** cooldown before it can call in backup again. **Investigate Missing Freighters** uses
this as its fallback defense for the decoy pirate shipyard whenever that mission doesn't roll a full wave
encounter.

## The Behemoth: buffed engagement window, Xavorion-aware loadout

The galaxy-wide **Behemoth** world-boss event ([see Behemoth](Behemoth) for the vanilla version) keeps
running under this mod, with two concrete changes:

- **The kill window is quadrupled.** Vanilla gives you **20 minutes** to find and fight the Behemoth before
  it moves on; this mod's override changes the underlying countdown to **120 minutes (2 hours)** — the
  in-file comment still says "20 minutes," but the actual value the game runs on is 2 hours.
- **If Xavorion: Weaponry is also active, the boss's railgun changes.** The mod checks
  `CoreModule.IsEnabled("X2-Weaponry")`, and if true, builds the Behemoth's railgun turret from one of five
  Xavorion: Weaponry capstone archetypes — **AC-XLA "Big Bang," RX-IL "SoulRipper," RBE-X-C "Deathray,"
  ZAP-XLA "Zeus,"** or **LRM-X-A "Rainfire"** — picked at random, with its reach forced out to **60 km**.
  Without that companion mod installed, the Behemoth keeps its normal vanilla-style loadout.

Everything else about the Behemoth is untouched: the four directional bosses (North/East/South/West), the
escalating loot table (Legendary ×2 through Common ×14, mirrored across both system upgrades and turrets),
and the flat **750,000 effective firepower** normalization that keeps every Behemoth equally dangerous
regardless of its actual build.

## Missions rebuilt on the new engine

| Mission | What you do | Reward |
|---|---|---|
| **Bounty Hunt** | Track a named Renegade Leader (tied to a flavor pirate sub-faction) across sectors, fighting a mothership-style target plus 4–6 escorts spawned from a fresh hostile faction | ~10,000+ credits (scales with steps) · +7,000 relations · bonus build material |
| **Clear Pirate Sector** | Find a nearby pirate-themed sector; it spins up one of the ten wave encounters above, and you clear every `is_wave`/`is_pirate` ship in it | 50,000 credits × sector reward factor · +6,000 relations · bonus material |
| **Investigate Missing Freighters** | Pose as a freighter, get ambushed, and root out a hidden pirate shipyard defended by 3 pirates + 3 bandits and (50% chance) a wave encounter, otherwise PirateBackup reinforcements | 45,000 credits × reward factor · +7,500 relations |
| **Transfer Vessel** | Escort a civilian ship alongside a SecCorp escort squad | 50,000 credits × factor · +6,500 relations |
| **Strategy Mode Tutorial** | Onboarding mission: meet and recruit a unique named companion ship, "Lady Adventurous," loaded from her own ship plan | — |

**Free Slaves** and **Settler Trek** ship as mission files in this mod but have their bodies fully commented
out — they don't currently do anything beyond what the base game already provides.

## What this mod turns off

A meaningful chunk of the override list exists purely to **disable** a vanilla system rather than replace
it — the function bodies are still physically present in the files, wrapped in a Lua block comment, so they
ship but never run:

- **The ambient persecutor spawner** (`spawnpersecutors.lua`) — vanilla's "you're badly outgunned for this
  sector" hunt-you mechanic (see [Enemy AI → Persecutors](Enemy-AI#persecutors)) no longer fires.
- **The reputation headhunter event** (`headhunter.lua`) — vanilla's "you tanked your standing with a
  faction" bounty-hunter event no longer fires either.
- **Faction War** (`initfactionwar.lua`, `factionwarbattle.lua`) — the entire background system that would
  pit two AI factions into open war and spawn battle fleets between them is inert; it never triggers.
- A handful of generic pirate-attack hooks (`pirateattack.lua`, `traderattackedbypirates.lua`,
  `piratefight.lua`, `piratesattackentity.lua`) are likewise overridden into no-ops.

**The Xsotan are untouched.** `lib/story/xsotan.lua` is overridden too, but its only live content is a
comment explaining the alien faction was deliberately left alone: it still fights with vanilla weapons,
since folding it into the overhaul "would require a separate [rebalance]."

## See also

- [Enemy AI](Enemy-AI) – the vanilla NPC behaviour states (Patrol, Evade, Persecutor) this mod partially disables
- [Special enemies](Special-enemies) – wave scaling, world bosses, and the vanilla Persecutor/Behemoth spawners this mod overrides
- [Behemoth](Behemoth) – the vanilla Behemoth event this mod extends (engagement window, loot, signature upgrades)
- [Missions](Missions) – the vanilla repeatable mission catalog this mod's Bounty Hunt/Clear Pirate Sector/etc. sit alongside
- [Diplomacy and Reputation](Diplomacy-and-Reputation) – relation status and the War state Faction War would have driven, had it been enabled
- [Xavorion: Weaponry](Xavorion-Weaponry) – the sibling mod whose named capstone weapons the Behemoth borrows when both mods are active

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry) · [Xavorion: Mining](Xavorion-Mining) · [Xavorion: Class System](Xavorion-Class-System) · [Xavorion: Encounters](Xavorion-Encounters) · [Xavorion: Combat AI](Xavorion-Combat-AI)*
