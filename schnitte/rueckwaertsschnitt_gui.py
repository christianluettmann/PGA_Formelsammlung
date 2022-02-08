import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import schnitte.rueckwaertsschnitt


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung.

                :param master: Anwendung
                :type master: Anwendung
                """
        super().__init__(master)

        # GUI
        self.__eingabe_pa_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_pa_y: tk.Entry = tk.Entry(self)
        self.__eingabe_pa_x: tk.Entry = tk.Entry(self)
        self.__eingabe_pm_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_pm_y: tk.Entry = tk.Entry(self)
        self.__eingabe_pm_x: tk.Entry = tk.Entry(self)
        self.__eingabe_pb_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_pb_y: tk.Entry = tk.Entry(self)
        self.__eingabe_pb_x: tk.Entry = tk.Entry(self)

        self.__eingabe_richtung_na: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_nm: tk.Entry = tk.Entry(self)
        self.__eingabe_richtung_nb: tk.Entry = tk.Entry(self)

        self.__ausgabe_pn_nr: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn_x: tk.Entry = tk.Entry(self)

        self.grid()

        zeile = 0
        spalten_max = 3

        self.master.title("Rückwärtsschnitt")

        # Eingabe
        tk.Label(self, text="Eingabe:").grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden).grid(row=zeile, column=2, sticky="e")
        zeile += 1

        # Eingabe: Punkt A
        tk.Label(self, text="Punkt A:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_pa_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt A laden",
                      command=lambda: self.lade_punkt_a(self.__eingabe_pa_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y A:").grid(row=zeile)
        self.__eingabe_pa_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x A:").grid(row=zeile)
        self.__eingabe_pa_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Richtung N->A
        tk.Label(self, text="Richtung N->A:").grid(row=zeile)
        self.__eingabe_richtung_na.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Eingabe: Punkt M
        tk.Label(self, text="Punkt M:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_pm_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt M laden",
                      command=lambda: self.lade_punkt_m(self.__eingabe_pm_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y M:").grid(row=zeile)
        self.__eingabe_pm_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x M:").grid(row=zeile)
        self.__eingabe_pm_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Richtung N->M
        tk.Label(self, text="Richtung N->M:").grid(row=zeile)
        self.__eingabe_richtung_nm.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 2

        # Eingabe: Punkt B
        tk.Label(self, text="Punkt B:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_pb_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt B laden",
                      command=lambda: self.lade_punkt_b(self.__eingabe_pb_nr.get())) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y B:").grid(row=zeile)
        self.__eingabe_pb_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x B:").grid(row=zeile)
        self.__eingabe_pb_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Richtung N->B
        tk.Label(self, text="Richtung N->B:").grid(row=zeile)
        self.__eingabe_richtung_nb.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

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
        pa_y = gui.eingabefeld_auswerten(self.__eingabe_pa_y)
        pa_x = gui.eingabefeld_auswerten(self.__eingabe_pa_x)
        pm_y = gui.eingabefeld_auswerten(self.__eingabe_pm_y)
        pm_x = gui.eingabefeld_auswerten(self.__eingabe_pm_x)
        pb_y = gui.eingabefeld_auswerten(self.__eingabe_pb_y)
        pb_x = gui.eingabefeld_auswerten(self.__eingabe_pb_x)
        r_na = gui.eingabefeld_auswerten(self.__eingabe_richtung_na)
        r_nm = gui.eingabefeld_auswerten(self.__eingabe_richtung_nm)
        r_nb = gui.eingabefeld_auswerten(self.__eingabe_richtung_nb)

        ergebnis = schnitte.rueckwaertsschnitt.Rueckwaertsschnitt.berechnen(pa_y, pa_x, pm_y, pm_x, pb_y, pb_x, r_na, r_nm, r_nb)

        gui.eingabefeld_schreiben(self.__ausgabe_pn_y, ergebnis[0])
        gui.eingabefeld_schreiben(self.__ausgabe_pn_x, ergebnis[1])

    def testdaten_laden(self):
        """Lädt Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [46867.94, 5537.00, 51293.86, 6365.89, 49666.56, 4448.58, 66.8117, 294.7845, 362.8516]

        gui.eingabefeld_schreiben(self.__eingabe_pa_y, testdaten[0])
        gui.eingabefeld_schreiben(self.__eingabe_pa_x, testdaten[1])
        gui.eingabefeld_schreiben(self.__eingabe_pm_y, testdaten[2])
        gui.eingabefeld_schreiben(self.__eingabe_pm_x, testdaten[3])
        gui.eingabefeld_schreiben(self.__eingabe_pb_y, testdaten[4])
        gui.eingabefeld_schreiben(self.__eingabe_pb_x, testdaten[5])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_na, testdaten[6])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_nm, testdaten[7])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_nb, testdaten[8])

        self.berechnen()

    def lade_punkt_a(self, p_pktnr):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_pa_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_pa_x, p.hole_x())

    def lade_punkt_m(self, p_pktnr):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_pm_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_pm_x, p.hole_x())

    def lade_punkt_b(self, p_pktnr):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_pb_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_pb_x, p.hole_x())

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
