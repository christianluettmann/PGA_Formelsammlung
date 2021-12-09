"""Erste geodätische Grundaufgabe

"""
from math import *
import Grundlagen.Punkt as pkt


def erstegrundaufgabe(p_p1: pkt.Punkt, p_s12: float, p_t12: float) -> pkt.Punkt:
    """
    Berechnet die Koordinaten eines Zielpunktes von einem Standpunkt mit dem Richtungswinkel und der Strecke.

    :param p_p1: Koordinate
    :type p_p1: pkt.Punkt
    :param p_s12: Strecke
    :type p_s12: float
    :param p_t12: Richtungswinkel
    :type p_t12: float
    :return Zielpunkt
    :rtype pkt.Punkt
    """

    y1: float = p_p1.hole_y()
    x1: float = p_p1.hole_x()
    p_t12_rad = p_t12 /200 *pi
    y2 = y1 + p_s12 * sin(p_t12_rad)
    x2 = x1 + p_s12 * cos(p_t12_rad)
    return pkt.Punkt(y2, x2)


if __name__ == "__main__":
    p1 = pkt.Punkt(713.64, 496.72)
    p2 = pkt.Punkt (16.10, 23.06)
    print(erstegrundaufgabe(p1, 135.25, 32.9645))
    print(erstegrundaufgabe(p2, 17.11, 214.1990))
