from common import *
from scenes_a import rotor_wiring
from common import _R

COLS = [("kb", 230), ("pb", 450), ("R", 760), ("M", 1030), ("L", 1300), ("UKW", 1600)]
TOP, BOT = 250, 830
def cy(i): return lerp(TOP, BOT, i / 25)

def slab(cv, x, a, w=84, c=BAKE2, hi=None, label_col=None, wiring=None):
    cv.rrect(x - w / 2 + 8, TOP - 40 + 12, x + w / 2 + 8, BOT + 40 + 12, 14, fill=(40, 30, 20), a=a * .14)
    cv.done()
    X0, Y0 = cv.pt(x - w / 2, TOP - 40); X1, Y1 = cv.pt(x + w / 2, BOT + 40)
    g = hgrad(int(X1 - X0), int(Y1 - Y0), [(0, (40, 38, 36)), (.35, (112, 108, 102)), (.6, (150, 146, 138)), (1, (46, 44, 40))])
    cv.im.paste(g, (int(X0), int(Y0)), Image.new("L", g.size, int(255 * a)))
    cv.rrect(x - w / 2, TOP - 40, x + w / 2, BOT + 40, 12, outline=(30, 28, 26), w=2, a=a)
    for i in range(26):
        cv.circ(x - w / 2, cy(i), 5, fill=BRASS2, a=a); cv.circ(x + w / 2, cy(i), 5, fill=BRASS2, a=a)
    if wiring:
        for i in range(26):
            j = ord(wiring[i]) - 65
            cv.line(bez((x + w / 2, cy(i)), (x, cy(i)), (x, cy(j)), (x - w / 2, cy(j)), 10), (200, 190, 168), 1.0, a * .35)

def signal_path(cv, a, f_fwd, f_back, key="A", pos="AAD"):
    st = enigma_path(key, pos)
    # stage x positions forward: kb -> pb(left) -> R -> M -> L -> UKW
    xs = [COLS[0][1] + 40, COLS[1][1], COLS[2][1], COLS[3][1], COLS[4][1], COLS[5][1] - 30]
    fwd = [(xs[0], cy(st[0])), (xs[1], cy(st[0]))]
    for k, xi in enumerate([2, 3, 4]):
        x = COLS[xi][1]
        fwd += bez((x - 35, cy(st[k])), (x, cy(st[k])), (x, cy(st[k + 1])), (x + 35, cy(st[k + 1])), 14)
    fwd += [(xs[5], cy(st[3]))]
    # reflector U-turn
    r0, r1 = cy(st[3]), cy(st[4])
    loop = bez((xs[5], r0), (xs[5] + 120, r0), (xs[5] + 120, r1), (xs[5], r1), 20)
    back = [(xs[5], cy(st[4]))]
    for k, xi in enumerate([4, 3, 2]):
        x = COLS[xi][1]
        back += bez((x + 35, cy(st[4 + k])), (x, cy(st[4 + k])), (x, cy(st[5 + k])), (x - 35, cy(st[5 + k])), 14)
    back += [(xs[1], cy(st[7])), (xs[0], cy(st[7]))]
    path1 = fwd + loop
    if f_fwd > 0:
        pp = partial(path1, f_fwd)
        cv.line([(x + 3, y + 4) for x, y in pp], (40, 30, 20), 7, a * .18)
        cv.line(pp, INK, 4.5, a)
        cv.circ(pp[-1][0], pp[-1][1], 9, fill=INK, a=a * (1 if f_fwd < 1 else 0))
    if f_back > 0:
        pp = partial(back, f_back)
        cv.line([(x + 3, y + 4) for x, y in pp], (40, 30, 20), 7, a * .18)
        cv.line(pp, OX, 4.5, a)
        if f_back < 1: cv.circ(pp[-1][0], pp[-1][1], 9, fill=OX, a=a)
    return st

