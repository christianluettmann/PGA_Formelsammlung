import tkinter as tk
import grundlagen.punkt as pkt


class Arbeitsbereich(tk.Frame):

    def __init__(self, p_master=None):
        """
        Initialisiert den Arbeitsbereich.
        :param p_master: Master-Anwendung
        :type p_master: Anwendung
        """

        super().__init__(p_master)

        self.__textfeld = tk.Text(self, height=200, width=100)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """
        Initialisiert die GUI des Arbeitsbereiches.
        """
        # tk.Button(self, text="Winkel", command=self.master.fenster_winkel).grid(row=1)
        # tk.Button(self, text="1. geod. GA", command=self.master.fenster_erstega).grid(row=2)
        # tk.Button(self, text="2. geod. GA", command=self.master.fenster_zweitega).grid(row=3)

        self.__textfeld.grid(row=4)

    def setze_text(self, p_text: str):
        """
        Setzt einen Text in ein Textfeld.
        :param p_text: Text
        :type p_text: str
        """
        self.__textfeld.insert(tk.END, p_text)

    def hole_punkt(self) -> pkt.Punkt:
        """

        :return: Punkt
        :rtype: pkt.Punkt
        """

        p: pkt.Punkt = pkt.Punkt(1234.56, 78.9, "Arbeitsbereich", 4326)

        return p

    def sende_punkt(self, p_p: pkt.Punkt):

        self.setze_text(str(p_p))
