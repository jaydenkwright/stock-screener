from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

engine = create_engine(
    DATABASE_URL, echo=True
)

SesssionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SesssionLocal()
Base = declarative_base()
