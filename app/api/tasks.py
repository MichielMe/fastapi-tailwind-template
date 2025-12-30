# app/api/tasks.py
from fastapi import APIRouter
from app.tasks.example import example_task

router = APIRouter()


@router.post("/trigger-task", status_code=202)
async def trigger_task():
    """
    Triggers an example background task.
    """
    task = example_task.delay("hello")
    return {"message": "Task triggered", "task_id": task.id}

