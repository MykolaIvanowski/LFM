select id,
    sum(if(month='jan', revenue, null)) as Jan_Revenue,
    sum(if(month='feb', revenue, null)) as Feb_Revenue,
    sum(if(month='mar', revenue, null)) as Mar_Revenue,
    sum(if(month='apr', revenue, null)) as Apr_Revenue,
    sum(if(month='may', revenue, null)) as May_Revenue,
    sum(if(month='jun', revenue, null)) as Jun_Revenue,
    sum(if(month='jul', revenue, null)) as Jul_Revenue,
    sum(if(month='aug', revenue, null)) as Aug_Revenue,
    sum(if(month='sep', revenue, null)) as Sep_Revenue,
    sum(if(month='oct', revenue, null)) as Oct_Revenue,
    sum(if(month='nov', revenue, null)) as Nov_Revenue,
    sum(if(month='dec', revenue, null)) as Dec_Revenue
from department
group by id


--   sum(if(month='sep', revenue, null)) as Sep_Revenue,
--For each month, it sums the column revenue if the month column matches
-- that month ('jan', 'feb', etc.)
--If the month does not match, it returns null, which effectively means
-- it does not contribute to the sum for that month.