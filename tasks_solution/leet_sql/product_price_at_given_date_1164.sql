
select distinct p2.product_id, coalesce(
    (select new_price
    from products p1
    where change_date <= '2019-08-16' and p1.product_id=p2.product_id
    order by p1.change_date desc
    limit 1
    ) ,10) as price
    from products p2


--ORDER BY p1.change_date DESC:
--Orders the results by change_date in descending order,
--so the most recent change date comes first.

--LIMIT 1: Limits the result to the first row, which is the most recent new_price
--before or on 2019-08-16

Retrieve the distinct product_id values from the products table.

For each product_id, find the most recent new_price up to and including 2019-08-16.
If no such price is found (i.e., the subquery returns NULL),
the COALESCE function will return 10 as the default price.

This query is useful for getting the latest price of each product as of a certain date,
and it provides a default value if no price is available.

Отримайте окремі значення product_id із таблиці продуктів.

Для кожного product_id знайдіть останню new_price до 2019-08-16 включно.
Якщо така ціна не знайдена (тобто підзапит повертає NULL),
функція COALESCE поверне 10 як ціну за замовчуванням.

Цей запит корисний для отримання останньої ціни кожного продукту станом на певну дату,
і він надає значення за умовчанням, якщо ціна недоступна