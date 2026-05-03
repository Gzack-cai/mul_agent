
import os
from openai import OpenAI

class AIAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, payload):
        prompt = payload.get("prompt", "Hello")
        try:
            res = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )
            return res.choices[0].message.content
        except Exception as e:
            return str(e)
