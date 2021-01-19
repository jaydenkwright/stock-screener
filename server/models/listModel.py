from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Numeric
from sqlalchemy.orm import sessionmaker
from server.db import session, Base, engine
from pydantic import BaseModel
from typing import Optional

class List(Base):
    __tablename__ = 'lists'
    id = Column('id', Integer, primary_key=True, index=True)
    userId = Column('userId', Integer)
    title = Column('title', String, nullable=False)
    description = Column('description', String)
    date = Column('date', DateTime, default=datetime.utcnow)

    def __init__(self, userId, title, description):
        self.userId = userId
        self.title = title
        self.description = description

class ListModel(BaseModel):
    title: str
    description: Optional[str]


Base.metadata.create_all(bind=engine)