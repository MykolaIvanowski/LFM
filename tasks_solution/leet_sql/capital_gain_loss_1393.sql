select s1.stock_name,
sum(if(s1.operation='Sell',price,0))-sum(if(s1.operation='Buy',price, 0)) as capital_gain_loss
from stocks as s1
group by 1


-- some other solution
select stock_name,
sum(case
    when operation = 'Buy' then -price
    when operation = 'Sell' then price
    End) as capital_gain_loss
from stocks
group by stock_name