
from sqlalchemy import Column,Integer,String
from database import BASE,engine
class Employee(BASE):
    __tablename__="employees"
    empid=Column(Integer,primary_key=True,index=False)
    name=Column(String(30),nullable=False)
    age=Column(Integer,nullable=False)
    salary=Column(Integer,nullable=False)
    city=Column(String(30),nullable=False)