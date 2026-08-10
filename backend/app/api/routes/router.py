from fastapi import APIRouter

from app.api.routes import auth,workspaces

# This is the single router that main.py will include.
# All sub-routers (auth, documents, chat, workspaces)
# get registered here as the project grows.
api_router = APIRouter(prefix="/api")

api_router.include_router(auth.router)
api_router.include_router(workspaces.router)
