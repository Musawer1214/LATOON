from common import *
from scenes_b import small_grid, out_icons, vbar, ball
from scenes_a import phone, FACE, PH_X, PH_Y, scene_sting

# ---------- training montage
def _cross(th):
    return int(np.argmax(OURP >= th))
I60, I80, I97 = _cross(.6), _cross(.8), _cross(.97)
NSTEP = len(OURP)
SM = np.convolve(np.pad(LOSSES, 4, mode="edge"), np.ones(9) / 9, mode="valid")

def scene_train(cv, t, S, T):
    b = Beat(S)
    knots = [(b(0, .1), 0), (b(0, .55), I60), (b(0, .64), I80), (b(0, .74), I97), (b(0, 1.0) + 1, NSTEP - 1)]
    if t <= knots[0][0]: st = 0
    elif t >= knots[-1][0]: st = NSTEP - 1
    else:
        for (ta, sa), (tb, sb) in zip(knots, knots[1:]):
            if ta <= t <= tb: st = int(lerp(sa, sb, (t - ta) / (tb - ta))); break
    si = st // 10
    old0 = Cam(1010 - (640 - 960) / .66, 540, .66)
    cv.cam = old0
    dust(cv, T, Cam())
    # pulse cycle accelerating
    per = lerp(2.6, .6, pr(t, b(0, .1), b(0, .5)))
    ph = 0; acc = 0.0; tt = b(0, .05)
    cyc = ((t - b(0, .05)) / per) % 1 if t > b(0, .05) else None
    fw = bw = None
    if cyc is not None and t < b(0, .9):
        if cyc < .5: fw = cyc * 2 * 3.4
        else: bw = (cyc - .5) * 2 * 3.4
    P = snap_np(si)
    G = grads(P, X_OURS)
    draw_net(cv, si, 1, x=X_OURS, kink=1, fwd=fw, bwd=bw, grads_=G)
    cv.math(INP_X - 48, SLOT_Y[0], "x_1", 26, MUT, 1); cv.math(INP_X - 58, SLOT_Y[-1], "x_{256}", 26, MUT, 1)
    cv.cam = Cam()
    # loss curve panel
    px0, py0, pw, ph_ = 1170, 150, 620, 330
    cv.rrect(px0 - 30, py0 - 60, px0 + pw + 30, py0 + ph_ + 40, 20, fill=(10, 13, 26), a=.85, outline=DIM, w=1.2)
    cv.text(px0, py0 - 30, "loss", 26, AM2, 1, "Medium", "lm")
    cv.line([(px0, py0 + ph_), (px0 + pw, py0 + ph_)], MUT, 1.5, .8); cv.line([(px0, py0), (px0, py0 + ph_)], MUT, 1.5, .8)
    if st > 1:
        xs = np.arange(0, st + 1, 3)
        pts = [(px0 + i / (NSTEP - 1) * pw, py0 + ph_ - cl(SM[i] / .8) * ph_) for i in xs]
        cv.line(pts, AM, 3, 1)
        cv.circ(pts[-1][0], pts[-1][1], 6, fill=AM2)
    # step counter
    cx, cy = px0 + pw - 60, py0 - 30
    cv.line([(cx - 40 + 12 * math.cos(a_), cy + 12 * math.sin(a_)) for a_ in np.linspace(.3, 5.6, 20)], MUT, 2.5, 1)
    cv.text(cx - 18, cy, f"{st}", 26, INK, 1, "SemiBold", "lm")
    # our cat + score
    small_grid(cv, 1170, 600, 220, 1)
    v = float(OURP[st]) if st > 0 else float(forward(snap_np(0), X_OURS[None])[-1][0, 0])
    cv.text(1610, 690, f"{v:.2f}", 92, mix(INK, GR, cl((v - .8) * 5)), 1, "SemiBold")
    cv.line([(1450, 800), (1770, 800)], DIM, 8, 1); cv.line([(1450, 800), (1450 + 320 * v, 800)], mix(CY, GR, cl((v - .8) * 5)), 8, 1)
    cat_icon(cv, 1610, 880, 60, mix(CY, GR, cl((v - .8) * 5)), 1, 3)

