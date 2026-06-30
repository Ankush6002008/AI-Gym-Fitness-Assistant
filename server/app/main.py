from fastapi import FastAPI

app = FastAPI(
    title="AI Gym Assistant API",
    version="1.0.0",
    description="Backend API for the AI Gym & Fitness Assistant project."
)


@app.get("/")
def root():
    return {"message": "AI Gym Assistant API is running 🚀"}