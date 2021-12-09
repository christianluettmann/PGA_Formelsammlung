import tkinter as tk
import grundlagen.winkel_gui
import grundlagen.erste_grundaufgabe_gui
import grundlagen.zweite_grundaufgabe_gui
import gui.menue as mn
import gui.werkzeugleiste as wl
import gui.statusleiste as sl
import gui.arbeitsbereich as ab


class Anwendung(tk.Frame):

    def __init__(self, master=None):
        """

        :param master:
        """
        super().__init__(master)
        #
        # GUI
        #
        self.grid()

        # TODO: Werkzeugleiste, Menü, ...

        self.__menue = mn.Menue(self, self.master)
        self.__werkzeugleiste = wl.Werkzeugleiste(self)
        self.__statusleiste = sl.Statusleiste(self)
        self.__arbeitsbereich = ab.Arbeitsbereich(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        """

        :return:
        """

        # Menü
        self.master.config(menu=self.__menue)

        # Werkzeugleiste(mit ins grid gepackt)
        self.__werkzeugleiste.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        # Arbeitsbereich
        self.__arbeitsbereich.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        # Statusleiste
        self.__statusleiste.grid(row=2, column=0, sticky=tk.E+tk.S+tk.W)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    @staticmethod
    def fenster_winkel():
        top = tk.Toplevel()
        grundlagen.winkel_gui.Anwendung(top)

    @staticmethod
    def fenster_erstega():
        top = tk.Toplevel()
        grundlagen.erste_grundaufgabe_gui.Anwendung(top)

    @staticmethod
    def fenster_zweitega():
        top = tk.Toplevel()
        grundlagen.zweite_grundaufgabe_gui.Anwendung(top)

    @staticmethod
    def menue_test():
        print("Menü Test")

    @staticmethod
    def werkzeug_test():
        print("Werkzeug Test")


if __name__ == "__main__":
    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)

    wurzel.columnconfigure(0, weight=1)
    wurzel.rowconfigure(0, weight=1)

    anwendung.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

    anwendung.mainloop()
