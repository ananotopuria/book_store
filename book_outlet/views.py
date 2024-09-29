# from django.shortcuts import get_object_or_404, render
# from django.http import Http404
# from .models import Book
# from .forms import UserForm 
# from rest_framework import generics
# from .serializers import BookSerializer

# def homepage(request):
#     return render(request, 'book_outlet/homepage.html')

# def book_detail(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'book_outlet/book_detail.html', {'book': book})


# def user_form_view(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             return render(request, 'book_outlet/success.html', {'name': name})
#     else:
#         form = UserForm()
    
    
#     return render(request, 'book_outlet/user_form.html', {'form': form})


from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from .forms import UserForm
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def get_book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(book)
    return Response(serializer.data)
