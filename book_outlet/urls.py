from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, homepage, book_detail, user_form_view

router = DefaultRouter()
router.register(r'books', BookViewSet)  
router.register(r'authors', AuthorViewSet) 

urlpatterns = [
    path('api/', include(router.urls)),  
    path('', homepage, name='homepage'), 
    path('books/<int:book_id>/', book_detail, name='book_detail'), 
    path('user-form/', user_form_view, name='user_form'), 
]