from math import sqrt
import grundlagen.punkt as pkt


class Bogenschnitt:

    @staticmethod
    def berechnen(p_p1: pkt.Punkt, p_s1: float, p_p2: pkt.Punkt, p_s2: float, p_s3: float = 0) -> tuple:
        """Berechnet den Bogenschnitt von zwei Punkten. Wenn die Strecke zwischen den bekannten Punkten
        gemessen wurde (=/= 0) wird ein Maßstab berücksichtigt.
        (Gruber, Joeckel: Formelsammlung für das Vermessungswesen, 18. Auflage, S. 84)

        :param p_p1: erster Punkt
        :type p_p1: pkt.Punkt
        :param p_s1: Strecke zwischen dem ersten Punkt und dem Neupunkt
        :type p_s1: float
        :param p_p2: zweiter Punkt
        :type p_p2: pkt.Punkt
        :param p_s2: Strecke zwischen dem zweiten Punkt und dem Neupunkt
        :type p_s2: float
        :param p_s3: Strecke zwischen den beiden bekannten Punkten
        :type p_s3: float
        :return: Beide Neupunkte und den Maßstab
        :rtype: tuple
        """

        # Koordinaten der Punkte
        p1_y: float = p_p1.hole_y()
        p1_x: float = p_p1.hole_x()
        p2_y: float = p_p2.hole_y()
        p2_x: float = p_p2.hole_x()

        # Koordinaten der Neupunkte (auf Null setzen)
        pn1_y: float = 0
        pn1_x: float = 0
        pn2_y: float = 0
        pn2_x: float = 0

        # Maßstab berechnen und Strecken reduzieren
        s3_b: float = (((p1_y - p2_y) ** 2) + ((p1_x - p2_x) ** 2)) ** 0.5
        massstab: float = 1.0

        if p_s3 != 0:
            massstab: float = p_s3 / s3_b
            s3_b: float = p_s3
            p_s1: float = p_s1 / massstab
            p_s2: float = p_s2 / massstab

        # Zwei Lösungen
        if p_s1 + p_s2 > s3_b:
            p: float = (s3_b**2 + p_s1**2 - p_s2**2) / (2 * s3_b)
            h: float = sqrt((p_s1**2) - (p**2))

            o: float = (p2_y - p1_y) / s3_b
            a: float = (p2_x - p1_x) / s3_b

            pn1_y: float = p1_y + o * p + a * h
            pn1_x: float = p1_x + a * p - o * h
            pn1: pkt.Punkt = pkt.Punkt(pn1_y, pn1_x)

            pn2_y: float = p1_y + o * p - a * h
            pn2_x: float = p1_x + a * p + o * h
            pn2: pkt.Punkt = pkt.Punkt(pn2_y, pn2_x)

            return pn1, pn2, massstab

        # Keine Lösung
        elif p_s1 + p_s2 < s3_b:
            pn1: pkt.Punkt = pkt.Punkt(pn1_y, pn1_x)
            pn2: pkt.Punkt = pkt.Punkt(pn2_y, pn2_x)
            return pn1, pn2, massstab

        # Eine Lösung
        elif p_s1 + p_s2 == s3_b:
            p: float = (s3_b**2 + p_s1**2 - p_s2**2) / (2 * s3_b)
            h: float = sqrt((p_s1 ** 2) - (p ** 2))

            o: float = (p2_y - p1_y) / s3_b
            a: float = (p2_x - p1_x) / s3_b

            pn1_y: float = p1_y + o * p + a * h
            pn1_x: float = p1_x + a * p - o * h
            pn1: pkt.Punkt = pkt.Punkt(pn1_y, pn1_x)

            pn2: pkt.Punkt = pkt.Punkt(pn2_y, pn2_x)

            return pn1, pn2, massstab
