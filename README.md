# IT-Company-Task-Manager

This is a Django project for managing tasks in an IT company.

### Deployed
[IT company task manager](https://it-company-task-manager-ic9q.onrender.com)

## Features

- **User Authentication:** Secure user authentication system to ensure only authorized users can access the application.
- **User management:** Ability to create or edit workers, adding them position and status.
- **Task Tracking:** Efficiently track tasks. Assign tasks to workers and set deadlines. Assign logged user to tasks.
  Change tasks details (task type and tag).
- **Search Functionality:** Search for workers, tasks, positions, task types or tags using keywords for quick access.
- **Responsive Design:** Mobile-friendly interface for seamless user experience across devices.

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

## DB schema

![DB-structure diagram](/static/assets/img/db_structure.drawio.png)

## Usage

- Open your browser and go to `http://127.0.0.1:8000/`.
- Log in as the superuser to access the admin panel.

## Testing

To run the tests, use the command:

```sh
python manage.py test
