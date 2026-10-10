from common import *

STREAM_Y = [300 + k * 26 for k in range(14)]

def _streams(cv, t, a, x0=330, x1=2000, over=False, ys=STREAM_Y, speed=220):
    for k, y in enumerate(ys):
        yy = y + 10 * math.sin(k * 1.7)
        stream(cv, x0, yy - 30 * ((k % 3) - 1), x1, yy + 40 * ((k % 3) - 1), t + k * .37, a * (.35 if over else .75), TERRA, 2.0, speed)

# ------------------------------------------------------------ HOOK
def scene_hook(cv, t, S, T):
    b = Beat(S)
    t_pull = b.kw(0, "Many flew"); t_nob = b.kw(1, "This year")
    # camera: start on the nail, pull back to the whole picture, then drift to the South Pole
    u = eio(pr(t, t_pull - .3, t_pull + 3.2))
    cx, cy, z = lerp(1520, 960, u), lerp(470, 540, u), lerp(2.5, 1.0, u)
    v = eio(pr(t, t_nob, t_nob + 2.8))
    cx, cy, z = lerp(cx, 880, v), lerp(cy, 600, v), lerp(z, 1.3, v)
    cv.cam = Cam(cx, cy, z + .015 * math.sin(t * .4))
    sun(cv, 230, 420, 105, t)
    earth_layers(cv, 860, 470, 250)
    _streams(cv, t, 1)
    # ice block at the South Pole (appears with the Nobel line)
    q = eo(pr(t, t_nob + 1.6, t_nob + 2.6))
    if q > 0:
        px, py = 860, 720
        cv.poly([(px - 46, py - 4), (px + 46, py - 4), (px + 40, py + 40 * q), (px - 40, py + 40 * q)], ICE, q, INK, 2.5)
        cv.poly([(px - 46, py - 4), (px - 30, py - 18), (px + 62, py - 18), (px + 46, py - 4)], SNOW, q, INK, 2.5)
        cv.line([(px + 30, py - 18), (px + 30, py - 70 * q)], INK, 3, q)
        cv.poly([(px + 30, py - 70 * q), (px + 62, py - 60 * q), (px + 30, py - 50 * q)], TERRA, q)
        chip(cv, px, py + 92, "South Pole", eo(pr(t, t_nob + 2.2, t_nob + 3)) * 1.0, size=20)
    finger(cv, 1520, 720)
    _streams(cv, t, 1, over=True)
    # screen-space annotations
    cam = cv.cam; cv.cam = Cam()
    t65 = b.kw(0, "sixty-five")
    a65 = win(t, t65 - .2, t_pull + 7.0, .5, .8)
    if a65 > 0:
        n = 65e9 * eo(pr(t, t65, t65 + 1.8))
        panel(cv, 90, 720, 760, 930, a65)
        cv.text(120, 820, f"{n:,.0f}", 92, INK, a65, "Black", "lm")
        cv.text(124, 892, "neutrinos / second", 30, INK2, a65 * eo(pr(t, t65 + .8, t65 + 1.6)), "SemiBold", "lm")
        cv.line([(124, 760), (124 + 260 * eo(pr(t, t65, t65 + 1)), 760)], TERRA, 5, a65)
    tn = b.kw(1, "neutrinos")
    an = win(t, tn, t_nob + .2, .6, .6)
    if an > 0:
        panel(cv, 90, 730, 640, 920, an)
        cv.text(120, 820, "ν", 120, TERRA, an, "Bold", "lm")
        cv.text(210, 812, "neutrino", 58, INK, an, "Bold", "lm")
        cv.text(212, 870, "the ghost particle", 30, INK2, an * eo(pr(t, b.kw(1, "ghost"), b.kw(1, "ghost") + .6)), "Medium", "lm")
    tq = b.kw(1, "So how")
    aq = win(t, tq, t_nob + .4, .5, .5)
    if aq > 0:
        cv.text(1780, 200, "?", 200, TERRA, aq, "Black")
    ab = win(t, t_nob + 1.0, S["dur"] + 1, .8, .5)
    if ab > 0:
        panel(cv, 1450, 120, 1830, 370, ab)
        cv.circ(1640, 220, 74, fill=OCHRE, a=ab); cv.circ(1640, 220, 60, fill=(222, 172, 78), a=ab); cv.circ(1640, 220, 74, outline=INK, w=3, a=ab)
        cv.text(1640, 222, "2026", 30, INK, ab, "Bold")
        cv.text(1640, 330, "Nobel Prize in Physics", 26, INK2, ab, "SemiBold")
    cv.cam = cam

