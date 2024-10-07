from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  

    class Meta:
        model = Book
        fields = ['id', 'title', 'rating', 'author', 'published_date']