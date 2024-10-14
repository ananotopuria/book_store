# Book Store Django Project

This project is a Django application designed for managing a book store. It allows users to interact with various models representing authors, books, students, and courses through both a web interface and a RESTful API.

## Description

The Book Store application provides functionalities to manage books and their authors, alongside features for student enrollment in courses. The project implements a clean and dynamic user interface using Django templates while also exposing RESTful endpoints for integration with other applications.

## Features

### Model Registration
- All models are registered to be visible and manageable through the Django admin interface, facilitating easy content management.

### Models
#### Existing Models
- **Author**: Represents a book author with attributes like name and email.
- **Book**: Represents a book with attributes including title, rating, author (linked through ForeignKey), and publication date.

#### New Models
- **Student**: Represents a student with attributes such as name, email, date of birth, and enrolled courses (ManyToManyField relationship with Course).
- **Course**: Represents a course with a name and description.

### Template Implementation
- **Dynamic Templates**: Implemented a `book_detail.html` template that displays detailed information about individual books.
- **Template Tags and Filters**: Utilized Django template tags and filters to manage dynamic content rendering, including loops, conditionals, and data formatting.

### Form and Validation
- **User Data Collection**: Created a form to collect user information (name and email) with required fields for form submission.
- **Basic Validation**: Ensured the name field is required and the email field contains a valid email address.
- **Form Integration**: Rendered the form within a view and displayed it using a corresponding template, managing form submission and providing feedback with success or error messages based on validation outcomes.

### Django REST Framework Integration
- Set up RESTful API endpoints for the Book and Author models, allowing for CRUD operations (Create, Read, Update, Delete) via HTTP requests.
- Applied permissions to restrict certain actions to authenticated users while keeping GET requests accessible to all users.
- **Pagination**: Implemented pagination in the Book API using DRF's built-in pagination classes, limiting results to 10 books per page.
- **Filtering**: Integrated Django-filter to allow filtering books by author and published date through query parameters.
- **Custom Permissions**: Created a custom permission class to allow only the author of a book or an admin to update or delete it, ensuring appropriate access control in the BookViewSet.

### Model Relationships
- **Author and Book**: The Book model has a ForeignKey relationship with the Author model, establishing a one-to-many relationship.
- **Student and Course**: The Student model has a ManyToManyField relationship with the Course model, allowing students to enroll in multiple courses and vice versa.

## Task: Integrate Celery with Django for Asynchronous Email Sending

1. **Install Celery and Set Up Django Settings**:
   - Install Celery and Redis as the message broker.
   - Configure Celery in Django's settings and create a task to send an email asynchronously.

2. **Define an Asynchronous Task**:
   - Create a task to send a welcome email when a user registers.
   - The email should be sent asynchronously using Celery.

3. **Schedule a Periodic Task**:
   - Set up Celery Beat to schedule a task that sends a randomly generated weekly newsletter.

## Technologies Used
- Python (v3.12.5)
- Django (v4.1)
- Django REST Framework (v3.15.2)
- SQLite3 (default Django database)

## Installation

### Clone the Repository
```bash
git clone git@github.com:ananotopuria/book_store.git
cd book_store
