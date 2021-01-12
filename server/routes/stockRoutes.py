from fastapi import Request, BackgroundTasks
from server import app
from server.models.stockModel import Stock
from server.models.stockInfoModel import StockInfo
from server.models.priceModel import Price
from server.db import session
from sqlalchemy import func, desc
import yfinance as yf
import alpaca_trade_api as tradeapi
from server.config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL
from datetime import datetime

@app.get('/api/stocks/all')
def getAllStocks():
    stocks = session.query(Stock).all()
    return stocks

@app.get('/api/stock/{id}')
def getStock(id: int):
    try:
        stock = session.query(Stock).get(id)
        return stock
    except Exception as error:
        return error

def updateInfo(id: int):
    symbol = session.query(Stock).get(id).symbol
    stockInfo = yf.Ticker(symbol).info
    try:
        marketCap = stockInfo['marketCap']
        volume = stockInfo['volume']
        twoHundredDayAverage = stockInfo['twoHundredDayAverage']
        fiftyDayAverage = stockInfo['fiftyDayAverage']
        forwardPe = stockInfo['forwardPE']
        forwardEps = stockInfo['forwardEps']
        dividendYield = stockInfo['dividendYield'] * 100 if stockInfo['dividendYield'] else None
        info = session.query(StockInfo).filter(StockInfo.stockId == id)

        if info:
            info.update({'marketCap': marketCap, 'volume': volume, 'twoHundredDayAverage': twoHundredDayAverage, 'fiftyDayAverage': fiftyDayAverage, 'forwardPe': forwardPe, 'forwardEps': forwardEps, 'dividendYield': dividendYield, 'dateUpdated': datetime.utcnow()}, synchronize_session="fetch")
            session.commit()
        session.close()
    except Exception as error:
        print(error)

@app.get('/api/stock/info/{id}')
def getStockInfo(id: int, background_task: BackgroundTasks):
    try:
        stockInfo = session.query(StockInfo).filter(StockInfo.stockId == id).first()
        background_task.add_task(updateInfo, id)
        return stockInfo
    except Exception as error:
        print(error)

@app.get('/api/stock/symbol/{symbol}')
def getStockBySymbol(symbol: str):
    try:
        stock = session.query(Stock).filter(func.lower(Stock.symbol) == func.lower(symbol)).first()
        return stock
    except Exception as error:
        return error

@app.get('/api/stocks/exchange/{exchange}')
def getStocksByExchange(exchange: str):
    try:
        stocks = session.query(Stock).filter(func.lower(Stock.exchange) == func.lower(exchange)).all()
        return stocks
    except Exception as error:
        print(error)

@app.get('/api/stocks/sector/{sector}')
def getStocksBySector(sector: str):
    try:
        stocks = session.query(Stock).filter(func.lower(Stock.sector) == func.lower(sector)).all()
        return stocks
    except Exception as error:
        print(error)

@app.get('/api/stocks/industry/{industry}')
def getStocksByIndustry(industry: str):
    try:
        stocks = session.query(Stock).filter(func.lower(Stock.industry) == func.lower(industry)).all()
        return stocks
    except Exception as error:
        print(error)

def updatePrices(id: int):
    api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url=ALPACA_BASE_URL)
    symbol = session.query(Stock).get(id).symbol
    barsets = api.get_barset(symbol, '1D', limit=31)
    for bar in barsets[symbol]:
        priceExist = session.query(Price).filter(Price.date == bar.t.date()).first()
        if not priceExist:
            price = Price(id, bar.o, bar.h, bar.l, bar.c, bar.t.date())
            session.add(price)
            session.commit()
    session.close()


@app.get('/api/prices/{id}')
def getPrices(id: int, background_task: BackgroundTasks):
    prices = session.query(Price).filter(Price.stockId == id).order_by(desc(Price.date)).limit(31).all()
    background_task.add_task(updatePrices, id)
    return prices
    