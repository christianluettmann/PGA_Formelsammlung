import tkinter as tk
from typing import Union


def eingabefeld_auswerten(p_eingabefeld: tk.Entry) -> float:
    """Gibt die Fließkommazahl aus einem Eingabefeld zurück.

    :param p_eingabefeld: Eingabefeld
    :type p_eingabefeld: tk.Entry
    :return: Wert des Feldes
    :rtype: float
    """
    sz_wert: str = p_eingabefeld.get()
    sz_wert: str = sz_wert.replace(",", ".")
    return wert2fliess(sz_wert)


def eingabefeld_schreiben(p_eingabefeld: tk.Entry, p_wert: Union[float, str]) -> None:
    """Schreibt einen Wert in ein Eingabefeld.

    :param p_eingabefeld: Eingabefeld
    :type p_eingabefeld: tk.Entry
    :param p_wert: einzufügender Wert
    :type p_wert: float
    :return: None
    :rtype: None
    """
    p_eingabefeld.delete(0, tk.END)
    p_eingabefeld.insert(0, str(p_wert))


def wert2fliess(p_wert: str) -> float:
    """Wandelt einen Zeichenkette in eine Fließkommazahl um.

    :param p_wert: umzuwandelder Wert
    :type p_wert: str
    :return: umgewandelter Wert
    :rtype: float
    """
    try:
        wert: float = float(p_wert)
    except:
        # todo
        wert: float = 0.0

    return wert
