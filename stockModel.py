from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from db import session, Base, engine

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    symbol = Column('symbol', String, nullable=False, unique=True)
    exchange = Column('exchange', String, nullable=False)
    sector = Column('sector', String, nullable=False)
    industry = Column('industry', String, nullable=False)
    location = Column('location', String, nullable=False)
    founded = Column('founded', String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, symbol, exchange, sector, industry, location, founded):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.sector = sector
        self.industry = industry
        self.location = location
        self.founded = founded

#Base.metadata.create_all(bind=engine)

