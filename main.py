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
import grundlagen.punkt as pkt
import gui.berechnungsfenster
import grundlagen.punktliste as pktlst


class Anwendung(tk.Tk):

    def __init__(self):
        """
        Initialisiert die Anwendung.
        """
        super().__init__()
        self.grid()

        # GUI
        self.__menue = mn.Menue(self)
        self.__werkzeugleiste = wl.Werkzeugleiste(self)
        self.__statusleiste = sl.Statusleiste(self)
        self.__arbeitsbereich = ab.Arbeitsbereich(self)

        # DATEN
        self.__pktlst: dict = {}

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """
        Initialisiert die GUI.
        """

        # Menü
        self.config(menu=self.__menue)

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
        top = gui.berechnungsfenster.Berechnungsfenster()
        grundlagen.winkel_gui.Anwendung(top)

    @staticmethod
    def fenster_erstega():
        top = gui.berechnungsfenster.Berechnungsfenster()
        grundlagen.erste_grundaufgabe_gui.Anwendung(top)

    @staticmethod
    def fenster_zweitega():
        top = gui.berechnungsfenster.Berechnungsfenster()
        grundlagen.zweite_grundaufgabe_gui.Anwendung(top)

    @staticmethod
    def fenster_bogenschnitt():
        top = gui.berechnungsfenster.Berechnungsfenster()
        schnitte_neu.bogenschnitt_gui.Anwendung(top)

    @staticmethod
    def menue_tut_nix():
        tkmb.showinfo("TODO", "Hier passiert noch nix!")

    def menue_datei_oeffnen(self):  #TODO: Was passiert, wenn die JSON-Datei keine Punktliste ist?

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

            self.__pktlst = pktlst.json2punktliste(json_daten).copy()

            # self.__arbeitsbereich.setze_text(json.dumps(json_daten, sort_keys=True, indent=4))

            for schluessel, wert in self.__pktlst.items():
                self.__arbeitsbereich.setze_text((str(wert)+"\n"))

    def menue_beenden(self):
        self.destroy()

    def lade_punkt(self) -> pkt.Punkt:
        return self.__arbeitsbereich.hole_punkt()

    def sende_punkt(self, p_p: pkt.Punkt):
        self.__arbeitsbereich.sende_punkt(p_p)


if __name__ == "__main__":

    anwendung = Anwendung()
    anwendung.mainloop()
