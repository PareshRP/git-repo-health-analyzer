from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router

app = FastAPI(title="Git Repository Health Analyzer")

# API first
app.include_router(router)

# Frontend second
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
