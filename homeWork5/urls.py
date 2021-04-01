"""homeWork5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import StudentView, CreateStudentView, \
    UpdateStudentView, BookView, SubjectView, TeacherView, \
    UpdateSubjectView, UpdateTeacherView, UpdateBookView, \
    CSVView, JsonView, SendMailView, DeleteStudentView, \
    RegisterView, LoginView, LogOutView, ActivateView

# from app.views import show_all_students as show, new_student_form,

urlpatterns = [
    path('admin/', admin.site.urls),

    path('students/', StudentView.as_view(), name='all_students'),
    path('students/create', CreateStudentView.as_view(),
         name='new_student'),
    path('students/update/<pk>/', UpdateStudentView.as_view(),
         name='update_student'),
    path('students/delete/<pk>/', DeleteStudentView.as_view(),
         name='delete_student'),

    path('subjects/', SubjectView.as_view(), name='subjects'),
    path('subjects/update/<id>', UpdateSubjectView.as_view(),
         name='subject_update'),

    path('books/', BookView.as_view(), name='books'),
    path('books/update/<id>', UpdateBookView.as_view(),
         name='book_update'),

    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('teachers/update/<id>', UpdateTeacherView.as_view(),
         name='teacher_update'),

    path('students/csv', CSVView.as_view(), name='csv_view'),
    path('students/json', JsonView.as_view(), name='json_view'),
    path('send_email/', SendMailView.as_view(), name='send_email'),

    path('registration/', RegisterView.as_view(), name='register_view'),
    path('logout/', LogOutView.as_view(), name='logout_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('activate/<uid>/<token>', ActivateView.as_view(), name='activate_view'),
]
