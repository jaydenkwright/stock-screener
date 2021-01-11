import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL
from stockModel import Stock
from db import session
from priceModel import Price

stockData = session.query(Stock).all()
symbols = []
stockIds = {}
for stock in stockData:
    stockIds[stock.symbol] = stock.id
    symbols.append(stock.symbol)

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url=ALPACA_BASE_URL)

chunk = 200
for i in range(0, len(symbols), chunk):
    symbol_chunk = symbols[i:i+chunk]

    barsets = api.get_barset(symbol_chunk, 'day')
    for symbol in barsets:
        for bar in barsets[symbol]:
            price = Price(stockIds[symbol], bar.o, bar.h, bar.l, bar.c, bar.t.date())
            session.add(price)

session.commit()
