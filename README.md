# Handling Long Running Tasks in Django Apps

This repository demonstrates how to off-load long running tasks in Django to Celery.

Read the [blog post](https://sevalla.com/blog/django-long-running-tasks-with-celery/).

## How to use?

1. Clone the repository.

2. Create a virtual environment, activate it, and install the requirements:

  ```sh
  $ python3 -m venv venv && source venv/bin/activate
  (venv) $ pip install -r requirements.txt
  ```

3. Migrate the database & start the development server:

  ```sh
  (venv) $ python manage.py migrate
  (venv) $ python manage.py runserver
  ```

4. Start a Redis instance via Docker (alternatively use a locally installed one):

  ```sh
  (venv) $ docker run -d --name redis -p 6379:6379 redis
  ```

6. Start a Celery worker:

  ```sh
  (venv) $ celery -A core worker --loglevel=INFO --concurrency=1
  ```

6. Navigate to [http://localhost:8000/](http://localhost:8000/) and kick off a few tasks.
