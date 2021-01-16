from fastapi import Request
from server import app
from server.models.listModel import List, ListModel
from server.models.listItemsModel import ListItem, ListItemModel
from server.models.stockModel import Stock
from server.models.stockInfoModel import StockInfo
from server.db import session
from datetime import datetime

@app.get('/api/lists/all')
def getAllLists():
    lists = session.query(List).all()
    return lists

@app.get('/api/lists/{id}')
def getListsByUser(id: int):
    lists = session.query(List).filter(List.userId == 0).all()
    return id

@app.get('/api/list/{id}')
def getListById(id: int):
    try:
        getList = session.query(List).get(id).first()
        return id
    except Exception as error:
        print(error)

@app.post('/api/list/create')
def createList(li: ListModel):
    newList = List(li.userId, li.title, li.description)
    session.add(newList)
    session.commit()
    return li

@app.post('/api/list/item/create')
def createListItem(listItem: ListItemModel):
    newListItem = ListItem(listItem.userId, listItem.listId, listItem.stockId)
    session.add(newListItem)
    session.commit()
    return listItem

@app.get('/api/list/items/{id}')
def getListItems(id: int):
    listItems = session.query(ListItem).filter(ListItem.listId == id).all()
    stocks = []
    for item in listItems:
        stock = {}
        stock['stock'] = session.query(Stock).get(item.stockId)
        stock['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == item.stockId).first()
        stocks.append(stock)
    return stocks
