from django.core.paginator import Paginator

from app.models import Student, Subject, Teacher, Book
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'sex', 'email']


class SubjectSerializer(serializers.ModelSerializer):

    students = serializers.SerializerMethodField('paginated_students')

    def paginated_students(self, obj):
        students = Student.objects.get_queryset().order_by('name')
        pagination = Paginator(students, per_page=10)
        paginated_students = pagination.page(1)

        return StudentSerializer(instance=paginated_students, many=True).data

    class Meta:
        model = Subject
        fields = ['title', 'students']


class TeacherSerializer(serializers.ModelSerializer):

    students = serializers.SerializerMethodField('paginated_students')

    def paginated_students(self, obj):
        students = Student.objects.get_queryset().order_by('name')
        pagination = Paginator(students, per_page=10)
        paginated_students = pagination.page(1)

        return StudentSerializer(instance=paginated_students, many=True).data

    class Meta:
        model = Teacher
        fields = ['name', 'students']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
