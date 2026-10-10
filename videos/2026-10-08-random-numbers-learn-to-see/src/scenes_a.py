from common import *

# ---------- face dots (stylized face for phone hook)
_r = np.random.default_rng(11)
FACE = []
for i in range(44):
    a_ = 2 * math.pi * i / 44
    FACE.append((.78 * math.cos(a_), 1.0 * math.sin(a_) * (1 - .12 * max(0, math.sin(a_)))))
for sg in (-1, 1):
    for i in range(10):
        a_ = 2 * math.pi * i / 10; FACE.append((sg * .33 + .14 * math.cos(a_), -.18 + .07 * math.sin(a_)))
    for i in range(6): FACE.append((sg * (.18 + .07 * i), -.36 - .03 * math.sin(i / 5 * math.pi)))
for i in range(6): FACE.append((.0 + .02 * math.sin(i), -.05 + .06 * i))
for i in range(5): FACE.append(((i - 2) * .05, .28))
for i in range(13): FACE.append(((i - 6) * .055, .5 + .06 * math.cos((i - 6) / 6 * math.pi / 2) - .06))
while len(FACE) < 150:
    u, v = _r.uniform(-.7, .7), _r.uniform(-.9, .9)
    if (u / .74) ** 2 + (v / .95) ** 2 < 1: FACE.append((u, v))
FACE = np.array(FACE)
FACE_VAL = _r.uniform(-1, 1, len(FACE))
# triangulation-ish mesh: connect each dot to 2 nearest
_d = np.linalg.norm(FACE[:, None] - FACE[None], axis=2); np.fill_diagonal(_d, 9)
MESH = sorted({tuple(sorted((i, int(j)))) for i in range(len(FACE)) for j in np.argsort(_d[i])[:3]})

PH_X, PH_Y, PH_W, PH_H = 960, 540, 330, 640

def phone(cv, a, unlock=0.0, x=PH_X, y=PH_Y):
    cv.rrect(x - PH_W / 2 - 6, y - PH_H / 2 - 6, x + PH_W / 2 + 6, y + PH_H / 2 + 6, 52, fill=(10, 13, 26), a=a, outline=mix(DIM, INK, .25), w=3)
    cv.rrect(x - PH_W / 2 + 6, y - PH_H / 2 + 6, x + PH_W / 2 - 6, y + PH_H / 2 - 6, 44, fill=(13, 18, 36), a=a)
    cv.rrect(x - 42, y - PH_H / 2 + 18, x + 42, y - PH_H / 2 + 40, 11, fill=(4, 5, 10), a=a)
    # lock glyph
    lx, ly = x, y - PH_H / 2 + 92
    col = mix(MUT, CY, unlock)
    cv.rrect(lx - 17, ly - 4, lx + 17, ly + 22, 5, fill=col, a=a)
    lift = 10 * eback(unlock)
    pts = [(lx - 10, ly - 3)] + [(lx + 10 * math.cos(math.pi - math.pi * i / 12), ly - 12 - lift - 10 * math.sin(math.pi * i / 12)) for i in range(13)] + [(lx + 10, ly - 3 - lift * (1 if unlock > 0 else 0))]
    pts[0] = (lx - 10, ly - 3 - lift)
    cv.line(pts, col, 4, a)
    if unlock > 0:
        cv.circ(lx, ly + 4, 30 + 70 * unlock, outline=CY, w=3, a=a * (1 - unlock) * .8)

