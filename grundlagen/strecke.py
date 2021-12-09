import grundlagen.punkt as pkt
import math
import copy
import sys


class Strecke:
    """Klasse Strecke

    """
    def __init__(self, p_pa: pkt.Punkt, p_pe: pkt.Punkt, p_nr: str = ""):
        """

        :param p_pa: Anfangspunkt
        :type p_pa: pkt.Punkt
        :param p_pe: Endpunkt
        :type p_pe: pkt.Punkt
        """
        # self.__pa: pkt.Punkt = p_pa
        # self.__pe: pkt.Punkt = p_pe

        if p_pa.hole_epsg() != p_pe.hole_epsg():
            # TODO: Fehler? Transformation?
            sys.exit(1)
        else:
            self.__epsg = p_pa.hole_epsg()

        # Tiefe kopien
        self.__pa: pkt.Punkt = copy.deepcopy(p_pa)
        self.__pe: pkt.Punkt = copy.deepcopy(p_pe)
        self.__nr: str = p_nr

    def hole_epsg(self):
        return self.__pa.hole_epsg()

    def hole_pa(self):
        return self.__pa

    def hole_pe(self):
        return self.__pe

    def setze_pa(self, p_pa: pkt.Punkt):

        if p_pa.hole_epsg() != self.__pa.hole_epsg():
            # TODO: Fehler? Transformation?
            sys.exit(1)

        self.__pa = copy.deepcopy(p_pa)

    def setze_pe(self, p_pe: pkt.Punkt):
        if p_pe.hole_epsg() != self.__pe.hole_epsg():
            # TODO: Fehler? Transformation?
            sys.exit(1)

        self.__pe = copy.deepcopy(p_pe)

    def laenge(self):
        """

        :return:
        """
        dy = self.__pe.hole_y() - self.__pa.hole_y()
        dx = self.__pe.hole_x() - self.__pa.hole_x()

        laenge: float = math.sqrt(math. pow(dy, 2) + math.pow(dx, 2))

        return laenge

    def __str__(self):
        sz: str = "Nr:" + self.__nr + " | PA: " + str(self.__pa) + " | PE: " + str(self.__pe) + " | s: " + str(self.laenge())
        return sz

    def hole_json(self) -> dict:

        json_daten: dict = {}

        for schluessel, wert in self.__dict__.items():

            if isinstance(wert, pkt.Punkt):
                json_daten[schluessel] = wert.hole_json()
            else:
                json_daten[schluessel] = wert
        return json_daten

    def setze_json(self, p_json: dict):

        for schluessel, wert in p_json.items():

            if isinstance(wert, dict):
                # Ist der Wert ein Punkt im JSON-Format?
                if schluessel == "_" + str(self.__class__.__name__) + "__pa" or schluessel == "_" + str(
                        self.__class__.__name__) + "__pe":
                    p: pkt.Punkt = pkt.Punkt()
                    p.setze_json(wert)
                    setattr(self, schluessel, p)
            else:
                setattr(self, schluessel, wert)


if __name__ == "__main__":

    pa: pkt.Punkt = pkt.Punkt()
    pe: pkt.Punkt = pkt.Punkt(10.0, 10.0)

    s: Strecke = Strecke(pa, pe)
    l1 = s.laenge()
    print(l1)

    pa.setze_y(1000.0)

    l2 = s.laenge()
    print(l2)
