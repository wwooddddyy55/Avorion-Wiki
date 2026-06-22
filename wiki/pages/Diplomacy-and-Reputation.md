<!-- Hand-written mechanics page. Sourced from lib/relations.lua (the relation-change model,
     caps, trait multipliers and status-transition thresholds), sector/background/relationchanges.lua
     (combat/destruction/witness reputation losses), lib/faction.lua (fee-from-relation), player/ui/diplomacy.lua
     (the Diplomacy tab: tribute/ceasefire/alliance negotiation, costs, cooldowns, patience), sector/neutralzone.lua,
     sector/background/warzonecheck.lua and lib/factioneradicationutility.lua. Numeric band names ("Hostile",
     "Bad" … "Excellent") are engine-defined and shown via Relation():getSegments(); they are not hard-coded in Lua. -->
# Diplomacy and Reputation

Every faction in Avorion keeps track of how it feels about you. That feeling is stored as **two things**: a
numeric **relation level** (from −100,000 to +100,000) and a **status** — *War*, *Ceasefire*, *Neutral* or
*Allies*. Together they decide whether a faction's stations will trade with you, dock you and repair you, or
open fire on sight, and how good a price you get when they do (see [Trading and Prices](Trading-and-Prices)).

> **In short:** keep relations **positive** with factions whose space you use — it earns better prices,
> docking and repairs; let them slide negative and you get worse prices, then ambushes and bounty hunters.
> Reputation is **per faction-pair**, so helping one rival doesn't help another. You **raise** it by trading
> and completing their missions; you **lose** it fast by attacking their ships or being caught with
> contraband. The **status** (War / Ceasefire / Neutral / Allies) can be steered directly from the Diplomacy
> tab with tribute, ceasefires and alliances.

Reputation is **per faction-pair**: improving your standing with one faction does nothing for your standing
with its rivals, and the same applies to relations *between* two AI factions. This page explains the scale,
what moves it up and down, how the statuses change, and how you can steer relations yourself from the
**Diplomacy** menu.

## The relation level

Your standing with a faction is a single number on a bar that runs from **−100,000** (total hostility) to
**+100,000** (the best possible). The game divides that bar into named bands — shown in the Diplomacy tab as
labels such as *Hostile*, *Bad*, *Neutral*, *Good* and *Excellent* — but under the hood it is one continuous
value, and almost everything that scales with relations (prices, fees, refining tax) reads the raw number
rather than the band.

A few examples of how the level is used elsewhere:

- **Station prices** shift in your favour as relations rise and against you when they fall ([Trading and Prices](Trading-and-Prices)).
- **Service fees** (repairs, etc.) are `0.5 − relation / 200,000` of the price, and are multiplied by **1.5×**
  whenever relations are negative — so hostile factions charge far more, friendly ones far less.
- Buying **upgrades, turrets, torpedoes and fighters** is blocked entirely while your relations are *Bad* or
  *Hostile*.

> Relations do **not** decay or drift back toward neutral on their own. The number only moves when something
> actually happens — a kill, a trade, a tribute. Whatever you earn or lose, you keep until you change it.

## Relation statuses

The **status** is separate from the number and governs whether you're actively fighting:

| Status | Meaning |
|---|---|
| **War** | Open hostility. Ships and stations attack you on sight. Reputation **gains are halved** while at war. |
| **Ceasefire** | A truce — not friendly, but not shooting. Any hostile act snaps it straight back to War. |
| **Neutral** | The default. Trade and services work normally, subject to your relation level. |
| **Allies** | A formal pact. Reputation **losses are halved**, and allied ships will help you in a fight. |

Most of the galaxy starts *Neutral* toward you. You push toward *Allies* by being useful, and you fall toward
*War* by being a threat.

## What changes your reputation

Every reputation change in the game runs through one system that tags the change with a **type** (combat,
trade, smuggling, tribute…). The type matters because each faction's **personality traits** — *forgiving*,
*peaceful*, *careful*, *greedy*, *honorable* and so on — amplify or dampen changes of that type, and because
each type has its own cap.

### Combat losses

Attacking or destroying a faction's property is the fastest way to wreck your standing. Destroying something
costs you a flat amount based on what it was:

| You destroy… | Relation loss |
|---|--:|
| Station | −100,000 |
| Ship | −40,000 |
| Fighter | −1,500 |
| Turret | −500 |
| Torpedo | 0 |

**Boarding** is treated just as harshly as destruction: −40,000 for a ship, −100,000 for a station. Merely
*damaging* a craft also bleeds reputation while you're shooting — hull hits cost roughly `damage × 5` (capped
at −3,000 per burst) and shield hits a little (capped at −500 per incident) — which is why a stray shot into a
neutral patrol earns an immediate *"Cease fire at once!"*.

### Witnesses

You don't have to be caught by the victim. Any **third-party faction with ships in the sector** reacts to what
it sees, scaled by how it already felt about the victim: harming someone a witness *likes* hurts your standing
with that witness, while attacking someone a witness *dislikes* can actually improve it. **Aggressive**
factions care more; **honorable** factions take particular offence at attacks on unarmed **civilian ships**,
and you'll get a chat warning when that costs you.

