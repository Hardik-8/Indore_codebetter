
from sqlalchemy import Column,Integer,String,Date,DateTime,Time,DECIMAL
from database import BASE,engine
class Employee(BASE):
    __tablename__="employees"
    empid=Column(Integer,primary_key=True,index=False)
    name=Column(String(30),nullable=False)
    age=Column(Integer,nullable=False)
    salary=Column(Integer,nullable=False)
    city=Column(String(30),nullable=False)

class Student(BASE):
    __tablename__="student"
    roll_no=Column(Integer,primary_key=True,index=False)
    name=Column(String(30),nullable=False)
    course=Column(String(30),nullable=False)
    fees=Column(Integer,nullable=False)

class Category(BASE):
    __tablename__="category"
    cat_id=Column(Integer,primary_key=True,index=False)
    cat_name=Column(String(30),nullable=False)

class Product(BASE):
    __tablename__="product"
    pd_id=Column(Integer,primary_key=True,index=False)
    pd_name=Column(String(30),nullable=False)
    pd_price=Column(Integer,nullable=False)