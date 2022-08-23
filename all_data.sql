select c.name as course, c.date_started, s.name as student, m.name as mentor, l.name as language
from user_course as c join user_student as s
on c.student_id = s.id
join user_mentor as m
on c.mentor_id = m.id
join user_language as l
on c.language_id = l.id

select l.name as language, sum(p.amount) as total amount
from user_language as l join payments as p
on l.id = p.language_id
group by l.id