# Hashing explainer: sage paper, ink, ochre, brick
BG0, BG1 = (222, 228, 208), (203, 212, 186)
INKC = (30, 36, 28); WHT = INKC
TERRA, MUST, FOR, PLUM = (178, 62, 44), (206, 148, 40), (44, 112, 84), (78, 70, 110)
PAPER, EDGE, SHAD = (248, 249, 238), (120, 132, 100), (160, 172, 140)
GOLD = TERRA; BL, BL2 = TERRA, TERRA
NOFADE_IN, NOFADE_OUT = {0}, set()
def load_imgs():
    global GLOW_O, GLOW_B, GLOW_S, GLOW_G
    z = radial(40, (222, 228, 208), 0.0)
    GLOW_O = GLOW_B = GLOW_S = GLOW_G = z
def kinetic(cv, t, y, txt, size, col, t0, w="Black", stag=.05):
    ws = [cv.tw(c, size, w) for c in txt]; tot = sum(ws); x = 540 - tot / 2
    for i, c in enumerate(txt):
        q = eback(pr(t, t0 + i * stag, t0 + i * stag + .35), 2)
        cv.text(x + ws[i] / 2, y + (1 - q) * size * .7, c, size, col, cl(q * 1.5), w)
        x += ws[i]
def card(cv, x0, y0, x1, y1, r=26, fill=PAPER, outline=EDGE, a=1):
    cv.rrect(x0 + 8, y0 + 12, x1 + 8, y1 + 12, r, fill=SHAD, a=.55 * a)
    cv.rrect(x0, y0, x1, y1, r, fill=fill, a=a, outline=outline, w=3, oa=a)

H_CAT="77af778b51abd4a3c51c5ddd97204a9c3ae614ebccb75a606c3b6865aed6744e"
H_CATS="d936608baaacc6b762c14b0c356026fba3b84e77d5b22e86f2fc29d3da09c675"
def head(cv, t, a, b, c=None):
    kinetic(cv, t, 310, a, 66, INKC, .0, "Black", .02)
    if b: cv.text(540, 400, b, 40, c or TERRA, eo(pr(t, .3, .7)), "SemiBold")
def xmark(cv, x, y, r, a, col=TERRA):
    cv.line([(x-r, y-r), (x+r, y+r)], col, 12, a); cv.line([(x+r, y-r), (x-r, y+r)], col, 12, a)
def hashrows(cv, h, y, p, col=INKC, diff=None, n=4, size=34):
    k = len(h)//n
    for r in range(n):
        s = h[r*k:(r+1)*k]; cnt = int(len(s)*cl(p*1.5 - r*.1))
        cv.text(540, y + r*52, s[:cnt], size, col, cl(p*2), "Bold")
def s0(cv, t, D):
    cv.rrect(250, 380, 830, 440, 30, fill=TERRA, a=eo(pr(t, 0, .3)))
    cv.text(540, 408, "HOW LOGINS WORK", 32, PAPER, eo(pr(t, 0, .3)), "Black")
    kinetic(cv, t, 600, "YOUR PASSWORD", 100, INKC, -.2, "Black", .02)
    q = eback(pr(t, .1, .6), 2)
    card(cv, 190, 740, 890, 940, 40, a=cl(q))
    cv.text(540, 840, "•  •  •  •  •  •  •  •", 78 * q, INKC, cl(q), "Black")
    kinetic(cv, t, 1090, "THEY NEVER", 110, INKC, .3, "Black", .03)
    kinetic(cv, t, 1230, "SEE IT", 130, TERRA, .5, "Black", .03)
