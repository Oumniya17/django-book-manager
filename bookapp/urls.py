from django.urls import path
from . import views

app_name = "bookapp"

urlpatterns = [
    path("list", views.book_list, name="book_list"),
    path("form", views.book_form, name="book_form"),
    path("<int:id>/detail", views.book_detail, name="book_detail"),
    path("<int:id>/edit", views.book_edit, name="book_edit"),
    path("<int:id>/delete", views.book_delete, name="book_delete"),
    path("stats", views.book_stats, name="book_stats"),
]