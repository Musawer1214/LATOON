from common import *
from scenes_b import small_grid, out_icons, vbar, ball, PATH, U0, V0
from scenes_a import relu_plot

G0 = grads(snap_np(0), X_OURS)
JD = int(np.argmin(G0["z1"]))   # a hidden neuron that is "off" for our cat

def labels_xs(cv, a=1):
    cv.math(INP_X - 48, SLOT_Y[0], "x_1", 26, MUT, a); cv.math(INP_X - 58, SLOT_Y[-1], "x_{256}", 26, MUT, a)

def chain_pts():
    return [(470, 540), (790, 540), (1110, 540), (1430, 540), (1720, 540)]

def scene_backprop(cv, t, S, T):
    b = Beat(S)
    # camera: zoom on a dead neuron during p3
    zd = eio(pr(t, b(3, .0), b(3, .15))) * (1 - eio(pr(t, b(3, .62), b(3, .76))))
    cam = Cam(lerp(960, H1_X + 120, zd), lerp(540, H1_Y[JD], zd), lerp(1, 2.3, zd)); cv.cam = cam
    dust(cv, T, cam)
    netA = (1 - eio(pr(t, b(1, 0), b(1, .08)))) + eio(pr(t, b(2, .84), b(2, .96)))
    netA = cl(netA) * (1 - eio(pr(t, b(4, 0), b(4, .08))))
    # backward waves
    bw = None
    if b(0, .66) < t < b(0, .66) + 3.2: bw = (t - b(0, .66)) * 1.1
    if b(2, .86) < t < b(3, 0): bw = (t - b(2, .86)) * 1.1
    if t > b(3, .72) and netA > 0: bw = ((t - b(3, .72)) * .9) % 3.6
    seq = b(0, .18) < t < b(0, .62)
    if netA > 0:
        draw_net(cv, 0, netA * (.55 if seq else 1), x=X_OURS, kink=1, grads_=G0, bwd=bw,
                 dead=eio(pr(t, b(3, .4), b(3, .55))) * (0 if t < b(3, 0) else 1))
        labels_xs(cv, netA); vbar(cv, float(forward(snap_np(0), X_OURS[None])[-1][0, 0]), netA)
    # one weight at a time
    if seq and netA > 0:
        n = int((t - b(0, .18)) * 5)
        P = snap_np(0)
        for m in range(max(0, n - 6), n + 1):
            j, s_ = (m * 7) % 16, (m * 5) % N_SLOT
            aa = 1 - (n - m) / 7
            cv.line([(INP_X + 12, SLOT_Y[s_]), (H1_X - 13, H1_Y[j])], AM2, 3.5, aa)
        old = cv.cam; cv.cam = Cam()
        ca = win(t, b(0, .18), b(0, .64), .4, .4)
        cv.math(960, 80, r"%d\ /\ 4232" % (n + 1), 48, INK, ca)
        cx, cy = 1160, 80
        cv.circ(cx, cy, 24, outline=MUT, w=3, a=ca)
        ang = t * 6
        cv.line([(cx, cy), (cx + 16 * math.cos(ang), cy + 16 * math.sin(ang))], AM2, 3, ca)
        cv.cam = old
    hud = Cam(); old = cv.cam; cv.cam = hud
    la = win(t, b(0, .68), b(1, .02), .6, .5)
    cv.text(960, 84, "backpropagation", 46, AM2, la, "SemiBold")
    cv.cam = old
    # ---- p1 football
    fa = eo(pr(t, b(1, .02), b(1, .1))) * (1 - eio(pr(t, b(2, 0), b(2, .1))))
    morph = eio(pr(t, b(2, 0), b(2, .12)))
    chainA = cl(eo(pr(t, b(2, 0), b(2, .1)))) * (1 - eio(pr(t, b(2, .82), b(2, .92))))
    pl = [(500, 720), (820, 400), (1160, 660), (1460, 430)]
    goal = (1730, 540)
    if fa > 0:
        cv.rrect(220, 200, 1780, 880, 30, outline=(40, 70, 70), w=2, a=fa * .8)
        cv.line([(1000, 200), (1000, 880)], (40, 70, 70), 2, fa * .8)
        cv.circ(1000, 540, 110, outline=(40, 70, 70), w=2, a=fa * .8)
        cv.line([(1780, 470), (1730, 470), (1730, 610), (1780, 610)], INK, 4, fa)
    if fa > 0 or chainA > 0:
        cp = chain_pts()
        for k in range(4):
            x = lerp(pl[k][0], cp[k][0], morph); y = lerp(pl[k][1], cp[k][1], morph)
            blame = [.35, .5, .7, 1.0][k]
            bt = b(1, .5 + (3 - k) * .1)
            ba = eo(pr(t, bt + .3, bt + .9)) * (1 - morph)
            cv.glow(x, y, 70 * blame + 20, AM, ba)
            cv.circ(x, y, 22 + 12 * blame * ba, outline=AM, w=3, a=ba * fa)
            cv.circ(x, y, 18, fill=mix((30, 60, 80), CY, .5), outline=CY2, w=2.5, a=max(fa, chainA))
        # ball passes
        if fa > 0 and morph < 1:
            segs = [(pl[0], pl[1], .08), (pl[1], pl[2], .16), (pl[2], pl[3], .24), (pl[3], (1765, 395), .32)]
            bx, by = pl[0]
            for (p0, p1, f0) in segs:
                q = eio(pr(t, b(1, f0), b(1, f0 + .08)))
                if q > 0: bx, by = lerp(p0[0], p1[0], q), lerp(p0[1], p1[1], q)
                if q > 0 and q < 1: cv.line([p0, (bx, by)], INK, 2, fa * .4)
            cv.circ(bx, by, 9, fill=INK, a=fa)
            xa = eo(pr(t, b(1, .42), b(1, .48)))
            if xa > 0:
                cx, cy = 1765, 395
                cv.line([(cx - 22, cy - 22), (cx + 22, cy + 22)], RD, 6, xa * fa)
                cv.line([(cx - 22, cy + 22), (cx + 22, cy - 22)], RD, 6, xa * fa)
            # blame arrows backward
            chain = [(1765, 395)] + pl[::-1]
            for k in range(4):
                bt = b(1, .5 + k * .1)
                q = eio(pr(t, bt, bt + .7))
                if q <= 0: continue
                p0, p1 = chain[k], chain[k + 1]
                cv.arrow(p0[0], p0[1], lerp(p0[0], p1[0], q * .88), lerp(p0[1], p1[1], q * .88), AM, 4, fa * .9, 18)
    # ---- p2 chain with local derivatives
    if chainA > 0:
        cp = chain_pts()
        labs = ["x", "h_1", "h_2", r"\hat{y}", "L"]
        cv.circ(cp[4][0], cp[4][1], 30, fill=(60, 34, 14), outline=AM, w=3, a=chainA)
        for k in range(5):
            cv.math(cp[k][0], cp[k][1] + 62, labs[k], 34, INK, chainA)
        facs = [r"\frac{\partial h_1}{\partial w}", r"\frac{\partial h_2}{\partial h_1}", r"\frac{\partial \hat{y}}{\partial h_2}", r"\frac{\partial L}{\partial \hat{y}}"]
        for k in range(4):
            cv.line([(cp[k][0] + 24, cp[k][1]), (cp[k + 1][0] - 24, cp[k + 1][1])], MUT, 2.5, chainA * .7)
            ft = b(2, .18 + (3 - k) * .1)
            q = eio(pr(t, ft, ft + .5))
            if q > 0:
                x0, x1 = cp[k + 1][0] - 24, cp[k][0] + 24
                cv.line([(x0, 540), (lerp(x0, x1, q), 540)], AM, 5, chainA)
                cv.glow(lerp(x0, x1, q), 540, 40, AM, chainA * (1 - q * .5))
                cv.math((cp[k][0] + cp[k + 1][0]) / 2, 470, facs[k], 40, AM2, chainA * eo(pr(t, ft + .3, ft + .7)))
        old = cv.cam; cv.cam = Cam()
        ea = eo(pr(t, b(2, .6), b(2, .68))) * chainA
        cv.math(960, 820, r"\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}}\cdot\frac{\partial \hat{y}}{\partial h_2}\cdot\frac{\partial h_2}{\partial h_1}\cdot\frac{\partial h_1}{\partial w}", 46, INK, ea)
        cv.text(960, 930, "chain rule", 32, AM2, ea * eo(pr(t, b(2, .7), b(2, .78))), "Medium")
        cv.cam = old
    # ---- p3 dead ReLU close-up
    ra = win(t, b(3, .08), b(3, .66), .6, .6)
    if ra > 0:
        ox, oy = H1_X + 150, H1_Y[JD] + 40
        cv.rrect(ox - 95, oy - 95, ox + 95, oy + 40, 14, fill=(10, 13, 26), a=ra * .9, outline=DIM, w=1)
        relu_plot(cv, ox + 10, oy + 10, ra, probe=-1.2, sc=42)
        cv.line([(ox - 75, oy + 10), (ox - 5, oy + 10)], AM, 4, ra * (.6 + .4 * math.sin(t * 5)))
        cv.math(ox, oy + 80, r"\frac{\partial a}{\partial z} = 0", 22, AM2, ra)
        # pulse that stops at the dead node
        q = pr(t, b(3, .3), b(3, .5))
        if 0 < q:
            x = lerp(H2_X - 16, H1_X + 16, eio(q)); y = lerp(H2_Y[3], H1_Y[JD], eio(q))
            cv.circ(x, y, 7, fill=mix(AM, MUT, q), a=ra * (1 - pr(t, b(3, .52), b(3, .62))))
    # ---- p4 speed + history
    sa = eo(pr(t, b(4, .02), b(4, .1)))
    if sa > 0:
        old = cv.cam; cv.cam = Cam()
        L1 = 280 * eo(pr(t, b(4, .05), b(4, .15)))
        L2 = 600 * eo(pr(t, b(4, .12), b(4, .24)))
        L3 = 1300 * eio(pr(t, b(4, .25), b(4, .42)))
        up = eio(pr(t, b(4, .48), b(4, .58))) * 120
        y1, y2, y3 = 300 - up, 420 - up, 540 - up
        cv.text(300, y1, "forward pass", 26, CY2, sa, "Medium", "rm")
        cv.rrect(340, y1 - 18, 340 + L1, y1 + 18, 8, fill=CY, a=sa * .85)
        cv.text(300, y2, "backward pass", 26, AM2, sa, "Medium", "rm")
        cv.rrect(340, y2 - 18, 340 + L2, y2 + 18, 8, fill=AM, a=sa * .85)
        cv.math(360 + L2 + 50, y2, r"\approx 2\!-\!3\times", 32, INK, sa * eo(pr(t, b(4, .2), b(4, .28))), "lm")
        for k in range(int(L3 / 16)):
            cv.rect(340 + k * 16, y3 - 14, 340 + k * 16 + 11, y3 + 14, fill=MUT, a=sa * .5)
        cv.math(300, y3, r"4232\times", 32, MUT, sa * eo(pr(t, b(4, .3), b(4, .38))), "rm")
        ta = eo(pr(t, b(4, .5), b(4, .6)))
        if ta > 0:
            yl = 760
            cv.line([(260, yl), (260 + 1400 * eio(pr(t, b(4, .5), b(4, .66))), yl)], MUT, 2.5, ta)
            for (x, yr, nm, t0) in ((640, "1970", "Linnainmaa", .56), (1260, "1986", "Rumelhart · Hinton · Williams", .76)):
                q = eo(pr(t, b(4, t0), b(4, t0 + .08)))
                if q <= 0: continue
                cv.circ(x, yl, 10, fill=AM2, a=q)
                cv.rrect(x - 26, yl - 120, x + 26, yl - 52, 4, outline=INK, w=2, a=q * .8)
                for k in range(4): cv.line([(x - 16, yl - 106 + k * 13), (x + 16, yl - 106 + k * 13)], MUT, 2, q * .7)
                chip(cv, x, yl + 60, yr, nm, q)
        cv.cam = old

