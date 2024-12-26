select teacher_id,
count(distinct subject_id) as cnt
from teacher
group by 1

--question
--Write a solution to calculate the number of unique subjects
--each teacher teaches in the university.