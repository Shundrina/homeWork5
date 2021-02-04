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
from app.views import StudentsView, CreateNewStudentView, UpdateStudentView

# from app.views import show_all_students as show, new_student_form,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentsView.as_view(), name='all_students'),
    path('students/create', CreateNewStudentView.as_view(), name='new_student'),
    path('students/update/<id>/', UpdateStudentView.as_view(), name='update_student'),
]
