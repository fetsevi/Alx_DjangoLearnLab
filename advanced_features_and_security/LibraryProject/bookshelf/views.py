from django.shortcuts import render

# Create your views here.

# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("You can add a new book here!")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You can edit the book: {book.title}")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You can delete the book: {book.title}")


from django.shortcuts import render
from django.db.models import Q
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data["query"]
        # Safe ORM query (prevents SQL injection)
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    return render(request, "bookshelf/book_list.html", {"form": form, "books": books})
