from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   
   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)
   
   def __init__(self, name, address, email):
       self.name = name
       self.address = address
       self.email = email