def scene_hook(cv, t, S, T):
    b = Beat(S)
    unlock = eo(pr(t, b(0, .30), b(0, .30) + .6))
    zoom_in = eio(pr(t, b(0, .36), b(0, .58)))
    cam = Cam(960, 540 + 40 * zoom_in, 1 + 1.25 * zoom_in)
    # p1: pull back to show cat + network
    pull = eio(pr(t, b(1, .25), b(1, .45)))
    cam.z = lerp(cam.z, 1.0, pull); cam.cy = lerp(cam.cy, 540, pull)
    cv.cam = cam
    dust(cv, T, cam)
    pa = eo(pr(t, 0, .8)) * (1 - eio(pr(t, b(0, .62), b(0, .8))))
    phone(cv, pa, unlock)
    # face dots
    fa = eo(pr(t, .4, 2.0))
    scan = pr(t, .8, b(0, .28))
    sc = 125
    rnd = pr(t, b(0, .62), b(0, .82))   # numbers become random / chaotic
    swirl = eio(pr(t, b(1, 0), b(1, .3)))
    form = eio(pr(t, b(1, .25), b(1, .48)))
    tick = int(t * 7)
    for i, (u, v) in enumerate(FACE):
        x0, y0 = PH_X + u * sc, PH_Y + 30 + v * sc * 1.05
        # chaos drift
        rr = np.random.default_rng(i * 31)
        jx, jy = rr.uniform(-1, 1, 2)
        x1 = x0 + rnd * (jx * 140 + 30 * math.sin(t * 1.3 + i)); y1 = y0 + rnd * (jy * 200 + 30 * math.cos(t * 1.1 + i * .7))
        # swirl into a pile
        ang = i * 2.39996 + t * .9; rad = 30 + 2.2 * math.sqrt(i) * 9
        x2, y2 = 960 + rad * math.cos(ang), 540 + rad * math.sin(ang) * .8
        x, y = lerp(x1, x2, swirl), lerp(y1, y2, swirl)
        if form >= 1: continue
        lit = cl((scan * 1.25 - (v + 1) / 2 * 1.0) * 3) if t < b(0, .35) else 1
        col = mix(MUT, CY, lit * (1 - rnd * .6))
        al = fa * (1 - form) * (.45 + .55 * lit)
        if (zoom_in > .3 or rnd > 0) and i % 2 == 0:
            val = FACE_VAL[i] if rnd < .05 else np.random.default_rng(i * 1000 + tick).uniform(-1, 1)
            cv.text(x, y, f"{val:+.2f}", 11, mix(col, INK, .2), al * cl(zoom_in * 2 - .6 + rnd * 3), "Medium")
            cv.circ(x, y - 11, 1.6, fill=col, a=al * (1 - cl(zoom_in * 2 - .6)) )
        else:
            cv.circ(x, y, 2.6 + 1.2 * lit, fill=col, a=al)
    # mesh
    ma = fa * cl(scan * 1.3) * (1 - rnd) * .35 * (1 - swirl)
    if ma > .01:
        for i, j in MESH:
            (u0, v0), (u1, v1) = FACE[i], FACE[j]
            cv.line([(PH_X + u0 * sc, PH_Y + 30 + v0 * sc * 1.05), (PH_X + u1 * sc, PH_Y + 30 + v1 * sc * 1.05)], CY, .8, ma)
    # scan line
    if .8 < t < b(0, .3):
        yy = PH_Y + 30 + (scan * 2.3 - 1.15) * sc * 1.05
        cv.line([(PH_X - 150, yy), (PH_X + 150, yy)], CY2, 2, .5 * fa)
    # p1: cat pixels + small network
    if form > 0:
        gx, gy, cs = 700 - 8 * 22, 540 - 8 * 22, 22
        for k in range(256):
            r_, c_ = divmod(k, 16)
            i = k % len(FACE)
            ang = i * 2.39996 + t * .9; rad = 30 + 2.2 * math.sqrt(i) * 9
            sx, sy = 960 + rad * math.cos(ang), 540 + rad * math.sin(ang) * .8
            q = eio(cl(form * 1.4 - (k / 256) * .4))
            x = lerp(sx, gx + c_ * cs + cs / 2, q); y = lerp(sy, gy + r_ * cs + cs / 2, q)
            v = OURS[r_, c_]
            col = mix((16, 20, 36), (196, 204, 222), v)
            s2 = lerp(3, cs / 2 - .8, q)
            cv.rect(x - s2, y - s2, x + s2, y + s2, fill=col, a=q)
        # small network to the right
        na = eo(pr(t, b(1, .45), b(1, .62)))
        if na > 0:
            old = cv.cam
            cv.cam = Cam(1010 - (1340 - 960) / .5, 540, .5 * old.z)
            cv.cam.cx = 1010 - (1340 - 960) / (.5 * old.z)
            draw_net(cv, 0, a=na, inp=na, h1=na, h2=na, out=na, e1=na, e2=na, e3=na, x=X_OURS, fwd=lerp(0, 3.2, pr(t, b(1, .55), b(1, .8))))
            cv.cam = old
            ia = eo(pr(t, b(1, .7), b(1, .8)))
            ox = 1010 + (1460 - 1010) * .5 + 330 * 0 + (1340 - 1010)  # screen x of output ~ 1565
            ox = 1340 + (1460 - 1010) * .5
            cat_icon(cv, ox + 110, 470, 64, CY, ia, 3)
            notcat_icon(cv, ox + 110, 610, 60, AM, ia, 3)
            pul = .5 + .5 * math.sin(t * 5)
            cv.line([(ox + 30, 540), (ox + 70, 470)], CY, 2, ia * pul * .8)
            cv.line([(ox + 30, 540), (ox + 70, 610)], AM, 2, ia * (1 - pul) * .8)
            cv.text(ox + 110, 540, "?", 40, INK, ia * .9, "SemiBold")

