import time

from celery import shared_task


@shared_task
def short_task():
    # Simulate a short running task
    time.sleep(5)

    return "Short task completed successfully."


@shared_task
def long_task():
    # Simulate a long-running task
    time.sleep(10)

    return "Long task completed successfully."
