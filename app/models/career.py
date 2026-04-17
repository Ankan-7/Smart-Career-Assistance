from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Career(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    required_skills = Column(Text)
    roadmap = Column(Text)
    exams = Column(Text)
    demand = Column(String)
    competition = Column(String)
    difficulty = Column(String)