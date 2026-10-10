from common import *

_rng = np.random.default_rng(1941)
NOL = "".join(chr(65 + i) for i in range(26) if chr(65 + i) != "L")
CIPHER_NOL = ["".join(_rng.choice(list(NOL), 5)) for _ in range(30)]
ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

def magnifier(cv, x, y, r, zoom=1.7, a=1.0):
    if a <= .01: return
    cv.done()
    R = int(r)
    box = (int(x - R / zoom), int(y - R / zoom), int(x + R / zoom), int(y + R / zoom))
    reg = cv.im.crop(box).resize((2 * R, 2 * R), Image.BICUBIC)
    m = Image.new("L", (2 * R, 2 * R), 0); ImageDraw.Draw(m).ellipse((0, 0, 2 * R - 1, 2 * R - 1), fill=int(255 * a))
    # handle + shadow
    ang = math.radians(45)
    hx0, hy0 = x + r * math.cos(ang), y + r * math.sin(ang)
    hx1, hy1 = x + (r + 190) * math.cos(ang), y + (r + 190) * math.sin(ang)
    cv.line([(hx0 + 12, hy0 + 18), (hx1 + 12, hy1 + 18)], (40, 30, 20), 34, a * .18)
    cv.circ(x + 14, y + 20, r + 16, fill=(40, 30, 20), a=a * .16)
    cv.done()
    cv.im.paste(reg, (int(x - R), int(y - R)), m)
    cv.circ(x, y, r, fill=(255, 250, 235), a=a * .06)
    cv.circ(x - r * .35, y - r * .4, r * .25, fill=SNOW, a=a * .18)
    cv.circ(x, y, r + 8, outline=(46, 40, 34), w=16, a=a)
    cv.circ(x, y, r + 1, outline=BRASS2, w=3, a=a * .8)
    cv.line([(hx0, hy0), (hx1, hy1)], (52, 36, 24), 30, a)
    cv.line([(hx0 + 4, hy0 - 4), (hx1 + 4, hy1 - 4)], (110, 78, 50), 6, a * .7)
    cv.line([(hx0 - 4, hy0 - 4), (hx0 + 30 * math.cos(ang) - 4, hy0 + 30 * math.sin(ang) - 4)], BRASS, 34, a)

def alpha_strip(cv, cx, cy, a, t, missing="L", counts=None, ring=1.0, tile=58, bar=16):
    x0 = cx - 13 * tile + tile / 2
    for i in range(26):
        ch = chr(65 + i); x = x0 + i * tile
        ap = a * eo(pr(t, i * .03, i * .03 + .4))
        if ch == missing:
            cv.rrect(x - tile * .42, cy - tile * .55, x + tile * .42, cy + tile * .55, 6, fill=PAPER2, a=ap, outline=OX, w=2.5)
            dashed(cv, [(x - tile * .3, cy - tile * .3), (x + tile * .3, cy + tile * .3)], OX, 2, ap * .6, 6, 6)
            cv.text(x, cy, ch, tile * .55, OX, ap * .35, "Bold")
            if ring > 0:
                rr = tile * (.9 + .25 * (1 - eo(ring)))
                cv.circ(x, cy, rr, outline=OX, w=4, a=ap * eo(ring))
        else:
            cv.rrect(x - tile * .42, cy - tile * .55, x + tile * .42, cy + tile * .55, 6, fill=SNOW, a=ap, outline=RULE, w=1.5)
            cv.text(x, cy, ch, tile * .55, INK, ap, "monob")
        if counts is not None:
            hgt = counts[i] * bar * eo(pr(t, .6 + i * .02, 1.4 + i * .02))
            cv.rect(x - tile * .28, cy + tile * .75, x + tile * .28, cy + tile * .75 + hgt, fill=INK2 if ch != missing else OX, a=a * .85)

