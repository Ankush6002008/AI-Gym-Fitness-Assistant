from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.workouts.schemas import WorkoutPlanSchema
from app.workouts.service import (
    create_workout_plan,
    get_user_workout_plans,
)

router = APIRouter(prefix="/workouts", tags=["Workouts"])


@router.post("/")
def create_workout(
    workout: WorkoutPlanSchema,
    current_user=Depends(get_current_user),
):
    return create_workout_plan(
        current_user["email"],
        workout,
    )


@router.get("/")
def get_workouts(
    current_user=Depends(get_current_user),
):
    return get_user_workout_plans(
        current_user["email"]
    )