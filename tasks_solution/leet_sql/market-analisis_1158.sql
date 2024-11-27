--my version (what is main difference?)
select u.user_id as buyer_id, u.join_date, count(o.order_id) as orders_in_2019 from orders o
right join users u  on u.user_id=o.buyer_id and year(o.order_date)=2019
group by 1



-- version from inet
SELECT
   Users.user_id AS buyer_id,
   Users.join_date,
   COUNT(Orders.order_id) AS orders_in_2019
FROM Users
LEFT JOIN Orders
   ON (Users.user_id = Orders.buyer_id AND YEAR(order_date) = '2019')
GROUP BY 1;

-- version 3
SELECT a.user_id AS buyer_id,
       a.join_date,
       COALESCE(COUNT(b.order_id), 0) AS orders_in_2019
FROM Users a
LEFT JOIN Orders b ON b.buyer_id = a.user_id
   AND b.order_date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY a.user_id, a.join_date;