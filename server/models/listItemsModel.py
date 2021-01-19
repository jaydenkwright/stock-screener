from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Numeric
from sqlalchemy.orm import sessionmaker
from server.db import session, Base, engine
from pydantic import BaseModel

class ListItem(Base):
    __tablename__ = 'listItems'
    id = Column('id', Integer, primary_key=True, index=True)
    userId = Column('userId', Integer)
    listId = Column('listId', Integer, nullable=False)
    stockId = Column('stockId', Integer, nullable=False)
    date = Column('date', DateTime, default=datetime.utcnow)

    def __init__(self, userId, listId, stockId):
        self.userId = userId
        self.listId = listId
        self.stockId = stockId

class ListItemModel(BaseModel):
    listId: int
    stockId: int


Base.metadata.create_all(bind=engine)