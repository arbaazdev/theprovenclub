
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Member

class BookAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.member = Member.objects.create(name="user", user=user)
        self.book = Book.objects.create(name="book 1", number_of_copies=22)

    def test_book_creation(self):
        url = '/api/books/'
        data = {'name': 'book 2', 'number_of_copies': 2}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_checkout(self):
        url = '/api/books/1/checkout/'
        response = self.client.get(url)
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        number_of_copies = self.book.number_of_copies - 1
        self.assertEqual(data["number_of_copies"], number_of_copies)
