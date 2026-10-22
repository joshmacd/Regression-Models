-- Compare missing horsepower before and after cleaning.
SELECT
    'Raw' AS dataset,
    COUNT(*) AS total_cars,
    COUNT(horsepower) AS cars_with_horsepower,
    SUM(CASE WHEN horsepower IS NULL THEN 1 ELSE 0 END)
        AS missing_horsepower
FROM auto_mpg_raw

-- Joins the two select statements together
UNION ALL

SELECT
    'Cleaned' AS dataset,
    COUNT(*) AS total_cars,
    COUNT(horsepower) AS cars_with_horsepower,
    SUM(CASE WHEN horsepower IS NULL THEN 1 ELSE 0 END)
        AS missing_horsepower
FROM auto_mpg;