from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split #train the regression model
from sklearn.linear_model import LinearRegression #Plot regression model
from sklearn.model_selection import KFold, cross_val_score #cross validation score on training data
from sklearn.dummy import DummyRegressor

#We locate and load the cleaned data set
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "auto_mpg"
    / "auto_mpg_cleaned.csv"
)

#Raise an error if the data set can't be found
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Cleaned data file not found: {DATA_PATH}")

#Load the data and check the available column names.
df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())


#We select the weight, horsepower and model year as our three predictors.
predictors = ["weight", "horsepower", "model_year"]
X = df[predictors]

# Select the target we want to predict.
y = df["mpg"]

#We set our training and testing variables and also save 20% of the data for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#We check the dimensions of the data sets with the training and testing sets
print("\nTraining predictor shape:", X_train.shape) #(313,3)
print("Testing predictor shape:", X_test.shape) #(79,3)
print("Training target shape:", y_train.shape) #(313,1)
print("Testing target shape:", y_test.shape) #(79,1)


#We now creat the the linear regression model with our the training data.
model = LinearRegression()
model.fit(X_train, y_train)

#Find the model intercept, the prediction where all three predictors are zero
intercept = model.intercept_
print("\nModel intercept:", intercept)

#We find the fitted coefficient and match them with their predictor.
coefficients = pd.DataFrame({
    "predictors": predictors,
    "coefficient": model.coef_,
})

#Print the model coeficients
print("\nModel coefficients:")
print(coefficients.to_string(index=False))

#Choose five validation folds for every model
cv = KFold(n_splits=5, shuffle=True, random_state=42)

#We now define each of our models model and the predictors that the model uses.
models = [
    ("Mean baseline", DummyRegressor(strategy="mean"), ["weight"]),
    ("Weight regression", LinearRegression(), ["weight"]),
    ("Multiple regression", LinearRegression(), predictors),
]

#initalise an empty list to store the cross validation results
cv_results = []

#Evaluate the models using the same cross validation 
for name, estimator, columns in models:
    scores = cross_val_score(estimator, X_train[columns], y_train, cv=cv, scoring="neg_mean_absolute_error")

    #Using Scikit-learn to returns negative MAE score and convert it back to a positive error in MPG.
    fold_mae = -scores

    #save the average error and its variation across folds for a comparision
    cv_results.append({
        "model": name,
        "mean_cv_mae": fold_mae.mean(),
        "std_cv_mae": fold_mae.std(),
    })

#The print the cross validation amounts in a 3x3 table with the model and the mean and standard deviation MAE(mean absoulute error)
print("\nCross-validation results (MPG):")
print(pd.DataFrame(cv_results).round(3).to_string(index=False))

