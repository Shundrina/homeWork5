from app.models import Student, Subject, Teacher, Book
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'sex', 'email']


class SubjectSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['title', 'students']


class TeacherSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ['name', 'students']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
