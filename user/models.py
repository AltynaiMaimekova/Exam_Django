from django.db import models
from datetime import datetime, timedelta


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, blank=True, unique=True, null=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if len(str(self.phone_number)) <= 10:
            self.phone_number = '+996' + str(self.phone_number)[1:]
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=30)
    month_to_learn = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).upper()
        super().save(*args, **kwargs)


class Student(AbstractPerson):

    OS_CHOICES = [
        ('windows', 'Windows'),
        ('macos', 'MacOS'),
        ('linux', 'Linux'),
    ]

    work_study_place = models.CharField(max_length=50, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=20, choices=OS_CHOICES)

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True, blank=True)
    experience = models.DateField()
    students = models.ManyToManyField(Student, through='Course')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_end_date(self):
    #     end_date = self.date_started + timedelta(days=30*self.language.month_to_learn)







