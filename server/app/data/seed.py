from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.career import Career


def seed_data():
    db: Session = SessionLocal()

    careers = [
        {
            "name": "Data Scientist",
            "required_skills": "Python, Machine Learning, Statistics, SQL, Data Visualization",
            "roadmap": "Learn Python → Learn Statistics → Learn ML → Work on Projects → Apply for Jobs",
            "exams": "None",
            "demand": "High",
            "competition": "High",
            "difficulty": "High"
        },
        {
            "name": "Doctor",
            "required_skills": "Biology, Chemistry, Patient Care, Diagnosis",
            "roadmap": "Class 12 PCB → NEET → MBBS → Internship → Specialization",
            "exams": "NEET",
            "demand": "High",
            "competition": "Very High",
            "difficulty": "Very High"
        }
    ]

    for career in careers:
        exists = db.query(Career).filter(Career.name == career["name"]).first()

        if not exists:
            new_career = Career(**career)
            db.add(new_career)

    db.commit()
    db.close()


if __name__ == "__main__":
    seed_data()