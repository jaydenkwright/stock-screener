from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from db import session, Base

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    symbol = Column('symbol', String, nullable=False, unique=True)
    exchange = Column('exchange', String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, symbol, exchange):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange




#Base.metadata.create_all(bind=engine)

