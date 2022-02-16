import tkinter as tk
import grundlagen.winkel as wk
import grundlagen.gui as gui


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """Initialisiert die Anwendung

        :param master: Berechnungsfenster
        :type master: Berechnungsfenster
        """

        super().__init__(master)
        self.grid()

        self.master.title("Winkelumrechnung")

        tk.Label(self, text="Winkelumrechnung", font=("arial", 14, "underline")).grid(row=0, columnspan=3)

        tk.Label(self, text="Rad:").grid(row=1)
        tk.Label(self, text="Deg:").grid(row=2)
        tk.Label(self, text="Gon:").grid(row=3)

        self.eingaberad: tk.Entry = tk.Entry(self)
        self.eingabedeg: tk.Entry = tk.Entry(self)
        self.eingabegon: tk.Entry = tk.Entry(self)

        self.eingaberad.grid(row=1, column=1)
        self.eingabedeg.grid(row=2, column=1)
        self.eingabegon.grid(row=3, column=1)

        tk.Button(self, text="Umrechnen", command=self.umrechnenrad, fg="blue").grid(row=1, column=2)
        tk.Button(self, text="Umrechnen", command=self.umrechnendeg, fg="blue").grid(row=2, column=2)
        tk.Button(self, text="Umrechnen", command=self.umrechnengon, fg="blue").grid(row=3, column=2)

        tk.Button(self, text="Beenden", command=self.master.destroy, fg="red").grid(row=4, column=1, sticky="ew")

    def umrechnenrad(self):
        rad: float = gui.eingabefeld_auswerten(self.eingaberad)

        gui.eingabefeld_schreiben(self.eingabedeg, wk.Winkel.rad2deg(rad))
        gui.eingabefeld_schreiben(self.eingabegon, wk.Winkel.rad2gon(rad))

    def umrechnendeg(self):
        deg: float = gui.eingabefeld_auswerten(self.eingabedeg)

        gui.eingabefeld_schreiben(self.eingaberad, wk.Winkel.deg2rad(deg))
        gui.eingabefeld_schreiben(self.eingabegon, wk.Winkel.deg2gon(deg))

    def umrechnengon(self):
        gon: float = gui.eingabefeld_auswerten(self.eingabegon)

        gui.eingabefeld_schreiben(self.eingaberad, wk.Winkel.gon2rad(gon))
        gui.eingabefeld_schreiben(self.eingabedeg, wk.Winkel.gon2deg(gon))


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
