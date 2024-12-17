
select p.product_name,  sum(o.unit) as unit from Products p
join Orders o on p.product_id = o.product_id
where left(o.order_date,7) = '2020-02'
group by p.product_name
having unit >= 100

--summary:
--The query provides a list of product names and the total number of units ordered
--for each product in February 2020, but only for those products with total orders of 100
--or more units. This can be useful for identifying popular products during a specific time period

--other solution
SELECT p.product_name,
       o.unit
FROM   (SELECT product_id,
               Sum(unit) AS unit
        FROM   orders
        WHERE  order_date BETWEEN '2020-02-01' AND '2020-02-29'
        GROUP  BY product_id
        HAVING unit >= 100) o
       INNER JOIN products p
               ON o.product_id = p.product_id

--
--Key Differences:
--Date Filtering:
--
--    First Query: Uses left(o.order_date,7) = '2020-02' to filter by year and month.
--    This approach might be less efficient, depending on the database implementation.
--
--    Second Query: Uses order_date BETWEEN '2020-02-01' AND '2020-02-29',
--    which is more explicit and can be more efficient.
--
--Join Type:
--
--    First Query: Performs the join first and then filters the results.
--
--    Second Query: Performs filtering and aggregation in a subquery before joining.
--
--Readability and Efficiency:
--
--    The second query might be more efficient because it reduces the number of rows in
--    the join operation by filtering and aggregating beforehand.
--
--    The second query is also clearer in its intent by explicitly defining the date range.