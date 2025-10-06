from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django_celery_results.models import TaskResult

from .tasks import short_task, long_task


def index_view(request):
    task_results = TaskResult.objects.annotate(
        duration=F("date_done") - F("date_created")
    )

    return render(
        request,
        "tasks/index.html",
        {
            "task_results": task_results,
        },
    )


def short_task_view(request):
    task = short_task.delay()

    return JsonResponse(
        {
            "message": "Short task has been started.",
            "task_id": task.id,
        }
    )


def long_task_view(request):
    task = long_task.delay()

    return JsonResponse(
        {
            "message": "Long task has been started.",
            "task_id": task.id,
        }
    )