# ---------- LATOON sting
def _letter_points():
    f = ImageFont.truetype(os.path.join(FONT_DIR, "Inter-Black.ttf"), 210)
    im = Image.new("L", (1400, 300), 0); d = ImageDraw.Draw(im)
    d.text((700, 150), "LATOON", font=f, fill=255, anchor="mm")
    a = np.asarray(im)
    ys, xs = np.nonzero(a[::6, ::6] > 128)
    pts = np.stack([xs * 6 - 700 + 960, ys * 6 - 150 + 520], 1).astype(float)
    return pts
LP = None
def scene_sting(cv, t, S, T):
    global LP
    if LP is None: LP = _letter_points()
    cam = Cam(960, 540, 1 + .04 * t); cv.cam = cam
    dust(cv, T, cam)
    D = S["dur"]
    conv = eio(pr(t, 0, 1.3)); dis = eio(pr(t, D - 1.0, D))
    rng = np.random.default_rng(2)
    for i, (x, y) in enumerate(LP[::2]):
        ang = rng.uniform(0, 6.283); rad = rng.uniform(300, 900)
        sx, sy = 960 + rad * math.cos(ang), 540 + rad * math.sin(ang)
        q = eio(cl(conv * 1.3 - (i % 37) / 37 * .3))
        px, py = lerp(sx, x, q), lerp(sy, y, q)
        px, py = lerp(px, 960 + (x - 960) * 3, dis), lerp(py, 540 + (y - 520) * 3, dis)
        cv.circ(px, py, 2.4, fill=mix(CY, LOGO, q), a=(.4 + .6 * q) * (1 - dis))
    wa = eo(pr(t, 1.0, 1.8)) * (1 - eio(pr(t, D - 1.1, D - .5)))
    cv.text(960, 520, "LATOON", 210, LOGO, wa, "Black")
    sw = pr(t, 1.3, 2.8)
    if 0 < sw < 1:
        cv.circ(960, 520, 120 + 900 * eo(sw), outline=LOGO, w=3, a=(1 - sw) * .6)
    cv.line([(760, 660), (760 + 400 * eo(pr(t, 1.4, 2.4)), 660)], LOGO, 3, wa * .8)

