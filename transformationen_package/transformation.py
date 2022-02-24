import math
import urllib.request
import grundlagen.punkt as pkt
import ssl
import json
import copy
import tkinter.filedialog as tkfd


class Transformation:

    def __init__(self):
        self._pkt_list_alt: dict = {}
        self._pkt_list_neu: dict = {}
        self._pkt_list_trans: dict = {}
        self._trafo_param: dict = {}
        self.identische_punkte_alt: list = []
        self.identische_punkte_neu: list = []
        self._identische_punkte_alt_schwerpunkt: list = []
        self._identische_punkte_neu_schwerpunkt: list = []
        self.identische_punkte_neu_transformiert = []
        self._liste_restklaffen: dict = {}

    def hole_liste_alt(self) -> dict:
        """Gibt die Punktliste des Startsystems zurück.

        :return: Punktliste der Quellsystemkoordinaten
        :rtype: Dictionary
        """
        return self._pkt_list_alt

    def hole_liste_neu(self) -> dict:
        """Gibt die Punktliste des Zielsystems zurück.

        :return: Punktliste der Zielsystemkoordinaten
        :rtype: Dictionary
        """
        return self._pkt_list_neu

    def punktliste_laden_url(self, link_quellsystem: str, link_zielsystem: str) -> tuple[dict, dict]:
        """Lädt beide Punktlisten von einer URL.

        :param link_zielsystem: Daten des Zielsystem als URL
        :type link_zielsystem: str
        :param link_quellsystem: Daten des Quellsystem als URL
        :type link_quellsystem: str
        :return: Dictionaries der eingefügten Systeme
        :rtype: tuple[dict, dict]
        """
        # Umwandlung der importierten Systeme von JSON in Dictionaries
        self._pkt_list_alt = self.punktliste_einlesen_url(link_quellsystem)
        self._pkt_list_neu = self.punktliste_einlesen_url(link_zielsystem)
        return self._pkt_list_alt, self._pkt_list_neu

    def punktliste_einlesen_url(self, p_url: str = "") -> dict:
        """Liest eine Punktliste von einer URL ein.

        :param p_url: URL der JSON Datei
        :type p_url: String
        :return: Dictionary der JSON
        :rtype: Dictionary
        """
        # Einlesen der Daten in ein Dictionary

        p_pkt_list: dict = {}
        with urllib.request.urlopen(p_url, context=ssl._create_unverified_context()) as url:
            json_daten = json.loads(url.read().decode())

        for schluessel, wert in json_daten.items():
            p: pkt.Punkt = pkt.Punkt()
            p.setze_json(wert)
            # nur wenn Punktnummer und Schlüssel übereinstimmen, in die Liste
            if schluessel == p.hole_nr():
                p_pkt_list[schluessel] = p
        return p_pkt_list

    def import_json_datei(self) -> tuple[dict, dict]:
        """ Liest jeweils eine JSON-Datei als Quell und Zielsystem ein.

        :return: Tuple mit den Punkt-Dictionaries in beiden Systemen
        :rtype: tuple[dict, dict]
        """
        # Auswahl Quellsystem Datei
        dateiname: str = tkfd.askopenfilename(title="Quellsystem laden",
                                              initialdir="./Daten_Import",
                                              defaultextension=".json",
                                              filetypes=(('JSON-Dateien', '*.json'), ('Alle Dateien', '*.*')))

        p_pkt_list: dict = {}
        with open(dateiname) as json_datei:
            datei_quellsystem: dict = json.load(json_datei)
            for schluessel, wert in datei_quellsystem.items():
                p: pkt.Punkt = pkt.Punkt()
                p.setze_json(wert)
                # nur wenn Punktnummer und Schlüssel übereinstimmen, in die Liste
                if schluessel == p.hole_nr():
                    p_pkt_list[schluessel] = p
            self._pkt_list_alt = p_pkt_list

        # Auswahl Zielsystem Datei
        p_pkt_list: dict = {}
        dateiname: str = tkfd.askopenfilename(title="Zielsystem laden",
                                              initialdir="./Daten_Import",
                                              defaultextension=".json",
                                              filetypes=(('JSON-Dateien', '*.json'), ('Alle Dateien', '*.*')))

        with open(dateiname) as json_datei:
            datei_zielsystem: dict = json.load(json_datei)
            for schluessel, wert in datei_zielsystem.items():
                p: pkt.Punkt = pkt.Punkt()
                p.setze_json(wert)
                # nur wenn Punktnummer und Schlüssel übereinstimmen, in die Liste
                if schluessel == p.hole_nr():
                    p_pkt_list[schluessel] = p
            self._pkt_list_neu = p_pkt_list

            ausgabe = (self._pkt_list_alt, self._pkt_list_neu)
            return ausgabe

    def schwerpunktbezogene_koordinaten(self) -> None:
        """Berechnet die schwerpunktbezogenen Koordinaten der identischen Punkte.

        :return: None
        :rtype: None
        """
        # Passpunkte bestimmen
        self.identische_punkte_alt = []
        self.identische_punkte_neu = []
        for punkt_ziel in self._pkt_list_neu.keys():
            for punkt_start in self._pkt_list_alt.keys():
                if punkt_ziel == punkt_start:
                    self.identische_punkte_alt.append(self._pkt_list_alt[punkt_start])
                    self.identische_punkte_neu.append(self._pkt_list_neu[punkt_ziel])
                    continue

        # Schwerpunkt der Passpunkte berechnen
        ys_alt = 0
        xs_alt = 0
        ys_neu = 0
        xs_neu = 0

        # Quellsystem
        for punkt in self.identische_punkte_alt:
            ys_alt += punkt.hole_y()
            xs_alt += punkt.hole_x()

        ys_alt = ys_alt / len(self.identische_punkte_alt)
        xs_alt = xs_alt / len(self.identische_punkte_alt)

        self._trafo_param["ys_alt"] = ys_alt
        self._trafo_param["xs_alt"] = xs_alt

        # Zielsystem
        for punkt in self.identische_punkte_neu:
            ys_neu += punkt.hole_y()
            xs_neu += punkt.hole_x()

        ys_neu = ys_neu / len(self.identische_punkte_neu)
        xs_neu = xs_neu / len(self.identische_punkte_neu)

        self._trafo_param["ys_neu"] = ys_neu
        self._trafo_param["xs_neu"] = xs_neu

        # Schwerpunktbezogene Koordinaten berechnen
        self._identische_punkte_alt_schwerpunkt = copy.deepcopy(self.identische_punkte_alt)
        self._identische_punkte_neu_schwerpunkt = copy.deepcopy(self.identische_punkte_neu)

        for punkt in self._identische_punkte_alt_schwerpunkt:
            punkt.setze_y(punkt.hole_y() - ys_alt)
            punkt.setze_x(punkt.hole_x() - xs_alt)

        for punkt in self._identische_punkte_neu_schwerpunkt:
            punkt.setze_y(punkt.hole_y() - ys_neu)
            punkt.setze_x(punkt.hole_x() - xs_neu)

    def restklaffen(self) -> None:
        """Berechnet die Restklaffen der Transformation und schreibt diese in eine JSON-Datei.

        :return: None
        :rtype: None
        """
        # Berechnung der Restklaffen
        for i in range(len(self.identische_punkte_alt)):
            y_soll = self.identische_punkte_neu[i].hole_y()
            y_ist = self.identische_punkte_neu_transformiert[i].hole_y()
            restklaffe_y = y_soll - y_ist
            x_soll = self.identische_punkte_neu[i].hole_x()
            x_ist = self.identische_punkte_neu_transformiert[i].hole_x()
            restklaffe_x = x_soll - x_ist
            restklaffe = restklaffe_y, restklaffe_x
            self._liste_restklaffen[self.identische_punkte_neu[i].hole_nr()] = restklaffe


