import alpaca_trade_api as tradeapi
from server.config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL
from server.models.stockModel import Stock
from server.db import session
from server.models.priceModel import Price

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

    barsets = api.get_barset(symbol_chunk, '1D', limit=31)
    for symbol in barsets:
        for bar in barsets[symbol]:
            priceExist = session.query(Price).filter(Price.date == bar.t.date(), Price.stockId == stockIds[symbol]).first()
            if not priceExist:
                price = Price(stockIds[symbol], bar.o, bar.h, bar.l, bar.c, bar.t.date())
                session.add(price)
                print(stockIds[symbol], bar.o, bar.h, bar.l, bar.c, bar.t.date())

session.commit()
