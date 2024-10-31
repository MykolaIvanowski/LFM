-- Write your MySQL query statement below
select Email from person
group by email having count(email) > 1


-- select Email, count(email) from person
-- group by email having count(email) > 1