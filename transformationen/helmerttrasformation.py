import math
import urllib.request
import grundlagen.punkt as pkt
import ssl
import json


class Helmerttransformation:

    def __init__(self):
        self.__pkt_list_alt: dict = {}
        self.__pkt_list_neu: dict = {}
        self.__pkt_list_trans: dict = {}
        self.__trafo_param: dict = {"o": 0, "a": 0, "y0": 0, "x0": 0, "m": 0, "e": 0}

    def hole_liste_alt(self):
        return self.__pkt_list_alt

    def hole_liste_neu(self):
        return self.__pkt_list_neu

    def punktliste_laden(self):
        url_alt: str = "https://py.kartographie.net/trans_alt.json"
        url_neu: str = "https://py.kartographie.net/trans_neu.json"

        self.__pkt_list_alt = self.punktliste_einlesen_url(url_alt)
        self.__pkt_list_neu = self.punktliste_einlesen_url(url_neu)

        # Testausgabe
        print(self.__pkt_list_alt)
        for schluessel, wert in self.__pkt_list_alt.items():
            print(schluessel + " : " + str(wert))
        print(self.__pkt_list_neu)
        for schluessel, wert in self.__pkt_list_neu.items():
            print(schluessel + " : " + str(wert))

    def punktliste_einlesen_url(self, p_url: str = ""):
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

    def transformationsparameter(self):

        # Passpunkte bestimmen

        print("Start der Berechnung:")
        identische_punkte_alt = []
        identische_punkte_neu = []
        for punkt_ziel in self.__pkt_list_neu.keys():
            for punkt_start in self.__pkt_list_alt.keys():
                if punkt_ziel == punkt_start:
                    identische_punkte_alt.append(self.__pkt_list_alt[punkt_start])
                    identische_punkte_neu.append(self.__pkt_list_neu[punkt_ziel])
                    continue

        print(identische_punkte_alt)
        print(identische_punkte_neu)
        print("-----------------------")

        # Schwerpunkt der Passpunkte berechnen

        ys_alt = 0
        xs_alt = 0
        ys_neu = 0
        xs_neu = 0

        for punkt in identische_punkte_alt:
            ys_alt += punkt.hole_y()
            xs_alt += punkt.hole_x()

        ys_alt = ys_alt / len(identische_punkte_alt)
        xs_alt = xs_alt / len(identische_punkte_alt)

        for punkt in identische_punkte_neu:
            ys_neu += punkt.hole_y()
            xs_neu += punkt.hole_x()

        ys_neu = ys_neu / len(identische_punkte_neu)
        xs_neu = xs_neu / len(identische_punkte_neu)

        print(ys_alt)
        print(xs_alt)
        print(ys_neu)
        print(xs_neu)
        print("----------------")

        # Schwerpunktbezogene Koordinaten berechnen

        for punkt in identische_punkte_alt:
            punkt.setze_y(punkt.hole_y() - ys_alt)
            punkt.setze_x(punkt.hole_x() - xs_alt)

        for punkt in identische_punkte_neu:
            punkt.setze_y(punkt.hole_y() - ys_neu)
            punkt.setze_x(punkt.hole_x() - xs_neu)

        for i in range(len(identische_punkte_alt)):
            print(str(identische_punkte_alt[i]))
            print(str(identische_punkte_neu[i]))
        print("-----------------------")

        # Parameter o, a, y0 und x0 berechnen

        o_zaehler = 0
        a_zaehler = 0
        nenner = 0

        for i in range(len(identische_punkte_alt)):
            o_zaehler += identische_punkte_alt[i].hole_x() * identische_punkte_neu[i].hole_y() - identische_punkte_alt[i].hole_y() * identische_punkte_neu[i].hole_x()
            a_zaehler += identische_punkte_alt[i].hole_x() * identische_punkte_neu[i].hole_x() + identische_punkte_alt[i].hole_y() * identische_punkte_neu[i].hole_y()
            nenner += identische_punkte_alt[i].hole_x() ** 2 + identische_punkte_alt[i].hole_y() ** 2

        self.__trafo_param['o'] = o_zaehler / nenner
        self.__trafo_param["a"] = a_zaehler / nenner

        self.__trafo_param["y0"] = ys_neu - self.__trafo_param["a"]*ys_alt - self.__trafo_param["o"]*xs_alt
        self.__trafo_param["x0"] = xs_neu - self.__trafo_param["a"]*xs_alt + self.__trafo_param["o"]*ys_alt

        self.__trafo_param["m"] = math.sqrt(self.__trafo_param["a"]**2 + self.__trafo_param["o"]**2)
        self.__trafo_param["e"] = math.atan(self.__trafo_param["o"]/self.__trafo_param["a"]) * 200 / math.pi

        print(self.__trafo_param)
        print("--------------------")

        # Trafo-Parameter in JSON-Datei
        with open("trafo_parameter.json", "w") as json_datei:
            json.dump(self.__trafo_param, json_datei)


    def restklaffen(self):
        pass





    def transformation(self):
        # Transformation

        for punkt in self.__pkt_list_alt.values():
            print(punkt)
            nr_trans = punkt.hole_nr()
            y_trans = self.__trafo_param["y0"] + self.__trafo_param["a"] * punkt.hole_y() + self.__trafo_param["o"] * punkt.hole_x()
            x_trans = self.__trafo_param["x0"] + self.__trafo_param["a"] * punkt.hole_x() - self.__trafo_param["o"] * punkt.hole_y()

            self.__pkt_list_trans[nr_trans] = pkt.Punkt(y_trans, x_trans, nr_trans)

        for schluessel, wert in self.__pkt_list_trans.items():
            print(schluessel + " : " + str(wert))

        print("ENDE")


if __name__ == "__main__":

    trafo = Helmerttransformation()
    trafo.punktliste_laden()
    print(trafo.hole_liste_alt())
    print(trafo.hole_liste_neu())
    trafo.transformationsparameter()
    trafo.transformation()
