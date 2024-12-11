
select 
    query_name, 
    round((sum(rating/position))/count(query_name),2) as quality, 
    round(avg(if(rating<3,1,0))*100,2) as poor_query_percentage from queries
group by query_name


--Result
--The query will produce a result set where each row represents a unique query_name and includes:
--
--quality: A calculated metric based on the sum of rating/position divided by
--the count of the query name, indicating some form of quality score.
--
--poor_query_percentage: The percentage of times the rating was less than 3
--for that query name, indicating the proportion of poor ratings.