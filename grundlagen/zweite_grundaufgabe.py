""" Zweite Grundaufgabe

"""
import math
import grundlagen.punkt as pkt

rhogon = 200.0 / math.pi


def zweitegrundaufgabe(p_p1: pkt.Punkt, p_p2: pkt.Punkt):
    """

    :param p_p1: Koordinaten des ersten Punktes
    :type p_p1: pkt.Punkt
    :param p_p2:Koordinaten des zweiten Punktes
    :type p_p2: pkt.Punkt
    :return:
    """
    y1: float = p_p1.hole_y()
    x1: float = p_p1.hole_x()
    y2: float = p_p2.hole_y()
    x2: float = p_p2.hole_x()

    delta_y: float = y2-y1
    delta_x: float = x2-x1

    s12 = float(delta_y**2+delta_x**2)**0.5

    if delta_x == 0:        # Punkt in Ost- West-Richtung
        if delta_y == 0:    # Punkt identisch
            t12 = 0
        elif delta_y < 0:   # Punkt Richtung Westen
            t12 = 300
        elif delta_y > 0:   # Punkt Richtung Osten
            t12 = 100

    else:
        t12: float = math.atan(delta_y/delta_x)*rhogon
        if delta_x > 0:
            if delta_y < 0:
                t12 += 200
        elif delta_x < 0:
            if delta_y < 0:
                t12 += 200
        elif delta_y > 0:
            t12 += 400

    return s12, t12, delta_x, delta_y


if __name__ == "__main__":
    p1 = pkt.Punkt(528.15, 407.65)
    p2 = pkt.Punkt(795.17, 525.10)

    p3 = pkt.Punkt(16.10, 23.06)
    p4 = pkt.Punkt(12.32, 6.37)

    print(zweitegrundaufgabe(p1, p2))
    print(zweitegrundaufgabe(p3, p4))
