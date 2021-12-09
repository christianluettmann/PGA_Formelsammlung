import tkinter as tk
import grundlagen.winkel_gui
import grundlagen.erste_grundaufgabe_gui
import grundlagen.zweite_grundaufgabe_gui
import gui.menue
import gui.werkzeugleiste
import gui.statusleiste
import gui.arbeitsbereich


class Anwendung(tk.Frame):

    # Initialisierung der Oberfläche
    def __init__(self, master=None):
        super().__init__(master)

        # TODO GUI

        self.grid()

        # TODO Werkzeugleiste, Statusleiste, Menü, ...
        self.__menue = gui.menue.Menue(self, self.master)
        self.__werkzeugleiste = gui.werkzeugleiste.Werkzeugleiste(self)
        self.__arbeitsbereich = gui.arbeitsbereich.Arbeitsbereich(self)
        self.__statusleiste = gui.statusleiste.Statusleiste(self)

        self.initialisiere_gui()

    def initialisiere_gui(self):


        # Menü
        self.master.config(menu=self.__menue)

        # Werkzeugleiste (mit ins Grid gepackt)
        self.__werkzeugleiste.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        # Arbeisbereich
        self.__arbeitsbereich.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        # Statusleiste
        self.__statusleiste.grid(row=2, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)



    @staticmethod
    def fenster_winkel():
        grundlagen.winkel_gui.Anwendung(tk.Toplevel())

    @staticmethod
    def fenster_erste_grundaufgabe():
        grundlagen.erste_grundaufgabe_gui.Anwendung(tk.Toplevel())

    @staticmethod
    def fenster_zweite_grundaufgabe():
        grundlagen.zweite_grundaufgabe_gui.Anwendung(tk.Toplevel())

    def menu_test(self):
        print("Menü Test")

    def werkzeug_test(self):
        print("Werkzeug Test")


if __name__ == "__main__":

    wurzel = tk.Tk()
    anwendung = Anwendung(wurzel)

    wurzel.columnconfigure(0, weight=1)
    wurzel.rowconfigure(0, weight=1)
    anwendung.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

    anwendung.mainloop()
