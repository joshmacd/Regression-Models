from pathlib import Path

#Importing the pandas library in order to clean the data
import pandas as pd

#Store the paths of the raw and processed data as varibles
#The project root is the parent directory of the current files grandparent directory. 
#This has been added to ensure code is portable and can be run on any machine without having to change the file paths.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "auto_mpg"
    / "auto-mpg.data"
)

PROCESSED_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "auto_mpg"
    / "auto_mpg_cleaned.csv"
)

#This is used to confirm that Python can find the raw file and raise an error if it isnt found
if not RAW_PATH.exists():
    raise FileNotFoundError(f"Raw data file not found: {RAW_PATH}")


#Now add the missing columns
columns_names = ["mpg", 
    "cylinders", 
    "displacement", 
    "horsepower", 
    "weight", 
    "acceleration", 
    "model_year", 
    "origin", 
    "car_name"]

#Reading the raw data into pandas and adding the missing columns to the data
df = pd.read_csv(RAW_PATH, 
    names = columns_names, 
    sep = r"\s+", 
    na_values = "?", 
    quotechar = '"')

#We now preview the data to ensure that the columns have been added as intended
print(df.head())

row_count, column_count = df.shape

#The following code is used to check aspects of the data set.
print(f"Number of rows: {row_count}")
print(f"Number of columns: {column_count}")

print("\nFirst five rows:")
print(df.head())

print("\nDataset dimensions:")
print(f"Number of rows: {row_count}")
print(f"Number of columns: {column_count}")

print("\nColumn information:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nNumerical summary:")
print(df.describe().T)

print("\nRows containing missing values:")
print(df[df.isna().any(axis=1)])

#Running the following bash code produces a summary of the data set:
#python Scripts/Script1-AutoMPG/Auto-MPG-CleanUp.py

#We now create the cleand data frame.
#Start by reamoving duplicate rows and rows with missing values.
clean_df = (
    df.drop_duplicates()
    .dropna()
    .reset_index(drop=True)
)

#Check that the new data frame exists and is correctly formatted
PROCESSED_PATH.parent.mkdir(
    parents=True,
    exist_ok=True,
)

#Store the cleaned data as a new CSV file.
clean_df.to_csv(
    PROCESSED_PATH,
    index=False,
)
#Print the following information to confirm that the cleaned data set has been created
print(f"Cleaned data saved to: {PROCESSED_PATH}")
print(f"Original rows: {len(df)}")
print(f"Cleaned rows: {len(clean_df)}")

