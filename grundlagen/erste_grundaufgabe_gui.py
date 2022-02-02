import tkinter as tk
import grundlagen.erste_grundaufgabe
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import random


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung.

        :param master: Anwendung
        :type master: Anwendung
        """
        super().__init__(master)

        self.__eingabe_p1_nr: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_x: tk.Entry = tk.Entry(self)
        self.__eingabe_s12: tk.Entry = tk.Entry(self)
        self.__eingabe_t12: tk.Entry = tk.Entry(self)

        self.__ausgabe_p2_nr: tk.Entry = tk.Entry(self)
        self.__ausgabe_p2_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_p2_x: tk.Entry = tk.Entry(self)

        self.grid()

        zeile: int = 0
        spalten_max: int = 3

        self.master.title("1. Grundaufgabe")

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
                      command=lambda: self.lade_punkt(self.__eingabe_p1_nr.get()))\
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

        # Eingabe: Strecke
        tk.Label(self, text="Strecke:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="s12:").grid(row=zeile)
        self.__eingabe_s12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Eingabe: Richtungswinkel
        tk.Label(self, text="Richtungswinkel:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="t12:").grid(row=zeile)
        self.__eingabe_t12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=zeile, columnspan=spalten_max)
        zeile += 1

        # Ausgabe
        tk.Label(self, text="Ausgabe:").grid(row=zeile)
        zeile += 1

        # Ausgabe:Punkt2
        tk.Label(self, text="Punkt2:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        # Koordinaten laden
        if __name__ != "__main__":
            self.__ausgabe_p2_nr.grid(row=zeile, column=1, sticky="ew")
            tk.Button(self,
                      text="Punkt2 speichern",
                      command=self.speicher_punkt) \
                .grid(row=zeile, sticky="w", column=2)
        zeile += 1
        # Koordinaten eingeben
        tk.Label(self, text="y2:").grid(row=zeile)
        self.__ausgabe_p2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x2:").grid(row=zeile)
        self.__ausgabe_p2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=zeile, columnspan=spalten_max)

    def berechnen(self):
        """Übergibt die Eingabewerte an die Berechnungsmethode und schreibt die berechneten Werte in die Ausgabefelder.

        :return: None
        :rtype: None
        """
        p1: pkt.Punkt = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p1_y), gui.eingabefeld_auswerten(self.__eingabe_p1_x))
        s12: float = gui.eingabefeld_auswerten(self.__eingabe_s12)
        t12: float = gui.eingabefeld_auswerten(self.__eingabe_t12)

        ergebnis: pkt.Punkt = grundlagen.erste_grundaufgabe.erstegrundaufgabe(p1, s12, t12)

        gui.eingabefeld_schreiben(self.__ausgabe_p2_y, ergebnis.hole_y())
        gui.eingabefeld_schreiben(self.__ausgabe_p2_x, ergebnis.hole_x())

    def testdaten_laden(self):
        """Lädt zufällige Testdaten für die Berechnung und führt die Berechnung durch.

        :return: None
        :rtype: None
        """
        testdaten = [
            [713.64, 496.72, 135.25, 32.9645],
            [16.10, 23.06, 17.11, 214.1990]
        ]

        i = random.randint(0, len(testdaten) - 1)
        gui.eingabefeld_schreiben(self.__eingabe_p1_y, testdaten[i][0])
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, testdaten[i][1])
        gui.eingabefeld_schreiben(self.__eingabe_s12, testdaten[i][2])
        gui.eingabefeld_schreiben(self.__eingabe_t12, testdaten[i][3])

        self.berechnen()

    def lade_punkt(self, p_pktnr):
        """Lädt einen Punkt aus der Main-Punktliste und fügt ihn in die Eingabefelder ein.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: None
        :rtype: None
        """
        # self ist ein Frame
        # self.master ist das Toplevel-Fenster, dass den Frame enthält
        # self.master.master ist die Hauptanwendung, aus der das Toplevel-Fenster aufgerufen wird
        # self.master.master.__arbeitsbereich ist Instanzvariable
        # je eine hole_punkt Methode in jedem master
        p: pkt.Punkt = self.master.lade_punkt(p_pktnr)
        gui.eingabefeld_schreiben(self.__eingabe_p1_y, p.hole_y())
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, p.hole_x())

    def speicher_punkt(self):
        """Speichert den berechneten Punkt in die Main-Punktliste.
        (erste_grundaufgabe_gui -> berechnungsfenster -> main -> arbeitsbereich -> tabelle)

        :return: None
        :rtype: None
        """
        p: pkt.Punkt = pkt.Punkt(
            gui.eingabefeld_auswerten(self.__ausgabe_p2_y),
            gui.eingabefeld_auswerten(self.__ausgabe_p2_x),
            self.__ausgabe_p2_nr.get(),
            0)   # TODO
        self.master.sende_punkt(p)


if __name__ == "__main__":

    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
