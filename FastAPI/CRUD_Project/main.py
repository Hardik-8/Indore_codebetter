from fastapi import FastAPI,HTTPException
from typing import List 
from pydantic import BaseModel


class Student(BaseModel):
    roll_no:int
    name:str
    course:str
    fee:float

app=FastAPI()

student_db:List[Student]=[]
@app.get("/student_list",response_model=list[Student])
def student_list_api():
    return student_db 


@app.post("/student_create",response_model=Student)
def student_create_list(st_Data:Student):
        for i in student_db:
            if i.roll_no==st_Data.roll_no:
                raise HTTPException(status_code=400,detail=("roll number already exist"))
            
        student_db.append(st_Data)
        return st_Data

@app.get("/student/{roll_no}",response_model=Student)
def student_getid(roll_no:int):
    for i in student_db:
        if i.roll_no==roll_no:
            return i
            # break
        # else : 
    raise HTTPException(status_code=404,detail=("roll no not exist"))

@app.delete("/student_delete/{roll_no}", response_model=Student)
def student_delete_record(roll_no:int,st_data:Student):
    for st in student_db:
        if st.roll_no==st_data.roll_no:
            student_db.remove(st_data)
            return st_data
    raise HTTPException(status_code=404, detail=("Record not found"))
