import uuid

# from django.core.management.base import BaseCommand
from django.core.management import BaseCommand
from faker import Faker

from app.models import Student, Book, Teacher, Subject


class Command(BaseCommand):

    help = 'Add new student'

    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        for _ in range(options['len']):
            book = Book()
            book.title = uuid.uuid4()
            book.save()

            subject, _ = Subject.objects.get_or_create(title='Python')

            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_number(digits=None)
            student.address = faker.address()
            student.birthday = faker.date()
            student.description = faker.text()
            student.email = faker.email()
            student.book = book
            student.subject = subject
            student.save()

            teacher, _ = Teacher.objects.get_or_create(name=faker.name())
            teacher.students.add(student)
            teacher.save()

