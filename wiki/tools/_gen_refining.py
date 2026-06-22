import re

goods_src = open("Avorion/data/scripts/lib/goodsindex.lua", "r", encoding="utf-8").read()
TIERS = ["Iron", "Titanium", "Naonite", "Trinium", "Xanion", "Ogonite", "Avorion"]
MATTAG = {m.lower(): m for m in TIERS}


def parse_set(block):
    return set(re.findall(r'(\w+)\s*=\s*true', block)) if block else set()


goods = {}
for m in re.finditer(r'goods\["([^"]+)"\]\s*=\s*\{(.*?)\}\s*,?\s*$', goods_src, re.M):
    name, body = m.group(1), m.group(2)
    pm = re.search(r'price\s*=\s*(\d+)', body)
    tagm = re.search(r'tags=\{([^}]*)\}', body)
    goods[name] = dict(price=int(pm.group(1)) if pm else 0, tags=parse_set(tagm.group(1) if tagm else ""))

by_mat = {m: {"ore": None, "rich": None, "scrap": None} for m in TIERS}
for name, g in goods.items():
    t = g["tags"]
    mat = next((MATTAG[x] for x in t if x in MATTAG), None)
    if not mat:
        continue
    if "ore" in t and "rich" in t:
        by_mat[mat]["rich"] = name
    elif "ore" in t:
        by_mat[mat]["ore"] = name
    elif "scrap" in t:
        by_mat[mat]["scrap"] = name

vol = {}
for m in re.finditer(r'goods\["([^"]+)"\].*?size=([\d.]+)', goods_src):
    vol[m.group(1)] = m.group(2)


def refine_fee(rel):
    lo, hi, vlo, vhi = -25000, 100000, 0.10, 0.01
    t = max(0.0, min(1.0, (rel - lo) / (hi - lo)))
    return vlo + (vhi - vlo) * t


examples = [
    ("Your own faction / alliance", "0% (free)"),
    ("−25,000 or lower", "{:.1f}%".format(refine_fee(-25000) * 100)),
    ("0 (neutral)", "{:.1f}%".format(refine_fee(0) * 100)),
    ("+50,000", "{:.1f}%".format(refine_fee(50000) * 100)),
    ("+100,000 or higher", "{:.1f}%".format(refine_fee(100000) * 100)),
]


def cell(x):
    return x if x else "—"


L = []
W = L.append
W("<!-- Generated from data/scripts/lib/goodsindex.lua + merchantutility.lua via wiki/tools/_gen_refining.py. Do not hand-edit. -->")
W("# Refining")
W("")
W("**Refining** is the process of converting raw **ores** and **scrap** into usable **materials** – the metals")
W("used to build ships and stations. Unlike [goods](Goods), ores and scrap **cannot be sold at stations**; they")
W("must be refined first. Refining is done at a **Resource Depot**, or passively aboard a ship fitted with a")
W("refinery, for a small fee that scales with your relations.")
W("")
W("> **In short:** mining and salvaging fill your hold with **ore and scrap**, which is dead weight until you")
W("> **refine** it into materials at a **Resource Depot** (or passively, with an onboard refinery). The fee")
W("> **shrinks as your relations improve** and is **free at your own faction's** depot — so refine where")
W("> you're liked. Materials, not ore, are what you spend to build ships and stations.")
W("")
W("## Overview")
W("")
W("Mining asteroids and salvaging wreckage fills your cargo bay with raw ore and scrap. These are dead weight")
W("until refined: the refinery sorts everything in your hold by material type and converts it into the")
W("corresponding refined material, which is then stored as a resource you can spend on building.")
W("")
W("Stolen ore is never refined. **Rich** ores (found only in rifts) are kept separate from normal ore because")
W("they yield far more material per unit (see below).")
W("")
W("## Materials")
W("")
W("There are seven materials, in ascending tier. Higher tiers are found deeper toward the galactic core and are")
W("required for more advanced blocks and equipment. Each material has a standard ore, a rich rift ore, and a")
W("scrap form that all refine into it.")
W("")
W("| Tier | Material | Standard ore | Rich rift ore (4×) | Scrap |")
W("|:--:|---|---|---|---|")
for i, mat in enumerate(TIERS, start=1):
    b = by_mat[mat]
    W("| %d | **%s** | %s | %s | %s |" % (i, mat, cell(b["ore"]), cell(b["rich"]), cell(b["scrap"])))
W("")
W("## Ores and scrap")
W("")
W("The raw resources below are sorted by material tier. Standard ores and scrap refine 1:1 by material type;")
W("**rich** rift ores yield **4×** as much material as the standard ore of the same metal.")
W("")
W("| Resource | Material | Type | Base price | Volume |")
W("|---|---|---|--:|--:|")
for tier_i, mat in enumerate(TIERS, start=1):
    for kind, label in (("ore", "Standard ore"), ("rich", "Rich rift ore (4×)"), ("scrap", "Scrap")):
        name = by_mat[mat][kind]
        if name:
            W("| %s | %s | %s | %s | %s |" % (
                name, mat, label, "{:,}".format(goods[name]["price"]), vol.get(name, "")))
W("")
W("## Refining fee")
W("")
W("Refining at a Resource Depot costs a **fee** taken as a fraction of the refined materials' value. The fee")
W("falls as your relations with the depot's faction improve, and refining at a station owned by your own faction")
W("is **free**. The fee is:")
W("")
W("$$\\text{fee} = \\operatorname{lerp}(\\rho,\\ -25{,}000,\\ +100{,}000,\\ 0.10,\\ 0.01)$$")
W("")
W("where $\\rho$ is your relations value, clamped to the range below. In other words the fee runs from **10%**")
W("at hostile relations down to **1%** at maximum relations:")
W("")
W("| Relations with the depot's faction | Refine fee |")
W("|---|--:|")
for cond, v in examples:
    W("| %s | %s |" % (cond, v))
W("")
W("## Conversion ratios")
W("")
W("> **Note:** The exact amount of material produced per unit of ore or scrap is determined by the game engine")
W("> and is not defined in the moddable script data, so it is not reproduced here. The rules that *are* defined")
W("> in the scripts – which ore refines into which material, the 4× rich-ore yield, and the refine fee – are")
W("> documented above.")
W("")
W("## See also")
W("")
W("- [Goods](Goods) – tradeable commodities (ore and scrap are listed under Raw resources)")
W("- [Trading and Prices](Trading-and-Prices) – how relations and fees affect other transactions")
W("- [Player stations](Player-stations) – building and operating your own stations")
W("")
W("---")
W("*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods)*")

open("wiki/pages/Refining.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote wiki/pages/Refining.md | materials=%d" % len(TIERS))
