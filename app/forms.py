from django.forms import ModelForm
from app.models import Student


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'surname',
            'age', 'sex',
            'address',
            'description',
            'birthday',
            'email'
        ]
