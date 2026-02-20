from django.contrib import admin
from .models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name")
    search_fields = ("name", "last_name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "pages",
        "rating",
        "status",
        "published_date",
    )
    list_filter = ("status", "rating")
    search_fields = ("title",)
    filter_horizontal = ("authors",)