# from django.shortcuts import render, get_object_or_404
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from django_filters import rest_framework as filters
# from .models import Book, Author
# from .forms import UserForm
# from .serializers import BookSerializer, AuthorSerializer
# from rest_framework.pagination import PageNumberPagination
# from .permissions import IsAuthorOrAdmin




# class CustomPagination(PageNumberPagination):
#     page_size = 10  
#     page_size_query_param = 'page_size'  


# class BookFilter(filters.FilterSet):
#     author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
#     published_date = filters.DateFilter(field_name='published_date')

#     class Meta:
#         model = Book
#         fields = ['author', 'published_date']


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     pagination_class = CustomPagination  
#     filterset_class = BookFilter 
#     permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrAdmin]

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

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


from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from .models import Book, Author
from .forms import UserForm
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAuthorOrAdmin 


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    published_date = filters.DateFilter(field_name='published_date')

    class Meta:
        model = Book
        fields = ['author', 'published_date']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrAdmin]
    pagination_class = CustomPagination
    filterset_class = BookFilter


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

