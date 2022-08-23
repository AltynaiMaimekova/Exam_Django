CREATE FUNCTION get_course_id_by_email (student_email varchar(30)) RETURNS integer AS $body$
    select id from user_course
    where student_id = (select id from user_student where email = student_email)
$body$ LANGUAGE SQL;