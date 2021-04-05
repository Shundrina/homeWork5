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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app.views import StudentView, CreateStudentView, \
    UpdateStudentView, BookView, SubjectView, TeacherView, \
    UpdateSubjectView, UpdateTeacherView, UpdateBookView, \
    CSVView, JsonView, SendMailView, DeleteStudentView, \
    RegisterView, LoginView, LogOutView, ActivateView, \
    StudentViewSet, TeacherViewSet, SubjectViewSet, BookViewSet

# from app.views import show_all_students as show, new_student_form,

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='api_students')
router.register(r'teachers', TeacherViewSet, basename='api_teachers')
router.register(r'subjects', SubjectViewSet, basename='api_subjects')
router.register(r'books', BookViewSet, basename='api_books')

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    path('api/', include(router.urls)),
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
    path('activate/<uid>/<token>', ActivateView.as_view(),
         name='activate_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
