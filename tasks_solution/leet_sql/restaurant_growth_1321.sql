with amount_t as (
    select visited_on,
    sum(amount) as amount
from customer
group by visited_on
)


select t1.visited_on,
    round(sum(t2.amount),2) as amount,
    round(avg(t2.amount),2) as average_amount
from amount_t as t1, amount_t as t2
where datediff(t1.visited_on,t2.visited_on) between 0 and 6
group by 1
having count(*)>6
order by 1


explanations:

with amount_t as (
    select visited_on,
    sum(amount) as amount
    from customer
    group by visited_on
)
--This part creates a CTE named amount_t, which calculates
--the total amount for each visited_on date by grouping the data from the customer table.

select t1.visited_on,
    round(sum(t2.amount),2) as amount,
    round(avg(t2.amount),2) as average_amount
from amount_t as t1, amount_t as t2
--This part selects the visited_on date from t1, the sum of amount from t2,
--and the average amount from t2.
--
--It uses a self-join (cross join) of the amount_t CTE with aliases t1 and t2.

where datediff(t1.visited_on, t2.visited_on) between 0 and 6
--This filters the rows to include only those where the date difference
--between t1.visited_on and t2.visited_on is between 0 and 6 days.
--Essentially, it looks at a 7-day window (current day plus the previous 6 days).


having count(*) > 6
--The having count(*) > 6 condition ensures that only those groups with
--more than 6 entries are included.
--This is likely to ensure that the 7-day window is fully populated.
по суті фільтрує, залишаючи тільки значення з різницею у 6 днів


--if it is not clear select next value in sql query:
--t1.visited_on,
--t2.visited_on,
--round(sum(t2.amount),2) as amount,
--round(avg(t2.amount),2) as average_amount,
--datediff(t1.visited_on,t2.visited_on) as days_diff