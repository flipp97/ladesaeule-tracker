import requests
import csv
import os
from datetime import datetime

URL = https://enbw-emp.azure-api.net/emobility-public-api/api/v1/chargestations/2064581

data = requests.get(URL).json()

total = data["numberOfChargePoints"]
free = data["availableChargePoints"]

# alternativ noch genauer:
free_check = sum(
    1 for cp in data["chargePoints"]
    if cp["status"] == "AVAILABLE"
)

datei = "daten.csv"
exists = os.path.exists(datei)

with open(datei, "a", newline="") as f:
    writer = csv.writer(f)

    if not exists:
        writer.writerow(["zeitpunkt", "frei", "gesamt"])

    writer.writerow([
        datetime.now().isoformat(),
        free_check,
        total
    ])

print(f"{free_check}/{total}")
