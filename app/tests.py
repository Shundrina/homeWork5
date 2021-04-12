import freezegun as freezegun
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# Create your tests here.

from app.models import Subject, Student, Teacher, Book


@freezegun.freeze_time('1900-01-01 00:00:00')
class StudentApiTests(APITestCase):

    def setUp(self) -> None:
        Student.objects.create(name='Name',
                               surname='Surname',
                               sex='male',
                               email='email@email.com')

    def test_get_students(self):
        response = self.client.get(reverse('api_students-list',))
        res = {'count': 1,
               'next': None,
               'previous': None,
               'results': [{'name': 'Name',
                            'surname': 'Surname',
                            'sex': 'male',
                            'email': 'email@email.com',
                            'created_at': '1900-01-01T00:00:00Z',
                            'updated_at': '1900-01-01T00:00:00Z',
                            }]
               }
        self.assertEqual(response.json(), res)

    def test_create_student(self):
        response = self.client.post(reverse('api_students-list'),
                                    data={'name': 'Name',
                                          'surname': 'Lastname',
                                          'sex': 'female',
                                          'email': 'mail@mail.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        students = Student.objects.all()
        self.assertEqual(students.count(), 2)

    def test_update_student(self):
        students = Student.objects.all()
        response = self.client.put(reverse('api_students-detail',
                                           kwargs={'pk': students[0].id}),
                                   data={'name': 'Noname',
                                         'surname': 'Some',
                                         'sex': 'unknown',
                                         'email': 'some@mail.com'})
        res = {'name': 'Noname',
               'surname': 'Some',
               'sex': 'unknown',
               'email': 'some@mail.com',
               'created_at': '1900-01-01T00:00:00Z',
               'updated_at': '1900-01-01T00:00:00Z',
               }
        self.assertEqual(response.json(), res)

    def test_delete_student(self):
        students = Student.objects.all()
        self.client.delete(reverse('api_students-detail',
                                   kwargs={'pk': students[0].id}))
        self.assertEqual(students.count(), 0)


@freezegun.freeze_time('1900-01-01 00:00:00')
class SubjectApiTests(APITestCase):

    def setUp(self) -> None:
        Subject.objects.create(title='title')

    def test_get_subjects(self):
        self.client.get(reverse('api_subjects-list'))
        subjects = Subject.objects.all()
        self.assertEqual(subjects.count(), 1)

    def test_create_subject(self):
        response = self.client.post(reverse('api_subjects-list'),
                                    data={'title': 'subj'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        subjects = Subject.objects.all()
        self.assertEqual(subjects.count(), 2)

    def test_update_subject(self):
        subjects = Subject.objects.all()
        response = self.client.put(reverse('api_subjects-detail',
                                           kwargs={'pk': subjects[0].id}),
                                   data={'title': 'some_subj'})
        res = {'students': [],
               'title': 'some_subj',
               'created_at': '1900-01-01T00:00:00Z',
               'updated_at': '1900-01-01T00:00:00Z',
               }
        self.assertEqual(response.json(), res)

    def test_delete_subject(self):
        subjects = Subject.objects.all()
        self.client.delete(reverse('api_subjects-detail',
                                   kwargs={'pk': subjects[0].id}))
        self.assertEqual(subjects.count(), 0)


@freezegun.freeze_time('1900-01-01 00:00:00')
class TeacherApiTests(APITestCase):
    def setUp(self) -> None:
        Teacher.objects.create(name='Name')

    def test_get_teachers(self):
        self.client.get(reverse('api_teachers-list'))
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 1)

    def test_create_teacher(self):
        response = self.client.post(reverse('api_teachers-list'),
                                    data={'name': 'Somename',
                                          'students': []})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 2)

    def test_update_teacher(self):
        teachers = Teacher.objects.all()
        response = self.client.put(reverse('api_teachers-detail',
                                           kwargs={'pk': teachers[0].id}),
                                   data={'name': 'First_name'})
        res = {
            'students': [],
            'name': 'First_name',
            'created_at': '1900-01-01T00:00:00Z',
            'updated_at': '1900-01-01T00:00:00Z',
        }
        self.assertEqual(response.json(), res)

    def test_delete_teacher(self):
        teachers = Teacher.objects.all()
        self.client.delete(reverse('api_teachers-detail',
                                   kwargs={'pk': teachers[0].id}))
        self.assertEqual(teachers.count(), 0)


@freezegun.freeze_time('1900-01-01 00:00:00')
class BookApiTests(APITestCase):

    def setUp(self) -> None:
        Book.objects.create(title='title')

    def test_get_books(self):
        self.client.get(reverse('api_books-list'))
        books = Book.objects.all()
        self.assertEqual(books.count(), 1)

    def test_create_book(self):
        response = self.client.post(reverse('api_books-list'),
                                    data={'title': 'boo'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        books = Book.objects.all()
        self.assertEqual(books.count(), 2)

    def test_update_book(self):
        books = Book.objects.all()
        response = self.client.put(reverse('api_books-detail',
                                           kwargs={'pk': books[0].id}),
                                   data={'title': 'some_boo'})
        res = {
            'title': 'some_boo',
            'created_at': '1900-01-01T00:00:00Z',
            'updated_at': '1900-01-01T00:00:00Z',
        }
        self.assertEqual(response.json(), res)

    def test_delete_book(self):
        books = Book.objects.all()
        self.client.delete(reverse('api_books-detail',
                                   kwargs={'pk': books[0].id}))
        self.assertEqual(books.count(), 0)
