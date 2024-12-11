--  WITH CTE (Common Table Expressions)

--The SQL WITH clause allows you to give a sub-query block
--a name (a process also called sub-query refactoring),
--which can be referenced in several places within the main SQL query.


--The clause is used for defining a temporary relation such
--that the output of this temporary relation is available
--and is used by the query that is associated with the WITH clause.

--Queries that have an associated WITH clause can also
--be written using nested sub-queries but doing so add more
--complexity to read/debug the SQL query.

--WITH clause is not supported by all database system.

--The name assigned to the sub-query is treated as though
--it was an inline view or table


[ WITH <common_table_expression> [ ,...n ] ]

WITH temporaryTable (averageValue) as
    (SELECT avg(Attr1)
    FROM Table)
    SELECT Attr1
    FROM Table, temporaryTable
    WHERE Table.Attr1 > temporaryTable.averageValue;



--Cross Join:
--
--A CROSS JOIN in SQL is a type of join that returns the Cartesian product of two tables.
--This means that every row from the first table is combined with every row
--from the second table, resulting in all possible combinations of rows between the two tables.
--
--SELECT columns
--FROM table1
--CROSS JOIN table2;
--
--
--Characteristics of CROSS JOIN:
--All Combinations: It produces a result set that includes every possible combination of rows from both tables.
--
--Cartesian Product: This is the mathematical term for the set of all ordered pairs
--obtained by combining each row of one table with each row of the other.
--
--No Join Condition: Unlike other types of joins (INNER JOIN, LEFT JOIN, etc.),
--CROSS JOIN does not require a condition to specify how rows should be combined.

--When to Use CROSS JOIN:
--Generating Combinations: Useful when you need to generate combinations of rows,
--such as creating a schedule where every student is paired with every possible subject.
--
--Testing and Debugging: Sometimes used in testing scenarios to ensure that
--your query logic can handle all possible combinations of data.