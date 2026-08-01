from fastapi import FastAPI

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