create table payments (
    id serial primary key,
    course_id integer references Course (id) ON DELETE CASCADE,
    amount integer,
    pay_date date,
);

insert into payments (course_id, amount, pay_date)
    values
    ((select get_course_id_by_email((select email from user_student where name like '%Aman%'))), 15000, '2022-8-15'),
    ((select get_course_id_by_email((select email from user_student where name like '%Alena%'))), 55000, '2022-8-5'),
    ((select get_course_id_by_email((select email from user_student where name like '%Phil%'))), 5000, '2022-8-25')








