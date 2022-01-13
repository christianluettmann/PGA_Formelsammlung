import tkinter as tk
import tkinter.messagebox as tkmb


class Menue(tk.Menu):

    def __init__(self, p_master, **p_kwargs):
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

        # Menü-Objekte erstellen:
        self.__menue_datei: tk.Menu = tk.Menu(self, tearoff=0)

        self.__menue_berechnungen: tk.Menu = tk.Menu(self, tearoff=0)
        self.__menue_berechnungen_grundlagen: tk.Menu = tk.Menu(self)
        self.__menue_berechnungen_schnitte: tk.Menu = tk.Menu(self)
        self.__menue_berechnungen_polygonzug: tk.Menu = tk.Menu(self)

        self.__menue_transformationen: tk.Menu = tk.Menu(self, tearoff=0)
        self.__menue_hilfe: tk.Menu = tk.Menu(self, tearoff=0)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """
        Initialisiert die GUI der Menü-Leiste.
        """

        self.menue_datei()
        self.add_cascade(label="Datei", menu=self.__menue_datei)

        self.menue_berechnungen()
        self.add_cascade(label="Berechnungen", menu=self.__menue_berechnungen)
        self.menue_transformationen()
        self.add_cascade(label="Transformationen", menu=self.__menue_transformationen)

        self.menue_hilfe()
        self.add_cascade(label="Hilfe", menu=self.__menue_hilfe)

    def menue_datei(self):
        """
        Initialisiert das Datei-Menü.
        """
        self.__menue_datei.add_command(label="öffnen...", command=self.master.menue_datei_oeffnen)
        self.__menue_datei.add_separator()
        self.__menue_datei.add_command(label="Importieren...", command=self.master.menue_tut_nix)
        self.__menue_datei.add_command(label="Exportieren...", command=self.master.menue_tut_nix)
        self.__menue_datei.add_separator()
        self.__menue_datei.add_command(label="Beenden", command=self.master.menue_beenden)

    def menue_berechnungen(self):
        """
        Initialisiert das Berechnungen-Menü mit den verschiedenen Untermenüs.
        """
        # Untermenüs anlegen
        self.menue_berechnungen_grundlagen()
        self.menue_berechnungen_schnitte()
        self.menue_berechnungen_polygonzug()
        # Untermenüs einhängen
        self.__menue_berechnungen.add_cascade(label="Grundlagen", menu=self.__menue_berechnungen_grundlagen)
        self.__menue_berechnungen.add_cascade(label="Schnitte", menu=self.__menue_berechnungen_schnitte)
        self.__menue_berechnungen.add_cascade(label="Polygonzug", menu=self.__menue_berechnungen_polygonzug)

    def menue_berechnungen_grundlagen(self):
        """
        Initialisiert das Grundlagen-Untermenü.
        """
        self.__menue_berechnungen_grundlagen.add_command(label="Winkelumrechnung", command=self.master.fenster_winkel)
        self.__menue_berechnungen_grundlagen.add_separator()
        self.__menue_berechnungen_grundlagen.add_command(label="1. geo. Grundaufgabe", command=self.master.fenster_erstega)
        self.__menue_berechnungen_grundlagen.add_command(label="2. geo. Grundaufgabe", command=self.master.fenster_zweitega)

    def menue_berechnungen_schnitte(self):
        """
        Initialisiert das Schnitte-Untermenü.
        """
        self.__menue_berechnungen_schnitte.add_command(label="Vorwärtsschnitt", command=self.master.menue_tut_nix)
        self.__menue_berechnungen_schnitte.add_command(label="Rückwärtsschnitt", command=self.master.menue_tut_nix)
        self.__menue_berechnungen_schnitte.add_command(label="Bogenschnitt", command=self.master.fenster_bogenschnitt)

    def menue_berechnungen_polygonzug(self):
        """
        Initialisiert das Polygonzug-Untermenü.
        """
        self.__menue_berechnungen_polygonzug.add_command(label="beidseitig angeschlossen", command=self.master.menue_tut_nix)
        self.__menue_berechnungen_polygonzug.add_command(label="Ring", command=self.master.menue_tut_nix)

    def menue_transformationen(self):
        """
        Initialisiert das Transformationen-Menü.
        """
        self.__menue_transformationen.add_command(label="Helmerttransformation", command=self.master.menue_tut_nix)
        self.__menue_transformationen.add_command(label="Affintransformation", command=self.master.menue_tut_nix)

    def menue_hilfe(self):
        """
        Initialisiert das Hilfe-Menü.
        """
        self.__menue_hilfe.add_command(label="Über...", command=self.menue_hilfe_ueber)

    @staticmethod
    def menue_hilfe_ueber():
        """
        Erzeugt die Über/Copyright-Nachricht.
        """
        copyright_zeichen = u"\u00A9"
        zeilen = ["copyright %s" % copyright_zeichen, "Lara Dick", "Lukas Looschen", "Christian Lüttmann", "Antonia Beekmann", ]
        nachricht = "\n". join(zeilen)
        tkmb.showinfo("Über", nachricht)
