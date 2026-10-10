from common import *
from scenes_a import nucleus

SEC = dict(x0=620, x1=1300, y0=170, y1=1000, dmax=2800)
def dy(d, S_=SEC): return S_["y0"] + d / S_["dmax"] * (S_["y1"] - S_["y0"])

def depth_scale(cv, a=1, S_=SEC, marks=(0, 500, 1000, 1500, 2000, 2500)):
    x = S_["x0"] - 30
    cv.line([(x, S_["y0"]), (x, S_["y1"])], INK, 2, a)
    for d in marks:
        y = dy(d, S_)
        cv.line([(x - 12, y), (x, y)], INK, 2, a)
        cv.text(x - 22, y, f"{d:,} m", 22, INK2, a, "SemiBold", "rm")

def bubbles(cv, t, a=1, S_=SEC, dlim=1400, n=320, seed=3):
    rng = np.random.default_rng(seed)
    for k in range(n):
        x = rng.uniform(S_["x0"] + 10, S_["x1"] - 10); d = rng.uniform(60, dlim) ** 1.0
        r = rng.uniform(2, 6) * (1.2 - d / dlim * .7)
        cv.circ(x, dy(d, S_), r * 1.3, fill=SNOW, a=a * .9, outline=ICE4, w=1.5)

def icon_tile(cv, x, y, kind, word, a=1, t=0):
    if a <= .01: return
    cv.rrect(x - 90 + 6, y - 90 + 8, x + 90 + 6, y + 90 + 8, 18, fill=(60, 45, 30), a=a * .1)
    cv.rrect(x - 90, y - 90, x + 90, y + 90, 18, fill=SNOW, a=a, outline=RULE, w=2)
    if kind == "dark":
        cv.rrect(x - 60, y - 60, x + 60, y + 40, 10, fill=(44, 42, 50), a=a)
        cv.circ(x + 10, y - 12, 26, fill=OCHRE2, a=a); cv.circ(x + 24, y - 22, 24, fill=(44, 42, 50), a=a)
    elif kind == "life":
        cv.poly([(x - 50, y - 10), (x + 10, y - 40), (x + 40, y - 10), (x + 10, y + 20)], ICE3, a, INK, 2.5)
        cv.poly([(x - 50, y - 10), (x - 74, y - 34), (x - 74, y + 14)], ICE3, a, INK, 2.5)
        cv.line([(x - 60, y + 30), (x + 60, y - 50)], TERRA, 6, a)
    elif kind == "rad":
        for k in range(3):
            a0 = k * 2.094 - 1.57
            pts = [(x, y - 10)] + [(x + 52 * math.cos(a0 + u), y - 10 + 52 * math.sin(a0 + u)) for u in np.linspace(-.5, .5, 8)]
            cv.poly(pts, OCHRE, a * .45, INK, 2)
        cv.circ(x, y - 10, 12, fill=INK, a=a)
    elif kind == "quake":
        pts = [(x - 66 + i * 4, y - 10 + (math.sin(i * 1.3) * 2)) for i in range(34)]
        cv.line(pts, INK, 3, a)
    cv.text(x, y + 62, word, 20, INK2, a, "SemiBold")

