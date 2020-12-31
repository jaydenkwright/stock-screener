import alpaca_trade_api as tradeapi
from stockModel import Stock
from db import session
from config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url=ALPACA_BASE_URL)

assets = api.list_assets()

for asset in assets:
    try:
        if asset and asset.status == 'active':
            stock = Stock(asset.name, asset.symbol, asset.exchange)
            session.add(stock)
    except Exception as error:
        print(error)

session.commit()