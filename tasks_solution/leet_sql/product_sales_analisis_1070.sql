-- version with join
select s1.product_id, s1.year as first_year, s1.quantity, s1.price from sales as s1
left join sales as s2 on  s1.product_id=s2.product_id and s1.year > s2.year
where s2.product_id is null


--version with subquery
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
)

--v2.1
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS min_year
    FROM Sales
    GROUP BY product_id
) subquery
ON s.product_id = subquery.product_id AND s.year = subquery.min_years



-- version with close
WITH
  ProductToYear AS (
    SELECT product_id, MIN(year) AS year
    FROM Sales
    GROUP BY 1
  )
SELECT
  Sales.product_id,
  ProductToYear.year AS first_year,
  Sales.quantity,
  Sales.price
FROM Sales
INNER JOIN ProductToYear
  USING (product_id, year);
