import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt


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
        # Punktliste
        self.__pktlst: dict = dict()
        # alle Eingabefelder zur Punktliste (als Instanzvariablen für den klassenweiten Zugriff aus allen Methoden)
        self.__eingabe_pktlst: dict = dict()

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

            # TODO: kann noch optimiert werden
            # Eintrag im Dict zur Aufnahme einer Tabellenzeile von Eingabefeldern
            # self.__eingabe_pktlst[schluessel]: list = list()
            self.__eingabe_pktlst[schluessel]: dict = dict()

            spalte: int = 0

            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "nr", wert.hole_nr())
            spalte += 1

            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "y", wert.hole_y())
            spalte += 1

            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "x", wert.hole_x())
            spalte += 1

            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "epsg", wert.hole_epsg())
            spalte += 1

            zeile += 1

    def erzeuge_eingabefeld(self, p_zeile, p_spalte, p_schluessel, p_attributname, p_attributwert):

        eingabe: tk.Entry = tk.Entry(self)
        self.__eingabe_pktlst[p_schluessel][p_attributname] = eingabe
        self.__eingabe_pktlst[p_schluessel][p_attributname].grid(row=p_zeile, column=p_spalte)
        gui.eingabefeld_schreiben(self.__eingabe_pktlst[p_schluessel][p_attributname], p_attributwert)


    def aenderungen(self):

        # Inhalt der Punktliste komplett löschen
        self.__pktlst.clear()
        # TODO: Soll wirklich die gesamte Tabelle wieder durchlaufen werden?
        for schluessel, wert in self.__eingabe_pktlst.items():

            nr: str = self.__eingabe_pktlst[schluessel]["nr"].get()
            y: float = gui.eingabefeld_auswerten(self.__eingabe_pktlst[schluessel]["y"])
            x: float = gui.eingabefeld_auswerten(self.__eingabe_pktlst[schluessel]["x"])
            epsg: int = gui.eingabefeld_auswerten(self.__eingabe_pktlst[schluessel]["epsg"])

            p: pkt.Punkt = pkt.Punkt(y, x, nr, epsg)

            self.__pktlst[nr] = p

        print("Stop")
        print(self.__pktlst)
