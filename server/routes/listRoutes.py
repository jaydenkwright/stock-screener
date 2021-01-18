from fastapi import Request, HTTPException
from server import app
from server.models.listModel import List, ListModel
from server.models.listItemsModel import ListItem, ListItemModel
from server.models.stockModel import Stock
from server.models.stockInfoModel import StockInfo
from server.db import session
from datetime import datetime

@app.get('/api/lists/all')
def getAllLists():
    try:
        lists = session.query(List).all()
        if not lists: raise HTTPException(status_code=404, detail="No lists were found!")
        return lists
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")


@app.get('/api/lists/{id}')
def getListsByUser(id: int):
    try:
        lists = session.query(List).filter(List.userId == id).all()
        if not lists: raise HTTPException(status_code=404, detail="No lists were found!")
        return lists
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@app.get('/api/list/{id}')
def getListById(id: int):
    try:
        getList = session.query(List).get(id)
        if not getList: raise HTTPException(status_code=404, detail="List was not found!")
        return getList
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@app.put('/api/list/{id}')
def updateList(id, li: ListModel):
    try:
        oldList = session.query(List).get(id)
        oldList.title = li.title
        oldList.description = li.description
        session.commit()
        return li
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@app.delete('/api/list/{id}')
def deleteList(id):
    try:
        li = session.query(List).get(id)
        if not li: raise HTTPException(status_code=404, detail="List was not found!")
        session.delete(li)
        session.commit()
        return li
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@app.get('/api/list/items/{id}')
def getListItems(id: int):
    try:
        listItems = session.query(ListItem).filter(ListItem.listId == id).all()
        if not listItems: raise HTTPException(status_code=404, detail="No stocks have been added!")
        stocks = []
        for item in listItems:
            stock = {}
            stock['stock'] = session.query(Stock).get(item.stockId)
            stock['stockInfo'] = session.query(StockInfo).filter(StockInfo.stockId == item.stockId).first()
            stocks.append(stock)
        return stocks
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")


@app.post('/api/list/create')
def createList(li: ListModel):
    try:
        newList = List(li.userId, li.title, li.description)
        session.add(newList)
        session.commit()
        return li
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")
    

@app.post('/api/list/item/create')
def createListItem(listItem: ListItemModel):
    try:
        newListItem = ListItem(listItem.userId, listItem.listId, listItem.stockId)
        session.add(newListItem)
        session.commit()
        return listItem
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")