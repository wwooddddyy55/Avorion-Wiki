<!-- Mod documentation. Code lineage (kept out of the reader-facing text on purpose):
     "Avorion Mods/2992808971/" (Xavorion: Combat AI, v2.6.5; modinfo: serverSideOnly=false,
     clientSideOnly=false, saveGameAltering=true; deps 2918443067 min 2.3.9 (shared Xavorion Core,
     which defines the base ShipXAI framework this mod extends), Avorion 2.0–2.5.*) — modinfo.lua;
     ShipXAI/Plugins/CombatAI.lua (751 lines; CombatAIPlugin controller: SetCombatTarget/
     CheckAttackedEntity using CombatTarget/TrackedTarget EntityCacheClass pair, GetGlobalState hijacks
     vanilla AIState.Attack into XAIState.FindTarget, SelfDefenseCheck >10 damage threshold while
     Passive/Idle/None and not player-seated → OnRestartCombat, CheckFighterLandingSequence 150m/5s
     auto-recall via BatteryClass, NotifyCombatHUD RPC, GetEngageDistance/GetKeepDistance FMath.Clamp
     15–60km/4–50km); ShipXAI/XAIState.lua (extends enum: SmartAttack=600, MoveAttack=601,
     FindTarget=603, SubAggressive=604; 602 unused); ShipXAI/XAIPlugins.lua (AddXAIPlugin("CombatAI",
     LoadOrder.Secondary), gated by Config/CoreModule.lua's CoreModule.bOverrideCombatComponent,
     default true, defined in dependency 2918443067); ShipXAI/States/NPCAggressive.lua (324 vs Core's
     179 lines: DebugSubState branches "Station Siege Mode"/"Carrier or Ship Attack Mode"/"Target
     Lookup Mode", KeepDistance reroll every 12s, OrdersTimer 5s 50/50 commit-vs-regroup coin flip
     "illusion of organized combat", IsReasonableTarget 25%/tick lock-on roll, drop target beyond
     EngageDistance*1.2, sector leash 160km vs Core's 50km); ShipXAI/States/XAIAggressive.lua (283 vs
     Core's 207 lines: RollTowards banking, MinDistance/MaxDistance split replacing Core's single
     randomized EngageDistance, boosted SetFly, proactive re-target beyond MinDistance, AIState.Attack
     direct-check formation workaround, unknown-state catch-all reset to XAIState.None); ShipXAI/
     States/NPCSmartAttack.lua (178 lines: 5s/EngageDistance disengage check, 99% bail-to-Aggressive
     chance) and XAISmartAttack.lua (139 lines: same entry logic, no disengage-by-range check at all);
     ShipXAI/States/XAIFindTarget.lua (108 lines: 250ms transitional buffer patching "AI does not
     instantly populate attackedEntity" engine timing bug); ShipXAI/States/XAIMoveAttack.lua (179
     lines: entered from Fly+Passive state-buffer history in both Aggressive states, soft-locks
     target while continuing toward fly destination, comment notes "Passive Shooting seems impossible
     to override"); CombatHUD/CombatHUD.lua (855 lines: client-only, active in Fly/CameraFlight only;
     live lock-on reticle via ServerSendData/ClientReceiveData RPC, ColorRGB(1.0,0.5,0.5) pulsing
     sine-wave; live targeting-assist reticle comparing median vs max turret reach, green/yellow/red,
     interface/select_sector + interface/select_answer UI sounds; dead/vestigial RenderOvercharge
     screen-center indicator tied to Xavorion: Class System's Overcharge mechanic, commented-out debug
     window, half-finished RenderHitbox velocity-leading predictor with "error factor" reticle tint);
     player/init.lua (attaches CombatHUD.lua to the Player object on server init). Image assets: see
     wiki/ASSETS.md. -->
# Xavorion: Combat AI

**Xavorion: Combat AI** (by **LM13**) is a *"combat AI extension for NPC and Player ships,"* with *"some
QoL improvements for RTS and TPP combat"* (Real-Time Strategy fleet control and Third-Person Piloting,
Avorion's two ways of fighting). It doesn't touch weapons, turrets or ship stats — it sits underneath
combat, rewriting *how* a ship that's already decided to fight actually closes distance, picks an
engagement range, and commits to (or abandons) a target. It runs on top of the **ShipXAI** framework
shared across the whole Xavorion suite (introduced by the dependency mod that underpins every Xavorion
mod), registering itself as a plugin named **"Combat AI."**

