import tkinter as tk
import tkinter.filedialog as tkfd
import json

import transformationen_package.transformation as tr
import grundlagen.punktliste as pktlst


class Anwendung(tk.Frame):

    def __init__(self, master=None) -> None:
        """Initialisiert die Anwendung

        :param master: Berechnungsfenster
        :type master: Berechnungsfenster
        """
        super().__init__(master)

        # Transformationsobjekte erstellen
        self.h_trafo = tr.Helmerttransformation()
        self.a_trafo = tr.Affintransformation()
        self.pkt_listen = ()

        # GUI initialisieren
        self.master.title("Transformation")
        self.pfad: str = ""
        self.grid()
        #self.option_add("*font", "arial 7")
        self.zeile: int = 0

        # Buttons: Daten laden
        tk.Button(self, text="JSON-Dateien importieren", command=self.datensatz_einfuegen, fg="purple").grid(row=self.zeile, column=1, sticky="e")
        tk.Button(self, text="URL importieren", command=self.einlesen_datensatz, fg="green").grid(row=self.zeile, column=2, sticky="e")
        tk.Button(self, text="Test URL laden", command=self.testdaten_laden, fg="green").grid(row=self.zeile, column=3, sticky="e")

        # Beenden Button
        tk.Button(self, text="Beenden", fg="red", command=self.master.destroy).grid(row=self.zeile, column=0, sticky="ew")
        self.zeile += 1

        # URL Eingabe
        tk.Label(self, text="URL Eingabe Quellsystem: ", fg="green").grid(row=self.zeile, sticky="e")
        self.__eingabe_link_quellsystem: tk.Entry = tk.Entry(self)
        self.__eingabe_link_quellsystem.grid(row=self.zeile, column=1, columnspan=3, sticky="ew")
        self.zeile += 1
        tk.Label(self, text="URL Eingabe Zielsystem: ", fg="green").grid(row=self.zeile, sticky="e")
        self.__eingabe_link_zielsystem: tk.Entry = tk.Entry(self)
        self.__eingabe_link_zielsystem.grid(row=self.zeile, column=1, columnspan=3, sticky="ew")
        self.zeile += 1

        # Buttons: Berechnen
        tk.Button(self, text="Helmert-Transformation", command=self.berechnung_helmert, fg="blue").grid(row=self.zeile, column=0, columnspan=2, sticky="e")
        tk.Button(self, text="Affin-Transformation", command=self.berechnung_affin, fg="blue").grid(row=self.zeile, column=2, columnspan=2)
        self.zeile += 1

    def testdaten_laden(self) -> None:
        """Lädt Testdaten für die Berechnung.

        :return: None
        :rtype: None
        """
        # Link der Testdaten der Transformation
        url_alt = "https://py.kartographie.net/trans_alt.json"
        url_neu = "https://py.kartographie.net/trans_neu.json"

        self.__eingabe_link_quellsystem.insert(0, url_alt)
        self.__eingabe_link_zielsystem.insert(0, url_neu)

    def datensatz_einfuegen(self) -> None:
        """ Liest jeweils eine JSON-Datei als Quell und Zielsystem ein und bindet es in das Programm ein.

        :return: Dictionaries der eingefügten Systeme
        :rtype: tuple[dict, dict]
        """
        self.pkt_listen = self.h_trafo.import_json_datei()
        self.visualisierung_datensaetze()

    def einlesen_datensatz(self) -> None:
        """ Bindet die Datensätze der angegebenen URL's ein.

        :return: None
        :rtype: None
        """
        self.pkt_listen = self.h_trafo.punktliste_laden_url(self.__eingabe_link_quellsystem.get(), self.__eingabe_link_zielsystem.get())
        self.visualisierung_datensaetze()

    def visualisierung_datensaetze(self) -> None:
        """ Darstellung und Übernahme der JSON von Datei oder URL.

        :return: None
        :rtype: None
        """
        self.h_trafo._pkt_list_alt = self.pkt_listen[0]
        self.h_trafo._pkt_list_neu = self.pkt_listen[1]
        self.a_trafo._pkt_list_alt = self.pkt_listen[0]
        self.a_trafo._pkt_list_neu = self.pkt_listen[1]

        # Quellsystem

        # Aufbau Tabellenkopf
        tk.Label(self, text="Quellsystem:", font=("arial", 14, "underline")).grid(row=self.zeile)
        self.zeile += 1
        tk.Label(self, text="Punktnummer:").grid(row=self.zeile, column=0)
        tk.Label(self, text="Rechtswert:").grid(row=self.zeile, column=1)
        tk.Label(self, text="Hochwert:").grid(row=self.zeile, column=2)
        tk.Label(self, text="EPSG Code:").grid(row=self.zeile, column=3)
        self.zeile += 1

        # Einfügen der Werte aus dem Quellsystem
        for punkt in self.h_trafo._pkt_list_alt.values():
            tk.Label(self, text=punkt.hole_nr()).grid(row=self.zeile, column=0)
            tk.Label(self, text=punkt.hole_y()).grid(row=self.zeile, column=1)
            tk.Label(self, text=punkt.hole_x()).grid(row=self.zeile, column=2)
            tk.Label(self, text=punkt.hole_epsg()).grid(row=self.zeile, column=3)
            self.zeile += 1

        # Zielsystem

        # Aufbau Tabellenkopf
        tk.Label(self, text="Zielsystem:", font=("arial", 14, "underline")).grid(row=self.zeile)
        self.zeile += 1
        tk.Label(self, text="Punktnummer:").grid(row=self.zeile, column=0)
        tk.Label(self, text="Rechtswert:").grid(row=self.zeile, column=1)
        tk.Label(self, text="Hochwert:").grid(row=self.zeile, column=2)
        tk.Label(self, text="EPSG Code:").grid(row=self.zeile, column=3)
        self.zeile += 1

        # Einfügen der Werte aus dem Zielsystem
        for punkt in self.h_trafo._pkt_list_neu.values():
            tk.Label(self, text=punkt.hole_nr()).grid(row=self.zeile, column=0)
            tk.Label(self, text=punkt.hole_y()).grid(row=self.zeile, column=1)
            tk.Label(self, text=punkt.hole_x()).grid(row=self.zeile, column=2)
            tk.Label(self, text=punkt.hole_epsg()).grid(row=self.zeile, column=3)
            self.zeile += 1

    def berechnung_helmert(self) -> None:
        """ Aufruf der Helmert-Transformation und Einbindung der neuen Tabelle mit den transformierten Werten und Restklaffen

        :return: None
        :rtype: None
        """
        # Berechnungsaufruf der Funktionen
        self.h_trafo.schwerpunktbezogene_koordinaten()
        self.h_trafo.transformationsparameter_helmert()
        self.h_trafo.transformation_helmert()
        self.h_trafo.restklaffen()

        # Ausgabe der Helmerttransformation an die GUI

        # Erstellen des Tabellenkopfes
        tk.Label(self, text="Helmert-Transformation transformierte Punkte:", font=("arial", 14, "underline")).grid(row=self.zeile)
        self.zeile += 1
        tk.Label(self, text="Punktnummer:").grid(row=self.zeile, column=0)
        tk.Label(self, text="Rechtswert:").grid(row=self.zeile, column=1)
        tk.Label(self, text="Hochwert:").grid(row=self.zeile, column=2)
        tk.Label(self, text="EPSG Code:").grid(row=self.zeile, column=3)
        tk.Label(self, text="Restklaffe x:").grid(row=self.zeile, column=4)
        tk.Label(self, text="Restklaffe y:").grid(row=self.zeile, column=5)
        self.zeile += 1

        # Einfügen der transformierten Punkte in die GUI
        for key, punkt in self.h_trafo._pkt_list_trans.items():
            tk.Label(self, text=punkt.hole_nr()).grid(row=self.zeile, column=0)
            tk.Label(self, text=punkt.hole_y()).grid(row=self.zeile, column=1)
            tk.Label(self, text=punkt.hole_x()).grid(row=self.zeile, column=2)
            tk.Label(self, text=punkt.hole_epsg()).grid(row=self.zeile, column=3)

            # Anhängen der Restklaffen an die Passpunkte
            if key in [i.hole_nr() for i in self.h_trafo.identische_punkte_alt]:
                tk.Label(self, text=self.h_trafo._liste_restklaffen.get(punkt.hole_nr())[0]).grid(row=self.zeile, column=4)
                tk.Label(self, text=self.h_trafo._liste_restklaffen.get(punkt.hole_nr())[1]).grid(row=self.zeile, column=5)
            self.zeile += 1

        # Export der Dateien

        # Speicherpfad
        self.pfad = tkfd.askdirectory(title="Speicherort für die Export-Dateien festlegen", initialdir="./Daten_Export")

        # Trafo-Parameter in JSON-Datei
        with open(f"{self.pfad}/export_helmert_parameter.json", "w") as json_datei:
            inhalt = json.dumps(self.h_trafo._trafo_param, indent=4)
            json_datei.write(inhalt)

        # transformierte Punkte in JSON-Datei
        with open(f"{self.pfad}/export_helmert_punkte.json", "w") as json_datei:
            punktliste = pktlst.punktliste2json(self.h_trafo._pkt_list_trans)
            inhalt = json.dumps(punktliste, indent=4)
            json_datei.write(inhalt)

        # Restklaffen in Datei schreiben
        with open(f"{self.pfad}/export_helmert_restklaffen.json", "w") as json_datei:
            inhalt = json.dumps(self.h_trafo._liste_restklaffen, indent=4)
            json_datei.write(inhalt)

    def berechnung_affin(self) -> None:
        """ Aufruf der Affin-Transformation und Einbindung der neuen Tabelle mit den transformierten Werten und Restklaffen

        :return: None
        :rtype: None
        """
        # Berechnungsaufruf der Funktionen

        self.a_trafo.schwerpunktbezogene_koordinaten()
        self.a_trafo.transformationsparameter_affin()
        self.a_trafo.transformation_affin()
        self.a_trafo.restklaffen()

        # Ausgabe der Affintransformation an die GUI

        # Erstellen des Tabellenkopfes
        tk.Label(self, text="Affin-Transformation transformierte Punkte:", font=("arial", 14, "underline")).grid(row=self.zeile)
        self.zeile += 1
        tk.Label(self, text="Punktnummer:").grid(row=self.zeile, column=0)
        tk.Label(self, text="Rechtswert:").grid(row=self.zeile, column=1)
        tk.Label(self, text="Hochwert:").grid(row=self.zeile, column=2)
        tk.Label(self, text="EPSG Code:").grid(row=self.zeile, column=3)
        tk.Label(self, text="Restklaffe x:").grid(row=self.zeile, column=4)
        tk.Label(self, text="Restklaffe y:").grid(row=self.zeile, column=5)
        self.zeile += 1

        # Einfügen der transformierten Punkte in die GUI
        for key, punkt in self.a_trafo._pkt_list_trans.items():
            tk.Label(self, text=punkt.hole_nr()).grid(row=self.zeile, column=0)
            tk.Label(self, text=punkt.hole_y()).grid(row=self.zeile, column=1)
            tk.Label(self, text=punkt.hole_x()).grid(row=self.zeile, column=2)
            tk.Label(self, text=punkt.hole_epsg()).grid(row=self.zeile, column=3)

            # Anhängen der Restklaffen an die Passpunkte
            if key in [i.hole_nr() for i in self.a_trafo.identische_punkte_alt]:
                tk.Label(self, text=self.a_trafo._liste_restklaffen.get(punkt.hole_nr())[0]).grid(row=self.zeile, column=4)
                tk.Label(self, text=self.a_trafo._liste_restklaffen.get(punkt.hole_nr())[1]).grid(row=self.zeile, column=5)
            self.zeile += 1

        # Export der Dateien

        # Speicherpfad
        self.pfad = tkfd.askdirectory(title="Speicherort für die Export-Dateien festlegen", initialdir="./Daten_Export")

        # Trafo-Parameter in JSON-Datei
        with open(f"{self.pfad}/export_affin_parameter.json", "w") as json_datei:
            inhalt = json.dumps(self.a_trafo._trafo_param, indent=4)
            json_datei.write(inhalt)

        # transformierte Punkte in JSON-Datei
        with open(f"{self.pfad}/export_affin_punkte.json", "w") as json_datei:
            punktliste = pktlst.punktliste2json(self.a_trafo._pkt_list_trans)
            inhalt = json.dumps(punktliste, indent=4)
            json_datei.write(inhalt)

        # Restklaffen in Datei schreiben
        with open(f"{self.pfad}/export_affin_restklaffen.json", "w") as json_datei:
            inhalt = json.dumps(self.a_trafo._liste_restklaffen, indent=4)
            json_datei.write(inhalt)


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)
    anwendung.mainloop()
