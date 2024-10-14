# from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name
    
#     def book_count(self):
#         return self.book_set.count()

# class Book(models.Model):
#     title = models.CharField(max_length=50)
#     rating = models.IntegerField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     published_date = models.DateField()

#     def __str__(self):
#         return self.title

from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")
    email = models.EmailField(verbose_name="Author Email")

    def __str__(self):
        return self.name

    def book_count(self):
        return self.book_set.count()

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="Book Title")
    rating = models.IntegerField(verbose_name="Book Rating")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")
    published_date = models.DateField(verbose_name="Published Date")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Course Name")
    description = models.TextField(verbose_name="Course Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(verbose_name="Student Email")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    courses = models.ManyToManyField(Course, related_name='students', verbose_name="Enrolled Courses")

    def __str__(self):
        return self.name

    def enrolled_courses(self):
        return self.courses.all()

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
