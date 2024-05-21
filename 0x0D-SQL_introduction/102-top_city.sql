-- Ensure you are using the correct database
USE hbtn_0c_0;

-- Display the top 3 cities' temperatures during July and August ordered by temperature in descending order
SELECT
    city,
    AVG(temperature) AS avg_temp
FROM
    temperatures
WHERE
    month IN ('July', 'August')
GROUP BY
    city
ORDER BY
    avg_temp DESC
LIMIT 3;
