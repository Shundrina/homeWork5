from django.db import models

# Create your models here.


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
                                null=True)
    subject = models.ForeignKey('app.Subject', on_delete=models.SET_NULL,
                                null=True)


class Subject(models.Model):
    title = models.CharField(max_length=200)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    students = models.ManyToManyField('app.Student')
