-- Summarise the cleaned data used for modelling.
SELECT
    COUNT(*) AS total_cars,
    ROUND(AVG(mpg), 2) AS average_mpg,
    MIN(mpg) AS minimum_mpg,
    MAX(mpg) AS maximum_mpg,
    ROUND(AVG(horsepower), 2) AS average_horsepower,
    ROUND(AVG(weight), 2) AS average_weight
FROM auto_mpg;