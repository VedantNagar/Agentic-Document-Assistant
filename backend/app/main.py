from fastapi import FastAPI

from app.database.connection import Base, engine
from app.database import models
from app.api.routes.router import api_router

app = FastAPI(
    title="ProjectAPI",
    description="Agentic Document Assistant",
    version="1.0"
)

# Register all API routes under /api
app.include_router(api_router)


@app.get("/")
def home():
    return {"message": "Backend is running..."}