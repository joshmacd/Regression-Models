from pathlib import Path

#Importing the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Load the data path and ensure that the cleaned data exists
DATA_PATH = Path(
    "data/processed/auto_mpg/auto_mpg_cleaned.csv"
)

#Raise an error if cleaned data is not found
if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned data file not found: {DATA_PATH}"
    )

#load the cleaned data into the pandas dataframe 
df = pd.read_csv(DATA_PATH)

#Prview the data and print the shape and first five rows of the dataset
print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

#We now define the predictor and target variables, X, Y, respectively
X = df[["weight"]]
y = df["mpg"]

#Print the shapes of the predictor and target variables to ensure they are correctly defined
print("\nPredictor shape:", X.shape)
print("Target shape:", y.shape)

#We now create traning and testing data sets to evealate the model performance.
#test_size = 0.20 stores 20% of the data for testing and the remaining 80% for training the model

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.20, random_state=42,)

#Now we print the length of the training and testing data sets to ensure they are consistent.
#We expect the training data set to be 80% of the total data and the testing data set to be 20% of the total data

print("\nTraining observations:", len(X_train))
print("Testing observations:", len(X_test))


#We now create a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train) #fit the model with the trained data

#Output the model intercept and the coefficient weights for the predictor variable
print("\nModel intercept:", model.intercept_)
print("Weight coefficient:", model.coef_[0])
