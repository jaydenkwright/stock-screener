import alpaca_trade_api as tradeapi
from server.models.stockModel import Stock
from server.db import session
from server.config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL
import bs4 as bs
import requests

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url=ALPACA_BASE_URL)
resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'id': 'constituents'})

for row in table.findAll('tr')[1:]:
    try:
        symbol = row.find('td').text.strip()
        name = row.findAll('td')[1].text
        sector = row.findAll('td')[3].text
        industry = row.findAll('td')[4].text
        location = row.findAll('td')[5].text
        founded = row.findAll('td')[8].text
        exchange = api.get_asset(symbol).exchange

        stock = Stock(name, symbol, exchange, sector, industry, location, founded)
        print(symbol)
        session.add(stock)
    except Exception as error:
        print(error)

session.commit()