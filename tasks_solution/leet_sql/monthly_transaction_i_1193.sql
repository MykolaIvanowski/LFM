select
    left(trans_date, 7) as month,
    country,
    count(id) as trans_count,
    sum(state='approved') as approved_count,
    sum(amount) as trans_total_amount,
    sum(if(state='approved',amount,0)) as approved_total_amount

from transactions
group by month, country


--The main purpose of your SQL query is to summarize transaction data by month and country,
--providing key metrics such as the total number of transactions,
--the number of approved transactions, the total transaction amount,
--and the total amount of approved transactions.