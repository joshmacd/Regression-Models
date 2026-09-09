# Auto MPG Dataset

## Project context

The Auto MPG dataset is the first dataset analysed in this regression project. The repository will be expanded over time to include additional datasets, regression techniques and machine-learning workflows.

Each dataset will have its own raw and processed data, analysis scripts, SQL queries and model outputs.

## Source

The Auto MPG dataset was obtained from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto).

## Purpose

This dataset is designed for regression analysis. The objective is to predict fuel efficiency, measured in miles per gallon (`mpg`), using vehicle characteristics such as weight, horsepower, displacement and model year.

It provides an accessible starting point for developing the project’s data-cleaning, exploratory-analysis and regression-modelling workflow before applying the same principles to more complex datasets.

## Data quality

The raw dataset:

- Contains 398 observations and nine variables.
- Does not include column names in the main data file.
- Represents missing values using `?`.
- Contains six missing values in the `horsepower` column.

## Processing

The `scripts/auto_mpg/01_clean_data.py` script adds the column names, identifies missing values and duplicates, and creates a cleaned dataset containing 392 complete observations.

The processed dataset is saved as:

`data/processed/auto_mpg/auto_mpg_cleaned.csv`