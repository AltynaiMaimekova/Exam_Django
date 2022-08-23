from django.contrib import admin

from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):

    @admin.display(description='level')
    def experience_level(self, obj):
        if obj.experience > 3:
            level = 'middle'
        else:
            level = 'strong junior'
        return level

    @admin.display(description='student_list')
    def student_list(self, obj):
        student_list = []
        for student in obj.students.all():
            info = {'name': student.name, 'job': student.work_study_place, 'phone': student.phone_number}
            student_list.append(info)
        return student_list

    list_display = ('name', 'email', 'phone_number', 'main_work',
                    'experience', 'experience_level', 'student_list')

    search_fields = ['name',]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    @admin.display(description='student name')
    def student_name(self, obj):
        return obj.student.name

    @admin.display(description='mentor name')
    def mentor_name(self, obj):
        return obj.mentor.name

    list_display = ('name', 'date_started', 'language', 'student_name', 'mentor_name')
    list_filter = ('language', 'mentor')
    search_fields = ['student__name', 'mentor__name']

