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

## Model Relationships

- **Author** and **Book**: The `Book` model has a ForeignKey relationship with the `Author` model.
- **Student** and **Course**: The `Student` model has a ManyToManyField relationship with the `Course` model.

## Technologies Used

- **Python** (v3.12.5)
- **Django** (v4.1)
- **SQLite3** (default Django database)

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd book_store