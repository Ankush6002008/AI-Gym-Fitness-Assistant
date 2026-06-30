from app.database.connection import db
from app.users.models import User
from app.auth.security import hash_password


users_collection = db["users"]


def register_user(user_data):
    # Check if email already exists
    existing_user = users_collection.find_one(
        {"email": user_data.email.lower()}
    )

    if existing_user:
        return {"success": False, "message": "Email already exists"}

    # Create User object
    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=hash_password(user_data.password),
        age=user_data.age,
        gender=user_data.gender,
        height=user_data.height,
        weight=user_data.weight,
        fitness_goal=user_data.fitness_goal,
    )

    # Save to MongoDB
    users_collection.insert_one(user.to_dict())

    return {
        "success": True,
        "message": "User registered successfully",
    }