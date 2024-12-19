
select unique_id, name from employees as e1
left join employeeuni as e2 on e1.id = e2.id

-- if fields have different name no need to use alias, example:
-- select unique_id, name ..., instead - select e1.id e2.name ...