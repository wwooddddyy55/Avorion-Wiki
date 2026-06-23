<!-- Hand-written mechanics page. Sourced from systems/shieldbooster.lua, systems/shieldimpenetrator.lua,
     systems/energytoshieldconverter.lua, systems/resistancesystem.lua (Shield Ionizer),
     systems/weaknesssystem.lua (Hull Polarizer) and systems/defensesystem.lua (Internal Defense Weapons).
     Numbers are what those scripts compute; the underlying shield/damage resolution is engine-side. -->
# Defensive systems

Beyond armor and shield blocks, a ship's survivability is shaped by **upgrade systems** (the modules you
slot into upgrade sockets) that boost shields, change how damage types apply, or fight off boarders. This
page covers the defensive upgrades; for the damage they defend against, see **[Combat](Combat)**.

> **In short — what to prioritize:**
> 1. **Shield Booster** first — raw extra shield HP is the broadest survivability upgrade.
> 2. **Point Defense / Anti-Fighter guns** if you face torpedoes or fighters (carriers, torpedo bosses).
> 3. **Situational:** *Shield Impenetrator* when shield-piercers (Pulse Cannons, Sabot torpedoes) are
>    eating you; *Shield Ionizer* for resistance to a known damage type; *IDWS* if you're being boarded.
> 4. **Avoid the Hull Polarizer** unless you're sure you won't meet its weak damage type — the downside is
>    crippling.
>
> Most of these reach **full strength only when permanently installed** — commit your best rolls.

## Permanent installation

Many defensive systems give a small bonus when slotted normally and their **full** effect only when
**permanently installed** (built into the ship at an Equipment Dock, which consumes the upgrade). Several
effects below — impenetrable shields, the emergency recharge, resistances and weaknesses — are
**permanent-only**, noted per system. Permanent installs cannot be removed without scrapping the upgrade.

Every defensive system also has an **energy cost** and **credit price** that rise steeply with rarity.

## Shield systems

### Shield Booster
Raises raw shield strength. It grants **shield durability** (extra HP), **shield recharge rate**, or both:

- **Durability:** base **5,000 HP**, plus **10,000 HP per rarity step**, plus a small random amount.
  A permanent install **triples** this.
- **Recharge rate:** roughly **+5%**, scaling up with rarity. A permanent install adds **+50%** on top.
- Low-rarity boosters often give only **one** of the two; from **Exotic** rarity up you always get both.
- **Emergency Recharge** (permanent install, **Rare** rarity and up): when your shield is depleted, it
  instantly restores **35%** of maximum shield. This can only trigger **once every 5 minutes**.

### Shield Impenetrator / Shield Reinforcer
Makes shields **impenetrable** — shots and torpedoes can no longer pierce or bypass them (countering
Pulse Cannons, Sabot torpedoes, etc.). This is a **permanent-only** effect and comes with two trade-offs:

- **Lower shield durability** — durability is diverted into the membrane, leaving roughly **25%–43%** of
  normal max shield (higher rarity keeps more).
- **Longer recharge delay** — the time before shields start recharging after a hit is greatly increased
  (higher rarity reduces the penalty).

Best on ships that rely on a big shield wall and are bleeding to shield-piercing weapons; poor on
recharge-tanking builds.

### Energy-to-Shield Converter
Re-routes power generation into shield strength: a large **shield durability** bonus (about
**+1.4× the listed base** when permanently installed, scaling with rarity) in exchange for **reduced
generated energy**. Strong on energy-rich ships; risky if your power budget is already tight. Balanced
around permanent installation.

## Damage-type modifiers

These change how specific [damage types](Combat#damage-types) apply to your ship. Both are **unique**
(only one of each can be active) and **permanent-only**.

### Shield Ionizer — resistance
Reduces incoming damage of **one** randomly-assigned type: **Physical, Plasma, Electric or Anti-Matter**.
The reduction scales with rarity:

| Rarity | Damage reduction (minimum) |
|---|--:|
| Petty | −4% |
| Common | −7% |
| Uncommon | −10% |
| Rare | −15% |
| Exceptional | −20% |
| Exotic | −25% |
| Legendary | −30% |

(The actual value rolls a little above each floor.) The variant name tells you the type it resists —
*Hardening* (Physical), *Plasmatic* (Plasma), *Grounding* (Electric), *Solidifying* (Anti-Matter).

### Hull Polarizer — weakness
A high-risk hull buff: it greatly increases **hull durability** but makes the ship take **far more**
damage from **one** type — **Energy, Plasma, Electric or Anti-Matter**:

| Rarity | Hull durability | Extra damage from the weak type |
|---|--:|--:|
| Petty | +10% | +300% |
| Common | +20% | +300% |
| Uncommon | +30% | +300% |
| Rare | +30% | +275% |
| Exceptional | +30% | +250% |
| Exotic | +30% | +225% |
| Legendary | +30% | +200% |

So higher rarity keeps the +30% hull bonus while **shrinking** the downside. Worth it only if you don't
expect to face that one damage type — otherwise the weakness is crippling.

## Anti-boarding

### Internal Defense Weapons System (IDWS)
Adds **internal defense weapons** that fight off enemy crew during a **boarding** attempt — it does not
affect normal weapon combat. The number of internal weapons (permanent install) scales with rarity:
roughly **(rarity + 2) × 5** at low rarities and **rarity × 10** at higher rarities, plus a small random
amount. Useful on ships you expect pirates or factions to try to capture.

## Active defenses (weapons)

Two turret classes are defensive rather than offensive and are covered on **[Weapons](Weapons)**:

- **Point Defense Cannon / Laser** — auto-target and destroy incoming **torpedoes and fighters**.
- **Anti-Fighter Gun** — flak that bursts among **fighter swarms** for area damage.

Pair these with the shield systems above to counter the [torpedoes](Torpedoes) and strike craft that
otherwise bypass a shield-and-armor build.

## See also

- [Combat](Combat) – damage types, resistances and weaknesses, shields vs hull
- [Weapons](Weapons) – point defense and anti-fighter turrets
- [Torpedoes](Torpedoes) – the shield-piercing and shield-deactivating threats these systems counter
- [Fighters](Fighters) – the swarms point defense and anti-fighter guns are built to kill
- [System upgrades](System-upgrades) – the wider upgrade framework these defensive systems are built on

---
*Combat & Weapons: [Combat](Combat) · [Weapons](Weapons) · [Turret crafting](Turret-crafting) · [Torpedoes](Torpedoes) · [Defensive systems](Defensive-systems) · [Fighters](Fighters)*
