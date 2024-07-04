# IT-Company-Task-Manager

This is a Django project for managing tasks in an IT company.

## Admin Credentials

- **Username:** TestAdmin
- **Password:** 1qazcde3

## Requirements

- Python 3.x
- Django 3.x or higher
- PostgreSQL or another compatible database

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/voboian/ITCompanyTaskManager.git
    cd ITCompanyTaskManager
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database and run migrations:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Open your browser and go to `http://127.0.0.1:8000/`.
- Log in as the superuser to access the admin panel.

## Testing

To run the tests, use the command:

```sh
python manage.py test
