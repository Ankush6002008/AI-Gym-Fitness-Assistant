from app.database.connection import db


def get_user_by_email(email: str):
    return db["users"].find_one({"email": email})


def get_user_profile(email: str):
    user = get_user_by_email(email)

    if not user:
        return None

    return {
        "full_name": user["full_name"],
        "email": user["email"],
        "age": user["age"],
        "gender": user["gender"],
        "height": user["height"],
        "weight": user["weight"],
        "fitness_goal": user["fitness_goal"],
    }

def update_user_profile(email: str, user_data):
    result = db["users"].update_one(
        {"email": email},
        {
            "$set": {
                "full_name": user_data.full_name,
                "age": user_data.age,
                "gender": user_data.gender,
                "height": user_data.height,
                "weight": user_data.weight,
                "fitness_goal": user_data.fitness_goal,
            }
        },
    )

    if result.modified_count == 0:
        return None

    return get_user_profile(email)