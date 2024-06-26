# Out of Office
This Django-based application helps manage employee leave requests, approval requests, projects, and more. The system supports roles for HR managers, Project managers, and Employees, providing each role with specific functionalities.
This application uses the built-in Sqlite3 database, which is alreadt in repo.

## Setup and Installation
### Prerequisites
Python 3.12.x
Poetry

## Installation
### Clone the repository:
~~~
git clone https://github.com/keyhot/out-of-office.git
cd out_of_office
~~~
### Set up the virtual environment and install dependencies:
~~~
poetry install
~~~
### Run database migrations:
~~~
poetry run python manage.py makemigrations
poetry run python manage.py migrate
~~~
### Create superuser for accessing Django Admin:
~~~
poetry run python manage.py createsuperuser
~~~
### Run the development server:
~~~
poetry run python manage.py runserver
~~~

## Usage
Access the Django Admin at http://127.0.0.1:8000/admin to manage roles and permissions.
Assign users to the appropriate roles (HR Manager, Project Manager, Employee) using the admin panel.