> **In short:** vanilla's high-level decision of *whether* to fight (Patrol, Evade, Persecutor — see
> [Enemy AI](Enemy-AI)) is untouched. What changes is everything **after** a ship enters Attack: this mod
> swaps in its own state machine that picks a smarter approach distance, briefly waits out an engine bug
> before locking on, fires while still flying to a waypoint when it can, and — crucially — behaves
> **differently for NPCs than for your own ships**. NPCs give up a chase if the target gets too far away;
> your captained ships and player-piloted ships do not. On the visual side, a lightweight HUD overlay adds
> a **lock-on reticle** and a **range-aware targeting reticle** while flying, both purely informational.

## Two layers of AI

Avorion's base game decides combat eligibility through a small set of high-level states — Patrol, Evade,
Persecutor, Attack (documented on [Enemy AI](Enemy-AI)). This mod doesn't replace that layer; it **hijacks
one branch of it**. The moment a ship's vanilla state becomes `Attack`, the Combat AI plugin intercepts
that order and redirects it into its own **XAIState** machine instead of letting the base game's simpler
attack logic run:

```
AIState.Attack  →  XAIState.FindTarget  →  XAIState.SmartAttack  ⇄  XAIState.MoveAttack
                                                  ↑                         |
                                          XAIState.Aggressive ←─────────────┘
```

Everything from here on is this mod's own logic, layered on top of (not instead of) the vanilla state.

## The plugin: target tracking and self-defense

The plugin tracks two separate notions of "target" per ship — a raw **TrackedTarget** (whatever the engine
currently has flagged as attacked) and a confirmed **CombatTarget** (what the AI has actually committed
to) — and keeps both notified across hyperspace jumps and target deletion. Two background checks run every
tick regardless of which combat state is active:

- **Self-defense.** A ship sitting **Passive, Idle or None** that takes more than **10 damage** in a tick —
  and isn't currently seated by a player — immediately aborts whatever it was doing and restarts combat.
  This is what makes an unarmed-looking miner or hauler suddenly fight back the instant it's actually shot.
- **Fighter auto-recall.** Every **5 seconds**, if every deployed fighter squad has been ordered to return
  and the average squad is already within **150 m** of the carrier, the hangar force-collects them rather
  than waiting for them to finish their final approach — a small QoL fix so fighters don't dawdle right
  next to an open hangar.

## The Aggressive state: choosing where to sit

**Aggressive** is the "I have a target, now get into position" state, and NPCs and player/captained ships
read it very differently:

| | NPC ships | Player & captained ships |
|---|---|---|
| Engagement range | Re-rolls every **12 s**; carriers hold farther out (`KeepDistance`×1.25 to `EngageDistance`×1.25), others sit closer (`KeepDistance` to `EngageDistance`) | Split into a fixed **Min/Max** distance: carriers hold at Max, every other ship pushes in to **Min** — a tighter, more decisive engagement range than the NPC roll |
| Closing the gap | Normal flight | **Boosted** — closes distance faster |
| Committing to attack | Coaxial-weapon ships and carriers commit immediately; everyone else needs a **25%-per-tick** roll to simulate a lock-on delay | Coaxial ships wait until within `KeepDistance` before committing |
| "Organized combat" illusion | Every **5 s**, a **50/50** coin flip either commits to the target or calls a regroup — explicitly so a squad doesn't look like it's all locking on in perfect unison | — |
| Losing the target | Drops the target and falls back to `FindTarget` if it drifts beyond `EngageDistance`×1.2 | Proactively re-targets if the target passes beyond Min distance, rather than waiting |
| Visual flair | — | Rolls/banks the ship toward its target every tick — a cosmetic touch for third-person flight |
| Range from sector center | Leashed at **160 km** (well beyond the underlying framework's 50 km default) — fleets can chase and fight far from the sector's middle before being pulled back | Same general logic, with a defensive catch-all: an unrecognized AI state logs the ship and resets cleanly instead of getting stuck |

Both Min/Max and Keep/Engage distances ultimately derive from `GetEngageDistance`/`GetKeepDistance`, which
clamp a ship's actual turret reach into a **15–60 km** (engage) / **4–50 km** (keep) band — so a ship with
unusually long- or short-ranged turrets still fights at a sane distance instead of literally using its raw
weapon range.

## FindTarget: a deliberate 250 ms pause

`FindTarget` exists purely to paper over an engine quirk: the game doesn't *instantly* populate a ship's
tracked target the moment combat starts. For up to **250 ms**, the ship waits and polls; the instant a real
target shows up it jumps straight to `SmartAttack`. If nothing materializes in that window, it falls back
to whatever combat target it already had, or back to `Aggressive` if it has none. You'll never consciously
notice this state — it's a buffer, not a behaviour.

## SmartAttack: committing to the kill — and the one rule that's asymmetric

Once locked on, `SmartAttack` calls a hard `SetAttack`+`LockOn` and tells any carrier in the fight to send
its fighters in too. The NPC and player/captained versions are nearly identical *except* for one rule that
matters a lot in practice:

- **NPCs check their distance every 5 seconds**, and if the target has drifted beyond engagement range,
  there's a **99% chance** they give up the chase and fall back to `Aggressive` — pirates and patrols don't
  chase you to the ends of the sector.
- **Player-piloted and captained ships have no such check.** Once one of your ships commits to a target in
  `SmartAttack`, it keeps attacking regardless of how far the target gets — your fleet is "stickier" than
  the enemies it fights.

## MoveAttack: shooting while still going somewhere

A ship that's mid-`Aggressive`/`SmartAttack` but also has a pending **Fly** order (moving to a formation
slot, a waypoint, regrouping) drops into `MoveAttack` instead of stopping to fight. It soft-locks the
target, keeps re-asserting it as priority each tick, tells any carrier fighters to keep firing, and lets
the hull itself continue toward its destination. The mod's own comments flag this as best-effort rather
than guaranteed — getting a ship's passive turret-fire to actually track a chosen target while it's busy
flying somewhere else fights against engine behaviour the mod can't fully override.

