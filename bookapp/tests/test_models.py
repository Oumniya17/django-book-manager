from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from bookapp.models import Book, Author


class BookModelTests(TestCase):

    def create_book(self):
        return Book(
            title="Libro",
            pages=100,
            rating=3,
            status="Pending",
            published_date=date.today()
        )

    def test_create_book_ok(self):
        book = self.create_book()
        book.full_clean()

    def test_invalid_pages(self):
        book = self.create_book()
        book.pages = 0
        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_invalid_rating(self):
        book = self.create_book()
        book.rating = 10
        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_invalid_read_date(self):
        book = self.create_book()
        book.read_date = date(2000, 1, 1)
        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_with_author(self):
        book = self.create_book()
        book.save()
        author = Author.objects.create(name="Ana", last_name="Lopez")
        book.authors.add(author)
        self.assertEqual(book.authors.count(), 1)

    def test_with_cover(self):
        cover = SimpleUploadedFile("cover.jpg", b"img", content_type="image/jpeg")
        book = self.create_book()
        book.cover_image = cover
        book.save()
        self.assertTrue(book.cover_image)
        
def test_rating_optional(self):
    book = self.create_book()
    book.rating = None
    book.full_clean()  # no debe fallar


def test_string_representation(self):
    book = self.create_book()
    book.full_clean()
    self.assertEqual(str(book), "Libro")
