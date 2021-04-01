import csv

from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
# Create your views here.
from app.emails import send_email
from app.forms import SubjectForm, BookForm, TeacherForm, UserRegisterForm
from app.models import Student, Subject, Book, Teacher


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


# class StudentsView(View):
#
#     def get(self, request):
#         students = Student.objects.all()
#
#         return render(
#             request=request,
#             template_name='index.html',
#             context={
#                 'students': students,
#             }
#         )
#
#     def post(self, request):
#
#         if request.POST.get('teacher_search'):
#             teachers_name = request.POST['teacher_search']
#             students = Student.objects.filter(teachers__name=teachers_name)
#             context = {
#                 'students': students,
#             }
#             return render(request, 'index.html', context=context)
#
#         if request.POST.get('subject_search'):
#             subject_title = request.POST['subject_search']
#             students = Student.objects.filter(subject__title=subject_title)
#             context = {
#                 'students': students,
#             }
#             return render(request, 'index.html', context=context)
#
#         if request.POST.get('book_search'):
#             book_title = request.POST['book_search']
#             students = Student.objects.filter(book__title=book_title)
#             context = {
#                 'students': students,
#             }
#             return render(request, 'index.html', context=context)


# @method_decorator(cache_page(settings.CACHE_TTL), name='dispatch')
class StudentView(ListView):

    model = Student
    template_name = 'index.html'


# class CreateNewStudentView(View):
#
#     def get(self, request):
#         student_form = StudentForm()
#         context = {
#             'student_form': student_form,
#         }
#         return render(request, 'student_form.html', context=context)
#
#     def post(self, request):
#         student_form = StudentForm(request.POST)
#         if student_form.is_valid():
#             student_form.save()
#
#         return redirect(reverse('all_students'))


class CreateStudentView(CreateView):

    model = Student
    fields = [
            'name',
            'surname',
            'age',
            'sex',
            'address',
            'description',
            'birthday',
            'email',
            'social_url',
            'subject',
        ]
    template_name = 'student_form.html'
    success_url = reverse_lazy('all_students')


# class UpdateStudentView(View):
#     def get(self, request, id):
#         student = get_object_or_404(Student, id=id)
#         student_form = StudentForm(instance=student)
#         context = {
#             'student_form': student_form,
#             'student': student,
#         }
#         return render(request, 'student_update.html', context=context)
#
#     def post(self, request, id):
#         student = get_object_or_404(Student, id=id)
#         student_form = StudentForm(request.POST, instance=student)
#         if student_form.is_valid():
#             student_form.save()
#
#         return redirect(reverse('all_students'))


class UpdateStudentView(UpdateView):
    model = Student
    fields = [
        'name',
        'surname',
        'age',
        'sex',
        'address',
        'description',
        'birthday',
        'email',
        'social_url',
        'subject',
    ]
    template_name = 'student_form.html'
    success_url = reverse_lazy('all_students')


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('all_students')


class SubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()

        return render(
            request=request,
            template_name='subjects.html',
            context={
                'subjects': subjects,
            }
        )


class UpdateSubjectView(View):
    def get(self, request, id):
        subject = get_object_or_404(Subject, id=id)
        subject_form = SubjectForm(instance=subject)
        subject_students = Student.objects.filter(subject__title=subject.title)
        no_subject_students = Student.objects.filter(subject=None)
        context = {
            'subject_form': subject_form,
            'subject': subject,
            'subject_students': subject_students,
            'no_subject_students': no_subject_students,
        }
        return render(request, 'subject_update.html', context=context)

    def post(self, request, id):
        subject = get_object_or_404(Subject, id=id)
        subject_form = SubjectForm(request.POST, instance=subject)

        if request.POST.get('delete_student'):
            student_id = request.POST['delete_student']
            student = Student.objects.get(id=student_id)
            subject.students.remove(student)
            subject_form = SubjectForm(instance=subject)
            subject_students = Student.objects.filter(
                subject__title=subject.title)
            no_subject_students = Student.objects.filter(subject=None)
            context = {
                'subject_form': subject_form,
                'subject': subject,
                'subject_students': subject_students,
                'no_subject_students': no_subject_students,
            }
            return render(request, 'subject_update.html', context=context)

        if request.POST.get('add_student'):
            student_id = request.POST['add_student']
            student = Student.objects.get(id=student_id)
            subject.students.add(student)
            subject_form = SubjectForm(instance=subject)
            subject_students = Student.objects.filter(
                subject__title=subject.title)
            no_subject_students = Student.objects.filter(subject=None)
            context = {
                'subject_form': subject_form,
                'subject': subject,
                'subject_students': subject_students,
                'no_subject_students': no_subject_students,
            }
            return render(request, 'subject_update.html', context=context)

        if subject_form.is_valid():
            subject_form.save()

        return redirect(reverse('subjects'))


