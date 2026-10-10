from common import *
from scenes_a import input_column

def small_grid(cv, x0, y0, size, a=1, img=None):
    img = OURS if img is None else img
    cv.image(gray_img(img), x0, y0, x0 + size, y0 + size, a, Image.NEAREST)
    cv.rect(x0, y0, x0 + size, y0 + size, outline=DIM, w=1.5, a=a)

def out_icons(cv, a):
    cat_icon(cv, OUT_X + 150, OUT_Y - 60, 70, CY, a, 3)
    notcat_icon(cv, OUT_X + 150, OUT_Y + 70, 58, AM, a, 3)

def vbar(cv, v, a, col=CY):
    cv.line([(OUT_X + 40, OUT_Y + 70), (OUT_X + 40, OUT_Y - 70)], DIM, 6, a)
    cv.line([(OUT_X + 40, OUT_Y + 70), (OUT_X + 40, OUT_Y + 70 - 140 * cl(v))], col, 6, a)
    cv.math(OUT_X + 60, OUT_Y + 70, "0", 22, MUT, a)
    cv.math(OUT_X + 60, OUT_Y - 70, "1", 22, MUT, a)

Y0 = float(forward(snap_np(0), X_OURS[None])[-1][0, 0])

# ---------- random
def scene_random(cv, t, S, T):
    b = Beat(S)
    cam = Cam(960, 540, 1.0 + .03 * eo(pr(t, 0, S["dur"]))); cv.cam = cam
    dust(cv, T, cam)
    shuf = t < b(0, .3)
    fw = None
    if t > b(0, .5): fw = min(3.2, (t - b(0, .5)) * 1.4)
    draw_net(cv, 0, 1, x=X_OURS if t > b(0, .42) else False, fwd=fw, kink=1, rand_t=(int(abs(t) * 6) if shuf else None))
    input_column(cv, 0) if False else None
    cv.math(INP_X - 48, SLOT_Y[0], "x_1", 26, MUT, 1); cv.math(INP_X - 58, SLOT_Y[-1], "x_{256}", 26, MUT, 1)
    # shuffling cards
    ca = win(t, b(0, .02), b(0, .36), .5, .6)
    if ca > 0:
        rng = np.random.default_rng(int(t * 6))
        for k in range(5):
            ph = (t * 1.6 + k * .2) % 1
            x = 230 + (k - 2) * 40 + 70 * math.sin(ph * math.pi * 2) * (1 if k % 2 else -1)
            y = 260 - 22 * math.sin(ph * math.pi)
            cv.rrect(x - 34, y - 48, x + 34, y + 48, 8, fill=(20, 26, 48), outline=mix(DIM, INK, .3), w=1.5, a=ca)
            cv.text(x, y, f"{rng.normal(0, .5):+.2f}", 15, CY2 if k % 2 else AM2, ca, "SemiBold")
    # cat slides in
    ga = eo(pr(t, b(0, .33), b(0, .45)))
    if ga > 0:
        gx = lerp(-260, 150, ga)
        small_grid(cv, gx, 540 - 112, 224, ga)
        cv.arrow(gx + 240, 540, INP_X - 80, 540, MUT, 3, ga * .8, 16)
    # output reading
    v = Y0 * eo(pr(t, b(0, .68), b(0, .78))) + .5 * (1 - eo(pr(t, b(0, .68), b(0, .78)))) if t > b(0, .6) else .5
    wob = (1 - pr(t, b(0, .6), b(0, .78))) * .25 * math.sin(t * 9) if t > b(0, .6) else 0
    vbar(cv, v + wob, 1)
    out_icons(cv, 1)
    na = eo(pr(t, b(0, .74), b(0, .82)))
    cv.text(OUT_X, OUT_Y + 140, f"{Y0:.2f}", 46, INK, na, "SemiBold")
    coin = eo(pr(t, b(0, .86), b(0, .92)))
    if coin > 0:
        cx, cy = OUT_X, OUT_Y - 170
        wd = 40 * abs(math.cos(t * 7)); col = AM2 if math.cos(t * 7) > 0 else MUT
        cv.poly([(cx + wd * math.cos(a_), cy + 40 * math.sin(a_)) for a_ in np.linspace(0, 6.283, 40)], col, coin * .85)

