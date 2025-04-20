from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,oauth2
from sqlalchemy.orm import Session
from typing import List
from .. repository import blog


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/",response_model=List[schemas.Show])

def get_data(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    

@router.post("/",status_code=status.HTTP_201_CREATED)

def create_post(request:schemas.CreateItem,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete("/{id}")

def delete_data(id:int,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)


@router.put("/{id}")

def update_data(id:int,request:schemas.CreateItem,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get("/{id}",status_code=200,response_model=schemas.Show)

def get_request(id,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)