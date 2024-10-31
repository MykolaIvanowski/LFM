
select w1.id from Weather w1, Weather w2
where w1.temperature > w2.temperature
and DATEDIFF(w1.recordDate,w2.recordDate) = 1


-- version for join
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperature