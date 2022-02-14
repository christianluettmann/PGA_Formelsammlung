import tkinter as tk


class Statusleiste(tk.Frame):

    def __init__(self, p_master=None):
        """Initialisiert die Statusleiste.

        :param p_master: Anwendung
        :type p_master: Anwendung
        """
        super().__init__(p_master)

        self.__inhalt = tk.StringVar()
        self.__beschriftung = tk.Label(self)

        self.grid()

        self.__beschriftung.configure(textvariable=self.__inhalt, anchor=tk.W, relief=tk.SUNKEN)
        self.__beschriftung.grid(row=0, column=0)

        self.__inhalt.set("PGA")