### Trade and commerce gains

Doing legitimate business slowly builds relations — but only up to a ceiling. Each kind of commerce can carry
you to a different maximum and no further, so you can never become *allied* purely by shopping:

| Activity | Relations cap |
|---|--:|
| Trading equipment / weapons | +75,000 |
| Trading goods & cargo | +65,000 |
| General commerce | +50,000 |
| Using services / trading resources | +45,000 |

Helping a faction in a fight (**combat support**) and completing **[missions](Missions)** for it are the main
ways to climb past those trade ceilings toward an alliance.

### Illegal activity

Smuggling contraband and raiding are tagged as illegal and drag your standing **down**, but not bottomlessly —
those changes are floored at **−75,000**, so being a known criminal makes a faction hostile without, by itself,
declaring outright war. Trade in dangerous, stolen or illegal goods requires the appropriate **cargo licenses**;
without them, anti-smuggling scans will fine you and cost you reputation.

## How the status changes

Status transitions are driven by the relation level crossing thresholds, with a twist: a faction's **trusting**
trait shifts every threshold by ±5,000 to ±10,000 (very trusting factions forgive faster, mistrustful ones
hold grudges).

- **Neutral → War** — a kill, boarding or raid that drops your level below about **−80,000**; or doing hull
  damage while already at **−100,000**.
- **Ceasefire → War** — *any* kill, boarding or raid, or hitting **−100,000**.
- **Ceasefire → Neutral** — relations climb back above **−30,000**.
- **Allies → Neutral** — relations fall below **+75,000**, or you raid/board one of their craft (which breaks
  the pact instantly).

Declaring war isn't silent: the faction sends you a formal **declaration-of-war mail**, and any
**[Reconstruction-site](Reconstruction-kits)** treaty you held with them is cancelled — your respawn point
reverts to your home sector.

> Climbing back out of a war is slow, because reputation gains are halved while it lasts. Often it's faster to
> negotiate your way out (below) than to grind the number back up.

## Doing diplomacy yourself

The **Diplomacy** tab (the shaking-hands icon) lists every faction you know, their status and relation bar,
their traits, and a set of action buttons. The negotiable actions all work the same way: you open a haggling
window and **make an offer in credits and/or materials**, and the faction accepts once the offer meets its
asking price. Each faction has a **patience** meter that drops every time you lowball it and refills over about
**10 minutes**; run it out and that faction won't talk to you for a while.

| Action | When it's available | Cost (before traits & sector wealth) |
|---|---|---|
| **Pay Tribute** | Neutral or Ceasefire | ~½ the relation points you're buying. Improves relations by up to **+20,000** per deal; 1-hour cooldown. |
| **Negotiate Ceasefire** | At War, **1 hour** after war was declared | Base **15,000** credits |
| **Negotiate Alliance** | Neutral, with relations **≥ +95,000** | Base **8,000** credits |
| **Declare War** | Any non-war, non-allied faction | Free (but consequential) |
| **Abandon Alliance** | While Allied | Free — drops you back to Neutral |

The listed costs are baselines: the final price is scaled by the faction's traits (a *greedy* or *opportunistic*
faction wants more; a *generous* or *peaceful* one less) and by how wealthy its home region is. You can't
negotiate with **player** factions through this menu, nor with factions that have **static** relations or have
been **eradicated**.

> Tribute can never make you *allied* on its own — it tops out before the +95,000 alliance threshold. Use
> tribute and trade to climb, then mission and combat work to clear the final stretch, and only then will the
> **Negotiate Alliance** button light up.

## Zones and special cases

**Neutral zones.** Some sectors are flagged as neutral zones, where **player-versus-player damage is disabled**
entirely and faction-war battles never spawn. You're told as much on arrival.

**Hazard (war) zones.** Sectors with stations track a hidden **war score** from 0 to 100. Destroying things
adds to it — about **+100** for a station and **+40** for a ship — though *your* actions are counted at only
**20%** to discourage griefing. At a score of **60** the sector is declared a **Hazard Zone**: civilian traders
stop coming and the controlling faction warps in a fleet of reinforcements. The score doesn't decay for a full
hour after the last violence, then bleeds off at **1 point per minute**, and the zone clears once it drops back
to **40**.

**Faction eradication.** A faction whose every presence is wiped out is permanently flagged as **eradicated** —
the server announces it galaxy-wide, its war battles and patrols stop spawning, and you can no longer negotiate
with it. There's no getting those relations back.

## See also

- [Trading and Prices](Trading-and-Prices) – how your relation level moves station buy/sell prices and fees
- [Missions](Missions) – faction missions are a primary way to raise reputation
- [Events](Events) – pirate attacks and distress calls where combat support earns standing
- [Reconstruction kits](Reconstruction-kits) – the treaty that war with a faction cancels

---
*Factions & Diplomacy: [Diplomacy and Reputation](Diplomacy-and-Reputation) — related: [Trading and Prices](Trading-and-Prices) · [Missions](Missions) · [Events](Events)*
