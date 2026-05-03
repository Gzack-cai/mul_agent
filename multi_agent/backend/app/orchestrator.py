
from app.agents.email_agent import EmailAgent
from app.agents.data_agent import DataAgent
from app.agents.ai_agent import AIAgent

class Orchestrator:
    def __init__(self):
        self.agents = {
            "email": EmailAgent(),
            "data": DataAgent(),
            "ai": AIAgent(),
        }

    def execute(self, task):
        agent = self.agents.get(task.task_type)
        if not agent:
            return "Unsupported task"
        return agent.run(task.payload)