# ---------- loss
YA, YB = 740, 340   # vertical number line 0..1 at x=LX
LX = 1640
def scene_loss(cv, t, S, T):
    b = Beat(S)
    pan = eio(pr(t, b(0, 0), b(0, .14)))
    p1 = eio(pr(t, b(1, 0), b(1, .1)))
    cam = Cam(lerp(960, 1300, pan), 540, lerp(1.0, 1.22, pan)); cv.cam = cam
    dust(cv, T, cam)
    na = 1 - p1
    if na > 0:
        draw_net(cv, 0, na * (1 - .72 * pan), x=X_OURS, kink=1)
        vbar(cv, Y0, na); out_icons(cv, na * (1 - pan))
        cv.text(OUT_X, OUT_Y + 140, f"{Y0:.2f}", 46, INK, na * (1 - pan), "SemiBold")
        la = na * eo(pr(t, b(0, .1), b(0, .2)))
        cv.line([(LX, YA), (LX, YB)], MUT, 2.5, la)
        for v_ in (0, 1): cv.math(LX - 34, lerp(YA, YB, v_), str(v_), 26, MUT, la)
        yp = lerp(YA, YB, Y0)
        cv.line([(OUT_X + 30, OUT_Y), (LX - 12, yp)], CY, 1.5, la * .5)
        cv.circ(LX, yp, 10, fill=CY, a=la); cv.math(LX + 26, yp, r"\hat{y} = %.2f" % Y0, 28, CY2, la, "lm")
        ta = na * eo(pr(t, b(0, .16), b(0, .26)))
        cv.circ(LX, YB, 10, fill=GR, a=ta); cv.math(LX + 26, YB, r"y = 1", 28, GR, ta, "lm")
        cat_icon(cv, LX + 150, YB, 54, GR, ta, 2.5)
        ga = na * eo(pr(t, b(0, .22), b(0, .32)))
        if ga > 0:
            cv.line([(LX, yp - 12), (LX, YB + 12)], AM, 7, ga * (.7 + .3 * math.sin(t * 4)))
        oa = na * eo(pr(t, b(0, .3), b(0, .4)))
        if oa > 0:
            ox, oy = 1720, 760
            cv.glow(ox, oy, 120, AM, oa * .8)
            cv.circ(ox, oy, 52 * eback(oa), fill=(60, 34, 14), outline=AM, w=3, a=oa)
            cv.text(ox, oy - 86, "loss", 30, AM2, oa, "Medium")
            va = eo(pr(t, b(0, .84), b(0, .92)))
            cv.text(ox, oy + 2, "0.73" if va > .5 else "?", 30, INK, oa, "SemiBold")
    hud = Cam(); old = cv.cam; cv.cam = hud
    e1 = eo(pr(t, b(0, .52), b(0, .6))) * (1 - p1)
    cv.math(960, 905, r"L = -\log\,\hat{y}", 46, INK, e1)
    cv.text(960, 975, "cross entropy", 30, AM2, e1 * eo(pr(t, b(0, .6), b(0, .68))), "Medium")
    e2 = eo(pr(t, b(0, .8), b(0, .88))) * (1 - p1)
    cv.math(960, 1040, r"-\log(0.48) \approx 0.73", 36, INK, e2)
    # p1: the -log curve
    pa = p1 * (1 - eio(pr(t, b(1, .52), b(1, .6))))
    if pa > 0:
        X0, Y0_, sx, sy = 560, 860, 800, 120
        cv.line([(X0, Y0_), (X0 + sx + 30, Y0_)], MUT, 2, pa); cv.line([(X0, Y0_), (X0, Y0_ - 5 * sy - 20)], MUT, 2, pa)
        cv.math(X0 + sx + 60, Y0_, r"\hat{y}", 30, MUT, pa); cv.math(X0 - 34, Y0_ - 5 * sy - 10, "L", 30, MUT, pa)
        for v_ in (0, 1): cv.math(X0 + v_ * sx, Y0_ + 30, str(v_), 24, MUT, pa)
        ps = np.linspace(.0067, 1, 120)
        cv.line([(X0 + p * sx, Y0_ - (-math.log(p)) * sy) for p in ps], AM, 4, pa)
        hi = eo(pr(t, b(1, .4), b(1, .46))) * (1 - eo(pr(t, b(1, .5), b(1, .56))))
        if hi > 0:
            cv.line([(X0 + p * sx, Y0_ - (-math.log(p)) * sy) for p in ps[:14]], AM2, 10, pa * hi * .6)
        q1 = eio(pr(t, b(1, .04), b(1, .16))); q2 = eio(pr(t, b(1, .22), b(1, .36)))
        p = lerp(lerp(.48, .99, q1), .01, q2)
        L = -math.log(p)
        x, y = X0 + p * sx, Y0_ - L * sy
        cv.glow(x, y, 50, CY, pa); cv.circ(x, y, 11, fill=CY2, a=pa)
        cv.line([(x, Y0_), (x, y)], CY, 1.5, pa * .5)
        cv.math(x + (30 if p < .6 else -30), y - 34, r"L \approx %.2f" % L, 30, INK, pa, "lm" if p < .6 else "rm")
    # averaging many pictures
    aa = eo(pr(t, b(1, .55), b(1, .62)))
    if aa > 0:
        mg = eio(pr(t, b(1, .7), b(1, .82)))
        Ls = [.73, .2, 1.4, .1, .9, .35, 2.1, .5]
        for k in range(8):
            x = 960 + (k - 3.5) * 170
            small_grid(cv, x - 60, 300, 120, aa * (1 - mg * .6), THUMBS[k + 3])
            bx = lerp(x, 960 + (k - 3.5) * 12, mg); h = Ls[k] * 110
            cv.rect(bx - (26 if mg < .9 else 5), 640 - h * (1 - mg) - .78 * 110 * mg, bx + (26 if mg < .9 else 5), 640, fill=AM, a=aa * (.8 - .4 * mg))
        if mg > .5:
            ab = eo((mg - .5) * 2)
            cv.rect(900, 640 - .79 * 110, 1020, 640, fill=AM, a=ab)
        cv.math(960, 760, r"L = \frac{1}{N}\sum_{i=1}^{N} \ell_i", 46, INK, aa * eo(pr(t, b(1, .66), b(1, .74))))
        da = eo(pr(t, b(1, .84), b(1, .9)))
        if da > 0:
            yy = 520 + 30 * eio((t * .8) % 1)
            cv.arrow(1080, yy - 60, 1080, yy + 40, GR, 5, da, 22)
    cv.cam = old

