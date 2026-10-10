from common import *
from scenes_b import deep_bg, cone, HEX
from scenes_a import nucleus

TIMECOL = [OCHRE, TERRA, PLUM]
def tcol(u):
    return mix(TIMECOL[0], TIMECOL[1], u * 2) if u < .5 else mix(TIMECOL[1], TIMECOL[2], (u - .5) * 2)

# ------------------------------------------------------------ DIRECTION
GRID = [(330 + i * 125, 250 + j * 52) for i in range(10) for j in range(14)]
TR0, TR1 = (1650, 140), (260, 1000)   # true muon track (from upper right)
def _track_param(x, y):
    dx, dy_ = TR1[0] - TR0[0], TR1[1] - TR0[1]; L = math.hypot(dx, dy_)
    s = ((x - TR0[0]) * dx + (y - TR0[1]) * dy_) / L
    d = abs((x - TR0[0]) * dy_ - (y - TR0[1]) * dx) / L
    return s / L, d

def scene_direction(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    t2 = b(1)
    A1 = win(t, 0, t2 + .3, .5, .7); A2 = win(t, t2, S["dur"] + 1, .7, .5)
    if A1 > 0:
        cv.ga = A1
        deep_bg(cv, A1)
        chapter_tag(cv, "10", "Connect the dots", 1)
        tt = b.kw(0, "Timing"); tc = b.kw(0, "Connect"); tf = b.kw(0, "Follow it")
        sweep = pr(t, tt - .3, tt + 4.5) * 1.15 - .05
        hits = []
        for (x, y) in GRID:
            s, d = _track_param(x, y)
            arr = s + d / 2600
            lit = d < 230 and sweep > arr
            col = tcol(cl(arr))
            if lit:
                q = eo(pr(sweep, arr, arr + .04))
                hits.append((x, y, arr))
                dom(cv, x, y, 9 + 9 * (1 - d / 230) * q, 1, lit=q, litc=col)
            else:
                dom(cv, x, y, 8, .9)
        # the wavefront (faint), only while sweeping
        if 0 < sweep < 1.05:
            mx = lerp(TR0[0], TR1[0], cl(sweep)); my = lerp(TR0[1], TR1[1], cl(sweep))
            ang = math.atan2(TR1[1] - TR0[1], TR1[0] - TR0[0])
            L = 300; fa = 1 - pr(sweep, .9, 1.05)
            e1 = (mx + L * math.cos(ang + math.pi + math.radians(41)), my + L * math.sin(ang + math.pi + math.radians(41)))
            e2 = (mx + L * math.cos(ang + math.pi - math.radians(41)), my + L * math.sin(ang + math.pi - math.radians(41)))
            cv.poly([(mx, my), e1, e2], CHER2, .22 * fa)
            cv.line([e1, (mx, my), e2], CHER, 3, .7 * fa)
            cv.circ(mx, my, 7, fill=INK, a=.8 * fa)
        qc = eo(pr(t, tc, tc + 1.6))
        if qc > 0 and hits:
            hs = sorted(hits, key=lambda h: h[2])
            n = max(2, int(len(hs) * qc))
            p0, p1 = (TR1[0], TR1[1]), (TR0[0], TR0[1])
            dashed(cv, [(lerp(p0[0], p1[0], .05), lerp(p0[1], p1[1], .05)), (lerp(p0[0], p1[0], .05 + .9 * qc), lerp(p0[1], p1[1], .05 + .9 * qc))], INK, 4, qc, 22, 10)
        qf = eo(pr(t, tf, tf + 1.4))
        if qf > 0:
            ex, ey = lerp(TR0[0], TR0[0] + 150, qf), lerp(TR0[1], TR0[1] - 92, qf)
            cv.arrow(TR0[0], TR0[1], ex, ey, INK, 4, qf, 22)
            panel(cv, 1500, 160, 1830, 300, qf)
            for k in range(5):
                a_ = k * 1.2566 - 1.57
                cv.poly([(1560 + 22 * math.cos(a_ + d_), 230 + 22 * math.sin(a_ + d_)) for d_ in (0, .63, 1.26)] , OCHRE, qf)
            cv.circ(1560, 230, 12, fill=OCHRE, a=qf)
            cv.text(1600, 230, "a spot in the sky", 26, INK, qf, "Bold", "lm")
        # legend: time colours
        ql = eo(pr(t, tt + 1, tt + 2))
        panel(cv, 110, 940, 640, 1020, ql)
        for k in range(30):
            cv.rect(140 + k * 8, 966, 148 + k * 8, 990, fill=tcol(k / 29), a=ql)
        cv.text(400, 978, "earlier  →  later", 22, INK2, ql, "SemiBold", "lm")
        cv.ga = 1
    if A2 > 0:
        cv.ga = A2
        chapter_tag(cv, "11", "The Earth as a shield", 1)
        ta = b.kw(1, "Particles"); tl = b.kw(1, "looks down"); tn = b.kw(1, "Almost nothing")
        cx, cy, R = 960, 1700, 1180
        for rr, c in [(1.0, (172, 150, 110)), (.94, (196, 120, 78)), (.55, (214, 152, 72))]:
            cv.circ(cx, cy, R * rr, fill=c, a=1)
        cv.circ(cx, cy, R, outline=INK, w=3, a=1)
        cv.circ(cx, cy, R + 40, outline=CHER2, w=26, a=.25)   # atmosphere band
        px, py = cx, cy - R
        cv.rect(px - 50, py, px + 50, py + 60, fill=ICE, a=1, outline=INK, w=2.5)
        cv.text(px, py + 100, "IceCube", 24, INK, 1, "Bold")
        # atmospheric rain from above
        qa = eo(pr(t, ta - .3, ta + .5))
        rng = np.random.default_rng(31)
        for k in range(70):
            x = px + rng.uniform(-420, 420); ph = (t * .9 + rng.random()) % 1
            y = lerp(150, py, ph)
            if abs(x - px) < 60 or rng.random() < .6:
                cv.line([(x, y - 26), (x, y)], OCHRE, 3, qa * .8)
        panel(cv, 110, 180, 600, 330, qa)
        cv.text(140, 240, "100,000,000+", 54, INK, qa, "Black", "lm")
        cv.text(142, 296, "atmospheric particles / day", 24, INK2, qa, "SemiBold", "lm")
        # neutrino through the Earth, coming up from below
        qn = eo(pr(t, tl, tl + 3.0))
        if qn > 0:
            x0, y0 = px - 700, 1080
            stream(cv, x0, y0, lerp(x0, px, qn), lerp(y0, py + 30, qn), t, 1, TERRA, 5, 220)
            cv.text(x0 + 260, 960, "ν", 60, TERRA, qn, "Bold")
        qk = eo(pr(t, tn, tn + .8))
        if qk > 0:
            panel(cv, 1260, 180, 1810, 330, qk)
            cv.text(1290, 240, "from below", 48, TERRA, qk, "Black", "lm")
            cv.text(1292, 296, "= very likely a neutrino", 26, INK2, qk, "SemiBold", "lm")
            cv.arrow(px + 90, py + 40, px + 90, py - 70, TERRA, 5, qk, 22)
        cv.ga = 1

# ------------------------------------------------------------ 2013: first cosmic neutrinos
def scene_f2013(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    chapter_tag(cv, "12", "Something from far away", 1)
    te = b.kw(0, "far too much"); tb = b.kw(0, "They came"); tn = b.kw(0, "Neutrino astronomy")
    bignum(cv, 120, 250, "2013", 150, TERRA, eo(pr(t, 0, 1)), "lm")
    x0, x1, yb = 300, 1700, 900
    cv.line([(x0, yb), (x1, yb)], INK, 3, 1); cv.line([(x0, yb), (x0, 380)], INK, 3, 1)
    cv.text(x1, yb + 40, "energy  →", 26, INK2, 1, "SemiBold", "rm")
    cv.text(x0 - 20, 400, "how many", 24, INK2, 1, "SemiBold", "rm")
    q = eo(pr(t, .3, 3))
    for k in range(28):
        x = x0 + 20 + k * 40
        h = 480 * math.exp(-k * .28) * q
        if h > 2: cv.rect(x, yb - h, x + 32, yb, fill=ICE3, a=1, outline=INK2, w=1)
    cv.text(470, 360, "made in our atmosphere", 24, INK2, q, "SemiBold", "lm")
    qe = eo(pr(t, te, te + .8))
    rng = np.random.default_rng(13)
    for k in range(9):
        x = 1300 + rng.uniform(0, 340); y = yb - 30 - rng.uniform(0, 30)
        tk = te + k * .15
        a_ = eo(pr(t, tk, tk + .5))
        cv.circ(x, y, 13 * eback(pr(t, tk, tk + .5)), fill=TERRA, a=a_, outline=INK, w=2)
    if qe > 0:
        panel(cv, 1180, 600, 1760, 740, qe)
        cv.text(1210, 650, "too energetic", 40, TERRA, qe, "Black", "lm")
        cv.text(1212, 702, "to come from here", 26, INK2, qe, "SemiBold", "lm")
    qb = eo(pr(t, tn, tn + .8))
    chip(cv, 1470, 230, "neutrino astronomy begins", qb, TERRA, size=30, w="Bold")

# ------------------------------------------------------------ TXS 0506+056
K = 46
def sky(ra_h, dec, cx=960, cy=560):
    return (cx + (5.55 - ra_h) * 15 * K, cy - dec * K)
ORION = {"Betelgeuse": (5.919, 7.41, 6), "Bellatrix": (5.419, 6.35, 4.5), "Mintaka": (5.533, -.30, 4), "Alnilam": (5.603, -1.20, 4.5),
         "Alnitak": (5.679, -1.94, 4.5), "Saiph": (5.796, -9.67, 4), "Rigel": (5.242, -8.20, 6), "Meissa": (5.585, 9.93, 3)}
OLINES = [("Betelgeuse", "Meissa"), ("Meissa", "Bellatrix"), ("Betelgeuse", "Bellatrix"), ("Betelgeuse", "Alnitak"), ("Bellatrix", "Mintaka"),
          ("Alnitak", "Alnilam"), ("Alnilam", "Mintaka"), ("Alnitak", "Saiph"), ("Mintaka", "Rigel")]
TXS = (5.157, 5.69)

def blazar(cv, x, y, s, t, a=1):
    for k in range(6):
        cv.circ(x, y, s * (1 - k * .14), fill=mix((236, 214, 170), OCHRE, k / 6), a=a * .55)
    cv.circ(x, y, s * .22, fill=(30, 26, 24), a=a)
    # jet pointing almost at us: foreshortened cone
    for k in range(4):
        r = s * (.18 + k * .1)
        cv.circ(x + s * .05 * k, y - s * .04 * k, r, outline=TERRA, w=3, a=a * (1 - k * .2))
    cv.circ(x, y, s * .1, fill=SNOW, a=a)

def scene_txs(cv, t, S, T):
    b = Beat(S)
    tev = b.kw(0, "On the"); tal = b.kw(0, "IceCube sent"); tdi = b.kw(0, "In that direction"); tbl = b.kw(0, "the blazar"); tfar = b.kw(0, "about four billion")
    tx, ty = sky(*TXS)
    z = lerp(1.0, 2.4, eio(pr(t, tdi, tdi + 2.5)))
    cv.cam = Cam(lerp(960, tx, eio(pr(t, tdi, tdi + 2.5))), lerp(540, ty, eio(pr(t, tdi, tdi + 2.5))), z)
    # graticule
    for h in np.arange(4.5, 6.8, .25):
        x0, y0 = sky(h, -16); x1, y1 = sky(h, 16)
        cv.line([(x0, y0), (x1, y1)], RULE, 1.5, .8)
    for d in range(-15, 17, 5):
        x0, y0 = sky(6.7, d); x1, y1 = sky(4.4, d)
        cv.line([(x0, y0), (x1, y1)], RULE, 1.5, .8)
    q = eo(pr(t, 0, 1.5))
    for a_, b_ in OLINES:
        p0 = sky(*ORION[a_][:2]); p1 = sky(*ORION[b_][:2])
        cv.line([p0, p1], INK2, 2, q * .6)
    rng = np.random.default_rng(17)
    for k in range(120):
        x, y = rng.uniform(0, 1920), rng.uniform(0, 1080)
        cv.circ(x, y, rng.uniform(1, 2.6), fill=INK2, a=.35)
    for nm, (ra, de, m) in ORION.items():
        x, y = sky(ra, de)
        cv.circ(x, y, m + 2, fill=INK, a=q)
    bx, by = sky(*ORION["Betelgeuse"][:2]); cv.text(bx - 14, by - 26, "Betelgeuse", 18, INK2, q * (1 - pr(t, tdi, tdi + 1)), "SemiBold", "rm")
    rx, ry = sky(*ORION["Rigel"][:2]); cv.text(rx + 14, ry + 26, "Rigel", 18, INK2, q * (1 - pr(t, tdi, tdi + 1)), "SemiBold", "lm")
    ox, oy = sky(5.6, -4.5); cv.text(ox, oy + 90, "ORION", 30, MUT, q * (1 - pr(t, tdi, tdi + 1)), "Bold")
    # error circle
    qe = eo(pr(t, tal, tal + 1.0))
    if qe > 0:
        dashed(cv, [(tx + 46 * math.cos(u), ty + 46 * math.sin(u)) for u in np.linspace(0, 6.3, 60)], TERRA, 2.5, qe, 8, 6)
        cv.circ(tx, ty, 46 + 20 * (1 - qe), outline=TERRA, w=1.5, a=qe * .5)
    qb = eo(pr(t, tbl - .3, tbl + .9))
    if qb > 0:
        blazar(cv, tx, ty, 26 * qb, t, qb)
    # screen-space overlays
    cam = cv.cam; cv.cam = Cam()
    chapter_tag(cv, "13", "A neutrino with an address", 1)
    qv = eo(pr(t, tev - .2, tev + .6))
    panel(cv, 1280, 150, 1810, 330, qv)
    cv.text(1310, 210, "22 Sep 2017", 48, INK, qv, "Black", "lm")
    cv.text(1312, 276, "one neutrino  ·  ≈ 290 TeV", 28, TERRA, qv, "Bold", "lm")
    # alert to telescopes (left bottom)
    qa = win(t, tal - .2, tdi + 1.2, .6, .8)
    if qa > 0:
        ix, iy = 260, 860
        cv.rect(ix - 40, iy - 30, ix + 40, iy + 30, fill=ICE, a=qa, outline=INK, w=2.5)
        cv.text(ix, iy + 64, "IceCube alert", 22, INK, qa, "Bold")
        for k in range(4):
            ph = ((t - tal) * .8 + k / 4) % 1
            cv.circ(ix, iy, 50 + ph * 420, outline=TERRA, w=3, a=qa * (1 - ph) * .7)
        for k, (xx, yy, kind) in enumerate([(700, 940, "dish"), (980, 990, "dome"), (1240, 920, "sat"), (1520, 980, "dome")]):
            qq = qa * eo(pr(t, tal + .6 + k * .3, tal + 1.2 + k * .3))
            if kind == "dish":
                cv.poly([(xx - 40, yy - 10), (xx + 40, yy - 40), (xx + 30, yy), (xx - 20, yy + 20)], SNOW, qq, INK, 2.5)
                cv.line([(xx, yy + 5), (xx, yy + 50)], INK, 4, qq)
            elif kind == "dome":
                cv.poly([(xx - 40, yy + 40)] + [(xx + 40 * math.cos(u), yy + 40 - 40 * math.sin(u)) for u in np.linspace(math.pi, 0, 16)] + [(xx + 40, yy + 40)], SNOW, qq, INK, 2.5)
                cv.rect(xx - 6, yy - 2, xx + 6, yy + 30, fill=INK, a=qq)
            else:
                cv.rect(xx - 18, yy - 18, xx + 18, yy + 18, fill=OCHRE2, a=qq, outline=INK, w=2.5)
                cv.rect(xx - 70, yy - 8, xx - 24, yy + 8, fill=ICE3, a=qq, outline=INK, w=2)
                cv.rect(xx + 24, yy - 8, xx + 70, yy + 8, fill=ICE3, a=qq, outline=INK, w=2)
    qn = eo(pr(t, tbl, tbl + .8))
    if qn > 0:
        panel(cv, 1240, 720, 1820, 940, qn)
        cv.text(1270, 780, "TXS 0506+056", 48, INK, qn, "Black", "lm")
        cv.text(1272, 840, "blazar  ·  giant black hole", 26, INK2, qn, "SemiBold", "lm")
        cv.text(1272, 890, "≈ 4 billion light years", 26, TERRA, eo(pr(t, tfar, tfar + .6)), "Bold", "lm")
    cv.cam = cam

# ------------------------------------------------------------ NGC 1068
def galaxy(cv, x, y, R, t, a=1, rot=0.0):
    rng = np.random.default_rng(23)
    for arm in range(2):
        for k in range(260):
            u = k / 260
            th = arm * math.pi + u * 3.6 * math.pi * .55 + rot
            r = R * (.12 + .88 * u)
            jx, jy = rng.normal(0, R * .045), rng.normal(0, R * .045)
            px, py = x + r * math.cos(th) + jx, y + r * math.sin(th) * .62 + jy
            cv.circ(px, py, rng.uniform(2.5, 6.5) * (1.2 - u * .6), fill=mix(OCHRE, TERRA, rng.random()) if rng.random() < .7 else PLUM, a=a * (.9 - .45 * u))
    for k in range(5):
        cv.circ(x, y, R * (.15 - k * .022), fill=mix(OCHRE2, (240, 220, 180), k / 5), a=a * .6)

def scene_ngc(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0 + .015 * t)
    chapter_tag(cv, "14", "Hidden behind dust", 1)
    t79 = b.kw(0, "seventy-nine"); tdu = b.kw(0, "thick dust"); tli = b.kw(0, "Light struggles"); tne = b.kw(0, "Neutrinos do not"); tev = b.kw(0, "Scientists")
    gx, gy = 760, 560
    galaxy(cv, gx, gy, 420, t, eo(pr(t, 0, 1.5)), rot=t * .01)
    qd = eo(pr(t, tdu - .4, tdu + .8))
    if qd > 0:
        for k in range(6):
            cv.circ(gx, gy, 90 - k * 9, fill=mix((96, 70, 52), (60, 44, 34), k / 6), a=qd * .55)
        cv.circ(gx, gy, 16, fill=INK, a=qd)
    ql = eo(pr(t, tli - .2, tli + .6))
    if ql > 0:
        for k in range(8):
            a_ = k * .785 + .3
            ph = ((t - tli) * .8 + k * .13) % 1
            L = 20 + 60 * ph
            cv.line([(gx + 18 * math.cos(a_), gy + 18 * math.sin(a_)), (gx + L * math.cos(a_), gy + L * math.sin(a_))], (250, 238, 210), 3, ql * (1 - ph))
            cv.line([(gx + 82 * math.cos(a_ - .1), gy + 82 * math.sin(a_ - .1)), (gx + 82 * math.cos(a_ + .1), gy + 82 * math.sin(a_ + .1))], INK, 3, ql * .5)
    qn = eo(pr(t, tne - .3, tne + .6))
    if qn > 0:
        for k in range(10):
            a_ = k * .628 + .1
            stream(cv, gx, gy, gx + 900 * math.cos(a_), gy + 900 * math.sin(a_), t + k * .2, qn * .9, TERRA, 2.5, 200)
    cam = cv.cam; cv.cam = Cam()
    q7 = eo(pr(t, t79 - .2, t79 + .6))
    panel(cv, 1300, 170, 1820, 420, q7)
    cv.text(1330, 260, f"{79 * eo(pr(t, t79, t79 + 1.2)):.0f}", 110, INK, q7, "Black", "lm")
    cv.text(1334, 350, "neutrinos  ·  NGC 1068", 28, INK2, q7, "SemiBold", "lm")
    cv.text(1334, 392, "≈ 47 million light years", 24, TERRA, q7, "Bold", "lm")
    qe = eo(pr(t, tev, tev + .7))
    panel(cv, 1300, 760, 1820, 900, qe)
    cv.text(1330, 812, "strong evidence", 40, INK, qe, "Black", "lm")
    cv.text(1332, 864, "not yet final proof  ·  4.2σ", 24, INK2, qe, "SemiBold", "lm")
    cv.text(1332, 140, "2022", 40, TERRA, eo(pr(t, 0, 1)), "Black", "lm")
    cv.cam = cam

# ------------------------------------------------------------ MILKY WAY in neutrinos
def scene_milky(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 560, 1.0)
    chapter_tag(cv, "15", "Our galaxy, in neutrinos", 1)
    tm = b.kw(0, "machine learning"); tp = b.kw(0, "first picture"); tn = b.kw(0, "but in neutrinos")
    cx, cy, A, B = 960, 580, 760, 380
    cv.circ(cx + 10, cy + 14, 1, fill=INK, a=0)
    pts = [(cx + A * math.cos(u), cy + B * math.sin(u)) for u in np.linspace(0, 6.3, 120)]
    cv.poly([(x + 10, y + 14) for x, y in pts], (60, 45, 30), .1)
    cv.poly(pts, SNOW, 1, INK, 3)
    for k in range(1, 6):
        yy = cy - B + k * 2 * B / 6
        w_ = A * math.sqrt(max(0, 1 - ((yy - cy) / B) ** 2))
        cv.line([(cx - w_, yy), (cx + w_, yy)], RULE, 1.5, .9)
    for k in range(-3, 4):
        pts2 = [(cx + A * (k / 3.5) * math.cos(u), cy + B * math.sin(u)) for u in np.linspace(-1.57, 1.57, 40)]
        cv.line(pts2, RULE, 1.5, .9)
    q = eo(pr(t, tp - 1.0, tp + 2.0))
    rng = np.random.default_rng(41)
    for k in range(60):
        f = 1 - k / 60
        w_ = A * .95 * f; h_ = 16 + 55 * (1 - f)
        cv.poly([(cx + w_ * math.cos(u), cy + h_ * math.sin(u)) for u in np.linspace(0, 6.3, 50)], TERRA, q * .03)
    for k in range(500):
        x = rng.normal(0, A * .45); y = rng.normal(0, 30 + abs(x) * .02)
        if (x / A) ** 2 + (y / B) ** 2 < .9:
            cv.circ(cx + x, cy + y, rng.uniform(1.5, 3.5), fill=TERRA, a=q * rng.uniform(.3, .8) * eo(pr(t, tp - 1 + k / 500 * 3, tp + k / 500 * 3)))
    qm = eo(pr(t, tm - .3, tm + .6))
    chip(cv, 520, 1020, "10 years of data  ·  machine learning", qm, size=24)
    qn = eo(pr(t, tn - .3, tn + .6))
    chip(cv, 1400, 1020, "2023  ·  the Milky Way in neutrinos", qn, TERRA, size=24, w="Bold")
    cv.text(cx, cy - B - 40, "whole sky", 22, INK2, eo(pr(t, 0, 1)), "SemiBold")
