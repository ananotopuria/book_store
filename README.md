# Book Store Django Project

This project is a Django application designed for managing a book store. It allows users to interact with various models representing authors, books, students, and courses through both a web interface and a RESTful API.

## Description

The Book Store application provides functionalities to manage books and their authors, alongside features for student enrollment in courses. The project implements a clean and dynamic user interface using Django templates, while also exposing RESTful endpoints for integration with other applications.

## Features

- **Model Registration**: 
  - All models are registered to be visible and manageable through the Django admin interface, facilitating easy content management.

- **Models**: 
  - **Existing Models**:
    - **Author**: Represents a book author with attributes like name and email.
    - **Book**: Represents a book with attributes including title, rating, author (linked through ForeignKey), and publication date.
  
  - **New Models**:
    - **Student**: Represents a student with attributes such as name, email, date of birth, and enrolled courses (ManyToManyField relationship with Course).
    - **Course**: Represents a course with a name and description.

- **Template Implementation**:
  - **Dynamic Templates**: Implemented a `book_detail.html` template that displays detailed information about individual books.
  - **Template Tags and Filters**: Utilized Django template tags and filters to manage dynamic content rendering, including loops, conditionals, and data formatting.

- **Form and Validation**:
  - **User Data Collection**:
    - Created a form to collect user information (name and email).
    - Defined required fields for form submission: `name` and `email`.
  - **Basic Validation**:
    - Ensured the `name` field is required and the `email` field contains a valid email address.
  - **Form Integration**:
    - Rendered the form within a view and displayed it using a corresponding template.
    - Managed form submission and provided feedback with success or error messages based on the validation outcome.

- **Django REST Framework Integration**:
  - Set up RESTful API endpoints for the `Book` and `Author` models, allowing for CRUD operations (Create, Read, Update, Delete) via HTTP requests.
  - Applied permissions to restrict certain actions to authenticated users while keeping GET requests accessible to all users.

## Model Relationships

- **Author and Book**: The `Book` model has a ForeignKey relationship with the `Author` model, establishing a one-to-many relationship.
- **Student and Course**: The `Student` model has a ManyToManyField relationship with the `Course` model, allowing students to enroll in multiple courses and vice versa.

## Technologies Used

- **Python** (v3.12.5)
- **Django** (v4.1)
- **Django REST Framework** (v3.15.2)
- **SQLite3** (default Django database)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd book_store