def scene_hook(cv, t, S, T):
    B = Beat(S)
    t_strip = B.kw(0, "single") - .6
    def s_mansion(cv, lt, al, d):
        fullphoto(cv, "mansion", lt / d, al, 1.04, 1.16, (.45, .5), (.52, .46), dark=.12)
    def s_sheet(cv, lt, al, d):
        message_sheet(cv, 960, 560, 1180, 760, al)
        rows = [CIPHER_NOL[r * 5:(r + 1) * 5] for r in range(6)]
        for r, row in enumerate(rows):
            for g, grp in enumerate(row):
                k = r * 5 + g
                rv = cl((lt * 9 - k * 1.4) / 1.4) * 5
                typed_row(cv, 470 + g * 205, 330 + r * 79, grp, 46, al, INK, 27, reveal=rv)
        # stamp header
        stamp(cv, 1380, 238, "GEHEIM", 40, -6, al * eo(pr(lt, 1.0, 1.4)), OX)
        # magnifier sweeps rows
        u = pr(lt, 1.5, d - .5)
        mx = 520 + (u * 3 % 1) * 900; my = 360 + int(u * 3) * 150
        magnifier(cv, mx, min(my, 690), 120, 1.6, al * eo(pr(lt, 1.2, 2.0)))
    def s_strip(cv, lt, al, d):
        rng = np.random.default_rng(3)
        counts = [0 if i == 11 else int(rng.integers(3, 12)) for i in range(26)]
        alpha_strip(cv, 960, 500, al, lt, "L", counts, ring=pr(lt, .8, 1.6), tile=66, bar=24)
        for r in range(2):
            for k in range(10):
                typed_row(cv, 250 + k * 150, 250 + r * 54, CIPHER_NOL[r * 10 + k], 30, al * .5, INK2, 19)
    def s_box(cv, lt, al, d):
        fullphoto(cv, "machine_rama", lt / d, al, 1.0, 1.18, (.5, .55), (.55, .42), dark=.05)
    def s_open(cv, lt, al, d):
        fullphoto(cv, "machine_open", lt / d, al, 1.05, 1.2, (.5, .45), (.5, .40), dark=.05)
    t_open = B.kw(1, "open") - .3
    seq(cv, t, [(0, 6.6, s_mansion), (6.6, t_strip, s_sheet), (t_strip, B(1, .48), s_strip),
                (B(1, .48), t_open, s_box), (t_open, S["dur"] + 1, s_open)])

def scene_sting(cv, t, S, T):
    a = eo(pr(t, .1, .9)) * (1 - eio(pr(t, S["dur"] - .5, S["dur"])))
    cv.done()
    # title type with letter spacing, each letter drops in
    word = "ENIGMA"; f = F(190, "serif"); trk = 34
    ws = [f.getlength(ch) for ch in word]; tot = sum(ws) + trk * (len(word) - 1); x = 960 - tot / 2
    for i, ch in enumerate(word):
        u = eo(pr(t, .1 + i * .07, .7 + i * .07))
        cv.text(x + ws[i] / 2, 470 - 30 * (1 - u), ch, 190, INK, a * u, "serif"); x += ws[i] + trk
    cv.line([(960 - 380 * eo(pr(t, .6, 1.4)), 610), (960 + 380 * eo(pr(t, .6, 1.4)), 610)], INK2, 2, a)
    s = eback(pr(t, 1.3, 1.75), 2.0)
    stamp(cv, 960, 730, "A \u2260 A", int(70 + 24 * (1 - cl(s))), -7, a * cl(s * 1.4), OX)

def rotor_wiring(cv, cx, cy, a, step, hi_in=0, t=0.0, scale=1.0, label=True):
    """rotor I as two contact columns joined by its real internal wiring; step shifts the entry by one."""
    top, bot = cy - 330 * scale, cy + 330 * scale
    xl, xr = cx - 260 * scale, cx + 260 * scale
    # body (metal disc seen as slab)
    cv.rrect(xl - 70, top - 40, xr + 70, bot + 40, 18, fill=(60, 56, 52), a=a * .10)
    cv.rrect(xl - 46, top - 30, xl + 10, bot + 30, 10, fill=BAKE2, a=a * .9)
    cv.rrect(xr - 10, top - 30, xr + 46, bot + 30, 10, fill=BAKE2, a=a * .9)
    yy = [lerp(top, bot, i / 25) for i in range(26)]
    sh = int(step) % 26
    for i in range(26):
        src = (i + sh) % 26
        dst = (ord(ROTOR_I[src]) - 65 - sh) % 26
        hi = (i == hi_in)
        p0 = (xl + 10, yy[i]); p3 = (xr - 10, yy[dst])
        pts = bez(p0, (cx - 60, yy[i]), (cx + 60, yy[dst]), p3, 22)
        if hi:
            cv.line([(x + 2, y + 3) for x, y in pts], (40, 30, 20), 6, a * .2)
            cv.line(pts, OX, 4.5, a)
        else:
            cv.line(pts, mix(BRASS3, INK2, (i % 3) / 3), 1.8, a * .55)
    for i in range(26):
        cv.circ(xl - 18, yy[i], 7, fill=BRASS2 if i != hi_in else OX, a=a)
        cv.circ(xr + 18, yy[i], 9, fill=STEEL3, a=a)
        cv.circ(xr + 18, yy[i], 9, outline=STEEL, w=1.5, a=a)
    if label:
        inn = chr(65 + hi_in); src = (hi_in + sh) % 26; out = chr(65 + (ord(ROTOR_I[src]) - 65 - sh) % 26)
        cv.text(xl - 90, yy[hi_in], inn, 44, OX, a, "Bold")
        cv.text(xr + 90, yy[(ord(ROTOR_I[src]) - 65 - sh) % 26], out, 44, OX, a, "Bold")
        for i in range(26):
            if i != hi_in: cv.text(xl - 60, yy[i], chr(65 + i), 16, MUT, a * .8, "SemiBold")