# ------------------------------------------------------------ STING (title)
def scene_sting(cv, t, S, T):
    cv.cam = Cam(960, 540, 1 + .02 * t)
    a = eo(pr(t, 0, .8))
    # isometric ice cube
    s = 1.0; ox, oy = 1380, 610
    L = 300
    def P(x, y, z): return iso(x, y, z, ox, oy, s)
    top = [P(0, 0, L), P(L, 0, L), P(L, L, L), P(0, L, L)]
    left = [P(0, L, L), P(L, L, L), P(L, L, 0), P(0, L, 0)]
    right = [P(L, 0, L), P(L, L, L), P(L, L, 0), P(L, 0, 0)]
    cv.poly([(x + 18, y + 26) for x, y in left + right], (60, 45, 30), a * .12)
    cv.poly(left, ICE2, a, INK, 3); cv.poly(right, ICE3, a, INK, 3); cv.poly(top, SNOW, a, INK, 3)
    # strings visible on faces
    for k in range(1, 5):
        x0, y0 = P(k * L / 5, L, L); x1, y1 = P(k * L / 5, L, 0)
        cv.line([(x0, y0), (x1, y1)], INK2, 1.5, a * .5)
        for j in range(1, 8): cv.circ(lerp(x0, x1, j / 8), lerp(y0, y1, j / 8), 3.5, fill=INK, a=a * .6)
    u = eo(pr(t, .6, 2.6))
    stream(cv, 980, 160, 1820, 1020, t, a, TERRA, 3, 200, reveal=u)
    cv.text(120, 430, "CATCHING", 150, INK, a, "Black", "lm")
    cv.text(120, 590, "A GHOST", 150, TERRA, eo(pr(t, .25, 1.1)), "Black", "lm")
    cv.line([(124, 700), (124 + 520 * eo(pr(t, .5, 1.5)), 700)], INK, 4, a)
    cv.text(124, 752, "LATOON  ·  Voyaging the Unseen", 28, INK2, eo(pr(t, .9, 1.7)), "SemiBold", "lm")

# ------------------------------------------------------------ GHOST (history + why hard)
def nucleus(cv, x, y, r, a=1, shake=0.0):
    rng = np.random.default_rng(2)
    for k in range(14):
        ang = rng.uniform(0, 6.28); rr = r * .55 * math.sqrt(rng.uniform(0, 1))
        dx, dy = rr * math.cos(ang) + shake * math.sin(k * 7.1), rr * math.sin(ang) + shake * math.cos(k * 3.3)
        c = TERRA2 if k % 2 else OCHRE2
        cv.circ(x + dx + 2, y + dy + 3, r * .32, fill=(60, 45, 30), a=a * .12)
        cv.circ(x + dx, y + dy, r * .32, fill=c, a=a, outline=INK, w=2)

def reactor(cv, x, y, s, a=1):
    cv.poly([(x - 90 * s, y), (x - 60 * s, y - 120 * s), (x - 66 * s, y - 210 * s), (x + 66 * s, y - 210 * s), (x + 60 * s, y - 120 * s), (x + 90 * s, y)], PAPER3, a, INK, 3)
    cv.line([(x - 60 * s, y - 120 * s), (x + 60 * s, y - 120 * s)], INK2, 1.5, a * .5)
    for k in range(3): cv.circ(x - 20 * s + k * 26 * s, y - 250 * s - k * 22 * s, (22 + 8 * k) * s, fill=SNOW, a=a * .8, outline=RULE, w=2)

