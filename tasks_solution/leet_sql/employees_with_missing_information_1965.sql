select s.employee_id from employees e
right join salaries s on e.employee_id = s.employee_id
where e.name is null
union
select e.employee_id from employees e
left join salaries s on e.employee_id = s.employee_id
where s.employee_id is null
order by 1

-- in this case order by 1 have te difference
-- than order by e.employee_id, s.employee_id
-- because union separate query
-- an db through exception: Table 'e' from one of the SELECTs cannot be used in global ORDER clause