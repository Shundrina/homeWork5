from django.db import models

# Create your models here.
from django.forms import ModelMultipleChoiceField


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    birthday = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    social_url = models.CharField(null=True, max_length=200)
    normalized_name = models.CharField(null=True, max_length=200)
    book = models.OneToOneField('app.Book', on_delete=models.CASCADE,
                                null=True, related_name='student',
                                related_query_name='student')
    subject = models.ForeignKey(to='app.Subject', on_delete=models.SET_NULL,
                                null=True, related_name='students')


class Subject(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(
        to='app.Student',
        related_name='teachers',
        related_query_name='teachers',
    )

