from django.urls import path
from .views import homepage, book_detail, user_form_view, BookList, BookCreate, get_book_detail

urlpatterns = [
    path('', homepage, name='homepage'),
    path('book/<int:book_id>/', book_detail, name='book-detail'),
    path('user-form/', user_form_view, name='user-form'),
    
    path('api/books/', BookList.as_view(), name='book-list-api'),
    path('api/books/create/', BookCreate.as_view(), name='book-create-api'),
    path('api/books/<int:pk>/', get_book_detail, name='book-detail-api'),
]