# ---------- feature tiles
_tiles = {}
def tile(kind, k, n=120):
    key = (kind, k)
    if key in _tiles: return _tiles[key]
    y, x = (np.mgrid[0:n, 0:n] - n / 2) / (n / 2)
    rng = np.random.default_rng(k + 17 * hash(kind) % 1000)
    if kind == "edge":
        th = k * math.pi / 9 * 2.1; f = 2.2 + (k % 3)
        xr = x * math.cos(th) + y * math.sin(th)
        g = np.cos(2 * math.pi * f * xr / 2 + (k % 2) * 1.5) * np.exp(-(x * x + y * y) / .45)
        tint = [np.array(c) for c in ((110, 200, 255), (255, 180, 100), (180, 150, 255), (120, 230, 170))][k % 4]
        img = 128 + g[..., None] * (tint[None, None, :] - 40) * .6
    elif kind == "tex":
        m = k % 4
        if m == 0:   # fur strokes
            a = np.zeros((n, n)); im = Image.fromarray(np.zeros((n, n), np.uint8)); d = ImageDraw.Draw(im)
            for _ in range(160):
                x0, y0 = rng.uniform(0, n, 2); an = .9 + rng.normal(0, .25); L = rng.uniform(8, 18)
                d.line([(x0, y0), (x0 + L * math.cos(an), y0 + L * math.sin(an))], fill=int(rng.uniform(120, 255)), width=2)
            g = np.asarray(im) / 255.
        elif m == 1: g = (np.sin(x * 22) * np.sin(y * 22) > .2) * .9
        elif m == 2: g = .5 + .5 * np.sin(x * 14 + 3 * np.sin(y * 6))
        else: g = ((np.sin(x * 18 + y * 18) > .5) | (np.sin(x * 18 - y * 18) > .7)) * .8
        tint = np.array([(230, 190, 140), (150, 200, 255), (200, 160, 255), (160, 230, 200)][k % 4])
        img = 18 + np.asarray(g)[..., None] * tint[None, None, :] * .85
    else:  # parts
        im = Image.new("RGB", (n, n), (16, 18, 30)); d = ImageDraw.Draw(im)
        m = k % 9
        if m in (0, 4):  # eye
            d.ellipse([20, 35, 100, 85], fill=(200, 210, 150)); d.ellipse([48, 36, 72, 84], fill=(20, 22, 20)); d.ellipse([54, 44, 62, 52], fill=(255, 255, 255))
        elif m in (1, 5):  # ear
            d.polygon([(20, 105), (60, 15), (100, 105)], fill=(190, 170, 150)); d.polygon([(40, 100), (60, 45), (80, 100)], fill=(230, 160, 160))
        elif m == 2:  # nose + whiskers
            d.polygon([(45, 50), (75, 50), (60, 68)], fill=(230, 150, 160))
            for s_ in (-1, 1):
                for j in range(3): d.line([(60 + s_ * 15, 70 + j * 6), (60 + s_ * 58, 62 + j * 12)], fill=(220, 220, 230), width=2)
        elif m == 3:
            im = gray_img(HI, (230, 220, 200)).resize((n, n), Image.LANCZOS)
        elif m == 6:  # wheel (a car part)
            d.ellipse([20, 20, 100, 100], fill=(60, 60, 70)); d.ellipse([42, 42, 78, 78], fill=(180, 180, 190))
        elif m == 7:  # face-ish blob
            d.ellipse([18, 25, 102, 105], fill=(170, 140, 110)); d.ellipse([38, 50, 52, 64], fill=(20, 20, 20)); d.ellipse([68, 50, 82, 64], fill=(20, 20, 20))
        else:  # paw
            d.ellipse([35, 55, 85, 100], fill=(200, 190, 180))
            for j, (xx, yy) in enumerate([(30, 35), (50, 22), (72, 22), (90, 35)]): d.ellipse([xx - 9, yy - 9, xx + 9, yy + 9], fill=(200, 190, 180))
        img = np.asarray(im, np.float32)
    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")
    _tiles[key] = out
    return out

def gallery(cv, cx, cy, kind, a, base=0, sz=118, gap=10, odd=None):
    for i in range(9):
        r_, c_ = divmod(i, 3)
        q = eo(cl(a * 1.6 - i / 9 * .6))
        if q <= 0: continue
        x = cx + (c_ - 1) * (sz + gap) - sz / 2; y = cy + (r_ - 1) * (sz + gap) - sz / 2
        cv.image(tile(kind, base + i), x, y, x + sz, y + sz, q, Image.BILINEAR)
        cv.rect(x, y, x + sz, y + sz, outline=DIM, w=1, a=q)
        if odd is not None and i == 8 and odd > 0:
            cv.image(tile("part", 6), x, y, x + sz / 2, y + sz, odd, Image.BILINEAR)
            cv.rect(x - 4, y - 4, x + sz + 4, y + sz + 4, outline=VI, w=3, a=odd)

