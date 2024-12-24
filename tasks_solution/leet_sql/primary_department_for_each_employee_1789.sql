select employee_id, department_id
from employee
where primary_flag ='Y'
union
select employee_id, department_id
from employee
group by 1
having count(*)=1


--first part (before union )
-- select employee with flag 'Y'
-- second part (after union)
-- select employee with only one department

-- other solution