# ---------- pixels
GRID_C, GRID_S = (960, 540), 720
def scene_pixels(cv, t, S, T):
    b = Beat(S); D = S["dur"]
    cs = GRID_S / 16; gx0, gy0 = GRID_C[0] - GRID_S / 2, GRID_C[1] - GRID_S / 2
    zc = eio(pr(t, b(0, .45), b(0, .62))); zb = eio(pr(t, b(1, 0), b(1, .14)))
    tx, ty = gx0 + 5.5 * cs, gy0 + 6.5 * cs
    z = lerp(lerp(.92 + .08 * eo(pr(t, 0, b(0, .3))), 2.8, zc), 1.0, zb)
    cam = Cam(lerp(lerp(960, tx, zc), 960, zb), lerp(lerp(540, ty, zc), 540, zb), z)
    fly0 = b(1, .45); fly = pr(t, fly0, fly0 + 2.4); comp = eio(pr(t, fly0 + 3.0, fly0 + 5.0))
    zfly = eio(pr(t, fly0, fly0 + 1.6))
    if t > fly0:
        cam = Cam(960, 540, lerp(1.0, .48, zfly))
        cam.z = lerp(cam.z, 1.0, comp)
    cv.cam = cam
    dust(cv, T, cam)
    smooth_a = eo(pr(t, 0, 1.0)) * (1 - pr(t, b(0, .22), b(0, .4)))
    pix_a = eo(pr(t, b(0, .22), b(0, .4)))
    if t < fly0:
        if smooth_a > 0:
            cv.image(gray_img(HI), gx0, gy0, gx0 + GRID_S, gy0 + GRID_S, smooth_a, Image.BILINEAR)
        if pix_a > 0:
            cv.image(gray_img(OURS), gx0, gy0, gx0 + GRID_S, gy0 + GRID_S, pix_a, Image.NEAREST)
            ga = pix_a * .5
            for k in range(17):
                cv.line([(gx0 + k * cs, gy0), (gx0 + k * cs, gy0 + GRID_S)], (60, 70, 100), 1.2, ga)
                cv.line([(gx0, gy0 + k * cs), (gx0 + GRID_S, gy0 + k * cs)], (60, 70, 100), 1.2, ga)
        na = eo(pr(t, b(0, .55), b(0, .7))) * (1 - eo(pr(t, b(1, 0), b(1, .1))))
        if na > 0:
            for r_ in range(16):
                for c_ in range(16):
                    v = OURS[r_, c_]
                    if abs(c_ - 5.5) > 4 or abs(r_ - 6.5) > 3: continue
                    cv.text(gx0 + c_ * cs + cs / 2, gy0 + r_ * cs + cs / 2, f"{v:.2f}", 10.5, (20, 24, 40) if v > .55 else INK, na, "SemiBold")
        dim_a = eo(pr(t, b(1, .1), b(1, .25))) * (1 - eo(pr(t, fly0 - .4, fly0)))
        if dim_a > 0:
            cv.line([(gx0, gy0 - 30), (gx0 + GRID_S, gy0 - 30)], MUT, 2, dim_a)
            cv.line([(gx0 - 30, gy0), (gx0 - 30, gy0 + GRID_S)], MUT, 2, dim_a)
            cv.math(GRID_C[0], gy0 - 62, "16", 34, INK, dim_a)
            cv.math(gx0 - 70, GRID_C[1], "16", 34, INK, dim_a)
    else:
        # fly pixels into a ribbon (list), then compress to the input column
        for k in range(256):
            r_, c_ = divmod(k, 16)
            q = eio(cl(fly * 1.6 - (k / 256) * .6))
            x0, y0 = gx0 + c_ * cs + cs / 2, gy0 + r_ * cs + cs / 2
            x1, y1 = 960, 540 + (k - 127.5) * 8
            s0, s1 = cs / 2 - .5, 3.5
            x, y, s2 = lerp(x0, x1, q), lerp(y0, y1, q), lerp(s0, s1, q)
            hw = lerp(s0, 46, q)
            al = 1.0
            if comp > 0:
                sl = int(round(k * (N_SLOT - 1) / 255))
                keep = SLOT_PIX[sl] == k
                x, y = lerp(x1, INP_X, comp), lerp(y1, SLOT_Y[sl], comp)
                s2 = lerp(s1, 10 if keep else 3, comp); hw = lerp(46, 10 if keep else 3, comp)
                al = 1 if keep else 1 - comp
            v = OURS[r_, c_]
            col = mix((16, 20, 36), (196, 204, 222), v)
            if comp > .95 and SLOT_PIX[int(round(k * (N_SLOT - 1) / 255))] == k:
                cv.rrect(x - 10, y - 10, x + 10, y + 10, 3, fill=col, a=al, outline=DIM, w=1.2)
            else:
                cv.rect(x - hw, y - s2, x + hw, y + s2, fill=col, a=al)
        la = eo(pr(t, fly0 + 4.4, fly0 + 5.2))
        cv.math(INP_X - 48, SLOT_Y[0], "x_1", 26, MUT, la)
        cv.math(INP_X - 58, SLOT_Y[-1], "x_{256}", 26, MUT, la)
    # HUD: scale bar 0..1 and 16x16=256
    hud = Cam(); old = cv.cam; cv.cam = hud
    sa = eo(pr(t, b(0, .74), b(0, .84))) * (1 - eo(pr(t, b(1, 0), b(1, .1))))
    if sa > 0:
        cv.rrect(560, 950, 1360, 1030, 20, fill=(10, 13, 26), a=sa * .92, outline=DIM, w=1.5)
        for i in range(60):
            v = i / 59
            cv.rect(660 + i * 10, 980, 670 + i * 10, 1000, fill=mix((10, 13, 24), (196, 204, 222), v), a=sa)
        cv.math(630, 990, "0", 30, INK, sa); cv.math(1290, 990, "1", 30, INK, sa)
    ea = eo(pr(t, b(1, .22), b(1, .34))) * (1 - eo(pr(t, fly0 + 1.6, fly0 + 2.4)))
    if ea > 0:
        cv.math(960, 1000, r"16 \times 16 = 256", 46, INK, ea)
    cv.cam = old

