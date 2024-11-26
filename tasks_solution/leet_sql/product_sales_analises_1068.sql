select p.product_name, s.year, s.price from product as p
join sales as s on p.product_id = s.product_id