## CombatHUD: two informational overlays, two unfinished ones

A lightweight client-side overlay, active only while you're actually flying (hidden the moment you open
Build Mode or the turret editor). It adds no separate window — everything draws over your normal flight
view:

- **Lock-on reticle.** When the server confirms a real combat lock on whatever you have selected — including
  a ship you command but aren't personally piloting — a pulsing pink/red targeter appears, sized on a
  sine-wave pulse so it visibly "breathes" rather than sitting static.
- **Targeting assist.** Before anything is locked, manually selecting a target shows a reticle colored by
  range: **green** (with a confirming UI chime) once you're within your ship's median effective weapon
  reach, sliding toward **yellow and red** the farther past your maximum reach the target sits, with a
  different chime when you lose that lock — a quick visual gut-check for "am I actually in range" without
  opening any menu.

Two more features exist in the file but never actually fire in this version, worth knowing about so you
don't go looking for them: a planned **Overcharge** screen indicator meant to tie into [Xavorion: Class
System](Xavorion-Class-System)'s Overcharge upgrades, and a half-finished **velocity-leading hitbox
predictor** that — once a lock is already established — draws a second dot and line showing where the
target is heading and tints the main reticle by how far off your aim currently is. Both are explicitly
experimental in the source and aren't wired up to actually display under normal play.

## Toggle and load order

The plugin is loaded under the name **"Combat AI"** at **Secondary** priority — after the shared
framework's baseline "BasicAI" plugin — and is gated by a single config flag
(`CoreModule.bOverrideCombatComponent`, on by default). The underlying ShipXAI framework itself has its own
master switch; if that's ever off, this mod's states don't run at all, since they're plugins on top of it
rather than a standalone system.

One loose thread in the source is worth flagging for the curious: the jump-tracking callback that fires
when a combat target jumps away carries only a comment — `@todo: Headhunters AI` — with no implementation.
That's the same "headhunter" bounty-hunter concept that [Xavorion: Encounters](Xavorion-Encounters) ships
with its trigger script fully disabled; this mod has a stub for reacting to one chasing you through a jump,
but nothing currently calls it.

## See also

- [Enemy AI](Enemy-AI) – the vanilla Patrol/Evade/Persecutor/Attack states this mod hooks into, not replaces
- [Xavorion: Encounters](Xavorion-Encounters) – the sibling mod that builds the fleets this AI then controls, and the disabled headhunter/persecutor systems referenced above
- [Combat](Combat) – damage types and weapon range, the numbers this mod's engagement distances are clamped against
- [Fighters](Fighters) – squad orders and hangar behaviour, relevant to the auto-recall and carrier-specific logic above
- [Xavorion: Class System](Xavorion-Class-System) – the Overcharge system the HUD's unused indicator was built for

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry) · [Xavorion: Mining](Xavorion-Mining) · [Xavorion: Class System](Xavorion-Class-System) · [Xavorion: Encounters](Xavorion-Encounters) · [Xavorion: Combat AI](Xavorion-Combat-AI)*
