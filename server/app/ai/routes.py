from fastapi import APIRouter

from app.ai.schemas import WorkoutGenerationSchema
from app.ai.workout_generator import generate_workout

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post("/generate-workout")
def generate_workout_route(
    workout_request: WorkoutGenerationSchema,
):
    workout = generate_workout(workout_request)

    return {
        "success": True,
        "workout": workout,
    }