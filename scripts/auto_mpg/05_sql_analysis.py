from pathlib import Path
import sqlite3 #Importing the sqlite3 library in order to connect to the database and run SQL queries
import pandas as pd

#We locate files relative to the repository root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

#Then define the paths to the clean data, database, sql script, results and raw data
CSV_PATH = ( PROJECT_ROOT / "data/processed/auto_mpg/auto_mpg_cleaned.csv")
DATABASE_PATH = PROJECT_ROOT / "data/database/auto_mpg.sqlite"
SQL_DIR = PROJECT_ROOT / "sql/auto_mpg"
RESULTS_PATH = PROJECT_ROOT / "outputs/results/auto_mpg/sql"
RAW_PATH = PROJECT_ROOT / "data/raw/auto_mpg/auto-mpg.data"

#create the required folders if they do not already exist
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
RESULTS_PATH.mkdir(parents=True, exist_ok=True)
RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

# The raw file has no column headings, so we define them here based on the dataset description
column_names = ["mpg", "cylinders", "displacement", "horsepower",
    "weight", "acceleration", "model_year", "origin", "car_name"]

# Read the raw data, interpreting ? as a missing value.
raw_df = pd.read_csv(RAW_PATH, sep=r"\s+", names=column_names, na_values="?")


#Now load the cleaned data
df = pd.read_csv(CSV_PATH)

#Connect to the database with sqlite 3
with sqlite3.connect(DATABASE_PATH) as connection:

    #Replace each table with the current data, excluding the pandas index
    raw_df.to_sql("auto_mpg_raw", connection, if_exists="replace", index=False )

    df.to_sql("auto_mpg", connection, if_exists="replace", index=False)

    #Loop through the SQL files in filename order
    for sql_file in sorted(SQL_DIR.glob("*.sql")):

        #Print the filename before running its query
        print(f"\n{sql_file.name}")

        #Read the SQL file and run its query
        query = sql_file.read_text(encoding="utf-8")
        results = pd.read_sql_query(query, connection)

        print(results.to_string(index=False))

        #Save the results and print their location
        output_file = RESULTS_PATH / f"{sql_file.stem}.csv"
        results.to_csv(output_file, index=False)
        print(f"Results saved to: {output_file}")