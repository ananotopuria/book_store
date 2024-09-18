from django.urls import path
from .views import homepage, book_detail, user_form_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('book/<int:book_id>/', book_detail, name='book_detail'), 
    path('user-form/', user_form_view, name='user_form'),  
]
