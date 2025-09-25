from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="admin", password="Fr@nc01$1er")
        
        # Login the client
        self.client.login(username="admin", password="Fr@nc01$1er")

        # Create an Author instance
        self.author1 = Author.objects.create(name="Alice")
        self.author2 = Author.objects.create(name="Bob")

        # Create books with author instances (NOT strings)
        self.book1 = Book.objects.create(
            title="Django Basics",
            author=self.author1,
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Advanced Django",
            author=self.author2,
            publication_year=2021
        )

        # API endpoints
        self.book_list_url = reverse("book-list")   # /api/books/
        self.book_detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})  # /api/books/<id>/

    # --- CRUD TESTS ---
    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {"title": "REST APIs", "author": "Charlie", "publication_year": 2022}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Basics")

    def test_update_book(self):
        data = {"title": "Django Basics Updated", "author": "Alice", "publication_year": 2020}
        response = self.client.put(self.book_detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Django Basics Updated")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- FILTERING, SEARCHING, ORDERING ---
    def test_filter_books_by_year(self):
        response = self.client.get(self.book_list_url, {"publication_year": 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Basics")

    def test_search_books_by_title(self):
        response = self.client.get(self.book_list_url, {"search": "Advanced"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced Django")

    def test_order_books_by_year_desc(self):
        response = self.client.get(self.book_list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Advanced Django")  # 2021 comes first

    # --- AUTHENTICATION TESTS ---
    def test_cannot_access_without_authentication(self):
        self.client.credentials()  # remove token
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
