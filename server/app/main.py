from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.database.connection import test_connection

app = FastAPI(
    title="AI Gym Assistant API",
    version="1.0.0",
    description="Backend API for the AI Gym & Fitness Assistant project."
)


@app.on_event("startup")
def startup_event():
    test_connection()


app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "AI Gym Assistant API is running 🚀"}