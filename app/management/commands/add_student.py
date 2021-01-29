from django.core.management import BaseCommand
from faker import Faker
import random

from app.models import Student


class Command(BaseCommand):

    help = 'Add new student'

    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        sex = ("F", "M")
        for _ in range(options['len']):
            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_number(digits=None)
            student.sex = random.choice(sex)
            student.address = faker.address()
            student.birthday = faker.date()
            student.description = faker.text()
            student.email = faker.email()
            student.save()
