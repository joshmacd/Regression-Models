# Regression-Models
A personal project for developing data-analysis skills with Python and SQL while exploring regression models and practical machine-learning workflows.

The repository will contain several datasets over time. Each dataset will have its own cleaning, exploratory-analysis and modelling workflow.


## Project goals

This repository documents my progress as I learn to:

 - Clean, explore, and analyze data with Python

 - Query and transform data using SQL

 - Visualize relationships and communicate findings

 - Build and evaluate regression models

 - Organize reproducible data science projects

 - Apply good practices such as testing and reusable code

## Current project progress (9/9/26):

- [x] Established a structure that can support multiple datasets.
- [x] Added and documented the Auto MPG dataset.
- [x] Created a Python data-cleaning workflow.
- [x] Performed initial exploratory data analysis.
- [x] Generated and saved data visualisations.
- [ ] Build and evaluate a simple linear regression model.
- [ ] Add SQL-based analysis.
- [ ] Build a multiple linear regression model.
- [ ] Add residual diagnostics and model validation.
- [ ] Compare regularised and nonlinear regression models.

## First dataset: Auto MPG

The first dataset included in the project is the Auto MPG dataset from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto).

The objective is to predict fuel efficiency, measured in miles per gallon (`mpg`), using vehicle characteristics such as:

- Weight
- Horsepower
- Displacement
- Cylinders
- Acceleration
- Model year
- Origin

The raw dataset contains 398 observations. Six observations have missing horsepower values, leaving 392 complete observations in the processed dataset.

More information is available in the [Auto MPG dataset documentation](data/raw/auto_mpg/README.md).

## Repository Structure

```text
Regression-Models/
├── data/
│   ├── raw/
│   │   └── auto_mpg/              # Original Auto MPG files
│   └── processed/
│       └── auto_mpg/              # Cleaned Auto MPG dataset
├── scripts/
│   └── auto_mpg/
│       ├── 01_clean_data.py       # Data inspection and cleaning
│       └── 02_eda.py              # Exploratory analysis and figures
├── outputs/
│   └── figures/
│       └── auto_mpg/              # Generated Auto MPG figures
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE


## Installation

Before running the project, install the required Python libraries from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

This installs the libraries currently required for data processing, analysis and visualisation, including pandas, Matplotlib and Seaborn.

## Running the project

Run the script:

```bash
python scripts/X/Y.py
```
where scripts/X/Y is the respective module that you wish to run.


