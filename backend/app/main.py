from fastapi import FastAPI

from app.database.connection import Base, engine
from app.database import models
from app.api.routes.router import api_router

# Create all tables that don't exist yet.
# SQLAlchemy reads every model registered under Base
# and issues CREATE TABLE IF NOT EXISTS for each one.
Base.metadata.create_all(bind=engine)

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