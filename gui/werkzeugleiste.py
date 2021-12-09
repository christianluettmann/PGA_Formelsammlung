import tkinter as tk


class Werkzeugleiste(tk.Frame):

    def __init__(self, p_master=None):

        super().__init__(p_master)

        self.__symbol_datei_oeffnen = tk.PhotoImage()
        self.__symbol_beenden = tk.PhotoImage()

        self.initialisiere_gui()

    def initialisiere_gui(self):

        self.grid()
        self.__symbol_datei_oeffnen.configure(file="./gui/grafik/symbol/24x24/file_yellow_open.gif")
        tk.Button(self, image=self.__symbol_datei_oeffnen,
                  command=self.befehl_datei_oeffnen,
                  width=24, height=24).grid(row=0, column=0)
        self.__symbol_beenden.configure(file="./gui/grafik/symbol/24x24/exit.gif")
        tk.Button(self, image=self.__symbol_beenden, text="Beenden",
                  command=self.befehl_beenden,
                  width=24, height=24).grid(row=0, column=1)

    def befehl_datei_oeffnen(self):

        self.master.werkzeug_test()

    def befehl_beenden(self):

        self.master.werkzeug_test()