# ---------- SGD
def _sgd_path(n=120, lr=.03, seed=3):
    rng = np.random.default_rng(seed); u, v = U0, V0; P = [(u, v)]
    for _ in range(n):
        gu, gv = Lgrad(u, v); u -= lr * (gu + rng.normal(0, .9)); v -= lr * (gv + rng.normal(0, .9)); P.append((u, v))
    return P
SGDP = _sgd_path()
GDP = gd_full = None
def _gd(n=120, lr=.03):
    u, v = U0, V0; P = [(u, v)]
    for _ in range(n):
        gu, gv = Lgrad(u, v); u -= lr * gu; v -= lr * gv; P.append((u, v))
    return P
GDP = _gd()
MAPZ = None
def mxy(u, v): return 960 + u * 520, 540 - v * 420

def scene_sgd(cv, t, S, T):
    global MAPZ
    b = Beat(S)
    cam = Cam(960, 540, 1.0 + .03 * math.sin(t * .2)); cv.cam = cam
    dust(cv, T, cam)
    wallA = eo(pr(t, 0, 1.2)) * (1 - eio(pr(t, b(1, 0), b(1, .08))))
    cols, rows, sz, gap = 20, 11, 62, 11
    x0 = 960 - (cols * (sz + gap) - gap) / 2; y0 = 540 - (rows * (sz + gap) - gap) / 2
    rngs = [np.random.default_rng(5), np.random.default_rng(6)]
    pick1 = set(rngs[0].choice(cols * rows, 32, replace=False).tolist())
    pick2 = set(rngs[1].choice(cols * rows, 32, replace=False).tolist())
    fly = eio(pr(t, b(0, .62), b(0, .76)))
    back = eio(pr(t, b(0, .84), b(0, .9)))
    if wallA > 0:
        for k in range(cols * rows):
            r_, c_ = divmod(k, cols)
            q = eo(cl(wallA * 1.5 - (r_ + c_) / (rows + cols) * .5))
            x, y = x0 + c_ * (sz + gap), y0 + r_ * (sz + gap)
            img = THUMBS[k % 64] if (k // 64) % 2 == 0 else THUMBS[k % 64][:, ::-1]
            sel1 = k in pick1; sel2 = k in pick2
            hl = eo(pr(t, b(0, .45), b(0, .52))) * (1 - back) if sel1 else 0
            if sel1 and fly > 0 and back < 1:
                i = sorted(pick1).index(k); tx, ty = 1690 + (i % 4) * 8, 360 + (i // 4) * 40
                x, y = lerp(x, tx, fly), lerp(y, ty, fly)
                q = q * (1 - back)
            dimw = 1 - .6 * fly * (1 - back) if not sel1 else 1
            small_grid(cv, x, y, sz, q * dimw, img)
            if hl > 0: cv.rect(x - 3, y - 3, x + sz + 3, y + sz + 3, outline=CY, w=3, a=hl)
            hl2 = eo(pr(t, b(0, .9), b(0, .96))) if sel2 else 0
            if hl2 > 0: cv.rect(x - 3, y - 3, x + sz + 3, y + sz + 3, outline=CY, w=3, a=hl2 * wallA)
        old = cv.cam; cv.cam = Cam()
        ma = eo(pr(t, b(0, .46), b(0, .54))) * wallA
        cv.rrect(760, 18, 1160, 120, 22, fill=(8, 10, 20), a=ma * .85)
        cv.text(960, 50, "mini-batch", 34, CY2, ma, "SemiBold"); cv.math(960, 96, r"B = 32", 34, INK, ma)
        ga = eo(pr(t, b(0, .74), b(0, .8))) * (1 - back) * wallA
        if ga > 0:
            cv.rrect(1640, 300, 1860, 820, 20, fill=(8, 10, 20), a=ga * .7)
            cv.arrow(1750, 760, 1750, 680, AM, 5, ga, 20); cv.math(1750, 790, r"\nabla L", 30, AM2, ga)
        cv.cam = old
    # p1: map
    ma = eo(pr(t, b(1, 0), b(1, .1)))
    if ma > 0:
        if MAPZ is None:
            us = np.linspace(-1, 1, 64); vs = np.linspace(-1, 1, 44)
            MAPZ = (us, vs, Lf(us[None, :], vs[:, None]))
        us, vs, Z = MAPZ
        for i, v in enumerate(vs):
            for j, u in enumerate(us):
                z = Z[i, j]; tt = cl(z / 1.2)
                c = mix(mix((40, 200, 230), VI, cl(tt * 1.6)), AM, cl(tt * 1.6 - .6))
                x, y = mxy(u, v)
                cv.circ(x, y, 2.2 + 2.2 * (1 - tt), fill=c, a=ma * (.25 + .35 * (1 - tt)))
        n = int(len(GDP) * eio(pr(t, b(1, .08), b(1, .6))))
        if n > 1:
            pts = [mxy(u, v) for u, v in GDP[:n]]
            for k in range(0, len(pts) - 1, 2): cv.line([pts[k], pts[k + 1]], INK, 2, ma * .5)
            pts = [mxy(u, v) for u, v in SGDP[:n]]
            cv.line(pts, AM2, 2.5, ma * .9)
            ball(cv, (pts[-1], 0), 10, ma)
        la = eo(pr(t, b(1, .34), b(1, .42)))
        cv.text(1560, 860, "SGD", 40, AM2, la * ma, "SemiBold")
        cv.math(1560, 915, r"w \leftarrow w - \eta\,\nabla L_{B}", 30, INK, la * ma)
        qa = eo(pr(t, b(1, .66), b(1, .74)))
        if qa > 0:
            x, y = mxy(*SGDP[min(n, len(SGDP)) - 1])
            cv.circ(x + 70, y - 70, 30 + 3 * math.sin(t * 4), outline=VI, w=2.5, a=qa * ma)
            cv.text(x + 70, y - 70, "?", 34, VI, qa * ma, "SemiBold")
