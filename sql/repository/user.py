from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status
#from .. hashing import Hash
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")




def create(request:schemas.User,db:Session):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user=models.Client(user=request.user,email=request.email,password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    show_user=db.query(models.Client).filter(models.Client.id == id).first()
    if not show_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Client With id {id} is Not Availablle")
    return show_user