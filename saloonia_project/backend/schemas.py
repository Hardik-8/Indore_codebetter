from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from datetime import time
from datetime import datetime
from enum import Enum
from typing import List,Optional

class RoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    branch_manager = "branch_manager"
    employee = "employee"

class UsersBase(BaseModel):
    name:str
    email:str
    phone:str
    password_hash:str
    role:RoleEnum                      
    branch_id: Optional[int] = None
    is_active: bool =True
    created_at: Optional[datetime] = None

class UsersCreate(UsersBase):
    pass

class UsersShow(BaseModel):
    id : int
    name : str
    email: str
    phone : str
    role: RoleEnum
    branch_id : Optional[int] = None
    is_active : bool 
    created_at : Optional[datetime] = None
    class Config:
        orm_mode=True

class BranchBase(BaseModel):
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

class BranchUpdate(BaseModel):
    name : Optional[str] = None
    address : Optional[str] = None
    city : Optional[str] = None
    phone : Optional[str] = None
    is_active : Optional[bool] = None

class BranchResponse(BranchBase):
    id: int
    class Config:
        orm_mode=True

class SalaryTypeEnum(str, Enum):
    fixed = "fixed"
    commission = "commission"
    hybrid = "hybrid"

class EmployeeBase(BaseModel):
    user_id:int
    branch_id:int
    designation:str
    specialization:str
    joining_date:date
    salary_type:SalaryTypeEnum
    base_salary:Decimal
    commission_percent:Optional[Decimal]= None
    shift_start:time
    shift_end:time
    is_active:bool = True

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeShow(EmployeeBase):
    id : int
    class Config:
        orm_mode=True
        
class AttendanceStatusEnum(str, Enum):
    present = "present"
    absent = "absent"
    half_day = "half_day"
    leave = "leave"

class AttendanceBase(BaseModel):
    employee_id : int
    branch_id : int
    date : date
    check_in_time : Optional[datetime] = None
    check_out_time : Optional[datetime] = None
    status : AttendanceStatusEnum

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceShow(AttendanceBase):
    id : int
    class Config:
        orm_mode = True


class GenderEnum(str,Enum):
    male = "male"
    female = "female"
    other = "other"

class MembershipEnum(str,Enum):
    no_membership = "no_membership"
    silver = "silver"
    gold = "gold"
    platinum = "platinum"

class ClientBase(BaseModel):
    branch_id : int
    name: str
    phone: str
    email: Optional[str] = None
    gender : GenderEnum
    dob: Optional[date] = None
    membership_type : Optional[MembershipEnum] = None
    loyalty_points : int =0

class ClientCreate(ClientBase):
    pass 

class ClientShow(ClientBase):
    id : int
    created_at: datetime
    class Config:
        orm_mode = True

class ServicesBase(BaseModel):
    branch_id : int
    name:str
    category:str
    gender:GenderEnum
    duration_minutes:int
    price:Decimal
    is_active : bool = True

class ServicesCreate(ServicesBase):
    pass

class ServicesShow(ServicesBase):
    id: int
    class Config:
        orm_mode=True

class AppointmentStatusEnum(str, Enum):
    scheduled = "scheduled"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"
    no_show = "no_show"

class AppointmentBase(BaseModel):
    branch_id : int
    client_id : int
    employee_id : int
    service_id : int
    appointment_date : date
    start_time : time
    end_time : time
    status : AppointmentStatusEnum

class AppointmentCreate(AppointmentBase):
    pass 

class AppointmentShow(AppointmentBase):
    id : int
    class Config:
        orm_mode = True

class PaymentMethodEnum(str, Enum):
    cash = "cash"
    card = "card"
    upi  = "upi"
 
class ClientVisitHistoryBase(BaseModel):
    client_id         : int
    branch_id         : int
    appointment_id    : Optional[int]     = None
    employee_id       : int
    services_availed  : str
    total_amount_paid : Decimal
    discount_applied  : Decimal           = Decimal("0.00")
    payment_method    : PaymentMethodEnum
    feedback          : Optional[str]     = None
    rating            : Optional[int]     = None          
    visited_at        : Optional[datetime] = None
 
class ClientVisitHistoryCreate(ClientVisitHistoryBase):
    pass
 
class ClientVisitHistoryShow(ClientVisitHistoryBase):
    id: int
    class Config:
        orm_mode = True


class InventoryBase(BaseModel):
    branch_id : int
    item_name : str
    category : str
    quantity : int
    unit : str
    minimum_threshold : int
    price_per_unit : Decimal
    supplier_name : Optional[str] = None
    last_restocked_at : Optional[datetime] = None

class InventoryCreate(InventoryBase):
    pass 
    
class InventoryShow(InventoryBase):
    id: int
    class Config:
        orm_mode = True

class CategoryEnum(str, Enum):
    client_feedback = "client_feedback"
    inventory = "inventory"
    service = "service"
    other = "other"
class SuggestionStatusEnum(str, Enum):
    pending = "pending"
    reviewed = "reviewed"
    done = "done"
class SuggestionBase(BaseModel):
    employee_id: int
    branch_id: int
    title: str
    description: str
    category: CategoryEnum 
    status:  SuggestionStatusEnum = SuggestionStatusEnum.pending
    manager_reply: Optional[str] = None

class SuggestionCreate(SuggestionBase):
    pass



class SuggestionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[CategoryEnum] = None       # ← Enum
    status: Optional[SuggestionStatusEnum] = None # ← Enum
    manager_reply: Optional[str] = None


class SuggestionResponse(SuggestionBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode =  True

class ChatRoleEnum(str, Enum):
    user      = "user"
    assistant = "assistant"
    system    = "system"

class ChatbotSessionBase(BaseModel):
    user_id    : Optional[int] = None
    session_id : str
    role       : ChatRoleEnum         
    message    : str

class ChatbotSessionCreate(ChatbotSessionBase):
    pass

class ChatbotSessionResponse(ChatbotSessionBase):
    id         : int
    created_at : datetime

    class Config:
       orm_mode = True


class SalaryBase(BaseModel):
    employee_id: int
    month: int
    year: int
    base_amount: Decimal
    commission_earned: Decimal = Decimal("0.00")
    deductions: Decimal = Decimal("0.00")
    bonus: Decimal = Decimal("0.00")
    total_amount: Decimal
    paid_at: Optional[datetime] = None
    payment_method: Optional[PaymentMethodEnum] = None

class SalaryCreate(SalaryBase):
    pass

class SalaryUpdate(BaseModel):
    commission_earned: Optional[Decimal] = None
    deductions: Optional[Decimal] = None
    bonus: Optional[Decimal] = None
    total_amount: Optional[Decimal] = None
    paid_at: Optional[datetime] = None
    payment_method: Optional[PaymentMethodEnum] = None

class SalaryResponse(SalaryBase):
    id: int

    class Config:
        orm_mode =  True

