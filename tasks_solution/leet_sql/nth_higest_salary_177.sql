--  solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      -- Write your MySQL query statement below.
SELECT distinct salary as nth_salary
from (
    select salary, DENSE_RANK() OVER (order by salary desc) AS rank_
    from Employee
    ) as ranked_salary
where rank_ = N
  );
END


-- from some repo github
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
  RETURN (
      -- Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER by Salary DESC LIMIT M, 1
  );
END

-- also solution

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      -- Write your MySQL query statement below.
with second_salary as (
    select salary,
    dense_rank() over (order by salary desc) as rank_
    from Employee
)
select max(salary) as SecondHighestSalary from second_salary
where rank_ = N

  );
END

