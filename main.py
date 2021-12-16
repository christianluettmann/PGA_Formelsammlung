import json
import tkinter as tk
import grundlagen.winkel_gui
import grundlagen.erste_grundaufgabe_gui
import grundlagen.zweite_grundaufgabe_gui
import gui.menue as mn
import gui.werkzeugleiste as wl
import gui.statusleiste as sl
import gui.arbeitsbereich as ab
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmb

import schnitte_neu.bogenschnitt_gui


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """
        Initialisiert die Anwendung.
        :param master: Master-Anwendung
        :type master: Tk
        """

        super().__init__(master)
        self.grid()

        self.__menue = mn.Menue(self, self.master)
        self.__werkzeugleiste = wl.Werkzeugleiste(self)
        self.__statusleiste = sl.Statusleiste(self)
        self.__arbeitsbereich = ab.Arbeitsbereich(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """
        Initialisiert die GUI.
        :return: None
        :rtype: None
        """

        # Menü
        self.master.config(menu=self.__menue)

        # Werkzeugleiste (in das Grid gepackt)
        self.__werkzeugleiste.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        # Arbeitsbereich (in das Grid gepackt)
        self.__arbeitsbereich.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        # Statusleiste (in das Grid gepackt)
        self.__statusleiste.grid(row=2, column=0, sticky=tk.E+tk.S+tk.W)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    @staticmethod
    def fenster_winkel():
        grundlagen.winkel_gui.Anwendung(tk.Toplevel())

    @staticmethod
    def fenster_erstega():
        grundlagen.erste_grundaufgabe_gui.Anwendung(tk.Toplevel())

    @staticmethod
    def fenster_zweitega():
        grundlagen.zweite_grundaufgabe_gui.Anwendung(tk.Toplevel())

    @staticmethod
    def fenster_bogenschnitt():
        schnitte_neu.bogenschnitt_gui.Anwendung(tk.Toplevel())

    @staticmethod
    def menue_tut_nix():
        tkmb.showinfo("TODO", "Hier passiert noch nix!")

    def menue_datei_oeffnen(self):

        dateitypen = (
            ('JSON-Dateien', '*.json'),
            ('Alle Dateien', '*.*')
        )

        dateiname = tkfd.askopenfilename(
            title="Datei öffnen",
            initialdir="/",
            filetypes=dateitypen
            )

        # JSON aus Datei
        with open(dateiname) as json_datei:
            json_daten = json.load(json_datei)
            self.__arbeitsbereich.setze_text(json.dumps(json_daten, sort_keys=True, indent=4))

    def menue_beenden(self):
        self.master.destroy()


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)

    wurzel.columnconfigure(0, weight=1)
    wurzel.rowconfigure(0, weight=1)

    anwendung.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

    anwendung.mainloop()
