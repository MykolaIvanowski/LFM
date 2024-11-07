select max(num) as num from (select num from mynumbers
group by num
having count(num) = 1) as t


--alternative solutions
SELECT
    CASE
        WHEN COUNT(1) = 1 THEN num
        ELSE NULL
    END AS num
FROM MyNumbers
GROUP BY num
ORDER BY 1 DESC
LIMIT 1;