#main.py
from database import BASE,engine,Session,get_db
from fastapi import FastAPI,Depends,HTTPException
from schemas import Employee_create,Employee_Show
from typing import List
from model import Employee
app=FastAPI()
BASE.metadata.create_all(bind=engine)

@app.get("/")
def hello():
    return {"hello ":"database connection succesfull"}

@app.get("/emp_show",response_model=List[Employee_Show])
def employee_show(db:Session=Depends(get_db)):
    rec=db.query(Employee).all()
    return rec 