# ---------- landscape
U0, V0 = -.62, .72
def ball(cv, pos, r=13, a=1, col=AM2):
    (x, y), _ = pos
    cv.glow(x, y, r * 4.5, AM, a)
    cv.circ(x, y, r, fill=col, a=a, outline=INK, w=1.5)

def gd_path(n=60, lr=.06, u=U0, v=V0):
    P = [(u, v)]
    for _ in range(n):
        gu, gv = Lgrad(u, v); u -= lr * gu; v -= lr * gv; P.append((u, v))
    return P
PATH = gd_path(80)

def scene_landscape(cv, t, S, T):
    b = Beat(S)
    cam = Cam(); cv.cam = cam
    dust(cv, T, cam)
    yaw = .55 + .045 * t
    pj = Proj(yaw, .98, 3.9, 450, 960, 650)
    hs = eio(pr(t, b(0, .36), b(0, .62)))
    sa = eo(pr(t, b(0, .28), b(0, .38)))
    fogr = lerp(4.0, .55, eio(pr(t, b(1, .5), b(1, .75))))
    if sa > 0:
        surface(cv, pj, hs=max(hs, .001), a=sa, fog=(U0, V0, fogr) if t > b(1, .4) else None)
    # knobs
    ka = win(t, .3, b(1, .08), .8, .8)
    u = .8 * math.sin(t * .55) ; v = .8 * math.sin(t * .37 + 1)
    if ka > 0:
        for k, (x, val, lab) in enumerate(((700, u, "w_1"), (1220, v, "w_2"))):
            cv.circ(x, 190, 62, fill=(16, 20, 38), outline=mix(DIM, INK, .3), w=2.5, a=ka)
            ang = math.radians(-90 + val * 150)
            cv.line([(x, 190), (x + 48 * math.cos(ang), 190 + 48 * math.sin(ang))], CY2, 5, ka)
            for i in range(11):
                aa_ = math.radians(-90 - 150 + 30 * i)
                cv.line([(x + 70 * math.cos(aa_), 190 + 70 * math.sin(aa_)), (x + 78 * math.cos(aa_), 190 + 78 * math.sin(aa_))], MUT, 2, ka * .6)
            cv.math(x, 290, lab, 30, INK, ka)
        Lv = float(Lf(u, v))
        cv.math(960, 190, r"L = %.2f" % Lv, 44, AM2, ka)
        if sa > 0:
            pos = pj(u, v, float(Lf(u, v)) * max(hs, .001))
            ball(cv, pos, 9, ka * sa, CY2)
    # p1: the hiker ball
    ba = eo(pr(t, b(1, 0), b(1, .1)))
    if ba > 0:
        pos = pj(U0, V0, float(Lf(U0, V0)))
        ball(cv, pos, 13, ba)
    va = win(t, b(1, .28), b(1, .6), .6, .6)
    if va > 0:
        um, vm = PATH[-1]
        (x, y), _ = pj(um, vm, float(Lf(um, vm)))
        cv.circ(x, y, 22 + 6 * math.sin(t * 4), outline=CY, w=3, a=va)
        cv.glow(x, y, 80, CY, va * .7)
    # 4232 dimensions
    da = eo(pr(t, b(1, .55), b(1, .7)))
    if da > 0:
        (x, y), _ = pj(U0, V0, float(Lf(U0, V0)))
        rng = np.random.default_rng(4)
        for k in range(46):
            th = rng.uniform(0, 6.283); ln = rng.uniform(120, 340) * eo(pr(t, b(1, .55) + k * .02, b(1, .75) + k * .02))
            cv.line([(x, y), (x + ln * math.cos(th), y + ln * math.sin(th) * .8)], mix(VI, CY, k / 46), 1.5, da * .45)
        cv.math(960, 980, r"\mathbb{R}^{4232}", 54, INK, da * eo(pr(t, b(1, .7), b(1, .8))))

