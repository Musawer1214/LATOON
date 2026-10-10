from common import *
from scenes_a import magnifier, alpha_strip, CIPHER_NOL, rotor_wiring
from scenes_b import folder

LCT = enigma("L" * 60, "KRV")

def scene_lever(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "06", win(t, 1, S["dur"] - .5))
    def s_back(cv, lt, al, d):
        message_sheet(cv, 960, 560, 1180, 760, al)
        for r in range(6):
            for g in range(5):
                typed_row(cv, 470 + g * 205, 330 + r * 79, LCT[(r * 5 + g) * 2 % 55:(r * 5 + g) * 2 % 55 + 5], 46, al, INK, 27)
        stamp(cv, 1380, 238, "GEHEIM", 40, -6, al, OX)
        magnifier(cv, 760 + lt * 40, 500, 130, 1.6, al)
    def s_keys(cv, lt, al, d):
        z = lerp(1.0, 1.75, eio(pr(lt, 0, 2.5)))
        cv.cam = Cam(lerp(960, 1250, eio(pr(lt, 0, 2.5))), lerp(540, 690, eio(pr(lt, 0, 2.5))), z)
        k = int(max(0, lt - 2.6) / .7); ph = (max(0, lt - 2.6) / .7) % 1
        press = math.sin(min(1, ph / .45) * math.pi) if lt > 2.6 else 0
        litv = eo(pr(ph, .15, .3)) * (1 - pr(ph, .85, 1)) if lt > 2.6 else 0
        machine_face(cv, 960, 560, 1.0, lt, lit_letter=LCT[k % 60], lit=litv, press_letter="L", press=press, a=al, rotors="KR" + chr(65 + (21 + k) % 26))
        cv.cam = Cam()
        # running ciphertext strip at top
        n = min(24, k)
        cv.rect(0, 126, W, 212, fill=(50, 36, 22), a=al * .15)
        cv.rect(0, 118, W, 202, fill=(246, 240, 226), a=al)
        typed_row(cv, 960 - 23 * 36 / 2, 160, LCT[:n], 40, al, INK, 36, font="monob")
    def s_hist(cv, lt, al, d):
        cnt = [LCT.count(chr(65 + i)) for i in range(26)]
        cnt2 = [enigma("L" * 300, "KRV").count(chr(65 + i)) for i in range(26)]
        alpha_strip(cv, 960, 360, al, lt, "L", [c / max(cnt2) * 14 for c in cnt2], ring=pr(lt, 2.5, 3.3), tile=66, bar=24)
    def s_reveal(cv, lt, al, d):
        sp = 54; x0 = 960 - sp * 13.5
        for i in range(28):
            ap = al * eo(pr(lt, i * .03, i * .03 + .3))
            cv.rrect(x0 + i * sp - 24, 330, x0 + i * sp + 24, 396, 5, fill=SNOW, a=ap, outline=RULE, w=1.5)
            cv.text(x0 + i * sp, 363, LCT[i], 36, INK, ap, "monob")
            al2 = al * eo(pr(lt, 1.2 + i * .05, 1.5 + i * .05))
            cv.text(x0 + i * sp, 470, "L", 40, OX, al2, "monob")
        # new rotor wiring revealed on the right side
        ap = al * eo(pr(lt, 4.5, 5.5))
        if ap > .01:
            cv.cam = Cam(960, 300, 1.0)
            cv.cam = Cam()
            rotor_wiring(cv, 960, 740, ap, 0, 11, lt, .5, label=False)
    t18 = B(1)
    seq(cv, t, [(0, 6.0, s_back), (6.0, t18 - .2, s_keys), (t18 - .2, B(1, .55), s_hist), (B(1, .55), S["dur"] + 1, s_reveal)])

def grid26(cv, x0, y0, cell, a, kind, t, hl=0.0):
    rng = np.random.default_rng(77 if kind == "aes" else 12)
    vals = rng.random((26, 26))
    for r in range(26):
        for c in range(26):
            ap = a * eo(pr(t, (r + c) * .02, (r + c) * .02 + .3))
            if ap <= .01: continue
            x, y = x0 + c * cell, y0 + r * cell
            if kind == "enigma" and r == c:
                cv.rect(x + 1, y + 1, x + cell - 1, y + cell - 1, fill=PAPER, a=ap, outline=OX, w=1.2 + 2 * hl)
                continue
            v = vals[r, c]
            col = mix((214, 200, 176), (70, 62, 54), v * .9)
            cv.rect(x + 1, y + 1, x + cell - 1, y + cell - 1, fill=col, a=ap)
    if kind == "enigma" and hl > 0:
        cv.line([(x0, y0), (x0 + 26 * cell, y0 + 26 * cell)], OX, 2.5, a * hl * .5)

