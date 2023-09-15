-- Data Definition Language   DDL

 --1 to 1
CREATE TABLE dbo.table_a(
    id_a int PRIMARY KEY,
    column_1 varchar(25),
);

CREATE TABLE dbo.table_b(
    id_b int PRIMARY KEY,
    column_1 varchar(15),
    fk_id INT UNIQUE FOREIGN KEY REFERENCES table_a(id_a)
);

-- 1 to many

CREATE TABLE table_a
(
id_a INT PRIMARY KEY,
column_1 VARCHAR(100)
);

CREATE TABLE table_b
(
id_b INT PRIMARY KEY,
column_1 VARCHAR(100),
fk_id INT FOREIGN KEY REFERENCES table_a(id_a)
);


-- many to many

CREATE TABLE table_a(
id_a INT(10) PRIMARY KEY,
column_1 VARCHAR(100),
);

CREATE TABLE table_b(
id_b INT(10) PRIMARY KEY,
column_1 VARCHAR(100),
);
CREATE TABLE table_a_b(
id_a INT(15) NOT NULL,
id_b INT(14) NOT NULL,
FOREIGN KEY (id_a) REFERENCES Student(id_b),
FOREIGN KEY (id_b) REFERENCES Class(id_a),
UNIQUE (id_a, id_b)
);

CREATE DATABASE `test`

-- add column
ALTER TABLE table_name
ADD column_name datatype;

-- rename
ALTER TABLE table_name
RENAME COLUMN old_name to new_name;

-- truncate vs delete
-- Removes all rows from a table or specified partitions of a table,
-- without logging the individual row deletions.
-- TRUNCATE TABLE is similar to the DELETE statement with no WHERE clause;
-- however, TRUNCATE TABLE is faster and uses fewer system and transaction log resources.

-- truncate
TRUNCATE TABLE table_name;

-- truncate vs delete vs drop vs insert

-- how delete works

-- If you don’t want to remove table structure or you’re only deleting specific rows,
-- use the DELETE command. It can remove one, some, or all rows in a table.
-- DELETE returns the number of rows removed from the table.

--However, DELETE uses a row lock during execution and can be rolled back.
--Every deleted row is locked, so it will require a lot of locks if you’re
--working in a large table.

--DELETE also keeps the auto-increment ID in the table.
--If you remove the last record in the table with ID=20 and then add a new record,
--this record will have ID=21 – even though the record immediately before it will be ID=19.

--DELETE can be executed by triggers.
--A trigger can be called before, after, or instead of the DELETE operation.
--It can be executed for any row change or when all rows are removed.
--Removing rows in another table can also trigger DELETE.


-- how truncate works

--TRUNCATE is faster than DELETE, as it doesn't scan every record before removing it.
--TRUNCATE TABLE locks the whole table to remove data from a table;
--thus, this command also uses less transaction space than DELETE.

--Unlike DELETE, TRUNCATE does not return the number of rows deleted from the table.
--It also resets the table auto-increment value to the starting value (usually 1).
--If you add a record after truncating the table, it will have ID=1. Note:
--In PostgreSQL, you can choose to restart or continue the auto-increment value.
--Oracle uses a sequence to increment values, which is not reset by TRUNCATE.

--Of course, you need permission to use TRUNCATE TABLE.
--In PostgreSQL, you need the privilege TRUNCATE;
--in SQL Server, the minimum permission is ALTER table;
--in MySQL, you need the DROP privilege. Finally,
--Oracle requires the DROP ANY TABLE system privilege to use this command.


-- how to drop works

--The DROP TABLE operation removes the table definition and data as well as the indexes,
--constraints, and triggers related to the table.

--This command frees the memory space.

--No triggers are fired when executing DROP TABLE.

--This operation cannot be rolled back in MySQL,
--but it can in Oracle, SQL Server, and PostgreSQL.

--In SQL Server, DROP TABLE requires
--ALTER permission in the schemato which the table belongs;
--MySQL requires the DROP privilege;
--Oracle the requires the DROP ANY TABLE privilege.
--In PostgreSQL, users can drop their own tables.