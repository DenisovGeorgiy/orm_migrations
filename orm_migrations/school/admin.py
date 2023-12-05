from django.contrib import admin

from .models import Student, Teacher, TeacherStudent


class TeacherStudentInline(admin.TabularInline):
    model = TeacherStudent
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInline]
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
