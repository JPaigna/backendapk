import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get database URL from environment or use SQLite as fallback
database_url = os.environ.get("DATABASE_URL", "sqlite:///./app.db")

# Special handling for SQLite to support multithreaded FastAPI usage
if database_url.startswith("sqlite"):
    engine = create_engine(
        database_url, connect_args={"check_same_thread": False}, echo=True
    )
else:
    engine = create_engine(database_url, echo=True)

# Creating a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to create tables
Base = declarative_base()
