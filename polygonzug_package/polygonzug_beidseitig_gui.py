import tkinter as tk
import tkinter.filedialog as tkfd
import json

import grundlagen.gui as gui
import gui.berechnungsfenster as berechnungsfenster
import grundlagen.punkt as pkt
import grundlagen.punktliste as pktlst
import polygonzug_package.polygonzug as pz


class Anwendung(tk.Frame):

    def __init__(self, p_master):
        """Initialisiert die Anwendung.

        :param p_master: Berechnungsfenster
        :type p_master: Berechnungsfenster
        """
        super().__init__(p_master)

        self.__zeilen_anzahl: int = 0
        self.__spalten_anzahl: int = 0

        # Punktliste und Abweichungen
        self.__messung: list = list()
        self.__abweichungen: dict = dict()

        # alle Eingabefelder zu den Messungen und Anschlusspunkten
        self.__eingabe_pktlst: dict = dict()
        self.__eingabe_messungen: dict = dict()

        self.__p0: pkt.Punkt = pkt.Punkt()
        self.__p1: pkt.Punkt = pkt.Punkt()
        self.__pn: pkt.Punkt = pkt.Punkt()
        self.__pn_1: pkt.Punkt = pkt.Punkt()

        self.__feld_p0_nr: tk.Entry = tk.Entry(self)
        self.__feld_p0_y: tk.Entry = tk.Entry(self)
        self.__feld_p0_x: tk.Entry = tk.Entry(self)
        self.__feld_pn_1_nr: tk.Entry = tk.Entry(self)
        self.__feld_pn_1_y: tk.Entry = tk.Entry(self)
        self.__feld_pn_1_x: tk.Entry = tk.Entry(self)

        self.grid()

        self.master.title("Polygonzug mit beidseitigem Richtungs- und Koordinatenanschluss")

        zeile: int = 0
        # Buttons
        tk.Button(self, text="Polygonzug laden", command=self.importieren_berechnen, fg="purple").grid(row=zeile, column=0, columnspan=2, sticky="ew")
        tk.Button(self, text="Neupunkte exportieren", command=self.exportieren, fg="purple").grid(row=zeile, column=9, columnspan=2, sticky="ew")
        zeile += 1

        # Überschriften
        tk.Label(self, text="Punktnummer", font="arial 11 underline").grid(row=zeile, column=0)
        tk.Label(self, text="Brechungswinkel", font="arial 11 underline").grid(row=zeile, column=1)
        tk.Label(self, text="    ").grid(row=zeile, column=2)
        tk.Label(self, text="Richtungswinkel", font="arial 11 underline").grid(row=zeile, column=3)
        tk.Label(self, text="Strecke", font="arial 11 underline").grid(row=zeile, column=4)
        tk.Label(self, text="Koordinatendifferenzen", font="arial 11 underline").grid(row=zeile, column=5, columnspan=2)
        tk.Label(self, text="    ").grid(row=zeile, column=7)
        tk.Label(self, text="Koordinaten", font="arial 11 underline").grid(row=zeile, column=9, columnspan=2)
        zeile += 1

        tk.Label(self, text="i").grid(row=zeile, column=0)
        tk.Label(self, text="β").grid(row=zeile, column=1)
        tk.Label(self, text="t").grid(row=zeile, column=3)
        tk.Label(self, text="s").grid(row=zeile, column=4)
        tk.Label(self, text="Δy").grid(row=zeile, column=5)
        tk.Label(self, text="Δx").grid(row=zeile, column=6)
        tk.Label(self, text="y").grid(row=zeile, column=9)
        tk.Label(self, text="x").grid(row=zeile, column=10)
        zeile += 1

        tk.Label(self, text="").grid(row=zeile, columnspan=9)

    def setze_punktliste(self, p_messungen: list) -> None:
        """Erstellt die Tabelle mit den Punkten und Messungen.

        :param p_messungen: Liste mit den Messungen
        :type p_messungen: list
        :return: None
        :rtype: None
        """
        self.__messung: list = p_messungen
        self.__zeilen_anzahl: int = len(p_messungen)
        self.__spalten_anzahl: int = 9   # nr, beta, leer, t, s, dy, dx, leer, y, x

        # Anschlusspunkt
        zeile: int = 3
        spalte: int = 0
        print("Stop")
        self.__feld_p0_nr.grid(row=zeile, column=spalte)
        gui.eingabefeld_schreiben(self.__feld_p0_nr, self.__p0.hole_nr())
        spalte += 9
        self.__feld_p0_y.grid(row=zeile, column=spalte)
        gui.eingabefeld_schreiben(self.__feld_p0_y, self.__p0.hole_y())
        spalte += 1
        self.__feld_p0_x.grid(row=zeile, column=spalte)
        gui.eingabefeld_schreiben(self.__feld_p0_x, self.__p0.hole_x())
        zeile += 1
        tk.Label(self, text="").grid(row=zeile, columnspan=9)
        zeile += 1

        for i, messung in enumerate(self.__messung):
            # Einträge je Tabellenzeile ausgeben
            self.__eingabe_pktlst[i]: dict = dict()
            spalte: int = 0
            self.erzeuge_eingabefeld(zeile, spalte, i, "Punktnummer", messung["Punktnummer"])
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "Beta", messung["Beta"])
            spalte += 1
            tk.Label(self, text="⮷", font="arial 15").grid(row=zeile, column=spalte)
            spalte += 6
            tk.Label(self, text="⮳", font="arial 15").grid(row=zeile, column=spalte)
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "Punkt", messung["Punkt"].hole_y())
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "Punkt", messung["Punkt"].hole_x())
            spalte = 3
            zeile += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "verb_riwi", messung["verb_riwi"])
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "Strecke", messung["Strecke"])
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "delta_y", messung["delta_y"])
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, i, "delta_x", messung["delta_x"])
            zeile += 1

        # Abschlussrichtung
        spalte = 0
        self.__feld_pn_1_nr.grid(row=zeile, column=spalte)
        gui.eingabefeld_schreiben(self.__feld_pn_1_nr, self.__pn_1.hole_nr())
        spalte += 9
        self.__feld_pn_1_y.grid(row=zeile, column=spalte)
        gui.eingabefeld_schreiben(self.__feld_pn_1_y, self.__pn_1.hole_y())
        spalte += 1
        self.__feld_pn_1_x.grid(row=zeile, column=spalte)
        gui.eingabefeld_schreiben(self.__feld_pn_1_x, self.__pn_1.hole_x())
        zeile += 1

        # Abweichungen
        tk.Label(self, text="Winkelabweichung", font="arial 11 underline").grid(row=zeile, column=1)
        tk.Label(self, text="Koordinatenabweichungen", font="arial 11 underline").grid(row=zeile, column=5, columnspan=2)
        zeile += 1
        tk.Label(self, text="Y").grid(row=zeile, column=5)
        tk.Label(self, text="X").grid(row=zeile, column=6)
        zeile += 1
        tk.Label(self, text=f"{round(self.__abweichungen['Abw_winkel'], 4)} gon").grid(row=zeile, column=1)
        tk.Label(self, text=f"{round(self.__abweichungen['Abw_y'], 4)} m").grid(row=zeile, column=5)
        tk.Label(self, text=f"{round(self.__abweichungen['Abw_x'], 4)} m").grid(row=zeile, column=6)

    def erzeuge_eingabefeld(self, p_zeile: int, p_spalte: int, p_schluessel: int, p_atributname: str, p_atributwert: str) -> None:
        """Erzeugt ein Eingabefeld an der angegebenen Stellt mit den Werten.

        :param p_zeile: Zeilennummer
        :type p_zeile: int
        :param p_spalte: Spaltennummer
        :type p_spalte: int
        :param p_schluessel: Schlüssel in der Punktliste
        :type p_schluessel: str
        :param p_atributname: Atributname
        :type p_atributname: str
        :param p_atributwert: Atributwert
        :type p_atributwert: str
        :return: None
        :rtype: None
        """
        eingabe: tk.Entry = tk.Entry(self)
        self.__eingabe_pktlst[p_schluessel][p_atributname] = eingabe
        self.__eingabe_pktlst[p_schluessel][p_atributname].grid(row=p_zeile, column=p_spalte)
        try:
            gui.eingabefeld_schreiben(self.__eingabe_pktlst[p_schluessel][p_atributname], round(float(p_atributwert), 4))
        except:
            gui.eingabefeld_schreiben(self.__eingabe_pktlst[p_schluessel][p_atributname], p_atributwert)

    def importieren_berechnen(self) -> None:
        """Importiert die Messung und die Anschlusspunkte aus einer JSON-Datei und berechnet den Polygonzug.

        :return: None
        :rtype: None
        """
        json_daten = berechnungsfenster.import_json_dialog()

        self.__p0.setze_json(json_daten["Anschlusspunkte"]["Start_Anschluss"])
        self.__p1.setze_json(json_daten["Anschlusspunkte"]["Start"])
        self.__pn.setze_json(json_daten["Anschlusspunkte"]["Ende"])
        self.__pn_1.setze_json(json_daten["Anschlusspunkte"]["Ende_Anschluss"])
        self.__messung: list = json_daten["Messung"]
        self.berechnen()

    def berechnen(self) -> None:
        """Berechnet den Polygonzug.

        :return: None
        :rtype: None
        """
        meinzug = pz.PolygonzugBeidseitig()
        punkte, self.__abweichungen = meinzug.berechnen(self.__p0, self.__p1, self.__pn, self.__pn_1, self.__messung)
        self.setze_punktliste(punkte)

    def exportieren(self) -> None:
        """Exportiert die Neupunkte des Polygonzuges.

        :return: None
        :rtype: None
        """
        # Daten zusammenstellen
        punkte: dict = {i["Punktnummer"]: i["Punkt"] for i in self.__messung[1:-1]}

        berechnungsfenster.export_json_dialog(punkte)
