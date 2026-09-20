from unicodedata import name

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(name = "First CRUD API", version = "v1", description = "First CRUD API")

class Item(BaseModel):
    name : str
    price : float

itemsStorage = { }

#Item adding in storage
@app.post("/items/")
def addData(item : Item):
    item_id = len(itemsStorage) + 1;
    itemsStorage[item_id] = item
    return {"id" : item_id , "item" : item}

@app.get("/items/{item_id}")
async def getData(item_id: int):
    return itemsStorage.get(item_id, {"error" : None})

@app.put("/items/update/{items_id}")
async def updateData(items_id : int, item: Item):
    if items_id in itemsStorage:
        itemsStorage[items_id] = item
        return {"messgae" : "Items updated successfully", "item" : item}

    return  {"error":"Item not found "}

@app.delete("/items/{item_id}")
def deleteData(item_id : int):
    if item_id in itemsStorage:
        itemsStorage.pop(item_id)
        return {"messgae" : "Item deleted successfully"}
@app.get("/")
def al() :
    return {"Hello" : "Welcome the the api"}