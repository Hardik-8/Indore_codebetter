from sqlalchemy import Column,Integer,String,ForeignKey
from database import BASE

class User(BASE):
    __tablename__ = "users"
    id=Column(Integer,primary_key=True,index=False)
    username=Column(String(20),unique=True,index=False)
    password=Column(String(100))

class Token(BASE):
    __tablename__ = "tokens"
    id=Column(Integer,primary_key=True,index=False)
    token=Column(String(100),unique=True,index=False)
    user_id=Column(Integer,ForeignKey("users.id"))
    