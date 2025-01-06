 --  Case Study Questions
   --------------------*/
-- -- Example Query:
-- SELECT
--   	product_id,
--     product_name,
--     price
-- FROM dannys_diner.menu
-- ORDER BY price DESC
-- LIMIT 5;

-- 1. What is the total amount each customer spent at the restaurant?
select
	s.customer_id,
	sum(m.price) as total_spend
from dannys_diner.sales s
join dannys_diner.menu m using(product_id)
group by s.customer_id;

-- 2. How many days has each customer visited the restaurant?
select
	customer_id,
	count(distinct order_date) as days_visited
from dannys_diner.sales
group by customer_id;

-- 3. What was the first item from the menu purchased by each customer?
with Common_table_expresion as (
	select
		s.customer_id,
		m.product_name,
		s.order_date,
		rank() over(partition by s.customer_id order by s.order_date) as rnk,
		row_number() over(partition by s.customer_id order by s.order_date) as rn
	from dannys_diner.menu m
	join dannys_diner.sales s on s.product_id = m.product_id
	)
select
	customer_id, product_name,order_date, rnk
from common_table_expresion
where rnk = 1;


-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
select m.product_name, count(order_date)
from dannys_diner.sales s
join dannys_diner.menu  m on s.product_id=m.product_id
group by   m.product_name
order by 2 desc
limit 1;
-- 5. Which item was the most popular for each customer?
with rank_rows_orders as(
	select
		s.customer_id,
		m.product_name,
		rank() over (partition by customer_id order by count(order_date) desc) as rank_orders,
		row_number() over (partition by customer_id order by count(order_date) desc) as row_oreders
	from dannys_diner.sales s
	join dannys_diner.menu m on m.product_id=s.product_id
	group by s.customer_id, m.product_name)

select * from rank_rows_orders
where rank_orders = 1;


-- 6. Which item was purchased first by the customer after they became a member?
with first_order as(select
		m.customer_id,
		s.order_date,
		m.join_date,
		me.product_name,
		rank() over(partition by s.customer_id order by order_date) as rnk_orders,
		row_number() over (partition by s.customer_id order by order_date) as rw_orders
	from dannys_diner.members m
	join  dannys_diner.sales s on m.customer_id = s.customer_id
	join dannys_diner.menu me on me.product_id = s.product_id
	where m.join_date <= s.order_date
)

select * from first_order
where rnk_orders = 1;

-- 7. Which item was purchased just before the customer became a member?
with purchased_just as(select s.customer_id, s.order_date, mem.join_date, m.product_name,
	rank() over(partition by s.customer_id order by s.order_date desc) as rnk_date,
	row_number() over(partition by s.customer_id order by s.order_date desc) as r_date
from dannys_diner.sales s
join dannys_diner.members as mem using(customer_id)
join dannys_diner.menu as m using(product_id)
where s.order_date < mem.join_date)

select * from purchased_just
where r_date =1;

-- 8. What is the total items and amount spent for each member before they became a member?
select s.customer_id, count(s.product_id),sum(m.price) from dannys_diner.sales s
join dannys_diner.members mr using(customer_id)
join dannys_diner.menu m using(product_id)
where s.order_date < mr.join_date
group by s.customer_id;

-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
select s.customer_id,
	sum( CASE WHEN m.product_name = 'sushi'
		 THEN m.price * 20
    	 ELSE m.price * 10 END) AS points
from dannys_diner.sales s
join dannys_diner.menu m using(product_id)
group by s.customer_id;

-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
select
	s.customer_id,
	sum(case
		when s.order_date between m.join_date and (join_date +interval '6 day')
		then mu.price * 10*2
		when mu.product_name ='sushi' then mu.price*10*2
		else mu.price*10 end)
	as points_first
from dannys_diner.sales s
join dannys_diner.members m using(customer_id)
join dannys_diner.menu mu using(product_id)
where s.order_date >= m.join_date and s.order_date <='2021-01-31'
group by s.customer_id;

-- bonus question 1
select
	s.customer_id,
	s.order_date, m.product_name,
	m.price ,
	case when s.order_date<mr.join_date then 'N'
	when s.order_date>=mr.join_date then 'Y'
	else 'N' end as member
from dannys_diner.sales s
join dannys_diner.members  mr using (customer_id)
join dannys_diner.menu  m using(product_id)
order by s.customer_id, s.order_date;

-- bonus question 2
select
	s.customer_id,
	s.order_date,
	m.product_name,
	m.price,
	case when s.order_date<mr.join_date then 'N'
	when s.order_date>=mr.join_date then 'Y'
	else 'N' end as members,
	case when s.order_date>=mr.join_date then rank() over(partition by s.customer_id, (
		case when s.order_date<mr.join_date then 'N'
		when s.order_date>=mr.join_date then 'Y'
		else 'N' end)
		order by s.order_date )
	else null end
	as ranking
from dannys_diner.sales s
left join dannys_diner.members mr using(customer_id)
join dannys_diner.menu m using(product_id)
order by s.customer_id;

-- or for better reading
with rank_member as (select
		s.customer_id,
		s.order_date,
		m.product_name,
		m.price,
		case when s.order_date<mr.join_date then 'N'
		when s.order_date>=mr.join_date then 'Y'
		else 'N' end as members
	from dannys_diner.sales s
	left join dannys_diner.members mr using(customer_id)
	join dannys_diner.menu m using(product_id)
	order by s.customer_id)

select *,
	case when members='N' then null
	else rank() over(partition by customer_id, members order by order_date ) end
	as ranking
from rank_member;

--else rank() over(partition by customer_id, members order by order_date ) end
-- adding members in sate mean that rank() function will not count nulls in ranking column