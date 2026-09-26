from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base


BASE = declarative_base() 

class Product(BASE):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String)
    qty = Column(Integer)
