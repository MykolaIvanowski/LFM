
select st.student_id, st.student_name, s.subject_name, count(e.subject_name) as attended_exams
from students as st
cross join subjects as s
left join examinations as e
on st.student_id = e.student_id and s.subject_name = e.subject_name
group by 1,2,3
order by 1,3


--Cross Join:
--
--The cross join between students and subjects generates a combination of each student
--with each subject, creating all possible student-subject pairs.
--This means every student is paired with every subject, whether
--they have attended an exam for that subject or not.
--
--Count Exams Attended: The query then performs a left join with the examinations
--table to find out how many times each student has attended an exam for each subject.
--The count() function is used to count the number of exams attended.