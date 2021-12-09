import tkinter as tk
from math import *
import grundlagen.winkel as wk
import mein_paket.mein_paket_modul as mpm
import grundlagen.gui as gui


class Anwendung(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.grid()

        param = 5
        ergebnis = mpm.meine_paket_modul_funktion(param)
        print(ergebnis)

        tk.Label(self, text="Winkelumrechnung").grid(row=0, columnspan=3)

        tk.Label(self, text="Rad:").grid(row=1)
        tk.Label(self, text="Deg:").grid(row=2)
        tk.Label(self, text="Gon:").grid(row=3)

        self.eingaberad = tk.Entry(self)
        self.eingabedeg = tk.Entry(self)
        self.eingabegon = tk.Entry(self)

        self.eingaberad.grid(row=1, column=1)
        self.eingabedeg.grid(row=2, column=1)
        self.eingabegon.grid(row=3, column=1)

        tk.Button(self, text="Umrechnen", command=self.umrechnenrad).grid(row=1, column=2)
        tk.Button(self, text="Umrechnen", command=self.umrechnendeg).grid(row=2, column=2)
        tk.Button(self, text="Umrechnen", command=self.umrechnengon).grid(row=3, column=2)

        tk.Button(self, text="Beenden", command=self.master.destroy).grid(row=4, columnspan=3)

    def umrechnenrad(self):
        rad = gui.eingabefeld_auswerten(self.eingaberad)


        gui.eingabefeld_schreiben(self.eingabedeg, wk.Winkel.rad2deg(rad))
        gui.eingabefeld_schreiben(self.eingabegon, wk.Winkel.rad2gon(rad))

    def umrechnendeg(self):
        deg = gui.eingabefeld_auswerten(self.eingabedeg)

        gui.eingabefeld_schreiben(self.eingaberad, wk.Winkel.deg2rad(deg))
        gui.eingabefeld_schreiben(self.eingabegon, wk.Winkel.deg2gon(deg))

    def umrechnengon(self):
        gon = gui.eingabefeld_auswerten(self.eingabegon)


        gui.eingabefeld_schreiben(self.eingaberad, wk.Winkel.gon2rad(gon))
        gui.eingabefeld_schreiben(self.eingabedeg, wk.Winkel.gon2deg(gon))


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()