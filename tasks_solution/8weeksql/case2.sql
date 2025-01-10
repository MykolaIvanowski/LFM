--A. Pizza Metrics
--
--    How many pizzas were ordered?
select count(*) as pizzas_ordered
from pizza_runner.customer_orders;
--    How many unique customer orders were made?
select count(distinct customer_id) as unique_customers
from pizza_runner.customer_orders;

--    How many successful orders were delivered by each runner?
select runner_id, count(order_id)
from pizza_runner.runner_orders
where duration not like 'null'
group by runner_id;
--    How many of each type of pizza was delivered?
select pizza_name, count(ro.order_id)
from pizza_runner.runner_orders as ro
join pizza_runner.customer_orders as co on ro.order_id=co.order_id
join pizza_runner.pizza_names as pn on pn.pizza_id=co.pizza_id
where ro.duration not like 'null'
group by pizza_name;
--    How many Vegetarian and Meatlovers were ordered by each customer?
select customer_id,pn.pizza_name, count(*)
from pizza_runner.pizza_names pn
join pizza_runner.customer_orders co using(pizza_id)
where pn.pizza_name = 'Vegetarian' or pn.pizza_name='Meatlovers'
group by customer_id, pizza_name;

--    What was the maximum number of pizzas delivered in a single order?
select order_time, count(pizza_id) as max_pizza_ordered
from pizza_runner.customer_orders
group by order_time
order by 2 desc
limit 1;

--    For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
select
	co.customer_id,
	sum(case when ((extras ~ '^[a-zA-Z0-9]' and extras is not null and extras <>'null')
	or (exclusions ~ '^[a-zA-Z0-9]' and exclusions is not null and exclusions<>'null'))
	then 1 else 0 end) as change,
	sum(case when ((extras ~ '^[a-zA-Z0-9]' and extras is not null and extras <>'null')
	or (exclusions ~ '^[a-zA-Z0-9]' and exclusions is not null and exclusions<>'null'))
	then 0 else 1 end) as no_change
from pizza_runner.customer_orders co
join pizza_runner.runner_orders ro on co.order_id =ro.order_id
where pickup_time <> 'null'
group by co.customer_id;

--    How many pizzas were delivered that had both exclusions and extras?
select
	sum(
		case when co.exclusions ~ '^[a-zA-Z0-9]' and co.extras ~ '^[a-zA-Z0-9]'
		and co.extras <> 'null' and co.exclusions <> 'null'
		and co.extras is not null and co.exclusions is not null
		then 1 else 0 end
	) as pizzas_both_changes
from pizza_runner.customer_orders co
join pizza_runner.runner_orders ro on co.order_id =ro.order_id
where pickup_time <> 'null';

--    What was the total volume of pizzas ordered for each hour of the day?
select
	extract(hour from order_time) as hour_of_day,
	count(pizza_id) as pizza_ordered
from pizza_runner.customer_orders
group by 1;

--    What was the volume of orders for each day of the week?
select
	to_char(order_time + interval '2 day', 'Day'),
	count(*) as total_pizza_ordered
from pizza_runner.customer_orders
group by 1;
--
--B. Runner and Customer Experience
--
--    How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)
select date_trunc('week', registration_date) + interval '4 days' as week, count(runner_id)
from pizza_runner.runners
where registration_date >= '2021-01-01'
group by 1
order by 1;

--    What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pickup the order?
select runner_id,
	avg(extract(EPOCH FROM
	(cast(pickup_time as timestamp) - cast(order_time as timestamp)))/60)
	as average_time
from pizza_runner.runner_orders ro
join pizza_runner.customer_orders co on ro.order_id=co.order_id
where pickup_time <> 'null'
group by runner_id;
--    Is there any relationship between the number of pizzas and how long the order takes to prepare?
with count_per_order as(
	select co.order_id,
		count(pizza_id) count_pizza,
		extract(epoch from (cast(pickup_time as timestamp)-cast(order_time as timestamp)))/60
		as time_diff
	from pizza_runner.runner_orders ro
	join pizza_runner.customer_orders co using(order_id)
	where pickup_time <> 'null'
	group by pickup_time, order_time, co.order_id
)

