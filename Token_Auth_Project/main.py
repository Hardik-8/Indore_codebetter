from database import BASE,engine,Session,get_db
from fastapi import FastAPI,Depends,HTTPException,Header
from schemas import LoginUser,RegisterUser,CreateResponse
# from typing import List
from model import User,Token
# from utils import uuid
import model , schemas , utils

app=FastAPI()
BASE.metadata.create_all(bind=engine)

@app.get("/")
def hello():
    return {"hello ":"database connection succesfull"}

@app.post("/register",response_model=schemas.CreateResponse)
def register(user:schemas.RegisterUser,db:Session= Depends(get_db)):
    existing=db.query(User).filter_by(username=user.username).first()
    if existing :
        raise HTTPException(status_code=404,detail="username already there")
    new_user = User(username=user.username,password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(user:LoginUser,db:Session=Depends(get_db)):
    db_user=db.query(User).filter_by(username=user.username,password=user.password).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="invalid")
    token=utils.generate_token()
    db_token=Token(token=token,user_id=db_user.id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return {'token':token}

@app.post("/logout")
def logout(authorization:str = Header(...),db:Session=Depends(get_db)):
    token = authorization.replace("Token ","")
    db_token = db.query(model.Token).filter_by(token=token).first()
    if not db_token:
        raise HTTPException(status_code=404,detail="invalid token")
    db.delete(db_token)
    db.commit()
    return {'message': 'logged out sccessfuall'}

@app.get("/profile")
def profile(authorization:str=Header(...),db:Session=Depends(get_db)):
    token = authorization.replace("Token ","")
    db_token = db.query(Token).filter_by(token=token).first()
    if not db_token:
        raise HTTPException(status_code=404,detail="invalid token")
    user = db.query(User).filter_by(id=db_token.user_id).first()
    return {'username': user.username , 'id': user.id, 'message' : 'welcome'}
