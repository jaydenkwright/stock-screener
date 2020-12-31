from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yfinance as yf

DATABASE_URL = 'postgres://postgres:postgres@localhost/stock_screener'

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SesssionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# msft = yf.Ticker("AAPL")

# print(msft.info['marketCap'])
