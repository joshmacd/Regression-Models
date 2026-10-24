#My current model performs well, but its residual plot shows a curved pattern.
#This suggests it may be missing nonlinear relationships.

#--------------------- Quadratic Regression ---------------------

#Linear regression assumes each extra unit of weight has the same effect on MPG, holding the other predictors constant.
#Adding weight^2 allows this effect to change with weight.
#Interactions, such as weight × horsepower, allow one predictor's effect to depend on another predictor.
#These terms may reduce the curved residual pattern.

#--------------------- Ridge Regularisation ---------------------

#Extra terms make the model more flexible, which can lead to overfitting.
#Ridge penalises large coefficients, which can help the model generalise.
#We will scale the predictors so their different units do not distort the penalty.

#--------------------- Model Evaluation ---------------------

#We will compare models using five fold cross validation on the training data.
#The 313 training cars are split into five roughly equal groups
#Each model is fitted on four groups and validated on the remaining group
#This repeats five times, so every group is used for validation once

#We compare average MAE and its variation across folds.
#Each fit uses around 250 cars, with around 63 used for validation
#Five folds balances training size, validation size and computation
#Every model uses the same folds, and the separate test set stays outside them

#Scaling and polynomial feature generation will run inside a pipeline, so preprocessing 
#is fitted using only the training portion of each fold.


from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline 

#Locate the cleaned dataset.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data/processed/auto_mpg/auto_mpg_cleaned.csv"

#Load the data.
df = pd.read_csv(DATA_PATH)

#Select the predictors and target.
predictors = ["weight", "horsepower", "model_year"]
X = df[predictors]
y = df["mpg"]

#Check the dimensions.
print("Predictor shape:", X.shape)
print("Target shape:", y.shape)