def slabs(cv, t, a):
    # stack of feature-map slabs receding in depth
    for k in range(6):
        x = 330 + k * 225; hgt = 420 - k * 50; dep = 6 + k * 5; sk = 70
        for j in range(dep):
            o = j * 7
            pts = [(x + o, 540 - hgt / 2 - o * .5), (x + o + sk, 540 - hgt / 2 - sk * .6 - o * .5), (x + o + sk, 540 + hgt / 2 - sk * .6 - o * .5), (x + o, 540 + hgt / 2 - o * .5)]
            glow = .5 + .5 * math.sin(t * 2 - k * .8 - j * .2)
            cv.poly(pts, mix((14, 20, 40), mix(CY, VI, k / 6), .25 + .3 * glow), a * .5, outline=mix(CY, VI, k / 6), w=1)
        if k < 5:
            cv.line([(x + 70 + dep * 7, 540 - 20), (x + 215, 540 - 10)], MUT, 1.5, a * .4)

def scene_features(cv, t, S, T):
    b = Beat(S)
    cam = Cam(960 + 40 * eo(pr(t, 0, b(0, 1))), 540, 1 + .06 * eo(pr(t, 0, b(0, 1)))); cv.cam = cam
    dust(cv, T, cam)
    sa = eo(pr(t, 0, 1.2)) * (1 - eio(pr(t, b(1, 0), b(1, .08))))
    if sa > 0:
        cv.image(gray_img(HI, (220, 210, 190)), 110, 400, 290, 580, sa, Image.BILINEAR)
        cv.line([(270, 480), (320, 500)], MUT, 2, sa * .6)
        slabs(cv, t, sa)
    old = cv.cam; cv.cam = Cam()
    ca = sa
    chip(cv, 760, 960, "2013", "Zeiler · Fergus", ca * eo(pr(t, b(0, .55), b(0, .62))))
    chip(cv, 1160, 960, "2017", "Olah et al.", ca * eo(pr(t, b(0, .75), b(0, .82))))
    # galleries
    ga = (1 - eio(pr(t, b(2, 0), b(2, .08))))
    if t > b(1, 0) and ga > 0:
        for (cx, kind, t0, lab) in ((420, "edge", .04, "layer 1"), (960, "tex", .22, "layer 3"), (1500, "part", .4, "layer 5")):
            q = pr(t, b(1, t0), b(1, t0 + .14))
            gallery(cv, cx, 540, kind, q * ga, odd=eo(pr(t, b(1, .74), b(1, .82))) if kind == "part" else None)
            cv.text(cx, 330, lab, 28, CY2, eo(q) * ga, "Medium")
        aa = eo(pr(t, b(1, .5), b(1, .62))) * ga
        cv.line([(300, 790), (1620, 790)], MUT, 2, aa)
        cv.arrow(1580, 790, 1640, 790, MUT, 2, aa, 16)
        qa = eo(pr(t, b(1, .78), b(1, .86))) * ga
        cv.math(1500, 860, r"\approx", 50, VI, qa)
    # Hubel & Wiesel
    ha = eo(pr(t, b(2, .02), b(2, .12)))
    if ha > 0:
        cat_icon(cv, 260, 420, 220, MUT, ha, 3)
        cv.line([(300, 360), (480, 300), (560, 420)], AM2, 2, ha * .8)
        rx, ry = 640, 520
        cv.circ(rx, ry, 120, outline=DIM, w=2, a=ha); cv.circ(rx, ry, 120, fill=(12, 16, 30), a=ha * .7)
        th = (t - b(2, 0)) * .55
        ang = (th % math.pi)
        dx, dy = 95 * math.cos(ang), 95 * math.sin(ang)
        cv.line([(rx - dx, ry - dy), (rx + dx, ry + dy)], INK, 14, ha)
        resp = math.exp(-(((ang - math.pi / 4 + math.pi / 2) % math.pi - math.pi / 2) / .3) ** 2)
        # spike raster
        rng = np.random.default_rng(int(t * 30))
        for k in range(60):
            tk = t - k / 30
            angk = ((tk - b(2, 0)) * .55) % math.pi
            rk = math.exp(-(((angk - math.pi / 4 + math.pi / 2) % math.pi - math.pi / 2) / .3) ** 2)
            if np.random.default_rng(int(tk * 30) + 7).random() < .05 + .8 * rk:
                x = 1130 - k * 6
                cv.line([(x, 470), (x, 530)], AM2, 2, ha * (1 - k / 60))
        cv.line([(780, 500), (1130, 500)], DIM, 1, ha * .5)
        cv.glow(rx, ry, 150, AM, ha * resp * .5)
        chip(cv, 640, 720, "1959", "Hubel · Wiesel", ha)
        # network edge filters to compare
        na = eo(pr(t, b(2, .42), b(2, .52)))
        if na > 0:
            for i in range(4):
                x = 1300 + (i % 2) * 140; y = 380 + (i // 2) * 140
                cv.image(tile("edge", i * 2), x, y, x + 120, y + 120, na, Image.BILINEAR)
        sym = eo(pr(t, b(2, .5), b(2, .58)))
        neq = eo(pr(t, b(2, .82), b(2, .9)))
        cv.math(1210, 520, r"\approx", 60, INK, sym * (1 - neq))
        cv.math(1210, 520, r"\neq", 60, AM2, neq)
    cv.cam = old

# ---------- open questions
def valley(cv, cx, cy, wdt, col, a, lab=None):
    pts = [(cx + x * 160, cy - 220 * (1 - math.exp(-(x / wdt) ** 2))) for x in np.linspace(-1.3, 1.3, 70)]
    cv.line(pts, col, 4, a)
    if lab: cv.text(cx, cy + 60, lab, 26, col, a, "Medium")

def ticket(cv, x, y, s, a):
    cv.rrect(x - s, y - s * .55, x + s, y + s * .55, 10, fill=(40, 30, 10), outline=AM2, w=3, a=a)
    for sg in (-1, 1): cv.circ(x + sg * s, y, s * .16, fill=BG0, a=a)
    cv.line([(x - s * .45, y), (x + s * .45, y)], AM2, 3, a * .7)

def scene_open(cv, t, S, T):
    b = Beat(S)
    cam = Cam(); cv.cam = cam
    dust(cv, T, cam)
    # p0
    a0 = eo(pr(t, 0, 1.0)) * (1 - eio(pr(t, b(1, 0), b(1, .08))))
    if a0 > 0:
        bars = eo(pr(t, b(0, .02), b(0, .2))) * (1 - eio(pr(t, b(0, .33), b(0, .4))))
        if bars > 0:
            cv.rect(700, 820 - 560 * bars, 860, 820, fill=(40, 110, 150), a=a0 * .9, outline=CY, w=2)
            cv.rect(1060, 820 - 160 * bars, 1220, 820, fill=(60, 66, 90), a=a0 * .9, outline=MUT, w=2)
            cv.text(780, 880, "weights", 28, CY2, a0 * bars, "Medium")
            for k in range(3): small_grid(cv, 1100 + k * 12, 860 + k * 8, 70, a0 * bars, THUMBS[k])
            cv.math(960, 640, r"\gg", 70, INK, a0 * eo(pr(t, b(0, .12), b(0, .2))) * (1 - eio(pr(t, b(0, .33), b(0, .4)))))
        ra = eo(pr(t, b(0, .38), b(0, .46)))
        if ra > 0:
            for k in range(6):
                x = 330 + k * 160; small_grid(cv, x - 60, 300, 120, a0 * ra, THUMBS[10 + k])
                lab = (k * 7 + 3) % 2
                if lab: cat_icon(cv, x, 250, 50, VI, a0 * ra, 2.5)
                else: notcat_icon(cv, x, 250, 44, VI, a0 * ra, 2.5)
            # training accuracy curve -> 100%
            ca = eo(pr(t, b(0, .55), b(0, .62)))
            q = eio(pr(t, b(0, .58), b(0, .9)))
            X0, Y0, w, h = 1340, 640, 420, 300
            cv.line([(X0, Y0), (X0 + w, Y0)], MUT, 2, a0 * ca); cv.line([(X0, Y0), (X0, Y0 - h)], MUT, 2, a0 * ca)
            n = int(60 * q)
            if n > 1:
                pts = [(X0 + i / 59 * w, Y0 - h * (1 - math.exp(-i / 14)) / (1 - math.exp(-59 / 14))) for i in range(n)]
                cv.line(pts, VI, 4, a0 * ca)
            cv.math(X0 + w + 10, Y0 - h - 30, r"100\%", 34, INK, a0 * eo(pr(t, b(0, .86), b(0, .92))), "rm")
            chip(cv, 960, 980, "2017", "Zhang et al.", a0 * eo(pr(t, b(0, .7), b(0, .78))))
    # p1
    a1 = eo(pr(t, b(1, 0), b(1, .08))) * (1 - eio(pr(t, b(2, 0), b(2, .08))))
    if a1 > 0:
        ta = 1 - eio(pr(t, b(1, .3), b(1, .38)))
        for k in range(6):
            x = 330 + k * 260; small_grid(cv, x - 70, 380, 140, a1 * ta, THUMBS[30 + k])
            ck = eo(pr(t, b(1, .06 + k * .03), b(1, .1 + k * .03)))
            cv.line([(x - 24, 580), (x - 4, 600), (x + 32, 560)], GR, 6, a1 * ta * ck)
        qa = eo(pr(t, b(1, .2), b(1, .28))) * (1 - eio(pr(t, b(1, .36), b(1, .42))))
        cv.text(960, 200, "?", 120, VI, a1 * qa, "SemiBold")
        va = eo(pr(t, b(1, .38), b(1, .46)))
        if va > 0:
            squeeze = eio(pr(t, b(1, .66), b(1, .8)))
            valley(cv, 560, 700, .22, AM, a1 * va, "sharp minimum")
            valley(cv, 1360, 700, lerp(.8, .22, squeeze), CY, a1 * va, "flat minimum")
            ball(cv, ((1360, 700 - 13), 0), 12, a1 * va)
            cv.math(1360, 380, r"w \to \alpha\, w", 40, INK, a1 * eo(pr(t, b(1, .62), b(1, .7))))
            q2 = eo(pr(t, b(1, .82), b(1, .9)))
            cv.text(960, 560, "?", 90, VI, a1 * q2, "SemiBold")
            chip(cv, 760, 980, "2017", "Keskar et al.", a1 * eo(pr(t, b(1, .5), b(1, .58))))
            chip(cv, 1160, 980, "2017", "Dinh et al.", a1 * eo(pr(t, b(1, .7), b(1, .78))))
    # p2 lottery ticket
    a2 = eo(pr(t, b(2, 0), b(2, .08)))
    if a2 > 0:
        pz = eio(pr(t, b(2, .6), b(2, .7)))
        cv.cam = Cam(1010 - (lerp(800, 620, pz) - 960) / .7, 540, .7)
        prune = eio(pr(t, b(2, .14), b(2, .34)))
        draw_net(cv, len(SNAPS) - 1, a2 * (1 - .75 * prune) * (1 - .4 * pz), x=X_OURS, kink=1)
        rng = np.random.default_rng(12)
        P = snap_np(len(SNAPS) - 1)
        if prune > 0:
            for j in range(16):
                for s_, k in enumerate(SLOT_PIX):
                    if rng.random() < .07:
                        cv.line([(INP_X + 12, SLOT_Y[s_]), (H1_X - 13, H1_Y[j])], AM2, 2.2, a2 * prune)
            for i in range(8):
                for j in range(16):
                    if rng.random() < .12:
                        cv.line([(H1_X + 13, H1_Y[j]), (H2_X - 16, H2_Y[i])], AM2, 2.6, a2 * prune)
            for i in range(0, 8, 2):
                cv.line([(H2_X + 16, H2_Y[i]), (OUT_X - 24, OUT_Y)], AM2, 3, a2 * prune)
        cv.cam = Cam()
        tk = eo(pr(t, b(2, .3), b(2, .38))) * (1 - pz)
        ticket(cv, 1500, 260, 70, a2 * tk)
        cv.text(1500, 360, "lottery ticket", 28, AM2, a2 * tk, "Medium")
        chip(cv, 1500, 980, "2019", "Frankle · Carbin", a2 * eo(pr(t, b(2, .36), b(2, .44))) * (1 - pz))
        # puzzle
        if pz > 0:
            pos = [(1360, 400), (1580, 400), (1360, 620), (1580, 620)]
            for k, (x, y) in enumerate(pos):
                q = eo(cl(pz * 1.5 - k * .15))
                if k < 3:
                    cv.rrect(x - 95, y - 95, x + 95, y + 95, 22, fill=(18, 22, 42), outline=mix(CY, VI, k / 3), w=2.5, a=q)
                    if k == 0: valley(cv, x, y + 70, .7, CY, q * .9) if False else cv.line([(x + u * 70, y + 40 - 70 * (1 - math.exp(-(u / .6) ** 2))) for u in np.linspace(-1, 1, 30)], CY, 4, q)
                    if k == 1: cv.line([(x - 60 + i * 12, y + (20 if i % 2 else -20) - i * 3) for i in range(11)], AM2, 3, q)
                    if k == 2: ticket(cv, x, y, 52, q)
                else:
                    pul = .5 + .5 * math.sin(t * 3)
                    cv.rrect(x - 95, y - 95, x + 95, y + 95, 22, outline=VI, w=2.5, a=q * (.4 + .5 * pul))
                    cv.text(x, y, "?", 80, VI, q * (.6 + .4 * pul), "SemiBold")

# ---------- close
def scene_close(cv, t, S, T):
    b = Beat(S)
    zin = eio(pr(t, b(0, .2), b(0, .4))) * (1 - eio(pr(t, b(1, 0), b(1, .12))))
    cam = Cam(960, 540 + 40 * zin, 1 + 1.2 * zin); cv.cam = cam
    dust(cv, T, cam)
    a0 = eo(pr(t, 0, 1.0)) * (1 - eio(pr(t, b(1, 0), b(1, .12))))
    if a0 > 0:
        phone(cv, a0, unlock=1.0)
        scr = eio(pr(t, b(0, .52), b(0, .62))) * (1 - eio(pr(t, b(0, .75), b(0, .92))))
        tick = int(t * 7)
        for i, (u, v) in enumerate(FACE):
            x0, y0 = PH_X + u * 125, PH_Y + 30 + v * 125 * 1.05
            r = np.random.default_rng(i * 31); jx, jy = r.uniform(-1, 1, 2)
            x, y = x0 + scr * jx * 110, y0 + scr * jy * 160
            col = mix(CY, MUT, scr)
            if zin > .4 and i % 2 == 0:
                val = np.random.default_rng(i * 999 + tick).uniform(-1, 1) if scr > .1 else math.sin(i * 1.7) * .9
                cv.text(x, y, f"{val:+.2f}", 11, col, a0, "Medium")
            else:
                cv.circ(x, y, 3, fill=col, a=a0)
    # p1: the long descent toward the horizon
    a1 = eo(pr(t, b(1, 0), b(1, .12))) * (1 - eio(pr(t, b(2, 0), b(2, .1))))
    if a1 > 0:
        pull = eio(pr(t, b(1, .1), b(1, 1)))
        cam2 = Cam(lerp(500, 960, pull), 540, lerp(2.2, .8, pull)); cv.cam = cam2
        n = len(SM)
        pts = [(100 + i / (n - 1) * 1720, 300 + 500 * (1 - cl(SM[i] / .75))) for i in range(0, n, 3)]
        prog = eio(pr(t, b(1, .05), b(1, .8)))
        m = max(2, int(len(pts) * prog))
        cv.line(pts[:m], AM, 3, a1)
        for p in pts[:m:6]: cv.circ(p[0], p[1], 3, fill=AM2, a=a1 * .7)
        cv.glow(pts[m - 1][0], pts[m - 1][1], 60, AM, a1)
        cv.circ(pts[m - 1][0], pts[m - 1][1], 8, fill=INK, a=a1)
        cv.cam = Cam()
    # end card
    a2 = eo(pr(t, b(2, 0), b(2, .15)))
    if a2 > 0:
        cv.text(960, 470, "LATOON", 170, LOGO, a2, "Black")
        cv.line([(800, 580), (800 + 320 * eo(pr(t, b(2, .1), b(2, .5))), 580)], LOGO, 3, a2 * .8)
        bx, by = 960, 690
        ba = eo(pr(t, b(2, .3), b(2, .45)))
        sw = math.sin(t * 6) * .25 * (1 - pr(t, b(2, .45), b(2, 1)))
        pts = []
        for k in range(21):
            u = k / 20; ang = math.pi + math.pi * u
            pts.append((bx + 34 * math.cos(ang), by - 6 + 34 * math.sin(ang)))
        pts = [(bx - 40, by + 26), (bx - 34, by - 6)] + pts + [(bx + 34, by - 6), (bx + 40, by + 26)]
        rot = [(bx + (x - bx) * math.cos(sw) - (y - by + 40) * math.sin(sw), by - 40 + (x - bx) * math.sin(sw) + (y - by + 40) * math.cos(sw)) for x, y in pts]
        cv.line(rot + [rot[0]], INK, 4, a2 * ba)
        cv.circ(bx - 40 * math.sin(sw), by + 40 - 40 * math.cos(sw) + 36, 7, fill=INK, a=a2 * ba)
        cv.text(960, 790, "@its_Latoon", 30, MUT, a2 * eo(pr(t, b(2, .4), b(2, .6))), "Medium")
