import grundlagen.punkt as pkt


def json2punktliste(p_json_daten: dict) -> dict:
    """Wandelt eine JSON-Punktliste in eine Dictionary-Punktliste um.

    :param p_json_daten: Punktliste im JSON-Format
    :type p_json_daten: dict
    :return: Punktliste als Dictionary
    :rtype: dict
    """
    pkt_list: dict = {}

    for schluessel, wert in p_json_daten.items():
        p: pkt.Punkt = pkt.Punkt()
        p.setze_json(wert)
        # nur wenn Punktnummer und Schlüssel übereinstimmen, in die Liste
        if schluessel == p.hole_nr():
            pkt_list[schluessel] = p
    return pkt_list


def punktliste2json(p_punktliste: dict) -> dict:
    """Wandelt die Punkt-Objekte in der Punktliste in Dictionaries um.

    :param p_punktliste: Punktliste
    :type p_punktliste: dict
    :return: Punktliste
    :rtype: dict
    """
    punktliste: dict = dict()
    for schluessel, punkt in p_punktliste.items():
        punktliste[schluessel]: dict = punkt.hole_json()
    return punktliste
