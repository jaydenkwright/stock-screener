from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Float
from sqlalchemy.orm import sessionmaker
from db import session, Base, engine

class StockInfo(Base):
    __tablename__ = 'stockInfo'
    id = Column('id', Integer, primary_key=True, index=True)
    stockId = Column('stockId', Integer, nullable=False)
    marketCap = Column('marketCap', Integer, nullable=False)
    volume = Column('volume', Integer, nullable=False)
    twoHundredDayAverage = Column('twoHundredDayAverage', Float, nullable=False)
    fiftyDayAverage = Column('fiftyDayAverage', Float, nullable=False)
    forwardPe = Column('forwardPe', Float, nullable=False)
    forwardEps = Column('forwardEps', Float, nullable=False)
    dividendYield = Column('dividendYield', Float)
    dateUpdated = Column('dateUpdated', DateTime, nullable=False)

    def __init__ (self, stockId, marketCap, volume, twoHundredDayAverage, fiftyDayAverage, forwardPe, forwardEps, dividendYield, dateUpdated):
        self.stockId = stockId
        self.marketCap = marketCap
        self.volume = volume
        self.twoHundredDayAverage = twoHundredDayAverage
        self.fiftyDayAverage = fiftyDayAverage
        self.forwardPe = forwardPe
        self.forwardEps = forwardEps
        self.dividendYield = dividendYield
        self.dateUpdated = dateUpdated

Base.metadata.create_all(bind=engine)