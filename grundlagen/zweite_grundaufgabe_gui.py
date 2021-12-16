import tkinter as tk
import grundlagen.zweite_grundaufgabe as zg
import grundlagen.punkt as pkt
import grundlagen.gui as gui
import random


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.__eingabe_p1_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_x: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_x: tk.Entry = tk.Entry(self)

        self.__ergebnis_s12: tk.Entry = tk.Entry(self)
        self.__ergebnis_t12: tk.Entry = tk.Entry(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):

        self.grid()

        zeile = 0
        spalten_max = 3

        self.master.title("2. Grundaufgabe")

        # Gegeben
        tk.Label(self, text="Gegeben:").grid(row=zeile)
        tk.Button(self, text="Testdaten laden", command=self.testdaten_laden).grid(row=zeile, column=spalten_max, sticky="e", columnspan=spalten_max-1)
        zeile += 1
        tk.Label(self, text="Punkt1:").grid(row=zeile, sticky="w")
        # Koordinaten laden
        if __name__ != "__main__":
            tk.Button(self, text="Punkt1 laden").grid(row=zeile, sticky="w", column=spalten_max)

        zeile += 1
        tk.Label(self, text="y1:").grid(row=zeile)
        self.__eingabe_p1_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x1:").grid(row=zeile)
        self.__eingabe_p1_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="Punkt2:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        # Koordinaten laden
        if __name__ != "__main__":
            tk.Button(self, text="Punkt2 laden").grid(row=zeile, sticky="w", column=spalten_max)

        zeile += 1
        tk.Label(self, text="y2:").grid(row=zeile)
        self.__eingabe_p2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x2:").grid(row=zeile)
        self.__eingabe_p2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=zeile, columnspan=spalten_max)
        zeile += 1

        # Ergebnisse
        tk.Label(self, text="Strecke:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="s12:").grid(row=zeile)
        self.__ergebnis_s12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="Richtungswinkel:").grid(row=zeile, sticky="w", columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="t12:").grid(row=zeile)
        self.__ergebnis_t12.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[gon]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=zeile, columnspan=spalten_max)

        # Temp Buttons:
        tk.Button(self, text="Lade Punkt", command=self.lade_punkt).grid(row=31, columnspan=3)
        tk.Button(self, text="Send Punkt", command=self.sende_punkt_knopf).grid(row=32, columnspan=3)

    def lade_punkt(self):

        # self ist ein Frame
        # self.master ist das Toplevel-Fenster, dass den Frame enthält
        # self.master.master ist die Hauptanwendung, aus der das Toplevel-Fenster aufgerufen wird
        # self.master.master.__arbeitsbereich ist Instanzvariable
        # je eine hole_punkt Methode in jedem master
        p: pkt.Punkt = self.master.lade_punkt()
        print(p)

    def sende_punkt(self, p_p: pkt.Punkt):

        self.master.sende_punkt(p_p)

    def sende_punkt_knopf(self):    # TODO: temp

        p: pkt.Punkt = pkt.Punkt(987.6, 543.2, "2. Grund Sende", 1234)

        self.sende_punkt(p)

    def testdaten_laden(self):
        testdaten = [
            [528.15, 407.65, 795.17, 525.10],
            [16.10, 23.06, 12.32, 6.37]
        ]

        i = random.randint(0, len(testdaten)-1)
        gui.eingabefeld_schreiben(self.__eingabe_p1_y, testdaten[i][0])
        gui.eingabefeld_schreiben(self.__eingabe_p1_x, testdaten[i][1])
        gui.eingabefeld_schreiben(self.__eingabe_p2_y, testdaten[i][2])
        gui.eingabefeld_schreiben(self.__eingabe_p2_x, testdaten[i][3])

        self.berechnen()

    def berechnen(self):

        p1 = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p1_y), gui.eingabefeld_auswerten(self.__eingabe_p1_x))
        p2 = pkt.Punkt(gui.eingabefeld_auswerten(self.__eingabe_p2_y), gui.eingabefeld_auswerten(self.__eingabe_p2_x))

        ergebnis = zg.zweitegrundaufgabe(p1, p2)

        gui.eingabefeld_schreiben(self.__ergebnis_s12, ergebnis[0])
        gui.eingabefeld_schreiben(self.__ergebnis_t12, ergebnis[1])


if __name__ == "__main__":

    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
