from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Login
# Post Data Supply
# Delete Data Supply
# Edit Data Supply
# Read Data Supply

class Item(BaseModel):
  id: int
  name: str
  description:str
  price: int
  on_offer: bool

@app.get('/')
def index(): 
  return {"Welcome"}

@app.put('/item/{item_id}')
def update_item(item_id:int, item:Item):
  return {'name': item.name,
          'desciption': item.description,
          'price': item.price,
          'on_offer': item.on_offer
          }


@app.post('item/{item_id}')
def add_item():
  return 0
