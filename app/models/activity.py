from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class UserActivity(Base):
    __tablename__ = "user_activity"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    mode = Column(String)
    input_data = Column(Text)
    output_data = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)