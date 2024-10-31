-- Write your MySQL query statement below
select  c.name as customers from customers c
left join orders o on c.id = o.customerId
where o.customerid is null

---other solutions

    SELECT *
    FROM TableA a
    WHERE NOT EXISTS (
        SELECT 1
        FROM TableB b
        WHERE a.id = b.id
    );

        SELECT *
    FROM TableA
    WHERE id NOT IN (
        SELECT id
        FROM TableB
    );

    SELECT id
    FROM TableA
    EXCEPT
    SELECT id
    FROM TableB;