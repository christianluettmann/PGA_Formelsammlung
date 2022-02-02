import tkinter as tk
import grundlagen.punkt as pkt
import gui.tabelle

class Arbeitsbereich(tk.Frame):

    def __init__(self, p_master=None):
        """
        Initialisiert den Arbeitsbereich.
        :param p_master: Master-Anwendung
        :type p_master: Anwendung
        """

        super().__init__(p_master)

        self.__textfeld = tk.Text(self, height=200, width=100)
        self.__tabelle: gui.tabelle.Tabelle = gui.tabelle.Tabelle(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """
        Initialisiert die GUI des Arbeitsbereiches.
        """
        zeile = 0

        # tk.Button(self, text="Winkel", command=self.master.fenster_winkel).grid(row=1)
        # tk.Button(self, text="1. geod. GA", command=self.master.fenster_erstega).grid(row=2)
        # tk.Button(self, text="2. geod. GA", command=self.master.fenster_zweitega).grid(row=3)

        # self.__textfeld.grid(row=4)
        self.__tabelle.grid(row=zeile, column=0)
        zeile += 1

    def setze_tabelle(self, p_pktlst: dict):
        """

        :param p_pktlst:
        :type p_pktlst:
        :return:
        :rtype:
        """
        self.__tabelle.setze_punktliste(p_pktlst)

    def hole_punkt(self, p_pktnr) -> pkt.Punkt:
        """Gibt die Anfrage von der Main-Anwendung an die Tabelle weiter.
        (Punkt aus Tabelle zur Berechnung)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: Punkt
        :rtype: pkt.Punkt
        """
        p: pkt.Punkt = self.__tabelle.hole_punkt(p_pktnr)
        return p

    def sende_punkt(self, p_p: pkt.Punkt):
        """Gibt die Anfrage von der Main-Anwendung an die Tabelle weiter.
        (Punkt aus Berechnung in der Tabelle speichern)

        :param p_p: Punkt
        :type p_p: pkt.Punkt
        :return: None
        :rtype: None
        """
        self.__tabelle.speicher_punkt(p_p)
