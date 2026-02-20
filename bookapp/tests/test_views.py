from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from datetime import date
from bookapp.models import Book


class BookViewTests(TestCase):

    def setUp(self):
        # Crear libro de prueba
        self.book = Book.objects.create(
            title="Libro Test",
            pages=100,
            rating=3,
            status="Pending",
            published_date=date.today()
        )

        # Crear grupo Admin con permisos sobre Book
        self.admin_group = Group.objects.create(name="Admin")
        permissions = Permission.objects.filter(content_type__model="book")
        self.admin_group.permissions.set(permissions)

        # Crear usuario admin
        self.admin_user = User.objects.create_user(
            username="admin",
            password="1234"
        )
        self.admin_user.groups.add(self.admin_group)

        # Crear usuario normal (sin permisos)
        self.normal_user = User.objects.create_user(
            username="user",
            password="1234"
        )

    # --------------------
    # LIST (accesible para todos)
    # --------------------

    def test_list_admin(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get("/bookapp/list")
        self.assertEqual(response.status_code, 200)

    def test_list_user(self):
        self.client.login(username="user", password="1234")
        response = self.client.get("/bookapp/list")
        self.assertEqual(response.status_code, 200)

    # --------------------
    # DETAIL (requiere login)
    # --------------------

    def test_detail_admin(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(f"/bookapp/{self.book.id}/detail")
        self.assertEqual(response.status_code, 200)

    def test_detail_user(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(f"/bookapp/{self.book.id}/detail")
        self.assertEqual(response.status_code, 200)

    def test_detail_requires_login(self):
        response = self.client.get(f"/bookapp/{self.book.id}/detail")
        self.assertEqual(response.status_code, 302)

    # --------------------
    # FORM (requiere permiso add)
    # --------------------

    def test_form_admin(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get("/bookapp/form")
        self.assertEqual(response.status_code, 200)

    def test_form_user_no_permission(self):
        self.client.login(username="user", password="1234")
        response = self.client.get("/bookapp/form")
        self.assertEqual(response.status_code, 302)

    # --------------------
    # EDIT (requiere permiso change)
    # --------------------

    def test_edit_admin(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(f"/bookapp/{self.book.id}/edit")
        self.assertEqual(response.status_code, 200)

    def test_edit_user_no_permission(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(f"/bookapp/{self.book.id}/edit")
        self.assertEqual(response.status_code, 302)

    # --------------------
    # DELETE (requiere permiso delete)
    # --------------------

    def test_delete_admin(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(f"/bookapp/{self.book.id}/delete")
        self.assertEqual(response.status_code, 200)

    def test_delete_user_no_permission(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(f"/bookapp/{self.book.id}/delete")
        self.assertEqual(response.status_code, 302)