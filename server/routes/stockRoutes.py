from fastapi import Request
from server import app
from server.models.stockModel import Stock
from server.db import session


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

@app.get('/api/stock/symbol/{symbol}')
def getStockBySymbol(symbol: str):
    try:
        symbol = symbol.upper()
        stock = session.query(Stock).filter(Stock.symbol == symbol).first()
        return stock
    except Exception as error:
        return error

@app.get('/api/stocks/exchange/{exchange}')
def getStocksByExchange(exchange: str):
    try:
        exchange = exchange.upper()
        stocks = session.query(Stock).filter(Stock.exchange == exchange).all()
        return stocks
    except Exception as error:
        print(error)

    