import datetime
from user.models import Student, Mentor, Language, Course

l1 = Language.objects.create(name='Python', month_to_learn=6)
l2 = Language.objects.create(name='Java Script', month_to_learn=6)
l3 = Language.objects.create(name='UX-UI', month_to_learn=2)


s1 = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
                            work_study_place='School №13', has_own_notebook=True, preferred_os='windows')

s2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
                            work_study_place='TV', has_own_notebook=True, preferred_os='macos')

s3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312',
                            work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')

m1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
                           experience=1)
m2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
                           main_work='University of Fort Collins', experience=12)

c1 = Course.objects.create(name='Python-21', language=l1, date_started='2022-8-1', mentor=m2, student=s1)
c2 = Course.objects.create(name='Python-21', language=l1, date_started='2022-8-1', mentor=m2, student=s2)
c2 = Course.objects.create(name='UXUI design-43', language=l3, date_started='2022-8-22', mentor=m1, student=s3)
