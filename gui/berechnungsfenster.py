import tkinter as tk
import grundlagen.punkt as pkt


class Berechnungsfenster(tk.Toplevel):

    def __init__(self):

        super().__init__()

    def lade_punkt(self, p_pktnr: str) -> pkt.Punkt:
        """Gibt die Anfrage von der Berechnung an die Main-Anwendung weiter.
        (Punkt aus Tabelle zur Berechnung)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: Punkt
        :rtype: pkt.Punkt
        """
        return self.master.lade_punkt(p_pktnr)

    def sende_punkt(self, p_p: pkt.Punkt) -> None:
        """Gibt die Anfrage von der Berechnung an die Main-Anwendung weiter.
        (Punkt aus Berechnung in der Tabelle speichern)

        :param p_p: Punkt
        :type p_p: pkt.Punkt
        :return: None
        :rtype: None
        """
        self.master.sende_punkt(p_p)
