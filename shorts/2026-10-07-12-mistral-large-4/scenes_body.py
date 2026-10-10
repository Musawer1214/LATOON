
# ---- S0 hook: 1,000 cells = 1 trillion params; almost all dark, 49 wake
GX0, GY0, GP = 540 - 39 * 23 / 2, 640, 23
def cellpos(k): return GX0 + (k % 40) * GP, GY0 + (k // 40) * GP
LIT = sorted(range(1000), key=lambda k: (k * 7919) % 1000)[:49]
def s0(cv, t, D):
    chip(cv, 540, 300, "MISTRAL LARGE 4  ·  NEW MODEL", 32, (30, 10, 5), AMB, 1)
    kinetic(cv, t, 420, "1 TRILLION", 112, WHT, -.3, "Black", .02)
    cv.text(540, 520, "PARAMETERS", 48, ORG2, 1, "Black")
    litset = set(LIT)
    for k in range(1000):
        x, y = cellpos(k)
        wave = pr(t, -.3 + (k % 40) * .012 + (k // 40) * .006, .5 + (k % 40) * .012 + (k // 40) * .006)
        on = k in litset and t > 1.9 + (LIT.index(k) % 7) * .05
        if on:
            f = eo(pr(t, 1.9 + (LIT.index(k) % 7) * .05, 2.3 + (LIT.index(k) % 7) * .05))
            cv.rrect(x - 9, y - 9, x + 9, y + 9, 4, fill=mix(DIM, ORG, f), a=1)
        else:
            cv.rrect(x - 8, y - 8, x + 8, y + 8, 4, fill=DIM, a=.75 * wave)
    q = eo(pr(t, 2.1, 2.6))
    cv.text(540, 1300, "MOST OF IT STAYS ASLEEP", 54, CREAM, q, "Black")
    cv.text(540, 1365, "1 cell = 1 billion parameters", 28, MUT, q, "Medium")

# ---- S1 Mistral Large 4 + le Chonk (real hero image from Mistral's launch post)
def s1(cv, t, D):
    p = eo(pr(t, .05, .6))
    shadow(cv, 90, 480, 990, 1040, 40, p)
    zoomcard(cv, "hero", 540, 760, 900, 560, 900 + 300 * pr(t, 0, D), 470, 1.05 + .25 * pr(t, 0, D), 40, p)
    cv.rrect(90, 480, 990, 1040, 40, outline=ORG, w=3, oa=.6 * p)
    kinetic(cv, t, 760, "MISTRAL", 120, WHT, .25, "Black", .04)
    kinetic(cv, t, 880, "LARGE 4", 120, ORG, .5, "Black", .04)
    chip(cv, 540, 310, "PUBLIC PREVIEW  ·  OCT 6, 2026", 32, (30, 10, 5), AMB, eo(pr(t, 0, .3)))
    q = eback(pr(t, 3.9, 4.5), 2.2)
    cv.text(540, 1180, "aka", 34, MUT, cl(q), "Medium")
    cv.text(540, 1290, "“LE CHONK”", 110, AMB, cl(q), "Black")
    cv.text(540, 1390, "image: © Mistral AI", 22, MUT, .8, "Medium")

# ---- S2 ring: 49B of 1T awake
def s2(cv, t, D):
    cv.text(540, 320, "ACTIVE AT ANY MOMENT", 56, WHT, eo(pr(t, .05, .4)), "Black")
    cx, cy, R = 540, 840, 320
    cv.circ(cx, cy, R, outline=DIM, w=46, oa=1)
    frac = .049 * eo(pr(t, 1.9, 3.0))
    cv.arc(cx, cy, R, 0, 360 * max(frac, .0001), ORG, 46)
    for k in range(3): cv.circ(cx, cy, R + 50 + k * 26 + 6 * math.sin(t * 2 + k), outline=ORG, w=2, oa=.15 * eo(pr(t, 2.5, 3)))
    cv.text(cx, cy - 20, "49B", 170, ORG, eo(pr(t, 1.9, 2.5)), "Black")
    cv.text(cx, cy + 90, "active", 44, CREAM, eo(pr(t, 2.1, 2.6)), "SemiBold")
    n = int(1000 * eo(pr(t, .2, 1.6)))
    cv.text(540, 1270, f"{n:,}B".replace("1,000B", "1,000B"), 90, DIM if t > 1.9 else ORG2, 1, "Black")
    cv.text(540, 1345, "total parameters", 34, MUT, eo(pr(t, .3, .7)), "SemiBold")

# ---- S3 MoE routing (illustrative)
EXP = [(150 + (i % 4) * 260, 1040 + (i // 4) * 150) for i in range(8)]
TOK = [("The", [1, 6]), ("cat", [3, 4]), ("sat", [0, 7]), ("down", [2, 5])]
def s3(cv, t, D):
    cv.text(540, 310, "MIXTURE OF EXPERTS", 60, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 375, "a router picks who works on each token", 30, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    cycle = 1.1; ti = int(max(0, t - 1.3) // cycle) % 4 if t > 1.3 else -1
    u = ((t - 1.3) % cycle) / cycle if t > 1.3 else 0
    # router box
    rp = eback(pr(t, .4, 1.0), 2)
    cv.rrect(290, 660, 790, 780, 40, fill=(50, 22, 12), a=cl(rp), outline=ORG, w=5, oa=cl(rp))
    cv.text(540, 720, "ROUTER", 54, ORG, cl(rp), "Black")
    ep = eback(pr(t, .7, 1.3), 1.6)
    active = TOK[ti][1] if ti >= 0 else []
    for i, (ex, ey) in enumerate(EXP):
        on = i in active and u > .35 and u < .95
        f = (eo(pr(u, .35, .5)) * (1 - eo(pr(u, .85, .95)))) if i in active else 0
        col = mix(DIM, ORG, f)
        cv.rrect(ex - 95, ey - 48, ex + 95, ey + 48, 22, fill=mix((40, 20, 14), (255, 112, 30), f * .85), a=cl(ep), outline=mix((100, 60, 44), AMB, f), w=4, oa=cl(ep))
        cv.text(ex, ey, f"E{i+1}", 44, mix(MUT, WHT, f), cl(ep), "Black")
        if f > .02:
            cv.circ(ex, ey, 60 + 18 * f, outline=ORG2, w=3, oa=.25 * f)
    if ti >= 0:
        w_, ex_ = TOK[ti]
        # token drops into router
        ty = lerp(500, 660, eo(pr(u, 0, .25)))
        if u < .3:
            chip(cv, 540, ty, w_, 46, (30, 10, 5), AMB, 1 - pr(u, .22, .3))
        for i in ex_:
            ex, ey = EXP[i]
            pp = eo(pr(u, .2, .5))
            x0, y0 = 540, 780
            cv.line([(x0, y0), (lerp(x0, ex, pp), lerp(y0, ey - 48, pp))], AMB, 6, (1 - pr(u, .8, .95)))
    cv.text(540, 1370, "only 2 of 8 experts fire per token  ·  illustration", 26, MUT, eo(pr(t, 1.2, 1.6)), "Medium")

# ---- S4 giant's knowledge, small model's cost
def s4(cv, t, D):
    cv.text(540, 310, "GIANT KNOWLEDGE", 68, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "small-model running cost", 46, ORG2, eo(pr(t, .3, .7)), "Black")
    base = 1300
    g1 = eo(pr(t, .3, 1.3)); g2 = eo(pr(t, 1.3, 2.1))
    cv.rrect(170, base - 700 * g1, 500, base, 24, fill=mix((120, 60, 30), ORG, g1), a=1)
    cv.rrect(580, base - 700 * .049 * g2 * 1.0 - 10 * g2, 910, base, 24, fill=AMB, a=1)
    cv.text(335, base - 700 * g1 - 50, "1T", 80, ORG, eo(pr(t, .9, 1.3)), "Black")
    cv.text(745, base - 60 * g2 - 90, "49B", 80, AMB, eo(pr(t, 1.8, 2.3)), "Black")
    cv.text(335, base + 55, "stored", 36, CREAM, 1, "SemiBold")
    cv.text(745, base + 55, "used per token", 36, CREAM, 1, "SemiBold")
    cv.text(540, 1410, "roughly: cost tracks active parameters", 24, MUT, eo(pr(t, 2.2, 2.6)), "Medium")

# ---- S5 training: 3,800 GPUs
NG = 3800; GC, GR = 76, 50
def s5(cv, t, D):
    cv.text(540, 300, "TRAINED FROM SCRATCH", 58, WHT, eo(pr(t, .05, .4)), "Black")
    n = int(NG * eo(pr(t, 1.3, 3.6)))
    x0, y0, pp = 540 - 75 * 12 / 2, 560, 12
    for k in range(NG):
        x, y = x0 + (k % GC) * pp, y0 + (k // GC) * pp
        lit = k < n
        w_ = math.sin(t * 5 - k * .05) * .5 + .5
        cv.rrect(x - 4, y - 4, x + 4, y + 4, 2, fill=mix(DIM, ORG, (.5 + .5 * w_) if lit else 0) if lit else (54, 32, 26), a=1 if lit else .55)
    cv.text(540, 1235, f"{n:,}", 140, ORG, eo(pr(t, 1.2, 1.6)), "Black")
    cv.text(540, 1345, "NVIDIA GRACE BLACKWELL GPUs", 38, CREAM, eo(pr(t, 1.6, 2.0)), "Bold")
    q = eo(pr(t, 4.4, 5.0))
    chip(cv, 540, 1425, "OWN DATA CENTRES IN EUROPE", 28, (30, 10, 5), AMB, q)

# ---- S6 Cybench chart (Mistral's own published chart)
def s6(cv, t, D):
    cv.text(540, 305, "CYBENCH", 72, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 375, "40 security challenges", 36, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    p = eo(pr(t, .2, .8))
    shadow(cv, 70, 450, 1010, 1070, 36, p)
    z = 1.0 + .3 * eio(pr(t, 3.0, 4.6))
    zoomcard(cv, "cyber", 540, 760, 940, 620, 700 - 140 * eio(pr(t, 3.0, 4.6)), 600, z, 36, p)
    cv.rrect(70, 450, 1010, 1070, 36, outline=ORG, w=3, oa=.6 * p)
    m = eback(pr(t, 4.0, 4.6), 2)
    cv.text(540, 1230, "93%", 210, ORG, cl(m), "Black")
    cv.text(540, 1370, "solved · Mistral's own reported score", 32, CREAM, eo(pr(t, 4.4, 4.9)), "SemiBold")
    cv.text(540, 1425, "chart: © Mistral AI", 22, MUT, .8, "Medium")

# ---- S7 weights: end of October
def s7(cv, t, D):
    cv.text(540, 310, "OPEN WEIGHTS", 76, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 385, "due by the end of October", 38, ORG2, eo(pr(t, .3, .7)), "SemiBold")
    padlock(cv, 540, 640, 230, eo(pr(t, 1.4, 2.2)), ORG, eo(pr(t, .2, .6)))
    # October 2026 calendar (Oct 1 = Thursday)
    cx0, cy0, cw, ch = 110, 860, 120, 86
    cv.rrect(80, 790, 1000 - 0, 1330, 30, fill=(28, 12, 8), outline=DIM, w=3)
    for i, d in enumerate("MTWTFSS"): cv.text(cx0 + i * cw + 30, 830, d, 30, MUT, 1, "Bold")
    for day in range(1, 32):
        idx = day - 1 + 3; r, c = idx // 7, idx % 7
        x, y = cx0 + c * cw + 30, 900 + r * ch
        last = day >= 26
        hl = eo(pr(t, 1.0, 1.6)) if last else 0
        if last and hl > 0:
            cv.rrect(x - 44, y - 34, x + 44, y + 34, 16, fill=ORG, a=hl * (.75 + .25 * math.sin(t * 6)))
        cv.text(x, y, str(day), 34, mix((160, 140, 130), WHT, hl), 1, "Bold")

# ---- S8 the catch
def s8(cv, t, D):
    kinetic(cv, t, 320, "THE CATCH", 92, AMB, .0, "Black", .04)
    p = eo(pr(t, .3, 1.0))
    cv.rrect(140, 470, 940, 930, 36, fill=(30, 14, 9), a=p, outline=DIM, w=3, oa=p)
    for i, (h, nm) in enumerate([(300, "A"), (380, "ML4"), (230, "B"), (330, "C")]):
        x = 240 + i * 210; g = eo(pr(t, .5 + i * .12, 1.2 + i * .12))
        col = ORG if nm == "ML4" else (150, 125, 108)
        cv.rrect(x - 60, 880 - h * g, x + 60, 880, 14, fill=col, a=p)
    s = eback(pr(t, 1.3, 1.8), 2.4)
    if s > .02:
        ang = -8 * math.pi / 180
        cx, cy = 540, 690; hw, hh = 330 * cl(s), 56 * cl(s)
        pts = [(cx + x * math.cos(ang) - y * math.sin(ang), cy + x * math.sin(ang) + y * math.cos(ang)) for x, y in [(-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh)]]
        cv.poly(pts, (30, 10, 5), .85 * cl(s))
        cv.line(pts + [pts[0]], RED, 6, cl(s))
        cv.text(cx, cy, "SELF-REPORTED", 56 * cl(s), RED, cl(s), "Black")
    q = eo(pr(t, 2.9, 3.4))
    cv.rrect(140, 1030, 940, 1210, 36, fill=(30, 14, 9), a=q, outline=AMB, w=4, oa=q)
    cv.text(470, 1095, "INDEPENDENT TESTS", 44, CREAM, q, "Black")
    cv.text(470, 1155, "replication pending", 32, MUT, q, "Medium")
    cv.arc(820, 1120, 42, (t * 320) % 360, (t * 320) % 360 + 260, AMB, 10, q)

# ---- S9 outro
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(1000):
        x = 90 + (k % 40) * 22.3; y = 470 + (k // 40) * 17
        on = ((k * 7919) % 1000) < 49
        cv.rrect(x - 6, y - 5, x + 6, y + 5, 3, fill=ORG if on else DIM, a=(.9 if on else .35) * p)
    kinetic(cv, t, 1000, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1130, "Voyaging the Unseen", 46, AMB, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1230, "would you self-host a trillion-parameter model?", 30, ORG2, eo(pr(t, 1.8, 2.3)), "Medium")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
