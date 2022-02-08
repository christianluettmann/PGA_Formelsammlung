import math
from grundlagen.winkel import rhogon


class Rueckwaertsschnitt:
    """ Klasse Rückwärtsschnitt"""

    def __int__(self):

        pass

    @staticmethod
    def berechnen(p_pa_y: float, p_pa_x: float, p_pm_y: float, p_pm_x: float, p_pb_y: float, p_pb_x: float, p_r_na: float, p_r_nm: float, p_r_nb: float):
        """Berechnet den Rückwärtsschnitt nach Cassini
        (Quelle: Formelsammlung für das Vermessungswesen (Gruber, Joeckel))

        :param p_pa_y: y-Koordinate für Punkt A
        :type p_pa_y: float
        :param p_pa_x: x-Koordinate für Punkt A
        :type p_pa_x: float
        :param p_pm_y: y-Koordinate für Punkt M
        :type p_pm_y: float
        :param p_pm_x: x-Koordinate für Punkt M
        :type p_pm_x: float
        :param p_pb_y: y-Koordinate für Punkt B
        :type p_pb_y: float
        :param p_pb_x: x-Koordinate für Punkt B
        :type p_pb_x: float
        :param p_r_na: Richtung vom Neupunkt N zu Punkt A
        :type p_r_na: float
        :param p_r_nm: Richtung vom Neupunkt N zu Punkt M
        :type p_r_nm: float
        :param p_r_nb: Richtung vom Neupunkt N zu Punkt B
        :type p_r_nb: float
        :return: Koordinaten des Neupunktes
        :rtype: tuple
        """
        # Winkel zwischen den Punkten
        alpha: float = p_r_nm - p_r_na
        beta: float = p_r_nb - p_r_nm

        # Hilfpunkt C
        pc_y: float = p_pa_y + (p_pm_x-p_pa_x) / math.tan(alpha/rhogon)
        pc_x: float = p_pa_x - (p_pm_y-p_pa_y) / math.tan(alpha/rhogon)

        # Hilfpunkt D
        pd_y: float = p_pb_y + (p_pb_x - p_pm_x) / math.tan(beta / rhogon)
        pd_x: float = p_pb_x - (p_pb_y - p_pm_y) / math.tan(beta / rhogon)

        # Richtungswinkel von C nach D
        t_cd: float = math.atan((pd_y-pc_y)/(pd_x-pc_x))
        tan_t: float = math.tan(t_cd)
        cot_t: float = 1 / tan_t

        # Neupunkt N
        pn_x: float = pc_x + (p_pm_y-pc_y+(p_pm_x-pc_x)*cot_t)/(tan_t+cot_t)
        if tan_t < cot_t:
            pn_y: float = pc_y + (pn_x-pc_x)*tan_t
        else:
            pn_y: float = p_pm_y - (pn_x-p_pm_x)*cot_t

        return pn_y, pn_x
