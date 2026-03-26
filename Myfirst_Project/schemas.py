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
