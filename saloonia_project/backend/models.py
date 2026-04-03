
from sqlalchemy import Column,Integer,String,ForeignKey,VARCHAR,BOOLEAN,Boolean,Text
from database import BASE,engine
from datetime import date
from decimal import Decimal
from datetime import time
from datetime import datetime
from enum import Enum
from sqlalchemy.orm import relationship

from sqlalchemy import Column,Integer,Text,VARCHAR,Enum,ForeignKey,Boolean,DateTime,DECIMAL
from database import BASE
from datetime import datetime


class users(BASE):
    tablename="users"

    id = Column(Integer,primary_key=True,index=False)
    name = Column(VARCHAR(50),nullable=False)
    email = Column(VARCHAR(80),unique=True,nullable=False)
    phone = Column(VARCHAR(14),nullable=False)
    password_hash = Column(Text,nullable=False)
    role = Column(Enum("admin","manager","branch_manager","employee"),nullable=False)
    branch_id = Column(Integer,ForeignKey("branches.id"), nullable=True)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.utcnow)


class branches(BASE):
    tablename = "branches"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String(100), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    branch_manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    opening_time = Column(time, nullable=False)
    closing_time = Column(time, nullable=False)
    is_active = Column(Boolean, default=True)

    branch_manager = relationship("User", back_populates="managed_branches")
    
class employees(BASE):
    __tablename__="employees"
    id=Column(Integer,primary_key=True,index=False,unique=True)
    user_id=Column(Integer,ForeignKey(users.id),nullable=False)
    branch_id=Column(Integer,ForeignKey(branches.id),nullable=False)
    designation=Column(VARCHAR(100),nullable=False)
    specialization=Column(VARCHAR(100),nullable=False)
    joining_date=Column(date,nullable=False)
    salary_type=Column(Enum('fixed' , 'commission' , 'hybrid'),nullable=False)
    base_salary=Column(Decimal(10,2),nullable=False)
    commission_percent=Column(Decimal(5,2),nullable=True)
    shift_start=Column(time,nullable=False)
    shift_end=Column(time,nullable=False)
    is_active=Column(Boolean,nullable=False,default=True)

class attendance(BASE):
    tablename="attendance"
    id = Column(Integer, primary_key=True,index=True, autoincrement=True )
    employee_id= Column(Integer, ForeignKey("employees.id"), nullable=False )
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    date = Column(datetime, nullable=False)
    check_in_time= Column(datetime, nullable=True)
    check_out_time= Column(datetime, nullable=True)
    status=Column(Enum("present", " absent", "half_day", "leave"), nullable=False)

    employee = relationship("Employee", back_populates="attendances")
    branch= relationship("Branch", back_populates="attendances")

class services(BASE):
    tablename="services"

    id = Column(Integer,primary_key=True,index=False)
    branch_id = Column(Integer,ForeignKey("branches.id"), nullable=False)
    name = Column(VARCHAR(50),nullable=False)
    category = Column(VARCHAR(100),nullable=False)
    gender = Column(Enum("male","female","unisex"),nullable=False)
    duration_minutes = Column(Integer,nullable=False)
    price = Column(DECIMAL(10,2),nullable=False)
    is_active = Column(Boolean,default=True)



























class Appointments(BASE):
    tablename= "appointments"
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    appointment_date= Column(date, nullable=False)
    start_time= Column(time, nullable=False)
    end_time= Column(time, nullable=False)
    status= Column(Enum("scheduled","in_progress","completed","cancelled","no_show"), nullable=False)
    notes= Column(String(50), nullable=True)




#model.py
from unicodedata import category
from datetime import Date
from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from database import BASE





#schemas
from typing import List,Optional
from pydantic import BaseModel
import enum
class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class MembershipEnum(enum.Enum):
    none = "none"
    silver = "silver"
    gold = "gold"
    platinum = "platinum"