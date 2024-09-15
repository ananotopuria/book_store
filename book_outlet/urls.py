from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
