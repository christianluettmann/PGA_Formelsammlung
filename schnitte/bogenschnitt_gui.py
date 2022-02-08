import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import schnitte.bogenschnitt


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung.

                :param master: Anwendung
                :type master: Anwendung
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
        spalten_max = 3

        self.master.title("Bogenschnitt")

        # Eingabe
        tk.Label(self, text="Eingabe:").grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden).grid(row=zeile, column=2, sticky="e")
        zeile += 1

        # Eingabe: Punkt1
        tk.Label(self, text="Punkt1:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p1_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt1 laden",
                      command=lambda: self.lade_punkt1(self.__eingabe_p1_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y1:").grid(row=zeile)
        self.__eingabe_p1_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x1:").grid(row=zeile)
        self.__eingabe_p1_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Strecke 1
        tk.Label(self, text="s1:").grid(row=zeile)
        self.__eingabe_s1_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Punkt2
        tk.Label(self, text="Punkt2:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p2_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt2 laden",
                      command=lambda: self.lade_punkt2(self.__eingabe_p2_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y2:").grid(row=zeile)
        self.__eingabe_p2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x2:").grid(row=zeile)
        self.__eingabe_p2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Strecke 2
        tk.Label(self, text="s2:").grid(row=zeile)
        self.__eingabe_s2_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Eingabe: Strecke 3 (Maßstab)
        tk.Label(self, text="Strecke zwischen den Punkten zur Maßstabsberechnung:").grid(row=zeile, columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="s3:").grid(row=zeile)
        self.__eingabe_s3_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=zeile, columnspan=spalten_max)
        zeile += 1

        # Ausgabe
        tk.Label(self, text="Ausgabe:").grid(row=zeile)
        zeile += 1

        # Ausgabe: Massstab
        tk.Label(self, text="Maßstab:").grid(row=zeile)
        self.__ausgabe_massstab.grid(row=zeile, column=1, sticky="ew")
        zeile += 1

        # Ausgabe:Punkt N1
        tk.Label(self, text="Punkt N1 (rechts der Linie):").grid(row=zeile, sticky="w", columnspan=spalten_max)
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn1_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt N1 speichern",
                      command=self.speicher_punkt_n1) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y N1:").grid(row=zeile)
        self.__ausgabe_pn1_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x N1:").grid(row=zeile)
        self.__ausgabe_pn1_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Ausgabe:Punkt N2
        tk.Label(self, text="Punkt N2 (links der Linie):").grid(row=zeile, sticky="w", columnspan=spalten_max)
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn2_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt N2 speichern",
                      command=self.speicher_punkt_n2) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y N2:").grid(row=zeile)
        self.__ausgabe_pn2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x N2:").grid(row=zeile)
        self.__ausgabe_pn2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=zeile, columnspan=spalten_max)

    def berechnen(self):
        """Übergibt die Eingabewerte an die Berechnungsmethode und schreibt die berechneten Werte in die Ausgabefelder.

        :return: None
        :rtype: None
        """
        p1_y = gui.eingabefeld_auswerten(self.__eingabe_p1_y)
        p1_x = gui.eingabefeld_auswerten(self.__eingabe_p1_x)
        p2_y = gui.eingabefeld_auswerten(self.__eingabe_p2_y)
        p2_x = gui.eingabefeld_auswerten(self.__eingabe_p2_x)
        s1 = gui.eingabefeld_auswerten(self.__eingabe_s1_laenge)
        s2 = gui.eingabefeld_auswerten(self.__eingabe_s2_laenge)
        s3 = gui.eingabefeld_auswerten(self.__eingabe_s3_laenge)

        ergebnis = schnitte.bogenschnitt.Bogenschnitt.berechnen(p1_y, p1_x, s1, p2_y, p2_x, s2, s3)

        gui.eingabefeld_schreiben(self.__ausgabe_pn1_y, ergebnis[0])
        gui.eingabefeld_schreiben(self.__ausgabe_pn1_x, ergebnis[1])
        gui.eingabefeld_schreiben(self.__ausgabe_pn2_y, ergebnis[2])
        gui.eingabefeld_schreiben(self.__ausgabe_pn2_x, ergebnis[3])
        gui.eingabefeld_schreiben(self.__ausgabe_massstab, ergebnis[4])

    def testdaten_laden(self):
        """Lädt zufällige Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [328.76, 1207.85, 925.04, 954.33, 294.33, 506.42, 648.08]

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


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
