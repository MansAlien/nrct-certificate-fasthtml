import enum

from sqlalchemy import TIMESTAMP, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


# ENUM Definitions
class AttendanceStatus(enum.Enum):
    registered = "registered"
    attended = "attended"
    absent = "absent"

class CertificateStatus(enum.Enum):
    generated = "generated"
    sent = "sent"
    viewed = "viewed"

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    event_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    description = Column(Text)
    duration = Column(Integer)
    certificate_template_url = Column(Text)

    participants = relationship("EventParticipant", back_populates="event")
    certificates = relationship("Certificate", back_populates="event")

# EventParticipant Table
class EventParticipant(Base):
    __tablename__ = "event_participant"

    event_id = Column(Integer, ForeignKey("event.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    registration_date = Column(TIMESTAMP, nullable=False)
    attendance_status = Column(Enum(AttendanceStatus), nullable=False)

    event = relationship("Event", back_populates="participants")
    user = relationship("User", back_populates="participants")

# Certificate Table
class Certificate(Base):
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey("event.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    certificate_number = Column(String(50), unique=True, nullable=False)
    type = Column(String(50))
    status = Column(Enum(CertificateStatus), nullable=False)
    file_url = Column(Text)
    generated_at = Column(TIMESTAMP, nullable=False)
    last_updated_at = Column(TIMESTAMP, nullable=False)

    event = relationship("Event", back_populates="certificates")
    user = relationship("User", back_populates="certificates")

