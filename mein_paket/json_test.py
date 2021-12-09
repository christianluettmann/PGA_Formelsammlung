import json
import urllib.request
import ssl
import grundlagen.punkt as pkt
import grundlagen.strecke as st

"""
with open("ausgabe.txt", "w") as datei:
    datei.write("Hallo")

json_daten = json.loads('{"Hersteller":"VW", "Modell":"Passat B2", "Baujahr":1985, '
                        '"Fahrzeughalter": {"Nachname": "Gollenstede", "Vorname": "Andreas"}}')

#print(json_daten)
#print(json.dumps(json_daten, sort_keys=True, indent=4))

with open("passat.json", "r") as json_datei2:
    json_daten2 = json.load(json_datei2)
    print(json.dumps(json_daten2, sort_keys=True, indent=4))
"""

kontext = ssl._create_unverified_context()
"""
with urllib.request.urlopen("https://py.kartographie.net/kfz.json", context=kontext) as json_url3:
    json_daten3 = json.loads(json_url3.read().decode())
    print(json.dumps(json_daten3, sort_keys=True, indent=4))

    with open("kfz_url.json", "w") as json_datei4:
        json.dump(json_daten3, json_datei4)

# Python Objekte als Json

p1 = pkt.Punkt(91.4, 56.73, "Testpunkt")
p2 = pkt.Punkt(95.4, 50.7, "Testpunkt")
print(p1)
print(p1.__dict__)
"""

# Punktliste

pl: dict = {}

with urllib.request.urlopen("https://py.kartographie.net/pktlst.json", context=kontext) as json_url5:
    json_daten5 = json.loads(json_url5.read().decode())
    print(json.dumps(json_daten5, indent=4))

    for schluessel, wert in json_daten5.items():
        p: pkt.Punkt = pkt.Punkt()
        p.setze_json(wert)
        # nur wenn Punktnummer und Schlüssel übereinstimmen, in die Liste
        if schluessel == p.hole_nr():
            pl[schluessel] = p

for schluessel, wert in pl.items():
    print(schluessel + " : " + str(wert))











# Strecken

#s = st.Strecke(p1, p2, "Teststrecke")

#print(s)
