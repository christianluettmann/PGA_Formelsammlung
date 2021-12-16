import tkinter as tk
import grundlagen.punkt as pkt


class Berechnungsfenster(tk.Toplevel):

    def __init__(self):

        super().__init__()

    def lade_punkt(self) -> pkt.Punkt:

        return self.master.lade_punkt()

    def sende_punkt(self, p_p: pkt.Punkt):

        self.master.sende_punkt(p_p)