# ---------- neuron
NX, NY, NR = 1180, 540, 34
J0 = None
def pick_j0():
    global J0
    if J0 is None:
        P = snap_np(0); z1 = (X_OURS @ P[0] + P[1])
        J0 = int(np.argmax(z1))
    return J0

def input_column(cv, a=1):
    for s_, k in enumerate(SLOT_PIX):
        v = X_OURS[k]
        cv.rrect(INP_X - 10, SLOT_Y[s_] - 10, INP_X + 10, SLOT_Y[s_] + 10, 3, fill=mix((16, 20, 36), (196, 204, 222), v), a=a, outline=DIM, w=1.2)
    cv.math(INP_X - 48, SLOT_Y[0], "x_1", 26, MUT, a)
    cv.math(INP_X - 58, SLOT_Y[-1], "x_{256}", 26, MUT, a)

def relu_plot(cv, ox, oy, a, probe=None, glow_bend=0.0, sc=110):
    cv.line([(ox - 2 * sc, oy), (ox + 1.8 * sc, oy)], MUT, 2, a)
    cv.line([(ox, oy + .4 * sc), (ox, oy - 1.9 * sc)], MUT, 2, a)
    cv.line([(ox - 1.9 * sc, oy), (ox, oy), (ox + 1.7 * sc, oy - 1.7 * sc)], CY, 5, a)
    cv.math(ox + 1.95 * sc, oy + 4, "z", 28, MUT, a, "lm")
    if glow_bend > 0:
        cv.glow(ox, oy, 70, AM, a * glow_bend)
        cv.circ(ox, oy, 14 + 8 * math.sin(glow_bend * 6), outline=AM, w=3, a=a * glow_bend)
    if probe is not None:
        z = probe; yv = max(0, z)
        px, py = ox + z * sc, oy - yv * sc
        cv.line([(px, oy), (px, py)], INK, 1.5, a * .5)
        cv.circ(px, oy, 6, fill=MUT, a=a)
        cv.circ(px, py, 9, fill=CY2, a=a)

def scene_neuron(cv, t, S, T):
    b = Beat(S); j0 = pick_j0()
    pan = eio(pr(t, b(2, 0), b(2, .12))) * (1 - eio(pr(t, b(2, .9), b(2, 1.0) + 1.2)))
    cam = Cam(960 + 260 * pan, 540, 1.0); cv.cam = cam
    dust(cv, T, cam)
    input_column(cv, 1)
    na = eo(pr(t, .3, 1.4))
    ea = pr(t, b(0, .1), b(0, .3))
    wm = eio(pr(t, b(0, .55), b(0, .7)))   # morph to weights
    P = snap_np(0); w = P[0][:, j0] * 9
    for s_, k in enumerate(SLOT_PIX):
        rev = cl(ea * 1.5 - s_ / N_SLOT * .5)
        if rev <= 0: continue
        c, st = wcol(w[k])
        col = mix(MUT, c, wm); wd = lerp(1.4, .8 + 3.2 * st, wm); al = lerp(.35, .15 + .6 * st, wm) * rev
        p0, p1 = (INP_X + 12, SLOT_Y[s_]), (NX - NR, NY)
        cv.line([p0, p1], col, wd, al)
        # votes travelling
        va = pr(t, b(0, .3), b(0, .38)) * (1 - pr(t, b(1, .9), b(1, 1)))
        if va > 0:
            ph = (t * .55 + s_ * .137) % 1
            cv.circ(lerp(p0[0], p1[0], ph), lerp(p0[1], p1[1], ph), lerp(3, 2 + 3 * st, wm), fill=mix(INK, c, wm), a=va * .9 * (1 - abs(ph - .5) * 1.2))
    # bias
    ba = eo(pr(t, b(1, .55), b(1, .65)))
    if ba > 0:
        bx, by = NX - 70, NY + 190
        cv.line([(bx, by), (NX - 10, NY + NR - 2)], VI, 2.5, ba * .8)
        cv.circ(bx, by, 16, fill=(30, 24, 60), outline=VI, w=2, a=ba)
        cv.math(bx, by, "b", 24, INK, ba)
        cv.text(bx, by + 44, "bias", 24, VI, ba, "Medium")
    # neuron
    cv.glow(NX, NY, 110, CY, na * (.6 + .2 * math.sin(t * 2)))
    cv.circ(NX, NY, NR * eback(na), fill=(18, 40, 70), outline=CY2, w=3, a=na)
    kink_in = eio(pr(t, b(2, .86), b(2, .96)))
    if kink_in > 0:
        k = NR * .5
        cv.line([(NX - k, NY + k * .35), (NX, NY + k * .35), (NX + k * .8, NY - k * .55)], INK, 2.4, kink_in)
    la = eo(pr(t, b(0, .05), b(0, .15))) * (1 - eo(pr(t, b(1, 0), b(1, .1))))
    cv.text(NX, NY - 72, "neuron", 30, CY2, la, "Medium")
    # weights label + highlighted w's
    wl = eo(pr(t, b(1, 0), b(1, .1))) * (1 - eo(pr(t, b(2, 0), b(2, .1))))
    if wl > 0:
        cv.text(870, 120, "weights", 30, CY2, wl, "Medium")
        for s_, lab in ((0, "w_1"), (N_SLOT - 1, "w_{256}")):
            mx, my = lerp(INP_X + 12, NX - NR, .42), lerp(SLOT_Y[s_], NY, .42)
            cv.math(mx, my - 22, lab, 24, INK, wl * eo(pr(t, b(1, .15), b(1, .25))))
    # equation HUD
    old = cv.cam; cv.cam = Cam()
    e1 = eo(pr(t, b(1, .22), b(1, .34))) * (1 - eo(pr(t, b(1, .78), b(1, .86))))
    e2 = eo(pr(t, b(1, .82), b(1, .92))) * (1 - eo(pr(t, b(2, .55), b(2, .62))))
    cv.math(960, 990, r"z = w_1x_1 + w_2x_2 + \cdots + w_{256}x_{256} + b", 40, INK, e1)
    cv.math(960, 990, r"z = \sum_{i} w_i\,x_i + b", 44, INK, e2)
    e3 = eo(pr(t, b(2, .62), b(2, .7))) * (1 - eo(pr(t, b(2, .86), b(2, .93))))
    cv.math(960, 990, r"W_2\,(W_1x) = (W_2W_1)\,x", 40, INK, e3)
    # weighted sum readout
    z1 = float(X_OURS @ P[0][:, j0] + P[1][j0])
    ra = eo(pr(t, b(1, .4), b(1, .5))) * (1 - eo(pr(t, b(2, .0), b(2, .08))))
    if ra > 0:
        cnt = z1 * eo(pr(t, b(1, .4), b(1, .6)))
        cv.cam = old
        cv.math(NX + 70, NY, r"z = %.2f" % cnt, 30, INK, ra, "lm")
        cv.cam = Cam()
    cv.cam = old
    # ReLU plot (world coords, right of neuron)
    pa = eo(pr(t, b(2, .05), b(2, .16))) * (1 - eio(pr(t, b(2, .9), b(2, 1.0))))
    if pa > 0:
        ox, oy = 1560, 640
        cv.line([(NX + NR, NY), (ox - 240, NY)], MUT, 2, pa * .5)
        probe = 1.6 * math.sin((t - b(2, .1)) * 1.1)
        relu_plot(cv, ox, oy, pa, probe=probe, glow_bend=eo(pr(t, b(2, .42), b(2, .5))) * (1 - eo(pr(t, b(2, .8), b(2, .88)))))
        cv.text(ox, oy - 260, "ReLU", 34, CY2, pa, "SemiBold")
        cv.math(ox, oy + 90, r"\max(0,\ z)", 34, INK, pa)
        cv.text(ox, oy + 150, "nonlinearity", 26, AM2, pa * eo(pr(t, b(2, .45), b(2, .55))), "Medium")
    # kink flying into the neuron
    fk = pr(t, b(2, .8), b(2, .9))
    if 0 < fk < 1:
        q = eio(fk); x = lerp(1560, NX, q); y = lerp(640, NY, q) - 120 * math.sin(q * math.pi)
        k = lerp(60, NR * .5, q)
        cv.line([(x - k, y + k * .35), (x, y + k * .35), (x + k * .8, y - k * .55)], AM2, 4, 1)
        cv.glow(x, y, 50, AM, .8)

