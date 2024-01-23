"""
Esto permite """
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()  # take environment variables from .env.

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database_name = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{user}:{password}@localhost/{database_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
