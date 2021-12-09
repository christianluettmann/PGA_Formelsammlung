import math
import grundlagen.winkel as wk
import grundlagen.punkt as pkt


def erstegrundaufgabe(p_p1: pkt.Punkt, p_s12: float, p_t12: float) -> pkt.Punkt:
    """
    Erste geodätische Grundaufgabe:
    Berechnet die Kordinaten eines Zielpunktes von einem Standpunkt mit dem Richtungswinkel und der Strecke.

    :param p_p1: Startpunkt
    :type p_p1: pkt.punkt
    :param p_s12: Strecke von Punkt 1 zu Punkt 2
    :type p_s12: float
    :param p_t12: Richtungswinkel von Punkt 1 zu Punkt 2
    :type p_t12: float
    :return: Zielpunkt
    :rtype: pkt.Punkt
    """
    y1: float = p_p1.hole_y()
    x1: float = p_p1.hole_x()
    delta_y: float = p_s12 * math.sin(p_t12/wk.rhogon)
    delta_x: float = p_s12 * math.cos(p_t12/wk.rhogon)
    y2: float = y1 + delta_y
    x2: float = x1 + delta_x
    return pkt.Punkt(y2, x2)


# Testdaten

if __name__ == "__main__":
    p1 = pkt.Punkt(713.64, 496.72)
    p2 = pkt.Punkt(16.10, 23.06)
    print(erstegrundaufgabe(p1, 135.25, 32.9645))  # x2 soll ...14.24
    print(erstegrundaufgabe(p2, 17.11, 214.1990))  # y2 soll 12.32
