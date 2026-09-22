# Weather Data ETL Pipeline

This is an automated ETL (Extract, Transform, Load) pipeline that extracts temperature data for Kraków using the Open-Meteo API, transforms it into a clean, relational format, and loads it into a local database.

## Architecture 
* **Extract:** Data is downloaded from the Open-Meteo API in raw JSON format.
* **Transform:** Using Pandas, the nested JSON is parsed into DataFrame. Data types are correctly cast (e.g., strings to datetime objects), and the dataset is enriched with a new 'city' column for future scalability.
* **Load:** Using SQLAlchemy, the cleaned data is loaded into a local SQLite database, ready for analytical queries.
* **Automation:** A `.bat` script is integrated with Windows Task Scheduler to run the pipeline automatically every day at 6:00 AM.

## Technologies
* Python 3.12
* Pandas
* SQLAlchemy & SQLite
* Requests
* Windows Task Scheduler

## Project Structure
* `main.py` - The main file that executes processes in the correct order.
* `extract.py` - Handles API requests and downloads raw data.
* `transform.py` - Parses the data into a DataFrame, cleans data types, and enriches the dataset.
* `load.py` - Establishes a database engine connection and loads clean data into the local database.

## How to Run Locally
1. Clone the repository:
   ```
   git clone https://github.com/AAAc11/Air-quality-data-pipeline.git
   ```
2. Create and activate a virtual environment:
   ```
    python -m venv venv
    venv\Scripts\activate
   ```
3. Install required dependencies:
   ```
   pip install pandas sqlalchemy requests
   ```
4. Run the ETL pipeline:
   ```
   python main.py
   ```
