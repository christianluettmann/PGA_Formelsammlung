import tkinter as tk
from grundlagen.erste_grundaufgabe import *
import grundlagen.gui as gui


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        # Oberfläche initialisieren
        tk.Label(self, text="Erste geodätische Grundaufgabe").grid(row=0, columnspan=3)
        tk.Label(self, text="gegeben:").grid(row=1, column=0)
        tk.Label(self, text="y1 [m]").grid(row=2, column=0)
        tk.Label(self, text="x1 [m]").grid(row=3, column=0)
        tk.Label(self, text="s12 [m]").grid(row=4, column=0)
        tk.Label(self, text="t12 [gon]").grid(row=5, column=0)

        self.eingabe_y1 = tk.Entry(self)
        self.eingabe_x1 = tk.Entry(self)
        self.eingabe_s12 = tk.Entry(self)
        self.eingabe_t12 = tk.Entry(self)
        self.ausgabe_y2 = tk.Entry(self)
        self.ausgabe_x2 = tk.Entry(self)

        self.eingabe_y1.grid(row=2, column=1)
        self.eingabe_x1.grid(row=3, column=1)
        self.eingabe_s12.grid(row=4, column=1)
        self.eingabe_t12.grid(row=5, column=1)
        self.ausgabe_y2.grid(row=8, column=1)
        self.ausgabe_x2.grid(row=9, column=1)

        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=6, columnspan=3)

        tk.Label(self, text="Ergebnis:").grid(row=7, column=0)
        tk.Label(self, text="y2 [m]").grid(row=8, column=0)
        tk.Label(self, text="x2 [m]").grid(row=9, column=0)

        tk.Button(self, text="Beenden", command=self.master.destroy, fg="red").grid(row=10, columnspan=3)

    def berechnen(self):
        p1 = pkt.Punkt(gui.eingabefeld_auswerten(self.eingabe_y1), gui.eingabefeld_auswerten(self.eingabe_x1))

        s12 = gui.eingabefeld_auswerten(self.eingabe_s12)
        t12 = gui.eingabefeld_auswerten(self.eingabe_t12)

        ergebnis = erstegrundaufgabe(p1, s12, t12)

        # Ergebnis visualisieren
        gui.eingabefeld_schreiben(self.ausgabe_y2, ergebnis.hole_y())
        gui.eingabefeld_schreiben(self.ausgabe_x2, ergebnis.hole_x())


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
