import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import gui.berechnungsfenster as berechnungsfenster
import schnitte.bogenschnitt


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

        self.__eingabe_s1_laenge: tk.Entry = tk.Entry(self)
        self.__eingabe_s2_laenge: tk.Entry = tk.Entry(self)
        self.__eingabe_s3_laenge: tk.Entry = tk.Entry(self)

        self.__ausgabe_massstab: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn1_nr: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn1_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn1_x: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn2_nr: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn2_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn2_x: tk.Entry = tk.Entry(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):

        self.grid()

        zeile = 0
        spalten_max = 5

        self.master.title("Bogenschnitt")

        # Eingabe
        tk.Label(self, text="Eingabe:", font=("arial", 14, "underline")).grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden, fg="green").grid(row=zeile, column=spalten_max, sticky="e")
        zeile = 1

        """
        Eingabe: Punkt1
        """
        pos = (1, 0)
        tk.Label(self, text="Punkt1:").grid(row=pos[0], column=pos[1], sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p1_nr.grid(row=pos[0], column=pos[1]+1, sticky="ew")
            tk.Button(self,
                      text="Punkt1 laden",
                      command=lambda: self.lade_punkt1(self.__eingabe_p1_nr.get())) \
                .grid(row=pos[0], column=pos[1]+2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y1:").grid(row=pos[0]+1, column=pos[1])
        self.__eingabe_p1_y.grid(row=pos[0]+1, column=pos[1]+1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0]+1, column=pos[1]+2, sticky="w")
        tk.Label(self, text="x1:").grid(row=pos[0]+2, column=pos[1])
        self.__eingabe_p1_x.grid(row=pos[0]+2, column=pos[1]+1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0]+2, column=pos[1]+2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0]+3, column=pos[1], columnspan=3)
        # Eingabe: Strecke 1
        tk.Label(self, text="s1:").grid(row=pos[0]+4, column=pos[1])
        self.__eingabe_s1_laenge.grid(row=pos[0]+4, column=pos[1]+1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0]+4, column=pos[1]+2, sticky="w")

        """
        Eingabe: Punkt2
        """
        pos = (1, 3)
        tk.Label(self, text="Punkt2:").grid(row=pos[0], column=pos[1], sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p2_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self,
                      text="Punkt2 laden",
                      command=lambda: self.lade_punkt2(self.__eingabe_p2_nr.get())) \
                .grid(row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y2:").grid(row=pos[0] + 1, column=pos[1])
        self.__eingabe_p2_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x2:").grid(row=pos[0] + 2, column=pos[1])
        self.__eingabe_p2_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        # Eingabe: Strecke 2
        tk.Label(self, text="s2:").grid(row=pos[0] + 4, column=pos[1])
        self.__eingabe_s2_laenge.grid(row=pos[0] + 4, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 4, column=pos[1] + 2, sticky="w")

        # Eingabe/Ausgabe: Strecke 3/Maßstab)
        zeile = 6
        tk.Label(self, text="Strecke zwischen den Punkten zur Maßstabsberechnung:", font="arial 11 underline").grid(row=zeile, columnspan=spalten_max, sticky="w")
        zeile += 1
        tk.Label(self, text="s3:").grid(row=zeile)
        self.__eingabe_s3_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        # Ausgabe: Massstab
        tk.Label(self, text="Maßstab:").grid(row=zeile, column=3)
        self.__ausgabe_massstab.grid(row=zeile, column=4, sticky="ew")
        zeile += 1

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen, fg="blue").grid(row=zeile, column=2, columnspan=2, sticky="ew")
        zeile += 1

        # Ausgabe
        tk.Label(self, text="Ausgabe:", font=("arial", 14, "underline")).grid(row=zeile)
        zeile += 1

        """
        Ausgabe: Punkt N1
        """
        pos = (11, 0)
        tk.Label(self, text="Punkt N1:").grid(row=pos[0], column=pos[1], sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn1_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self, text="Punkt N1 speichern", command=self.speicher_punkt_n1).grid(row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y N1:").grid(row=pos[0] + 1, column=pos[1])
        self.__ausgabe_pn1_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x N1:").grid(row=pos[0] + 2, column=pos[1])
        self.__ausgabe_pn1_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)

        """
        Ausgabe: Punkt N2
        """
        pos = (11, 3)
        tk.Label(self, text="Punkt N2:").grid(row=pos[0], column=pos[1], sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn2_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self, text="Punkt N2 speichern", command=self.speicher_punkt_n2).grid(row=pos[0],
                                                                                                    column=pos[1] + 2,
                                                                                                    sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y N2:").grid(row=pos[0] + 1, column=pos[1])
        self.__ausgabe_pn2_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x N2:").grid(row=pos[0] + 2, column=pos[1])
        self.__ausgabe_pn2_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)

        # JSON Import/Export
        tk.Button(self, text="JSON laden", fg="purple", command=self.json_laden).grid(row=20, column=0, columnspan=2, sticky="ew")
        tk.Button(self, text="JSON speichern", fg="purple", command=self.json_speichern).grid(row=20, column=spalten_max-1, columnspan=2, sticky="ew")

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=20, column=2, columnspan=2, sticky="ew")

    def berechnen(self):
        """Übergibt die Eingabewerte an die Berechnungsmethode und schreibt die berechneten Werte in die Ausgabefelder.

        :return: None
        :rtype: None
        """
        p1: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p1_y), gui.eingabefeld_auswerten(self.__eingabe_p1_x))
        p2: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p2_y), gui.eingabefeld_auswerten(self.__eingabe_p2_x))
        s1: float = gui.eingabefeld_auswerten(self.__eingabe_s1_laenge)
        s2: float = gui.eingabefeld_auswerten(self.__eingabe_s2_laenge)
        s3: float = gui.eingabefeld_auswerten(self.__eingabe_s3_laenge)

        neupunkt1, neupunkt2, massstab = schnitte.bogenschnitt.Bogenschnitt.berechnen(p1, s1, p2, s2, s3)

        gui.eingabefeld_schreiben(self.__ausgabe_pn1_y, neupunkt1.hole_y())
        gui.eingabefeld_schreiben(self.__ausgabe_pn1_x, neupunkt1.hole_x())
        gui.eingabefeld_schreiben(self.__ausgabe_pn2_y, neupunkt2.hole_y())
        gui.eingabefeld_schreiben(self.__ausgabe_pn2_x, neupunkt2.hole_x())
        gui.eingabefeld_schreiben(self.__ausgabe_massstab, massstab)

    def testdaten_laden(self):
        """Lädt zufällige Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [328.76, 1207.85, 925.04, 954.33, 294.33, 506.42, 648.08]
        # Soll: PN2(593.??, 1336.??), Quelle: PGA Vorlesung

        gui.eingabefeld_schreiben(self.__eingabe_p1_y, testdaten[0])
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, testdaten[1])
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, testdaten[2])
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, testdaten[3])
        gui.eingabefeld_schreiben(self.__eingabe_s1_laenge, testdaten[4])
        gui.eingabefeld_schreiben(self.__eingabe_s2_laenge, testdaten[5])
        gui.eingabefeld_schreiben(self.__eingabe_s3_laenge, testdaten[6])

        self.berechnen()

    def lade_punkt1(self, p_pktnr):
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

    def lade_punkt2(self, p_pktnr):
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

    def speicher_punkt_n1(self):
        """Speichert den berechneten Punkt in die Main-Punktliste.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :return: None
        :rtype: None
        """
        p: pkt.Punkt = pkt.Punkt(
            gui.eingabefeld_auswerten(self.__ausgabe_pn1_y),
            gui.eingabefeld_auswerten(self.__ausgabe_pn1_x),
            self.__ausgabe_pn1_nr.get(),
            0)   # TODO
        self.master.sende_punkt(p)

    def speicher_punkt_n2(self):
        """Speichert den berechneten Punkt in die Main-Punktliste.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :return: None
        :rtype: None
        """
        p: pkt.Punkt = pkt.Punkt(
            gui.eingabefeld_auswerten(self.__ausgabe_pn2_y),
            gui.eingabefeld_auswerten(self.__ausgabe_pn2_x),
            self.__ausgabe_pn2_nr.get(),
            0)   # TODO
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

        gui.eingabefeld_schreiben(self.__eingabe_s1_laenge, json_daten["Messung"]["S1"]["Strecke"])
        gui.eingabefeld_schreiben(self.__eingabe_s2_laenge, json_daten["Messung"]["S2"]["Strecke"])
        gui.eingabefeld_schreiben(self.__eingabe_s3_laenge, json_daten["Messung"]["S3"]["Strecke"])

        self.berechnen()

    def json_speichern(self) -> None:
        """Speichert die berechneten Neupunkte in eine JSON-Datei.

        :return: None
        :rtype: None
        """
        punkte = {self.__ausgabe_pn1_nr.get():pkt.Punkt(gui.eingabefeld_auswerten(self.__ausgabe_pn1_y),
                                                        gui.eingabefeld_auswerten(self.__ausgabe_pn1_x),
                                                        self.__ausgabe_pn1_nr.get()),
                  self.__ausgabe_pn2_nr.get(): pkt.Punkt(gui.eingabefeld_auswerten(self.__ausgabe_pn2_y),
                                                         gui.eingabefeld_auswerten(self.__ausgabe_pn2_x),
                                                         self.__ausgabe_pn2_nr.get())
                  }
        berechnungsfenster.export_json_dialog(punkte)


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
