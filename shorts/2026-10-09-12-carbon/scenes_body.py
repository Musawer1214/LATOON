import random
COP, AMB, SAGE, ROSE = (204, 104, 72), (232, 172, 62), (126, 172, 140), (196, 96, 96)
NUC = {"A": (232, 172, 62), "C": (126, 172, 140), "G": (204, 104, 72), "T": (150, 150, 200)}
GOLD = COP; BL, BL2 = COP, COP
def dna_str(n, seed):
    r = random.Random(seed); return "".join(r.choice("ACGT") for _ in range(n))
def tile(cv, x, y, ch, s, a=1, col=None):
    c = col or NUC[ch]
    cv.rrect(x - s / 2, y - s / 2 + 4, x + s / 2, y + s / 2 + 4, s * .22, fill=SHAD, a=.5 * a)
    cv.rrect(x - s / 2, y - s / 2, x + s / 2, y + s / 2, s * .22, fill=c, a=a)
    cv.text(x, y + 1, ch, s * .62, (28, 36, 32), a, "Black")
def strip(cv, y, seq, off, s, a=1, hl=None, dim=.35, hlcol=None):
    # scrolling letter strip; hl = list of (i0,i1) index ranges highlighted
    gap = s * 1.12; n0 = int(off // gap) - 1
    for k in range(n0, n0 + int(1200 / gap) + 3):
        x = 540 + (k * gap - off) - 540 + 0
        x = k * gap - off
        if x < -30 or x > 1110: continue
        ch = seq[k % len(seq)]
        on = hl is None or any(i0 <= k <= i1 for i0, i1 in hl)
        tile(cv, x, y, ch, s, a * (1 if on else dim), hlcol if (hl and on and hlcol) else None)
def s0(cv, t, D):
    kinetic(cv, t, 320, "READ IN A DAY", 96, INKC, -.2, "Black", .02)
    kinetic(cv, t, 430, "UNDERSTOOD? NO.", 80, COP, -.1, "Black", .02)
    seq = dna_str(400, 5)
    for r in range(7):
        y = 640 + r * 108
        sp = (90 + r * 30) * (1 if r % 2 == 0 else -1)
        strip(cv, y, seq[r * 50:] + seq[:r * 50], 400 + t * sp, 72, eo(pr(t, .05 * r, .05 * r + .5)) * (1 - .1 * abs(r - 3)))
    cv.rrect(250, 1352, 830, 1428, 38, fill=CARDC, outline=LINEC, w=3)
    n = int(3_000_000_000 * eio(pr(t, .3, 3.6)))
    cv.text(540, 1390, f"{n:,} letters", 38, AMB, 1, "Black")
def s1(cv, t, D):
    head(cv, t, "WHERE ARE THE GENES?", "recipes for proteins")
    seq = dna_str(300, 9)
    hl = [(12, 26), (40, 49), (63, 80)]
    off = 300 + t * 70
    p = eo(pr(t, .3, 1.0))
    for r in range(3):
        strip(cv, 640 + r * 130, seq[r * 70:] + seq[:r * 70], off * (1 if r != 1 else -1) + (700 if r == 1 else 0), 78, p, None)
    # center card with a gene
    card(cv, 70, 1040, 1010, 1400, 34)
    cv.text(110, 1090, "GENE = A READABLE STRETCH", 30, MUTE, eo(pr(t, 2.5, 3.0)), "Black", anchor="lm")
    s = 62
    chars = "ATGGCTAAGCTTTAA"
    for i, ch in enumerate(chars):
        a = eback(pr(t, 3.0 + i * .08, 3.5 + i * .08), 2)
        col = SAGE if i < 3 else (ROSE if i >= 12 else None)
        tile(cv, 130 + i * 72, 1190, ch, s, cl(a), col)
    cv.text(202, 1270, "START", 30, SAGE, eo(pr(t, 4.2, 4.7)), "Black")
    cv.text(850, 1270, "STOP", 30, ROSE, eo(pr(t, 4.5, 5.0)), "Black")
    cv.text(540, 1345, "finding it took experts + lab data", 36, INKC, eo(pr(t, 6.5, 7.2)), "Bold")
def s2(cv, t, D):
    head(cv, t, "CARBON-A", "open model · Hugging Face", AMB)
    seq = dna_str(300, 12)
    off = 200 + t * 120
    strip(cv, 1000, seq, off, 80, 1, None)
    # scanning window with prediction bars
    cx = 540
    cv.rrect(cx - 250, 920, cx + 250, 1080, 24, outline=AMB, w=5)
    for i in range(24):
        x = cx - 240 + i * 20.8
        hgt = 40 + 70 * (math.sin(i * .45 + t * 1.5) * .5 + .5) * (1 if 6 < i < 18 else .25)
        cv.rrect(x, 880 - hgt, x + 14, 880, 5, fill=AMB if 6 < i < 18 else LINEC, a=eo(pr(t, .8, 1.4)))
    cv.text(540, 740, "GENE?", 54, INKC, eo(pr(t, 1.0, 1.5)), "Black")
    cv.text(540, 1180, "raw DNA in  ->  gene map out", 40, INKC, eo(pr(t, 2.0, 2.6)), "Bold")
    chip(cv, 200, 1260, 680, "NO SPECIES-SPECIFIC EXPERT", COP, eo(pr(t, 3.0, 3.6)), size=30, h=80)
def s3(cv, t, D):
    head(cv, t, "1.2 BILLION PARAMETERS", "one model", AMB)
    seq = dna_str(400, 21)
    p = eo(pr(t, .2, .8))
    strip(cv, 900, seq, 200 + t * 60, 56, p * .45, None)
    w = lerp(120, 940, eio(pr(t, .6, 3.2)))
    cv.rrect(540 - w / 2, 810, 540 + w / 2, 990, 30, outline=AMB, w=6, oa=p)
    n = int(98304 * eio(pr(t, .6, 3.2)))
    cv.text(540, 1130, f"{n:,}", 130, INKC, eo(pr(t, .6, 1.0)), "Black")
    cv.text(540, 1240, "letters read at once", 44, AMB, eo(pr(t, 1.4, 2.0)), "Bold")
    cv.text(540, 1330, "both strands, letter by letter", 34, MUTE, eo(pr(t, 2.6, 3.2)), "SemiBold")
def s4(cv, t, D):
    head(cv, t, "ONE MODEL, ALL LIFE", "no expert per species", AMB)
    items = [("cat", "MAMMALS", 190), ("roo", "BIRDS", 540), ("ara", "PLANTS", 890)]
    for i, (k, lab, x) in enumerate(items):
        p = eback(pr(t, .2 + i * .5, .9 + i * .5), 2)
        cv.rrect(x - 150 + 8, 560 + 12, x + 150 + 8, 960 + 12, 28, fill=SHAD, a=.5 * cl(p))
        kenburns(cv, k, x, 760, 300, 400, 1.0 + .1 * pr(t, 0, D), 28, cl(p), panx=(-.2 if k != "ara" else 0))
        cv.rrect(x - 150, 560, x + 150, 960, 28, outline=LINEC, w=3, oa=cl(p))
        cv.text(x, 1000, lab, 32, AMB, eo(pr(t, .8 + i * .5, 1.3 + i * .5)), "Black")
    chip(cv, 260, 1100, 560, "+ FUNGI  + PROTISTS", COP, eo(pr(t, 2.4, 3.0)), size=34, h=84)
    cv.text(540, 1260, "same weights, every kingdom", 40, INKC, eo(pr(t, 3.4, 4.0)), "Bold")
    cv.text(540, 1560 - 20, "", 20, INKC, 0)
    cv.text(540, 1330, "Photos: Wikimedia Commons (CC BY-SA)", 24, MUTE, eo(pr(t, 1.5, 2.0)), "SemiBold")
def s5(cv, t, D):
    head(cv, t, "A RULE-BREAKING MICROBE", "Tetrahymena thermophila", AMB)
    p = eback(pr(t, .1, .8), 2)
    cv.rrect(90 + 8, 480 + 12, 990 + 8, 900 + 12, 30, fill=SHAD, a=.5 * cl(p))
    kenburns(cv, "tet", 540, 690, 900, 420, 1.0 + .12 * pr(t, 0, D), 30, cl(p))
    cv.rrect(90, 480, 990, 900, 30, outline=LINEC, w=4, oa=cl(p))
    q = eio(pr(t, 2.4, 3.4))
    for i, cod in enumerate(["UAA", "UAG"]):
        x = 290 + i * 500
        col = mix(ROSE, SAGE, q)
        cv.rrect(x - 130, 1010, x + 130, 1110, 26, fill=col, a=eo(pr(t, 1.2 + i * .3, 1.8 + i * .3)))
        cv.text(x, 1060, cod, 54, (28, 36, 32), eo(pr(t, 1.2 + i * .3, 1.8 + i * .3)), "Black")
        cv.text(x, 1160, "STOP" if q < .5 else "GLUTAMINE (Q)", 34, ROSE if q < .5 else SAGE, eo(pr(t, 1.6, 2.2)), "Black")
    cv.text(540, 1290, "it still scored 0.960 F1", 50, INKC, eo(pr(t, 3.6, 4.2)), "Black")
    cv.text(540, 1360, "without a custom model", 36, MUTE, eo(pr(t, 4.2, 4.8)), "SemiBold")
def s6(cv, t, D):
    head(cv, t, "AT GENBANK SCALE", "Carbon Annotation Database", AMB)
    cv.text(540, 640, f"{int(48167 * eio(pr(t, .2, 2.4))):,}", 120, INKC, eo(pr(t, .1, .5)), "Black")
    cv.text(540, 740, "genome assemblies", 42, AMB, eo(pr(t, .4, .9)), "Bold")
    rs = random.Random(3)
    for i in range(160):
        a = eo(pr(t, 1.0 + i * .008, 1.4 + i * .008))
        x = 120 + (i % 20) * 42; y = 830 + (i // 20) * 42
        cv.circ(x, y, 13, fill=[SAGE, AMB, COP][rs.randint(0, 2)], a=a)
    cv.text(540, 1250, f"{int(566e6 * eio(pr(t, 3.2, 5.4))):,}", 104, COP, eo(pr(t, 3.0, 3.5)), "Black")
    cv.text(540, 1345, "possible protein-coding genes", 40, INKC, eo(pr(t, 3.4, 4.0)), "Bold")
def s7(cv, t, D):
    head(cv, t, "LAB CHECK", "full RNA reads from living cells", AMB)
    items = [("cat", "CAT", 190), ("roo", "CHICKEN", 540), ("ara", "ARABIDOPSIS", 890)]
    for i, (k, lab, x) in enumerate(items):
        p = eback(pr(t, .1 + i * .3, .7 + i * .3), 2)
        cv.rrect(x - 140, 540, x + 140, 840, 26, fill=SHAD, a=.4 * cl(p))
        kenburns(cv, k, x, 690, 280, 300, 1.0, 26, cl(p), panx=0)
        cv.rrect(x - 140, 540, x + 140, 840, 26, outline=LINEC, w=3, oa=cl(p))
        cv.text(x, 880, lab, 28, AMB, eo(pr(t, .5 + i * .3, 1.0 + i * .3)), "Black")
    card(cv, 90, 960, 990, 1360, 34)
    rows = [("REFERENCE LIST", "gene missing", ROSE), ("CARBON-A", "gene predicted", AMB), ("LAB RNA DATA", "gene supported", SAGE)]
    for i, (a_, b_, c_) in enumerate(rows):
        pp = eo(pr(t, 1.8 + i * .7, 2.4 + i * .7))
        y = 1040 + i * 105
        cv.text(130, y, a_, 30, MUTE, pp, "Black", anchor="lm")
        cv.text(950, y, b_, 34, c_, pp, "Black", anchor="rm")
    cv.text(540, 1440, "", 10, INKC, 0)
def s8(cv, t, D):
    kinetic(cv, t, 330, "CANDIDATES,", 96, INKC, -.1, "Black", .02)
    kinetic(cv, t, 440, "NOT PROOF", 96, COP, .0, "Black", .02)
    steps = [("RNA", "supported", SAGE, 1), ("PROTEIN", "next test", AMB, 0), ("FUNCTION", "unknown", ROSE, 0)]
    for i, (a_, b_, c_, done) in enumerate(steps):
        x = 190 + i * 350; p = eback(pr(t, .6 + i * .5, 1.2 + i * .5), 2)
        cv.circ(x, 820, 96 * cl(p), fill=c_ if done else CARDC, a=cl(p), outline=c_, w=6, oa=cl(p))
        if done: check(cv, x, 820, 52, pr(t, 1.2, 1.8), (28, 36, 32), 12)
        else: cv.text(x, 820, "?", 100, c_, cl(p), "Black")
        cv.text(x, 970, a_, 36, INKC, eo(pr(t, 1.0 + i * .5, 1.5 + i * .5)), "Black")
        cv.text(x, 1020, b_, 30, MUTE, eo(pr(t, 1.2 + i * .5, 1.7 + i * .5)), "SemiBold")
        if i < 2: cv.line([(x + 110, 820), (x + 240, 820)], LINEC, 6, eo(pr(t, 1.0 + i * .5, 1.6 + i * .5)))
    cv.text(540, 1250, "the map of life just got more readable", 40, INKC, eo(pr(t, 2.6, 3.4)), "Bold")
    p = eo(pr(t, 3.4, 4.2))
    cv.text(540, 1340, "LATOON", 70, AMB, p, "Black")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
