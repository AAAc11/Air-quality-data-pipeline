import pandas as pd
import json

with open("raw_data/extract_data.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)
    hourly_data = raw_data.get("hourly")

    df = pd.DataFrame(hourly_data)
    df["time"] = pd.to_datetime(df["time"])
    df["city"] = "Kraków"
    print(df)