# ------------------------------------------------------------ ICE
def scene_ice(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    t2 = b(1)
    A1 = win(t, 0, t2 + .3, .5, .7); A2 = win(t, t2, S["dur"] + 1, .7, .5)
    if A1 > 0:
        cv.ga = A1
        chapter_tag(cv, "05", "An idea made of ice", 1)
        th = b.kw(0, "Francis"); tt = b.kw(0, "Why build"); ta = b.kw(0, "Antarctica"); td = b.kw(0, "Deep ice")
        q = eo(pr(t, th - .3, th + .9))
        paste_card(cv, photo("halzen.jpg"), 470, 520, 470, 520, q, crop=(150, 0, 1280, 1250), rot=-2.0)
        chip(cv, 470, 840, "Francis Halzen  ·  UW–Madison", q, size=24)
        # water tank -> Antarctica
        qt = win(t, tt - .2, ta + .6, .6, .6)
        if qt > 0:
            x, y = 1330, 450
            cv.rrect(x - 230, y - 170, x + 230, y + 170, 16, fill=SNOW, a=qt, outline=INK, w=3)
            cv.rect(x - 228, y - 80 + 8 * math.sin(t * 2), x + 228, y + 168, fill=CHER3, a=qt)
            for k in range(4): cv.line([(x - 200 + k * 40, y - 70 + 8 * math.sin(t * 2 + k)), (x - 170 + k * 40, y - 72 + 8 * math.sin(t * 2 + k))], CHER, 2, qt * .6)
            cv.rrect(x - 230, y - 170, x + 230, y + 170, 16, outline=INK, w=3, a=qt)
        qa = eo(pr(t, ta, ta + 1.0))
        if qa > 0:
            paste_card(cv, photo("icl_2023.jpg"), 1330, 430, 620, 410, qa, crop=(0, 120, 1920, 1300), rot=1.5)
            chip(cv, 1330, 680, "South Pole  ·  IceCube Lab", qa, size=22)
        qd = eo(pr(t, td, td + .8))
        for k, (kind, word) in enumerate([("dark", "dark"), ("life", "no life"), ("rad", "low radioactivity"), ("quake", "no earthquakes")]):
            tk = td + .6 + k * .9
            icon_tile(cv, 1030 + k * 205, 870, kind, word, eo(pr(t, tk, tk + .6)) * qd, t)
        cv.ga = 1
    if A2 > 0:
        cv.ga = A2
        chapter_tag(cv, "06", "Clear, deep ice", 1)
        ta = b.kw(1, "AMANDA"); tb = b.kw(1, "bubbles"); tc = b.kw(1, "But below"); tf = b.kw(1, "A flash")
        ice_section(cv, SEC["x0"], SEC["y0"], SEC["x1"], SEC["y1"], 1)
        depth_scale(cv, 1)
        bubbles(cv, t, eo(pr(t, tb - .4, tb + .6)))
        # AMANDA string
        qa = eo(pr(t, ta, ta + 1))
        xs = 1180
        cv.line([(xs, SEC["y0"]), (xs, dy(2000) * qa + SEC["y0"] * (1 - qa))], INK, 2, qa)
        for k in range(10):
            d = 1500 + k * 55
            if dy(d) < dy(2000) * qa + SEC["y0"] * (1 - qa): dom(cv, xs, dy(d), 7, qa)
        chip(cv, xs, 130, "AMANDA  ·  1990s", qa, size=22)
        # scattered light in bubbly ice
        qs = eo(pr(t, tb, tb + 1))
        if qs > 0:
            rng = np.random.default_rng(5)
            x, y = 820, dy(700); pts = [(x, y)]
            for k in range(26):
                ang = rng.uniform(0, 6.28); L = rng.uniform(14, 30)
                x += L * math.cos(ang); y += L * math.sin(ang); pts.append((x, y))
            n = int(len(pts) * pr(t, tb, tb + 3))
            if n > 1: cv.line(pts[:n], CHER, 3, qs * .9)
            cv.circ(820, dy(700), 9, fill=CHER, a=qs)
        # clear line
        qc = eo(pr(t, tc, tc + .8))
        if qc > 0:
            dashed(cv, [(SEC["x0"], dy(1400)), (SEC["x0"] + (SEC["x1"] - SEC["x0"]) * qc, dy(1400))], INK, 2.5, qc, 12, 8)
            cv.text(SEC["x1"] + 26, dy(1400), "1,400 m", 30, INK, qc, "Bold", "lm")
            cv.text(SEC["x1"] + 26, dy(1400) - 40, "bubbles above", 22, INK2, qc, "SemiBold", "lm")
            cv.text(SEC["x1"] + 26, dy(1400) + 40, "crystal clear below", 22, INK2, qc, "SemiBold", "lm")
        qf = eo(pr(t, tf, tf + 2.2))
        if qf > 0:
            y = dy(2150); x0 = 700; x1 = lerp(x0, 1290, qf)
            for k in range(14):
                u = k / 13
                cv.line([(lerp(x0, x1, u), y), (lerp(x0, x1, min(1, u + 1 / 13)), y)], CHER, 5, (1 - u * .8) * qf)
            cv.circ(x0, y, 10, fill=CHER, a=qf)
            cv.text((700 + 1290) / 2, y + 46, "hundreds of metres", 24, INK2, qf, "SemiBold")
        cv.ga = 1

# ------------------------------------------------------------ DRILL
SEC2 = dict(x0=560, x1=1360, y0=230, y1=1000, dmax=2600)
def dy2(d): return dy(d, SEC2)
def hex_points(n=86, sp=1.0):
    pts = []
    for i in range(-7, 8):
        for j in range(-7, 8):
            x = (i + j * .5) * sp; y = j * .866 * sp
            pts.append((x, y))
    pts.sort(key=lambda p: max(abs(p[1]) / .866, abs(p[0] + p[1] / 1.732 * .0) ) + .001 * math.hypot(*p))
    pts.sort(key=lambda p: math.hypot(p[0], p[1]))
    return pts[:n]
HEX = hex_points()

def rig(cv, x, y, a=1):
    cv.line([(x - 90, y), (x - 10, y - 170), (x + 70, y)], INK, 5, a)
    cv.line([(x - 60, y - 60), (x + 40, y - 60)], INK, 3, a)
    cv.circ(x - 10, y - 170, 10, fill=INK, a=a)
    # hose reel
    rx, ry = x - 300, y - 70
    cv.circ(rx + 6, ry + 8, 70, fill=(60, 45, 30), a=a * .12)
    cv.circ(rx, ry, 70, fill=TERRA2, a=a, outline=INK, w=3)
    for k in range(4): cv.circ(rx, ry, 58 - k * 11, outline=TERRA, w=3, a=a * .8)
    cv.circ(rx, ry, 12, fill=INK, a=a)
    cv.line([(rx + 40, ry - 50), (x - 10, y - 170), (x, y - 160)], TERRA, 6, a)
    cv.rect(rx - 60, y - 10, rx + 60, y, fill=INK2, a=a)

def scene_drill(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    t2 = b(1)
    chapter_tag(cv, "07", "Melting a way down", 1)
    tm = b.kw(0, "You melt"); tsh = b.kw(0, "shower"); th = b.kw(0, "melted holes"); te = b.kw(0, "Each hole")
    tr = b.kw(1, "Crews"); tw = b.kw(1, "Within weeks"); ts = b.kw(1, "Over seven")
    A1 = 1 - eio(pr(t, ts - .2, ts + .8)); A2 = eo(pr(t, ts, ts + 1.0))
    if A1 > 0:
        cv.ga = A1
        ice_section(cv, SEC2["x0"], SEC2["y0"], SEC2["x1"], SEC2["y1"], 1)
        rng = np.random.default_rng(12)
        for k in range(22):
            yy = SEC2["y0"] + 12 + k * 35 + rng.uniform(-6, 6)
            pts = [(x, yy + 4 * math.sin(x / 90 + k)) for x in range(SEC2["x0"] + 4, SEC2["x1"] - 4, 24)]
            cv.line(pts, SNOW if k % 3 else ICE4, 1.5, .35)
        depth_scale(cv, 1, SEC2, (0, 500, 1000, 1500, 2000, 2450))
        hx = 1000
        rig(cv, hx, SEC2["y0"], eo(pr(t, 0, 1)))
        D = 2450 * esm(pr(t, th, b(0) + b.PD[0] + 1.2))
        yb = dy2(D)
        if D > 1:
            frozen = eo(pr(t, tw, tw + 2.5))
            cv.rect(hx - 14, SEC2["y0"], hx + 14, yb, fill=mix(CHER3, ICE2, frozen * .8), a=1)
            cv.line([(hx - 14, SEC2["y0"]), (hx - 14, yb)], INK2, 1.5, .6 * (1 - frozen))
            cv.line([(hx + 14, SEC2["y0"]), (hx + 14, yb)], INK2, 1.5, .6 * (1 - frozen))
            cv.line([(hx, SEC2["y0"] - 160), (hx, yb - 10)], TERRA, 3, 1 - pr(t, tr - .5, tr))
            if t < tr:
                cv.poly([(hx - 12, yb - 22), (hx + 12, yb - 22), (hx + 6, yb), (hx - 6, yb)], INK, 1)
                for k in range(3):
                    ph = (t * 2 + k / 3) % 1
                    cv.line([(hx - 20 + k * 20, yb + 4 + ph * 30), (hx - 16 + k * 20, yb + 14 + ph * 30)], TERRA, 2.5, (1 - ph))
            # cable of sensors lowering
            ql = pr(t, tr, tr + 5)
            if ql > 0:
                bot = lerp(SEC2["y0"] - 40, dy2(2450), esm(ql))
                cv.line([(hx, SEC2["y0"] - 160), (hx, bot)], INK, 2.5, 1)
                for k in range(12):
                    yy = bot - k * 34
                    if yy > SEC2["y0"] + 5: dom(cv, hx, yy, 9, 1)
        panel(cv, 1420, 300, 1830, 540, eo(pr(t, th, th + .6)))
        cv.text(1450, 360, f"{D:,.0f} m", 64, INK, eo(pr(t, th, th + .6)), "Black", "lm")
        cv.text(1452, 420, "deep", 26, INK2, eo(pr(t, th, th + .6)), "SemiBold", "lm")
        cv.text(1452, 490, "hole  ≈ 60 cm wide", 26, INK2, eo(pr(t, th + 1.5, th + 2.2)), "SemiBold", "lm")
        qe = eo(pr(t, te, te + .6)) * (1 - eio(pr(t, tr - .3, tr + .3)))
        qr = eo(pr(t, tr, tr + .6))
        for qq, big, small in [(qe, "≈ 2 days", "per hole"), (qr * (1 - eo(pr(t, tw, tw + .5))), "≈ 11 h", "to lower a cable"), (eo(pr(t, tw, tw + .5)), "refrozen", "in a couple of weeks")]:
            if qq > 0:
                panel(cv, 1420, 590, 1830, 760, qq)
                cv.text(1450, 650, big, 56, TERRA, qq, "Black", "lm")
                cv.text(1452, 712, small, 26, INK2, qq, "SemiBold", "lm")
        qsh = win(t, tsh - .2, th + 2.5, .5, .6)
        if qsh > 0:
            panel(cv, 110, 560, 470, 900, qsh)
            x, y = 290, 650
            cv.rrect(x - 70, y - 30, x + 70, y, 14, fill=INK2, a=qsh)
            cv.line([(x, y - 30), (x, y - 70), (x + 80, y - 70)], INK2, 8, qsh)
            for k in range(7):
                ph = (t * 1.5 + k * .13) % 1
                xx = x - 54 + k * 18
                cv.line([(xx, y + 10 + ph * 160), (xx + (k - 3) * 3, y + 30 + ph * 160)], CHER, 3, (1 - ph) * qsh)
            cv.text(290, 860, "hot water", 26, INK2, qsh, "SemiBold")
        cv.ga = 1
    if A2 > 0:
        cv.ga = A2
        cx, cy, sc = 960, 560, 40
        n = int(86 * eo(pr(t, ts + .4, ts + 4.0)))
        cv.circ(cx, cy, 430, fill=SNOW, a=1, outline=RULE, w=2)
        for k, (x, y) in enumerate(HEX):
            if k < n:
                cv.circ(cx + x * sc, cy + y * sc, 9, fill=INK, a=1)
            else:
                cv.circ(cx + x * sc, cy + y * sc, 9, outline=RULE, w=1.5, a=.8)
        panel(cv, 1450, 380, 1830, 700, 1)
        cv.text(1480, 470, f"{n}", 110, INK, 1, "Black", "lm")
        cv.text(1484, 560, "holes", 28, INK2, 1, "SemiBold", "lm")
        cv.text(1484, 640, "7 summers  ·  2004–2010", 24, TERRA, eo(pr(t, ts + 1, ts + 2)), "Bold", "lm")
        cv.text(cx, 1040, "top view  ·  125 m between strings", 22, INK2, 1, "SemiBold")
        cv.ga = 1

# ------------------------------------------------------------ ARRAY (3D)
def scene_array(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    chapter_tag(cv, "08", "A telescope of ice", 1)
    tn = b.kw(0, "five thousand"); tl = b.kw(0, "light bulb")
    rot = .35 + t * .025
    ca, sa = math.cos(rot), math.sin(rot)
    sc = 33; zs = .5
    ox, oy = 760, 330
    def P(x, y, z):
        xr, yr = x * ca - y * sa, x * sa + y * ca
        return iso(xr * sc, yr * sc, z * zs, ox, oy, 1.0)
    # ice block outline (cube around strings), z: 0 (surface) to -1000*?; use depth in metres scaled
    def D(d): return -(d - 1450) * .55 - 40
    grow = eo(pr(t, .2, 6.0))
    # surface plane
    R = 6.4
    sq = [P(-R, -R, 140), P(R, -R, 140), P(R, R, 140), P(-R, R, 140)]
    cv.poly(sq, SNOW, .9, RULE, 2)
    # cube block
    top = [P(-R, -R, D(1450)), P(R, -R, D(1450)), P(R, R, D(1450)), P(-R, R, D(1450))]
    bot = [P(-R, -R, D(2450)), P(R, -R, D(2450)), P(R, R, D(2450)), P(-R, R, D(2450))]
    for k in range(4):
        cv.poly([top[k], top[(k + 1) % 4], bot[(k + 1) % 4], bot[k]], ICE2, .18)
    cv.poly(top, ICE, .35, ICE3, 2)
    order = sorted(range(len(HEX)), key=lambda k: (HEX[k][0] * sa + HEX[k][1] * ca))
    for k in order:
        x, y = HEX[k]
        if k / 86 > grow: continue
        p0 = P(x, y, 140); p1 = P(x, y, D(2450))
        cv.line([p0, p1], INK2, 1.2, .55)
        for j in range(0, 60, 3):
            d = 1450 + j * 17
            px, py = P(x, y, D(d))
            cv.circ(px, py, 2.6, fill=INK, a=.85)
    for k in range(4):
        cv.line([top[k], bot[k]], ICE4, 1.5, .6)
    cv.line(bot + [bot[0]], ICE4, 1.5, .6)
    cv.line(top + [top[0]], ICE4, 1.5, .6)
    qn = eo(pr(t, tn - .3, tn + .5))
    panel(cv, 1390, 170, 1830, 440, qn)
    cv.text(1420, 260, f"{5160 * eo(pr(t, tn, tn + 1.6)):,.0f}", 96, INK, qn, "Black", "lm")
    cv.text(1424, 340, "sensors  ·  86 strings", 26, INK2, qn, "SemiBold", "lm")
    cv.text(1424, 392, "1 km³  ·  1,450–2,450 m deep", 26, TERRA, qn, "Bold", "lm")
    ql = eo(pr(t, tl - .4, tl + .6))
    if ql > 0:
        paste_card(cv, photo("dom.jpg"), 1540, 720, 300, 300, ql, rot=2)
        # reversed bulb diagram
        y = 960
        cv.text(1250, y, "light", 26, CHER, ql, "Bold")
        cv.arrow(1310, y, 1420, y, INK, 3, ql, 14)
        cv.text(1540, y, "sensor", 26, INK, ql, "Bold")
        cv.arrow(1640, y, 1740, y, INK, 3, ql, 14)
        pts = [(1760 + i * 3, y + 14 * math.sin(i * .6 + t * 4)) for i in range(25)]
        cv.line(pts, TERRA, 3, ql)
        cv.text(1540, 540, "a light bulb in reverse", 26, INK2, ql, "SemiBold")

# ------------------------------------------------------------ LIGHT (interaction + Cherenkov)
def deep_bg(cv, a=1):
    cv.done()
    g = vgrad(W, H, [(0, (198, 214, 216)), (1, (150, 174, 182))])
    cv.im.paste(g, (0, 0), Image.new("L", (W, H), int(255 * a)))
    rng = np.random.default_rng(8)
    for k in range(40):
        x = rng.uniform(0, W); cv.line([(x, 0), (x + rng.uniform(-30, 30), H)], SNOW, rng.uniform(1, 4), a * .08)

def boat_inset(cv, x, y, w, h, t, a=1, half=40):
    panel(cv, x - w / 2, y - h / 2, x + w / 2, y + h / 2, a, fill=(176, 198, 200))
    bx = x + w * .25
    for k in range(5):
        L = 70 + k * 55; ph = (t * 1.2 + k * .2) % 1
        ang = math.radians(half)
        cv.line([(bx - L * math.cos(ang), y - L * math.sin(ang)), (bx, y), (bx - L * math.cos(ang), y + L * math.sin(ang))], SNOW, 3, a * (1 - k / 5))
    cv.poly([(bx + 40, y), (bx - 30, y - 18), (bx - 46, y - 14), (bx - 46, y + 14), (bx - 30, y + 18)], TERRA, a, INK, 2.5)
    cv.rect(bx - 20, y - 8, bx + 4, y + 8, fill=SNOW, a=a)

def cone(cv, mx, my, length, a=1, half=41):
    """Cherenkov light: soft restrained blue cone trailing the muon tip at (mx,my), moving right"""
    ang = math.radians(half)
    for k, (f, al) in enumerate([(1.0, .10), (.82, .12), (.62, .16), (.42, .2)]):
        L = length * f
        cv.poly([(mx, my), (mx - L, my - L * math.tan(ang)), (mx - L, my + L * math.tan(ang))], CHER2, a * al)
    for s in (-1, 1):
        cv.line([(mx, my), (mx - length, my + s * length * math.tan(ang))], CHER, 3, a * .8)
        for k in range(1, 6):
            L = length * k / 6
            px, py = mx - L, my + s * L * math.tan(ang)
            nx_, ny_ = math.sin(ang), s * math.cos(ang)
            cv.arrow(px, py, px + nx_ * 40, py + ny_ * 40, CHER, 2, a * .7, 10)

def scene_light(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    deep_bg(cv, 1)
    chapter_tag(cv, "09", "A flash in the dark", 1)
    th = b.kw(0, "Very rarely"); tsm = b.kw(0, "smashes"); tmu = b.kw(0, "muon")
    tsl = b.kw(1, "light slows"); tco = b.kw(1, "So it leaves"); tbo = b.kw(1, "speedboat"); tch = b.kw(1, "This is Cherenkov")
    nx, ny = 700, 560
    # the detector around us: faint strings of sensors receding in depth
    for k, (xs, r, al) in enumerate([(240, 7, .35), (520, 5, .25), (1060, 6, .3), (1380, 8, .4), (1760, 5, .25)]):
        cv.line([(xs, 0), (xs, H)], INK2, 1.2, al)
        for j in range(-1, 12):
            yy = 40 + j * (95 if r > 6 else 70) + (k * 23) % 50
            dom(cv, xs, yy, r, al * 1.6)
    # many neutrinos pass, one hits
    for k in range(6):
        if k == 2: continue
        stream(cv, -50, 380 + k * 70, 1980, 300 + k * 80, t + k * .4, .55 * (1 - pr(t, tco, tco + 1)), TERRA, 2, 260)
    q_in = eo(pr(t, th, tsm))
    if t < tsm + .2:
        stream(cv, -50, ny - 120, lerp(-50, nx, q_in), lerp(ny - 120, ny, q_in), t, 1, TERRA, 3.5, 260)
    nucleus(cv, nx, ny, 34, 1 - .7 * pr(t, tsm, tsm + .4))
    fl = pr(t, tsm, tsm + 1.4)
    if 0 < fl < 1:
        for k in range(3):
            cv.circ(nx, ny, 20 + 160 * fl * (1 - k * .25), outline=OCHRE, w=4, a=(1 - fl) * .8)
        cv.circ(nx, ny, 40 * (1 - fl), fill=OCHRE2, a=(1 - fl))
    qi = win(t, tsm - .6, tco - .2, .5, .6)
    if qi > 0:
        ix, iy, ir = 1460, 330, 190
        cv.circ(ix + 8, iy + 12, ir, fill=(60, 45, 30), a=qi * .12)
        cv.circ(ix, iy, ir, fill=PAPER, a=qi * .96)
        cv.line([(nx + 30, ny - 30), (ix - ir * .7, iy + ir * .7)], INK2, 1.5, qi * .5)
        u = pr(t, tsm - .6, tsm)
        stream(cv, ix - 170, iy - 40, lerp(ix - 170, ix - 10, u), lerp(iy - 40, iy - 4, u), t, qi, TERRA, 4, 200)
        cv.text(ix - 150, iy - 80, "ν", 40, TERRA, qi, "Bold")
        nucleus(cv, ix, iy, 70 if t < tsm else 70 * (1 + .1 * math.sin(t * 30) * (1 - pr(t, tsm, tsm + .5))), qi)
        if t > tsm:
            v = eo(pr(t, tsm, tsm + 1.2))
            cv.line([(ix + 10, iy + 4), (ix + 10 + 150 * v, iy + 24 * v)], INK, 4, qi)
            cv.circ(ix + 10 + 150 * v, iy + 24 * v, 8, fill=INK, a=qi)
            cv.text(ix + 40, iy + 70, "μ", 40, INK, qi * v, "Bold")
            for k in range(3):
                a_ = -1.2 + k * 1.1
                cv.line([(ix, iy), (ix + 90 * v * math.cos(a_ + 2.2), iy + 90 * v * math.sin(a_ + 2.2))], OCHRE, 3, qi * (1 - v) * .9)
        cv.circ(ix, iy, ir, outline=INK, w=3, a=qi)
    qm = pr(t, tsm + .2, S["dur"] - 1)
    if qm > 0:
        mx = nx + (1700 - nx) * esm(qm) ** .9
        my = ny + (mx - nx) * .12
        cv.line([(nx, ny), (mx, my)], INK, 4, 1)
        cv.circ(mx, my, 10, fill=INK, a=1)
        qc = eo(pr(t, tco, tco + 1.2))
        if qc > 0:
            cone(cv, mx, my, min(mx - nx, 520) * qc, qc)
        ql = eo(pr(t, tmu, tmu + .6)) * (1 - eo(pr(t, tco, tco + .6)))
        cv.text(mx + 10, my - 50, "μ  muon", 34, INK, ql, "Bold", "lm")
    # speed comparison
    qs = win(t, tsl - .3, tbo + .2, .6, .6)
    if qs > 0:
        panel(cv, 110, 160, 860, 400, qs)
        for k, (lab, f, c) in enumerate([("light in empty space", 1.0, INK2), ("light in ice", .76, CHER), ("muon", .99, INK)]):
            y = 220 + k * 64; u = eo(pr(t, tsl + k * .5, tsl + k * .5 + 1.0))
            cv.rect(140, y, 140 + 420 * f * u, y + 26, fill=c, a=qs)
            cv.text(140 + 420 * f * u + 14, y + 13, lab, 22, INK, qs * u, "SemiBold", "lm")
    qb = eo(pr(t, tbo - .2, tbo + .6))
    if qb > 0:
        boat_inset(cv, 1480, 860, 620, 300, t, qb)
    qch = eo(pr(t, tch - .2, tch + .6))
    if qch > 0:
        panel(cv, 110, 160, 700, 300, qch)
        cv.text(140, 230, "Cherenkov light", 54, CHER, qch, "Black", "lm")
