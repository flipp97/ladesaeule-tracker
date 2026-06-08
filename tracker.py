import csv
import os
from datetime import datetime

# Testdaten
freie_ladepunkte = 2
gesamt_ladepunkte = 2

datei = "daten.csv"

existiert = os.path.exists(datei)

with open(datei, "a", newline="") as f:
    writer = csv.writer(f)

    if not existiert:
        writer.writerow([
            "zeitpunkt",
            "frei",
            "gesamt"
        ])

    writer.writerow([
        datetime.now().isoformat(),
        freie_ladepunkte,
        gesamt_ladepunkte
    ])
