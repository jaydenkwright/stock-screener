from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Numeric
from sqlalchemy.orm import sessionmaker
from db import session, Base, engine

class Price(Base):
    __tablename__ = 'prices'
    id = Column('id', Integer, primary_key=True, index=True)
    stockId = Column('stockId', Integer, nullable=False)
    open = Column('open', Numeric, nullable=False)
    high = Column('high', Numeric, nullable=False)
    low = Column('low', Numeric, nullable=False)
    close = Column('high', Numeric, nullable=False)
    date = Column('date', DateTime, nullable=False)

    def __init__(self, stockId, open, high, low, close, date):
        self.stockId = stockId
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.date = date
    
Base.metadata.create_all(bind=engine)