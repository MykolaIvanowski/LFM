select p.product_id, coalesce(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price from prices as p
left join unitssold as u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by 1


--This query provides a clear and accurate calculation of
--the average price at which products were sold,
--weighted by the number of units sold during their respective pricing periods.
