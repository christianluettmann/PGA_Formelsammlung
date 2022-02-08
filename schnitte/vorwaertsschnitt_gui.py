import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import schnitte.vorwaertsschnitt


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

        self.__eingabe_richtung_1n: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_12: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_2n: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_21: tk.Entry = tk.Entry(self)

        self.__ausgabe_pn_nr: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn_x: tk.Entry = tk.Entry(self)

        self.grid()

        zeile = 0
        spalten_max = 3

        self.master.title("Vorwärtsschnitt")

        # Eingabe
        tk.Label(self, text="Eingabe:").grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden).grid(row=zeile, column=2, sticky="e")
        zeile += 1

        # Eingabe: Punkt 1
        tk.Label(self, text="Punkt 1:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p1_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt 1 laden",
                      command=lambda: self.lade_punkt_1(self.__eingabe_p1_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y 1:").grid(row=zeile)
        self.__eingabe_p1_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x 1:").grid(row=zeile)
        self.__eingabe_p1_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Richtung 1->N
        tk.Label(self, text="Richtung 1->N:").grid(row=zeile)
        self.__eingabe_richtung_1n.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Eingabe: Richtung 1->2
        tk.Label(self, text="Richtung 1->2:").grid(row=zeile)
        self.__eingabe_richtung_12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Eingabe: Punkt 2
        tk.Label(self, text="Punkt 2:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p2_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt 2 laden",
                      command=lambda: self.lade_punkt_2(self.__eingabe_p2_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y 2:").grid(row=zeile)
        self.__eingabe_p2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x 2:").grid(row=zeile)
        self.__eingabe_p2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Richtung 2->N
        tk.Label(self, text="Richtung 2->N:").grid(row=zeile)
        self.__eingabe_richtung_2n.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Eingabe: Richtung 2->1
        tk.Label(self, text="Richtung 2->1:").grid(row=zeile)
        self.__eingabe_richtung_21.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=zeile, columnspan=spalten_max)
        zeile += 1

        # Ausgabe
        tk.Label(self, text="Ausgabe:").grid(row=zeile)
        zeile += 1

        # Ausgabe:Punkt N
        tk.Label(self, text="Punkt N:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt N speichern",
                      command=self.speicher_punkt_n) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y N:").grid(row=zeile)
        self.__ausgabe_pn_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x N:").grid(row=zeile)
        self.__ausgabe_pn_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=zeile, columnspan=spalten_max)

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
            0)   # TODO
        self.master.sende_punkt(p)


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
