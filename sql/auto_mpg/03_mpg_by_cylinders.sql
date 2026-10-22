-- Compare fuel efficiency by cylinder count.
SELECT
    cylinders,
    COUNT(*) AS total_cars,
    ROUND(AVG(mpg), 2) AS average_mpg,
    ROUND(AVG(horsepower), 2) AS average_horsepower,
    ROUND(AVG(weight), 2) AS average_weight
FROM auto_mpg
GROUP BY cylinders
ORDER BY cylinders;