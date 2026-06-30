from pydantic import BaseModel, Field


class WorkoutGenerationSchema(BaseModel):
    goal: str = Field(..., examples=["Muscle Gain"])
    experience: str = Field(..., examples=["Beginner"])
    equipment: str = Field(..., examples=["Gym"])
    days_per_week: int = Field(..., ge=1, le=7)
    workout_duration: int = Field(
        ...,
        ge=20,
        le=180,
        description="Workout duration in minutes",
    )
    injuries: str | None = Field(
        default=None,
        description="Any injuries or physical limitations",
    )