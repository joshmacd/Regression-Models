from pathlib import Path

#Important the necessary libraries required for data analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#store the path of the cleaned data as Proj_Root
PROJ_ROOT = Path("Data/Processed-Data/AutoMPG/auto-mpg-cleaned.csv")

#We now choose the an appropriate path to store the cleaned data and figures generated from the analysis
DATA_PATH = (
    PROJECT_ROOT
    / "Data"
    / "Processed-Data"
    / "AutoMPG"
    / "auto-mpg-cleaned.csv"
)

FIGURES_PATH = (
    PROJECT_ROOT
    / "Outputs"
    / "Figures"
    / "AutoMPG"
)

#Now we read the cleaned data from script 1 into the panda frame
df = pd.read_csv(DATA_PATH)

FIGURES_PATH.mkdir(parents=True, exist_ok=True)

#we now preview the data and print some common statistics about the data set
#Summary statistics prints the count, mean, standard deviation, minimum, maximum and quartile ranges
print("\nSummary statistics:")
print(df.describe().T)

#This prints the correlation between numerical features and the target varible (mpg) 
print("\nCorrelation with MPG:")
print(
    df.select_dtypes(include="number")
    .corr()["mpg"]
    .sort_values(ascending=False)
)

#This prints the average MPG across different cylinder sizes
print("\nAverage MPG by cylinder count:")
print(
    df.groupby("cylinders")["mpg"]
    .mean()
    .round(2)
)

#This prints the average MPG across different model years
print("\nAverage MPG by model year:")
print(
    df.groupby("model_year")["mpg"]
    .mean()
    .round(2)
)

# We now generate some figures to visulalise the data and relationships between the variables.
#The figures are saved in the Outputs/Figures/AutoMPG directory.