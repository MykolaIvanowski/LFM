-- Write your MySQL query statement below


with second_salary as (
    select salary,
    dense_rank() over (order by salary desc) as rank_
    from Employee
)
select max(salary) as SecondHighestSalary from second_salary
where rank_ = 2




-- pandas
/*
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary'])
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        employee['sal_rank'] = employee['salary'].rank(ascending=False)
        second_highest = employee[employee['sal_rank'] == 2]
        second_highest = second_highest.rename(columns={'salary': 'SecondHighestSalary'})
        return second_highest[['SecondHighestSalary']]

*/
