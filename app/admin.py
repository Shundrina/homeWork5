

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.utils.html import format_html

from app.models import Student


class StudentAdmin(ModelAdmin):
    model = Student
    list_display = ('social', 'email', 'birthday')

    def social(self, Student):
        social_url = Student.social_url
        name = Student.name + ' ' + Student.surname
        if social_url:
            return format_html("<a href='{url}'>{name}</a>", url=social_url, name=name)
        else:
            return Student.name + " " + Student.surname


admin.site.register(Student, StudentAdmin)
