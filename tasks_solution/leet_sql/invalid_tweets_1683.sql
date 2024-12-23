select tweet_id from tweets
where length(content) > 15


--do not work
select tweet_id from tweets
having length(content) > 15
-- Since there is no GROUP BY clause in this query,
--using HAVING here is incorrect and will result in an error in most SQL databases.
--The HAVING clause expects the query to perform some grouping operation first.

-- also sometimes better use char_length(),
-- because some special string character count twice with length() function