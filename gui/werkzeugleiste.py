import tkinter as tk


class Werkzeugleiste(tk.Frame):

    def __init__(self, p_master=None):
        """Initialisiert die Werkzeugleiste.

        :param p_master: Master-Anwendung
        :type p_master: Anwendung
        """
        super().__init__(p_master)

        self.__symbol_datei_importieren: tk.PhotoImage = tk.PhotoImage()
        self.__symbol_beenden: tk.PhotoImage = tk.PhotoImage()

        self.initialisiere_gui()

    def initialisiere_gui(self) -> None:
        """Initialisieren der GUI der Werkzeugleiste.

        :return: None
        :rtype: None
        """
        self.grid()

        self.__symbol_datei_importieren.configure(file="./gui/grafik/file_yellow_open.gif")
        tk.Button(self,
                  image=self.__symbol_datei_importieren,
                  text="Öffnen",
                  command=self.werkzeug_datei_importieren,
                  width=24, height=24).grid(row=0, column=0)

        self.__symbol_beenden.configure(file="./gui/grafik/exit.gif")
        tk.Button(self,
                  image=self.__symbol_beenden,
                  text="Beenden",
                  command=self.werkzeug_beenden,
                  width=24, height=24).grid(row=0, column=1)

    def werkzeug_datei_importieren(self) -> None:
        """Ruft die Importieren-Funktion auf.

        :return: None
        :rtype: None
        """
        self.master.menue_datei_importieren()

    def werkzeug_beenden(self) -> None:
        """Ruft die Beenden-Funktion auf.

        :return: None
        :rtype: None
        """
        self.master.menue_beenden()
