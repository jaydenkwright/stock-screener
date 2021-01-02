import yfinance as yf
from stockModel import Stock
from stockInfoModel import StockInfo
from db import session
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
                print('already in database')
                info.update({'marketCap': marketCap, 'volume': volume, 'twoHundredDayAverage': twoHundredDayAverage, 'fiftyDayAverage': fiftyDayAverage, 'forwardPe': forwardPe, 'forwardEps': forwardEps, 'dividendYield': dividendYield}, synchronize_session="fetch")
            else:
                stockInfo = StockInfo(stockId, marketCap, volume, twoHundredDayAverage, fiftyDayAverage, forwardPe, forwardEps, dividendYield)
                session.add(stockInfo)
        except Exception as error:
            print(error)

session.commit()
            