def scene_mirror(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "02", win(t, 1, S["dur"] - .5))
    def s_photo(cv, lt, al, d):
        fullphoto(cv, "machine_milan", lt / d, al, 1.0, 1.25, (.5, .45), (.45, .42))
    def s_path(cv, lt, al, d, both=False):
        for (name, x), wr in zip(COLS[1:5], [None, _R[2], _R[1], _R[0]]): slab(cv, x, al * eo(pr(lt, .1, .7)), wiring=wr)
        # reflector: half-disc slab
        x = COLS[5][1]
        cv.rrect(x - 40, TOP - 40, x + 90, BOT + 40, 60, fill=STEEL, a=al)
        cv.rrect(x - 30, TOP - 30, x + 60, BOT + 30, 50, fill=STEEL2, a=al * .6)
        for i in range(26): cv.circ(x - 40, cy(i), 5, fill=BRASS2, a=al)
        # keyboard + lamp column on the left
        for i in range(26):
            cv.text(COLS[0][1] - 20, cy(i), chr(65 + i), 18, MUT, al, "SemiBold")
        f1 = eio(pr(lt, 1.0, 6.0)); f2 = eio(pr(lt, 6.0, 10.5))
        st = signal_path(cv, al, f1, f2, "A", "AAD")
        key_cap(cv, COLS[0][1] - 80, cy(st[0]), 30, "A", math.sin(min(1, lt / .6) * math.pi) if lt < .6 else 0, al)
        lamp(cv, COLS[0][1] - 80, cy(st[7]), 30, "G", eo(pr(lt, 10.2, 10.7)) * .95, al)
    def s_reverse(cv, lt, al, d):
        for (name, x), wr in zip(COLS[1:5], [None, _R[2], _R[1], _R[0]]): slab(cv, x, al, wiring=wr)
        x = COLS[5][1]
        cv.rrect(x - 40, TOP - 40, x + 90, BOT + 40, 60, fill=STEEL, a=al)
        cv.rrect(x - 30, TOP - 30, x + 60, BOT + 30, 50, fill=STEEL2, a=al * .6)
        for i in range(26): cv.text(COLS[0][1] - 20, cy(i), chr(65 + i), 18, MUT, al, "SemiBold")
        st = enigma_path("A", "AAD")
        # ghost of A->G path, then G->A drawn: same wires reversed
        signal_path(cv, al * .25, 1, 1, "A", "AAD")
        f1 = eio(pr(lt, .6, 4.0)); f2 = eio(pr(lt, 4.0, 7.0))
        signal_path(cv, al, f1, f2, "G", "AAD")
        key_cap(cv, COLS[0][1] - 80, cy(6), 30, "G", math.sin(min(1, lt / .6) * math.pi) if lt < .6 else 0, al)
        lamp(cv, COLS[0][1] - 80, cy(0), 30, "A", eo(pr(lt, 6.8, 7.3)) * .95, al)
    def s_pair(cv, lt, al, d):
        paste_card(cv, "machine_milan", 470, 470, 520, 520, al, rot=-2)
        paste_card(cv, "machine_open", 1450, 470, 460, 520, al * eo(pr(lt, .3, .9)), rot=2)
        plain = "WETTERBERICHT"; ci = enigma(plain)
        u = pr(lt, 1.0, 5.0)
        typed_row(cv, 250, 820, plain, 40, al, INK, 32, font="monob")
        typed_row(cv, 1240, 820, ci, 40, al * eo(pr(lt, 4.5, 5.0)), INK, 32, font="monob")
        typed_row(cv, 1240, 880, enigma(ci), 40, al * eo(pr(lt, 6.0, 6.6)), OX, 32, font="monob")
        typed_row(cv, 250, 880, ci, 40, al * eo(pr(lt, 1.5, 2.0)), INK2, 32, font="mono")
        # morse dots travelling
        for k in range(18):
            x = lerp(760, 1180, ((lt * .5 + k / 18) % 1))
            if 2.0 < lt < 5.5:
                if k % 3 == 0: cv.rrect(x - 12, 466, x + 12, 474, 4, fill=OX, a=al * .8)
                else: cv.circ(x, 470, 5, fill=OX, a=al * .8)
    def s_ring(cv, lt, al, d):
        cx_, cy_, R = 960, 520, 300
        pairs = {}
        for i, c in enumerate("YRUHQSLDPXNGOKMIEBFZCWVJAT"): pairs[i] = ord(c) - 65
        cv.circ(cx_ + 10, cy_ + 16, R + 60, fill=(40, 30, 20), a=al * .10)
        cv.circ(cx_, cy_, R + 60, fill=STEEL2, a=al); cv.circ(cx_, cy_, R + 46, fill=STEEL3, a=al * .7)
        cv.circ(cx_, cy_, R + 10, fill=(236, 230, 214), a=al)
        done = set()
        for i in range(26):
            j = pairs[i]
            if (j, i) in done: continue
            done.add((i, j))
            a1 = -math.pi / 2 + i * 2 * math.pi / 26; a2 = -math.pi / 2 + j * 2 * math.pi / 26
            p1 = (cx_ + R * .92 * math.cos(a1), cy_ + R * .92 * math.sin(a1)); p2 = (cx_ + R * .92 * math.cos(a2), cy_ + R * .92 * math.sin(a2))
            ap = eo(pr(lt, .3 + len(done) * .12, .8 + len(done) * .12))
            hi = (i == 0)
            pts = bez(p1, (lerp(p1[0], cx_, .55), lerp(p1[1], cy_, .55)), (lerp(p2[0], cx_, .55), lerp(p2[1], cy_, .55)), p2, 20)
            cv.line(pts, OX if hi else BRASS3, 4.5 if hi else 2, al * ap * (1 if hi else .7))
        for i in range(26):
            an = -math.pi / 2 + i * 2 * math.pi / 26
            x, y = cx_ + R * .92 * math.cos(an), cy_ + R * .92 * math.sin(an)
            cv.circ(x, y, 9, fill=OX if i == 0 else BRASS2, a=al)
            cv.text(cx_ + (R + 30) * math.cos(an), cy_ + (R + 30) * math.sin(an), chr(65 + i), 26, OX if i == 0 else INK, al, "Bold")
        # attempted return to A: a loop that is blocked
        u = pr(lt, 6.0, 8.0)
        if u > 0:
            an = -math.pi / 2; x, y = cx_ + R * .92 * math.cos(an), cy_ + R * .92 * math.sin(an)
            loop = [(x + 70 * math.sin(k / 30 * 2 * math.pi) , y + 60 - 60 * math.cos(k / 30 * 2 * math.pi)) for k in range(31)]
            dashed(cv, partial(loop, eo(u) * .85), OX, 3, al * .8, 10, 8)
            if u >= 1:
                stamp(cv, x, y + 70, "\u00d7", 70, 0, al * eo(pr(lt, 8.0, 8.3)), OX, box=False)
        if lt > 9.5:
            stamp(cv, 1530, 300, "A \u2260 A", 72, -8, al * eo(pr(lt, 9.5, 9.9)), OX)
    def s_leak(cv, lt, al, d):
        plain = "KEINEBESONDERENEREIGNISSE"[:20]; ci = enigma(plain, "BLQ")
        sp = 74; x0 = 960 - sp * 9.5
        for i in range(20):
            ap = al * eo(pr(lt, i * .06, i * .06 + .4))
            cv.rrect(x0 + i * sp - 30, 380, x0 + i * sp + 30, 450, 6, fill=SNOW, a=ap, outline=RULE, w=1.5)
            cv.text(x0 + i * sp, 415, plain[i], 40, INK2, ap, "monob")
            cv.rrect(x0 + i * sp - 30, 560, x0 + i * sp + 30, 630, 6, fill=SNOW, a=ap, outline=RULE, w=1.5)
            cv.text(x0 + i * sp, 595, ci[i], 40, INK, ap, "monob")
            cv.text(x0 + i * sp, 505, "\u2260", 34, OX, al * eo(pr(lt, 1.5 + i * .08, 1.9 + i * .08)), "Bold")
    t6, t7 = B(1), B(2)
    seq(cv, t, [(0, 4.6, s_photo), (4.6, t6 - .2, s_path), (t6 - .2, B(1, .45), s_reverse), (B(1, .45), t7 - .2, s_pair),
                (t7 - .2, B(2, .72), s_ring), (B(2, .72), S["dur"] + 1, s_leak)])

