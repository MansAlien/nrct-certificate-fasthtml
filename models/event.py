from sqlalchemy import Column, Date, DateTime, Integer, String, func

from database import Base


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    event_date = Column(Date)
    created_at = Column(DateTime, default=func.now())
    file = Column(String)

