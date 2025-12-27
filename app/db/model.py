from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from .database import Base

class URL(Base):
    __tablename__ = "urls"
    url_id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, nullable=True)
    short_code = Column(String, unique=True,index=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))