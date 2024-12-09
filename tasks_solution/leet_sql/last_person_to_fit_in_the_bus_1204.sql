select person_name from (
    select person_name,
    sum(weight) over(order by turn) as total_weight
    from queue
) as sq
where total_weight <= 1000
order by total_weight desc
limit 1


--Final Result:
--The query finds the person whose cumulative weight is less than or equal to 1000,
-- sorts them by person_name in descending order, and then returns the top result.
-- Essentially, it identifies the total_weight in numerical order (descending)
--  whose cumulative weight is less than or equal to 1000.


--- inner query
select person_name,
       sum(weight) over(order by turn) as total_weight
from queue
--Selecting Columns:
--
--person_name: This column selects the name of the person.
--
--sum(weight) over(order by turn) as total_weight: This is a window function that
--calculates a running total of the weight column, ordered by the turn column.
--
--The OVER (order by turn) clause creates a running total for the weight column,
--which means the total weight accumulates as you move down the ordered rows.
--
--Result of the Inner Query:
--The result of the inner query will be a table where each row contains a person_name
--and the total_weight so far for each turn: