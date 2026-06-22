import re

prod_src = open("Avorion/data/scripts/lib/productionsindex.lua", "r", encoding="utf-8").read()
goods_src = open("Avorion/data/scripts/lib/goodsindex.lua", "r", encoding="utf-8").read()

price = {}
for m in re.finditer(r'goods\["([^"]+)"\]\s*=\s*\{(.*?)\}\s*,?\s*$', goods_src, re.M):
    name, body = m.group(1), m.group(2)
    pm = re.search(r'price\s*=\s*(\d+)', body)
    p = int(pm.group(1)) if pm else 0
    price[name] = p if p != 0 else 500
price["Silicium"] = price.get("Silicon", 500)
price["Aluminium"] = price.get("Aluminum", 500)


def parse_items(block):
    items = []
    for em in re.finditer(r'\{([^{}]*)\}', block):
        e = em.group(1)
        nm = re.search(r'name\s*=\s*"([^"]+)"', e)
        am = re.search(r'amount\s*=\s*(\d+)', e)
        om = re.search(r'optional\s*=\s*(\d+)', e)
        if nm:
            items.append(dict(name=nm.group(1), amount=int(am.group(1)) if am else 1,
                              optional=(om.group(1) == "1") if om else False))
    return items


recipes = []
for m in re.finditer(r'table\.insert\(productions,\s*\{(.*)\}\)\s*$', prod_src, re.M):
    body = m.group(1)
    fac = re.search(r'factory\s*=\s*"([^"]*)"', body)
    sty = re.search(r'factoryStyle\s*=\s*"([^"]*)"', body)
    factory = fac.group(1) if fac else ""
    style = sty.group(1) if sty else ""
    i_ing, i_res, i_gar = body.index("ingredients="), body.index("results="), body.index("garbages=")
    ings = parse_items(body[i_ing:i_res])
    ress = parse_items(body[i_res:i_gar])
    gars = parse_items(body[i_gar:])
    recipes.append(dict(factory=factory, style=style, ings=ings, ress=ress, gars=gars))


def resolve_name(r):
    nm = r["factory"]
    good = r["ress"][0]["name"] if r["ress"] else ""
    nm = nm.replace("${good}", good).replace("${size}", "")
    return re.sub(r"\s+", " ", nm).strip()


def val(items):
    return sum(price.get(i["name"], 0) * i["amount"] for i in items)


def build_cost(r):
    return 2500000 + (val(r["ress"]) - val(r["ings"])) * 3500


def fmt_items(items, opt=False):
    if not items:
        return "—"
    parts = []
    for i in items:
        s = "%d× %s" % (i["amount"], i["name"])
        if opt and i["optional"]:
            s += " *(opt.)*"
        parts.append(s)
    return "<br>".join(parts)


def money(n):
    return "{:,}".format(int(round(n)))


recipes.sort(key=lambda r: (r["ress"][0]["name"] if r["ress"] else "", resolve_name(r)))

L = []
W = L.append
W("<!-- Generated from data/scripts/lib/productionsindex.lua via wiki/tools/_gen_production.py. Do not hand-edit. -->")
W("# Production")
W("")
W("**Production** is the process by which **factories** and **mines** turn input [goods](Goods) into more")
W("valuable output goods. Buying a factory's inputs cheaply and selling its outputs is a core source of credit")
W("income, and chaining factories that feed each other is the basis of an industrial empire. This page lists")
W("every production recipe in the game. For how the resulting goods are priced when traded, see")
W("**[Trading and Prices](Trading-and-Prices)**.")
W("")
W("> **In short:** a factory profits by **adding value** — it buys cheap inputs and sells dearer outputs.")
W("> The most reliable money comes from **chaining** factories so one's output feeds the next, and from")
W("> owning a factory in a sector that already **demands** its product. Mines and collectors need **no")
W("> inputs** at all, making them the simplest first factory. See [Picking a factory](#picking-a-factory).")
W("")
W("## How factories work")
W("")
W("Each factory runs a fixed **recipe**: it consumes a set of **ingredients** and produces one or more")
W("**results**, sometimes alongside low-value **byproducts**. A factory only produces while it has all of its")
W("required ingredients in stock; **optional** ingredients (marked *opt.* below, usually Energy Cells) speed up")
W("or improve production but are not strictly required.")
W("")
W("Larger factories process proportionally more goods per cycle. (The exact per-cycle timing and the")
W("factory-size output multiplier are handled by the game engine and are not defined in the recipe data.)")
W("")
W("## Factory types")
W("")
W("Recipes come in several **styles**, which mostly affect appearance and how the factory is generated:")
W("")
W("- **Mine** – extracts a raw good from an asteroid with no inputs (also **Oil Rig**).")
W("- **Collector** – gathers gases or other goods from the environment with no inputs.")
W("- **Factory** – the standard converter: consumes ingredients to make products.")
W("- **Farm** / **Ranch** – agricultural producers (crops, livestock), usually needing Water.")
W("- **SolarPowerPlant** – produces Energy Cells from sunlight.")
W("")
W("## Factory cost")
W("")
W("The cost to **found** a factory is based on how much value its recipe adds – the difference between the")
W("value of one cycle's outputs and its inputs:")
W("")
W("$$\\text{cost} = 2{,}500{,}000 + 3500 \\times (\\text{output value} - \\text{input value})$$")
W("")
W("with a minimum of **2,500,000** credits. The cost to **upgrade** an existing factory to a larger size adds")
W("byproduct value to the outputs and scales with the target size:")
W("")
W("$$\\text{upgrade cost} = 1000 \\times \\text{size} \\times (\\text{output value} + \\text{byproduct value} - \\text{input value})$$")
W("")
W("The *Build cost* column below applies the founding formula using base good prices.")
W("")
W("## Production recipes")
W("")
W("All %d production recipes. Quantities are per production cycle." % len(recipes))
W("")
W("| Factory | Type | Requires | Produces | Byproducts | Build cost |")
W("|---|---|---|---|---|--:|")
for r in recipes:
    W("| %s | %s | %s | %s | %s | %s |" % (
        resolve_name(r), r["style"], fmt_items(r["ings"], opt=True),
        fmt_items(r["ress"]), fmt_items(r["gars"]), money(build_cost(r))))
W("")
W("## Picking a factory")
W("")
W("- **Simplest starters:** **Mines**, **Collectors** and **Solar Power Plants** take **no inputs**, so they")
W("  never stall waiting on supply — pure output you just collect and sell. A good first investment while")
W("  you learn the loop.")
W("- **Build a short chain:** pick two or three recipes where one's **output is the next's input** (e.g.")
W("  a metal → component → device line). Feeding your own factories cuts out the middleman and multiplies")
W("  the value you add.")
W("- **Site it where it's wanted:** found a factory in a region that already **demands** its product (and")
W("  has cheap **inputs** nearby). Local supply/demand sets the price — see [Trading and Prices](Trading-and-Prices).")
W("- **Mind the founding cost:** the *Build cost* column scales with how much value a recipe adds, so")
W("  high-value tech/military factories are expensive but lucrative; basic producers are cheap to start.")
W("- Stock and tax for player-owned factories are covered on [Player stations](Player-stations).")
W("")
W("## See also")
W("")
W("- [Goods](Goods) – the commodities produced and consumed here")
W("- [Trading and Prices](Trading-and-Prices) – how outputs are priced when sold")
W("- [Refining](Refining) – turning ores and scrap into materials")
W("- [Consumer goods](Consumer-goods) – what population stations consume")
W("")
W("---")
W("*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods)*")

open("wiki/pages/Production.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote wiki/pages/Production.md | recipes=%d" % len(recipes))
