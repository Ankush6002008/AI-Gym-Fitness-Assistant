from app.database.connection import db
from app.workouts.models import WorkoutPlan

workouts_collection = db["workout_plans"]


def create_workout_plan(user_email: str, workout_data):
    workout = WorkoutPlan(
        user_email=user_email,
        plan_name=workout_data.plan_name,
        goal=workout_data.goal,
        days_per_week=workout_data.days_per_week,
        duration_weeks=workout_data.duration_weeks,
        exercises=[
            exercise.model_dump() for exercise in workout_data.exercises
        ],
    )

    result = workouts_collection.insert_one(workout.to_dict())

    return {
        "message": "Workout plan created successfully",
        "workout_plan_id": str(result.inserted_id),
    }


def get_user_workout_plans(user_email: str):
    plans = list(
        workouts_collection.find(
            {"user_email": user_email},
            {"_id": 0},
        )
    )

    return plans