def s1(cv, t, D):
    head(cv, t, "HASHING", "text in, fingerprint out")
    p1 = eback(pr(t, .3, .8), 2); p2 = eo(pr(t, 1.2, 1.8)); p3 = eback(pr(t, 2.0, 2.6), 2)
    card(cv, 200, 520, 880, 660, 30, a=cl(p1)); cv.text(540, 590, "any text, any length", 44, INKC, cl(p1), "Bold")
    cv.line([(540, 680), (540, 760)], INKC, 8, p2); cv.line([(500, 730), (540, 770), (580, 730)], INKC, 8, p2)
    card(cv, 260, 790, 820, 960, 30, fill=MUST, outline=MUST, a=cl(p2))
    cv.text(540, 850, "HASH FUNCTION", 46, INKC, cl(p2), "Black")
    cv.text(540, 915, "a one-way grinder", 32, INKC, cl(p2), "SemiBold")
    cv.line([(540, 975), (540, 1045)], INKC, 8, p3); cv.line([(500, 1015), (540, 1055), (580, 1015)], INKC, 8, p3)
    card(cv, 120, 1070, 960, 1330, 30, a=cl(p3))
    cv.text(540, 1120, "fixed-size fingerprint", 38, FOR, cl(p3), "Black")
    hashrows(cv, H_CAT, 1190, pr(t, 2.6, 3.4), n=2, size=30)
def s2(cv, t, D):
    head(cv, t, "TYPE “cat”", "SHA-256 output")
    p = eback(pr(t, .3, .8), 2)
    card(cv, 330, 520, 750, 680, 36, fill=TERRA, outline=TERRA, a=cl(p))
    cv.text(540, 600, "cat", 110 * p, PAPER, cl(p), "Black")
    card(cv, 70, 780, 1010, 1160, 34, a=eo(pr(t, .8, 1.2)))
    cv.text(540, 840, "64 characters", 40, FOR, eo(pr(t, 1.0, 1.4)), "Black")
    hashrows(cv, H_CAT, 920, pr(t, 1.2, 3.4), size=34)
    cv.text(540, 1290, "always exactly 64", 46, INKC, eo(pr(t, 3.2, 3.8)), "Bold")
def s3(cv, t, D):
    head(cv, t, "ADD ONE LETTER", "“cats”: everything changes")
    for k, (w_, h, col, y) in enumerate([("cat", H_CAT, FOR, 520), ("cats", H_CATS, TERRA, 920)]):
        p = eo(pr(t, .3 + k * 1.4, .9 + k * 1.4))
        card(cv, 70, y, 1010, y + 340, 34, a=p)
        cv.text(300, y + 56, w_, 54, col, p, "Black")
        for r in range(4):
            s = h[r*16:(r+1)*16]
            x = 540 - cv.tw(s, 38, "Bold") / 2
            for j, ch in enumerate(s):
                same = (k == 1 and H_CAT[r*16+j] == ch)
                cv.text(x + cv.tw(s[:j], 38, "Bold") + cv.tw(ch, 38, "Bold") / 2, y + 130 + r * 52, ch, 38, MUST if same else (INKC if k == 0 else TERRA), p, "Bold")
    cv.text(540, 1330, "no pattern. no resemblance.", 44, INKC, eo(pr(t, 3.0, 3.6)), "Bold")
def s4(cv, t, D):
    head(cv, t, "ONE WAY ONLY", "forward yes, backward no")
    p = eo(pr(t, .3, .9))
    card(cv, 100, 560, 980, 800, 34, a=p)
    cv.text(300, 680, "cat", 70, INKC, p, "Black"); cv.text(780, 680, "77af78…", 54, INKC, p, "Black")
    cv.line([(430, 680), (640, 680)], FOR, 10, p); cv.line([(600, 645), (645, 680), (600, 715)], FOR, 10, p)
    cv.text(540, 760, "same input, same fingerprint", 32, FOR, eo(pr(t, 1.0, 1.5)), "Bold")
    q = eo(pr(t, 2.0, 2.6))
    card(cv, 100, 900, 980, 1140, 34, a=q)
    cv.text(780, 1000, "77af78…", 54, INKC, q, "Black"); cv.text(300, 1000, "???", 70, TERRA, q, "Black")
    cv.line([(640, 1000), (430, 1000)], TERRA, 10, q); xmark(cv, 535, 1000, 30, q)
    cv.text(540, 1085, "can't run it backwards", 32, TERRA, q, "Bold")
