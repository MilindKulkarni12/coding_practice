# Write your MySQL query statement below

with merged as (
    select s.*, sb.*
    from Students s, Subjects sb 
)
select m.student_id, m.student_name, m.subject_name, count(e.subject_name) as attended_exams
from merged m
left join examinations e
    on e.student_id = m.student_id and e.subject_name = m.subject_name
group by m.student_id, m.student_name, m.subject_name
order by m.student_id, m.subject_name

-- select s.student_id, s.student_name, e.subject_name, count(0) as attended_exams
-- from Students as s
-- left join Examinations as e on s.student_id = e.student_id
-- group by s.student_id, s.student_name, e.subject_name
-- order by s.student_id, s.student_name