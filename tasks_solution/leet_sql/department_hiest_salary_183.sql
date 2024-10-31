-- Write your MySQL query statement below


select department.name as Department, employee.name as Employee, employee.Salary
from employee
join department on employee.departmentid = department.id
where (department.id, employee.salary) in (
    select departmentid, max(salary)
    from employee
    group by departmentid
    )


