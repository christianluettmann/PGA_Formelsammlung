from math import sin, cos, sqrt
from grundlagen.winkel import Winkel
import grundlagen.punkt as pkt
import grundlagen.zweite_grundaufgabe


class Polygonzug:
    @staticmethod
    def richtungswinkel(messungen: list[dict], abweichungen: dict, richtung_anschluss: float) -> list[dict]:
        """Berechnet die Richtungswinkel aus den Messwerten in einem Polygonzug.

        :param messungen: Liste mit Dictionaries der einzelnen Messungen
        :type messungen: list[dict]
        :param abweichungen: Dictionary mit den Abweichungen des Polygonzuges (Winkel-, Koordinaten-, ...)
        :type abweichungen: dict
        :param richtung_anschluss: Anschlussrichtung des ersten Punktes
        :type richtung_anschluss: float
        :return: Liste der einzelnen Messungen, ergänzt um die Richtungswinkel
        :rtype: list[dict]
        """
        for i, messung in enumerate(messungen):
            if i == 0:
                messung["verb_riwi"]: float = (richtung_anschluss + messung["Beta"]
                                               + 200 + abweichungen["Delta_abw_winkel"]) % 400
            else:
                messung["verb_riwi"]: float = (messungen[i - 1]["verb_riwi"] + messung["Beta"]
                                               + 200 + abweichungen["Delta_abw_winkel"]) % 400
        return messungen

    @staticmethod
    def koordinatenunterschiede(messungen: list[dict]) -> list[dict]:
        """Berechnet die Koordinatenunterschiede zwischen den einzelnen Punkten
        und fügt diese in die Liste der Messungen ein.

        :param messungen: Liste mit Dictionaries der einzelnen Messungen
        :type messungen: list[dict]
        :return: Liste mit Dictionaries der einzelnen Messungen, ergänzt um die Koordinatenunterschiede
        :rtype: list[dict]
        """
        for messung in messungen:
            messung["delta_y"]: float = messung["Strecke"] * sin(Winkel.gon2rad(messung["verb_riwi"]))
            messung["delta_x"]: float = messung["Strecke"] * cos(Winkel.gon2rad(messung["verb_riwi"]))
        return messungen

    @staticmethod
    def koordinatenverbesserungen(messungen: list[dict], abweichungen: dict) -> list[dict]:
        """Berechnet die Koordinatenverbesserungen zwischen den einzelnen Punkten
        und fügt diese in die Liste der Messungen ein.

        :param messungen: Liste mit Dictionaries der einzelnen Messungen
        :type messungen: list[dict]
        :param abweichungen: Dictionary mit den Abweichungen des Polygonzuges (Winkel-, Koordinaten-, ...)
        :type abweichungen: dict
        :return: Liste mit Dictionaries der einzelnen Messungen, ergänzt um die Koordinatenverbesserungen
        :rtype: list[dict]
        """
        sum_strecke: float = sum(i["Strecke"] for i in messungen)
        for messung in messungen:
            messung["verb_y"]: float = messung["Strecke"] / sum_strecke * abweichungen["Abw_y"]
            messung["verb_x"]: float = messung["Strecke"] / sum_strecke * abweichungen["Abw_x"]
        return messungen

    @staticmethod
    def endgueltige_koordinaten(messungen: list[dict], startpunkt: pkt.Punkt = pkt.Punkt()) -> list[dict]:
        """Berechnet die endgültigen Koordinaten der Punkte mit den verbesserten Messwerten.

        :param messungen: Liste mit Dictionaries der einzelnen Messungen
        :type messungen: list[dict]
        :param startpunkt: erster Punkt des Polygonzuges
        :type startpunkt: pkt.Punkt
        :return: Liste mit Dictionaries der einzelnen Messungen, ergänzt um die endgültigen Punkte
        :rtype: list[dict]
        """
        for i, messung in enumerate(messungen):
            if i == 0:
                messung["Punkt"]: pkt.Punkt = startpunkt
            elif i == 1:
                messung["Punkt"]: pkt.Punkt = pkt.Punkt(
                    p_y=startpunkt.hole_y() + messungen[i - 1]["delta_y"] + messungen[i - 1]["verb_y"],
                    p_x=startpunkt.hole_x() + messungen[i - 1]["delta_x"] + messungen[i - 1]["verb_x"],
                    p_nr=messung["Punktnummer"])
            elif i < len(messungen):
                messung["Punkt"]: pkt.Punkt = pkt.Punkt(
                    p_y=messungen[i - 1]["Punkt"].hole_y() + messungen[i - 1]["delta_y"] + messungen[i - 1]["verb_y"],
                    p_x=messungen[i - 1]["Punkt"].hole_x() + messungen[i - 1]["delta_x"] + messungen[i - 1]["verb_x"],
                    p_nr=messung["Punktnummer"])
        return messungen


