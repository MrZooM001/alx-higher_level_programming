-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(VALUES) AS `avg_temp`
FROM `temperature` GROUP BY `city`
ORDER BY `avg_temp` DESC;
