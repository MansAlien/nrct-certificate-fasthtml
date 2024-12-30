from sqlalchemy import TIMESTAMP, Column, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


# User Table
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    full_name = Column(String(255))
    phone = Column(String(20))
    whatsapp = Column(String(20))
    city = Column(String(100))
    address = Column(Text)
    major = Column(String(100))
    created_at = Column(TIMESTAMP, nullable=False)

    participants = relationship("EventParticipant", back_populates="user")
    certificates = relationship("Certificate", back_populates="user")

