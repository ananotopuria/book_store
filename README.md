# Book Store Django Project

This project is a Django application for managing a book store. It includes two models, `Author` and `Book`, which are registered and customized in the Django admin interface.

## Features

- **Model Registration**: Models are registered to be visible and manageable through the Django admin interface.
- **Existing Models**: Author and Book.
- **New Models**: Student and Course.
  - **Student**: Represents a student with a name, email, date of birth, and enrolled courses.
  - **Course**: Represents a course with a name and description.

- **Template Implementation**:
  - **Dynamic Templates**: Added a `book_detail.html` template to display detailed information about books.
  - **Template Tags and Filters**: Utilized Django template tags and filters for dynamic content, including loops, conditionals, and data formatting.

- **Form and Validation**:
  - **Create a Simple Form**:
    - Added a form to collect user data, specifically a user’s name and email.
    - Defined fields for the form: `name` and `email`.
  - **Add Basic Validation**:
    - Ensured the `name` field is required.
    - Validated that the `email` field contains a valid email address.
  - **Integrate the Form into a View**:
    - Displayed the form in a view and rendered it in a template.
    - Handled form submission and showed success or error messages based on the form's validity.

## Model Relationships

- **Author** and **Book**: The `Book` model has a ForeignKey relationship with the `Author` model.
- **Student** and **Course**: The `Student` model has a ManyToManyField relationship with the `Course` model.

## Technologies Used

- **Python** (v3.12.5)
- **Django** (v4.1)
- **SQLite3** (default Django database)

## Set Up Django REST Framework

1. **Install Django REST Framework**:
   Make sure you have `djangorestframework` installed in your virtual environment:

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd book_store