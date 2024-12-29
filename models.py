import os

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    String,
    create_engine,
    func,
)
from sqlalchemy.orm import declarative_base, sessionmaker

os.makedirs("data", exist_ok=True)
# SQLAlchemy setup
DATABASE_URL = "sqlite:///./data/todo.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the Todo model
class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, default=False)

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    event_date = Column(Date)
    created_at = Column(DateTime, default=func.now())
    file = Column(String)

# Create the tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)


