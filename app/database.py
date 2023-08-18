from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# Entry point for the database. 
engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
)

# SessionLocal is a class whose instances are used to manage transactions with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Connects the db engine to the sqlalchemy functionality of the db model.
Base = declarative_base()
