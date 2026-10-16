import json
import os
from datetime import datetime, timezone
import redis
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django_celery_results.models import TaskResult
from .tasks import short_task, long_task

STATS_KEY = "stats:summary"

STATS_TTL = 30  # seconds


def get_stats():

    # Read the stats from Valkey. If the key is missing or expired, query Postgres.

    client = redis.Redis.from_url(
        os.environ["REDIS_URL"], decode_responses=True
    )

    cached = client.get(STATS_KEY)

    if cached:

        stats = json.loads(cached)

        stats["source"] = "Valkey cache"

        return stats

    finished = TaskResult.objects.filter(status__in=["SUCCESS", "FAILURE"])

    total = finished.count()

    success = finished.filter(status="SUCCESS").count()

    stats = {
        "total": total,
        "success_rate": round(success / total * 100) if total else 0,
        "computed_at": datetime.now(timezone.utc).strftime("%H:%M:%S UTC"),
    }

    client.setex(STATS_KEY, STATS_TTL, json.dumps(stats))

    stats["source"] = "Postgres"

    return stats


def index_view(request):

    task_results = TaskResult.objects.annotate(
        duration=F("date_done") - F("date_created")
    )

    return render(
        request,
        "tasks/index.html",
        {
            "task_results": task_results,
            "stats": get_stats(),
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
