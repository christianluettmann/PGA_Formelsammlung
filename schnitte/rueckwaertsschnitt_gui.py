import tkinter as tk

import grundlagen.gui as gui
import grundlagen.punkt as pkt
import gui.berechnungsfenster as berechnungsfenster
import schnitte.rueckwaertsschnitt


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung.

                :param master: Berechnungsfenster
                :type master: Berechnungsfenster
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
        spalten_max = 8

        self.master.title("Rückwärtsschnitt")

        # Eingabe
        tk.Label(self, text="Eingabe:", font=("arial", 14, "underline")).grid(row=zeile)
        tk.Label(self, text="Achtung: Die Punkte müssen im Uhrzeitersinn eingegeben werden (A->M->B)!", fg="red").grid(
            row=zeile, column=1, columnspan=7)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden, fg="green").grid(
            row=zeile, column=spalten_max, sticky="e")
        zeile += 1

        """
        Eingabe: Punkt A
        """
        pos = (1, 0)
        tk.Label(self, text="Punkt A:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_pa_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self,
                      text="Punkt A laden",
                      command=lambda: self.lade_punkt_a(self.__eingabe_pa_nr.get())) \
                .grid(row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y A:").grid(row=pos[0] + 1, column=pos[1])
        self.__eingabe_pa_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x A:").grid(row=pos[0] + 2, column=pos[1])
        self.__eingabe_pa_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)
        # Eingabe: Richtung N->A
        tk.Label(self, text="Richtung N->A:").grid(row=pos[0] + 4, column=pos[1])
        self.__eingabe_richtung_na.grid(row=pos[0] + 4, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=pos[0] + 4, column=pos[1] + 2, sticky="w")

        """
        Eingabe: Punkt M
        """
        pos = (1, 3)
        tk.Label(self, text="Punkt M:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_pm_nr.grid(row=pos[0], column=pos[1] + 1, sticky="ew")
            tk.Button(self,
                      text="Punkt M laden",
                      command=lambda: self.lade_punkt_m(self.__eingabe_pm_nr.get())) \
                .grid(row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y M:").grid(row=pos[0] + 1, column=pos[1])
        self.__eingabe_pm_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x M:").grid(row=pos[0] + 2, column=pos[1])
        self.__eingabe_pm_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)
        # Eingabe: Richtung N->M
        tk.Label(self, text="Richtung N->M:").grid(row=pos[0] + 4, column=pos[1])
        self.__eingabe_richtung_nm.grid(row=pos[0] + 4, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=pos[0] + 4, column=pos[1] + 2, sticky="w")

        """
        Eingabe: Punkt B
        """
        pos = (1, 6)
        tk.Label(self, text="Punkt B:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_pb_nr.grid(row=pos[0], column=pos[1] + 1, sticky="w")
            tk.Button(self,
                      text="Punkt B laden",
                      command=lambda: self.lade_punkt_b(self.__eingabe_pb_nr.get())) \
                .grid(row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y B:").grid(row=pos[0] + 1, column=pos[1], sticky="ew")
        self.__eingabe_pb_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x B:").grid(row=pos[0] + 2, column=pos[1])
        self.__eingabe_pb_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)
        # Eingabe: Richtung N->B
        tk.Label(self, text="Richtung N->B:").grid(row=pos[0] + 4, column=pos[1])
        self.__eingabe_richtung_nb.grid(row=pos[0] + 4, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=pos[0] + 4, column=pos[1] + 2, sticky="w")

        # Berechnen Button
        zeile = 6
        tk.Button(self, text="Berechnen", command=self.berechnen, fg="blue").grid(row=zeile, column=4, sticky="ew")
        zeile += 1

        # Ausgabe
        tk.Label(self, text="Ausgabe:", font=("arial", 14, "underline")).grid(row=zeile)
        zeile += 1

        """
        Ausgabe: Punkt N
        """
        pos = (8, 3)
        tk.Label(self, text="Punkt N:").grid(row=pos[0], column=pos[1], sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_pn_nr.grid(row=pos[0], column=pos[1] + 1, sticky="w")
            tk.Button(self,
                      text="Punkt N speichern",
                      command=self.speicher_punkt_n) \
                .grid(row=pos[0], column=pos[1] + 2, sticky="w")
        # Koordinaten eingeben
        tk.Label(self, text="y N:").grid(row=pos[0] + 1, column=pos[1], sticky="ew")
        self.__ausgabe_pn_y.grid(row=pos[0] + 1, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 1, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="x N:").grid(row=pos[0] + 2, column=pos[1])
        self.__ausgabe_pn_x.grid(row=pos[0] + 2, column=pos[1] + 1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=pos[0] + 2, column=pos[1] + 2, sticky="w")
        tk.Label(self, text="").grid(row=pos[0] + 3, column=pos[1], columnspan=3)

        # JSON Import/Export
        tk.Button(self, text="JSON laden", fg="purple", command=self.json_laden).grid(row=20, column=1, sticky="ew")
        tk.Button(self, text="JSON speichern", fg="purple", command=self.json_speichern).grid(row=20,
                                                                                              column=spalten_max - 1,
                                                                                              sticky="ew")

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=20, column=4,
                                                                                    sticky="ew")

    def berechnen(self):
        """Übergibt die Eingabewerte an die Berechnungsmethode und schreibt die berechneten Werte in die Ausgabefelder.

        :return: None
        :rtype: None
        """
        pa: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_pa_y),
                                  gui.eingabefeld_auswerten(self.__eingabe_pa_x))
        pm: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_pm_y),
                                  gui.eingabefeld_auswerten(self.__eingabe_pm_x))
        pb: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_pb_y),
                                  gui.eingabefeld_auswerten(self.__eingabe_pb_x))
        r_na: float = gui.eingabefeld_auswerten(self.__eingabe_richtung_na)
        r_nm: float = gui.eingabefeld_auswerten(self.__eingabe_richtung_nm)
        r_nb: float = gui.eingabefeld_auswerten(self.__eingabe_richtung_nb)

        neupunkt = schnitte.rueckwaertsschnitt.Rueckwaertsschnitt.berechnen(pa, pm, pb, r_na, r_nm, r_nb)

        gui.eingabefeld_schreiben(self.__ausgabe_pn_y, neupunkt.hole_y())
        gui.eingabefeld_schreiben(self.__ausgabe_pn_x, neupunkt.hole_x())

    def testdaten_laden(self):
        """Lädt Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [46867.94, 5537.00, 51293.86, 6365.89, 49666.56, 4448.58, 66.8117, 294.7845, 362.8516]
        # Soll: yN = 48613.34 [m], Quelle: PGA Vorlesung

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
            0)
        self.master.sende_punkt(p)

    def json_laden(self) -> None:
        """Lädt die Eingabewerte aus einer JSON-Datei.

        :return: None
        :rtype: None
        """
        json_daten = berechnungsfenster.import_json_dialog()

        gui.eingabefeld_schreiben(self.__eingabe_pa_nr, json_daten["Punkte"]["PA"]["_Punkt__nr"])
        gui.eingabefeld_schreiben(self.__eingabe_pa_y, json_daten["Punkte"]["PA"]["_Punkt__y"])
        gui.eingabefeld_schreiben(self.__eingabe_pa_x, json_daten["Punkte"]["PA"]["_Punkt__x"])
        gui.eingabefeld_schreiben(self.__eingabe_pm_nr, json_daten["Punkte"]["PM"]["_Punkt__nr"])
        gui.eingabefeld_schreiben(self.__eingabe_pm_y, json_daten["Punkte"]["PM"]["_Punkt__y"])
        gui.eingabefeld_schreiben(self.__eingabe_pm_x, json_daten["Punkte"]["PM"]["_Punkt__x"])
        gui.eingabefeld_schreiben(self.__eingabe_pb_nr, json_daten["Punkte"]["PB"]["_Punkt__nr"])
        gui.eingabefeld_schreiben(self.__eingabe_pb_y, json_daten["Punkte"]["PB"]["_Punkt__y"])
        gui.eingabefeld_schreiben(self.__eingabe_pb_x, json_daten["Punkte"]["PB"]["_Punkt__x"])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_na, json_daten["Messung"]["R_NA"]["Richtung"])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_nm, json_daten["Messung"]["R_NM"]["Richtung"])
        gui.eingabefeld_schreiben(self.__eingabe_richtung_nb, json_daten["Messung"]["R_NB"]["Richtung"])

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
