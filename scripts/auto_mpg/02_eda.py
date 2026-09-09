from pathlib import Path

#Important the necessary libraries required for data analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#We set the project root - parent 2 identifies the project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "auto_mpg"
    / "auto_mpg_cleaned.csv"
)

FIGURES_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "figures"
    / "auto_mpg"
)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned data file not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

#Ensure that the figures path exists and if not create it, (parents=True - ensures that missing parent directories are created)
FIGURES_PATH.mkdir(parents=True, exist_ok=True,)

#we now preview the data and print some common statistics about the data set
#Summary statistics prints the count, mean, standard deviation, minimum, maximum and quartile ranges
print("\nSummary statistics:")
print(df.describe().T)

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

#We select only the numerical columns for the correlation analysis
numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr()

#Display the correlation matrix to display 
print("\nCorrelation with MPG:")
print(correlation_matrix["mpg"].sort_values(ascending=False)) #sets the highest correlation with mpg first


#We set a theme for the plot and keep the style consistent
sns.set_theme(style="whitegrid")

#We plot the distribution of MPG using a histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="mpg", bins=20, kde=True, color="skyblue",)

#Set up the title and labels for the plot 
plt.title("Distribution of Fuel Efficiency")
plt.xlabel("Miles per Gallon")
plt.ylabel("Number of Cars")
plt.tight_layout() #Removes clipping of labels

#Save the figure to a figure path 
plt.savefig(FIGURES_PATH / "mpg_distribution.png", dpi=300,)
plt.close()


# We now plot the MPG against vehicle weight using a linear regression 
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="weight", y="mpg",seed =42, scatter_kws={"alpha": 0.6}, line_kws={"color": "red"},)

#Set the titles and labels for the plot
plt.title("Fuel Efficiency Against Vehicle Weight")
plt.xlabel("Vehicle Weight")
plt.ylabel("Miles per Gallon")
plt.tight_layout()

#Saving the figure to the figures path
plt.savefig(FIGURES_PATH / "mpg_vs_weight.png", dpi=300,)
plt.close()


# We again use regplot to visualise the relationship between MPG and horsepower using linear regression
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="horsepower", y="mpg",seed =42, scatter_kws={"alpha": 0.6}, line_kws={"color": "red"},)

#Set the titles and labels for the plot
plt.title("Fuel Efficiency Against Horsepower")
plt.xlabel("Horsepower")
plt.ylabel("Miles per Gallon")
plt.tight_layout()

#Saving the figure in the appropriate root
plt.savefig(FIGURES_PATH / "mpg_vs_horsepower.png", dpi=300,)
plt.close()


#display the correlation heatmap 
plt.figure(figsize=(10, 7))

sns.heatmap( correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0,)

#setting the title for the heatmap and saving the figure to the appropriate path
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig(FIGURES_PATH / "correlation_heatmap.png", dpi=300,)
plt.close()

#Print the following text to confirm that the figures have been generated and saved in the appropriate location
print(f"\nFigures saved in: {FIGURES_PATH.resolve()}")