from pathlib import Path

#Importing the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Importing the sklean metrics to evaluate the model performance
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
#Importing DummyRegressor to create a simple baseline model for comparison
from sklearn.dummy import DummyRegressor

#Importing matplotlib in order to visualise the comparision between the models.
import matplotlib.pyplot as plt


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

#Now use the model to make a prediction on the target variable using the testing data set
y_pred = model.predict(X_test)

#Compare actual MPG from the data set with the model's predictions.
comparison = pd.DataFrame({"actual_mpg": y_test, "predicted_mpg": y_pred})

#print the first tent rows of the comparision dataframe to see how the model performed on the test data set
print("\nActual versus predicted MPG:")
print(comparison.head(10))

#Now we evaluate the model performance using the sklearn metrics on the test set

mean_abs_error = mean_absolute_error(y_test, y_pred) # Calculate mean absolute error
root_mean_square_error = (mean_squared_error(y_test, y_pred)) ** 0.5 # Calculate root mean square error
r2 = r2_score(y_test, y_pred) # Calculate R-squared 

#Note that R^2 is a statistical measure of how well the regression predictions approximate the real data points. An R^2 of 1 indicates that the regression predictions perfectly fit the data.
#The RMSE is the square root of the average of the squared differences between predicted and actual values. The lower the RMSE, the better the model's performance.
#The MAE is the average of the absolute differences between predicted and actual values. The lower the MAE, the better the model's performance.

#Output the performance metrics
print("\nTest-set performance:")
print(f"Mean Absolute Error:  {mean_abs_error:.3f} MPG")
print(f"Root Mean Square Error: {root_mean_square_error:.3f} MPG")
print(f"R-squared:   {r2:.3f}")

#We now fit a baseline that always predicts the training-set mean MPG. This allows us to compare the performance
#of the regression model against a baseline model and help us ensure the regression model is learning something from the data.
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train) #fit with the trading data set

baseline_pred = baseline.predict(X_test)

#Now compare both models on the same test cars using the metrics we defined above
#Define a panda dataframe
results = pd.DataFrame({
    "model": [ "Mean baseline", "Weight regression"], "MAE": [mean_absolute_error(y_test, baseline_pred), mean_abs_error],
    "RMSE": [ mean_squared_error(y_test, baseline_pred) ** 0.5, root_mean_square_error],
    "R2": [ r2_score(y_test, baseline_pred), r2],
})

#Display the results table
print("\nModel comparison:")
print(results.round(3).to_string(index=False))

#Now work out the reduction in average absolute error as a percent
baseline_mean_abs_error = results.loc[0, "MAE"]
improvement = (baseline_mean_abs_error - mean_abs_error) / baseline_mean_abs_error * 100

#output the reduction in average absolute error
print(f"\nThe weight model reduces MAE by {improvement:.1f}%.")

#We initalise a location for the figures to be saved
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FIGURES_PATH = PROJECT_ROOT / "outputs" / "figures" / "auto_mpg"
FIGURES_PATH.mkdir(parents=True, exist_ok=True)

#We firstly plot each cars MPG from the testing data against its predicted MPG.
fig, ax = plt.subplots(figsize=(7, 6))
ax.scatter(y_test, y_pred, alpha=0.7)

#Add diagonal line (y=x) accross the lower,upper range as a reference to show perfect predictions
lower = min(y_test.min(), y_pred.min()) - 1
upper = max(y_test.max(), y_pred.max()) + 1

ax.plot(
    [lower, upper],
    [lower, upper],
    color="red",
    linestyle="--",
    label="Perfect prediction",
)

ax.set(
    xlabel="Actual MPG",
    ylabel="Predicted MPG",
    title="Weight Model: Actual vs Predicted MPG",
    xlim=(lower, upper),
    ylim=(lower, upper),
)
ax.set_aspect("equal", adjustable="box")
ax.legend()

#Save the figure in the correcct location after generating 
fig.tight_layout()
fig.savefig(
    FIGURES_PATH / "simple_linear_regression_actual_vs_predicted.png",
    dpi=180,
)
plt.show()
plt.close(fig)
