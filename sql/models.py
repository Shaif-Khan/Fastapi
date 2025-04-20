from sqlalchemy import Column,Integer,String,ForeignKey
from . database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    age=Column(Integer,index=True)
    course=Column(String(255),index=True)
    sem=Column(Integer,index=True)
    name=Column(String(255),index=True)
    client_id=Column(Integer,ForeignKey('client.id'))

    creator=relationship("Client",back_populates="users")

class Client(Base):
    __tablename__ = "client"
    id=Column(Integer,primary_key=True,index=True)
    user=Column(String(255),index=True)
    email=Column(String(255),index=True)
    password=Column(String(255),index=True)

    users=relationship("Blog",back_populates="creator")