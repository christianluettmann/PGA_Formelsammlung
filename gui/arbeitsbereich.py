import tkinter as tk


class Arbeitsbereich(tk.Frame):

    def __init__(self, p_master=None):

        super().__init__(p_master)

        self.initialisiere_gui()

    def initialisiere_gui(self):
        tk.Button(self, text="Winkel", command=self.master.fenster_winkel).grid(row=1)
        tk.Button(self, text="1. geod. GA", command=self.master.fenster_erstega).grid(row=2)
        tk.Button(self, text="2. geod. GA", command=self.master.fenster_zweitega).grid(row=3)
        pass
