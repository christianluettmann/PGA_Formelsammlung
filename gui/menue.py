import tkinter as tk
import tkinter.messagebox as tkmb


class Menue(tk.Menu):

    def __init__(self, p_anwendung, p_master, **p_kwargs):

        # Konsturktor der Elternklasse
        super().__init__(master=p_master, **p_kwargs)

        self.__anwendung = p_anwendung

        # Datei-Menü
        self.__menue_datei = tk.Menu(self, tearoff=0)

        # Hilfe-Menü
        self.__menue_hilfe = tk.Menu(self, tearoff=0)

        self.initialisiere_gui()


    def initialisiere_gui(self):

        self.menue_datei()
        self.menue_hilfe()

    def menue_datei(self):

        self.__menue_datei.add_command(label="Öffnen...", command=self.__anwendung.menu_test)
        self.__menue_datei.add_separator()
        self.__menue_datei.add_command(label="Import...")
        self.__menue_datei.add_separator()
        self.__menue_datei.add_command(label="Beenden...")

        self.add_cascade(label="Datei", menu=self.__menue_datei)

    def menue_hilfe(self):

        self.__menue_hilfe.add_command(label="Über...", command=self.menue_hilfe_ueber)

        self.add_cascade(label="Hilfe", menu=self.__menue_hilfe)

    def menue_hilfe_ueber(self):

        zeilen = ["Copyright: \u00A9 Christian Lüttmann",
                  "christian.luettmann@student.jade-hs.de"]

        nachricht = "\n".join(zeilen)

        tkmb.showinfo("Über", nachricht)
