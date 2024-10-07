from django.shortcuts import render, get_object_or_404 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Author
from .forms import UserForm
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def homepage(request):
    return render(request, 'book_outlet/homepage.html')


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_outlet/book_detail.html', {'book': book})


def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'book_outlet/success.html', {'name': name})
    else:
        form = UserForm()
    
    return render(request, 'book_outlet/user_form.html', {'form': form})
