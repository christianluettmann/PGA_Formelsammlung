from math import atan
from grundlagen.winkel import rhogon
import grundlagen.punkt as pkt


def zweite_grundaufgabe(p_p1: pkt.Punkt, p_p2: pkt.Punkt) -> tuple:
    """Berechnet die Strecke und den Richtungswinkel zwischen zwei Punkten.

    :param p_p1: erster Punkt
    :type p_p1: pkt.Punkt
    :param p_p2: zweiter Punkt
    :type p_p2: pkt.Punkt
    :return: Strecke und Richtungswinkel
    :rtype: tuple
    """
    # Koordinaten der Punkte und Koordinatenunterschiede
    y1: float = p_p1.hole_y()
    x1: float = p_p1.hole_x()
    y2: float = p_p2.hole_y()
    x2: float = p_p2.hole_x()

    delta_y: float = y2 - y1
    delta_x: float = x2 - x1

    # Strecke
    s12: float = float(delta_y**2+delta_x**2)**0.5

    # Richtungswinkel
    t12: float = 0

    if delta_x == 0:            # Punkt liegt in Ost-/West-Richtung -> Teilen durch 0 im arctan!
        if delta_y == 0:        # Punkt ist identisch
            t12 = 0
        elif delta_y < 0:       # Punkt liegt in Richtung Westen
            t12 = 300
        elif delta_y > 0:       # Punkt liegt in Richtung Osten
            t12 = 100
    else:
        t12: float = atan(delta_y/delta_x)*rhogon
        if delta_x < 0:         # Punkt liegt im 2. oder 3. Quadranten
            t12 += 200
        else:
            if delta_y < 0:     # Punkt liegt im 4. Quadrant
                t12 += 400

    return s12, t12