def scene_machine(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "01", win(t, 1, S["dur"] - .5))
    def s_hands(cv, lt, al, d):
        fullphoto(cv, "bundesarchiv", lt / d, al, 1.0, 1.15, (.55, .5), (.62, .42))
    def s_face(cv, lt, al, d):
        plain = "WETTERBERICHT"; ciph = enigma(plain)
        k = int(max(0, lt - .8) / .62); ph = (max(0, lt - .8) / .62) % 1
        press = math.sin(min(1, ph / .5) * math.pi) if k < len(plain) else 0
        litv = eo(pr(ph, .15, .3)) * (1 - pr(ph, .8, 1)) if k < len(plain) else 0
        kk = min(k, len(plain) - 1)
        rot = "AA" + chr(65 + (1 + min(k, len(plain))) % 26)
        machine_face(cv, 650, 545, .9, lt, lit_letter=ciph[kk], lit=litv, press_letter=plain[kk], press=press, a=al, rotors=rot)
        # notebook on the right: glowing letters written down
        panel(cv, 1260, 300, 1820, 800, al, 6, (246, 240, 226))
        for j in range(7): cv.line([(1290, 380 + j * 56), (1790, 380 + j * 56)], (196, 206, 214), 1.4, al * .7)
        cv.line([(1300, 310), (1300, 790)], OX2, 1.4, al * .6)
        n = min(len(ciph), k + (1 if ph > .3 else 0))
        typed_row(cv, 1330, 355, plain[:min(len(plain), k + 1)], 34, al * .45, INK2, 30, font="mono")
        typed_row(cv, 1330, 467, ciph[:n], 46, al, INK, 34, font="monob")
        cv.arrow(1340, 390, 1340, 428, OX, 3, al * .7, 12)
    def s_rotorphoto(cv, lt, al, d):
        fullphoto(cv, "rotors_rings", lt / d, al, 1.0, 1.14, (.4, .5), (.55, .5))
    def s_wiring(cv, lt, al, d):
        step = int(eio(pr(lt, d * .55, d * .55 + .5)) + .5)
        sm = eio(pr(lt, d * .55, d * .55 + .5))
        rotor_wiring(cv, 1000, 540, al, step, 0, lt)
        paste_card(cv, "rotor_wired", 380, 520, 440, 330, al * eo(pr(lt, .3, 1.0)), rot=-3)
    def s_odometer(cv, lt, al, d):
        out = "BDZGO"
        k = int(max(0, lt - 1.0) / 1.25); ph = (max(0, lt - 1.0) / 1.25) % 1
        nst = min(5, k + (1 if ph > .25 else 0))
        sm = nst - 1 + eio(pr(ph, 0, .25)) if k < 5 else 5
        sm = max(0, sm) if k < 5 else 5
        offs = [0, 0, sm + (0 if k < 5 else 0)]
        for j, (x, o) in enumerate(zip([680, 960, 1240], offs)):
            rotor_band(cv, x, 400, 230, 430, o, al)
        cv.text(960, 160, "", 1)
        # key A pressed five times and the lamps it lights
        press = math.sin(min(1, ph / .4) * math.pi) if k < 5 else 0
        key_cap(cv, 470, 760, 56, "A", press, al)
        cv.arrow(560, 760, 660, 760, INK2, 3, al * .8, 14)
        for j in range(5):
            lv = 1.0 if j < nst else 0.0
            if j == nst - 1 and k < 5: lv = eo(pr(ph, .25, .4))
            lamp(cv, 760 + j * 130, 760, 46, out[j] if j < nst else "", lv * .9, al * (1 if j < nst else .35))
    def s_plugphoto(cv, lt, al, d):
        fullphoto(cv, "plugboard", lt / d, al, 1.0, 1.15, (.45, .5), (.6, .55))
    def s_plugboard(cv, lt, al, d):
        pos = keyboard_layout(960 - 4 * 160, 400, 160, 150)
        cv.rrect(960 - 800 + 10, 300 + 14, 960 + 800 + 10, 760 + 14, 18, fill=(40, 30, 20), a=al * .2)
        cv.rrect(960 - 800, 300, 960 + 800, 760, 18, fill=BAKE, a=al)
        cv.rrect(960 - 786, 314, 960 + 786, 746, 12, outline=BAKE2, w=3, a=al)
        for ch, (x, y) in pos.items():
            for dx in (-16, 16):
                cv.circ(x + dx, y, 12, fill=(12, 11, 10), a=al); cv.circ(x + dx, y, 12, outline=STEEL2, w=3, a=al)
            cv.text(x, y - 42, ch, 26, (226, 218, 200), al, "SemiBold")
        pairs = ["AQ", "BP", "CE", "DM", "FK", "GZ", "HX", "IV", "JS", "NU"]
        for j, pq in enumerate(pairs):
            f = eio(pr(lt, .4 + j * .45, 1.1 + j * .45))
            if f <= 0: continue
            p0 = pos[pq[0]]; p1 = pos[pq[1]]
            cable(cv, (p0[0], p0[1]), (p1[0], p1[1]), al, 90 + 20 * (j % 3), f=f)
    def s_number(cv, lt, al, d):
        num = "158,962,555,217,826,360,000"
        u = eo(pr(lt, .2, 3.2))
        shown = ""
        rng = np.random.default_rng(int(max(0, lt) * 20))
        for i, ch in enumerate(num):
            if ch == ",": shown += ","; continue
            done_t = .3 + i * .1
            shown += ch if lt > done_t + .2 else str(rng.integers(0, 10))
        cv.text(960, 470, shown, 104, INK, al, "Black")
        cv.line([(260, 560), (1660, 560)], RULE, 2, al)
        # small rotor-order / position / plug icons as multiplication
        items = [("60", "I II III"), ("17,576", "AAA\u2192ZZZ"), ("150,738,274,937,250", "\u2194 \u00d710")]
        for j, (n, sub) in enumerate(items):
            aj = al * eo(pr(lt, 1.2 + j * .4, 1.8 + j * .4))
            x = [470, 830, 1360][j]
            cv.text(x, 640, n, 40, OX if j == 0 else INK2, aj, "Bold")
            cv.text(x, 690, sub, 26, MUT, aj, "SemiBold")
            if j < 2: cv.text([650, 1040][j], 640, "\u00d7", 40, MUT, aj, "Bold")
    def s_keysheet(cv, lt, al, d):
        panel(cv, 360, 210, 1560, 880, al, 4, (244, 238, 220))
        rng = np.random.default_rng(31)
        rom = ["I", "II", "III", "IV", "V"]
        scroll = eio(pr(lt, .6, d)) * 260
        cv.done()
        for r in range(14):
            y = 260 + r * 52 - scroll
            if y < 230 or y > 860: continue
            day = 31 - r
            ws = " ".join(rng.permutation(rom)[:3]); rs = " ".join(f"{int(v):02d}" for v in rng.integers(1, 27, 3))
            pl = " ".join("".join(rng.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 2, replace=False)) for _ in range(10))
            col = OX if r == 3 else INK
            cv.text(420, y, f"{day:02d}", 30, col, al, "monob", "lm")
            cv.text(520, y, ws, 30, col, al, "monob", "lm")
            cv.text(760, y, rs, 30, col, al, "monob", "lm")
            cv.text(930, y, pl, 28, col, al, "mono", "lm")
            cv.line([(400, y + 26), (1520, y + 26)], RULE, 1, al)
        stamp(cv, 1380, 820, "GEHEIM", 46, 8, al * eo(pr(lt, .4, .8)), OX)
    t3 = B(1); t4 = B(2)
    seq(cv, t, [(0, 6.8, s_hands), (6.8, t3 - .3, s_face),
                (t3 - .3, B(1, .26), s_rotorphoto), (B(1, .26), B(1, .58), s_wiring), (B(1, .58), t4 - .3, s_odometer),
                (t4 - .3, B(2, .22), s_plugphoto), (B(2, .22), B(2, .48), s_plugboard), (B(2, .48), B(2, .82), s_number),
                (B(2, .82), S["dur"] + 1, s_keysheet)])
