
class DataAgent:
    def run(self, payload):
        data = payload.get("data", [])
        return {"count": len(data)}
