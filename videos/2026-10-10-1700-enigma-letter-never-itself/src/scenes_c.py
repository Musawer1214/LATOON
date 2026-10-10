from common import *
from scenes_a import magnifier

CT = "OHJYPDOMQNJCOSGAWHLEIHYSOPJSMNU"; CRIB = "KEINEBESONDERENEREIGNISSE"

def scene_crib(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "04", win(t, 1, S["dur"] - .5))
    def s_hut(cv, lt, al, d):
        fullphoto(cv, "hut8", lt / d, al, 1.0, 1.15, (.5, .55), (.42, .5), dark=.05)
    def s_turing(cv, lt, al, d):
        fullphoto(cv, "turing_office", lt / d, al, 1.05, 1.15, (.5, .5), (.55, .5), dark=.42)
        portrait(cv, "turing16", 960, 520, 400, 540, al * eo(pr(lt, .4, 1.2)), rot=-2)
        paperclip(cv, 840, 250, al * eo(pr(lt, .4, 1.2)))
    def s_field(cv, lt, al, d):
        z = lerp(1.6, .55, eio(pr(lt, 0, d)))
        cv.cam = Cam(960, 540, z)
        rng = np.random.default_rng(9)
        cols, rows = 30, 26
        for r in range(rows):
            for c in range(cols):
                x = 960 + (c - cols / 2 + .5) * 118; y = 540 + (r - rows / 2 + .5) * 70
                X, Y = cv.pt(x, y)
                if X < -80 or X > W + 80 or Y < -60 or Y > H + 60: continue
                k = r * cols + c
                lab = chr(65 + (k // 676) % 26) + chr(65 + (k // 26) % 26) + chr(65 + k % 26)
                hit = (k < lt * 40)
                cv.rrect(x - 50, y - 26, x + 50, y + 26, 6, fill=(220, 208, 186) if hit else SNOW, a=al, outline=RULE, w=1.5)
                cv.text(x, y, lab, 26, INK2 if hit else INK, al, "monob")
        cv.cam = Cam()
    def s_routine(cv, lt, al, d):
        sheets = [(560, 560, -4), (960, 520, 2), (1360, 570, -1)]
        texts = ["WETTERVORHERSAGE", "KEINEBESONDERENEREIGNISSE", "ANDIEGRUPPE"]
        for k, (x, y, r) in enumerate(sheets):
            ak = al * eo(pr(lt, k * .5, k * .5 + .6))
            message_sheet(cv, x, y, 420, 560, ak)
            rng = np.random.default_rng(40 + k)
            for row in range(7):
                yy = y - 170 + row * 56
                if row == 2 + k:
                    txt = "KEINEBESONDE" if k != 0 else "WETTERVORHER"
                    if k == 1: txt = "KEINEBESONDE"
                    if k == 2: txt = "KEINEBESONDE"
                    typed_row(cv, x - 175, yy, txt, 30, ak, OX if lt > 2.5 else INK, 29, font="monob")
                    if lt > 2.5:
                        f = eio(pr(lt, 2.5 + k * .3, 3.3 + k * .3))
                        cv.line([(x - 190, yy + 22), (x - 190 + 350 * f, yy + 22)], OX, 3, ak)
                else:
                    typed_row(cv, x - 175, yy, "".join(rng.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 12)), 30, ak * .8, INK, 29, font="monob")
    def s_cribstrip(cv, lt, al, d):
        sp = 52; x0 = 960 - sp * 15
        for i, ch in enumerate(CT):
            cv.rrect(x0 + i * sp - 22, 600, x0 + i * sp + 22, 660, 5, fill=SNOW, a=al, outline=RULE, w=1.5)
            cv.text(x0 + i * sp, 630, ch, 34, INK, al, "monob")
        # paper strip with the crib, floating with a question
        u = eo(pr(lt, .4, 1.4))
        y = lerp(300, 440, u)
        xs = x0 + 1.5 * sp + math.sin(lt * 1.3) * sp * 1.2
        cv.rect(xs - 34 + 8, y - 36 + 12, xs + sp * 24 + 34 + 8, y + 36 + 12, fill=(50, 36, 22), a=al * .14)
        cv.rect(xs - 34, y - 36, xs + sp * 24 + 34, y + 36, fill=(250, 238, 200), a=al)
        for i, ch in enumerate(CRIB): cv.text(xs + i * sp, y, ch, 34, OX, al, "monob")
        cv.text(xs + sp * 12, 540, "?", 54, MUT, al * (.5 + .5 * math.sin(lt * 3)), "Bold")
    def s_slide(cv, lt, al, d):
        sp = 52; x0 = 960 - sp * 15
        nP = len(CT) - len(CRIB) + 1
        seg = (d - 3.0) / nP
        k = min(nP - 1, int(max(0, lt - .6) / seg)); ph = (max(0, lt - .6) / seg) % 1 if lt - .6 < seg * nP else 1
        kf = k + (eio(pr(ph, 0, .3)) if k < nP - 1 and False else 0)
        posx = k * sp
        if lt - .6 < seg * nP and k > 0: posx = (k - 1 + eio(pr(ph, 0, .25))) * sp
        hits = [i for i in range(len(CRIB)) if CT[k + i] == CRIB[i]]
        show_hits = ph > .3 or lt - .6 >= seg * nP
        for i, ch in enumerate(CT):
            hit = show_hits and (i - k) in hits
            cv.rrect(x0 + i * sp - 22, 600, x0 + i * sp + 22, 660, 5, fill=OX3 if hit else SNOW, a=al, outline=OX if hit else RULE, w=2 if hit else 1.5)
            cv.text(x0 + i * sp, 630, ch, 34, OX if hit else INK, al, "monob")
        y = 520
        xs = x0 + posx
        cv.rect(xs - 26 + 8, y - 36 + 12, xs + sp * 24 + 26 + 8, y + 36 + 12, fill=(50, 36, 22), a=al * .14)
        cv.rect(xs - 26, y - 36, xs + sp * 24 + 26, y + 36, fill=(250, 238, 200), a=al)
        for i, ch in enumerate(CRIB):
            hit = show_hits and i in hits
            cv.text(xs + i * sp, y, ch, 34, OX if hit else INK, al, "monob")
            if hit:
                cv.line([(xs + i * sp, y + 40), (xs + i * sp, 592)], OX, 3, al)
                stamp(cv, xs + i * sp, y - 70, "\u00d7", 60, 0, al * eo(pr(ph, .3, .45)) if lt - .6 < seg * nP else al, OX, box=False)
        # tally of positions
        for j in range(nP):
            done_ = j < k or (j == k and show_hits)
            ok = j == 3
            x = 960 + (j - 3) * 110; yy = 800
            cv.rrect(x - 42, yy - 34, x + 42, yy + 34, 8, fill=SNOW if not done_ else (OX3 if not ok else (214, 226, 206)), a=al, outline=RULE if not done_ else (OX if not ok else GREEN), w=2)
            cv.text(x, yy, str(j + 1), 32, INK if not done_ else (OX if not ok else GREEN), al, "Bold")
            if done_ and not ok: cv.line([(x - 30, yy + 24), (x + 30, yy - 24)], OX, 3.5, al)
    t12, t13 = B(1), B(2)
    seq(cv, t, [(0, 5.8, s_hut), (5.8, B(0, .62), s_turing), (B(0, .62), t12 - .2, s_field),
                (t12 - .2, B(1, .72), s_routine), (B(1, .72), t13 - .2, s_cribstrip), (t13 - .2, S["dur"] + 1, s_slide)])

MENU_N = {"E": (760, 520), "S": (1100, 360), "P": (1100, 690), "N": (980, 220), "O": (1300, 180), "I": (560, 300), "H": (620, 120), "D": (420, 520), "K": (300, 760), "Y": (520, 820)}
MENU_E = [("E", "P", 2), ("E", "N", 7), ("E", "S", 25), ("S", "P", 23), ("N", "S", 21), ("N", "O", 4), ("I", "O", 22), ("I", "H", 19), ("N", "H", 15), ("I", "D", 3), ("D", "S", 11), ("E", "I", 18), ("K", "Y", 1)]
LOOP = [("E", "S", 25), ("S", "P", 23), ("E", "P", 2)]

def drum(cv, x, y, r, ang, ring_col, a=1):
    shadow_circ(cv, x, y, r, a, (r * .08, r * .14))
    cv.circ(x, y, r, fill=ring_col, a=a)
    cv.circ(x, y, r * .82, fill=(214, 206, 186), a=a)
    for k in range(26):
        an = ang + k * 2 * math.pi / 26
        cv.line([(x + r * .7 * math.cos(an), y + r * .7 * math.sin(an)), (x + r * .8 * math.cos(an), y + r * .8 * math.sin(an))], INK2, 1.4, a)
    an = ang
    cv.text(x + r * .55 * math.cos(an), y + r * .55 * math.sin(an), "A", r * .22, OX, a, "Bold")
    cv.circ(x, y, r * .2, fill=STEEL, a=a); cv.circ(x - r * .05, y - r * .05, r * .08, fill=STEEL3, a=a)
    cv.circ(x, y, r, outline=(30, 28, 26), w=2, a=a)

def scene_bombe(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "05", win(t, 1, S["dur"] - .5))
    def s_menu(cv, lt, al, d):
        sp = 44; x0 = 1380
        # crib + cipher pairs list on right as a paper card
        panel(cv, 1330, 160, 1840, 900, al, 4, (246, 240, 226))
        for i in range(16):
            ap = al * eo(pr(lt, .2 + i * .1, .6 + i * .1))
            y = 200 + i * 44
            cv.text(1390, y, f"{i + 1:02d}", 22, MUT, ap, "monob", "lm")
            cv.text(1480, y, CRIB[i], 30, INK, ap, "monob")
            cv.text(1540, y, "\u2194", 26, MUT, ap, "Bold")
            cv.text(1600, y, CT[3 + i], 30, OX, ap, "monob")
        u = pr(lt, 2.5, 9.0)
        for j, (a_, b_, s_) in enumerate(MENU_E):
            f = eio(pr(u, j / len(MENU_E), (j + 1.5) / len(MENU_E)))
            if f <= 0: continue
            p, q = MENU_N[a_], MENU_N[b_]
            inloop = (a_, b_, s_) in LOOP and lt > 10
            cv.line(partial([p, q], f), OX if inloop else INK2, 4.5 if inloop else 2.4, al)
            if f >= 1:
                mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
                cv.circ(mx, my, 20, fill=PAPER, a=al)
                cv.text(mx, my, str(s_), 20, OX if inloop else INK2, al, "Bold")
        for n, (x, y) in MENU_N.items():
            ap = al * eo(pr(lt, 2.0, 3.0))
            inl = n in "ESP" and lt > 10
            cv.circ(x + 4, y + 6, 36, fill=(50, 36, 22), a=ap * .15)
            cv.circ(x, y, 36, fill=SNOW if not inl else OX3, a=ap, outline=OX if inl else INK, w=2.5)
            cv.text(x, y, n, 34, OX if inl else INK, ap, "monob")
        # contradiction: wrong setting -> loop flashes and breaks
        if lt > 14.5:
            fl = (math.sin((lt - 14.5) * 9) > 0) and lt < 17
            if fl:
                p, q = MENU_N["S"], MENU_N["P"]
                stamp(cv, (p[0] + q[0]) / 2 + 60, (p[1] + q[1]) / 2, "\u00d7", 80, 0, al, OX, box=False)
    def s_wartime(cv, lt, al, d):
        fullphoto(cv, "bombe_wartime", lt / d, al, 1.0, 1.12, (.45, .5), (.55, .45))
    def s_welchman(cv, lt, al, d):
        fullphoto(cv, "welchman_desk", lt / d, al, 1.0, 1.1, (.5, .5), (.5, .45), dark=.35)
        panel(cv, 1120, 300, 1720, 760, al * eo(pr(lt, .6, 1.2)), 6, (246, 240, 226))
        ap = al * eo(pr(lt, 1.0, 1.6))
        for k, (a_, b_) in enumerate([("A", "N"), ("N", "A")]):
            y = 440 + k * 180
            cv.circ(1260, y, 46, fill=SNOW, a=ap, outline=INK, w=2.5); cv.text(1260, y, a_, 44, INK, ap, "monob")
            cv.circ(1580, y, 46, fill=SNOW, a=ap, outline=INK, w=2.5); cv.text(1580, y, b_, 44, INK, ap, "monob")
            f = eio(pr(lt, 1.6 + k * .8, 2.4 + k * .8))
            cv.arrow(1315, y, lerp(1315, 1525, f), y, OX, 4, ap, 18)
    def s_victory(cv, lt, al, d):
        fullphoto(cv, "bombe_peel2", lt / d, al, 1.0, 1.15, (.5, .5), (.5, .4), dark=.18)
        panel(cv, 620, 400, 1300, 680, al * eo(pr(lt, .5, 1.0)), 6, (246, 240, 226))
        cv.text(960, 500, "III \u00b7 1940", 70, INK, al * eo(pr(lt, .7, 1.3)), "Black")
        stamp(cv, 960, 610, "VICTORY", 48, -4, al * eo(pr(lt, 1.4, 1.8)), OX)
    def s_peel(cv, lt, al, d):
        fullphoto(cv, "bombe_peel", lt / d, al, 1.0, 1.16, (.4, .5), (.6, .5))
    def s_drums(cv, lt, al, d):
        cv.rrect(170, 150, 1750, 900, 20, fill=(48, 40, 34), a=al)
        cv.rrect(190, 170, 1730, 880, 14, fill=(66, 56, 48), a=al)
        stop = 6.0
        cols_ = [(150, 50, 46), (64, 76, 92), (152, 120, 60)]
        for r in range(3):
            for c in range(12):
                x = 280 + c * 124; y = 290 + r * 250
                spd = [3.0, .115, .0044][r] * 2 * math.pi
                tt = min(lt, stop) if lt > stop else lt
                ang = -math.pi / 2 + spd * tt + c * .4 + r
                if lt > stop: ang = -math.pi / 2 + (round((spd * stop + c * .4 + r) / (2 * math.pi / 26))) * 2 * math.pi / 26
                drum(cv, x, y, 52, ang, cols_[r], al)
            cv.text(1690, 290 + r * 250, ["", "", ""][r], 20, PAPER, al)
        if lt > stop:
            g = eo(pr(lt, stop, stop + .4))
            cv.rrect(1590, 200, 1720, 840, 10, fill=LAMP, a=al * g * .25, outline=LAMP2, w=3)
            if lt > stop + 2.0:
                panel(cv, 520, 380, 1400, 680, al * eo(pr(lt, stop + 2.0, stop + 2.5)), 6, (246, 240, 226))
                pl = "WETTERVORHERSAG"; cip = enigma(pl, "QMT")
                ap = al * eo(pr(lt, stop + 2.4, stop + 3.0))
                typed_row(cv, 960 - 14 * 25, 470, cip, 40, ap, INK2, 50, font="mono")
                typed_row(cv, 960 - 14 * 25, 580, pl, 44, ap, OX, 50, reveal=cl((lt - stop - 3.0) * 6, 0, 15), font="monob")
    t15, t16 = B(1), B(2)
    seq(cv, t, [(0, t15 - .3, s_menu), (t15 - .3, B(1, .32), s_wartime), (B(1, .32), B(1, .6), s_welchman),
                (B(1, .6), t16 - .3, s_victory), (t16 - .3, B(2, .82), s_drums), (B(2, .82), S["dur"] + 1, s_peel)])