select count_pizza,avg(time_diff) from count_per_order
group by 1;
--    What was the average distance travelled for each customer?
select co.customer_id,
	avg(cast(replace(distance,'km','') as double precision))
from pizza_runner.runner_orders ro
join pizza_runner.customer_orders co on ro.order_id = co.order_id
where pickup_time<>'null'
group by co.customer_id;

--    What was the difference between the longest and shortest delivery times for all orders?
select
	max(cast(regexp_replace(duration,'[^0-9]','','g') as double precision)) -
	min(cast(regexp_replace(duration,'[^0-9]','','g') as double precision))
	as diff_delivery
from pizza_runner.runner_orders
where pickup_time<>'null';

--    What was the average speed for each runner for each delivery and do you notice any trend for these values?
select order_id, runner_id,
	avg(
		(cast(replace(distance,'km','') as double precision)) /
		(cast(regexp_replace(duration,'[^0-9]','','g') as double precision))
	)as avg_distance
from pizza_runner.runner_orders
where pickup_time <> 'null'
group by order_id, runner_id
order by 2,1; -- the longer wor then faster move?

--    What is the successful delivery percentage for each runner?
select runner_id,
	sum(case when distance = 'null' then 0 else 1 end)::float/
	count(runner_id)*100 as percetage_rate
from pizza_runner.runner_orders
group by runner_id;

--
--C. Ingredient Optimisation
--    What are the standard ingredients for each pizza?
with pizza_toppings as(
	select
		pr.pizza_id,
		unnest(string_to_array(toppings,','))::int as topping_id,
		pizza_name
	from pizza_runner.pizza_recipes pr
	join pizza_runner.pizza_names pn on pn.pizza_id=pr.pizza_id
)

select topping_name
from pizza_toppings p1
join pizza_runner.pizza_toppings p2 on p1.topping_id=p2.topping_id
group by topping_name
having count(distinct p1.pizza_id)>1;

--    What was the most commonly added extra?
with extras_toppings as(
	select order_id,
		unnest(string_to_array(extras,','))::int as topping_id
	from pizza_runner.customer_orders
	where extras <> 'null'
)

select count(et.topping_id), topping_name from extras_toppings et
join pizza_runner.pizza_toppings pt on pt.topping_id = et.topping_id
group by topping_name
order by 1 desc
limit 1;

--    What was the most common exclusion?
--    Generate an order item for each record in the customers_orders table in the format of one of the following:
--        Meat Lovers
--        Meat Lovers - Exclude Beef
--        Meat Lovers - Extra Bacon
--        Meat Lovers - Exclude Cheese, Bacon - Extra Mushroom, Peppers
--    Generate an alphabetically ordered comma separated ingredient list for each pizza order from the customer_orders table and add a 2x in front of any relevant ingredients
--        For example: "Meat Lovers: 2xBacon, Beef, ... , Salami"
--    What is the total quantity of each ingredient used in all delivered pizzas sorted by most frequent first?
--
--D. Pricing and Ratings
--
--    If a Meat Lovers pizza costs $12 and Vegetarian costs $10 and there were no charges for changes - how much money has Pizza Runner made so far if there are no delivery fees?
--    What if there was an additional $1 charge for any pizza extras?
--        Add cheese is $1 extra
--    The Pizza Runner team now wants to add an additional ratings system that allows customers to rate their runner, how would you design an additional table for this new dataset - generate a schema for this new table and insert your own data for ratings for each successful customer order between 1 to 5.
--    Using your newly generated table - can you join all of the information together to form a table which has the following information for successful deliveries?
--        customer_id
--        order_id
--        runner_id
--        rating
--        order_time
--        pickup_time
--        Time between order and pickup
--        Delivery duration
--        Average speed
--        Total number of pizzas
--    If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost for extras and each runner is paid $0.30 per kilometre traveled - how much money does Pizza Runner have left over after these deliveries?
--
--E. Bonus Questions
--
--If Danny wants to expand his range of pizzas - how would this impact the existing data design? Write an INSERT statement to demonstrate what would happen if a new Supreme pizza with all the toppings was added to the Pizza Runner menu?