from django.contrib import admin

from cource.models import Classes, Teacher


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass