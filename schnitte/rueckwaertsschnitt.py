from math import tan, atan
from grundlagen.winkel import Winkel
import grundlagen.punkt as pkt


class Rueckwaertsschnitt:

    @staticmethod
    def berechnen(p_pa: pkt.Punkt, p_pm: pkt.Punkt, p_pb: pkt.Punkt,
                  p_r_na: float, p_r_nm: float, p_r_nb: float) -> pkt.Punkt:
        """Berechnet den Rückwärtsschnitt nach Cassini. ACHTUNG: Die Punkte müssen im Uhrzeigersinn übergeben werden!
        (Gruber, Joeckel: Formelsammlung für das Vermessungswesen, 18. Auflage, S. 87)

        :param p_pa: linker Punkt
        :type p_pa: pkt.Punkt
        :param p_pm: mittlerer Punkt
        :type p_pm: pkt.Punkt
        :param p_pb: rechter Punkt
        :type p_pb: pkt.Punkt
        :param p_r_na: Richtung vom Neupunkt N zum linken Punkt A
        :type p_r_na: float
        :param p_r_nm: Richtung vom Neupunkt N zum mittleren Punkt M
        :type p_r_nm: float
        :param p_r_nb: Richtung vom Neupunkt N zum rechten Punkt B
        :type p_r_nb: float
        :return: Neupunkt N
        :rtype: pkt.Punkt
        """
        # Koordinaten der Punkte
        pa_y: float = p_pa.hole_y()
        pa_x: float = p_pa.hole_x()
        pm_y: float = p_pm.hole_y()
        pm_x: float = p_pm.hole_x()
        pb_y: float = p_pb.hole_y()
        pb_x: float = p_pb.hole_x()

        # Winkel zwischen den Punkten
        alpha: float = p_r_nm - p_r_na
        beta: float = p_r_nb - p_r_nm

        # Hilfpunkt C
        pc_y: float = pa_y + (pm_x-pa_x) / tan(Winkel.gon2rad(alpha))
        pc_x: float = pa_x - (pm_y-pa_y) / tan(Winkel.gon2rad(alpha))

        # Hilfpunkt D
        pd_y: float = pb_y + (pb_x-pm_x) / tan(Winkel.gon2rad(beta))
        pd_x: float = pb_x - (pb_y-pm_y) / tan(Winkel.gon2rad(beta))

        # Richtungswinkel von C nach D
        t_cd: float = atan((pd_y-pc_y)/(pd_x-pc_x))
        tan_t: float = tan(t_cd)
        cot_t: float = 1 / tan_t

        # Neupunkt N
        pn_x: float = pc_x + (pm_y - pc_y + (pm_x-pc_x) * cot_t) / (tan_t+cot_t)
        if tan_t < cot_t:
            pn_y: float = pc_y + (pn_x-pc_x)*tan_t
        else:
            pn_y: float = pm_y - (pn_x-pm_x) * cot_t

        return pkt.Punkt(pn_y, pn_x)
