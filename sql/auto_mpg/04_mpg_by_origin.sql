-- Compare fuel efficiency by origin.
-- Case statement converts the original codes into clear labels for each origin

SELECT
    CASE origin
        WHEN 1 THEN 'USA'
        WHEN 2 THEN 'Europe'
        WHEN 3 THEN 'Japan'
    END AS origin,
    COUNT(*) AS total_cars,
    ROUND(AVG(mpg), 2) AS average_mpg,
    ROUND(AVG(horsepower), 2) AS average_horsepower,
    ROUND(AVG(weight), 2) AS average_weight
FROM auto_mpg
GROUP BY origin
ORDER BY average_mpg DESC;