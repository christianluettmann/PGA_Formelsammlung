import grundlagen.punkt as pkt
import math
import copy
import sys


class Strecke:

    def __init__(self, p_pa: pkt.Punkt, p_pe: pkt.Punkt, p_nr: str = ""):
        """Primärer Konstruktor
        :param p_pa: Anfangspunkt
        :type p_pa: pkt.Punkt
        :param p_pe: Endpunkt
        :type p_pe: pkt.Punkt
        :param p_nr: optionale Streckennummer
        :type p_nr: str
        """
        if p_pa.hole_epsg() != p_pe.hole_epsg():
            # TODO: Fehler? Transformation?
            sys.exit(1)
        else:
            self.__epsg = p_pa.hole_epsg()

        # Tiefe kopien
        self.__pa: pkt.Punkt = copy.deepcopy(p_pa)
        self.__pe: pkt.Punkt = copy.deepcopy(p_pe)
        self.__nr: str = p_nr

    @classmethod
    def init_koordinaten(cls, p_y1: float, p_x1: float, p_y2: float, p_x2: float, p_nr: str = ""):
        """Alternativer Konstruktor "Koordinaten"

        :param p_y1: y-Koordinate des ersten Punktes
        :type p_y1: float
        :param p_x1: x-Koordinate des ersten Punktes
        :type p_x1: float
        :param p_y2: y-Koordinate des zweiten Punktes
        :type p_y2: float
        :param p_x2: x-Koordinate des zweiten Punktes
        :type p_x2: float
        :param p_nr: optionale Streckennummer
        :type p_nr: str
        :return: Strecke aus den Koordinaten
        :rtype: Strecke
        """
        pa: pkt.Punkt = pkt.Punkt(p_y1, p_x1)
        pe: pkt.Punkt = pkt.Punkt(p_y2, p_x2)
        # Objekt der Klasse Strecke mit Hilfe des primären Konstruktors anlegen und zurückgeben
        return cls(pa, pe, p_nr)

    @classmethod
    def init_ortsvektor(cls, p_pe, p_nr: str = ""):
        """Alternativer Konstruktor "Ortsvektor"

        :param p_pe: Endpunkt
        :type p_pe: pkt.Punkt
        :param p_nr: optionale Streckennummer
        :type p_nr: str
        :return: Strecke als Ortsvektor
        :rtype: Strecke
        """
        pa: pkt.Punkt = pkt.Punkt(0.0, 0.0)
        return cls(pa, p_pe, p_nr)

    @classmethod
    def init_leerstrecke(cls, p_nr: str = ""):
        """Alternativer Konstruktor "Leere Strecke"

        :param p_nr: optionale Streckennummer
        :type p_nr: str
        :return: Strecke
        :rtype: Strecke
        """
        pa: pkt.Punkt = pkt.Punkt(0.0, 0.0)
        pe: pkt.Punkt = pkt.Punkt(0.0, 0.0)
        return cls(pa, pe, p_nr)

    def hole_epsg(self) -> int:
        """Getter für EPSG-Code.

        :return: EPSG-Code
        :rtype: int
        """
        return self.__pa.hole_epsg()

    def hole_pa(self) -> pkt.Punkt:
        """Getter für Anfangspunkt.

        :return: Anfangspunkt
        :rtype: pkt.Punkt
        """
        return self.__pa

    def hole_pe(self) -> pkt.Punkt:
        """Getter für Endpunkt.

        :return: Endpunkt
        :rtype: pkt.Punkt
        """
        return self.__pe

    def setze_pa(self, p_pa: pkt.Punkt) -> None:
        """Setter für Anfangspunkt.

        :param p_pa: Anfangspunkt
        :type p_pa: pkt.Punkt
        :return: None
        :rtype: None
        """
        if p_pa.hole_epsg() != self.__pa.hole_epsg():
            # TODO: Fehler? Transformation?
            sys.exit(1)

        self.__pa: pkt.Punkt = copy.deepcopy(p_pa)

    def setze_pe(self, p_pe: pkt.Punkt) -> None:
        """Setter für Endpunkt.

        :param p_pe: Endpunkt
        :type p_pe: pkt.Punkt
        :return: None
        :rtype: None
        """
        if p_pe.hole_epsg() != self.__pe.hole_epsg():
            # TODO: Fehler? Transformation?
            sys.exit(1)

        self.__pe: pkt.Punkt = copy.deepcopy(p_pe)

    def laenge(self) -> float:
        """Gibt die Länge der Strecke zurück.

        :return: Länge der Strecke
        :rtype: float
        """
        dy: float = self.__pe.hole_y() - self.__pa.hole_y()
        dx: float = self.__pe.hole_x() - self.__pa.hole_x()

        laenge: float = math.sqrt(math. pow(dy, 2) + math.pow(dx, 2))

        return laenge

    def __str__(self):
        """ Gibt eine Beschreibung der Strecke zurück.

        :return: Beschreibung der Strecke
        :rtype: str
        """
        sz: str = "Nr:" + self.__nr + " | PA: " + str(self.__pa) + " | PE: " + str(self.__pe) + " | s: " + str(self.laenge())
        return sz

    def hole_json(self) -> dict:
        """Gibt die Stecke als JSON/Dictionary zurück.

        :return: JSON/Dictionary
        :rtype: dict
        """
        json_daten: dict = {}

        for schluessel, wert in self.__dict__.items():

            if isinstance(wert, pkt.Punkt):
                json_daten[schluessel] = wert.hole_json()
            else:
                json_daten[schluessel] = wert
        return json_daten

    def setze_json(self, p_json: dict) -> None:
        """Setzt die Attribute einer Strecke mit den Werten des Dictionaries.

        :param p_json: JSON/Dictionary
        :type p_json: dict
        :return: None
        :rtype: None
        """
        for schluessel, wert in p_json.items():

            if isinstance(wert, dict):
                # Ist der Wert ein Punkt im JSON-Format?
                if schluessel == "_" + str(self.__class__.__name__) + "__pa" \
                        or schluessel == "_" + str(self.__class__.__name__) + "__pe":
                    p: pkt.Punkt = pkt.Punkt()
                    p.setze_json(wert)
                    setattr(self, schluessel, p)
            else:
                setattr(self, schluessel, wert)
