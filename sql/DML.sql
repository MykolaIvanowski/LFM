-- Data Manipulation Language   DDL


-- having vs where

-- WHERE Clause is used to filter the records from the table
-- based on the specified condition. HAVING Clause is used to filter record
-- from the groups based on the specified condition.

--WHERE comes before GROUP BY, which means
--WHERE clause filter rows before performing aggregate calculations.
--HAVING comes after GROUP BY, which means the HAVING clause filters rows
--after performing aggregate calculations. Consequently,
--HAVING is slower than WHERE in terms of efficiency and should be avoided
--wherever possible.

--We can combine the WHERE and HAVING clause together in a SELECT query.
--In this case, the WHERE clause is used first to filter individual rows.
--The rows are then grouped, perform aggregate calculations, and finally,
--the HAVING clause is used to filter the groups.

--The WHERE clause retrieves the desired data based on the specified condition.
--On the other hand, the HAVING clause first fetches whole data,
--and then separation is done based on the specified condition.

--WHERE clause is a pre-filter, whereas HAVING clause is a post-filter.

--why use join
--Explicit joins convey intent, leaving the where clause to do the filtering.
--It is cleaner and it is standard, and you can do things such
--as left outer or right outer which is harder to do only with where.
--You can't use WHERE to combine two tables


-- join is faster than where?
--Using WHERE or ON to JOIN the data should produce the same query plan.

-- difference on join vs where
--JOINs are operations on sets that can produce more records or less records
--in the result than you had in the original tables.
--On the other side WHERE will always restrict the number of results.

--  INNER JOIN is generally faster than OUTER JOIN




The conceptual order of query processing is:

1. FROM - Including JOINs
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY


-- join vs subqueries

--joins tend to execute faster. In fact, query retrieval time using
--joins will almost always outperform one that employs a subquery.
--The reason is that joins mitigate the processing burden on the database
--by replacing multiple queries with one join query.
--This in turn makes better use of the database's ability to search through,
--filter, and sort records. Having said that, as you add more joins to a query,
--the database server has to do more work, which translates to slower
--data retrieval times.

--While joins are a necessary part of data retrieval from a normalized database,
--it is important that joins be written correctly, as improper joins can result
--in serious performance degradation and inaccurate query results.
--There are also some cases where a subquery can replace complex joins
--and unions with only minimal performance degradation, if any.