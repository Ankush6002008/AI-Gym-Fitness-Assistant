from datetime import datetime


class WorkoutPlan:
    def __init__(
        self,
        user_email: str,
        plan_name: str,
        goal: str,
        days_per_week: int,
        duration_weeks: int,
        exercises: list,
    ):
        self.user_email = user_email
        self.plan_name = plan_name
        self.goal = goal
        self.days_per_week = days_per_week
        self.duration_weeks = duration_weeks
        self.exercises = exercises
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "user_email": self.user_email,
            "plan_name": self.plan_name,
            "goal": self.goal,
            "days_per_week": self.days_per_week,
            "duration_weeks": self.duration_weeks,
            "exercises": self.exercises,
            "created_at": self.created_at,
        }