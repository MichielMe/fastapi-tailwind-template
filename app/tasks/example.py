# app/tasks/example.py
import time
from app.core.celery_app import celery_app


@celery_app.task
def example_task(word: str) -> str:
    """A simple example task that sleeps for 5 seconds."""
    print(f"Starting task for word: {word}")
    time.sleep(5)
    print(f"Finished task for word: {word}")
    return f"Task completed for word: {word}"

