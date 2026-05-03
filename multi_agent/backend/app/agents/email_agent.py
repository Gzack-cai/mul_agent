
class EmailAgent:
    def run(self, payload):
        return f"[EmailAgent] Send email to {payload.get('to')}"
