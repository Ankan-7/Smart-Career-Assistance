from fastapi import APIRouter, Depends
from app.services.deps import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "education_level": current_user.education_level,
        "class_or_degree": current_user.class_or_degree
    }