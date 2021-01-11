from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Float, BigInteger
from sqlalchemy.orm import sessionmaker

class StockInfo(Base):
    __tablename__ = 'stockInfo'
    id = Column('id', Integer, primary_key=True, index=True)
    stockId = Column('stockId', BigInteger, nullable=False)
    marketCap = Column('marketCap', BigInteger)
    volume = Column('volume', BigInteger)
    twoHundredDayAverage = Column('twoHundredDayAverage', Float)
    fiftyDayAverage = Column('fiftyDayAverage', Float)
    forwardPe = Column('forwardPe', Float)
    forwardEps = Column('forwardEps', Float)
    dividendYield = Column('dividendYield', Float)
    dateUpdated = Column('dateUpdated', DateTime, default=datetime.utcnow)

    def __init__ (self, stockId, marketCap, volume, twoHundredDayAverage, fiftyDayAverage, forwardPe, forwardEps, dividendYield):
        self.stockId = stockId
        self.marketCap = marketCap
        self.volume = volume
        self.twoHundredDayAverage = twoHundredDayAverage
        self.fiftyDayAverage = fiftyDayAverage
        self.forwardPe = forwardPe
        self.forwardEps = forwardEps
        self.dividendYield = dividendYield

#Base.metadata.create_all(bind=engine)