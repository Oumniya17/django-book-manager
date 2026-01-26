from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book


# lista real de libros
def book_list(request):
    books = Book.objects.all()
    return HttpResponse(f"Books: {books.count()}")


# requiere login
@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return HttpResponse(f"Detail: {book.title}")


# permiso add
@permission_required('bookapp.add_book')
def book_form(request):
    return HttpResponse("form")


# permiso change
@permission_required('bookapp.change_book')
def book_edit(request, id):
    book = get_object_or_404(Book, pk=id)
    return HttpResponse(f"edit {book.title}")


# permiso delete
@permission_required('bookapp.delete_book')
def book_delete(request, id):
    book = get_object_or_404(Book, pk=id)
    return HttpResponse(f"delete {book.title}")
