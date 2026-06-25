<!-- Mod documentation. Code lineage (kept out of the reader-facing text on purpose):
     "Avorion Mods/2992808396/" (XSF: Arms Generator, v2.5.3) — modinfo.lua;
     data/scripts/ArmsGenerator.lua (GetTurret pipeline GetTurretMetadata/ApplyInputParameters/
       ApplyRarityScaling/ApplyMaterialScaling/ApplyTechLevelScaling/ConvertToMultibarrel/ApplyCooling,
       GetScaledShotDamage, IsExtendedType);
     ArmsGenerator/ArmsLibrary.lua (WeaponTTK.Volume / ToDamage);
     ArmsGenerator/BarrelFunctions/BarrelFunction_Default.lua (_ApplyBarrelFactors, _AddPenetration);
     .../MaterialFunctions/MaterialFunction_Default.lua; .../RarityFunctions/RarityFunction_Default.lua;
     .../CoolingFunction.lua; data/scripts/lib/{turretgenerator,weapongenerator,sectorturretgenerator,
     inventoryitemprice}.lua (wrapped, original saved as _generateTurret/_ArmedObjectPrice etc.);
     shared FMath.ScalarCut in "Avorion Mods/2918443067/Core/CoreLibrary.lua".
     Image assets: see wiki/ASSETS.md. -->
# XSF: Arms Generator

**XSF: Arms Generator** (by **LM13**) is the **turret-stat engine** behind the [Xavorion](Xavorion-Weaponry)
mod suite. Where the base game rolls a turret's stats from loose random ranges (see [Weapons](Weapons)),
this mod rebuilds every modded turret deterministically from four stacking **dials** — **tech**, **rarity**,
**material** and **barrel** — driven by a per-weapon archetype defined in
[Xavorion: Weaponry](Xavorion-Weaponry).

> **In short — for players:** with this mod, turrets stop being slot-machine pulls. A weapon's stats follow
> directly from four readable inputs — its **tech level**, its **rarity**, the **material** it's made of,
> and which **barrel** it rolled. **Tech is the biggest damage lever (~7×), rarity next (~2×), material is a
> trade-off rather than a straight upgrade.** Once you know these four dials you can predict what any drop
> will do and see *why* one turret beats another. It does **not** change vanilla turrets — only the mod's
> own weapons use the formulas below.

This page documents those dials. For the weapon catalog the engine builds from, see
[Xavorion: Weaponry](Xavorion-Weaponry); for vanilla turret generation and damage types, see
[Weapons](Weapons) and [Combat](Combat).

## Does it break normal turrets? No.

The mod slots in **beside** the base game's turret code rather than replacing it: it keeps a copy of the
original generator and only takes over when the turret being built is one of its own weapon types. Vanilla
turrets — and other mods' turrets — fall straight through to the untouched original. So only the mod's own
archetypes use the formulas here; everything else behaves exactly as it always did.

## The generation pipeline

Building one turret is an assembly line. The engine starts from the weapon's **base archetype** (the plain
numbers listed in [Xavorion: Weaponry](Xavorion-Weaponry)) and runs it through a fixed sequence, each step
layering on one dial. Order matters — rarity, material and tech adjust the raw stats first, *then* the
barrel step splits the result into a Heavy/Gatling/etc. variant, and cooling is fitted last:

1. **Copy the archetype's base stats.**
2. **Set base damage** from the weapon's Time-To-Kill goal (below).
3. **Rarity scaling** — per-stat bonuses.
4. **Material scaling** — per-material multipliers.
5. **Tech-level scaling.**
6. **Barrel split** — barrels, block penetration, auto-balance factors.
7. **Cooling** — heat / energy drain / battery.

## Base damage — the Time-To-Kill model

The clever bit: weapon damage isn't a number a designer picked — it's worked *backwards* from a goal. Each
weapon says "I should destroy a ship of *this* size in *this* many seconds," and the engine solves for the
per-shot damage that achieves it. That's why the catalog lists a **Time-To-Kill** instead of a damage
figure, and why a slow weapon and a fast one aimed at the same target end up comparably lethal — they're
balanced to the same kill time.

The Tech-1, Iron baseline that every other stage scales is:

