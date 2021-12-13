import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import schnitte_neu.bogenschnitt


class Anwendung(tk.Frame):

    def __init__(self, p_master=None):
        super().__init__(p_master)

        # GUI
        self.__eingabe_p1_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p1_x: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_y: tk.Entry = tk.Entry(self)
        self.__eingabe_p2_x: tk.Entry = tk.Entry(self)

        self.__eingabe_s1_laenge: tk.Entry = tk.Entry(self)
        self.__eingabe_s2_laenge: tk.Entry = tk.Entry(self)
        self.__eingabe_s3_laenge: tk.Entry = tk.Entry(self)

        self.__ausgabe_pn1_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn1_x: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn2_y: tk.Entry = tk.Entry(self)
        self.__ausgabe_pn2_x: tk.Entry = tk.Entry(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):

        self.grid()

        zeile = 0
        spalten_max = 3

        self.master.title("Bogenschnitt")

        # Gegeben
        tk.Label(self, text="Gegeben:").grid(row=zeile, columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="y1:").grid(row=zeile)
        self.__eingabe_p1_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x1:").grid(row=zeile)
        self.__eingabe_p1_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="y2:").grid(row=zeile)
        self.__eingabe_p2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x2:").grid(row=zeile)
        self.__eingabe_p2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Gemessen
        tk.Label(self, text="Gemessen:").grid(row=zeile, columnspan=spalten_max)
        zeile += 1
        tk.Label(self, text="s1:").grid(row=zeile)
        self.__eingabe_s1_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="s2:").grid(row=zeile)
        self.__eingabe_s2_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="s3:").grid(row=zeile)
        self.__eingabe_s3_laenge.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Berechnen Button
        tk.Button(self, text="Berechnen", command=self.berechnen).grid(row=zeile, columnspan=spalten_max)
        zeile += 1

        # Ergebnisse

        tk.Label(self, text="Punkt N1 (?rechts? der Linie):").grid(row=zeile, columnspan=spalten_max)   # TODO: überprüfen rechts/links
        zeile += 1
        tk.Label(self, text="y1:").grid(row=zeile)
        self.__ausgabe_pn1_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x1:").grid(row=zeile)
        self.__ausgabe_pn1_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="Punkt N2 (?links? der Linie):").grid(row=zeile, columnspan=spalten_max)    # TODO: überprüfen rechts/links
        zeile += 1
        tk.Label(self, text="y1:").grid(row=zeile)
        self.__ausgabe_pn2_y.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1
        tk.Label(self, text="x1:").grid(row=zeile)
        self.__ausgabe_pn2_x.grid(row=zeile, column=1, sticky="ew")
        tk.Label(self, text="[m]").grid(row=zeile, column=2, sticky="w")
        zeile += 1

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=zeile, columnspan=spalten_max)

    def berechnen(self):
        p1_y = gui.eingabefeld_auswerten(self.__eingabe_p1_y)
        p1_x = gui.eingabefeld_auswerten(self.__eingabe_p1_x)
        p2_y = gui.eingabefeld_auswerten(self.__eingabe_p2_y)
        p2_x = gui.eingabefeld_auswerten(self.__eingabe_p2_x)
        s1 = gui.eingabefeld_auswerten(self.__eingabe_s1_laenge)
        s2 = gui.eingabefeld_auswerten(self.__eingabe_s2_laenge)

        ergebnis = schnitte_neu.bogenschnitt.Bogenschnitt.berechnen(p1_y, p1_x, s1, p2_y, p2_x, s2)

        gui.eingabefeld_schreiben(self.__ausgabe_pn1_y, ergebnis[0])
        gui.eingabefeld_schreiben(self.__ausgabe_pn1_x, ergebnis[1])
        gui.eingabefeld_schreiben(self.__ausgabe_pn2_y, ergebnis[2])
        gui.eingabefeld_schreiben(self.__ausgabe_pn2_x, ergebnis[3])


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
