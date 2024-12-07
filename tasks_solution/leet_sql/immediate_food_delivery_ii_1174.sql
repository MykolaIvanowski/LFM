# Write your MySQL query statement below
select round(
    (
    select count(*) from
        (
            select customer_id from delivery
            group by customer_id
            having min(order_date) = min(customer_pref_delivery_date)
        ) as d
    )* 100.0/count(distinct customer_id), 2) as immediate_percentage
from delivery



--Final Result
--The query returns the percentage of customers whose first order date was the same
--as their preferred delivery date, rounded to two decimal places,
--and labels this result as immediate_percentage


--inner sub query
--select customer_id from delivery
--group by customer_id
--having min(order_date) = min(customer_pref_delivery_date)
--Purpose: Find customers whose first order date is the same as their preferred delivery date.


--middle subquery
--select count(*) from
--    (
--        select customer_id from delivery
--        group by customer_id
--        having min(order_date) = min(customer_pref_delivery_date)
--    ) as d
--Purpose: Count the number of customers who had their first order delivered on their preferred date.



--quoter query
--select round(
--    (
--    select count(*) from
--        (
--            select customer_id from delivery
--            group by customer_id
--            having min(order_date) = min(customer_pref_delivery_date)
--        ) as d
--    )* 100.0/count(distinct customer_id), 2) as immediate_percentage
--from delivery
--Purpose: Calculate the percentage of such customers and round it to 2 decimal places.