> **base shot damage = (target Volume × 4 ÷ kill-time-seconds ÷ 5) ÷ fire rate**

The target is one of eight ship-size **classes** (M1 the smallest, M8 the largest), each with a reference
volume:

| Class | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **Volume** | 100 | 500 | 1,000 | 3,000 | 9,000 | 25,000 | 75,000 | 200,000 |

So a weapon set to kill an M3 (Volume 1,000) in 5 s at 1 shot/s starts at
(1,000 × 4 ÷ 5 ÷ 5) ÷ 1 = **160** base damage per shot, *before* the tech and rarity multipliers below.

## Tech & rarity damage scaling

This is what makes a high-tech Legendary turret hit so much harder than an early grey one. The Iron baseline
gets multiplied twice — once by **tech level**, once by **rarity** — and the two stack:

> **final shot = base shot × tech factor × rarity factor**
> where, by default, **tech factor = 1 + 6 × (tech ÷ 52)** (tech runs 1–52) and
> **rarity factor = 1 + 1 × ((rarity value + 2) ÷ 7)** (rarity value −1…5).

That's up to **~7× from tech** and **~2× from rarity** — so finding higher-tech weapons matters more for raw
damage than chasing rarity. A few archetypes dial these down to lean on their other strengths (for example
the laser line scales tech ×3 / rarity ×1.5, and the fighter proton torpedo ×9 / ×2.5; see
[Xavorion: Weaponry](Xavorion-Weaponry)).

## Barrels

The **barrel** is why two turrets of the same weapon can play completely differently. One archetype can
split into four variants, each a distinct feel:

- **Heavy** – a single barrel firing slow, enormous shots (×5 damage, half the fire rate) at long range,
  and it drills through armour (penetration 9). The sniper/brawler build.
- **Medium** – two barrels, a balanced middle ground with modest penetration (3).
- **Burst** – three barrels that dump a tight burst of shots and always pierce shields, then pause.
- **Gatling** – four barrels of rapid, lighter fire; the sustained-DPS, fighter-shredding build.

Each variant locks in a barrel count and block penetration, then multiplies the base stats by a table of
**auto-balancing factors** (applied only where the archetype hasn't already fixed an exact value):

| Barrel | Barrels | Tracking | Recoil | Range | Accuracy | Velocity | ShotDamage | Volley/s | Reload | ShootTime |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **Heavy** | 1 | ×0.5 | ×5.0 | ×1.5 | ×1.15 | ×2.5 | ×5.0 | ×0.5 | ×1.5 | ×1.5 |
| **Medium** | 2 | ×0.75 | ×2.0 | ×1.2 | ×1.0 | ×1.5 | ×2.0 | ×0.75 | ×1.0 | ×2.0 |
| **Burst** | 3 | ×0.9 | ×VolleySize | ×0.8 | ×0.90 | ×1.5 | ×1.3333 | ×0.6 | ×2.0 | ×4.0 |
| **Gatling** | 4 | ×1.0 | ×1.0 | ×1.0 | ×0.95 | ×1.0 | ×1.875 | ×1.0 | ×2.0 | ×4.0 |

> **Block penetration** is set to (blocks − 1) with a **minimum of 3**, and penetrating barrels set both the
> shield- and hull-damage multipliers to 4.0. **Heavy** drills 9 blocks; **Medium** drills 3. **Burst** also
> forces a guaranteed shield pierce, a minimum volley of 6 shots, and burst-fire behaviour. Accuracy is
> finally clamped to 0.1–1.0 and tracking to 0.01–3.0.

## Materials

The **material** a turret is built from (Iron up to Avorion) gives each tier its own personality, not just a
flat power bump — higher materials aren't strictly better, they're *differently* tuned, so picking a
material is a trade-off. The table lists every factor that isn't ×1.0 (Size, Slot and VolleySize are
unchanged by material):

