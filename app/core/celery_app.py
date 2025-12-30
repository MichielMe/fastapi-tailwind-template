# app/core/celery_app.py
from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["app.tasks.example"]
)

celery_app.conf.update(
    task_track_started=True,
)