def s5(cv, t, D):
    head(cv, t, "THE LOGIN CHECK", "the site stores only the hash")
    p = eo(pr(t, .3, .8))
    card(cv, 80, 520, 1000, 700, 30, a=p); cv.text(540, 580, "database stores", 34, PLUM, p, "Black"); cv.text(540, 650, "d936608b…", 54, INKC, p, "Black")
    q = eo(pr(t, 1.0, 1.6))
    card(cv, 80, 780, 1000, 940, 30, a=q); cv.text(540, 835, "you type  “cats”", 40, INKC, q, "Bold")
    cv.text(540, 900, "→ hashed → d936608b…", 40, MUST, eo(pr(t, 1.8, 2.4)), "Black")
    r = eback(pr(t, 3.0, 3.6), 2)
    card(cv, 220, 1040, 860, 1230, 40, fill=FOR, outline=FOR, a=cl(r))
    check(cv, 360, 1135, 50, cl(r), PAPER, 14); cv.text(620, 1135, "MATCH", 74, PAPER, cl(r), "Black")
def s6(cv, t, D):
    head(cv, t, "IF HACKERS STEAL IT", "they get this")
    p = eo(pr(t, .3, .9))
    card(cv, 100, 520, 980, 1100, 34, a=p)
    names = ["anna", "omar", "li", "sam", "zoya"]; hs = ["a91f03…", "5e7c20…", "c04b9d…", "73d1ea…", "e2086f…"]
    for k in range(5):
        a_ = eo(pr(t, .6 + k * .25, 1.1 + k * .25)); y = 600 + k * 95
        cv.text(250, y, names[k], 40, INKC, a_, "Bold"); cv.text(700, y, hs[k], 44, EDGE, a_, "Black")
    q = eback(pr(t, 2.4, 3.0), 2)
    card(cv, 200, 1180, 880, 1330, 36, fill=TERRA, outline=TERRA, a=cl(q))
    cv.text(540, 1255, "not your password", 52, PAPER, cl(q), "Black")
def s7(cv, t, D):
    head(cv, t, "RED FLAG", "a site that can email your password")
    p = eback(pr(t, .4, 1.0), 2)
    card(cv, 120, 560, 960, 1000, 36, a=cl(p))
    cv.text(540, 650, "“Your password is:", 46, INKC, cl(p), "Bold")
    cv.text(540, 760, "hunter2”", 90, TERRA, cl(p), "Black")
    cv.text(540, 880, "stored as plain text", 38, PLUM, eo(pr(t, 1.2, 1.7)), "SemiBold")
    xmark(cv, 540, 1160, 60, eo(pr(t, 1.6, 2.1)))
    cv.text(540, 1290, "it's doing it wrong", 52, INKC, eo(pr(t, 2.0, 2.6)), "Black")
def s8(cv, t, D):
    head(cv, t, "SAME IDEA, EVERYWHERE", None)
    for k, (n_, s_, c) in enumerate([("Downloads", "is this file intact?", FOR), ("Git", "every commit is a hash", PLUM), ("Bitcoin", "blocks chained by hashes", MUST)]):
        p = eback(pr(t, .5 + k * .6, 1.0 + k * .6), 2); y = 640 + k * 230
        card(cv, 120, y - 90, 960, y + 90, 36, fill=c, outline=c, a=cl(p))
        cv.text(540, y - 22, n_, 66, PAPER if c != MUST else INKC, cl(p), "Black")
        cv.text(540, y + 45, s_, 34, PAPER if c != MUST else INKC, cl(p), "SemiBold")
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(4):
        u = (t * .3 + k / 4) % 1
        cv.circ(540, 640, 60 + u * 300, outline=TERRA, w=4, oa=(1 - u) * .6 * p)
    cv.circ(540, 640, 70 * p, fill=TERRA, a=p)
    kinetic(cv, t, 1010, "LATOON", 150, INKC, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, TERRA, eo(pr(t, 1.0, 1.5)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
