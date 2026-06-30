from pydantic import BaseModel, EmailStr, Field


class UserRegisterSchema(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=13, le=100)
    gender: str
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)
    fitness_goal: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserUpdateSchema(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    age: int = Field(..., ge=13, le=100)
    gender: str
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)
    fitness_goal: str