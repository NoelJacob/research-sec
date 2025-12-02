ENERGY_STEMS = [
    # Power & Energy basics
    r"electr",  # electric, electrical, electricity
    # power — prevent: voting, proxy, attorney, bargaining, purchasing, market
    r"(?<!voting )(?<!proxy )(?<!attorney )(?<!bargaining )(?<!purchasing )(?<!market )power",
    # energy — prevent physics & sentiment contexts
    r"(?<!kinetic )(?<!potential )(?<!negative )(?<!positive )energ",
    r"watt",
    # volt — avoid "revolt", "revolting"
    r"(?<!re)volt",
    # amp — avoid prefixes: ex, sw, cl, st, tr, d  (all fixed width)
    r"(?<!ex)(?<!sw)(?<!cl)(?<!st)(?<!tr)(?<!d)amp(?!le|lif)",
    r"joule",
    r"btu",
    # therm — avoid "isotherm"
    r"(?<!iso)therm",
    # Units
    r"kwh",
    r"mwh",
    r"gwh",
    r"twh",
    # Mining
    r"(?<!re)hash",  # avoid "rehash"
    r"\basic\b",  # ASIC
    # Generation & Sources
    # avoid: de + generat, re + generat
    r"(?<!de)(?<!re)generat",
    r"solar",
    # wind — avoid: headwind, tailwind, downwind, crosswind
    r"(?<!head)(?<!tail)(?<!down)(?<!cross)wind",
    r"hydro",
    r"nuclear",
    # coal — avoid "charcoal"
    r"(?<!char)coal",
    r"geotherm",
    # bio — avoid symbio-, aerobio-
    r"(?<!sym)(?<!aero)bio",
    r"flare",
    r"renewab",
    r"fossil",
    # fuel — avoid "refuel"
    r"(?<!re)fuel",
    # Infrastructure
    r"\bgrid\b",
    r"substation",
    r"transformer",
    r"transmiss",
    r"data[ -]?center",
    r"facilit",
    r"interconnect",
    # Cooling & Efficiency
    r"(?<!over)cool",
    r"hvac",
    r"pue",
    r"immersion",
    # heat — avoid "reheat"
    r"(?<!re)heat",
    # Costs & Contracts
    r"utilit",
    r"tariff",
    r"\bppa\b",
    r"curtail",
    r"wholesale",
    # Environmental
    r"\bepa\b",
    r"carbon",
    r"co2",
    r"emission",
    r"greenhouse",
    r"ghg",
    r"sustainab",
    r"esg",
    r"footprint",
    r"net[ -]?zero",
    r"scope [123]",
    # natural — avoid super-, unnat-, preter-
    r"(?<!super)(?<!unnat)(?<!preter)natural",
    r"\bnature\b",
    r"environment",
    # Storage & Backup
    r"batter(?:y|ies)",
    # storage — avoid cold storage, data storage
    r"(?<!cold )(?<!data )storage",
    r"\bups\b",
    r"diesel",
    r"backup",
    # Regulatory
    r"\bercot\b",
    r"\bferc\b",
    r"\bpjm\b",
    r"\bnerc\b",
    r"\biso\b",
    r"\brto\b",
    # Consumption terms
    r"consum",
    r"usage",
    r"utiliz",
    r"efficien",
    # capacity — avoid in-, over-
    r"(?<!in)(?<!over)capacity",
    # load — avoid: download, upload, workload, payload
    r"(?<!down)(?<!up)(?<!work)(?<!pay)load",
    # demand — avoid on-demand, on demand
    r"(?<!on-)(?<!on )demand",
    # supply — avoid money, blood, water, food, labor
    r"(?<!money )(?<!blood )(?<!water )(?<!food )(?<!labor )supply",
    r"procure",
]
