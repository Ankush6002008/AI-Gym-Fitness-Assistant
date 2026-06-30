from pydantic import BaseModel, Field
from typing import List


class ExerciseSchema(BaseModel):
    name: str
    sets: int = Field(..., gt=0)
    reps: str


class WorkoutPlanSchema(BaseModel):
    plan_name: str = Field(..., min_length=3, max_length=100)
    goal: str
    days_per_week: int = Field(..., ge=1, le=7)
    duration_weeks: int = Field(..., ge=1, le=52)
    exercises: List[ExerciseSchema]