<!-- Mod documentation. Sourced from "Avorion Mods/2992809109/" (Xavorion: Weaponry, v2.6.5) Lua:
     modinfo.lua; data/scripts/TurretsDatabase/Combat{Artillery,Blasters,Disruptors,Lasers,Launchers,
     Machineguns,ProtonTorpedos,Railguns}.lua; data/scripts/systems/{fightersquadsystem,shieldbooster}.lua;
     data/scripts/weaponsounds/*.lua. The damage model WeaponTTK.ToDamage and all stat scaling live in the
     companion mod XSF: Arms Generator (2992808396) — see that page. Formulas as monospace code blocks. -->
# Xavorion: Weaponry

**Xavorion: Weaponry** (Workshop ID `2992809109`, by **LM13**) is a *"complete weapons overhaul for
Xavorion"* — it replaces the random vanilla turrets with a designed armoury of **named weapon families**,
each built around a clear job: flak auto-cannons to swat fighters, slow railguns that punch through hull,
torpedoes that ignore shields, and so on. Where [XSF: Arms Generator](XSF-Arms-Generator) is the **engine**
that turns a weapon into concrete numbers, this mod is the **content** it works on: the weapon catalog
below, plus a fighter-squad module, a shield-booster module, and the custom firing sounds.

Because every weapon is generated through that engine, the values in these tables are the **starting
point only** — the Iron, lowest-tech, base form of each weapon. A turret you actually loot or buy is the
same archetype scaled up by its **tech level, rarity and hull material** and split into a **barrel variant**
(see [XSF: Arms Generator](XSF-Arms-Generator) for how much that adds). Read the base tables as *relative*
character — how a weapon fires, what it's good against, how it ranks against its siblings — rather than as
the final damage you'll see in-game. For vanilla weapon types and damage types, see [Weapons](Weapons)
and [Combat](Combat).

> **Mod metadata.** `version = "2.6.5"`, `serverSideOnly = false`, `clientSideOnly = false`,
> `saveGameAltering = true`. Dependencies: `2918443067`, `2923179923`, `2992808396` (all min `2.3.9`),
> optional `2992808561` / `2992808472`, and `Avorion` `2.0`–`2.5.*`.

## How to read the weapon tables

**Ship classes (M1–M8).** Every weapon is rated against a ladder of ship sizes, from **M1** (the smallest
— fighters and tiny corvettes) up to **M8** (capital ships and bosses). Two columns place each weapon on
that ladder:

- **Class** – the size of hull the weapon is *built to sit on*. A Class M6 turret is heavy enough that it
  only makes sense on a large ship.
- **vs** – the enemy size its damage is *tuned to kill*. This is the weapon's intended prey, and it's why
  the families ladder upward: an M5 weapon "vs M5" is your line gun, while one rated "vs M8" exists to
  hurt the biggest targets.

**Damage as Time-To-Kill.** Instead of a flat damage number, each weapon states how *fast* it should kill
its target: `WeaponTTK.ToDamage(TTK, vs, fireRate)` means *"sized to destroy a ship of class `vs` in `TTK`
seconds."* A lower **TTK** is more lethal per second. The engine converts that into per-shot damage
(`(Volume[vs] × 4 / TTK) / 5 / fireRate`, see [the TTK model](XSF-Arms-Generator#base-damage--the-time-to-kill-model))
and then multiplies it by tech and rarity. So TTK is best read as the weapon's *ambition* against its
prey, not a literal kill timer at base tech.

**The other columns.** **Fire/s** is shots per second (higher = more sustained, lower = slower but harder
hits). **Acc** is accuracy, **Range** the reach in km. **Energy** is the power draw for energy-fed weapons
— a high figure means it's only practical on a ship with a strong reactor. **Reload**, **Crew**, **Size**
and **Slot** are the turret's cost in seconds, manpower and ship space. **Cool.** names the cooling model
(see [cooling systems](XSF-Arms-Generator#cooling-systems)).

**Recurring terms.** A few behaviours show up across families:

- **Flak** – the shot explodes on impact in a small radius, splashing nearby targets; ideal against
  clustered fighters, drones and torpedoes.
- **Seeking** – the projectile homes onto its target instead of flying straight, so it lands on fast or
  evasive ships.
- **Block / shield penetration** – the shot drills through several armour blocks (or bypasses shields)
  instead of stopping at the first, hitting the soft interior.
- **Coaxial** – the turret only fires straight ahead along the ship's axis; you aim it by aiming the ship,
  in exchange for stronger stats.
- **Barrel variants.** Every weapon also generates in **Heavy / Medium / Burst / Gatling** forms that
  trade fire rate for hitting power (and sometimes change behaviour entirely). Names ending **NPC** are
  enemy-only versions you won't loot.

## Combat Artillery — Auto-Cannons

Mid-range **flak** artillery: every round explodes on impact (`ExplosionRadius 10`), so the line shines
against anything small and clustered — fighter swarms, drones, torpedoes — while still threatening larger
ships. They climb the whole ladder, from the light **AC-3-C** up to the slow, devastating **AC-XLA "Big
Bang."** Higher tiers trade fire rate for reach and per-shot weight: the cannons get bigger, slower and
longer-ranged as you go down the table.
_(Engine: `WeaponTech.Cannon`, **Heat** cooling, custom **AC** scaling, sound `"ac"`.)_

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

The energy-fed **workhorse line** — steady, accurate, recoilless guns that form the backbone of a general
loadout. The **PPG** ("Pulse Plasma Gun") models cover the early-to-mid ladder; the heavier **HPE**
("Heavy Plasma Emitter") tiers take over for big ships, at a steep energy cost (the M7 draws **28 GW**, so
these belong on a ship with reactor capacity to spare). There's no flak here — blasters are a clean,
single-target damage dealer rather than a crowd-clearer. Projectile colour shifts toward blue as the tier
rises.
_(Engine: `WeaponTech.Blaster`, **Battery** cooling, no recoil; PPG uses the default fire sound, HPE uses `"hpe"`.)_

| Name | Class | vs | TTK | Fire/s | Acc | Range | Energy | Crew | Size | Slot | Reload | Price |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **PPG-1-A** | M1 | M1 | 5 | 0.85 | 0.96 | 8 km | 25 MW | 0 | 0.5 | 1 | 3 | 1k → 40k |
| **PPG-2-A** | M2 | M2 | 11 | 0.8 | 0.95 | 10 km | 175 MW | 1 | 1.0 | 1 | 5 | 5k → 160k |
| **PPG-4-A** | M4 | M3 | 12 | 0.65 | 0.92 | 15 km | 500 MW | 2 | 1.0 | 1 | 7 | 25k → 320k |
| **PPG-5-A** | M5 | M4 | 18 | 0.6 | 0.91 | 18 km | 5 GW | 2 | 1.5 | 1 | 8 | 50k → 640k |
| **HPE-6-A** | M6 | M5 | 32 | 0.55 | 0.90 | 22 km | 12 GW | 4 | 1.5 | 2 | 12 | 120k → 2M |
| **HPE-7-A** | M7 | M6 | 60 | 0.5 | 0.88 | 30 km | 28 GW | 6 | 2.0 | 2 | 15 | 300k → 5M |

## Combat Disruptors — Zappers & EMP Guns

The **Electric-damage** line, which hits shields and hull about equally — useful when you want to grind
down a target's protection rather than specialise against one or the other. It splits into two flavours:
**Zappers (ZAP)**, continuous-drain beams that pour out a steady stream, and **EMP Guns (EEG)**, which
fire in faster bursts. Both get an extra damage multiplier on top of the usual TTK base (shown as
**TTK ×mult**), so they punch a little above their listed kill time. The capstone **ZAP-XLA "Zeus"** is a
ship-scale beam with a brutal **350 GW** draw.
_(Engine: Zappers `WeaponTech.EMP`; EMP Guns `WeaponTech.Blaster` tech with Electric damage. Cooling is **Drain** or **Battery** as noted per row.)_

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

Pin-point **beam weapons** (the **RBE** family) — near-perfect accuracy (`0.98`) and instant hit, so they
never miss and never need leading. The trade-off is energy hunger that grows viciously with tier: the
early **P-RBE-1** sips half a gigawatt, but the **RBE-X-C "Deathray"** demands a colossal **1,000 GW** and
1,000 crew, making it a true capital-ship signature weapon. Lasers scale more gently with tech and rarity
than other families (the line caps its multipliers lower), so they reward steady accurate fire over spikes.
In the **Burst** and **Gatling** barrels the beam becomes a rapid **pulse-laser** instead of a steady stream.
_(Engine: `WeaponTech.Laser`/`PulseLaser`, **Battery** cooling, no recoil; `TechDamageMult 3.0`, `RarityDamageMult 1.5`, **RBE** scaling.)_

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

The missile line, built for **reach and area denial**. It comes in two ranges — short-range **SRM** and
long-range **LRM** — and each model mixes two tricks: **seeking** (the missile homes in, so it lands on
fast or distant ships) and **flak** (it bursts on arrival, splashing whatever is nearby). The early
**SRM-1-GC** is a pure homing missile for chasing fighters; the mid-tier models add flak to clear groups;
the **LRM-X-A "Rainfire"** combines a wide explosion with a long reach to saturate an area from afar. The
**Behaviour** column spells out which tricks each model carries.
_(Engine: `WeaponTech.Launcher`, **Heat** cooling.)_

| Name | Class | vs | TTK | Fire/s | Acc | Range | Crew | Size | Slot | Reload | Behaviour |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **SRM-1-GC** | M1 | M1 | 2 | 1.5 | 0.8 | 6 km | 0 | 0.5 | 1 | 5 | **Seeking**, coaxial |
| **SRM-3-C** | M3 | M3 | 5 | 1.4 | 0.9 | 10 km | 4 | 1.0 | 2 | 12 | **Flak**, expl. radius 10, coaxial |
| **SRM-5-A** | M5 | M4 | 5 | 1.25 | 0.9 | 14 km | 8 | 2.0 | 3 | 15 | **Flak**, expl. radius 10 |
| **LRM-6-GA** | M6 | M4 | 10 | 1.15 | 0.9 | 20 km | 15 | 2.5 | 4 | 25 | **Seeking + Flak**, expl. radius 10 |
| **LRM-X-A "Rainfire"** | M8 | M6 | 1 | 1.5 | 0.9 | 25 km | 100 | 5.0 | 8 | 30 | **Flak**, expl. radius 50, proj. size 5 |

## Combat Machineguns

The cheap, **high-rate-of-fire** small-ship line — the first weapons you'll arm a starting ship with. The
**SMG** and **MG** are spray weapons that stack lots of light shots quickly; the **MG** hits harder but
kicks more (recoil ×1.3). The **bolter (BMG)** is the precision cousin: near-perfect accuracy (`0.99`) and
**coaxial**, so it's aimed by pointing the ship and rewards that with reliable hits. All four sit at the
bottom of the ladder, for fighters and corvette-scale targets.
_(Engine: `WeaponTech.Gun` for SMG/MG, `WeaponTech.Bolter` for BMG, **Heat** cooling.)_

| Name | Class | vs | Tech | TTK | Fire/s | Acc | Range | Crew | Size | Slot | Reload | Sound | Notes |
|---|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| **SMG-1-A** | M1 | M1 | Gun | 4 | 2.5 | 0.96 | 6 km | 0 | 0.5 | 1 | 3 | submachinegun | tracking 2.6 |
| **MG-2-A** | M2 | M2 | Gun | 8 | 2.0 | 0.94 | 8 km | 1 | 1.0 | 1 | 3 | machinegun | damage ×1.3, recoil ×1.3 |
| **BMG-3-C** | M3 | M3 | Bolter | 5 | 1.5 | 0.99 | 6 km | 2 | 1.0 | 2 | 3 | flak | coaxial |
| **BMG-4-C** | M4 | M4 | Bolter | 5 | 1.5 | 0.99 | 8 km | 4 | 1.5 | 3 | 3 | flak | coaxial |

## Combat Railguns

The **alpha-strike** line: every railgun fires just one shot every four seconds (`0.25`/s) at near-perfect
accuracy, putting all its damage into rare, heavy, precise hits. They reward picking your shot and landing
it cleanly rather than hosing down a target, and their long reach lets them open fire first. Energy draw
climbs hard with tier; the capstone **RX-IL "SoulRipper"** is a 500 GW capital sniper.
_(Engine: `WeaponTech.Rail`, **Battery** cooling, **RIL** scaling, sound `"ril"`.)_

| Name | Class | vs | TTK | Fire/s | Acc | Range | Energy | Crew | Size | Slot | Reload | Price |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **R4-IL** | M4 | M3 | 1 | 0.25 | 0.98 | 8 km | 5 GW | 6 | 1.5 | 4 | 15 | 60k → 650k |
| **R6-IL** | M6 | M4 | 1 | 0.25 | 0.98 | 14 km | 25 GW | 16 | 3.0 | 6 | 25 | 240k → 5M |
| **R8-IL** | M7 | M5 | 1 | 0.25 | 0.98 | 18 km | 150 GW | 24 | 4.0 | 8 | 40 | 520k → 12M |
| **RX-IL "SoulRipper"** | M8 | M6 | 1 | 0.25 | 0.98 | 24 km | 500 GW | 100 | 6.0 | 10 | 60 | 1k → 20M |

## Combat Proton Torpedos

The **shield-bypassing siege** line. These Anti-Matter torpedoes drill through armour (**block
penetration 6**) and largely **ignore shields** (high shield-penetration chance), so they hit a target's
hull almost regardless of its defences — the answer to a heavily-shielded capital. The cost is that the
projectiles crawl (≈0.1 km/s), so they're for slow, deliberate targets rather than dogfighting, and most
are **coaxial** (aimed by the ship). Several entries are **NPC-only** enemy loadouts; the player-usable
ones are marked in the **Player?** column, including the **F-PTL-2-C** fighter torpedo, which trades raw
size for a big damage multiplier so it stays lethal on a tiny fighter hull.
_(Engine: `WeaponTech.Torpedo`, `DamageType.AntiMatter`, **Battery** cooling, sound `"eh"`.)_

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

This is a **system upgrade** (the kind you slot into a ship's upgrade sockets), not a turret. It grants
extra fighter squads and boosts your fighter **production rate** — how fast a carrier rebuilds its wing.
The squad count is left to the vanilla rules, but the mod rewrites the production bonus so it scales with
the upgrade's **rarity** and with two galaxy-wide tuning constants
(`systems/fightersquadsystem.lua`, overriding `getBonuses(seed, rarity, permanent)`):

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

Another **system upgrade** — this one adds shield capacity. The mod throws away the vanilla "random roll"
and instead pins shield HP and energy cost to a clean **per-rarity table**, so you always know exactly what
a given rarity gives you. The jump between tiers is steep (a Legendary booster carries **half a million**
shield HP, 500× the Petty one), making rarity the thing to chase here
(`systems/shieldbooster.lua`, overriding `getBonuses` and `getEnergy`):

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

Pure flavour, but it's why the overhaul *feels* different: each weapon family fires its own custom sound
set rather than the stock effects. Every entry below is a small sound pool the game draws from at random
when the weapon fires, plus how far away it can be heard (**Range**) and how loud it is (**Volume**). A
weapon picks its set by id; a few still point at vanilla sounds like `"flak"`. The practical upshot is
audio readability — you can tell what's shooting, and from how far, by ear
(`weaponsounds/<id>.lua`, each defining a `WeaponSounds` table).

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
