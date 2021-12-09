import math


class Bogenschnitt:

    def __init__(self):

        pass

    def berechnen(self, p_p1y, p_p1x, p_p2y, p_p2x, p_s1N, p_s2N, p_s12):

        # Maßstab
        s12_berechnet = math.sqrt((p_p2y - p_p1y) ** 2 + (p_p2x - p_p1x) ** 2)
        m = s12_berechnet / p_s12
        print(m)

        # Anzahl möglicher Schnittpunkte
        if p_s1N + p_s2N < p_s12:
            return "keine Lösung"

        # Berechnung der Schnittpunkte
        p = (s12_berechnet ** 2 + p_s1N ** 2 - p_s2N ** 2) / (2 * s12_berechnet)
        h = math.sqrt(p_s1N ** 2 - p ** 2)
        o = (p_p2y - p_p1y) / s12_berechnet
        a = (p_p2x - p_p1x) / s12_berechnet

        N1y = p_p1y + o * p + a * h
        N1x = p_p1x + a * p - o * h

        if p_s1N + p_s2N == p_s12:
            return "nur eine Lösung: ", N1y, N1x

        else:
            N2y = p_p1y + o*p - a*h
            N2x = p_p1x + a*p + o*h
            return "zwei Lösungen: ", N1y, N1x, N2y, N2x


if __name__ == "__main__":

    p1_y = 328.76
    p1_x = 1207.85

    p2_y = 925.04
    p2_x = 954.33

    s1 = 294.33
    s2 = 506.42
    s3 = 648.08

    bs: Bogenschnitt = Bogenschnitt()
    print(bs.berechnen(p1_y, p1_x, p2_y, p2_x, s1, s2, s3))
