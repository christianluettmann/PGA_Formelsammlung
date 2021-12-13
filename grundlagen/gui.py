import tkinter as tk




def eingabefeld_auswerten(p_eingabefeld: tk.Entry):
    """

    :param p_eingabefeld:
    :return:
    """
    sz_wert: str = p_eingabefeld.get()
    sz_wert = sz_wert.replace(",", ".")
    return wert2fliess(sz_wert)

def eingabefeld_schreiben(p_eingabefeld: tk.Entry, p_wert: float):
    """
    :param p_eingabefeld: Eingabefeld
    :type p_eingabefeld: tk.Entry
    :param p_wert: zu schreibender Wert
    :type p_wert float
    """
    p_eingabefeld.delete(0, tk.END)
    p_eingabefeld.insert(0, str(p_wert))


def wert2fliess(p_wert: str) -> float:
    """

    :param p_wert:
    :return:
    """
    try:
        wert: float = float(p_wert)
    except:
        # todo
        wert = 0.0

    return wert
