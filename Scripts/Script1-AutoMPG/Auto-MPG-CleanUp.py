from pathlib import Path

#Importing the pandas library in order to clean the data
import pandas as pd

#Store the paths of the raw and processed data as varibles
RAW_PATH = Path("Data/Raw-Data/AutoMPG/auto-mpg.data")
PROCESSED_PATH = Path("Data/Processed-Data/AutoMPG/auto-mpg-cleaned.csv")

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
