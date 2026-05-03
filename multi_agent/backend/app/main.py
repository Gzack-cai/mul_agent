
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Enterprise Multi-Agent Platform")

app.include_router(router)
