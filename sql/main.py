from fastapi import FastAPI
from .database import engine
from passlib.context import CryptContext
from . import models
from .router import blog,user,authentication

models.Base.metadata.create_all(bind=engine)

app=FastAPI()
pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


