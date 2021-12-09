import tkinter as tk

class Arbeitsbereich(tk.Frame):

    def __init__(self, p_master=None):

        super().__init__(p_master)

        self.initialisiere_gui()

    def initialisiere_gui(self):

        # TODO Commands einfügen
        tk.Button(self, text="Winkelumrechnung", command=self.master.fenster_winkel).grid(row=1, column=0)
        tk.Button(self, text="1. geo Grundaufgabe", command=self.master.fenster_erste_grundaufgabe).grid(row=2, column=0)
        tk.Button(self, text="2. geo Grundaufgabe", command=self.master.fenster_zweite_grundaufgabe).grid(row=3, column=0)

        tk.Button(self, text="Beenden", command=self.master.destroy, fg="red").grid(row=10, column=0)