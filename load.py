import pandas as pd
from sqlalchemy import create_engine

def save_to_database(df):
    engine = create_engine("sqlite:///weather_data.db")

    df.to_sql("weather_measurements", con=engine, if_exists="replace", index=False)