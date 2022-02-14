from math import sin, cos
from grundlagen.winkel import rhogon
from grundlagen.zweite_grundaufgabe import zweite_grundaufgabe
import grundlagen.punkt as pkt


class Vorwaertsschnitt:

    @staticmethod
    def berechnen_dreieckswinkel(p_p1: pkt.Punkt, p_p2: pkt.Punkt,
                                 p_r_1n: float, p_r_12: float, p_r_2n: float, p_r_21: float) -> pkt.Punkt:
        """Berechnet den Vorwärtsschnitt über Dreieckswinkel.
        (Gruber, Joeckel: Formelsammlung für das Vermessungswesen, 18. Auflage, S. 85)

        :param p_p1: Punkt 1
        :type p_p1: pkt.Punkt
        :param p_p2: Punkt 2
        :type p_p2: pkt.Punkt
        :param p_r_1n: Richtung von Punkt 1 zum Neupunkt
        :type p_r_1n: float
        :param p_r_12: Richtung von Punkt 1 zu Punkt 2
        :type p_r_12: float
        :param p_r_2n: Richtung von Punkt 2 zum Neupunkt
        :type p_r_2n: float
        :param p_r_21: Richtung von Punkt 2 zu Punkt 1
        :type p_r_21: float
        :return: Neupunkt
        :rtype: pkt.Punkt
        """
        # Strecke und Richtungswinkel zwischen Punkt 1 und Punkt 2
        s_12, t_12 = zweite_grundaufgabe(p_p1, p_p2)

        # Winkel und Richtungswinkel im Dreieck
        alpha: float = p_r_1n - p_r_12
        beta: float = p_r_21 - p_r_2n

        t_1n: float = t_12 + alpha

        # Strecken im Dreieck
        s_1n: float = s_12 / (sin((alpha+beta)/rhogon)) * sin(beta/rhogon)

        # Koordinaten des Neupunkts
        pn_y: float = p_p1.hole_y() + s_1n * sin(t_1n/rhogon)
        pn_x: float = p_p1.hole_x() + s_1n * cos(t_1n/rhogon)

        return pkt.Punkt(pn_y, pn_x)

    @staticmethod
    def berechnen_richtungswinkel(p_p1: pkt.Punkt, p_p2: pkt.Punkt, p_p3: pkt.Punkt, p_p4: pkt.Punkt,
                                  p_r_1n: float, p_r_13: float, p_r_2n: float, p_r_24: float) -> pkt.Punkt:
        """Berechnet den Vorwärtsschnitt über Dreieckswinkel.
        (Gruber, Joeckel: Formelsammlung für das Vermessungswesen, 18. Auflage, S. 86)

        :param p_p1: Punkt 1
        :type p_p1: pkt.Punkt
        :param p_p2: Punkt 2
        :type p_p2: pkt.Punkt
        :param p_p3: Punkt 3
        :type p_p3: pkt.Punkt
        :param p_p4: Punkt 4
        :type p_p4: pkt.Punkt
        :param p_r_1n: Richtung von Punkt 1 zum Neupunkt
        :type p_r_1n: float
        :param p_r_13: Richtung von Punkt 1 zu Punkt 3
        :type p_r_13: float
        :param p_r_2n: Richtung von Punkt 2 zum Neupunkt
        :type p_r_2n: float
        :param p_r_24: Richtung von Punkt 2 zu Punkt 4
        :type p_r_24: float
        :return: Neupunkt
        :rtype: pkt.Punkt
        """
        # Strecke und Richtungswinkel zwischen Punkt 1 und Punkt 2
        t_12: float = zweite_grundaufgabe(p_p1, p_p2)[1]
        t_13: float = zweite_grundaufgabe(p_p1, p_p3)[1]
        t_24: float = zweite_grundaufgabe(p_p2, p_p4)[1]

        # Richtungswinkel zum Neupunkt
        t_1n: float = t_13 + (p_r_1n - p_r_13)
        t_2n: float = t_24 + (p_r_2n - p_r_24)

        # Übergabe an Berechnungsfunktion über Dreieckswinkel
        ergebnis: pkt.Punkt = Vorwaertsschnitt.berechnen_dreieckswinkel(p_p1, p_p2, t_1n, t_12, t_2n, t_12+200)

        return ergebnis
