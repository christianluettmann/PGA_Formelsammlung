import tkinter as tk


def eingabefeld_auswerten(p_eingabefeld: tk.Entry) -> float:
    """

    :param p_eingabefeld: Eingabefeld
    :type p_eingabefeld: tk.Entry
    :return: Wert als Fliesskommazahl
    :rtype: float
    """
    sz_wert: str = p_eingabefeld.get()
    sz_wert = sz_wert.replace(",", ".")
    return wert2fliess(sz_wert)


def wert2fliess(p_wert: str) -> float:
    """

    :param p_wert: Umzuwandelder Wert
    :type p_wert: str
    :return: Umgewandelter Wert
    :rtype: float
    """
    try:
        wert: float = float(p_wert)
    except:
        wert = 0.0  # TODO
    return wert


def eingabefeld_schreiben(p_eingabefeld: tk.Entry, p_wert: float):
    """

    :param p_eingabefeld: Eingabefeld
    :type p_eingabefeld: tk.Entry
    :param p_wert: zu schreibender Wert
    :type p_wert float
    """
    p_eingabefeld.delete(0, tk.END)
    p_eingabefeld.insert(0, str(p_wert))
