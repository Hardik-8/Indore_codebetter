from database import BASE,engine,get_db
from fastapi import FastAPI,Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sqlalchemy import and_
from jose import jwt, JWTError
# from passlib.context import CryptContext
from datetime import datetime, timedelta, date
from typing import List

from schemas import UsersBase, UsersCreate, UsersShow,BranchBase, BranchCreate, BranchUpdate, BranchResponse
from schemas import EmployeeBase, EmployeeCreate, EmployeeShow,AttendanceBase, AttendanceCreate, AttendanceShow
from schemas import ClientBase, ClientCreate, ClientShow,ServicesBase, ServicesCreate, ServicesShow
from schemas import AppointmentBase, AppointmentCreate, AppointmentShow,ClientVisitHistoryBase, ClientVisitHistoryCreate
from schemas import ClientVisitHistoryShow,InventoryBase, InventoryCreate, InventoryShow,SuggestionBase, SuggestionCreate
from schemas import SuggestionUpdate, SuggestionResponse,ChatbotSessionBase, ChatbotSessionCreate, ChatbotSessionResponse
from schemas import SalaryBase, SalaryCreate, SalaryUpdate, SalaryResponse

from models import Users, Branches, Employees, Attendance, Clients, Services, Appointments, ClientVisitHistory, Inventory
from models import Suggestion, ChatbotSession, SalaryRecord


app=FastAPI()
BASE.metadata.create_all(bind=engine)


# SECRET_KEY = "your_super_secret_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# pwd_context = CryptContext(schemes= ["bcrypt"], deprecated = "auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain: str, hashed: str) -> bool:
#     return pwd_context.verify(plain, hashed)

# def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def decode_token(token: str):
#     try:
#         return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     except JWTError:
#         return None

# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     payload = decode_token(token)
#     if not payload:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#     email = payload.get("sub")
#     user = db.query(Users).filter(Users.email == email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# def require_roles(allowed_roles: list):
#     def role_checker(current_user: Users = Depends(get_current_user)):
#         if current_user.role not in allowed_roles:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail=f"Access denied. Required roles: {allowed_roles}"
#             )
#         return current_user
#     return role_checker


@app.get("/")
def hello():
    return {"message": "Database connection successful"}

# @app.post("/register", response_model=UsersShow, status_code=status.HTTP_201_CREATED)
# def register(payload: UsersCreate, db: Session = Depends(get_db)):
#     if db.query(Users).filter(Users.email == payload.email).first():
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered")
#     new_user = Users(name= payload.name,email= payload.email,phone= payload.phone,password_hash = hash_password(payload.password_hash),role = payload.role,
#                      branch_id= payload.branch_id,is_active= payload.is_active,)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
 
# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(Users).filter(Users.email == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.password_hash):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
#     token = create_access_token(data={"sub": user.email, "role": user.role})
#     return {"access_token": token, "token_type": "bearer"}
 
# @app.get("/profile", response_model=UsersShow)
# def get_profile(current_user: Users = Depends(get_current_user)):
#     return current_user
 
# @app.get("/logout")
# def logout():
#     return {"message": "Remove the token from the client to logout."}

# @app.post("/attendance/", response_model=AttendanceShow, status_code=status.HTTP_201_CREATED)
# def mark_attendance(payload : AttendanceCreate,db : Session = Depends(get_db),current_user : Users = Depends(require_roles(["admin", "manager", "branch_manager"]))):
#     employee = db.query(Employees).filter(Employees.id == payload.employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
#     branch = db.query(Branches).filter(Branches.id == payload.branch_id).first()
#     if not branch:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Branch not found")
#     existing = db.query(Attendance).filter(
#         and_(Attendance.employee_id == payload.employee_id,Attendance.date == payload.date)).first()                                             
#     if existing:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Attendance already marked for employee {payload.employee_id} on {payload.date}") 
#     new_record = Attendance(**payload.dict())
#     db.add(new_record)
#     db.commit()
#     db.refresh(new_record)
#     return new_record
 
# @app.get("/attendance/", response_model=List[AttendanceShow])  
# def get_all_attendance(branch_id: int  = None,employee_id : int  = None,date_filter : date = None,db : Session = Depends(get_db),current_user: Users   = Depends(get_current_user)):
#     query = db.query(Attendance)
#     if branch_id:
#         query = query.filter(Attendance.branch_id == branch_id)
#     if employee_id:
#         query = query.filter(Attendance.employee_id == employee_id)
#     if date_filter:
#         query = query.filter(Attendance.date == date_filter)
#     records = query.all()
#     if not records:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attendance records found")
#     return records                                              

# @app.get("/attendance/employee/{employee_id}", response_model=List[AttendanceShow])
# def get_employee_attendance(employee_id  : int,db : Session = Depends(get_db),current_user : Users = Depends(get_current_user)):
#     employee = db.query(Employees).filter(Employees.id == employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
#     records = db.query(Attendance).filter(Attendance.employee_id == employee_id).all()
#     if not records:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No attendance records found for employee")
#     return records

# @app.get("/attendance/branch/{branch_id}/date/{attendance_date}", response_model=List[AttendanceShow])
# def get_branch_attendance_by_date(branch_id : int,attendance_date : date,db : Session = Depends(get_db),current_user : Users   = Depends(require_roles(["admin", "manager", "branch_manager"]))):
#     branch = db.query(Branches).filter(Branches.id == branch_id).first()
#     if not branch:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Branch not found")
#     records = db.query(Attendance).filter(and_(Attendance.branch_id == branch_id,Attendance.date == attendance_date)).all()
#     if not records:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No attendance found for branch for this date")
#     return records

# @app.get("/attendance/{attendance_id}", response_model=AttendanceShow)  
# def get_attendance(attendance_id : int,db: Session = Depends(get_db),current_user : Users = Depends(get_current_user)):
#     record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
#     if not record:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance record not found")
#     return record

# @app.put("/attendance/{attendance_id}", response_model=AttendanceShow)  
# def update_attendance(attendance_id : int,payload: AttendanceCreate,db: Session = Depends(get_db),current_user : Users = Depends(require_roles(["admin", "manager", "branch_manager"]))):
#     record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
#     if not record:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance record not found")
#     for field, value in payload.dict(exclude_unset=True).items():
#         setattr(record, field, value)
#     db.commit()
#     db.refresh(record)
#     return record
 
# @app.delete("/attendance/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT) 
# def delete_attendance(attendance_id : int,db : Session = Depends(get_db),current_user : Users= Depends(require_roles(["admin"]))):
#     record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
#     if not record:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance record not found")
#     db.delete(record)
#     db.commit()
#     return None
 