# ---------- gradient
def scene_gradient(cv, t, S, T):
    b = Beat(S)
    cam = Cam(); cv.cam = cam
    dust(cv, T, cam)
    yaw = .55 + .045 * (t + 28.9)
    lr_on = eio(pr(t, b(2, 0), b(2, .1)))
    zoom = eio(pr(t, 0, b(0, .3))) * (1 - eio(pr(t, b(1, .55), b(1, .8))))
    pj = Proj(yaw, .98, 3.9, 450 * (1 + .55 * zoom), 960, 650)
    # steps along path
    nsteps = 0
    st_times = [b(0, .5) + k * 1.1 for k in range(80)]
    for k, tk in enumerate(st_times):
        if t > tk: nsteps = k + 1
    nsteps = min(nsteps, len(PATH) - 1)
    frac = eio(pr(t, st_times[nsteps] if nsteps < len(st_times) else 1e9, (st_times[nsteps] if nsteps < len(st_times) else 1e9) + .5))
    if nsteps > 0:
        tk = st_times[nsteps - 1]; frac = eio(pr(t, tk, tk + .5))
        u0, v0 = PATH[nsteps - 1]; u1, v1 = PATH[nsteps]
        uc, vc = lerp(u0, u1, frac), lerp(v0, v1, frac)
    else:
        uc, vc = PATH[0]
    # recentre projection on the ball when zoomed
    (bx, by), _ = pj(uc, vc, float(Lf(uc, vc)))
    pj.cx += (960 - bx) * zoom; pj.cy += (600 - by) * zoom
    fogr = lerp(.55, 4.0, eio(pr(t, b(1, .55), b(1, .85))))
    sa = 1 - lr_on
    if sa > 0:
        surface(cv, pj, hs=1.0, a=sa, fog=(uc, vc, fogr))
        # trail
        tr = [pj(u, v, float(Lf(u, v)))[0] for (u, v) in PATH[:nsteps]] + [pj(uc, vc, float(Lf(uc, vc)))[0]]
        if len(tr) > 1: cv.line(tr, AM2, 3, sa * .8)
        for p in tr[:-1]: cv.circ(p[0], p[1], 4, fill=AM2, a=sa * .8)
        pos = pj(uc, vc, float(Lf(uc, vc)))
        ball(cv, pos, 13, sa)
        # downhill arrow
        ga = sa * eo(pr(t, b(0, .35), b(0, .45)))
        if ga > 0:
            gu, gv = Lgrad(uc, vc); n = math.hypot(gu, gv) + 1e-9
            du, dv = -gu / n * .22, -gv / n * .22
            p0 = pos[0]; p1, _ = pj(uc + du, vc + dv, float(Lf(uc + du, vc + dv)))
            cv.arrow(p0[0], p0[1], p1[0], p1[1], CY2, 5, ga, 22)
            cv.text(p1[0] + 20, p1[1] - 34, "gradient", 28, CY2, ga * win(t, b(1, 0), b(1, .9), .6, .6), "Medium", "lm")
    hud = Cam(); old = cv.cam; cv.cam = hud
    e1 = win(t, b(1, .1), b(1, .62), .6, .5) * sa
    cv.math(960, 985, r"\nabla L = \left(\frac{\partial L}{\partial w_1},\ \frac{\partial L}{\partial w_2},\ \ldots,\ \frac{\partial L}{\partial w_{4232}}\right)", 40, INK, e1)
    e2 = eo(pr(t, b(1, .64), b(1, .72))) * sa
    cv.math(960, 985, r"w \;\leftarrow\; w - \eta\, \nabla L", 50, INK, e2)
    # p2: learning rate panels
    if lr_on > 0:
        cv.text(960, 120, "learning rate", 34, CY2, lr_on, "Medium")
        cv.math(960, 175, r"\eta", 40, INK, lr_on)
        cfg = [(420, .05, b(2, .08)), (1500, 1.06, b(2, .3)), (960, .35, b(2, .62))]
        for (cx, eta, t0) in cfg:
            pa = lr_on * eo(pr(t, t0, t0 + .6))
            if pa <= 0: continue
            sx, sy, base = 190, 230, 760
            pts = [(cx + x * sx, base - x * x * sy) for x in np.linspace(-1.25, 1.25, 60)]
            cv.line(pts, mix(VI, CY, .4), 3, pa)
            cv.circ(cx, base, 6, fill=CY, a=pa * .7)
            n = int(max(0, (t - t0 - .4) / .5)); x = -1.0; xs = [x]
            for _ in range(min(n, 30)):
                x = x - eta * 2 * x; xs.append(x)
            for i in range(1, len(xs)):
                xa, xb = xs[i - 1], xs[i]
                if abs(xb) > 1.25: break
                cv.line([(cx + xa * sx, base - xa * xa * sy - 13), (cx + xb * sx, base - xb * xb * sy - 13)], AM2, 2, pa * .55)
            xl = xs[-1]
            if abs(xl) < 1.25:
                ball(cv, ((cx + xl * sx, base - xl * xl * sy - 13), 0), 12, pa)
            else:
                fly = (t - t0) * 80
                fly = max(0, (t - t0 - .4 - .5 * next(i for i, x_ in enumerate(xs) if abs(x_) > 1.25)) * 260)
                ball(cv, ((cx + math.copysign(1.25 * sx + fly * .5, xl), base - 1.56 * sy - 13 - fly), 0), 12, pa * cl(1 - fly / 400))
            cv.math(cx, base + 70, r"\eta = %.2f" % eta, 30, INK, pa)
            if eta == .35 and len(xs) > 6:
                from scenes_a import phone  # noqa
                ck = eo(pr(t, t0 + 3.5, t0 + 4.2))
                cv.line([(cx - 26, base + 128), (cx - 6, base + 148), (cx + 30, base + 108)], GR, 6, pa * ck)
    cv.cam = old