| Material | Crew | Tracking | Recoil | Range | Accuracy | Velocity | ShotDmg | Reload | ShootTime | Energy/s | Size | BasePrice |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **Iron** | ×0.5 | — | — | — | — | — | — | — | — | — | — | ×0.5 |
| **Titanium** | — | ×1.15 | — | ×1.15 | — | ×1.15 | — | — | — | — | — | ×1.0 |
| **Naonite** | ×2.0 | — | — | — | ×1.1 | ×1.1 | — | ×0.5 | ×2.0 | ×0.5 | — | ×1.5 |
| **Trinium** | — | — | ×2.0 | — | — | — | ×1.5 | — | ×0.5 | ×2.0 | — | ×1.5 |
| **Xanion** | — | — | — | ×0.8 | ×0.95 | — | ×0.75 | — | ×1.5 | — | — | ×2.5 |
| **Ogonite** | — | — | ×0.15 | — | — | — | ×1.25 | ×2.0 | — | ×0.5 | ×1.5 | ×2.0 |
| **Avorion** | ×3.0 | — | — | ×1.25 | ×1.1 | ×1.15 | ×1.15 | — | ×2.0 | ×2.0 | — | ×3.0 |

The rough personalities: **Iron** is cheap; **Titanium** tracks and reaches farther; **Naonite** is
cooling/energy-efficient but crew-hungry; **Trinium** trades recoil for raw power; **Xanion** is a fast
glass cannon; **Ogonite** is big and low-recoil; **Avorion** is broadly superior but crew-, energy- and
price-heavy.

## Rarity

Where material trades stats off against each other, **rarity** broadly *improves* everything — a
higher-rarity turret reaches farther, aims better, fires faster and reloads quicker. One formula scales each
stat by the rarity value (Petty −1 through Legendary 5), so the gain is smooth and predictable. A Petty
weapon is actually slightly *penalised* below baseline, which is why the lowest rarities feel genuinely
weak:

| Stat | How rarity scales it | Range (Petty → Legendary) |
|---|---|---|
| **Range** | × (1 + 0.05 × value) | −5% → +25% |
| **Accuracy** | + 0.01 × value | −1pp → +5pp |
| **Velocity** | × (1 + 0.05 × value) | −5% → +25% |
| **Fire rate** | × (1 + 0.10 × value) | −10% → +50% |
| **Reload** | × (1 − 0.10 × value) | +10% → −50% (lower is better) |
| **Shooting time** | × (1 + 0.25 × (value + 1)) | +0% → +150% |
| **Efficiency** | × (1 + 0.30 × (value + 2) ÷ 7) | up to +30% |

## Cooling

Cooling decides whether a weapon can **fire continuously or has to pace itself** — the difference between a
gun you hold the trigger on and one that overheats or drains your reactor. Each weapon family uses one of
three models, matched to its character:

| Cooling type | Used by | Behaviour |
|---|---|---|
| **Heat** | physical guns | Standard heat build-up; a single shot can never exceed the reservoir. |
| **Battery** | energy-fed weapons (blasters, lasers, railguns) | Fires off a stored energy reservoir of the same shape as Heat. |
| **Drain** | continuous-drain weapons (zappers, beams) | Bleeds power the whole time it fires; runs on a 120%-charge reservoir. |

## Pricing

A weapon's price climbs by the same three dials that drive its power, weighted the same way damage is — so
what you pay tracks what you get. Each archetype defines a **base** and **max** price (the columns in
[Xavorion: Weaponry](Xavorion-Weaponry)), and the engine fills the gap between them by tech, rarity and
material. **Tech moves the price most, rarity next, material least** — the same pecking order as damage — so
a high-tech turret is the expensive one even at low rarity. The span between base and max is split
**10 : 5 : 3** across tech : rarity : material, with a floor of 100 credits. A missing max price defaults to
100× the base.

## See also

- [Xavorion: Weaponry](Xavorion-Weaponry) – the weapon archetypes this engine generates, plus fighters, shields and sounds
- [Weapons](Weapons) – the vanilla turret types and how base-game generation works
- [Combat](Combat) – damage types, shields vs hull, and how vanilla weapon power scales
- [Turret crafting](Turret-crafting) – building turrets and the stat each ingredient raises

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry) · [Xavorion: Mining](Xavorion-Mining) · [Xavorion: Class System](Xavorion-Class-System) · [Xavorion: Encounters](Xavorion-Encounters) · [Xavorion: Combat AI](Xavorion-Combat-AI)*
