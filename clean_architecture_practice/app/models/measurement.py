from sqlalchemy import Column, Integer, Float, DateTime
from app.core.database import Base
from datetime import datetime

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    weight = Column(Float)
    height = Column(Float)
    imt = Column(Float)
    created_at = Column(DateTime, default=datetime.now)