import grundlagen.punkt as pkt
import math
from grundlagen.winkel import rhogon


def zweitegrundaufgabe(p_p1: pkt.Punkt, p_p2: pkt.Punkt):
    """Zweite geodätische Grundaufgabe:
    Berechnet aus zwei Punkten die Strecke und den Richtungswinkel.

    :param p_p1: erster Punkt
    :type p_p1: pkt.Punkt
    :param p_p2: zweiter Punkt
    :type p_p2: pkt.Punkt
    :return: Strecke und Richtungswinkel
    :rtype: tuple
    """
    y1: float = p_p1.hole_y()
    x1: float = p_p1.hole_x()
    y2: float = p_p2.hole_y()
    x2: float = p_p2.hole_x()

    delta_y: float = y2-y1
    delta_x: float = x2-x1

    s12: float = (delta_y**2+delta_x**2)**0.5
    t12: float = 0

    if delta_x == 0:  # Punkt in Ost-West-Richtung
        if delta_y == 0:  # Punkt identisch
            t12 = 0
        elif delta_y < 0:  # Punkt Richtung Westen
            t12 = 300
        elif delta_y > 0:  # Punkt Richtung Osten
            t12 = 100
    else:
        t12: float = math.atan(delta_y / delta_x) * rhogon
        if delta_x > 0:
            if delta_y < 0:
                t12 += 400  # Punkt im 4. Quadranten
        elif delta_x < 0:
            t12 += 200  # Punkt im 2. oder 3. Quadranten

    return s12, t12


# Testausgaben


if __name__ == "__main__":
    p1 = pkt.Punkt(528.15, 407.65)
    p2 = pkt.Punkt(795.17, 525.10)

    p3 = pkt.Punkt(16.10, 23.06)
    p4 = pkt.Punkt(12.32, 6.37)

    p10 = pkt.Punkt(1, 1)
    p11 = pkt.Punkt(1, 2)
    p12 = pkt.Punkt(2, 2)
    p13 = pkt.Punkt(2, 1)
    p14 = pkt.Punkt(2, 0)
    p15 = pkt.Punkt(1, 0)
    p16 = pkt.Punkt(0, 0)
    p17 = pkt.Punkt(0, 1)
    p18 = pkt.Punkt(0, 2)
    p19 = pkt.Punkt(1, 1)

    print(zweitegrundaufgabe(p1, p2))
    print(zweitegrundaufgabe(p3, p4))
    print(zweitegrundaufgabe(p10, p11))
    print(zweitegrundaufgabe(p10, p12))
    print(zweitegrundaufgabe(p10, p13))
    print(zweitegrundaufgabe(p10, p14))
    print(zweitegrundaufgabe(p10, p15))
    print(zweitegrundaufgabe(p10, p16))
    print(zweitegrundaufgabe(p10, p17))
    print(zweitegrundaufgabe(p10, p18))
    print(zweitegrundaufgabe(p10, p19))
