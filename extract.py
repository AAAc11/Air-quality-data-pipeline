import requests
import json

URL = "https://api.open-meteo.com/v1/forecast?latitude=50.0614&longitude=19.9366&hourly=temperature_2m&timezone=Europe%2FBerlin"

try:
    respond = requests.get(URL)

    respond.raise_for_status()

    raw_data = respond.json()

    with open("raw_data/extract_data.json", "w", encoding="utf-8") as file:
        json.dump(raw_data, file, indent=4)

except Exception as e:
    print(f"Error accured: {e}")

