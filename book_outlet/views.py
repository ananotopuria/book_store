from django.shortcuts import render
from .models import Book

def homepage(request):
    return render(request, 'book_outlet/homepage.html')


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_outlet/book_detail.html', {'book': book})
