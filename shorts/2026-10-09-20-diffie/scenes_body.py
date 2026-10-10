
def fadectx(cv, a):
    g = cv.ga; cv.ga = g * cl(a); return g
def envelope(cv, x, y, s, col=YEL, a=1):
    cv.rrect(x - 34 * s + 3, y - 24 * s + 6, x + 34 * s + 3, y + 24 * s + 6, 5 * s, fill=SHAD, a=.4 * a)
    cv.rrect(x - 34 * s, y - 24 * s, x + 34 * s, y + 24 * s, 5 * s, fill=col, a=a, outline=INK, w=2, oa=a)
    cv.line([(x - 32 * s, y - 22 * s), (x, y + 3 * s), (x + 32 * s, y - 22 * s)], INK, 2, a * .8)
def s0(cv, t, D):
    kinetic(cv, t, 330, "A SECRET,", 112, INKC, -.2, "Black", .03)
    kinetic(cv, t, 460, "IN PUBLIC", 112, YEL, -.1, "Black", .03)
    p = eo(pr(t, .0, .5))
    card(cv, 100, 590, 980, 1360, 34, a=p)
    cv.line([(330, 1000), (750, 1000)], mix(PAPER, INK, .45), 4, .9 * p)
    phone(cv, 250, 1000, 1.05, p)
    cv.text(250, 1195, "YOUR PHONE", 30, INK, p, "Black")
    icon_person(cv, 830, 975, 230, TEA, p)
    cv.text(830, 1195, "STRANGER", 30, INK, p, "Black")
    for k in range(3):
        u = ((t * .5 + k / 3.0) % 1.0)
        x = lerp(340, 740, u) if k % 2 == 0 else lerp(740, 340, u)
        envelope(cv, x, 1000, .9, YEL if k % 2 == 0 else TEA, eo(pr(t, .5, .9)))
    pts = [(420, 790), (540, 770), (660, 790), (420, 1210), (540, 1230), (660, 1210)]
    px = lerp(340, 740, (t * .5) % 1.0)
    for i, (x, y) in enumerate(pts):
        q = eback(pr(t, .6 + i * .1, 1.0 + i * .1), 2)
        eye(cv, x, y, .8 * q, px, 1000, cl(q * 1.4))
def s1(cv, t, D):
    head(cv, t, "DIFFIE–HELLMAN", "published in 1976", YEL)
    q1 = eback(pr(t, .1, .8), 1.5); q2 = eback(pr(t, .3, 1.0), 1.5)
    img(cv, None, lerp(-300, 290, q1), 960, .92, a=eo(pr(t, .1, .4)), src=IM["p_diffie"])
    img(cv, None, lerp(1380, 790, q2), 985, .92, a=eo(pr(t, .3, .6)), src=IM["p_hellman"])
    chip(cv, 110, 1310, 860, "NEW DIRECTIONS IN CRYPTOGRAPHY", YEL, eo(pr(t, 1.6, 2.2)), INK, 34)
