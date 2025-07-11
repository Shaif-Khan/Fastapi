from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. hashing import Hash

router=APIRouter(
    tags=["Authentication"]
)



def verify(hashed_password,plain_password):
    return pwd_cxt.verify(plain_password,hashed_password)

@router.post("/login")

def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.Client).filter(models.Client.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Invalid Credentials !")
    
    if not Hash.verify(user.password,request.password):
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Incorrect Password !")
    
    access_token = token.create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}
