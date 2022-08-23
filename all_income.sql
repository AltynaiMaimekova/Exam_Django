select l.name as language, sum(p.amount) as total_amount
from user_course as c join payments as p
on c.id = p.course_id
join user_language as l
on c.language_id = l.id
group by l.id