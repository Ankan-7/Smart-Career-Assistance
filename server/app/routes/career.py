from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy import func
from app.services.reality_check import calculate_reality
from app.database import get_db
from app.models.career import Career
from app.services.skill_gap import calculate_skill_gap
from app.services.predict import predict_career
import json
from app.models.activity import UserActivity
from app.services.deps import get_current_user
from app.models.user import User

router = APIRouter()


# -------------------------------
# MODE 1: Career → Roadmap
# -------------------------------
@router.get("/career/{name}")
def get_career(
    name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    career = db.query(Career).filter(func.lower(Career.name) == name.lower()).first()
    if not career:
        raise HTTPException(status_code=404, detail="Career not found")

    reality = calculate_reality(
        career.demand,
        career.competition,
        career.difficulty
    )
    activity = UserActivity(
        user_id = current_user.id,  # temporary
        mode="career",
        input_data=name,
        output_data=json.dumps({
            "career": career.name
        })
    )
    db.add(activity)
    db.commit()

    return {
        "name": career.name,
        "required_skills": career.required_skills,
        "roadmap": career.roadmap,
        "exams": career.exams,
        "demand": career.demand,
        "competition": career.competition,
        "difficulty": career.difficulty,
        "reality_check": reality
    }


# -------------------------------
# Skill Gap Request Schema
# -------------------------------
class SkillGapRequest(BaseModel):
    career_name: str
    user_skills: str


# -------------------------------
# Skill Gap API
# -------------------------------
@router.post("/career/skill-gap")
def get_skill_gap(data: SkillGapRequest, db: Session = Depends(get_db)):

    career = db.query(Career).filter(
        func.lower(Career.name) == data.career_name.lower()
    ).first()

    if not career:
        raise HTTPException(status_code=404, detail="Career not found")

    skill_gap = calculate_skill_gap(data.user_skills, career.required_skills)

    return {
        "career": career.name,
        "your_skills": data.user_skills,
        "missing_skills": skill_gap
    }

class PredictionRequest(BaseModel):
    skills: str

@router.post("/predict-career")
def predict(
    data: PredictionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):

    predictions = predict_career(data.skills)

    final_results = []

    for i, pred in enumerate(predictions):

        # Get career from DB
        career = db.query(Career).filter(
            func.lower(Career.name) == pred["career"].lower()
        ).first()

        if not career:
            continue

        # Skill gap
        skill_gap = calculate_skill_gap(
            data.skills,
            career.required_skills
        )

        # Reality check
        if i == 0:
            reality = calculate_reality(
                career.demand,
                career.competition,
                career.difficulty
            )
        else:
            reality = "Less Relevant Option"

        final_results.append({
            "career": career.name,
            "confidence": pred["confidence"],
            "missing_skills": skill_gap,
            "reality_check": reality
        })
    activity = UserActivity(
        user_id=current_user.id,  # temporary (we'll fix later with auth)
        mode="prediction",
        input_data=data.skills,
        output_data=json.dumps(final_results)
    )
    db.add(activity)
    db.commit()

    return {
        "input_skills": data.skills,
        "results": final_results
    }

@router.get("/history")
def get_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    activities = db.query(UserActivity).filter(
        UserActivity.user_id == current_user.id
    ).all()

    result = []

    for a in activities:
        try:
            parsed_output = json.loads(a.output_data)
        except:
            parsed_output = a.output_data

        result.append({
            "mode": a.mode,
            "input": a.input_data,
            "output": parsed_output,
            "timestamp": a.timestamp
        })

    return result