from fastapi import Request
from server import app
from server.models.stockModel import Stock
from server.db import session


@app.get('/api/stocks/all')
async def getAllStocks(request: Request):
    stocks = session.query(Stock).all()
    return stocks
