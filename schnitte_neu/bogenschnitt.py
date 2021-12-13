import math


class Bogenschnitt:
    """ Klasse Bogenschnitt"""

    def __int__(self):

        pass

    @staticmethod
    def berechnen(p_p1_y, p_p1_x, p_s1, p_p2_y, p_p2_x, p_s2):

        s3_b = (((p_p1_y - p_p2_y) ** 2) + ((p_p1_x - p_p2_x) ** 2)) ** 0.5

        if p_s1 + p_s2 > s3_b:
            print("zwei Lösungen")
            p = (s3_b**2 + p_s1**2 - p_s2**2) / (2 * s3_b)
            h = math.sqrt((p_s1**2) - (p**2))

            o = (p_p2_y - p_p1_y) / s3_b
            a = (p_p2_x - p_p1_x) / s3_b

            pn1_y = p_p1_y + o * p + a * h
            pn1_x = p_p1_x + a * p - o * h

            pn2_y = p_p1_y + o * p - a * h
            pn2_x = p_p1_x + a * p + o * h

        if p_s1 + p_s2 < s3_b:
            print("keine Lösung")

        if p_s1 + p_s2 == s3_b:
            print("schlechter Schnitt")
            p = (s3_b**2 + p_s1**2 - p_s2**2) / (2 * s3_b)
            h = math.sqrt((p_s1 ** 2) - (p ** 2))

            o = (p_p2_y - p_p1_y) / s3_b
            a = (p_p2_x - p_p1_x) / s3_b

            pn1_y = p_p1_y + o * p + a * h
            pn1_x = p_p1_x + a * p - o * h

        return pn1_y, pn1_x, pn2_y, pn2_x


if __name__ == "__main__":

    p1_y = 328.76
    p1_x = 1207.85
    s1 = 294.33

    p2_y = 925.04
    p2_x = 954.33
    s2 = 506.42

    s3 = 648.08

    bs: Bogenschnitt = Bogenschnitt()
    print(bs.berechnen(p1_y, p1_x, s1, p2_y, p2_x, s2))
