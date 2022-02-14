from math import sin, cos
from grundlagen.winkel import Winkel
import grundlagen.punkt as pkt


def erste_grundaufgabe(p_p1: pkt.Punkt, p_s12: float, p_t12: float) -> pkt.Punkt:
    """Berechnet die Koordinaten eines Zielpunktes von einem Standpunkt mit dem Richtungswinkel und der Strecke.

    :param p_p1: Standpunkt
    :type p_p1: pkt.Punkt
    :param p_s12: Strecke
    :type p_s12: float
    :param p_t12: Richtungswinkel
    :type p_t12: float
    :return: Zielpunkt
    :rtype: pkt.Punkt
    """
    # Koordinaten des Standpunktes
    y1: float = p_p1.hole_y()
    x1: float = p_p1.hole_x()

    # Richtungswinkel umrechnen
    p_t12_rad = Winkel.gon2rad(p_t12)

    # Koordinaten des Zielpunktes
    y2: float = y1 + p_s12 * sin(p_t12_rad)
    x2: float = x1 + p_s12 * cos(p_t12_rad)

    return pkt.Punkt(y2, x2)
