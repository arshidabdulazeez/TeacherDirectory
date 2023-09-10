# TeacherDirectory
# Teacher Directory - Django Project
## Overview

Teacher Directory is a Django web application that allows you to manage and organize information about teachers in a school. It provides features for adding, editing, and filtering teachers' details. This README provides essential information about setting up, running, and customizing the project.

## Features

- Add, edit, and delete teachers' profiles.
- Filter teachers by the first letter of their last name and by subject.
- Secure importer for bulk teacher data uploads.
- User authentication for admin access.
- Use of PostgreSQL as the database backend.
- AJAX-based filtering and dynamic content loading.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x) and pip installed on your development environment.
- Git installed to clone the project repository.
- PostgreSQL database setup with necessary credentials.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/teacher-directory.git
   cd teacher-directory

1. Create a Virtual env:
     python -m venv venv
     source venv/bin/activate  # On Windows, use: venv\Scripts\activate
2. Install project dependencies:
      pip install -r requirements.txt
   
4. Configure the database in teacher_directory/settings.py:
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL
        'NAME': 'td_maindb',  # Replace with your database name
        'USER': 'postgres',  # Replace with your database user
        'PASSWORD': 'postgres',  # Replace with your database password
        'HOST': 'localhost',  # Replace with your database host if needed
        'PORT': '5432',  # Replace with your database port if needed
    }
}


5. Apply Migrations :
     python manage.py makemigrations
      python manage.py migrate

6. Start the server:
     python manage.py runserver
     Access the project at http://localhost:8000/ in your web browser.






   


