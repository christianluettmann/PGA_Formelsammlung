import tkinter as tk

import grundlagen.gui as gui
import grundlagen.punkt as pkt
import grundlagen.zweite_grundaufgabe


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung

        :param master: Berechnungsfenster
        :type master: Berechnungsfenster
        """
        super().__init__(master)

        self.__eingabe_p1_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_x: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_x: tk.Entry = tk.Entry(self)

        self.__ausgabe_s12: tk.Entry = tk.Entry(self)
        self.__ausgabe_t12: tk.Entry = tk.Entry(self)

        self.grid()

        zeile: int = 0
        spalten_max: int = 3

        self.master.title("2. geodätische Grundaufgabe")

        # Eingabe
        tk.Label(self, text="Eingabe:", font=("arial", 14, "underline")).grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden, fg="green").grid(row=zeile, column=2,
                                                                                               sticky="e")
        zeile += 1

        # Eingabe: Punkt 1
        tk.Label(self, text="Punkt 1:").grid(row=zeile, sticky="ew")
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p1_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self, text="Punkt 1 laden", command=lambda: self.lade_punkt1(self.__eingabe_p1_nr.get())).grid(
                row=zeile, sticky="w", column=2)
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

        # Eingabe: Punkt 2
        tk.Label(self, text="Punkt 2:").grid(row=zeile, column=0)
        # Koordinaten laden
        if __name__ != "__main__":
            self.__eingabe_p2_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self, text="Punkt 2 laden", command=lambda: self.lade_punkt2(self.__eingabe_p2_nr.get())).grid(
                row=zeile, sticky="w", column=2)
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

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen, fg="blue").grid(row=zeile, columnspan=spalten_max)
        zeile += 1

        # Ausgabe
        tk.Label(self, text="Ausgabe:", font=("arial", 14, "underline")).grid(row=zeile)
        zeile += 1
        tk.Label(self, text="Strecke:").grid(row=zeile)
        zeile += 1
        tk.Label(self, text="s12:").grid(row=zeile)
        self.__ausgabe_s12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="Richtungswinkel:").grid(row=zeile)
        zeile += 1
        tk.Label(self, text="t12:").grid(row=zeile)
        self.__ausgabe_t12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="").grid(row=zeile, column=0, columnspan=3)
        zeile += 1

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=zeile, column=1, sticky="ew")

    def lade_punkt1(self, p_pktnr: str):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (zweite_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_p1_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, p.hole_x())

    def lade_punkt2(self, p_pktnr: str):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (zweite_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, p.hole_x())

    def testdaten_laden(self):
        """Lädt Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [528.15, 407.65, 795.17, 525.10]

        gui.eingabefeld_schreiben(self.__eingabe_p1_y, testdaten[0])
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, testdaten[1])
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, testdaten[2])
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, testdaten[3])

        self.berechnen()

    def berechnen(self):
        """Übergibt die Eingabewerte an die Berechnungsmethode und schreibt die berechneten Werte in die Ausgabefelder.

        :return: None
        :rtype: None
        """
        p1: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p1_y),
                                  gui.eingabefeld_auswerten(self.__eingabe_p1_x))
        p2: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p2_y),
                                  gui.eingabefeld_auswerten(self.__eingabe_p2_x))

        strecke, richtungswinkel = grundlagen.zweite_grundaufgabe.zweite_grundaufgabe(p1, p2)

        gui.eingabefeld_schreiben(self.__ausgabe_s12, strecke)
        gui.eingabefeld_schreiben(self.__ausgabe_t12, richtungswinkel)


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
