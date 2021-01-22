from django.shortcuts import render, redirect
# Create your views here.
from app.forms import StudentForm
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


def new_student_form(request):
    if request.method == 'GET':
        student_form = StudentForm()
        context = {
            'student_form': student_form,
        }
        return render(request, 'student_form.html', context=context)

    elif request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()

        return redirect('/students/create')
