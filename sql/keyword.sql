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