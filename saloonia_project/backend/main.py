from database import BASE,engine,Session,get_db
from fastapi import FastAPI,Depends,HTTPException
from schemas import UsersBase, UsersCreate, UsersShow,BranchBase, BranchCreate, BranchUpdate, BranchResponse,EmployeeBase, EmployeeCreate, EmployeeShow,AttendanceBase, AttendanceCreate, AttendanceShow,ClientBase, ClientCreate, ClientShow,ServicesBase, ServicesCreate, ServicesShow,AppointmentBase, AppointmentCreate, AppointmentShow,ClientVisitHistoryBase, ClientVisitHistoryCreate, ClientVisitHistoryShow,InventoryBase, InventoryCreate, InventoryShow,SuggestionBase, SuggestionCreate, SuggestionUpdate, SuggestionResponse,ChatbotSessionBase, ChatbotSessionCreate, ChatbotSessionResponse,SalaryBase, SalaryCreate, SalaryUpdate, SalaryResponse
from typing import List
from models import Users, Branches, Employees, Attendance, Clients, Services, Appointments, ClientVisitHistory, Inventory, Suggestion, ChatbotSession, SalaryRecord
app=FastAPI()
BASE.metadata.create_all(bind=engine)

@app.get("/")
def hello():
    return {"hello ":"database connection succesfull"}