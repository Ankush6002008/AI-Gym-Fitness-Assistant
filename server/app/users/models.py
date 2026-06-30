from datetime import datetime


class User:
    def __init__(
        self,
        full_name: str,
        email: str,
        password: str,
        age: int,
        gender: str,
        height: float,
        weight: float,
        fitness_goal: str,
    ):
        self.full_name = full_name
        self.email = email.lower()
        self.password = password
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.fitness_goal = fitness_goal
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "fitness_goal": self.fitness_goal,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }