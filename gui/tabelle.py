import tkinter as tk
import grundlagen.gui as gui


class Tabelle(tk.Frame):
    """
    Klasse Tabelle
    """

    def __init__(self, p_master):
        """

        :param p_master:
        :type p_master:
        """
        super().__init__(p_master)

        self.__zeilen_anzahl: int = 0
        self.__spalten_anzahl: int = 0
        self.__pktlst: dict = dict()

        self.initialisiere_gui()

    def initialisiere_gui(self):

        self.grid()

    def setze_punktliste(self, p_pktlst: dict):

        self.__pktlst = p_pktlst    # beide dict belegen einen identischen Speicherplatz
        self.__zeilen_anzahl = len(p_pktlst)
        self.__spalten_anzahl = 4   # nr, y, x, epsg

        zeile: int = 0

        tk.Button(self, text="Änderungen übernehmen", command=self.aenderungen).grid(row=zeile, column=4)
        zeile += 1

        tk.Label(self, text="Punktnummer").grid(row=zeile, column=0)
        tk.Label(self, text="Rechtswert").grid(row=zeile, column=1)
        tk.Label(self, text="Hochwert").grid(row=zeile, column=2)
        tk.Label(self, text="EPSG-Code").grid(row=zeile, column=3)
        zeile += 1

        for schluessel, wert in self.__pktlst.items():

            eingabe_nr: tk.Entry = tk.Entry(self)
            eingabe_nr.grid(row=zeile, column=0)
            gui.eingabefeld_schreiben(eingabe_nr, wert.hole_nr())

            eingabe_y: tk.Entry = tk.Entry(self)
            eingabe_y.grid(row=zeile, column=1)
            gui.eingabefeld_schreiben(eingabe_y, wert.hole_y())

            eingabe_x: tk.Entry = tk.Entry(self)
            eingabe_x.grid(row=zeile, column=2)
            gui.eingabefeld_schreiben(eingabe_x, wert.hole_x())

            eingabe_epsg: tk.Entry = tk.Entry(self)
            eingabe_epsg.grid(row=zeile, column=3)
            gui.eingabefeld_schreiben(eingabe_epsg, wert.hole_epsg())

            zeile += 1

    def aenderungen(self):

        for schluessel, wert in self.__pktlst.items():

            # Nur zu Demozwecken, später aus Eingabefeldern der Tabelle übernehmen
            self.__pktlst[schluessel].setze_y(99)

        print("Stop")