class Helmerttransformation(Transformation):

    # Erstellung der Unterklasse Helmerttransformation

    def __init__(self):
        super().__init__()

    def transformationsparameter_helmert(self) -> None:
        """Berechnet die Transformationsparameter der Helmerttransformation und schreibt diese in eine JSON-Datei: y0, x0, o und a.

        :return: None
        :rtype: None
        """
        o_zaehler = 0
        a_zaehler = 0
        nenner = 0

        for i in range(len(self._identische_punkte_alt_schwerpunkt)):
            o_zaehler += self._identische_punkte_alt_schwerpunkt[i].hole_x() * self._identische_punkte_neu_schwerpunkt[i].hole_y() - self._identische_punkte_alt_schwerpunkt[i].hole_y() * self._identische_punkte_neu_schwerpunkt[i].hole_x()
            a_zaehler += self._identische_punkte_alt_schwerpunkt[i].hole_x() * self._identische_punkte_neu_schwerpunkt[i].hole_x() + self._identische_punkte_alt_schwerpunkt[i].hole_y() * self._identische_punkte_neu_schwerpunkt[i].hole_y()
            nenner += self._identische_punkte_alt_schwerpunkt[i].hole_x() ** 2 + self._identische_punkte_alt_schwerpunkt[i].hole_y() ** 2

        self._trafo_param["o"] = o_zaehler / nenner
        self._trafo_param["a"] = a_zaehler / nenner

        self._trafo_param["y0"] = self._trafo_param["ys_neu"] - self._trafo_param["a"] * self._trafo_param["ys_alt"] - self._trafo_param["o"] * self._trafo_param["xs_alt"]
        self._trafo_param["x0"] = self._trafo_param["xs_neu"] - self._trafo_param["a"] * self._trafo_param["xs_alt"] + self._trafo_param["o"] * self._trafo_param["ys_alt"]

        self._trafo_param["m"] = math.sqrt(self._trafo_param["a"] ** 2 + self._trafo_param["o"] ** 2)
        self._trafo_param["e"] = math.atan(self._trafo_param["o"] / self._trafo_param["a"]) * 200 / math.pi

    def transformation_helmert(self) -> None:
        """Transformiert die Punkte in das Zielsystem und schreibt diese in eine JSON-Datei.

        :return: None
        :rtype: None
        """
        # Transformation der Koordinaten in das Zielsystem
        for punkt in self._pkt_list_alt.values():
            nr_trans = punkt.hole_nr()
            y_trans = self._trafo_param["y0"] + self._trafo_param["a"] * punkt.hole_y() + self._trafo_param["o"] * punkt.hole_x()
            x_trans = self._trafo_param["x0"] + self._trafo_param["a"] * punkt.hole_x() - self._trafo_param["o"] * punkt.hole_y()

            self._pkt_list_trans[nr_trans] = pkt.Punkt(y_trans, x_trans, nr_trans)

        for schluessel, wert in self._pkt_list_trans.items():
            # Einfügen der transformierten Passpunkte für die Restklaffenberechnung
            if schluessel in self.hole_liste_neu():
                self.identische_punkte_neu_transformiert.append(wert)


