from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View
# Create your views here.
from app.forms import StudentForm
from app.models import Student


# def show_all_students(request):
#
#     students = Student.objects.all()
#
#     return render(
#         request=request,
#         template_name='index.html',
#         context={
#             'students': students,
#         }
#     )


# def new_student_form(request):
#     if request.method == 'GET':
#         student_form = StudentForm()
#         context = {
#             'student_form': student_form,
#         }
#         return render(request, 'student_form.html', context=context)
#
#     elif request.method == 'POST':
#         student_form = StudentForm(request.POST)
#         if student_form.is_valid():
#             student_form.save()
#
#         return redirect(reverse('new_student'))


class StudentsView(View):

    def get(self, request):
        students = Student.objects.all()

        return render(
            request=request,
            template_name='index.html',
            context={
                'students': students,
            }
        )


class CreateNewStudentView(View):

    def get(self, request):
        student_form = StudentForm()
        context = {
            'student_form': student_form,
        }
        return render(request, 'student_form.html', context=context)

    def post(self, request):
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()

        return redirect(reverse('all_students'))


class UpdateStudentView(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        student_form = StudentForm(instance=student)
        context = {
            'student_form': student_form,
            'student': student,
        }
        return render(request, 'student_update.html', context=context)

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()

        return redirect(reverse('all_students'))
