from django.contrib import admin
from .models import Author, Book, Course, Student

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('rating', 'published_date')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
    search_fields = ('name', 'email')
    list_filter = ('courses',)