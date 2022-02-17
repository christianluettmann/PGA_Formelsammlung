import tkinter as tk

import grundlagen.gui as gui
import grundlagen.punkt as pkt
import schnitte.vorwaertsschnitt
import gui.berechnungsfenster as berechnungsfenster


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung.

                :param master: Berechnungsfenster
                :type master: Berechnungsfenster
                """
        super().__init__(master)

        # GUI
        self.__eingabe_p1_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_x: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_x: tk.Entry = tk.Entry(self)

        self.__eingabe_richtung_1n: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_12: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_2n: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_21: tk.Entry = tk.Entry(self)

        self.__ausgabe_pn_nr: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn_x: tk.Entry = tk.Entry(self)

        self.grid()

        zeile = 0
        spalten_max = 5

        self.master.title("Vorwärtsschnitt")

        # Eingabe
        tk.Label(self, text="Eingabe:", font=("arial", 14, "underline")).grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden, fg="green").grid(
            row=zeile, column=spalten_max, sticky="e")
        zeile += 1

        """
        Eingabe: Punkt 1
        """
        pos = (1, 0)
        tk.Label(self, text="Punkt 1:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p1_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self,
                      text="Punkt 1 laden",
                      command=lambda: self.lade_punkt_1(self.__eingabe_p1_nr.get())).grid(
                row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y 1:").grid(row=pos[0] + 1, column=pos[1])
        self.__eingabe_p1_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x 1:").grid(row=pos[0] + 2, column=pos[1])
        self.__eingabe_p1_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)
        # Eingabe: Richtung 1->N
        tk.Label(self, text="Richtung 1->N:").grid(row=pos[0] + 4, column=pos[1])
        self.__eingabe_richtung_1n.grid(row=pos[0] + 4, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=pos[0] + 4, column=pos[1] + 2, sticky="w")
        # Eingabe: Richtung 1->2
        tk.Label(self, text="Richtung 1->2:").grid(row=pos[0] + 5, column=pos[1])
        self.__eingabe_richtung_12.grid(row=pos[0] + 5, column=pos[1] + 1, sticky="ew")
        gui.eingabefeld_schreiben(self.__eingabe_richtung_12, 0.0)
        tk.Label(self, text="[gon]").grid(row=pos[0] + 5, column=pos[1] + 2, sticky="w")

        """
        Eingabe: Punkt 2
        """
        pos = (1, 3)
        tk.Label(self, text="Punkt 2:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p2_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self,
                      text="Punkt 2 laden",
                      command=lambda: self.lade_punkt_2(self.__eingabe_p2_nr.get())).grid(
                row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y 2:").grid(row=pos[0] + 1, column=pos[1])
        self.__eingabe_p2_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x 2:").grid(row=pos[0] + 2, column=pos[1])
        self.__eingabe_p2_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)
        # Eingabe: Richtung 2->N
        tk.Label(self, text="Richtung 2->N:").grid(row=pos[0] + 4, column=pos[1])
        self.__eingabe_richtung_2n.grid(row=pos[0] + 4, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=pos[0] + 4, column=pos[1] + 2, sticky="w")
        # Eingabe: Richtung 2->1
        tk.Label(self, text="Richtung 2->1:").grid(row=pos[0] + 5, column=pos[1])
        self.__eingabe_richtung_21.grid(row=pos[0] + 5, column=pos[1] + 1, sticky="ew")
        gui.eingabefeld_schreiben(self.__eingabe_richtung_21, 0.0)
        tk.Label(self, text="[gon]").grid(row=pos[0] + 5, column=pos[1] + 2, sticky="w")

        # Berechnen Button
        zeile = 7
        tk.Button(self, text="Berechnen", command=self.berechnen, fg="blue").grid(
            row=zeile, column=2, columnspan=2, sticky="ew")
        zeile += 1
        # Ausgabe
        tk.Label(self, text="Ausgabe:", font=("arial", 14, "underline")).grid(row=zeile)
        zeile += 1

        """
        Ausgabe: Punkt N
        """
        pos = (9, 0)
        tk.Label(self, text="Punkt N:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn_nr.grid(row=pos[0], column=pos[1] + 1, sticky="w")
            tk.Button(self,
                      text="Punkt N speichern",
                      command=self.speicher_punkt_n).grid(
                row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y N:").grid(row=pos[0] + 1, column=pos[1], sticky="ew")
        self.__ausgabe_pn_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x N:").grid(row=pos[0] + 2, column=pos[1])
        self.__ausgabe_pn_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)

        # JSON Import/Export
        tk.Button(self, text="JSON laden", fg="purple", command=self.json_laden).grid(
            row=20, column=0, columnspan=2, sticky="ew")
        tk.Button(self, text="JSON speichern", fg="purple", command=self.json_speichern).grid(
            row=20, column=spalten_max - 1, columnspan=2, sticky="ew")

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(
            row=20, column=2, columnspan=2, sticky="ew")

    def berechnen(self):
        """Übergibt die Eingabewerte an die Berechnungsmethode und schreibt die berechneten Werte in die Ausgabefelder.

        :return: None
        :rtype: None
        """
        p1 = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p1_y), gui.eingabefeld_auswerten(self.__eingabe_p1_x))
        p2 = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p2_y), gui.eingabefeld_auswerten(self.__eingabe_p2_x))

        r_1n = gui.eingabefeld_auswerten(self.__eingabe_richtung_1n)
        r_12 = gui.eingabefeld_auswerten(self.__eingabe_richtung_12)
        r_2n = gui.eingabefeld_auswerten(self.__eingabe_richtung_2n)
        r_21 = gui.eingabefeld_auswerten(self.__eingabe_richtung_21)

        neupunkt = schnitte.vorwaertsschnitt.Vorwaertsschnitt.berechnen_dreieckswinkel(p1, p2, r_1n, r_12, r_2n, r_21)

        gui.eingabefeld_schreiben(self.__ausgabe_pn_y, neupunkt.hole_y())
        gui.eingabefeld_schreiben(self.__ausgabe_pn_x, neupunkt.hole_x())

    def testdaten_laden(self):
        """Lädt Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [1019.120, 3157.620, 1111.880, 3080.350, 10.1, 74.4025, 0.0, 331.1513]
        # Soll: , Quelle: http://www.moroder.it/daniel/data/GEO%20Vermessungskunde%20Lagepunktbestimmung.pdf

        gui.eingabefeld_schreiben(self.__eingabe_p1_y, testdaten[0])
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, testdaten[1])
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, testdaten[2])
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, testdaten[3])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_1n, testdaten[4])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_12, testdaten[5])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_2n, testdaten[6])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_21, testdaten[7])

        self.berechnen()

    def lade_punkt_1(self, p_pktnr):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_p1_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, p.hole_x())

    def lade_punkt_2(self, p_pktnr):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, p.hole_x())

    def speicher_punkt_n(self):
        """Speichert den berechneten Punkt in die Main-Punktliste.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :return: None
        :rtype: None
        """
        p: pkt.Punkt = pkt.Punkt(
            gui.eingabefeld_auswerten(self.__ausgabe_pn_y),
            gui.eingabefeld_auswerten(self.__ausgabe_pn_x),
            self.__ausgabe_pn_nr.get(),
            0)
        self.master.sende_punkt(p)

    def json_laden(self) -> None:
        """Lädt die Eingabewerte aus einer JSON-Datei.

        :return: None
        :rtype: None
        """
        json_daten = berechnungsfenster.import_json_dialog()

        gui.eingabefeld_schreiben(self.__eingabe_p1_nr, json_daten["Punkte"]["P1"]["_Punkt__nr"])
        gui.eingabefeld_schreiben(self.__eingabe_p1_y, json_daten["Punkte"]["P1"]["_Punkt__y"])
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, json_daten["Punkte"]["P1"]["_Punkt__x"])
        gui.eingabefeld_schreiben(self.__eingabe_p2_nr, json_daten["Punkte"]["P2"]["_Punkt__nr"])
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, json_daten["Punkte"]["P2"]["_Punkt__y"])
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, json_daten["Punkte"]["P2"]["_Punkt__x"])

        gui.eingabefeld_schreiben(self.__eingabe_richtung_1n, json_daten["Messung"]["R_1N"]["Richtung"])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_12, json_daten["Messung"]["R_12"]["Richtung"])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_2n, json_daten["Messung"]["R_2N"]["Richtung"])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_21, json_daten["Messung"]["R_21"]["Richtung"])

        self.berechnen()

    def json_speichern(self) -> None:
        """Speichert den berechneten Neupunkt in eine JSON-Datei.

        :return: None
        :rtype: None
        """
        punkte: dict = {self.__ausgabe_pn_nr.get(): pkt.Punkt(gui.eingabefeld_auswerten(self.__ausgabe_pn_y),
                                                              gui.eingabefeld_auswerten(self.__ausgabe_pn_x),
                                                              self.__ausgabe_pn_nr.get())}
        berechnungsfenster.export_json_dialog(punkte)


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