class BookView(View):
    def get(self, request):
        books = Book.objects.all()

        return render(
            request=request,
            template_name='books.html',
            context={
                'books': books,
            }
        )


class UpdateBookView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        book_form = BookForm(instance=book)
        book_students = Student.objects.filter(book__title=book.title)
        context = {
            'book_form': book_form,
            'book': book,
            'book_students': book_students,
        }
        return render(request, 'book_update.html', context=context)

    def post(self, request, id):
        if request.POST.get('delete_book'):
            student_id = request.POST['delete_book']
            student = Student.objects.get(id=student_id)
            student.book.delete()

            return redirect(reverse('books'))


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()

        return render(
            request=request,
            template_name='teachers.html',
            context={
                'teachers': teachers,
            }
        )


class UpdateTeacherView(View):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher_form = TeacherForm(instance=teacher)
        teacher_students = Student.objects.filter(
            teachers__name=teacher.name)
        no_teacher_students = Student.objects.exclude(
            teachers__name=teacher.name)
        context = {
            'teacher_form': teacher_form,
            'teacher': teacher,
            'teacher_students': teacher_students,
            'no_teacher_students': no_teacher_students,
        }
        return render(request, 'teacher_update.html', context=context)

    def post(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher_form = TeacherForm(request.POST, instance=teacher)

        if request.POST.get('delete_student'):
            student_id = request.POST['delete_student']
            student = Student.objects.get(id=student_id)
            teacher.students.remove(student)
            teacher_form = TeacherForm(instance=teacher)
            teacher_students = Student.objects.filter(
                teachers__name=teacher.name)
            no_teacher_students = Student.objects.exclude(
                teachers__name=teacher.name)
            context = {
                'teacher_form': teacher_form,
                'teacher': teacher,
                'teacher_students': teacher_students,
                'no_teacher_students': no_teacher_students,
            }
            return render(request, 'teacher_update.html', context=context)

        if request.POST.get('add_student'):
            student_id = request.POST['add_student']
            student = Student.objects.get(id=student_id)
            teacher.students.add(student)
            teacher_form = TeacherForm(instance=teacher)
            teacher_students = Student.objects.filter(
                teachers__name=teacher.name)
            no_teacher_students = Student.objects.exclude(
                teachers__name=teacher.name)
            context = {
                'teacher_form': teacher_form,
                'teacher': teacher,
                'teacher_students': teacher_students,
                'no_teacher_students': no_teacher_students,
            }
            return render(request, 'teacher_update.html', context=context)

        if teacher_form.is_valid():
            teacher_form.save()

        return redirect(reverse('teachers'))


class CSVView(View):

    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = "attachment; " \
                                          "filename=students_data.csv"
        writer_for_response = csv.writer(response)
        writer_for_response.writerow(["Name",
                                      "Surname",
                                      "Birthday",
                                      "Book",
                                      "Subject"])
        students = Student.objects.all()
        for student in students:
            writer_for_response.writerow([
                student.name,
                student.surname,
                student.birthday,
                student.book,
                student.subject if student.subject else None,
            ])
        return response


class JsonView(View):

    def get(self, request):
        students = Student.objects.all()
        return JsonResponse({
            "students": list(students.values(
                "name",
                "surname",
                "birthday",
                "email",
                "book__title",
                "subject__title",
            ))
        })


class SendMailView(View):

    def get(self, request):

        send_email(recipient_list=['email@gmail.com', ])

        return HttpResponse('email sent')


class RegisterView(View):

    def get(self, request):
        register_form = UserRegisterForm()

        return render(request, 'registration.html', context={
            'form': register_form,
        })

    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.is_active = False
            user.set_password(request.POST['password1'])
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))

            activate_url = "{}/{}/{}".format(
                "http://localhost:8000/activate",
                uid,
                default_token_generator.make_token(user=user)
            )

            send_email(
                recipient_list=[user.email],
                activate_url=activate_url
            )

            return HttpResponse("Check your email list to activate account!")
        return HttpResponse("Wrong Data")


class ActivateView(View):

    def get(self, request, uid, token):
        user_id = force_bytes(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=user_id)

        if not user.is_active and default_token_generator.check_token(user,
                                                                      token):
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponse('token checked')

        return HttpResponse('Your account activated')


class LoginView(View):

    def get(self, request):
        auth_form = AuthenticationForm()

        return render(request, 'login.html', context={
            'form': auth_form,
        })

    def post(self, request):
        auth_form = AuthenticationForm(request.POST)
        print(auth_form)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('all_students'))
        else:
            return HttpResponse('No')


class LogOutView(View):

    def get(self, request):
        logout(request)
        return render(request=request, template_name='logout.html')
