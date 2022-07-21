from fastapi import FastAPI, Path, Query
import uvicorn
from file2 import *

app = FastAPI()

'''@app.get('/')
def index():
    return {"hey": "Hello Arun"}


@app.get('/item{arun}')
def home(arun:int):
    return {'id': arun, 'cars': ['Swift', 'Bmw']}


uvicorn.run(app)'''


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, desccription="The Id of the yu would like to add.", gt=0)):
    return inventory[item_id]


@app.get("/get-by-name")
def get_by_name(name: str = Query(None, title="Name", description="Name of the item")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}

    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID already exists."}

    if item.name is not None:
        inventory[item_id].name = item.name

    if item.price is not None:
        inventory[item_id].price = item.price

    if item.brand is not None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The Item ID is deleted")):
    if item_id not in inventory:
        return {"Error": "Item ID already exists."}

    del inventory[item_id]
