select e1.employee_id,
    e1.name,
    count(e2.reports_to) as reports_count,
    round(avg(e2.age)) as average_age
from employees e1
join employees e2 on e1.employee_id = e2.reports_to
group by e1.employee_id, e1.name
order by 1


--first two column in select statement takes value from left table
-- next two column in select statement takes value from right table
-- trik is that value not in the same rows example

id | name | reports_to
1  | bob  | nik
2  | nik  | lise
3  | lise | null

--than query combines mixed rows (how much reports to nik)
id |name| count(reports_to)
1  |nik | 1

