from fastapi import APIRouter

from app.auth.service import login_user, register_user
from app.users.schemas import UserLoginSchema, UserRegisterSchema

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegisterSchema):
    return register_user(user)


@router.post("/login")
def login(user: UserLoginSchema):
    return login_user(user)