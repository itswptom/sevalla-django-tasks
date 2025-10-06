import time

from django.http import JsonResponse
from django.shortcuts import render


def index_view(request):
    return render(request, "tasks/index.html")


def short_task_view(request):
    # Simulate a short running task
    time.sleep(5)

    return JsonResponse(
        {
            "message": "Short task completed successfully.",
        }
    )


def long_task_view(request):
    # Simulate a long-running task
    time.sleep(10)

    return JsonResponse(
        {
            "message": "Long task completed successfully.",
        }
    )
