from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.database.connection import test_connection
from app.users.routes import router as users_router
from app.workouts.routes import router as workouts_router
from fastapi.middleware.cors import CORSMiddleware
from app.ai.routes import router as ai_router

app = FastAPI(
    title="AI Gym Assistant API",
    version="1.0.0",
    description="Backend API for the AI Gym & Fitness Assistant project."
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    test_connection()


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(workouts_router)
app.include_router(ai_router)


@app.get("/")
def root():
    return {"message": "AI Gym Assistant API is running 🚀"}