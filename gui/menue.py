import tkinter as tk
import tkinter.messagebox as tkmb


class Menue(tk.Menu):

    def __init__(self, p_anwendung, p_master, **p_kwargs):
        """
        Initialisiert die Menü-Leiste.
        :param p_anwendung: Anwendung
        :type p_anwendung: Anwendung
        :param p_master: Elternklasse
        :type p_master: Anwendung
        :param p_kwargs:
        :type p_kwargs:
        """

        # Konstruktor der Elternklasse
        super().__init__(p_master, **p_kwargs)

        self.__anwendung = p_anwendung

        # Menü-Objekte erstellen:
        self.__menue_datei = tk.Menu(self, tearoff=0)
        self.__menue_berechnungen = tk.Menu(self, tearoff=0)
        self.__menue_transformationen = tk.Menu(self, tearoff=0)
        self.__menue_hilfe = tk.Menu(self, tearoff=0)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """
        Initialisiert die GUI der Menü-Leiste.
        """

        self.menue_datei()
        self.menue_hilfe()
        self.menue_berechnungen()
        self.menue_transformationen()

    def menue_datei(self):
        """
        Initialisiert das Datei-Menü.
        """
        self.__menue_datei.add_command(label="öffnen...", command=self.__anwendung.menue_datei_oeffnen)
        self.__menue_datei.add_separator()
        self.__menue_datei.add_command(label="Importieren...", command=self.__anwendung.menue_tut_nix)
        self.__menue_datei.add_separator()
        self.__menue_datei.add_command(label="Beenden", command=self.__anwendung.menue_beenden)

        self.add_cascade(label="Datei", menu=self.__menue_datei)

    def menue_berechnungen(self):
        """
        Initialisiert das Berechnungen-Menü.
        """
        self.__menue_berechnungen.add_command(label="Winkelumrechnung", command=self.__anwendung.fenster_winkel)
        self.__menue_berechnungen.add_separator()
        self.__menue_berechnungen.add_command(label="1. geo. Grundaufgabe", command=self.__anwendung.fenster_erstega)
        self.__menue_berechnungen.add_command(label="2. geo. Grundaufgabe", command=self.__anwendung.fenster_zweitega)
        self.__menue_berechnungen.add_separator()
        self.__menue_berechnungen.add_command(label="Bogenschnitt", command=self.__anwendung.fenster_bogenschnitt)

        self.add_cascade(label="Berechnungen", menu=self.__menue_berechnungen)

    def menue_transformationen(self):
        """
        Initialisiert das Transformationen-Menü.
        """
        self.__menue_transformationen.add_command(label="Helmerttransformation", command=self.__anwendung.menue_tut_nix)

        self.add_cascade(label="Transformationen", menu=self.__menue_transformationen)

    def menue_hilfe(self):
        """
        Initialisiert das Hilfe-Menü.
        """
        self.__menue_hilfe.add_command(label="Über...", command=self.menue_hilfe_ueber)

        self.add_cascade(label="Hilfe", menu=self.__menue_hilfe)

    @staticmethod
    def menue_hilfe_ueber():
        """
        Erzeugt die Über/Copyright-Nachricht.
        """
        copyright_zeichen = u"\u00A9"
        zeilen = ["copyright %s" % copyright_zeichen, "Lara Dick", "Lukas Looschen", "Christian Lüttmann", "Antonia Beekmann", ]
        nachricht = "\n". join(zeilen)
        tkmb.showinfo("Über", nachricht)
