from fastapi import APIRouter

from app.auth.service import register_user
from app.users.schemas import UserRegisterSchema

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegisterSchema):
    return register_user(user)