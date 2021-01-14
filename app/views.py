from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import Student


def show_all_students(request):

    students = Student.objects.all()

    return render(
        request=request,
        template_name='index.html',
        context={
            'students': students,
        }
    )
