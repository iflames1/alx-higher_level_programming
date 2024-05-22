-- Display the top 3 cities' temperatures during July and August ordered by
-- temperature in descending order
SELECT
    state,
    MAX(value) as max_temp
FROM
    temperatures
GROUP BY
    state
ORDER BY
    state
