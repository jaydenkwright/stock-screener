from server.models.stockModel import Stock
from server.models.stockInfoModel import StockInfo
from server.models.priceModel import Price
import yfinance as yf
from server.db import session
from datetime import datetime
from server.config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL
import alpaca_trade_api as tradeapi

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