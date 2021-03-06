import yfinance as yf
from server.models.stockModel import Stock
from server.models.stockInfoModel import StockInfo
from server.db import session
from datetime import datetime

stockData = session.query(Stock).all()
symbols = []
stockIds = {}
for stock in stockData:
    stockIds[stock.symbol] = stock.id
    symbols.append(stock.symbol)


chunk = 200
for i in range(0, len(symbols), chunk):
    symbol_chunk = symbols[i:i+chunk]

    info = yf.Tickers(symbol_chunk)

    for stock in info.tickers:
        try:
            symbol = stock.info['symbol']
            stockId = stockIds[stock.info['symbol']]
            marketCap = stock.info['marketCap']
            volume = stock.info['volume']
            twoHundredDayAverage = stock.info['twoHundredDayAverage']
            fiftyDayAverage = stock.info['fiftyDayAverage']
            forwardPe = stock.info['forwardPE']
            forwardEps = stock.info['forwardEps']
            dividendYield = stock.info['dividendYield'] * 100 if stock.info['dividendYield'] else None

            info = session.query(StockInfo).filter(StockInfo.stockId == stockId)

            if info:
                info.update({'marketCap': marketCap, 'volume': volume, 'twoHundredDayAverage': twoHundredDayAverage, 'fiftyDayAverage': fiftyDayAverage, 'forwardPe': forwardPe, 'forwardEps': forwardEps, 'dividendYield': dividendYield, 'dateUpdated': datetime.utcnow()}, synchronize_session="fetch")
                session.commit()
            else:
                stockInfo = StockInfo(stockId, marketCap, volume, twoHundredDayAverage, fiftyDayAverage, forwardPe, forwardEps, dividendYield)
                session.add(stockInfo)
                session.commit()
        except Exception as error:
            print(error)

session.close()
            

