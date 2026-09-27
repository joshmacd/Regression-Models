from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split  #Split data into training and test sets
from sklearn.linear_model import LinearRegression  #Fit a linear regression model
from sklearn.model_selection import KFold, cross_val_score #cross validation score on training data
from sklearn.dummy import DummyRegressor #dummyRegressor provides a simple baseline for comparison.
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score) # we use these functions to measure how well predictions match the actual target values
import matplotlib.pyplot as plt #Ploting figures 


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
print("Training target shape:", y_train.shape) #(313)
print("Testing target shape:", y_test.shape) #(79)


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

#Evaluate each model using the same five validation folds.
for name, estimator, columns in models:
    scores = cross_val_score(estimator, X_train[columns], y_train, cv=cv, scoring="neg_mean_absolute_error")

    #convert negative MAE scores into positive errors in MPG.
    fold_mae = -scores

    #store the average error and its variation across folds.
    cv_results.append({"model": name, "mean_cv_mae": fold_mae.mean(), "std_cv_mae": fold_mae.std()})

#The print the cross validation amounts in a 3x3 table with the model and the mean and standard deviation MAE(mean absoulute error)
print("\nCross-validation results (MPG):")
print(pd.DataFrame(cv_results).round(3).to_string(index=False))


#We store the predictions and test results, test results and initalised as an empty list and the predictions as an empty dictonary
test_results = []
test_predictions = {}

for name, estimator, columns in models:
    #Then fit on all training observations to find the models parameters
    estimator.fit(X_train[columns], y_train)

    #predict MPG for the 79 test cars.
    predictions = estimator.predict(X_test[columns])
    test_predictions[name] = predictions

    #We now calculate the performance metrics for the test set data.
    test_results.append({ 
        "model": name, "MAE": mean_absolute_error(y_test, predictions),
        "RMSE": mean_squared_error(y_test, predictions) ** 0.5,
        "R2": r2_score(y_test, predictions)
    })

#Print out the test data as a 
print("\nTest-set results:")
print(pd.DataFrame(test_results).round(3).to_string(index=False))



#Create the folder for saved figures.
FIGURES_PATH = PROJECT_ROOT / "outputs" / "figures" / "auto_mpg"
FIGURES_PATH.mkdir(parents=True, exist_ok=True)

#Create two plots with shared axes for a fair visual comparison.
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True, sharey=True)

model_names = ["Weight regression", "Multiple regression"]

for ax, name in zip(axes, model_names):
    #Take the predictions saved during test-set evaluation.
    predictions = test_predictions[name]

    #Positive residuals mean MPG was underestimated.
    residuals = y_test - predictions

    ax.scatter(predictions, residuals, alpha=0.7)
    ax.axhline(y=0, color="red", linestyle="--", label="Zero residual")

    ax.set_title(name)
    ax.set_xlabel("Predicted MPG")
    ax.legend()

axes[0].set_ylabel("Residual (actual - predicted MPG)")

#Save the figure in the correct location
fig.tight_layout()
fig.savefig(FIGURES_PATH / "regression_residual_comparison.png", dpi=180)

plt.show()
plt.close(fig)