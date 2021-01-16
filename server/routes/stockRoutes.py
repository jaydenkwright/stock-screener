from fastapi import Request, BackgroundTasks
from server import app
from server.models.stockModel import Stock
from server.models.stockInfoModel import StockInfo
from server.models.priceModel import Price
from server.tasks.stockTasks import updateInfo, updatePrices
from server.db import session
from sqlalchemy import func, desc
import yfinance as yf
import alpaca_trade_api as tradeapi
from server.config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL
from datetime import datetime

@app.get('/api/stocks/all')
def getAllStocks():
    try:
        stocks = session.query(Stock).all()
        result = []
        for stock in stocks:
            item = {}
            item['stock'] = stock
            item['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == stock.id).first()
            result.append(item)
        return result
    except Exception as error:
        print(error)

@app.get('/api/stock/{id}')
def getStock(id: int, background_task: BackgroundTasks):
    try:
        stock = session.query(Stock).get(id)
        item = {}
        item['stock'] = stock
        item['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == stock.id).first()
        item['prices'] = session.query(Price).filter(Price.stockId == stock.id).order_by(desc(Price.date)).limit(31).all()
        background_task.add_task(updateInfo, id)
        background_task.add_task(updatePrices, id)
        return item
    except Exception as error:
        return error

@app.get('/api/stock/symbol/{symbol}')
def getStockBySymbol(symbol: str, background_task: BackgroundTasks):
    try:
        stock = session.query(Stock).filter(func.lower(Stock.symbol) == func.lower(symbol)).first()
        item = {}
        item['stock'] = stock
        item['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == stock.id).first()
        item['prices'] = session.query(Price).filter(Price.stockId == stock.id).order_by(desc(Price.date)).limit(31).all()
        background_task.add_task(updateInfo, stock.id)
        background_task.add_task(updatePrices, stock.id)
        return item
    except Exception as error:
        return error

@app.get('/api/stocks/exchange/{exchange}')
def getStocksByExchange(exchange: str):
    try:
        stocks = session.query(Stock).filter(func.lower(Stock.exchange) == func.lower(exchange)).all()
        result = []
        for stock in stocks:
            item = {}
            item['stock'] = stock
            item['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == stock.id).first()
            result.append(item)
        return result
    except Exception as error:
        print(error)

@app.get('/api/stocks/sector/{sector}')
def getStocksBySector(sector: str):
    try:
        stocks = session.query(Stock).filter(func.lower(Stock.sector) == func.lower(sector)).all()
        result = []
        for stock in stocks:
            item = {}
            item['stock'] = stock
            item['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == stock.id).first()
            result.append(item)
        return result
    except Exception as error:
        print(error)

@app.get('/api/stocks/industry/{industry}')
def getStocksByIndustry(industry: str):
    try:
        stocks = session.query(Stock).filter(func.lower(Stock.industry) == func.lower(industry)).all()
        result = []
        for stock in stocks:
            item = {}
            item['stock'] = stock
            item['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == stock.id).first()
            result.append(item)
        return result
    except Exception as error:
        print(error)