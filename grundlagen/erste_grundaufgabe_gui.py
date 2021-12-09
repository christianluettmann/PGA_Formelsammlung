import tkinter as tk
import grundlagen.erste_grundaufgabe as eg
import grundlagen.gui as gui
import grundlagen.punkt as pkt


class Anwendung(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.grid()

        tk.Label(self, text="1. Geodätische Hauptaufgabe").grid(row=0, columnspan=3)

        tk.Label(self, text="Rechts:\ny1[m]").grid(row=1, column=1)
        tk.Label(self, text="Hoch:\nx1[m]").grid(row=1, column=2)
        tk.Label(self, text="Strecke:\ns12[m]").grid(row=1, column=3)
        tk.Label(self, text="RiWi:\nt12[gon]").grid(row=1, column=4)
        tk.Label(self, text="Rechts:\ny2[m]").grid(row=1, column=5)
        tk.Label(self, text="Hoch:\nx2[m]").grid(row=1, column=6)

        self.eingaberechts = tk.Entry(self)
        self.eingabehoch = tk.Entry(self)
        self.eingabestrecke = tk.Entry(self)
        self.eingaberiwi = tk.Entry(self)
        self.eingaberechts2 = tk.Entry(self)
        self.eingabehoch2 = tk.Entry(self)

        self.eingaberechts.grid(row=2, column=1)
        self.eingabehoch.grid(row=2, column=2)
        self.eingabestrecke.grid(row=2, column=3)
        self.eingaberiwi.grid(row=2, column=4)
        self.eingaberechts2.grid(row=2, column=5)
        self.eingabehoch2.grid(row=2, column=6)

        tk.Button(self, text="Umrechnen", command=self.berechnen).grid(row=3, columnspan=4)
        tk.Button(self, text="Beenden", command=self.master.destroy).grid(row=3, columnspan=6)

    def berechnen(self):
        p1 = pkt.Punkt(gui.eingabefeld_auswerten(self.eingaberechts), gui.eingabefeld_auswerten(self.eingabehoch))
        s12 = gui.eingabefeld_auswerten(self.eingabestrecke)
        t12 = gui.eingabefeld_auswerten(self.eingaberiwi)

        ergebnis = eg.erstegrundaufgabe(p1, s12, t12)
        gui.eingabefeld_schreiben(self.eingaberechts2, ergebnis.hole_y())
        gui.eingabefeld_schreiben(self.eingabehoch2, ergebnis.hole_x())

if __name__ == "__main__":

    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()