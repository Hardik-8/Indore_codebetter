from sqlalchemy import Column,Integer,String,ForeignKey,VARCHAR,Boolean,Text,Numeric,Date,Enum,DateTime, Time, func 
from database import BASE,engine
from datetime import datetime
from sqlalchemy.orm import relationship
from datetime import timezone
default=lambda: datetime.now(timezone.utc)


class Users(BASE):
    __tablename__="users" 

    id = Column(Integer,primary_key=True,index=True, autoincrement=True)
    name = Column(VARCHAR(50),nullable=False)
    email = Column(VARCHAR(80),unique=True,nullable=False)
    phone = Column(VARCHAR(14),nullable=False)
    password_hash = Column(Text,nullable=False)
    role = Column(Enum("admin","manager","branch_manager","employee"),nullable=False)
    branch_id = Column(Integer,ForeignKey("branches.id"), nullable=True)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.utcnow)

    branch = relationship("Branches", back_populates="users")
    chatbot_sessions = relationship("ChatbotSession", back_populates="user")
    managed_branches = relationship("Branches", back_populates="branch_manager", foreign_keys="[Branches.branch_manager_id]")
    employee = relationship("Employees", back_populates="user")


class Branches(BASE): 
    __tablename__ = "branches"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String(100), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    branch_manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)
    is_active = Column(Boolean, default=True)


    inventory    = relationship("Inventory", back_populates="branch")
    attendances  = relationship("Attendance", back_populates="branch")
    branch_manager = relationship("Users", back_populates="managed_branches")
    users = relationship("Users", back_populates="branch", foreign_keys="[Users.branch_id]")
    employees = relationship("Employees", back_populates="branch")
    clients = relationship("Clients", back_populates="branch")
    services = relationship("Services", back_populates="branch")
    appointments = relationship("Appointments", back_populates="branch")
    suggestions= relationship("Suggestion", back_populates="branch")
    
