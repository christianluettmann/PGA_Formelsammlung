import json
import grundlagen.punkt as pkt
import math
import copy
from grundlagen.winkel import rhogon
import sys


class Strecke:
    """Klasse Strecke

    """
    def __init__(self, p_pa: pkt.Punkt, p_pe: pkt.Punkt, p_nr: str = ""):
        """
        TODO: gleiche EPSG-Codes
        """
        if p_pa.hole_epsg() != p_pe.hole_epsg():
            # TODO: Fehler oder Transformation?
            sys.exit(1)

        # Tiefe Kopien
        self.__pa: pkt.Punkt = copy.deepcopy(p_pa)
        self.__pe: pkt.Punkt = copy.deepcopy(p_pe)
        self.__nr: str = p_nr

    def hole_epsg(self):
        return self.__pa.hole_epsg()

    def hole_nr(self):
        return self.__nr

    def hole_pa(self):
        return self.__pa

    def hole_pe(self):
        return self.__pe

    def setze_nr(self, p_nr: str):
        self.__nr = p_nr

    def setze_pa(self, p_pa: pkt.Punkt):

        if p_pa.hole_epsg() != self.__pa.hole_epsg():
            # TODO: Fehler oder Transformation?
            sys.exit(1)
        self.__pa = copy.deepcopy(p_pa)

    def setze_pe(self, p_pe: pkt.Punkt):
        if p_pe.hole_epsg() != self.__pe.hole_epsg():
            # TODO: Fehler oder Transformation?
            sys.exit(1)
        self.__pe = copy.deepcopy(p_pe)

    def laenge(self):
        """

        :return:
        """
        delta_y = self.__pe.hole_y() - self.__pa.hole_y()
        delta_x = self.__pe.hole_x() - self.__pa.hole_x()

        laenge: float = math.sqrt((math.pow(delta_y, 2)+math.pow(delta_x, 2)))

        return laenge

    def riwi(self):

        delta_y = self.__pe.hole_y() - self.__pa.hole_y()
        delta_x = self.__pe.hole_x() - self.__pa.hole_x()

        t12 = 0
        if delta_x == 0:  # Punkt in Ost-West-Richtung
            if delta_y == 0:  # Punkt identisch
                t12 = 0
            elif delta_y < 0:  # Punkt Richtung Westen
                t12 = 300
            elif delta_y > 0:  # Punkt Richtung Osten
                t12 = 100
        else:
            t12: float = math.atan(delta_y / delta_x) * rhogon
            if delta_x > 0:
                if delta_y < 0:
                    t12 += 400  # Punkt im 4. Quadranten
            elif delta_x < 0:
                t12 += 200  # Punkt im 2. oder 3. Quadranten
        return t12

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
                # Test: Ist Wert ein Punkt im JSON-Format?
                if schluessel == f"_{str(self.__class__.__name__)}__pa" or schluessel == f"_{str(self.__class__.__name__)}__pe":
                    p: pkt.Punkt = pkt.Punkt()
                    p.setze_json(wert)
                    setattr(self, schluessel, p)
            else:
                setattr(self, schluessel, wert)

    def __str__(self):
        return f"Steckennummer:{self.hole_nr()} Anfangspunkt:{self.__pa.hole_nr()} Endpunkt:{self.__pe.hole_nr()} Länge:{round(self.laenge(),2)}m Richtung:{round(self.riwi(),4)}gon"


if __name__ == "__main__":
    p1 = pkt.Punkt(0, 0, "A")
    p2 = pkt.Punkt(10, 5, "B")

    s = Strecke(p1, p2, "Strecke")
    l1 = s.laenge()
    print(l1)

    p1.setze_y(1000)

    l2 = s.laenge()
    print(l2)

    print(s)

    print(s.hole_json())
    print(json.dumps(s.hole_json(), indent=4))

    pa: pkt.Punkt = pkt.Punkt()
    pe: pkt.Punkt = pkt.Punkt()
    # TODO: für leere Strecke muss man noch zwei leere Punkte anlegen
    s2: Strecke = Strecke(pa, pe)
    print(s2)
    s2.setze_json(s.hole_json())
    print(s2)
