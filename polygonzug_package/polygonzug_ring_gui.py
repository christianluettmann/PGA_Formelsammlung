import tkinter as tk

import grundlagen.gui as gui
import gui.berechnungsfenster as berechnungsfenster
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

        self.grid()

        self.master.title("Ringpolygon")

        zeile: int = 0
        # Buttons
        tk.Button(self, text="Polygonzug laden", command=self.importieren, fg="purple").grid(
            row=zeile, column=0, columnspan=2, sticky="ew")
        tk.Button(self, text="Neupunkte exportieren", command=self.exportieren, fg="purple").grid(
            row=zeile, column=9, columnspan=2, sticky="ew")
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

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=100, column=4, columnspan=2,
                                                                                    sticky="ew")

    def setze_punktliste(self, p_messungen: list) -> None:
        """Erstellt die Tabelle mit den Punkten.

        :param p_messungen: Liste mit den Messungen
        :type p_messungen: list
        :return: None
        :rtype: None
        """
        self.__messung = p_messungen
        self.__zeilen_anzahl = len(p_messungen)
        self.__spalten_anzahl = 7   # nr, beta, leer, t, s, dy, dx, leer, y, x

        zeile: int = 3

        for i, messung in enumerate(self.__messung):
            # Eintraege je Tabellenzeile ausgeben
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

    def erzeuge_eingabefeld(self, p_zeile: int, p_spalte: int,
                            p_schluessel: int, p_atributname: str, p_atributwert: str) -> None:
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
            self.__eingabe_pktlst[p_schluessel][p_atributname].insert(0, p_atributwert)

    def importieren(self) -> None:

        json_daten = berechnungsfenster.import_json_dialog()

        self.__messung: list = json_daten["Messung"]

        self.berechnen()

    def berechnen(self) -> None:
        """Berechnet den Polygonzug

        :return: None
        :rtype: None
        """
        meinzug = pz.PolygonzugRing()
        punkte, self.__abweichungen = meinzug.berechnen(self.__messung)
        self.setze_punktliste(punkte)

    def exportieren(self) -> None:
        """Exportiert die Neupunkte des Polygonzuges.

        :return: None
        :rtype: None
        """
        # Daten zusammenstellen
        punkte: dict = {i["Punktnummer"]: i["Punkt"] for i in self.__messung}

        berechnungsfenster.export_json_dialog(punkte)


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
