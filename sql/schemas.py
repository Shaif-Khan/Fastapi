from pydantic import BaseModel
from typing import List,Optional


class CreateItem(BaseModel):
    sem:int
    name:str
    course:str
    age:int

class Config():
    orm_mode=True


class User(BaseModel):
    user:str
    email:str
    password:str

class ShowUser(BaseModel):
    user:str
    email:str
    users:List[CreateItem]=[]
    
class Config():
    orm_mode=True

class Show(CreateItem):
    sem:int
    name:str
    course:str
    age:int
    creator:ShowUser
    
    
class Config():
    orm_mode=True

class Login(BaseModel):
    username:str
    password:str


class TokenData(BaseModel):
    email: Optional[str]= None
