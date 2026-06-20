<!-- Mod documentation. Sourced from "Avorion Mods/2992809109/" (Xavorion: Weaponry, v2.6.5) Lua:
     modinfo.lua; data/scripts/TurretsDatabase/Combat{Artillery,Blasters,Disruptors,Lasers,Launchers,
     Machineguns,ProtonTorpedos,Railguns}.lua; data/scripts/systems/{fightersquadsystem,shieldbooster}.lua;
     data/scripts/weaponsounds/*.lua. The damage model WeaponTTK.ToDamage and all stat scaling live in the
     companion mod XSF: Arms Generator (2992808396) — see that page. Formulas as monospace code blocks. -->
# Xavorion: Weaponry

**Xavorion: Weaponry** (Workshop ID `2992809109`, by **LM13**) is the *"complete weapons overhaul for
Xavorion"*. Where [XSF: Arms Generator](XSF-Arms-Generator) is the **engine** that scales turret stats,
this mod is the **content**: the turret database of named weapon archetypes, the fighter-squad and
shield-booster system modules, and the custom weapon-sound pools. Every turret here is generated through
the Arms Generator pipeline — barrel, material, rarity and tech scaling — so the values below are the
**M1-tech, Iron, base archetype** before that scaling is applied.

For how those base numbers are scaled up by tech/rarity/material and split into barrel variants, read
[XSF: Arms Generator](XSF-Arms-Generator) first. For vanilla weapon types and damage types, see
[Weapons](Weapons) and [Combat](Combat).

> **Mod metadata.** `version = "2.6.5"`, `serverSideOnly = false`, `clientSideOnly = false`,
> `saveGameAltering = true`. Dependencies: `2918443067`, `2923179923`, `2992808396` (all min `2.3.9`),
> optional `2992808561` / `2992808472`, and `Avorion` `2.0`–`2.5.*`.

## How to read the archetype tables

Each archetype declares its damage as a **Time-To-Kill** target, not a flat number:
`ShotDamage = WeaponTTK.ToDamage(TTK, vs, fireRate)` means *"sized to destroy a ship of class `vs` in
`TTK` seconds"*. The base per-shot damage works out to
`(Volume[vs] * 4 / TTK) / 5 / fireRate` (see [the TTK model](XSF-Arms-Generator#base-damage--the-time-to-kill-model)),
then multiplied by tech and rarity. Columns:

- **Class** – the ship class the turret is *intended for* (`TargetClass`); **vs** – the class its damage
  is *balanced to kill* (`CounterClass`).
- **Fire/s** – base `VolleyPerSecond`. **Range** is optimal reach; **Energy** is `EnergyPerSecond` where
  the weapon is energy-fed. **Reload** is `ReloadTime` in seconds; **Crew**/**Size**/**Slot** are the
  turret requirements. **Cool.** is the cooling model (see [XSF: Arms Generator](XSF-Arms-Generator#cooling-systems)).

Every archetype also generates in **Heavy / Medium / Burst / Gatling** barrel variants. Names ending
`NPC` are flagged NPC-only loadout weapons.

## Combat Artillery — Auto-Cannons

`WeaponTech.Cannon`, sound `"ac"`, **Heat** cooling, custom **AC** barrel/rarity scaling. All are
**flak** rounds (`bFlak`, `bImpactExplode`) with `ExplosionRadius 10` (125 on the Big Bang).

| Name | Class | vs | TTK | Fire/s | Acc | Range | Crew | Size | Slot | Reload | Price (Base→Max) |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **AC-3-C** | M3 | M4 | 8 | 0.75 | 0.96 | 28 km | 4 | 1.0 | 3 | 3 | 35k → 600k |
| **AC-4-A** | M4 | M3 | 5 | 1.5 | 0.88 | 22 km | 5 | 2.0 | 3 | 15 | 45k → 750k |
| **AC-5-C** | M5 | M5 | 10 | 0.95 | 0.96 | 35 km | 10 | 1.5 | 5 | 4 | 120k → 2M |
| **AC-6-A** | M6 | M6 | 15 | 0.85 | 0.96 | 40 km | 20 | 2.5 | 6 | 5 | 250k → 5M |
| **AC-7-A** | M7 | M7 | 15 | 0.75 | 0.96 | 50 km | 40 | 4.0 | 8 | 3 | 550k → 8M |
| **AC-XLA "Big Bang"** | M8 | M8 | 15 | 0.25 | 0.92 | 60 km | 100 | 6.0 | 10 | 60 | 1M → 20M |

> The **Big Bang** is the experimental tier: projectile size 5.0, `ExplosionRadius 125`.

## Combat Blasters — Plasma Guns

`WeaponTech.Blaster`, **Battery** cooling, `WeaponRecoil.None`, no flak. Projectile colour shifts by tier
(HSV hue 206° → 172°). The PPG line uses the default fire sound; HPE uses `"hpe"`.

| Name | Class | vs | TTK | Fire/s | Acc | Range | Energy | Crew | Size | Slot | Reload | Price |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **PPG-1-A** | M1 | M1 | 5 | 0.85 | 0.96 | 8 km | 25 MW | 0 | 0.5 | 1 | 3 | 1k → 40k |
| **PPG-2-A** | M2 | M2 | 11 | 0.8 | 0.95 | 10 km | 175 MW | 1 | 1.0 | 1 | 5 | 5k → 160k |
| **PPG-4-A** | M4 | M3 | 12 | 0.65 | 0.92 | 15 km | 500 MW | 2 | 1.0 | 1 | 7 | 25k → 320k |
| **PPG-5-A** | M5 | M4 | 18 | 0.6 | 0.91 | 18 km | 5 GW | 2 | 1.5 | 1 | 8 | 50k → 640k |
| **HPE-6-A** | M6 | M5 | 32 | 0.55 | 0.90 | 22 km | 12 GW | 4 | 1.5 | 2 | 12 | 120k → 2M |
| **HPE-7-A** | M7 | M6 | 60 | 0.5 | 0.88 | 30 km | 28 GW | 6 | 2.0 | 2 | 15 | 300k → 5M |

## Combat Disruptors — Zappers & EMP Guns

`DamageType.Electric` throughout. Two families: **Zappers** (`WeaponTech.EMP`, **Drain** cooling at the
extremes) and **EMP Guns** (`WeaponTech.Blaster` tech but Electric damage, **Battery** cooling). Damage
is boosted by an explicit multiplier on top of the TTK base.

| Name | Class | vs | Tech | TTK ×mult | Fire/s | Acc | Range | Energy | Crew | Size | Slot | Reload | Cool. | Sound |
|---|---|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| **ZAP-1-A** | M1 | M2 | EMP | 10 ×1.25 | 1.0 | 0.98 | 8 km | 100 MW | 0 | 0.5 | 1 | 3 | Drain | zap |
| **EEG-2-A** | M2 | M2 | Blaster | 5 ×1.75 | 1.25 | 0.95 | 8 km | 250 MW | 1 | 1.0 | 1 | 8 | Battery | ppg |
| **ZAP-5-A** | M5 | M5 | EMP | 5 ×1.25 | 1.0 | 0.95 | 8 km | 10 GW | 6 | 2.0 | 3 | 12 | Battery | zap |
| **EEG-7-A** | M7 | M6 | Blaster | 12 ×1.75 | 1.0 | 0.90 | 28 km | 20 GW | 10 | 2.0 | 2 | 15 | Battery | ppg |
| **ZAP-XLA "Zeus"** | M8 | M7 | EMP | 8 ×1.0 | 0.5 | 0.95 | 30 km | 350 GW | 100 | 5.0 | 10 | 30 | Drain | zap |

> A disabled **EC-4-A "Flak"** EMP cannon (`WeaponTech.EMPCannon`, `ExplosionRadius 150`) is present in
> the source but commented out, so it is not generated.

## Combat Lasers

`WeaponTech.Laser` (or `PulseLaser`), **Battery** cooling, `WeaponRecoil.None`. The whole line overrides
the damage multipliers to `TechDamageMult = 3.0, RarityDamageMult = 1.5` and uses **RBE** scaling. In
**Burst** and **Gatling** barrels the laser becomes a **Pulse-Laser**.

| Name | Class | vs | Tech | TTK | Fire/s | Acc | Range | Energy | Crew | Size | Slot | Reload | Price |
|---|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **P-RBE-1-C** | M1 | M1 | Pulse | 0.33 | 3.0 | 0.98 | 5 km | 0.5 GW | 0 | 0.5 | 1 | 4 | 1.2k → 162k |
| **P-RBE-1-C** *(NPC)* | M1 | M1 | Pulse | 0.33 | 3.0 | 0.98 | 8 km | 0.5 GW | 0 | 0.5 | 1 | 4 | 1.2k → 162k |
| **RBE-3-A** | M3 | M3 | Laser | 1.0 | 3.0 | 0.98 | 6.5 km | 5 GW | 6 | 1.5 | 2 | 10 | 45k → 800k |
| **RBE-5-A** | M5 | M5 | Laser | 2.0 | 2.5 | 0.98 | 7.5 km | 50 GW | 60 | 2.0 | 4 | 20 | 150k → 4M |
| **RBE-7-A** | M7 | M6 | Laser | 2.67 | 2.0 | 0.98 | 8.5 km | 250 GW | 100 | 4.0 | 6 | 30 | 350k → 8M |
| **RBE-X-C "Deathray"** | M8 | M7 | Laser | 1.0 | 1.0 | 0.98 | 16 km | 1000 GW | 1000 | 6.0 | 16 | 60 | 1M → 20M |
| **RBE-X-C "Deathray"** *(NPC)* | M8 | M7 | Laser | 1.0 | 1.0 | 0.98 | 16 km | 0.01 GW | 1000 | 6.0 | 16 | 60 | 1M → 20M |

> The NPC Deathray is identical to the player one except its energy draw is a token `0.01 GW` so AI ships
> can fire it without an energy economy.

## Combat Launchers — Missiles

`WeaponTech.Launcher`, **Heat** cooling. Short-range (**SRM**) and long-range (**LRM**) missiles, with
seeking and flak behaviour varying by model.

| Name | Class | vs | TTK | Fire/s | Acc | Range | Crew | Size | Slot | Reload | Behaviour |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **SRM-1-GC** | M1 | M1 | 2 | 1.5 | 0.8 | 6 km | 0 | 0.5 | 1 | 5 | **Seeking**, coaxial |
| **SRM-3-C** | M3 | M3 | 5 | 1.4 | 0.9 | 10 km | 4 | 1.0 | 2 | 12 | **Flak**, expl. radius 10, coaxial |
| **SRM-5-A** | M5 | M4 | 5 | 1.25 | 0.9 | 14 km | 8 | 2.0 | 3 | 15 | **Flak**, expl. radius 10 |
| **LRM-6-GA** | M6 | M4 | 10 | 1.15 | 0.9 | 20 km | 15 | 2.5 | 4 | 25 | **Seeking + Flak**, expl. radius 10 |
| **LRM-X-A "Rainfire"** | M8 | M6 | 1 | 1.5 | 0.9 | 25 km | 100 | 5.0 | 8 | 30 | **Flak**, expl. radius 50, proj. size 5 |

## Combat Machineguns

`WeaponTech.Gun` (SMG/MG) and `WeaponTech.Bolter` (BMG), **Heat** cooling. The MG and bolters add a
damage and/or recoil multiplier; bolters are near-perfectly accurate and coaxial.

| Name | Class | vs | Tech | TTK | Fire/s | Acc | Range | Crew | Size | Slot | Reload | Sound | Notes |
|---|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| **SMG-1-A** | M1 | M1 | Gun | 4 | 2.5 | 0.96 | 6 km | 0 | 0.5 | 1 | 3 | submachinegun | tracking 2.6 |
| **MG-2-A** | M2 | M2 | Gun | 8 | 2.0 | 0.94 | 8 km | 1 | 1.0 | 1 | 3 | machinegun | damage ×1.3, recoil ×1.3 |
| **BMG-3-C** | M3 | M3 | Bolter | 5 | 1.5 | 0.99 | 6 km | 2 | 1.0 | 2 | 3 | flak | coaxial |
| **BMG-4-C** | M4 | M4 | Bolter | 5 | 1.5 | 0.99 | 8 km | 4 | 1.5 | 3 | 3 | flak | coaxial |

## Combat Railguns

`WeaponTech.Rail`, **Battery** cooling, sound `"ril"`, **RIL** scaling. All fire at a constant slow
`0.25` shots/s with `0.98` accuracy — the slow, hard-hitting precision line.

| Name | Class | vs | TTK | Fire/s | Acc | Range | Energy | Crew | Size | Slot | Reload | Price |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **R4-IL** | M4 | M3 | 1 | 0.25 | 0.98 | 8 km | 5 GW | 6 | 1.5 | 4 | 15 | 60k → 650k |
| **R6-IL** | M6 | M4 | 1 | 0.25 | 0.98 | 14 km | 25 GW | 16 | 3.0 | 6 | 25 | 240k → 5M |
| **R8-IL** | M7 | M5 | 1 | 0.25 | 0.98 | 18 km | 150 GW | 24 | 4.0 | 8 | 40 | 520k → 12M |
| **RX-IL "SoulRipper"** | M8 | M6 | 1 | 0.25 | 0.98 | 24 km | 500 GW | 100 | 6.0 | 10 | 60 | 1k → 20M |

## Combat Proton Torpedos

`WeaponTech.Torpedo`, `DamageType.AntiMatter`, **Battery** cooling, sound `"eh"`, Tesla projectile
appearance. All carry **block penetration 6** and a high **shield-penetration chance**, fire very slow
projectiles (≈0.1 km/s), and most are coaxial. Only the **Fighter** torpedo overrides the damage
multipliers (`TechDamageMult 9`, `RarityDamageMult 2.5`).

| Name | Class | vs | TTK | Fire/s | Acc | Range | ShieldPen | Expl. R | Crew | Size | Slot | Energy | Player? |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **NPC-Only-PTL-1** | M1 | M4 | 1 | 0.25 | 0.8 | 6 km | 1.0 | 1 | 0 | 1.0 | 2 | 0.01 GW | NPC |
| **F-PTL-2-C** *(Fighter)* | M2 | M2 | 1 | 0.5 | 0.8 | 6 km | 0.5 | — | 0 | 1.0 | 2 | 2.5 GW | Player |
| **NPC-Only-PTL-2** | M2 | M5 | 2 | 0.25 | 0.8 | 7 km | 1.0 | 2 | 2 | 1.5 | 4 | 0.01 GW | NPC |
| **PTL-3-C** | M3 | M5 | 1 | 1.0 | 0.8 | 6 km | 1.0 | 3 | 0 | 1.0 | 2 | 2.5 GW | Player |
| **NPC-Only-PTL-3** | M3 | M6 | 3 | 0.25 | 0.8 | 8 km | 1.0 | 3 | 2 | 1.5 | 4 | 0.01 GW | NPC |
| **X-PTL-3-C** | M4 | M7 | 4 | 1.0 | 0.8 | 22 km | 1.0 | 75 | 2 | 2.5 | 4 | 15 GW | Player |

> The player torpedoes' **barrel variants change behaviour dramatically**: e.g. PTL-3-C's Heavy barrel
> raises block penetration to 10 and adds a `250`-radius flak explosion, while Burst/Gatling trade
> penetration for tighter spreads — so the same torpedo plays very differently per barrel.

## Fighter squad system

`systems/fightersquadsystem.lua` overrides `getBonuses(seed, rarity, permanent)`. Squad count comes from
the vanilla `getNumSquads`; the **production** bonus is recomputed from rarity and two tunable galaxy
constants:

```
baseValue  = (rarity.value + 3) * GalaxyModule.FighterProductionMult
production  = max(0, lerp(rand(0,1), 0,1, baseValue-1, baseValue)) * 1000
production  = round(production / 100) * 100               -- snap to nearest 100
production  = production + GalaxyModule.FighterProductionReduction
```

Only **permanent** (installed) systems grant production; a temporary/loot copy returns `0`. The
multiplier and flat reduction (`GalaxyModule.FighterProductionMult` / `FighterProductionReduction`) are
defined in the suite's galaxy config, so production scales with rarity but is centrally tunable.

## Shield booster system

`systems/shieldbooster.lua` overrides `getBonuses` and `getEnergy` with an explicit **per-rarity table**
(the randomised vanilla durability roll is computed but then replaced by this fixed value):

| Rarity | Shield HP | Energy |
|---|--:|--:|
| **Petty** | 1,000 | 0.5 GW |
| **Common** | 2,500 | 1 GW |
| **Uncommon** | 5,000 | 4 GW |
| **Rare** | 15,000 | 8 GW |
| **Exceptional** | 50,000 | 24 GW |
| **Exotic** | 120,000 | 40 GW |
| **Legendary** | 500,000 | 80 GW |

Recharge percentage and the permanent/temporary modifiers:

```
recharge = 5 + (rarity.value * 2)               -- base 5%, +2% per rarity step
recharge = recharge + rand() * (rarity.value*2) -- randomised extra, span scales with rarity
recharge = (recharge * 0.8) / 100               -- damp, convert to fraction
if rand() < 0.5 then recharge = 0 end           -- 50% of rolls have NO recharge at all

if permanent:  recharge *= 1.5 ; durability unchanged ; emergencyRecharge = 1 if rarity.value <= 2
else        :  durability *= 0.5                -- temporary copies are half-strength

energy = table.Energy * (permanent and 1.0 or 0.6)
```

So a permanent booster keeps full shield HP and energy, gets a 1.5× recharge, and (only at Uncommon or
lower, `rarity.value ≤ 2`) qualifies for an **emergency recharge**; a temporary one is halved on
durability and energy.

## Weapon sounds

`weaponsounds/<id>.lua` each define a `WeaponSounds` table: a `sounds` pool, an audible `range` (metres)
and a `volume`. A weapon binds to one by setting `Sound = "<id>"`; the fire event then draws randomly
from that pool at the given range/volume. (Some weapons point at vanilla sounds like `"flak"` instead.)

| Sound id | Used by | Active variants | Range | Volume |
|---|---|--:|--:|--:|
| `ac` | Auto-cannons | 5 | 500 | 0.25 |
| `eh` | Proton torpedos | 5 | 3000 | 0.25 |
| `epg` | (EMP/plasma) | 1 | 400 | 0.12 |
| `hpe` | Heavy Plasma Emitter | 4 | 400 | 0.40 |
| `lrm` | Long-range missiles | 5 | 400 | 0.28 |
| `machinegun` | Machinegun | 5 (`ar1–5`) | 400 | 0.18 |
| `ppg` | Plasma / EMP guns | 4 | 400 | 0.12 |
| `ril` | Railguns | 1 | 400 | 0.25 |
| `srm` | Short-range missiles | 5 | 400 | 0.15 |
| `submachinegun` | SMG | 5 (`sub1–5`) | 400 | 0.18 |
| `zap` | Zappers | 1 | 400 | 0.12 |

> "Active variants" counts only the uncommented entries — several files ship a single sound with the
> remaining four slots commented out. The proton-torpedo pool (`eh`) carries far the longest audible
> range (3 km) so torpedo launches read across a whole engagement.

## See also

- [XSF: Arms Generator](XSF-Arms-Generator) – the stat engine that scales every archetype above
- [Weapons](Weapons) – the vanilla turret types these replace
- [Combat](Combat) – damage types and how shields vs hull resolve
- [Defensive systems](Defensive-systems) – shields and point defense on the receiving end

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry)*
