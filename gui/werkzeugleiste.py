import tkinter as tk


class Werkzeugleiste(tk.Frame):

    def __init__(self, p_master=None):
        """Initialisiert die Werkzeugleiste.

        :param p_master: Master-Anwendung
        :type p_master: Anwendung
        """
        super().__init__(p_master)

        self.__symbol_datei_oeffnen = tk.PhotoImage()
        self.__symbol_beenden = tk.PhotoImage()

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """Initialisieren der GUI der Werkzeugleiste.

        :return: None
        :rtype: None
        """
        self.grid()

        self.__symbol_datei_oeffnen.configure(file="./gui/grafik/symbol/24x24/file_yellow_open.gif")
        tk.Button(self, image=self.__symbol_datei_oeffnen, text="Öffnen", command=self.werkzeug_datei_oeffnen,
                  width=24, height=24).grid(row=0, column=0)

        self.__symbol_beenden.configure(file="./gui/grafik/symbol/24x24/exit.gif")
        tk.Button(self, image=self.__symbol_beenden, text="Beenden", command=self.werkzeug_beenden,
                  width=24, height=24).grid(row=0, column=1)

    def werkzeug_datei_oeffnen(self):
        """Ruft das "Datei öffnen"-Menü auf.

        :return: None
        :rtype: None
        """
        self.master.menue_datei_oeffnen()

    def werkzeug_beenden(self):
        """Ruft das "Beenden-Menü" auf.

        :return: None
        :rtype: None
        """
        self.master.menue_beenden()