class PolygonzugBeidseitig(Polygonzug):
    def berechnen(self, p_p0: pkt.Punkt, p_p1: pkt.Punkt, p_pn: pkt.Punkt, p_pn1: pkt.Punkt,
                  messungen: list) -> tuple[list[dict], dict]:
        """Berechnet den Polygonzug mit beidseitigem Richtungs- und Koordinatenanschluss.
        (Gruber, Joeckel: Formelsammlung für das Vermessungswesen, 18. Auflage, S. 91)

        :param p_p0: Punkt für die Anschlussrichtung
        :type p_p0: pkt.Punkt
        :param p_p1: Startpunkt des Polygonzuges
        :type p_p1: pkt.Punkt
        :param p_pn: Endpunkt des Polygonzuges
        :type p_pn: pkt.Punkt
        :param p_pn1: Punkt für die Abschlussrichtung
        :type p_pn1: pkt.Punkt
        :param messungen: Liste mit Dictionaries der einzelnen Messungen (Punktnummer, Brechungswinkel, Strecke)
        :type messungen: list[dict]
        :return: Liste mit Dictionaries der einzelnen Messungen, ergänzt um alle Berechnungen und Dictionary mit den Abweichungen
        :rtype: tuple[list[dict], dict]
        """
        # Dictionary für die Abweichungen anlegen
        abweichungen: dict = dict()

        # 1. Anschluss- und Abschlussrichtung
        strecke_anschluss, richtung_anschluss = grundlagen.zweite_grundaufgabe.zweite_grundaufgabe(p_p0, p_p1)
        strecke_abschluss, richtung_abschluss = grundlagen.zweite_grundaufgabe.zweite_grundaufgabe(p_pn, p_pn1)

        # 2. Winkelabweichung
        sum_beta: float = sum(i["Beta"] for i in messungen)
        abweichungen["Abw_winkel"]: float = richtung_abschluss - (
                richtung_anschluss + sum_beta - (len(messungen) - 2) * 200)  # TODO: Überprüfen len-2
        abweichungen["Delta_abw_winkel"]: float = abweichungen["Abw_winkel"] / len(messungen)

        # 3. Richtungswinkel
        messungen: list[dict] = self.richtungswinkel(messungen, abweichungen, richtung_anschluss)

        # 4. Koordinatenunterschiede
        messungen: list[dict] = self.koordinatenunterschiede(messungen)

        # 5. Koordinatenabweichungen
        abweichungen["Abw_y"]: float = p_pn.hole_y() - p_p1.hole_y() - sum(i["delta_y"] for i in messungen)
        abweichungen["Abw_x"]: float = p_pn.hole_x() - p_p1.hole_x() - sum(i["delta_x"] for i in messungen)

        # 6. Koordinatenverbesserung
        messungen: list[dict] = self.koordinatenverbesserungen(messungen, abweichungen)

        # 7. endgültige Koordinaten
        messungen: list[dict] = self.endgueltige_koordinaten(messungen, p_p1)

        # 8. Abweichungen
        sum_delta_y: float = sum(i["delta_y"] for i in messungen)
        sum_delta_x: float = sum(i["delta_x"] for i in messungen)
        # Lineare Abweichung
        abweichungen["Abw_linear"]: float = sqrt(abweichungen["Abw_y"] ** 2 + abweichungen["Abw_x"] ** 2)
        # Laengsabweichung
        abweichungen["Abw_laengs"]: float = (abweichungen["Abw_y"]*sum_delta_y + abweichungen["Abw_x"] * sum_delta_x) \
                                            / (sqrt(sum_delta_y ** 2 + sum_delta_x ** 2))
        # Querabweichung
        abweichungen["Abw_quer"]: float = (abweichungen["Abw_y"] * sum_delta_x - abweichungen["Abw_x"] * sum_delta_y) \
                                          / (sqrt(sum_delta_y ** 2 + sum_delta_x ** 2))

        return messungen, abweichungen


class PolygonzugRing(Polygonzug):

    def berechnen(self, messungen: list) -> tuple[list[dict], dict]:
        """Berechnet den Ring-Polygonzug.
        (Gruber, Joeckel: Formelsammlung für das Vermessungswesen, 18. Auflage, S. 93)

        :param messungen: Liste mit Dictionaries der einzelnen Messungen (Punktnummer, Brechungswinkel, Strecke)
        :type messungen: list[dict]
        :return: Liste mit Dictionaries der einzelnen Messungen, ergänzt um alle Berechnungen und Dictionary mit den Abweichungen
        :rtype: tuple[list[dict], dict]
        """
        # Dictionary für die Abweichungen anlegen
        abweichungen: dict = dict()

        # 2. Winkelabweichung
        sum_beta: float = sum(i["Beta"] for i in messungen)
        abweichungen["Abw_winkel"]: float = (len(messungen) + 2) * 200 - sum_beta
        abweichungen["Delta_abw_winkel"]: float = abweichungen["Abw_winkel"] / len(messungen)

        # 3. Richtungswinkel
        messungen: list[dict] = self.richtungswinkel(messungen, abweichungen,
                                                     200 - messungen[0]["Beta"] - abweichungen["Delta_abw_winkel"])

        # 4. Koordinatenunterschiede
        messungen: list[dict] = self.koordinatenunterschiede(messungen)

        # 5. Koordinatenabweichungen
        abweichungen["Abw_y"]: float = 0 - sum(i["delta_y"] for i in messungen)
        abweichungen["Abw_x"]: float = 0 - sum(i["delta_x"] for i in messungen)

        # 6. Koordinatenverbesserung
        messungen: list[dict] = self.koordinatenverbesserungen(messungen, abweichungen)

        # 7. endgültige Koordinaten
        startpunkt: pkt.Punkt = pkt.Punkt(0.0, 500.0, messungen[0]["Punktnummer"])
        messungen: list[dict] = self.endgueltige_koordinaten(messungen, startpunkt)

        return messungen, abweichungen
