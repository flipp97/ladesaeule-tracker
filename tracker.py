import requests
import csv
import os
from datetime import datetime

URL = https://enbw-emp.azure-api.net/emobility-public-api/api/v1/chargestations/2064581



# GitHub Secret wird als Environment Variable übergeben
API_KEY = os.getenv("ENBW_API_KEY")

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY
}

response = requests.get(URL, headers=headers)

# falls API fehlschlägt → klarer Fehler
response.raise_for_status()

data = response.json()

total = data["numberOfChargePoints"]
free = sum(
    1 for cp in data["chargePoints"]
    if cp["status"] == "AVAILABLE"
)

file = "daten.csv"
exists = os.path.exists(file)

with open(file, "a", newline="") as f:
    writer = csv.writer(f)

    if not exists:
        writer.writerow(["zeitpunkt", "frei", "gesamt"])

    writer.writerow([
        datetime.now().isoformat(),
        free,
        total
    ])

print(f"{free}/{total}")
