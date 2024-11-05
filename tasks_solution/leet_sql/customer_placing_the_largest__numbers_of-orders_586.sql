select customer_number from orders
group by customer_number
having count(*) >= All(
    select count(customer_number)
    from orders
    group by customer_number
    )


--- easy way
select customer_number from orders
group by customer_number
order by count(distinct order_number) desc limit 1;