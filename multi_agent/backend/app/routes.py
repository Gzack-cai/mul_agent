
from fastapi import APIRouter
from app.schemas import TaskRequest
from app.orchestrator import Orchestrator

router = APIRouter()
orch = Orchestrator()

@router.post("/run-task")
def run_task(task: TaskRequest):
    return {"result": orch.execute(task)}
