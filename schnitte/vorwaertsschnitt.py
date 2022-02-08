import math
from grundlagen.winkel import rhogon
from grundlagen.zweite_grundaufgabe import zweitegrundaufgabe
import grundlagen.punkt as pkt


class Vorwaertsschnitt:
    """ Klasse Rückwärtsschnitt"""

    def __int__(self):

        pass

    @staticmethod
    def berechnen_dreieckswinkel(p_p1: pkt.Punkt, p_p2: pkt.Punkt,
                                 p_r_1n: float, p_r_12: float, p_r_2n: float, p_r_21: float):
        """Berechnet den Vorwärtsschnitt über Dreieckswinkel
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
        ergebnis: tuple = zweitegrundaufgabe(p_p1, p_p2)
        s_12: float = ergebnis[0]
        t_12: float = ergebnis[1]

        # Winkel und Richtungswinkel im Dreieck
        alpha: float = p_r_1n - p_r_12
        beta: float = p_r_21 - p_r_2n

        t_1n: float = t_12 + alpha
        t_2n: float = t_12 - beta + 200

        # Strecken im Dreieck
        s_1n: float = s_12 / (math.sin((alpha+beta)/rhogon)) * math.sin(beta/rhogon)
        # s_2n: float = s_12 / (math.sin((alpha+beta)/rhogon)) * math.sin(alpha/rhogon)

        # Koordinaten des Neupunkts
        pn_y = p_p1.hole_y() + s_1n * math.sin(t_1n/rhogon)
        pn_x = p_p1.hole_x() + s_1n * math.cos(t_1n/rhogon)

        return pkt.Punkt(pn_y, pn_x)

    @staticmethod
    def berechnen_richtungswinkel(p_p1: pkt.Punkt, p_p2: pkt.Punkt, p_p3: pkt.Punkt, p_p4: pkt.Punkt,
                                  p_r_1n: float, p_r_13: float, p_r_2n: float, p_r_24: float):
        """Berechnet den Vorwärtsschnitt über Dreieckswinkel
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
        t_12: float = zweitegrundaufgabe(p_p1, p_p2)[1]
        t_13: float = zweitegrundaufgabe(p_p1, p_p3)[1]
        t_24: float = zweitegrundaufgabe(p_p2, p_p4)[1]

        # Richtungswinkel zum Neupunkt
        t_1n: float = t_13 + (p_r_1n - p_r_13)
        t_2n: float = t_24 + (p_r_2n - p_r_24)

        # Übergabe an Berechnungsfunktion über Dreieckswinkel
        ergebnis = Vorwaertsschnitt.berechnen_dreieckswinkel(p_p1, p_p2, t_1n, t_12, t_2n, t_12+200)

        return ergebnis







# Testwerte
"""
pA = pkt.Punkt(1019.120, 3157.620)
pB = pkt.Punkt(1111.880, 3080.350)
rAN = 10.1
rAB = 74.4025
rBN = 0
rBA = 331.1513

punkt = Vorwaertsschnitt.berechnen_dreieckswinkel(pA, pB, rAN, rAB, rBN, rBA)

print("------------")
p1 = pkt.Punkt(24681.92, 90831.87)
p4 = pkt.Punkt(23231.58, 91422.92)
p2 = pkt.Punkt(24877.72, 89251.09)
p3 = pkt.Punkt(22526.65, 89150.52)

phi = 331.6174
psi = 60.7510

Vorwaertsschnitt.berechnen_richtungswinkel(p1, p2, p4, p3, phi, 0.0, psi, 0.0)
"""
