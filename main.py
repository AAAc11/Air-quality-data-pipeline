from extract import fetch_data
from load import save_to_database
from transform import procces_data

print("Starting pipeline ETL")
fetch_data()
print("Data downloaded")
clean_data = procces_data()
print("Data transformed")
save_to_database(clean_data)
print("Data saved in database")