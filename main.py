import json

import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmb

import grundlagen.punkt as pkt
import grundlagen.punktliste as pktlst
import grundlagen.winkel_gui
import grundlagen.erste_grundaufgabe_gui
import grundlagen.zweite_grundaufgabe_gui

import schnitte.rueckwaertsschnitt_gui
import schnitte.vorwaertsschnitt_dreieckswinkel_gui
import schnitte.vorwaertsschnitt_richtungswinkel_gui
import schnitte.bogenschnitt_gui

import gui.menue
import gui.werkzeugleiste
import gui.statusleiste
import gui.arbeitsbereich
import gui.berechnungsfenster
import gui.tabelle

import polygonzug_package.polygonzug_beidseitig_gui
import polygonzug_package.polygonzug_ring_gui


class Anwendung(tk.Tk):

    def __init__(self):
        """Initialisiert die Anwendung.

        """
        super().__init__()
        self.minsize(600, 400)
        self.grid()

        # GUI
        self.__menue = gui.menue.Menue(self)
        self.__werkzeugleiste = gui.werkzeugleiste.Werkzeugleiste(self)
        self.__statusleiste = gui.statusleiste.Statusleiste(self)
        self.__arbeitsbereich = gui.arbeitsbereich.Arbeitsbereich(self)

        # DATEN
        self.__pktlst: dict = {}

        self.initialisiere_gui()

    def initialisiere_gui(self) -> None:
        """Initialisiert die GUI.

        :return: None
        :rtype: None
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

        self.option_add("*font", "arial 11")
        self.title("PGA Formelsammlung")

    @staticmethod
    def fenster_winkel():
        top = gui.berechnungsfenster.Berechnungsfenster()
        grundlagen.winkel_gui.Anwendung(top)

    @staticmethod
    def fenster_erste_grundaufgabe():
        top = gui.berechnungsfenster.Berechnungsfenster()
        grundlagen.erste_grundaufgabe_gui.Anwendung(top)

    @staticmethod
    def fenster_zweite_grundaufgabe():
        top = gui.berechnungsfenster.Berechnungsfenster()
        grundlagen.zweite_grundaufgabe_gui.Anwendung(top)

    @staticmethod
    def fenster_bogenschnitt():
        top = gui.berechnungsfenster.Berechnungsfenster()
        schnitte.bogenschnitt_gui.Anwendung(top)

    @staticmethod
    def fenster_rueckwaertsschnitt():
        top = gui.berechnungsfenster.Berechnungsfenster()
        schnitte.rueckwaertsschnitt_gui.Anwendung(top)

    @staticmethod
    def fenster_vorwaertsschnitt_dreieckswinkel():
        top = gui.berechnungsfenster.Berechnungsfenster()
        schnitte.vorwaertsschnitt_dreieckswinkel_gui.Anwendung(top)

    @staticmethod
    def fenster_vorwaertsschnitt_richtungswinkel():
        top = gui.berechnungsfenster.Berechnungsfenster()
        schnitte.vorwaertsschnitt_richtungswinkel_gui.Anwendung(top)

    @staticmethod
    def fenster_polygonzug_beidseitig():
        top = gui.berechnungsfenster.Berechnungsfenster()
        polygonzug_package.polygonzug_beidseitig_gui.Anwendung(top)

    @staticmethod
    def fenster_polygonzug_ring():
        top = gui.berechnungsfenster.Berechnungsfenster()
        polygonzug_package.polygonzug_ring_gui.Anwendung(top)

    @staticmethod
    def menue_tut_nix():
        tkmb.showinfo("TODO", "Hier passiert noch nix!")

    def menue_datei_importieren(self) -> None:
        """Öffnet eine JSON-Datei mit einer Punktliste und schreibt diese in die Tabelle.

        :return: None
        :rtype: None
        """
        # TODO: Was passiert, wenn die JSON-Datei keine Punktliste ist?
        # Datei festlegen
        dateiname = tkfd.askopenfilename(
            title="Datei öffnen",
            initialdir="/Desktop",
            filetypes=(('JSON-Dateien', '*.json'), ('Alle Dateien', '*.*'))
            )
        # JSON-Daten aus Datei lesen
        with open(dateiname) as json_datei:
            json_daten = json.load(json_datei)
            self.__pktlst = pktlst.json2punktliste(json_daten).copy()
            self.__arbeitsbereich.setze_tabelle(self.__pktlst)

    def menue_exportieren(self) -> None:
        """Schreibt den Inhalt der Punktliste in eine JSON-Datei.

        :return: None
        :rtype: None
        """
        # Datei festlegen
        dateiname = tkfd.asksaveasfile(
            mode="w",
            title="Datei exportieren",
            initialdir="/Desktop",
            defaultextension=".json",
            filetypes=(('JSON-Dateien', '*.json'), ('Alle Dateien', '*.*')),
        )
        # JSON-Datei schreiben
        inhalt = json.dumps(self.__arbeitsbereich.hole_punktliste(), indent=4)
        dateiname.write(inhalt)
        dateiname.close()

    def menue_beenden(self):
        self.destroy()

    def lade_punkt(self, p_pktnr) -> pkt.Punkt:
        """Gibt die Anfrage vom Berechnungsfenster an den Arbeitsbereich weiter.
        (Punkt aus Tabelle zur Berechnung)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: Punkt
        :rtype: pkt.Punkt
        """
        return self.__arbeitsbereich.hole_punkt(p_pktnr)

    def sende_punkt(self, p_p: pkt.Punkt) -> None:
        """Gibt die Anfrage vom Berechnungsfenster an den Arbeitsbereich weiter.
        (Punkt aus Berechnung in der Tabelle speichern)

        :param p_p: Punkt
        :type p_p: pkt.Punkt
        :return: None
        :rtype: None
        """
        self.__arbeitsbereich.sende_punkt(p_p)


if __name__ == "__main__":

    anwendung = Anwendung()
    anwendung.mainloop()
