import tkinter as tk
import grundlagen.gui as gui
import grundlagen.punkt as pkt
import grundlagen.punktliste as pktlst


class Tabelle(tk.Frame):

    def __init__(self, p_master):
        """Initialisiert die Klasse Tabelle.

        :param p_master: Anwendung
        :type p_master: Anwendung
        """
        super().__init__(p_master)

        self.__zeilen_anzahl: int = 0
        self.__spalten_anzahl: int = 0

        # Punktliste
        self.__pktlst: dict = dict()

        # alle Eingabefelder zur Punktliste (als Instanzvariablen für den klassenweiten Zugriff aus allen Methoden)
        self.__eingabe_pktlst: dict = dict()

        self.grid()

    def setze_punktliste(self, p_pktlst: dict) -> None:
        """Erstellt die Tabelle mit den Punkten.

        :param p_pktlst: Punktliste
        :type p_pktlst: dict
        :return: None
        :rtype: None
        """
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
            self.__eingabe_pktlst[schluessel]: dict = dict()
            spalte: int = 0
            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "nr", wert.hole_nr())
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "y", wert.hole_y())
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "x", wert.hole_x())
            spalte += 1
            self.erzeuge_eingabefeld(zeile, spalte, schluessel, "epsg", wert.hole_epsg())
            zeile += 1

    def erzeuge_eingabefeld(self, p_zeile: int, p_spalte: int, p_schluessel: str, p_atributname: str, p_atributwert: str) -> None:
        """Erzeugt ein Eingabefeld an der angegebenen Stellt mit den Werten.

        :param p_zeile: Zeilennummer
        :type p_zeile: int
        :param p_spalte: Spaltennummer
        :type p_spalte: int
        :param p_schluessel: Schlüssel in der Punktliste
        :type p_schluessel: str
        :param p_atributname: Atributname
        :type p_atributname: str
        :param p_atributwert: Atributwert
        :type p_atributwert: str
        :return: None
        :rtype: None
        """
        eingabe: tk.Entry = tk.Entry(self)
        self.__eingabe_pktlst[p_schluessel][p_atributname] = eingabe
        self.__eingabe_pktlst[p_schluessel][p_atributname].grid(row=p_zeile, column=p_spalte)
        gui.eingabefeld_schreiben(self.__eingabe_pktlst[p_schluessel][p_atributname], p_atributwert)

    def aenderungen(self) -> None:
        """Aktualisiert die Punktliste.

        :return: None
        :rtype: None
        """
        # Inhalt der Punktliste komplett löschen
        self.__pktlst.clear()
        # TODO: Soll wirklich die gesamte Tabelle wieder durchlaufen werden?
        for schluessel, wert in self.__eingabe_pktlst.items():

            nr: str = self.__eingabe_pktlst[schluessel]["nr"].get()
            y: float = gui.eingabefeld_auswerten(self.__eingabe_pktlst[schluessel]["y"])
            x: float = gui.eingabefeld_auswerten(self.__eingabe_pktlst[schluessel]["x"])
            epsg: int = int(gui.eingabefeld_auswerten(self.__eingabe_pktlst[schluessel]["epsg"]))

            p: pkt.Punkt = pkt.Punkt(y, x, nr, epsg)

            self.__pktlst[nr] = p

    def hole_punkt(self, p_pktnr) -> pkt.Punkt:
        """Gibt den Punkt aus der Tabelle zur übergebenen Punktnummer zurück.
        (Punkt aus Tabelle zur Berechnung)

        :param p_pktnr: Punktnummer
        :type p_pktnr: str
        :return: Punkt
        :rtype: pkt.Punkt
        """
        try:
            return self.__pktlst[p_pktnr]
        except KeyError:    # Die Punktnummer ist nicht vorhanden -> (0,0)-Punkt wird zurückgegeben
            return pkt.Punkt()

    def speicher_punkt(self, p_p: pkt.Punkt) -> None:
        """Speichert den übergebenen Punkt in der Tabelle.
        (Punkt aus Berechnung in der Tabelle speichern)

        :param p_p: Punkt
        :type p_p: pkt.Punkt
        :return: None
        :rtype: None
        """
        self.__pktlst[p_p.hole_nr()] = p_p
        self.setze_punktliste(self.__pktlst)

    def hole_punktliste(self) -> dict:
        """Gibt die Punktliste als Dictionary zurück.
        (Punkliste aus Tabelle zum Export)

        :return: Punktliste
        :rtype: dict
        """
        return pktlst.punktliste2json(self.__pktlst)
