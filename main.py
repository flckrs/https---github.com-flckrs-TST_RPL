from os import stat
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app = FastAPI()

class Supply(BaseModel):
  id_supply: int
  nama_produk: str
  jumlah: int
  deskripsi: str
  jenis: str
  status: bool

  class Config:
    orm_mode=True

db = SessionLocal()

@app.get('/')
def index(): 
  return {"Welcome":"Hello :p"}

# Read All Products
@app.get('/supply', response_model=List[Supply], status_code=200)
def get_all_products():
  supply=db.query(models.Supply).all()

  return supply

# Read One Product
@app.get('/supply/{product_id}',response_model=Supply,status_code=status.HTTP_200_OK)
def get_a_product(product_id:int):
    supply=db.query(models.Supply).filter(models.Supply.id_supply==product_id).first()
    if supply is not None:
      return supply
    raise HTTPException(status_code=404, detail="Product Not Found")

# Add New Product
@app.post('/supply',response_model=Supply, status_code=status.HTTP_201_CREATED)
def add_new_product(supply:Supply):
    db_supply=db.query(models.Supply).filter(models.Supply.id_supply==supply.id_supply).first()

    if db_supply is not None:
        raise HTTPException(status_code=400,detail="Product already exists")

    new_supply=models.Supply(
        id_supply=supply.id_supply,
        nama_produk=supply.nama_produk,
        jumlah=supply.jumlah,
        deskripsi=supply.deskripsi,
        jenis=supply.jenis,
        status=supply.status
    )

    db.add(new_supply)
    db.commit()

    return new_supply

# Update A Product
@app.put('/supply/{supply_id}',response_model=Supply,status_code=status.HTTP_200_OK)
def update_a_product(supply_id:int,supply:Supply):

    product_to_update=db.query(models.Supply).filter(models.Supply.id_supply==supply.id_supply).first()

    product_to_update.nama_produk=supply.nama_produk
    product_to_update.jumlah=supply.jumlah
    product_to_update.deskripsi=supply.deskripsi
    product_to_update.jenis=supply.jenis
    product_to_update.status=supply.status

    db.commit()

    return product_to_update

# Delete One Product
@app.delete('/supply/{supply_id}')
def delete_product(supply_id:int):
    product_to_delete=db.query(models.Supply).filter(models.Supply.id_supply==supply_id).first()

    if product_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product Not Found")
    
    db.delete(product_to_delete)
    db.commit()

    return ("Produk " + product_to_delete.nama_produk +" sudah terhapus dari database")