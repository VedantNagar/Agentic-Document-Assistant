from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create a single database engine.
# The engine manages the connection to PostgreSQL.
engine = create_engine(DATABASE_URL)


# SessionLocal creates a new database session for each request.
# Every API request gets its own session, which is closed afterwards
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# Base is the parent class that all SQLAlchemy models inherit from.

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()