from pydantic import BaseModel

class Employee_PD(BaseModel):
    empid:int
    name:str
    age:int
    salary:int
    city:str

class Employee_Show(Employee_PD):
    pass
    class config:
        orm_mode=True
        
class Employee_create(Employee_PD):
    pass
    class config:
        orm_mode=True

class Student_PD(BaseModel):
    roll_no:int
    name:str
    course:str
    fees:int
     

class Student_Show(Student_PD):
    pass
    class config:
        orm_mode=True
        
class Student_create(Student_PD):
    pass
    class config:
        orm_mode=True 

