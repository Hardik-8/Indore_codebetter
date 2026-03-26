#25 march 26 aman sir
#pydantic model

from fastapi import FastAPI, HTTPException
from typing import List                               #used for static database or temporary database
from pydantic import BaseModel                        #first clss is made using basemodel or first class will inherit basemodel

class Student(BaseModel):
    roll_no: int
    name: str
    course: str
    fee: int                                           # float can also be used 

app=FastAPI()    
student_db: List[Student]=[]
                                                         #app is commonly used # an obj is created
@app.get("/student_list", response_model=List[Student])  #for multiple mmodel we use response to return and for multiple we use List[student]                             
def student_list_api():                                  #@ is used as decorator
    return student_db
                                                         # put--   fully update; to change an object
                                                         # patch-- partial updation
@app.post("/student_create", response_model=Student)
def student_create_list(st_data:Student):
    for st in student_db:
        if st.roll_no==st_data.roll_no:
            raise HTTPException(status_code=400,detail=("Roll no already exists"))        #raise is used to return error through exception
    student_db.append(st_data)
    print(student_db)
    return st_data

@app.get("/student_sp/{roll_no}",response_model=Student)
def student_single_record(roll_no:int):
    for st in student_db:
        if st.roll_no==roll_no:
            return st
    raise HTTPException(status_code=404, detail=("record not found"))

@app.delete("/student_delete/{roll_no}", response_model=Student)
def student_delete_record(roll_no:int,st_data:Student):
    for st in student_db:
        if st.roll_no==st_data.roll_no:
            student_db.remove(st_data)
            return st_data
    raise HTTPException(status_code=404, detail=("Record not found"))