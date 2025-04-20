from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from .. import models,schemas


def get_all(db:Session):
    users=db.query(models.Blog).all()
    return users

def create(request:schemas.CreateItem,db:Session):
    new_blog=models.Blog(age=request.age,course=request.course,sem=request.sem,name=request.name,client_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    users=db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not users:
        return f"Data with id {id} is not available"
    else:
        return f"Data with id {id} is deleted successfully" 

def update(id:int,request:schemas.CreateItem,db:Session ):
    users=db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    db.commit()
    if not users:
        return {'Detail':f'The Data of Id {id} is Not Available'}
    else:
        return {'message':f'The Data of Id {id} is Updated Successfully. '}
    
def show(id:int,db:Session):
    users=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Blog With id {id} is Not Availablle")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {"Detail": f"The Blog With id {id} is Not Available"}

    return users
