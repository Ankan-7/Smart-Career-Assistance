from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    education_level: str | None = None
    class_or_degree: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str