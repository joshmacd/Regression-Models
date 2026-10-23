-- Compare fuel efficiency by model year, adding the model year to 1900 to 
-- get correct year format

SELECT
    model_year + 1900 AS model_year,
    COUNT(*) AS total_cars,
    ROUND(AVG(mpg), 2) AS average_mpg,
    ROUND(AVG(horsepower), 2) AS average_horsepower,
    ROUND(AVG(weight), 2) AS average_weight
FROM auto_mpg
GROUP BY model_year
ORDER BY model_year;