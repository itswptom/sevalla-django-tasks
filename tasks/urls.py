from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.index_view),
    path("short-task/", views.short_task_view),
    path("long-task/", views.long_task_view),
]
