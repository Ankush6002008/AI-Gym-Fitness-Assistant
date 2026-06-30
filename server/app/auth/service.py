from app.database.connection import db
from app.users.models import User
from app.auth.security import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

users_collection = db["users"]


def register_user(user_data):
    existing_user = users_collection.find_one(
        {"email": user_data.email.lower()}
    )

    if existing_user:
        return {
            "success": False,
            "message": "Email already exists"
        }

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

    users_collection.insert_one(user.to_dict())

    return {
        "success": True,
        "message": "User registered successfully",
    }


def login_user(user_data):
    user = users_collection.find_one(
        {"email": user_data.email.lower()}
    )

    if not user:
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    if not verify_password(user_data.password, user["password"]):
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    access_token = create_access_token(
        {
            "sub": user["email"]
        }
    )

    return {
        "success": True,
        "access_token": access_token,
        "token_type": "bearer"
    }