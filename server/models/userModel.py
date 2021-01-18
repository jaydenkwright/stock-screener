from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from server.db import session, Base, engine
from pydantic import BaseModel

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    email = Column('email', String, nullable=False)
    password = Column('password', String, nullable=False)
    date = Column('date', DateTime, default=datetime.utcnow)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class RegistrationModel(BaseModel):
    name: str
    email: str
    password: str    

class LoginModel(BaseModel):
    email: str
    password: str


Base.metadata.create_all(bind=engine)