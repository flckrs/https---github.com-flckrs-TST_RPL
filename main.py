from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()

# Login (Login tinggal ambil)
# Post Data Supply (Post)
# Delete Data Supply (Delete)
# Edit Data Supply (Put)
# Read Data Supply (Get One/All)

class Item(BaseModel):
  id: int
  name: str
  description:str
  price: int
  on_offer: bool
  
  class Config:       #serialize sql algorithm to json
    orm_mod=True

db = SessionLocal()

@app.get('/')
def index(): 
  return {"Welcome":"Hello :p"}

@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
  items=db.query(models.Item).all()

  return items

@app.get('/item/{item_id}')
def get_an_item(item_id: int):
  return 0

@app.post('/items')
def create_an_item():
  return 0

@app.put ('/item/item_id}')
def update_an_item(item_id:int):
  return 0

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
  return 0