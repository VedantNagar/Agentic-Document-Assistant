from fastapi import FastAPI

from app.database.connection import Base, engine
from app.database import models

Base.metadata.create_all(bind=engine)
app = FastAPI(
 title = "ProjectAPI",
 description = "Agentic Document Assistant",
 version = "1.0"
)

@app.get('/')
def home():
 return {
  "message":"Backend is running..."
 }