class Affintransformation(Transformation):

    def __init__(self):
        super().__init__()

    def transformationsparameter_affin(self) -> None:
        """Berechnet die Transformationsparameter der Helmerttransformation und schreibt diese in eine JSON-Datei:
        y0, x0, a1, a2, a3 und a4.

        :return: None
        :rtype: None
        """
        # Berechnung der Summen
        summe_y_quell_m_y_quell = 0
        summe_x_quell_m_x_quell = 0
        summe_y_quell_m_x_quell = 0
        summe_x_quell_m_x_ziel = 0
        summe_y_quell_m_x_ziel = 0
        summe_y_quell_m_y_ziel = 0
        summe_x_quell_m_y_ziel = 0

        for i in range(len(self.identische_punkte_alt)):
            y_quell_reduktion_schwerpunkt = self._identische_punkte_alt_schwerpunkt[i].hole_y()
            x_quell_reduktion_schwerpunkt = self._identische_punkte_alt_schwerpunkt[i].hole_x()
            y_ziel_reduktion_schwerpunkt = self._identische_punkte_neu_schwerpunkt[i].hole_y()
            x_ziel_reduktion_schwerpunkt = self._identische_punkte_neu_schwerpunkt[i].hole_x()

            summe_y_quell_m_y_quell += y_quell_reduktion_schwerpunkt * y_quell_reduktion_schwerpunkt
            summe_x_quell_m_x_quell += x_quell_reduktion_schwerpunkt * x_quell_reduktion_schwerpunkt
            summe_y_quell_m_x_quell += y_quell_reduktion_schwerpunkt * x_quell_reduktion_schwerpunkt
            summe_x_quell_m_x_ziel += x_quell_reduktion_schwerpunkt * x_ziel_reduktion_schwerpunkt
            summe_y_quell_m_x_ziel += y_quell_reduktion_schwerpunkt * x_ziel_reduktion_schwerpunkt
            summe_y_quell_m_y_ziel += y_quell_reduktion_schwerpunkt * y_ziel_reduktion_schwerpunkt
            summe_x_quell_m_y_ziel += x_quell_reduktion_schwerpunkt * y_ziel_reduktion_schwerpunkt

        n = (summe_x_quell_m_x_quell * summe_y_quell_m_y_quell) - summe_y_quell_m_x_quell**2

        # Berechnung der Transformationsparameter y0, x0, a1, a2, a3 und a4
        self._trafo_param["a1"] = (summe_x_quell_m_x_ziel * summe_y_quell_m_y_quell - summe_y_quell_m_x_ziel * summe_y_quell_m_x_quell) / n
        self._trafo_param["a2"] = (summe_x_quell_m_x_ziel * summe_y_quell_m_x_quell - summe_y_quell_m_x_ziel * summe_x_quell_m_x_quell) / n
        self._trafo_param["a3"] = (summe_y_quell_m_y_ziel * summe_x_quell_m_x_quell - summe_x_quell_m_y_ziel * summe_y_quell_m_x_quell) / n
        self._trafo_param["a4"] = (summe_x_quell_m_y_ziel * summe_y_quell_m_y_quell - summe_y_quell_m_y_ziel * summe_y_quell_m_x_quell) / n

        self._trafo_param["y0"] = self._trafo_param["ys_neu"] - self._trafo_param["a3"] * self._trafo_param["ys_alt"] - self._trafo_param["a4"] * self._trafo_param["xs_alt"]
        self._trafo_param["x0"] = self._trafo_param["xs_neu"] - self._trafo_param["a1"] * self._trafo_param["xs_alt"] + self._trafo_param["a2"] * self._trafo_param["ys_alt"]

    def transformation_affin(self) -> None:
        """Transformiert die Punkte in das Zielsystem und schreibt diese in eine JSON-Datei.

        :return: None
        :rtype: None
        """
        # Transformation der Punkte in das Zielsystem nach der Affintransformation
        for punkt in self._pkt_list_alt.values():
            nr_trans = punkt.hole_nr()
            y_trans = self._trafo_param["y0"] + self._trafo_param["a3"] * punkt.hole_y() + self._trafo_param["a4"] * punkt.hole_x()
            x_trans = self._trafo_param["x0"] + self._trafo_param["a1"] * punkt.hole_x() - self._trafo_param["a2"] * punkt.hole_y()

            self._pkt_list_trans[nr_trans] = pkt.Punkt(y_trans, x_trans, nr_trans)

        # Punktliste speichern
        self.identische_punkte_neu_transformiert = []
        for schluessel, wert in self._pkt_list_trans.items():
            if schluessel in self.hole_liste_neu():
                self.identische_punkte_neu_transformiert.append(wert)


if __name__ == "__main__":

    """trafo = Helmerttransformation()
    #trafo.import_json_datei()
    trafo.punktliste_laden_url("https://py.kartographie.net/trans_alt.json", "https://py.kartographie.net/trans_neu.json")
    trafo.schwerpunktbezogene_koordinaten()
    trafo.transformationsparameter_helmert()
    trafo.transformation_helmert()
    trafo.restklaffen()"""

    trafo = Affintransformation()
    trafo.punktliste_laden_url("https://py.kartographie.net/trans_alt.json", "https://py.kartographie.net/trans_neu.json")
    trafo.schwerpunktbezogene_koordinaten()
    trafo.transformationsparameter_affin()
    trafo.transformation_affin()
    trafo.restklaffen()
