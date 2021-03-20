from django.forms import ModelForm
from app.models import Student, Subject, Book, Teacher


class StudentForm(ModelForm):
    class Meta:
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
            'book',
            'subject',
        ]


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = [
            'title',
        ]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
        ]


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'name',
        ]
