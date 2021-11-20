from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text

class Supply(Base):
  __tablename__='supply'
  id_supply= Column(Integer, nullable= False, primary_key= True)
  nama_produk= Column(String(255), nullable= False)
  jumlah= Column(Integer, nullable= False)
  deskripsi= Column(Text)
  jenis= Column(String(255), nullable=False)
  status=Column(Boolean, default=False)

  def __repr__(self):
    return f"<Supply ID= {self.id_supply} Supply name={self.nama_produk}>"