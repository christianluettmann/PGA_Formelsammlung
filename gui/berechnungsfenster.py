import tkinter as tk
import tkinter.filedialog as tkfd
import json

import grundlagen.punkt as pkt
import grundlagen.punktliste as pktlst


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


def import_json_dialog() -> dict:
    """Importdialog fuer das Laden von JSON-Dateien.

            :return: JSON-Daten
            :rtype: dict
            """
    # Datei festlegen
    dateiname: str = tkfd.askopenfilename(title="Polygonzug laden",
                                          initialdir="./Daten_Import",
                                          defaultextension=".json",
                                          filetypes=(('JSON-Dateien', '*.json'), ('Alle Dateien', '*.*')))
    # JSON-Daten aus Datei lesen
    with open(dateiname) as json_datei:
        json_daten: dict = json.load(json_datei)
    return json_daten


def export_json_dialog(punkte) -> None:
    """Exportdialog für das Speichern von Punkten.

    :param punkte: Dictionary mit den zu exportierenden Punkten
    :type punkte: dict[pkt.Punkt]
    :return: None
    :rtype: None
    """
    # Datei festlegen
    dateiname = tkfd.asksaveasfile(mode="w",
                                   title="Punkte exportieren",
                                   initialdir="./Daten_Export",
                                   defaultextension=".json",
                                   filetypes=(('JSON-Dateien', '*.json'), ('Alle Dateien', '*.*')))
    # JSON-Datei schreiben
    punktliste: dict = pktlst.punktliste2json(punkte)
    inhalt: str = json.dumps(punktliste, indent=4)
    dateiname.write(inhalt)
    dateiname.close()
