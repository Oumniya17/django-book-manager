from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Avg, Count
from .models import Book
from .forms import BookForm



# LIST

def book_list(request):
    books = Book.objects.all()

    # Search
    search = request.GET.get("search")
    if search:
        books = books.filter(title__icontains=search)

    # Order (validated)
    allowed_orders = ["title", "pages", "rating", "status", "published_date"]
    order = request.GET.get("order")
    if order in allowed_orders:
        books = books.order_by(order)

    # Pagination
    paginator = Paginator(books, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "bookapp/book_list.html", {
        "page_obj": page_obj,
        "search": search,
        "order": order,
    })



# DETAIL

@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "bookapp/book_detail.html", {"book": book})



# CREATE

@permission_required('bookapp.add_book')
def book_form(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("bookapp:book_list")
    else:
        form = BookForm()

    return render(request, "bookapp/book_form.html", {"form": form})



# EDIT

@permission_required('bookapp.change_book')
def book_edit(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookapp:book_detail", id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, "bookapp/book_edit.html", {
        "form": form,
        "book": book
    })


# DELETE

@permission_required('bookapp.delete_book')
def book_delete(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        book.delete()
        return redirect("bookapp:book_list")

    return render(request, "bookapp/book_delete.html", {"book": book})



# STATS

def book_stats(request):
    books = Book.objects.all()

    max_pages = books.order_by("-pages").first()
    min_pages = books.order_by("pages").first()

    avg_pages = books.aggregate(Avg("pages"))["pages__avg"] or 0
    avg_rating = books.aggregate(Avg("rating"))["rating__avg"] or 0

    status_data = books.values("status").annotate(count=Count("status"))
    rating_data = books.values("rating").annotate(count=Count("rating"))

    return render(request, "bookapp/book_stats.html", {
        "max_pages": max_pages,
        "min_pages": min_pages,
        "avg_pages": avg_pages,
        "avg_rating": avg_rating,
        "status_data": status_data,
        "rating_data": rating_data,
    })