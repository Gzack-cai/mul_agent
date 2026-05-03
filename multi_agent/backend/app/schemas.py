
from pydantic import BaseModel
from typing import Dict, Any

class TaskRequest(BaseModel):
    task_type: str
    payload: Dict[str, Any]
