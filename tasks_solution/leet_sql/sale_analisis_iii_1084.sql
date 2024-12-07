
select  p.product_id, p.product_name from product p
join sales s on p.product_id=s.product_id
group by s.product_id
having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31'

--interesting version (not in between (because between is not correct))
SELECT DISTINCT p.product_id, p.product_name
FROM Product as p
LEFT JOIN Sales AS s ON p.product_id=s.product_id
WHERE s.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
);