--
select distinct x.num as ConsecutiveNums from logs as x
join logs as y on x.id = y.id + 1 and x.num = y.num
join logs as z on x.id = z.id +2 and x.num = z.num

-- cte solutions
WITH
  LogsNeighbors AS (
    SELECT
      *,
      LAG(num) OVER(ORDER BY id) AS prev_num,
      LEAD(num) OVER(ORDER BY id) AS next_num
    FROM LOGS
  )
SELECT DISTINCT num AS ConsecutiveNums
FROM LogsNeighbors
WHERE
  num = prev_num
  AND num = next_num;