def scene_ghost(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    t26 = b.kw(0, "It took"); t56 = b.kw(0, "In 1956"); tw = b(1)
    A1 = win(t, 0, t26 + .3, .4, .7)       # 1930 letter + beta decay
    A2 = win(t, t26 - .1, tw + .2, .7, .7)  # timeline + reactor
    A3 = win(t, tw, S["dur"] + 1, .7, .5)   # atom + person detector
    chapter_tag(cv, "01", "A desperate remedy", win(t, 0, tw + .2))
    if A1 > 0:
        cv.ga = A1
        cv.text(120, 250, "1930", 150, TERRA, eo(pr(t, .2, 1.2)), "Black", "lm")
        # Pauli's letter (abstract)
        q = eo(pr(t, .6, 1.8))
        cx, cy = 370, 650
        cv.poly([(cx - 190 + 12, cy - 230 + 16), (cx + 190 + 12, cy - 250 + 16), (cx + 210 + 12, cy + 250 + 16), (cx - 170 + 12, cy + 270 + 16)], (60, 45, 30), q * .12)
        cv.poly([(cx - 190, cy - 230), (cx + 190, cy - 250), (cx + 210, cy + 250), (cx - 170, cy + 270)], SNOW, q, RULE, 2)
        for k in range(12):
            y0 = cy - 190 + k * 30; L = 300 if k % 4 != 3 else 180
            x0 = cx - 160 + k * 1.6
            cv.line([(x0, y0 - k * 0.0), (x0 + L * eo(pr(t, 1 + k * .12, 1.4 + k * .12)), y0 - L * .05)], INK2, 3, q * .55)
        cv.line([(cx + 20, cy + 205), (cx + 50, cy + 185), (cx + 70, cy + 210), (cx + 100, cy + 182), (cx + 140, cy + 200)], INK, 3, q * eo(pr(t, 2.6, 3.4)))
        # beta decay
        td = b.kw(0, "decay"); tm = b.kw(0, "missing"); tr = b.kw(0, "desperate")
        nx, ny = 1060, 470
        nucleus(cv, nx, ny, 120, eo(pr(t, .5, 1.5)), shake=2 * math.sin(t * 9) * (1 - pr(t, td, td + .4)))
        qe = eo(pr(t, td, td + 1.2))
        if qe > 0:
            ex, ey = lerp(nx, 1560, qe), lerp(ny, 320, qe)
            cv.line([(nx + 60, ny - 20), (ex, ey)], INK2, 2, .4 * qe)
            cv.circ(ex, ey, 22, fill=INK, a=1); cv.text(ex + 46, ey - 4, "e⁻", 34, INK, 1, "Bold")
        qn = eo(pr(t, tr + .4, tr + 1.6))
        if qn > 0:
            stream(cv, nx + 60, ny + 30, lerp(nx + 60, 1600, qn), lerp(ny + 30, 600, qn), t, 1, TERRA, 3, 160)
            cv.text(lerp(nx + 60, 1600, qn) + 40, lerp(ny + 30, 600, qn), "ν", 46, TERRA, qn, "Bold")
        # energy bars
        qb = eo(pr(t, td + .4, td + 1.4))
        if qb > 0:
            bx, by, bw = 860, 780, 820
            cv.text(bx - 24, by + 26, "E", 34, INK2, qb, "Bold", "rm")
            cv.rect(bx, by, bx + bw * qb, by + 52, fill=OCHRE, a=qb, outline=INK, w=2)
            cv.text(bx - 24, by + 126, "E", 34, INK2, qb, "Bold", "rm")
            e_w = bw * .62
            cv.rect(bx, by + 100, bx + e_w * qb, by + 152, fill=OCHRE, a=qb, outline=INK, w=2)
            cv.text(bx + 18, by + 126, "e⁻", 28, INK, qb, "Bold", "lm")
            qm = eo(pr(t, tm - .2, tm + .6))
            if qm > 0 and qn < 1:
                dashed(cv, [(bx + e_w, by + 100), (bx + bw, by + 100), (bx + bw, by + 152), (bx + e_w, by + 152)], TERRA, 2.5, qm * (1 - qn))
                cv.text(bx + (e_w + bw) / 2, by + 126, "?", 44, TERRA, qm * (1 - qn), "Black")
            if qn > 0:
                cv.rect(bx + e_w, by + 100, bx + e_w + (bw - e_w) * qn, by + 152, fill=TERRA2, a=1, outline=INK, w=2)
                cv.text(bx + (e_w + bw) / 2, by + 126, "ν", 34, INK, qn, "Bold")
        cv.ga = 1
    if A2 > 0:
        cv.ga = A2
        q = eo(pr(t, t26, t26 + 1.6))
        x0, x1, y = 260, 1660, 300
        cv.line([(x0, y), (lerp(x0, x1, q), y)], INK, 4)
        for k in range(27):
            xx = lerp(x0, x1, k / 26)
            if xx <= lerp(x0, x1, q): cv.line([(xx, y - (16 if k % 5 == 0 else 8)), (xx, y + (16 if k % 5 == 0 else 8))], INK, 2)
        cv.text(x0, y - 60, "1930", 48, TERRA, 1, "Black")
        cv.text(x1, y - 60, "1956", 48, TERRA, eo(pr(t, t26 + 1.2, t26 + 1.8)), "Black")
        cv.text((x0 + x1) / 2, y + 56, "26 years", 34, INK2, eo(pr(t, t26 + .8, t26 + 1.6)), "SemiBold")
        q2 = eo(pr(t, t56, t56 + 1.2))
        if q2 > 0:
            reactor(cv, 560, 860, 1.0, q2)
            for k in range(6):
                stream(cv, 660, 640 + k * 34, 1240, 640 + k * 34 + (k - 2.5) * 10, t + k * .3, q2 * .8, TERRA, 2, 180)
            # detector tank
            tx, ty = 1400, 760
            cv.rrect(tx - 150 + 10, ty - 110 + 14, tx + 150 + 10, ty + 110 + 14, 18, fill=(60, 45, 30), a=q2 * .12)
            cv.rrect(tx - 150, ty - 110, tx + 150, ty + 110, 18, fill=ICE, a=q2, outline=INK, w=3)
            cv.rect(tx - 150, ty - 40, tx + 150, ty + 110, fill=ICE2, a=q2 * .7)
            fl = 0.5 + 0.5 * math.sin(t * 3)
            fl = max(0, math.sin((t - t56) * 2.1)) ** 8
            cv.circ(tx + 30, ty + 30, 18 + 40 * fl, fill=CHER2, a=q2 * fl * .8)
            cv.rrect(tx - 150, ty - 110, tx + 150, ty + 110, 18, outline=INK, w=3, a=q2)
            chip(cv, 1020, 980, "Cowan  ·  Reines", eo(pr(t, t56 + .8, t56 + 1.6)), size=26)
        cv.ga = 1
    if A3 > 0:
        cv.ga = A3
        chapter_tag(cv, "02", "Why so hard?", 1)
        tp = b.kw(1, "With a detector")
        ua = 1 - eio(pr(t, tp - .2, tp + .8))
        if ua > 0:
            cx, cy = 900, 560
            zz = eo(pr(t, tw, tw + 1.5))
            for k, (rx, ry, rot) in enumerate([(330, 120, .4), (330, 120, -.6), (330, 120, 1.5)]):
                pts = [(cx + rx * math.cos(a_) * math.cos(rot) - ry * math.sin(a_) * math.sin(rot), cy + rx * math.cos(a_) * math.sin(rot) + ry * math.sin(a_) * math.cos(rot)) for a_ in np.linspace(0, 6.3, 80)]
                cv.line(pts, INK2, 2, ua * zz * .55)
                ph = t * (.8 + .3 * k) + k * 2
                ex = cx + rx * math.cos(ph) * math.cos(rot) - ry * math.sin(ph) * math.sin(rot); ey = cy + rx * math.cos(ph) * math.sin(rot) + ry * math.sin(ph) * math.cos(rot)
                cv.circ(ex, ey, 9, fill=INK, a=ua * zz)
            cv.circ(cx, cy, 380, outline=RULE, w=2, a=ua * zz)
            nucleus(cv, cx, cy, 26, ua * zz)
            for k in range(5):
                stream(cv, 100, 340 + k * 110, 1820, 300 + k * 120, t + k * .4, ua * zz, TERRA, 2.6, 260)
            c1, c2 = b.kw(1, "no electric"), b.kw(1, "almost no mass")
            cv.text(1460, 420, "charge", 30, INK2, ua * eo(pr(t, c1, c1 + .6)), "SemiBold", "lm")
            cv.text(1460, 470, "0", 64, TERRA, ua * eo(pr(t, c1, c1 + .6)), "Black", "lm")
            cv.text(1460, 590, "mass", 30, INK2, ua * eo(pr(t, c2, c2 + .6)), "SemiBold", "lm")
            cv.text(1460, 640, "≈ 0", 64, TERRA, ua * eo(pr(t, c2, c2 + .6)), "Black", "lm")
        ub = eo(pr(t, tp, tp + 1.0))
        if ub > 0:
            cx, cy = 760, 600
            cv.rrect(cx - 170 + 12, cy - 300 + 16, cx + 170 + 12, cy + 300 + 16, 20, fill=(60, 45, 30), a=ub * .12)
            cv.rrect(cx - 170, cy - 300, cx + 170, cy + 300, 20, fill=ICE, a=ub, outline=INK, w=3)
            cv.circ(cx, cy - 170, 56, fill=ICE3, a=ub)
            cv.rrect(cx - 95, cy - 100, cx + 95, cy + 270, 70, fill=ICE3, a=ub)
            for k in range(6):
                stream(cv, 150, 380 + k * 90, 1780, 360 + k * 96, t + k * .5, ub, TERRA, 2.4, 300)
            yrs = 100 * eo(pr(t, tp + .8, S["dur"] - 2.0))
            cv.text(1180, 560, f"{yrs:,.0f}", 170, INK, ub, "Black", "lm")
            cv.text(1186, 680, "years, on average", 34, INK2, ub, "SemiBold", "lm")
            cv.text(1186, 730, "for one neutrino to hit", 34, INK2, ub, "SemiBold", "lm")
            hit = pr(t, S["dur"] - 2.0, S["dur"] - .6)
            if 0 < hit < 1:
                cv.circ(cx + 20, cy + 40, 20 + 120 * hit, fill=CHER2, a=(1 - hit) * .7)
                cv.circ(cx + 20, cy + 40, 12, fill=CHER, a=1 - hit)
        cv.ga = 1

# ------------------------------------------------------------ BIGGER (shooting stars + cosmic rays)
def scene_bigger(cv, t, S, T):
    b = Beat(S); cv.cam = Cam(960, 540, 1.0)
    t2 = b(1)
    A1 = win(t, 0, t2 + .3, .5, .7)
    A2 = win(t, t2, S["dur"] + 1, .7, .5)
    chapter_tag(cv, "03", "Build a bigger trap", A1)
    if A1 > 0:
        cv.ga = A1
        tw_ = b.kw(0, "Watch the whole"); ts_ = b.kw(0, "Think of")
        x0, y0, x1, y1 = 220, 180, 1700, 900
        cv.rrect(x0 + 14, y0 + 18, x1 + 14, y1 + 18, 26, fill=(60, 45, 30), a=.14)
        cv.rrect(x0, y0, x1, y1, 26, fill=(44, 42, 50), a=eo(pr(t, 0, 1)), outline=INK, w=3)
        rng = np.random.default_rng(9)
        for k in range(260):
            x, y = rng.uniform(x0 + 20, x1 - 20), rng.uniform(y0 + 20, y1 - 20)
            r = rng.uniform(.8, 2.6)
            cv.circ(x, y, r, fill=(240, 230, 205), a=(.35 + .5 * rng.random()) * (.75 + .25 * math.sin(t * 1.5 + k)))
        # small patch
        px, py, ps = 1180, 420, 150
        qp = eo(pr(t, ts_ + 1.0, ts_ + 2.0)) * (1 - eio(pr(t, tw_, tw_ + 1)))
        cv.rect(px, py, px + ps, py + ps, outline=OCHRE, w=4, a=qp)
        seen_patch = 0; seen_all = 0
        rng2 = np.random.default_rng(21)
        for k in range(40):
            st = tw_ + .2 + rng2.uniform(0, b.PD[0] + 3); sx, sy = rng2.uniform(x0 + 100, x1 - 200), rng2.uniform(y0 + 60, y1 - 200)
            u = pr(t, st, st + .9)
            if 0 < u < 1:
                L = 260
                cv.line([(sx + L * u - 140, sy + L * .5 * u - 70), (sx + L * u, sy + L * .5 * u)], (250, 236, 200), 4, (1 - u) ** .5)
                cv.circ(sx + L * u, sy + L * .5 * u, 4, fill=(255, 246, 220), a=1 - u)
            if t > st: seen_all += 1
        cv.text(x1 - 40, y1 - 50, f"{seen_all}", 64, OCHRE2, eo(pr(t, tw_, tw_ + .6)), "Black", "rm")
        cv.text(px + ps / 2, py + ps + 40, "0", 40, OCHRE2, qp, "Black")
        cv.ga = 1
    if A2 > 0:
        cv.ga = A2
        chapter_tag(cv, "04", "Messengers from deep space", 1)
        tc = b.kw(1, "cosmic rays"); tm = b.kw(1, "But magnetic"); tn = b.kw(1, "Neutrinos are made"); th = b.kw(1, "They point")
        # source: black hole with jets (left)
        sx, sy = 330, 540
        q = eo(pr(t, t2, t2 + 1.2))
        for k in range(5):
            cv.circ(sx, sy, 120 - k * 18, fill=mix(OCHRE2, TERRA, k / 5), a=q * .5)
        cv.circ(sx, sy, 34, fill=INK, a=q)
        cv.poly([(sx - 10, sy - 30), (sx + 10, sy - 30), (sx + 40, sy - 260), (sx - 40, sy - 260)], OCHRE2, q * .55)
        cv.poly([(sx - 10, sy + 30), (sx + 10, sy + 30), (sx + 40, sy + 260), (sx - 40, sy + 260)], OCHRE2, q * .55)
        # Earth (right)
        ex, ey = 1600, 540
        earth_cut(cv, ex, ey, 110, q)
        # magnetic field lines
        qm = eo(pr(t, tm - .3, tm + 1.0))
        for k in range(7):
            yy = 220 + k * 105
            pts = [(x, yy + 40 * math.sin(x / 160 + k)) for x in range(520, 1440, 20)]
            cv.line(pts, PLUM, 2, qm * .35)
        # cosmic rays: curved paths
        qc = eo(pr(t, tc, tc + .5))
        for k in range(5):
            ph = (t - tc) * .25 + k * .2
            u = ph % 1.0
            pts = []
            for j in range(60):
                s_ = j / 59 * u
                x = lerp(sx + 60, 1450, s_)
                y = sy + (k - 2) * 50 + 220 * math.sin(s_ * (5 + k) + k) * qm * s_
                pts.append((x, y))
            if len(pts) > 1:
                cv.line(pts, OCHRE, 2.5, qc * (1 - u) * .8)
                cv.circ(pts[-1][0], pts[-1][1], 12, fill=OCHRE, a=qc * (1 - u), outline=INK, w=2)
                cv.text(pts[-1][0], pts[-1][1] - 1, "+", 18, INK, qc * (1 - u), "Black")
        qn = eo(pr(t, tn, tn + 1.5))
        if qn > 0:
            stream(cv, sx + 40, sy, lerp(sx + 40, ex - 115, qn), sy, t, 1, TERRA, 4, 220)
            cv.text(lerp(sx + 40, ex - 115, qn) - 60, sy - 50, "ν", 54, TERRA, qn, "Bold")
        qh = eo(pr(t, th, th + 1.2))
        if qh > 0:
            cv.arrow(ex - 180, sy + 70, lerp(ex - 180, sx + 80, qh), sy + 70, INK, 3, qh, 18)
            cv.text((ex + sx) / 2, sy + 120, "points straight back", 30, INK2, qh, "SemiBold")
        cv.text(sx, 860, "source", 28, INK2, q, "SemiBold")
        cv.text(ex, 700, "Earth", 28, INK2, q, "SemiBold")
        cv.text(980, 140, "cosmic ray  +", 28, OCHRE, qc, "Bold")
        cv.ga = 1
