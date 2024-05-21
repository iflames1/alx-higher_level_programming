-- Ensure you are using the correct database
USE hbtn_0c_0;

-- Display the average temperature by city, ordered by temperature in descending order
SELECT
    city,
    AVG(temperature) AS avg_temp
FROM
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp DESC;
