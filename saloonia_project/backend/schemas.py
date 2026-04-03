from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from datetime import time
from datetime import datetime
from enum import Enum
from typing import List,Optional
# from sqlalchemy import Column,Integer,String,Date,DateTime,Time,DECIMAL
class Employees(BaseModel):
    id:int
    user_id:int
    branch_id:int
    designation:str
    specialization:str
    joining_date:date
    salary_type:Enum
    base_salary:Decimal
    commission_percent:Decimal
    shift_start:time
    shift_end:time
    is_active:bool

class Employee_Show(Employees):
    pass
    class config:
        orm_mode=True
        
class Employee_create(Employees):
    pass
    class config:
        orm_mode=True

class BranchBase(BaseModel):
    id:int
    name              : str
    address           : str
    city              : str
    phone             : str
    branch_manager_id : Optional[int] = None
    opening_time      : time
    closing_time      : time
    is_active         : bool = True

class BranchCreate(BranchBase):
    pass
    class config:
        orm_mode=True

class BranchUpdate(BaseModel):
    pass
    class config:
        orm_mode=True

class BranchResponse(BranchBase):
    id: int
    class config:
        orm_mode=True








class users_PD(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    password_hash:str
    role = Enum
    branch_id = Optional[int] = None
    is_active = bool
    created_at = datetime

class users_Show(users_PD):
    pass
    class Config:
        orm_mode=True

class users_Create(users_PD):
    pass
    class Config:
        orm_mode=True 

class services_PD(BaseModel):
    id:int
    branch_id = int
    name:str
    category:str
    gender:Enum
    duration_minutes:int
    price:Decimal
    is_active = bool

class services_Show(services_PD):
    pass
    class Config:
        orm_mode=True

class services_Create(services_PD):
    pass
    class Config:
        orm_mode=True