# ---------------- Poland
def folder(cv, cx, cy, w, h, a=1, rot=0):
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    cv.rrect(x0 + 12, y0 + 18, x1 + 12, y1 + 18, 10, fill=(50, 36, 22), a=a * .16)
    cv.rrect(x0 + 40, y0 - 40, x0 + 300, y0 + 20, 12, fill=(206, 176, 118), a=a)
    cv.rrect(x0, y0, x1, y1, 10, fill=(214, 186, 128), a=a)
    cv.rrect(x0 + 16, y0 + 16, x1 - 16, y1 - 16, 6, fill=(222, 196, 140), a=a * .6)
    cv.rrect(x0, y0, x1, y1, 10, outline=(170, 138, 82), w=2, a=a)

PERM = "FQHPLWOGBMVEXIKRJCTSUYAZDN"
def cycles(perm):
    seen = set(); out = []
    for i in range(26):
        if i in seen: continue
        c = []; j = i
        while j not in seen: seen.add(j); c.append(j); j = ord(perm[j]) - 65
        out.append(c)
    return out

def scene_poland(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "03", win(t, 1, S["dur"] - .5))
    def s_dossier(cv, lt, al, d):
        folder(cv, 960, 560, 1100, 700, al)
        portrait(cv, "rejewski", 760, 540, 380, 480, al * eo(pr(lt, .3, 1.0)), rot=-3)
        paperclip(cv, 700, 290, al)
        stamp(cv, 1250, 420, "XII \u00b7 1932", 60, -6, al * eo(pr(lt, 1.6, 2.0)), OX)
        # permutation sketch on a note
        panel(cv, 1050, 520, 1450, 800, al * eo(pr(lt, 2.4, 3.0)), 4, (246, 240, 226))
        cv.text(1250, 600, "P N P\u207b\u00b9", 50, INK, al * eo(pr(lt, 2.8, 3.4)), "math")
        cv.text(1250, 700, "S\u207b\u00b9 A S", 50, INK2, al * eo(pr(lt, 3.2, 3.8)), "math")
    def s_shuffle(cv, lt, al, d):
        cyc = cycles(PERM)
        u = eio(pr(lt, 3.5, 6.0))
        sp = 62; x0 = 960 - 12.5 * sp
        # positions in cycle layout
        cpos = {}; cx = 300
        rad = [max(46, len(c) * 15) for c in cyc]
        totw = sum(2 * r + 60 for r in rad); cx = 960 - totw / 2
        for c, r in zip(cyc, rad):
            cx += r + 30
            for k, i in enumerate(c):
                an = -math.pi / 2 + k * 2 * math.pi / len(c)
                cpos[i] = (cx + r * math.cos(an), 560 + r * math.sin(an))
            cx += r + 30
        for i in range(26):
            top = (x0 + i * sp, 330); j = ord(PERM[i]) - 65; bot = (x0 + j * sp, 760)
            ap = al * (1 - u)
            if ap > .01:
                cv.text(top[0], top[1], chr(65 + i), 34, INK, ap, "monob")
                cv.text(x0 + i * sp, 790, chr(65 + i), 34, INK2, ap, "monob")
                f = eio(pr(lt, .4 + i * .08, 1.4 + i * .08))
                cv.line(partial([(top[0], top[1] + 26), (bot[0], bot[1] - 2)], f), OX if i == 0 else BRASS3, 3 if i == 0 else 1.6, ap * .8)
        if u > 0:
            for c, r in zip(cyc, rad):
                for k, i in enumerate(c):
                    j = c[(k + 1) % len(c)]
                    p, q = cpos[i], cpos[j]
                    cv.arrow(lerp(p[0], q[0], .22), lerp(p[1], q[1], .22), lerp(p[0], q[0], .78), lerp(p[1], q[1], .78), OX2, 2.4, al * u, 10)
            for i in range(26):
                p = (lerp(x0 + i * sp, cpos[i][0], u), lerp(330, cpos[i][1], u))
                cv.circ(p[0], p[1], 24, fill=SNOW, a=al * u, outline=RULE, w=1.5)
                cv.text(p[0], p[1], chr(65 + i), 30, INK, al, "monob")
    def s_spy(cv, lt, al, d):
        # envelope + key-sheet pages sliding out
        ex, ey = 760, 600
        cv.rect(ex - 330 + 12, ey - 200 + 18, ex + 330 + 12, ey + 200 + 18, fill=(50, 36, 22), a=al * .16)
        u = eo(pr(lt, .6, 2.2))
        for k in range(2):
            px = ex + 60 + k * 40 + u * (420 + k * 160); py = ey - 40 - k * 30
            panel(cv, px - 220, py - 280, px + 220, py + 260, al, 2, (246, 241, 228))
            rng = np.random.default_rng(5 + k)
            for r in range(12):
                y = py - 240 + r * 40
                cv.text(px - 190, y, f"{30 - r:02d}", 20, INK, al, "monob", "lm")
                cv.text(px - 130, y, " ".join(rng.permutation(["I", "II", "III"])), 20, INK, al, "monob", "lm")
                cv.text(px - 10, y, " ".join("".join(rng.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 2, replace=False)) for _ in range(4)), 20, INK2, al, "mono", "lm")
            stamp(cv, px + 110, py + 200, "GEHEIM", 30, -10, al, OX)
        cv.rect(ex - 330, ey - 200, ex + 330, ey + 200, fill=(206, 180, 128), a=al)
        cv.poly([(ex - 330, ey - 200), (ex, ey + 20), (ex + 330, ey - 200)], (190, 162, 108), al)
        cv.rect(ex - 330, ey - 200, ex + 330, ey + 200, outline=(160, 130, 80), w=2, a=al)
        stamp(cv, ex - 120, ey + 110, "1931\u20131932", 40, -4, al * eo(pr(lt, .2, .6)), INK2)
    def s_solve(cv, lt, al, d):
        f = eio(pr(lt, 2.0, d - 1))
        cv.text(560, 300, "A = SHPNP\u207b\u00b9QPN\u207b\u00b9P\u207b\u00b9H\u207b\u00b9S\u207b\u00b9", 50, INK, al * eo(pr(lt, .2, 1.0)), "math")
        cv.line([(150, 360), (970, 360)], RULE, 2, al)
        for k in range(4):
            cv.text(560, 440 + k * 90, ["B = SHP\u00b2NP\u207b\u00b2 \u2026", "C = SHP\u00b3NP\u207b\u00b3 \u2026", "D = SHP\u2074NP\u207b\u2074 \u2026", "\u2026"][k], 42, INK2, al * eo(pr(lt, .8 + k * .4, 1.4 + k * .4)), "math")
        rotor_wiring(cv, 1420, 560, al * cl(f * 3), 0, 0, lt, .82, label=False)
        cv.done()
        # unsolved wires veil: cover lower part progressively
        stamp(cv, 1420, 140, "N", 60, 0, al * eo(pr(lt, d - 2.0, d - 1.5)), OX)
    def s_trio(cv, lt, al, d):
        for k, (nm, x, r) in enumerate([("rejewski", 520, -3), ("rozycki", 960, 2), ("zygalski", 1400, -2)]):
            ak = al * eo(pr(lt, .2 + k * .5, .8 + k * .5))
            portrait(cv, nm, x, 470 + 20 * (1 - ak), 330, 430, ak, rot=r)
            paperclip(cv, x - 120, 250, ak)
    def s_sheets(cv, lt, al, d):
        fullphoto(cv, "zyg_sheets", lt / d, al, 1.0, 1.2, (.5, .5), (.45, .4))
    def s_orders(cv, lt, al, d):
        import itertools
        rom = ["I", "II", "III", "IV", "V"]
        orders = list(itertools.permutations(range(5), 3))
        first6 = [o for o in orders if max(o) < 3]
        rest = [o for o in orders if max(o) >= 3]
        allo = first6 + rest
        u = pr(lt, 3.5, 8.0)
        for k, o in enumerate(allo):
            if k < 6:
                ap = eo(pr(lt, .3 + k * .15, .7 + k * .15))
                big = 1 - eio(pr(lt, 3.0, 3.8))
                gx = 960 + (k - 2.5) * lerp(150, 270, big); gy = lerp(260, 520, big)
            else:
                ap = eo(pr(lt, 3.6 + (k - 6) * .07, 4.0 + (k - 6) * .07))
                gx = None
            if gx is None or k >= 6 or True:
                col_ = k % 10; row = k // 10
                tx, ty = 330 + col_ * 140, 260 + row * 100
                if k < 6: x, y = lerp(gx, tx, eio(pr(lt, 3.0, 3.8))), lerp(gy, ty, eio(pr(lt, 3.0, 3.8)))
                else: x, y = tx, ty
            sc = 1.0 if k >= 6 else lerp(1.0, 1.7, 1 - eio(pr(lt, 3.0, 3.8)))
            w_, h_ = 116 * sc, 70 * sc
            new = any(v >= 3 for v in o)
            cv.rrect(x - w_ / 2, y - h_ / 2, x + w_ / 2, y + h_ / 2, 8, fill=SNOW if not new else (240, 226, 214), a=al * ap, outline=OX if new else RULE, w=2)
            cv.text(x, y, " ".join(rom[v] for v in o), 22 * sc, OX if new else INK, al * ap, "Bold")
        cv.text(1730, 520, "6", 80, INK2, al * eo(pr(lt, 1.2, 1.6)) * (1 - pr(lt, 3.2, 3.6)), "Black")
        cv.text(1730, 520, "60", 80, OX, al * eo(pr(lt, 6.5, 7.0)), "Black")
    def s_handover(cv, lt, al, d):
        u = eio(pr(lt, 2.0, 6.0))
        cv.line([(960, 260), (960, 860)], RULE, 2, al)
        dashed(cv, [(960, 260), (960, 860)], INK2, 2, al * .5, 10, 10)
        stamp(cv, 520, 260, "VII \u00b7 1939", 52, -5, al * eo(pr(lt, .3, .7)), OX)
        paste_card(cv, "machine_milan", lerp(520, 1400, u), 560, 400, 440, al, rot=lerp(-3, 3, u))
        for k in range(3):
            paste_card(cv, "zyg_sheets", lerp(380, 1250, eio(pr(lt, 2.5 + k * .3, 6.5 + k * .3))) + k * 30, 790 - k * 12, 220, 160, al * .95, rot=-4 + k * 3)
    t9, t10 = B(1), B(2)
    seq(cv, t, [(0, 8.4, s_dossier), (8.4, t9 - .3, s_shuffle), (t9 - .3, B(1, .3), s_spy), (B(1, .3), B(1, .62), s_solve),
                (B(1, .62), B(1, .86), s_trio), (B(1, .86), t10 - .2, s_sheets), (t10 - .2, B(2, .5), s_orders), (B(2, .5), S["dur"] + 1, s_handover)])
