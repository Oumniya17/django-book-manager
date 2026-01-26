from django.test import TestCase
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from bookapp.forms import BookForm


class BookFormTests(TestCase):

    # datos válidos reutilizables
    def valid_data(self):
        return {
            "title": "Libro",
            "pages": 50,
            "rating": 3,
            "status": "Pending",
            "published_date": date.today(),
        }

    # creación correcta
    def test_valid_form(self):
        form = BookForm(data=self.valid_data())
        self.assertTrue(form.is_valid())

    # título demasiado largo
    def test_title_too_long(self):
        data = self.valid_data()
        data["title"] = "a" * 51

        form = BookForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "The title must be less than 50 characters long",
            form.errors["title"]
        )

    # título vacío
    def test_title_empty(self):
        data = self.valid_data()
        data["title"] = ""

        form = BookForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "The title is mandatory",
            form.errors["title"]
        )

    # páginas inválidas
    def test_invalid_pages(self):
        data = self.valid_data()
        data["pages"] = 0

        form = BookForm(data=data)

        self.assertFalse(form.is_valid())

    # rating inválido
    def test_invalid_rating(self):
        data = self.valid_data()
        data["rating"] = 10

        form = BookForm(data=data)

        self.assertFalse(form.is_valid())

    # EXTRA PRO → rating opcional
    def test_rating_optional(self):
        data = self.valid_data()
        data["rating"] = ""

        form = BookForm(data=data)

        self.assertTrue(form.is_valid())

    # read_date antes de published_date
    def test_invalid_read_date(self):
        data = self.valid_data()
        data["published_date"] = date(2024, 1, 10)
        data["read_date"] = date(2024, 1, 1)

        form = BookForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "The read date must be after the published date",
            form.errors["read_date"]
        )

    # con portada (imagen válida real para Pillow)
    def test_with_cover(self):
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00'
            b'\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00'
            b'\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
        )

        file_data = {
            "cover_image": SimpleUploadedFile(
                "cover.gif",
                image_content,
                content_type="image/gif"
            )
        }

        form = BookForm(data=self.valid_data(), files=file_data)

        self.assertTrue(form.is_valid())