def scene_lesson(cv, t, S, T):
    B = Beat(S)
    chapter_tag(cv, "07", win(t, 1, S["dur"] - .5))
    def s_peel(cv, lt, al, d):
        fullphoto(cv, "bombe_peel", lt / d, al, 1.12, 1.0, (.55, .5), (.45, .5), dark=.08)
    def s_two(cv, lt, al, d):
        # left: reflector ring miniature ; right: stacked routine phrases
        panel(cv, 200, 230, 900, 830, al, 8, (246, 240, 226))
        panel(cv, 1020, 230, 1720, 830, al * eo(pr(lt, .6, 1.2)), 8, (246, 240, 226))
        cx_, cy_, R = 550, 520, 210
        cv.circ(cx_, cy_, R + 34, fill=STEEL2, a=al); cv.circ(cx_, cy_, R + 6, fill=(236, 230, 214), a=al)
        pairs = "YRUHQSLDPXNGOKMIEBFZCWVJAT"; done = set()
        for i in range(26):
            j = ord(pairs[i]) - 65
            if (j, i) in done: continue
            done.add((i, j))
            a1 = -math.pi / 2 + i * 2 * math.pi / 26; a2 = -math.pi / 2 + j * 2 * math.pi / 26
            p1 = (cx_ + R * .9 * math.cos(a1), cy_ + R * .9 * math.sin(a1)); p2 = (cx_ + R * .9 * math.cos(a2), cy_ + R * .9 * math.sin(a2))
            cv.line(bez(p1, (lerp(p1[0], cx_, .5), lerp(p1[1], cy_, .5)), (lerp(p2[0], cx_, .5), lerp(p2[1], cy_, .5)), p2, 16), OX if i == 0 else BRASS3, 3 if i == 0 else 1.6, al)
        stamp(cv, 550, 300, "A \u2260 A", 40, -6, al * eo(pr(lt, 1.0, 1.4)), OX)
        ap = al * eo(pr(lt, .9, 1.5))
        for k in range(6):
            y = 330 + k * 82
            cv.text(1080, y, "KEINEBESONDERENEREIGNISSE"[:20], 34, OX if k % 2 == 0 else INK, ap * eo(pr(lt, 1.2 + k * .25, 1.6 + k * .25)), "monob", "lm")
    def s_kerck(cv, lt, al, d):
        portrait(cv, "kerckhoffs", 640, 520, 360, 520, al, rot=-3)
        paste_card(cv, "lacrypto", 1180, 540, 380, 560, al * eo(pr(lt, .5, 1.1)), rot=3)
        stamp(cv, 1500, 300, "1883", 64, -8, al * eo(pr(lt, 1.2, 1.6)), OX)
    def s_key(cv, lt, al, d):
        # machine plans (rotor wiring blueprint) visible to everyone; the key is the only secret
        panel(cv, 180, 220, 1000, 860, al, 4, (238, 232, 216))
        rotor_wiring(cv, 590, 540, al * .85, 0, 4, lt, .78, label=False)
        stamp(cv, 590, 820, "\u2713", 50, 0, al * eo(pr(lt, 1.0, 1.4)), GREEN, box=False)
        brass_key(cv, 1400, 540, 1.6, al * eo(pr(lt, .8, 1.6)), -.25 + .05 * math.sin(lt))
        stamp(cv, 1400, 780, "GEHEIM", 46, -6, al * eo(pr(lt, 2.0, 2.4)), OX)
        # leak arrow from the machine to the side
        if lt > d * .6:
            f = eio(pr(lt, d * .6, d * .6 + 1.2))
            dashed(cv, partial([(1000, 400), (1150, 330), (1300, 300)], f), OX, 3, al, 10, 8)
            if f >= 1: cv.text(1340, 300, "A \u2260 A", 34, OX, al, "Bold", "lm")
    def s_grids(cv, lt, al, d):
        cell = 22
        grid26(cv, 300, 250, cell, al, "enigma", lt, hl=eo(pr(lt, d - 7.5, d - 6.5)))
        grid26(cv, 1050, 250, cell, al * eo(pr(lt, .8, 1.4)), "aes", lt - .8)
        cv.text(300 + 13 * cell, 850, "ENIGMA", 30, INK, al, "Bold")
        cv.text(1050 + 13 * cell, 850, "AES", 30, INK, al * eo(pr(lt, .8, 1.4)), "Bold")
        for i in range(0, 26, 5):
            cv.text(290, 250 + i * cell + cell / 2, chr(65 + i), 16, MUT, al, "SemiBold", "rm")
            cv.text(300 + i * cell + cell / 2, 240, chr(65 + i), 16, MUT, al, "SemiBold", "mb")
    t20, t21 = B(1), B(2)
    seq(cv, t, [(0, 9.0, s_peel), (9.0, t20 - .2, s_two), (t20 - .2, B(1, .5), s_kerck), (B(1, .5), t21 - .2, s_key), (t21 - .2, S["dur"] + 1, s_grids)])

def scene_close(cv, t, S, T):
    B = Beat(S)
    a1 = 1 - eio(pr(t, B.end(0) + .6, B.end(0) + 1.6))
    if a1 > .01:
        rng = np.random.default_rng(3)
        counts = [0 if i == 11 else int(rng.integers(3, 12)) for i in range(26)]
        cv.cam = Cam(960, 540, lerp(1.0, 1.07, eio(pr(t, 0, B.end(0)))))
        alpha_strip(cv, 960, 470, a1, t, "L", counts, ring=pr(t, 2, 3), tile=66, bar=20)
        cv.cam = Cam()
    a2 = eo(pr(t, B.end(0) + 1.2, B.end(0) + 2.2)) * (1 - eio(pr(t, S["dur"] - 1.0, S["dur"])))
    if a2 > .01:
        # end card: wordmark + tagline, room for end-screen elements (subscribe left, video right)
        cv.text(960, 250, "LATOON", 96, INK, a2, "Black")
        cv.line([(960 - 220 * a2, 320), (960 + 220 * a2, 320)], OX, 3, a2)
        cv.text(960, 365, "Voyaging the Unseen", 34, INK2, a2, "SemiBold")
        # faint rotor illustration at the bottom
        cv.done()
        for k, x in enumerate([760, 960, 1160]):
            rotor_band(cv, x, 900, 150, 200, (t * .8 + k * 5) if k == 2 else k * 7, a2 * .35)