def s2(cv, t, D):
    head(cv, t, "STEP 1", "agree on a public color", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    split = eio(pr(t, 1.7, 2.7))
    big = eback(pr(t, .2, .8), 1.8)
    if split < 1:
        bucket(cv, 540, lerp(930, 950, split), 1.55 * big * (1 - .32 * split), YEL, 1 - split * .0)
    if split > 0:
        bucket(cv, lerp(540, 290, split), 950, .95 * split + .01, YEL, split)
        bucket(cv, lerp(540, 790, split), 950, .95 * split + .01, YEL, split)
        cv.text(290, 1130, "YOU", 40, INK, split, "Black"); cv.text(790, 1130, "STRANGER", 40, INK, split, "Black")
    a = eo(pr(t, 1.0, 1.6))
    chip(cv, 300, 1240, 480, "PUBLIC YELLOW", YEL, a, INK, 34)
    eye(cv, 880, 680, .8, 560, 930, eo(pr(t, 1.2, 1.8)))
    cv.text(880, 735, "spy sees it", 28, mix(INK, PAPER, .3), eo(pr(t, 1.4, 2.0)), "Bold")
def s3(cv, t, D):
    head(cv, t, "STEP 2", "add a secret color, then swap", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    q = eo(pr(t, .9, 1.5))
    sw = eio(pr(t, 1.9, 3.3))
    # secret swatches
    for x, c, nm in ((200, RED, "your secret"), (880, TEA, "their secret")):
        cv.circ(x, 1260, 42, fill=c, a=eo(pr(t, .1, .5)), outline=INK, w=3)
        lock(cv, x, 1260, .7, PAPER, eo(pr(t, .2, .6)))
        cv.text(x, 1330, nm, 26, INK, eo(pr(t, .3, .7)), "Bold")
    # drops
    for x, c, d0 in ((290, RED, .2), (790, TEA, .2)):
        u = pr(t, d0, d0 + .8)
        if 0 < u < 1: drop(cv, x, lerp(640, 840, u * u), 54, c, 1 - pr(t, d0 + .7, d0 + .8))
    cL, cR = mix(YEL, ORG, q), mix(YEL, GRN, q)
    ay = 120 * math.sin(sw * math.pi)
    bucket(cv, lerp(290, 790, sw), 950 - ay, .95, cL)
    bucket(cv, lerp(790, 290, sw), 950 + ay, .95, cR)
    if sw > .02:
        eye(cv, 540, 690, .85, 540, 950, eo(pr(t, 2.0, 2.5)))
    cv.text(540, 1140, "mixed buckets cross in plain sight", 32, INK, eo(pr(t, 2.9, 3.5)), "Bold")
def s4(cv, t, D):
    head(cv, t, "STEP 3", "add your secret again", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    q = eo(pr(t, 1.0, 1.7))
    for x, c, base, d0 in ((290, RED, GRN, .3), (790, TEA, ORG, .3)):
        u = pr(t, d0, d0 + .8)
        if 0 < u < 1: drop(cv, x, lerp(640, 840, u * u), 54, c, 1 - pr(t, d0 + .7, d0 + .8))
        bucket(cv, x, 950, .95, mix(base, BRN, q))
    cv.text(290, 1130, "YOU", 36, INK, 1, "Black"); cv.text(790, 1130, "STRANGER", 36, INK, 1, "Black")
    e = eback(pr(t, 2.0, 2.6), 2)
    cv.text(540, 950, "=", int(150 * e), INK, cl(e), "Black")
    pulse = pr(t, 2.2, 3.3)
    if 0 < pulse < 1:
        for x in (290, 790): cv.circ(x, 950, 150 * eo(pulse) + 20, outline=BRN, w=6, oa=1 - pulse)
    chip(cv, 300, 1230, 480, "SAME BROWN", BRN, eo(pr(t, 2.4, 3.0)), INKC, 38)
def s5(cv, t, D):
    A = 1 - eo(pr(t, 2.9, 3.3))
    g = fadectx(cv, A)
    head(cv, t, "WHAT THE SPY SEES", "every bucket that crossed", YEL)
    cv.ga = g
    card(cv, 100, 560, 980, 1380, 34)
    if A > .02:
        g = fadectx(cv, A)
        for i, (x, c, nm) in enumerate(((235, YEL, "public"), (425, ORG, "yours"), (615, GRN, "theirs"))):
            q = eback(pr(t, .2 + i * .25, .8 + i * .25), 1.8)
            bucket(cv, x, 1010, .62 * q + .01, c, cl(q * 1.4))
            cv.text(x, 1130, nm, 28, INK, cl(q * 1.4), "Bold")
        # missing brown
        qq = eo(pr(t, 1.2, 1.8))
        for k in range(14):
            a0 = k * 2 * math.pi / 14
            cv.line([(805 + 66 * math.cos(a0), 1010 + 66 * math.sin(a0)), (805 + 66 * math.cos(a0 + .25), 1010 + 66 * math.sin(a0 + .25))], mix(PAPER, INK, .55), 4, qq)
        cv.text(805, 1010, "?", 90, BRN, qq, "Black")
        cv.text(805, 1130, "final", 28, INK, qq, "Bold")
        ex = lerp(235, 805, (math.sin(t * 2.1) + 1) / 2)
        eye(cv, 540, 740, 1.5 * eo(pr(t, .3, .8)), ex, 1010, 1)
        chip(cv, 215, 1230, 650, "SEES BOTH. CAN'T MAKE BROWN.", RED, eo(pr(t, 1.8, 2.4)), INKC, 30)
        cv.ga = g
    B = eo(pr(t, 3.3, 3.8))
    if B > .02:
        g = fadectx(cv, B)
        kinetic(cv, t, 310, "MIXING IS EASY", 66, INKC, 3.3, "Black", .02)
        kinetic(cv, t, 400, "UN-MIXING IS HARD", 52, YEL, 3.6, "Black", .02)
        cv.ga = g
        u1 = eo(pr(t, 3.9, 4.6)); u2 = eo(pr(t, 5.0, 5.8))
        for yy, lab in ((830, "MIX"), (1130, "UN-MIX")):
            bucket(cv, 260, yy, .5, YEL); cv.text(260, yy + 86, "yellow + red", 24, INK, 1, "Bold") if yy == 830 else None
        # row 1: forward easy
        bucket(cv, 820, 830, .5, ORG, u1)
        cv.line([(380, 830), (lerp(380, 700, u1), 830)], GRN, 10, 1)
        cv.poly([(lerp(380, 700, u1) + 36, 830), (lerp(380, 700, u1), 800), (lerp(380, 700, u1), 860)], GRN, u1)
        chip(cv, 400, 905, 260, "EASY", GRN, u1, INKC, 34, 62)
        # row 2: reverse hard
        bucket(cv, 820, 1130, .5, ORG, u2); bucket(cv, 260, 1130, .5, mix(PAPER, INK, .15), u2)
        cv.text(260, 1130, "?", 70, INK, u2, "Black")
        cv.line([(700, 1130), (lerp(700, 380, u2), 1130)], RED, 8, u2)
        for k in range(5):
            xx = lerp(700, 380, k / 4.0)
            cv.line([(xx - 6, 1130 - 26), (xx + 6, 1130 + 26)], PAPER, 8, u2)
        cx_ = 540; cv.line([(cx_ - 30, 1090), (cx_ + 30, 1170)], RED, 12, u2); cv.line([(cx_ + 30, 1090), (cx_ - 30, 1170)], RED, 12, u2)
        chip(cv, 400, 1215, 260, "HARD", RED, u2, INKC, 34, 62)
def s6(cv, t, D):
    head(cv, t, "SAME TRICK, WITH NUMBERS", "5^x mod 23 · a toy version", YEL)
    card(cv, 100, 520, 980, 1400, 34)
    vals = [pow(5, x, 23) for x in range(1, 23)]
    cw, chh = 132, 118; x0, y0 = 540 - 3 * cw, 590
    scan = pr(t, 3.5, 5.7)
    si = int(scan * 22) if 0 < scan < 1 else (14 if scan >= 1 else -1)
    for i in range(22):
        r, c = divmod(i, 6)
        x, y = x0 + c * cw, y0 + r * chh
        q = eback(pr(t, .2 + i * .045, .6 + i * .045), 1.6)
        hl_f = (i == 5 and 1.6 < t < 3.2)
        hl_s = (i == si and scan > 0)
        found = (scan >= 1 and i == 14) or (i == 14 and si >= 14 and scan > 0)
        col = PAPER2
        if hl_f: col = GRN
        elif found: col = YEL
        elif hl_s: col = mix(PAPER2, RED, .55)
        cv.rrect(x + 6, y + 6, x + cw - 6, y + chh - 6, 14, fill=mix(col, (0, 0, 0), .0), a=cl(q * 1.4), outline=mix(col, INK, .35), w=2, oa=cl(q * 1.4))
        cv.text(x + 24, y + 24, str(i + 1), 22, mix(INK, PAPER, .35), cl(q * 1.4), "Bold")
        cv.text(x + cw / 2, y + chh / 2 + 8, str(vals[i]), 52 * (.6 + .4 * q), INKC if hl_f else INK, cl(q * 1.4), "Black")
    a1 = eo(pr(t, 1.6, 2.1)) * (1 - eo(pr(t, 3.2, 3.5)))
    chip(cv, 170, 1300, 740, "FORWARD: 5^6 mod 23 = 8, INSTANT", GRN, a1, INKC, 32)
    a2 = eo(pr(t, 3.5, 4.0))
    lbl = "BACKWARD: SEARCH EVERY CELL..." if scan < 1 else "FOUND x = 15, FOR A TOY PRIME"
    chip(cv, 140, 1300, 800, lbl, RED if scan < 1 else YEL, a2, INKC if scan < 1 else INK, 32)
def s7(cv, t, D):
    head(cv, t, "NOW MAKE IT HUGE", "a prime about 2048 bits long", YEL)
    card(cv, 100, 560, 980, 1400, 34, fill=INK)
    rs = random.Random(8)
    cols, rows = 18, 14
    for r in range(rows):
        for c in range(cols):
            d = str(rs.randint(0, 9))
            if (c * 7 + r * 3 + int(t * 8)) % 11 == 0: d = str((int(d) + int(t * 8)) % 10)
            q = eo(pr(t, r * .06, .5 + r * .06))
            wave = .5 + .5 * math.sin(t * 3 - c * .5 + r * .4)
            cv.text(145 + c * 44.5, 610 + r * 56 + (1 - q) * -30, d, 36, mix((120, 100, 60), YEL, wave), cl(q * (.35 + .5 * wave)), "Bold")
    a = eback(pr(t, 1.0, 1.6), 1.6)
    card(cv, 190, 840, 890, 1090, 26, a=cl(a))
    cv.text(540, 930, "≈ 617 DIGITS", int(84 * (.7 + .3 * a)), INK, cl(a), "Black")
    cv.text(540, 1015, "2048 bits long", 36, mix(INK, PAPER, .25), eo(pr(t, 1.4, 1.9)), "Bold")
    chip(cv, 170, 1230, 740, "NO KNOWN FAST WAY BACK", RED, eo(pr(t, 2.6, 3.2)), INKC, 34)
def circ_img(key, size):
    k = "c_" + key
    if k not in IM:
        im = ImageOps.fit(IM[key].convert("RGB"), (size, size), Image.LANCZOS, centering=(.5, .3))
        m = Image.new("L", (size * 2, size * 2), 0); ImageDraw.Draw(m).ellipse((0, 0, size * 2 - 1, size * 2 - 1), fill=255)
        m = m.resize((size, size), Image.LANCZOS)
        out = Image.new("RGBA", (size + 24, size + 24), (0, 0, 0, 0))
        ImageDraw.Draw(out).ellipse((0, 0, size + 23, size + 23), fill=PAPER + (255,))
        im = im.convert("RGBA"); im.putalpha(m); out.alpha_composite(im, (12, 12)); IM[k] = out
    return IM[k]
def medal(cv, cx, cy, s, a=1):
    cv.poly([(cx - 70 * s, cy - 200 * s), (cx - 10 * s, cy - 200 * s), (cx + 40 * s, cy - 20 * s), (cx - 20 * s, cy - 20 * s)], RED, a)
    cv.poly([(cx + 70 * s, cy - 200 * s), (cx + 10 * s, cy - 200 * s), (cx - 40 * s, cy - 20 * s), (cx + 20 * s, cy - 20 * s)], mix(RED, (0, 0, 0), .3), a)
    cv.circ(cx + 6, cy + 14, 112 * s, fill=SHAD, a=.5 * a)
    cv.circ(cx, cy, 112 * s, fill=(176, 130, 40), a=a)
    cv.circ(cx, cy, 104 * s, fill=(228, 182, 70), a=a, outline=(250, 226, 150), w=4, oa=a)
    cv.circ(cx, cy, 80 * s, outline=(176, 130, 40), w=3, oa=a)
    cv.text(cx, cy - 6 * s, "2015", int(56 * s), (92, 62, 16), a, "Black")
    cv.text(cx, cy + 40 * s, "TURING", int(24 * s), (92, 62, 16), a, "Black")
def s8(cv, t, D):
    head(cv, t, "2015 TURING AWARD", "for public-key cryptography", YEL)
    card(cv, 100, 560, 980, 1400, 34)
    q = eback(pr(t, .2, .9), 1.6)
    medal(cv, 540, 860 + (1 - q) * -60, 1.25, cl(q * 1.4))
    img(cv, None, 205, 800, 1.0, eo(pr(t, .5, 1.0)), circ_img("diffie", 190))
    img(cv, None, 875, 800, 1.0, eo(pr(t, .7, 1.2)), circ_img("hellman", 190))
    cv.text(205, 935, "Diffie", 28, INK, eo(pr(t, .7, 1.2)), "Black"); cv.text(875, 935, "Hellman", 28, INK, eo(pr(t, .9, 1.4)), "Black")
    b = eo(pr(t, 2.2, 2.9))
    cv.rrect(150, 1080, 930, 1180, 50, fill=(250, 246, 234), a=b, outline=INK, w=3, oa=b)
    lock(cv, 220, 1130, .75, GRN, b)
    cv.text(300, 1130, "https://", 40, INK, b, "Bold", anchor="lm")
    cv.text(470, 1130, "your-bank.com", 40, mix(INK, PAPER, .45), b, "Bold", anchor="lm")
    chip(cv, 210, 1250, 660, "STILL IN YOUR BROWSER TODAY", YEL, eo(pr(t, 3.4, 4.0)), INK, 32)
def s9(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, YEL, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