class Employees(BASE):
    __tablename__="employees"
    id=Column(Integer,primary_key=True,index=True,unique=True, autoincrement=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    branch_id=Column(Integer,ForeignKey("branches.id"),nullable=False)
    designation=Column(VARCHAR(100),nullable=False)
    specialization=Column(VARCHAR(100),nullable=False)
    joining_date=Column(Date,nullable=False)
    salary_type=Column(Enum('fixed' , 'commission' , 'hybrid'),nullable=False)
    base_salary=Column(Numeric(10,2),nullable=False)
    commission_percent=Column(Numeric(5,2),nullable=True)
    shift_start=Column(Time,nullable=False)
    shift_end=Column(Time,nullable=False)
    is_active=Column(Boolean,nullable=False,default=True)

    attendances  = relationship("Attendance", back_populates="employee")
    appointments = relationship("Appointments", back_populates="employee")
    user = relationship("Users", back_populates="employee")
    branch = relationship("Branches", back_populates="employees")
    suggestions= relationship("Suggestion", back_populates="employee")
    salary_records = relationship("SalaryRecord", back_populates="employee")


class Attendance(BASE):
    __tablename__="attendance"
    id = Column(Integer, primary_key=True,index=True, autoincrement=True )
    employee_id= Column(Integer, ForeignKey("employees.id"), nullable=False )
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    date = Column(Date, nullable=False)
    check_in_time= Column(DateTime, nullable=True)
    check_out_time= Column(DateTime, nullable=True)
    status=Column(Enum("present", "absent", "half_day", "leave"), nullable=False)

    employee = relationship("Employees", back_populates="attendances")
    branch = relationship("Branches", back_populates="attendances")

#clients 
class Clients(BASE):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    name = Column(VARCHAR(100), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    email = Column(VARCHAR(100), nullable=True)
    gender = Column(Enum("male", "female", "other"), nullable=False)
    dob = Column(Date, nullable=True)
    membership_type = Column(Enum("no_membership", "silver", "gold", "platinum"), nullable=False, default="no_membership")
    loyalty_points = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationship
    appointments = relationship("Appointments", back_populates="client")
    branch = relationship("Branches", back_populates="clients")
    visit_history = relationship("ClientVisitHistory", foreign_keys="[ClientVisitHistory.client_id]")

class Services(BASE):
    __tablename__="services"

    id = Column(Integer,primary_key=True,index=True, autoincrement=True)
    branch_id = Column(Integer,ForeignKey("branches.id"), nullable=False)
    name = Column(VARCHAR(50),nullable=False)
    category = Column(VARCHAR(100),nullable=False)
    gender = Column(Enum("male","female","other"),nullable=False)
    duration_minutes = Column(Integer,nullable=False)
    price = Column(Numeric(10,2),nullable=False)
    is_active = Column(Boolean,default=True)

    appointments = relationship("Appointments", back_populates="service")
    branch = relationship("Branches", back_populates="services")        # Branch se connected
    

class Appointments(BASE):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    appointment_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(Enum("scheduled", "in_progress", "completed", "cancelled", "no_show"), nullable=False)
    notes = Column(String(50), nullable=True)

    # Relationships
    branch = relationship("Branches", back_populates="appointments")
    client = relationship("Clients", back_populates="appointments")
    employee = relationship("Employees", back_populates="appointments")
    service = relationship("Services", back_populates="appointments")

class ClientVisitHistory(BASE):
    __tablename__ = "client_visit_history"
 
    id                 = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    branch_id          = Column(Integer, ForeignKey("branches.id"), nullable=False)
    appointment_id     = Column (Integer,ForeignKey("appointments.id"), nullable=True)        
    employee_id        = Column (Integer,ForeignKey("employees.id"), nullable=False)        
    services_availed   = Column(Text, nullable=False)            # e.g. "Haircut, Facial"
    total_amount_paid  = Column(Numeric(10, 2), nullable=False)
    discount_applied   = Column(Numeric(10, 2), nullable=False, default=0.00)
    payment_method     = Column(Enum("card", "cash" ,"upi"), nullable=False)
    feedback           = Column(Text, nullable=True)
    rating             = Column(Integer, nullable=True)          # 1–5 stars
    visited_at         = Column(DateTime, nullable=False, default=datetime.utcnow)
 
    # Relationships
    client = relationship("Clients", foreign_keys=[client_id], back_populates="visit_history")
    branch = relationship("Branches", foreign_keys=[branch_id])
    appointment = relationship("Appointments", foreign_keys=[appointment_id])
    employee = relationship("Employees", foreign_keys=[employee_id])


class Inventory(BASE):
    __tablename__= "inventory"
    id= Column(Integer, primary_key=True, index=True)
    branch_id= Column(Integer, ForeignKey("branches.id"), nullable=False)
    item_name= Column(VARCHAR(100),nullable=False)
    category= Column(VARCHAR(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit = Column(VARCHAR(30), nullable=False)
    minimum_threshold = Column(Integer, nullable=False)
    price_per_unit= Column(Numeric(10,2), nullable=False)
    supplier_name= Column(VARCHAR(100),nullable=True)
    last_restocked_at= Column(DateTime, nullable=True)

    branch= relationship("Branches", back_populates="inventory")


class Suggestion(BASE):
    __tablename__ = "suggestions"
    id=Column(Integer, primary_key=True,index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"),nullable=False)
    branch_id=Column(Integer, ForeignKey("branches.id"),nullable=False)
    title=Column(String(100), nullable=False)
    description=Column(Text, nullable=False)
    category=Column(Enum("client_feedback","inventory","service","other"), nullable=False)
    status=Column(Enum("pending","reviewed","done"), nullable=False,default="pending")
    manager_reply=Column(Text,nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.utcnow)

    employee = relationship("Employees",back_populates="suggestions")
    branch = relationship("Branches",back_populates="suggestions")


class ChatbotSession(BASE):
    __tablename__ = "chatbot_sessions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    session_id = Column(String(100), nullable=False)
    role = Column(Enum("user", "assistant", "system"), nullable=False)  
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("Users",back_populates="chatbot_sessions")


class SalaryRecord(BASE):
    __tablename__ = "salary_records"
    id=Column(Integer, primary_key=True,index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"),nullable=False)
    month=Column(Integer,nullable=False)
    year=Column(Integer, nullable=False)
    base_amount=Column(Numeric(10,2), nullable=False)
    commission_earned=Column(Numeric(10,2), nullable=False,default= 0.00)
    deductions=Column(Numeric(10,2), nullable=False,default= 0.00)
    bonus=Column(Numeric(10,2),nullable=False,default= 0.00)
    total_amount=Column(Numeric(10,2),nullable=False)
    paid_at=Column(DateTime,nullable=True)
    payment_method=Column(Enum("cash","card","upi"),nullable=True)


    employee = relationship("Employees",back_populates="salary_records")