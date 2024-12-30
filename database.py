import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

os.makedirs("data", exist_ok=True)

# SQLAlchemy setup
DATABASE_URL = "sqlite:///./data/nrct.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

