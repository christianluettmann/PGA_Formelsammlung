import tkinter as tk
import grundlagen.zweite_grundaufgabe as zg
import grundlagen.punkt as pkt


class Anwendung(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.grid()

        tk.Label(self, text="2. geodätische Hauptaufgabe").grid(row=0, columnspan=3)

        tk.Label(self, text="Punkt 1").grid(row=1, column=1)
        tk.Label(self, text="Punkt 2").grid(row=1, column=2)
        tk.Label(self, text=" ").grid(row=1, column=3)
        tk.Label(self, text="Gesucht").grid(row=1, column=4)

        tk.Label(self, text="Rechts: y[m]").grid(row=2, column=0)
        tk.Label(self, text="Hoch: x[m]").grid(row=3, column=0)
        tk.Label(self, text="Strecke:").grid(row=3, column=4)
        tk.Label(self, text="Winkel [gon]").grid(row=3, column=5)

        self.eingabe_y1 = tk.Entry(self)
        self.eingabe_x1 = tk.Entry(self)
        self.eingabe_y2 = tk.Entry(self)
        self.eingabe_x2 = tk.Entry(self)
        self.ergebnis_s12 = tk.Entry(self)
        self.ergebnis_t12 = tk.Entry(self)

        self.eingabe_y1.grid(row=2, column=1)
        self.eingabe_x1.grid(row=3, column=1)
        self.eingabe_y2.grid(row=2, column=2)
        self.eingabe_x2.grid(row=3, column=2)
        self.ergebnis_s12.grid(row=2, column=4)
        self.ergebnis_t12.grid(row=2, column=5)

        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=8, columnspan=5)
        tk.Button(self, text="Beenden", command=self.master.destroy).grid(row=8, columnspan=3)

    def berechnen(self):

        p1 = pkt.Punkt(float(self.eingabe_y1.get()), float(self.eingabe_x1.get()))
        p2 = pkt.Punkt(float(self.eingabe_y2.get()), float(self.eingabe_x2.get()))
        #p1 = pkt.Punkt(528.15, 407.65)
        #p2 = pkt.Punkt(795.17, 525.10)
        ergebnis = zg.zweitegrundaufgabe(p1, p2)
        s12 = ergebnis[0]
        t12 = ergebnis[1]

        self.ergebnis_s12.delete(0, tk.END)
        self.ergebnis_t12.delete(0, tk.END)

        self.ergebnis_s12.insert(0, s12)
        self.ergebnis_t12.insert(0, t12)


if __name__ == "__main__":

    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
