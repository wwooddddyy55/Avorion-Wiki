import re

src = open("Avorion/data/scripts/lib/goodsindex.lua", "r", encoding="utf-8").read()
CATS = ["basic", "consumer", "industrial", "military", "technology"]
MAT = {"iron": "Iron", "titanium": "Titanium", "naonite": "Naonite", "trinium": "Trinium",
       "xanion": "Xanion", "ogonite": "Ogonite", "avorion": "Avorion"}


def parse_set(block):
    return set(re.findall(r'(\w+)\s*=\s*true', block)) if block else set()


goods = []
for m in re.finditer(r'goods\["([^"]+)"\]\s*=\s*\{(.*?)\}\s*,?\s*$', src, re.M):
    name, body = m.group(1), m.group(2)

    def grab(key):
        mm = re.search(key + r'\s*=\s*("?)(.*?)\1\s*,', body)
        return mm.group(2) if mm else None

    bclean = body.replace(" ", "")
    tagm = re.search(r'tags=\{([^}]*)\}', body)
    goods.append(dict(
        name=name, price=grab("price"), size=grab("size"),
        level=(None if grab("level") == "nil" else grab("level")),
        imp=grab("importance"),
        illegal="illegal=true" in bclean, dangerous="dangerous=true" in bclean,
        tags=parse_set(tagm.group(1) if tagm else "")))
goods.sort(key=lambda g: g["name"])


def price_fmt(p):
    try:
        return "{:,}".format(int(p))
    except Exception:
        return p


def cat_of(g):
    c = sorted(t for t in g["tags"] if t in CATS)
    return ", ".join(s.capitalize() for s in c) if c else "—"


def tier(g):
    return g["level"] if g["level"] is not None else "—"


def flags(g):
    f = []
    if g["illegal"]:
        f.append("Illegal")
    if g["dangerous"]:
        f.append("Dangerous")
    return ", ".join(f) if f else "—"


trade = [g for g in goods if not ("ore" in g["tags"] or "scrap" in g["tags"])]
raw = [g for g in goods if ("ore" in g["tags"] or "scrap" in g["tags"])]
illegal = [g for g in trade if g["illegal"]]
dang = [g for g in goods if g["dangerous"]]

L = []
W = L.append
W("<!-- Generated from data/scripts/lib/goodsindex.lua via wiki/tools/_gen_goods.py. Do not hand-edit. -->")
W("# Goods")
W("")
W("**Goods** (also called **commodities** or **trading goods**) are bulk cargo items bought and sold at")
W("stations for profit. Each good has a fixed **base price** and **volume**, and belongs to one or more")
W("**production chains**. Goods are produced by [factories](Production), consumed by population stations, and")
W("moved between sectors by traders. For how prices are calculated at a station, see")
W("**[Trading and Prices](Trading-and-Prices)**.")
W("")
W("## Good attributes")
W("")
W("| Attribute | Meaning |")
W("|---|---|")
W("| **Base price** | The good's fixed value in credits, before supply/demand, relations and station modifiers. Any good with a defined value of 0 is treated as **500**. |")
W("| **Volume** | Cargo space one unit occupies. Determines how much fits in a cargo bay and how much stock a station can hold. |")
W("| **Tier** | Production/tech level, **0–9**. Higher-tier goods sit deeper in their production chain. Raw resources and special items have no tier. |")
W("| **Importance** | An internal weighting used by factory generation; higher values appear more often as shared inputs (for example Energy Cell, Water, Steel). |")
W("| **Category** | The production chain(s) the good belongs to: Basic, Consumer, Industrial, Military or Technology. |")
W("| **Flags** | Special handling: **Illegal** (contraband), **Dangerous** (hazardous), and the runtime states **Stolen**/**Suspicious**. Stations only trade these if their policies allow it. |")
W("")
W("## Production chains")
W("")
W("Goods are grouped into five overlapping **production chains**. A chain describes which goods feed into which")
W("products; a single good can belong to several chains (for example, Aluminum is used across all five).")
W("")
W("- **Basic** – raw and refined fundamentals (metals, gases, crystals).")
W("- **Consumer** – food, drink and lifestyle goods consumed by population stations.")
W("- **Industrial** – intermediate manufacturing materials.")
W("- **Technology** – high-tech components and devices.")
W("- **Military** – weapons, ammunition and combat equipment.")
W("")
W("See [Production](Production) for the full recipe list and [Consumer goods](Consumer-goods) for what each")
W("station type consumes.")
W("")
W("## Trade restrictions")
W("")
W("Some goods cannot be traded freely:")
W("")
W("- **Raw resources** (ores and scrap) are never bought or sold through the normal trade menu – they are processed at resource depots instead. See [Raw resources](#raw-resources) below and [Refining](Refining).")
W("- **Contraband** (illegal goods) is only traded by stations with the matching policy, such as smuggler-friendly outposts. Selling it openly damages relations.")
W("- **Dangerous** goods are legal but flagged hazardous.")
W("")
W("**Contraband (illegal goods):** " + ", ".join(g["name"] for g in illegal) + ".")
W("")
W("**Dangerous goods:** " + ", ".join(g["name"] for g in dang) + ".")
W("")
W("## Raw resources")
W("")
W("Ores and scrap are not traded at stations; they are refined into materials at resource depots. **Rich** rift")
W("ores yield **4×** as much material as their standard counterparts. The refine fee scales with your relations")
W("(see [Refining](Refining)).")
W("")
W("| Resource | Base price | Volume | Refines into | Rich (4×) |")
W("|---|--:|--:|---|:--:|")
for g in raw:
    mat = next((MAT[t] for t in g["tags"] if t in MAT), "—")
    rich = "Yes" if "rich" in g["tags"] else "—"
    W("| %s | %s | %s | %s | %s |" % (g["name"], price_fmt(g["price"]), g["size"], mat, rich))
W("")
W("## Complete goods list")
W("")
W("All %d normally-tradeable goods." % len(trade))
W("")
W("| Good | Base price | Volume | Tier | Importance | Category | Flags |")
W("|---|--:|--:|:--:|--:|---|---|")
for g in trade:
    W("| %s | %s | %s | %s | %s | %s | %s |" % (
        g["name"], price_fmt(g["price"]), g["size"], tier(g), g["imp"], cat_of(g), flags(g)))
W("")
W("## See also")
W("")
W("- [Trading and Prices](Trading-and-Prices) – how station prices are calculated")
W("- [Production](Production) – factory recipes that produce these goods")
W("- [Refining](Refining) – turning ores and scrap into materials")
W("- [Consumer goods](Consumer-goods) – what each station type consumes")
W("")
W("---")
W("*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods)*")

open("wiki/pages/Goods.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote wiki/pages/Goods.md | tradeable=%d raw=%d illegal=%d" % (len(trade), len(raw), len(illegal)))
