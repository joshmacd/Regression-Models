from pathlib import Path

#Importing the pandas library in order to clean the data
import pandas as pd

#Store the paths of the raw and processed data as varibles
RAW_PATH = Path("Data/Raw-Data/AutoMPG/auto-mpg.data")
PROCESSED_PATH = Path("Data/Processed-Data/AutoMPG/auto-mpg-cleaned.csv")

#This is used to confirm that Python can find the raw file.
print(f"Raw file found: {RAW_PATH.exists()}")


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
    sep = "r\s+", 
    na_values = "?", 
    quotechar = '"')

#We now preview the data to ensure that the columns have been added as intended
display(df.head())

row_count, column_count = df.shape

print(f"Number of rows: {row_count}")
print(f"Number of columns: {column_count}")