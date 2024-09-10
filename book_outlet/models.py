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
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def book_count(self):
        return self.book_set.count()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name='students')

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
