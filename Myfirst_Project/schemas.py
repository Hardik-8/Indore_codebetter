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

class Category_PD(BaseModel):
    cat_id:int
    cat_name:str
   
class Category_Show(Category_PD):
    pass
    class config:
        orm_mode=True
        
class Category_Create(Category_PD):
    pass
    class config:
        orm_mode=True 


class Product_PD(BaseModel):
    pd_id:int
    pd_name:str
    pd_price:int
   
class Product_Show(Product_PD):
    pass
    class config:
        orm_mode=True
        
class Product_Create(Product_PD):
    pass
    class config:
        orm_mode=True 
