select e2.employee_id
from employees e1
right join employees e2 on e1.employee_id = e2.manager_id
where e1.employee_id is null and e2.salary <30000 and e2.manager_id is not null
order by 1