# ---------- layers
def scene_layers(cv, t, S, T):
    b = Beat(S); j0 = pick_j0()
    zo = eio(pr(t, b(1, .74), b(1, .86))); zi = eio(pr(t, S["dur"] - 2.4, S["dur"] - .4))
    z = lerp(1.0, .07, zo); z = lerp(z, 1.0, zi)
    cam = Cam(960, 540, z); cv.cam = cam
    dust(cv, T, cam)
    m = eio(pr(t, .2, 1.8))
    h1 = pr(t, b(0, .15), b(0, .35)); e1 = pr(t, b(0, .2), b(0, .45))
    h2 = pr(t, b(0, .55), b(0, .7)); e2 = pr(t, b(0, .58), b(0, .78))
    out = pr(t, b(1, 0), b(1, .1)); e3 = pr(t, b(1, 0), b(1, .12))
    fw = None
    if b(0, .82) < t < b(0, .82) + 3: fw = (t - b(0, .82)) * 1.2
    if m < 1:
        # morph the single neuron to its slot in layer 1
        x, y = lerp(NX, H1_X, m), lerp(NY, H1_Y[j0], m)
        r = lerp(NR, 13, m)
        P = snap_np(0); w = P[0][:, j0] * 9
        input_column(cv, 1)
        for s_, k in enumerate(SLOT_PIX):
            c, st = wcol(w[k])
            cv.line([(INP_X + 12, SLOT_Y[s_]), (x - r, y)], c, .8 + 3.2 * st * (1 - m * .5), .15 + .6 * st * (1 - m * .5))
        cv.glow(x, y, 110 * (1 - m) + 30, CY, .6)
        cv.circ(x, y, r, fill=(18, 40, 70), outline=CY2, w=3)
        k = r * .5
        cv.line([(x - k, y + k * .35), (x, y + k * .35), (x + k * .8, y - k * .55)], INK, 2.4, 1)
    else:
        draw_net(cv, 0, 1, inp=1, h1=max(h1, .0001), h2=h2, out=out, e1=max(e1, .0001), e2=e2, e3=e3, fwd=fw, kink=1, hl_h1=j0 if h1 < 1 else None)
        # always show j0 node
        if h1 < 1:
            cv.circ(H1_X, H1_Y[j0], 13, fill=(18, 40, 70), outline=CY2, w=3)
        cv.math(INP_X - 48, SLOT_Y[0], "x_1", 26, MUT, 1)
        cv.math(INP_X - 58, SLOT_Y[-1], "x_{256}", 26, MUT, 1)
    la = eo(pr(t, b(0, .42), b(0, .52))) * (1 - eo(pr(t, b(1, .7), b(1, .76))))
    cv.text(H1_X, H1_Y[-1] + 62, "layer", 26, CY2, la, "Medium")
    cv.text(H2_X, H1_Y[-1] + 62, "layer", 26, CY2, la * eo(pr(t, b(0, .7), b(0, .8))), "Medium")
    # output meter + icons
    oa = eo(pr(t, b(1, .08), b(1, .2)))
    if oa > 0:
        v = .5 + .0 * math.sin(t)
        cv.math(OUT_X + 60, OUT_Y + 70, "0", 22, MUT, oa)
        cv.math(OUT_X + 60, OUT_Y - 70, "1", 22, MUT, oa)
        cv.line([(OUT_X + 40, OUT_Y + 70), (OUT_X + 40, OUT_Y - 70)], DIM, 6, oa)
        cv.line([(OUT_X + 40, OUT_Y + 70), (OUT_X + 40, OUT_Y + 70 - 140 * (.5 + .45 * math.sin(t * 1.7)))], CY, 6, oa)
        cat_icon(cv, OUT_X + 150, OUT_Y - 60, 70, CY, oa, 3)
        notcat_icon(cv, OUT_X + 150, OUT_Y + 70, 58, AM, oa, 3)
    # weights counter
    ca = eo(pr(t, b(1, .5), b(1, .58))) * (1 - eo(pr(t, b(1, .74), b(1, .8))))
    if ca > 0:
        old = cv.cam; cv.cam = Cam()
        n = int(4232 * eo(pr(t, b(1, .5), b(1, .66))))
        cv.text(960, 70, f"{n:,}".replace(",", " "), 64, INK, ca, "SemiBold")
        cv.text(960, 128, "weights", 26, CY2, ca, "Medium")
        cv.cam = old
    # zoom-out field of many networks
    fa = cl(zo * 1.4) * (1 - zi)
    if fa > 0.01:
        rng = np.random.default_rng(9)
        for i in range(700):
            gx, gy = rng.uniform(-9000, 11000), rng.uniform(-6500, 7500)
            if abs(gx - 960) < 900 and abs(gy - 540) < 600: continue
            for kk in range(3):
                cv.circ(gx + kk * 160, gy + (kk - 1) * 40, 26, fill=mix(CY, VI, (i % 7) / 7), a=fa * .5)
        old = cv.cam; cv.cam = Cam()
        cv.math(960, 980, r"10^{6}\,+", 50, INK, fa * eo(pr(t, b(1, .84), b(1, .92))))
        cv.cam = old
