from fastapi import APIRouter, Depends, HTTPException

from app.auth.dependencies import get_current_user
from app.users.schemas import UserUpdateSchema
from app.users.service import (
    get_user_profile,
    update_user_profile,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    profile = get_user_profile(current_user["email"])

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return profile


@router.put("/me")
def update_me(
    user_data: UserUpdateSchema,
    current_user=Depends(get_current_user),
):
    updated_profile = update_user_profile(
        current_user["email"],
        user_data,
    )

    if updated_profile is None:
        raise HTTPException(
            status_code=404,
            detail="User not found or no changes made",
        )

    return updated_profile