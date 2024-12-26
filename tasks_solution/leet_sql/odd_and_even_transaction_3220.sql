
select transaction_date,
        sum(if(mod(amount,2) = 1, amount,0)) as odd_sum,
        sum(if(mod(amount,2) = 0, amount,0)) as even_sum
from transactions
group by 1
order by 1

--question
--Write a solution to find the sum of amounts for odd and even transactions for each day.
--If there are no odd or even transactions for a specific date, display as 0.